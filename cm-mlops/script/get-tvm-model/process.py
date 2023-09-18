import os
import tempfile
from typing import Dict, Tuple, Optional, List, Any, Union

if os.environ.get("CM_TVM_FRONTEND_FRAMEWORK", None) == "pytorch":
    import torch
    import torchvision
    
import tvm
from tvm import relay, meta_schedule
from tvm.driver.tvmc.frontends import load_model

def get_shape_dict_from_onnx(
    shape: List[int],
    model_path: str
) -> Dict[str, List[int]]:
    import onnx
    onnx_model = onnx.load(model_path)
    if len(shape) == 1:
        for _input in onnx_model.graph.input:
            tensor_type = _input.type.tensor_type
            if (tensor_type.HasField("shape")):
                for dimension in tensor_type.shape.dim:
                    if dimension.dim_value != 0:
                        shape.append(dimension.dim_value)
    input_all = [node.name for node in onnx_model.graph.input]
    input_initializer =  [node.name for node in onnx_model.graph.initializer]
    net_feed_input = list(set(input_all)  - set(input_initializer))
    return {input_name: shape for input_name in net_feed_input}

def get_mod_params(
    model_path: str,
    model_name: str,
    batch_size: int,
    frontend: str,
    input_shapes_str: Optional[str] = None,
    input_layer_name: Optional[str] = None,
    num_channels: Optional[int] = None,
    image_width: Optional[int] = None,
    image_height: Optional[int] = None,
    max_seq_length: Optional[int] = None
) -> Tuple[tvm.IRModule, Dict[str, tvm.nd.NDArray]]:
    if not input_shapes_str and (not image_width or not image_height) and not max_seq_length and frontend != "onnx":
        raise RuntimeError(
            "Error: None of environment variables storing shape is set!"
        )
    if input_shapes_str:
        shape_dict = eval('{' + input_shapes_str.replace('BATCH_SIZE', str(batch_size)) + '}')
    else:
        shape = []
        if image_width and image_height:
            shape = [batch_size, num_channels, image_height, image_width]
        elif max_seq_length:
            shape = [batch_size, max_seq_length]
        if frontend == "onnx":
            shape_dict = get_shape_dict_from_onnx(shape if len(shape) > 0 else [batch_size], model_path)
        else:
            raise RuntimeError(
                "Error: Cannot find proper shapes in environment variables"
            )
    print(f"Shape dict {shape_dict}")
    if frontend == "pytorch":
        torch_model = getattr(torchvision.models, model_name)(weights=None)
        torch_model.load_state_dict(torch.load(model_path))
        torch_model.fc = torch.nn.Sequential(
            torch_model.fc,
            torch.nn.Softmax(dim=1)
        )
        torch_model = torch_model.eval()
        shape_list = list(shape_dict.items())
        input_data = torch.randn(shape_list[0][1])
        traced_model = torch.jit.trace(torch_model, input_data).eval()
        mod, params = tvm.relay.frontend.from_pytorch(traced_model, shape_list)
    else:
        tvmc_model = load_model(path=model_path, shape_dict=shape_dict)
        mod, params = tvm.relay.transform.DynamicToStatic()(tvmc_model.mod), tvmc_model.params
    
    input_layer_name_file = os.path.join(os.getcwd(), "input_layer_name")
    if not input_layer_name:
        input_layer_name = shape_dict.keys()[0]
    with open(input_layer_name_file, 'w') as file:
        file.write(input_layer_name)
    
    return mod, params

def tune_model(
    mod: tvm.IRModule,
    params: Dict[str, tvm.nd.NDArray],
    target: tvm.target.Target,
) -> Tuple[str, meta_schedule.database.Database]:
    work_dir = os.path.join(os.getcwd(), "metaschedule_workdir")
    if not os.path.exists(work_dir):
        os.mkdir(work_dir)
    print("Extracting tasks...")
    extracted_tasks = meta_schedule.relay_integration.extract_tasks(
        mod, target, params
    )
    tasks, task_weights = meta_schedule.relay_integration.extracted_tasks_to_tune_contexts(
        extracted_tasks, work_dir, strategy="evolutionary"
    )

    print("Begin tuning...")
    evaluator_config = meta_schedule.runner.config.EvaluatorConfig(
        number=1,
        repeat=10,
        enable_cpu_cache_flush=True
    )
    database = meta_schedule.tune.tune_tasks(
        tasks=tasks,
        task_weights=task_weights,
        work_dir=work_dir,
        max_trials_global=10000,
        num_trials_per_iter=64,
        max_trials_per_task=512,
        builder=meta_schedule.builder.LocalBuilder(),
        runner=meta_schedule.runner.LocalRunner(
            evaluator_config=evaluator_config
        ),
    )
    
    return work_dir, database


def compile_model(
    mod: tvm.IRModule,
    params: Dict[str, tvm.nd.NDArray],
    work_dir: str,
    target: tvm.target.Target,
    opt_level: int,
    build_conf: Dict[str, Any],
    use_vm: bool,
    database: Optional[meta_schedule.database.Database] = None,
) -> Union[tvm.runtime.Module, tvm.runtime.vm.Executable]:
    if work_dir != '':
        if not database:
            database = meta_schedule.database.JSONDatabase(
                f"{work_dir}/database_workload.json",
                f"{work_dir}/database_tuning_record.json",
                allow_missing=False
            )
        build_conf["relay.backend.use_meta_schedule"] = True
        with tvm.transform.PassContext(
            opt_level=opt_level, 
            config=build_conf
        ):
            lib = meta_schedule.relay_integration.compile_relay(
                database=database,
                mod=mod,
                target=target,
                params=params,
                backend="vm" if use_vm else "graph"
            )
    else:
        with tvm.transform.PassContext(
            opt_level=opt_level, 
            config=build_conf, 
        ):
            if use_vm:
                lib = tvm.relay.backend.vm.compile(
                    mod=mod, 
                    target=target, 
                    params=params
                )
            else:
                lib = tvm.relay.build(
                    mod, 
                    target=target, 
                    params=params
                )
    return lib

def serialize_vm(
    vm_exec: tvm.runtime.vm.Executable
) -> tvm.runtime.Module:
    path_consts = os.path.join(
        tempfile.mkdtemp(
            dir=os.getcwd(), 
            suffix="-tvm-tmp"
        ), 
        "consts"
    )
    code_path = os.path.join(os.getcwd(), "vm_exec_code.ro")
    vm_exec.move_late_bound_consts(path_consts, byte_limit=256)
    code, lib = vm_exec.save()
    with open(code_path, "wb") as file:
        file.write(code)
    return lib

def main() -> None:
    model_path = os.environ.get('CM_ML_MODEL_FILE_WITH_PATH', None)
    compiled_model = os.path.join(os.getcwd(), 'model-tvm.so')
    print('TVM model: ' + model_path)
    if model_path.endswith('.so') or model_path.endswith('.dylib'):
        compiled_model = model_path
        if not os.path.isfile(compiled_model):
            print('')
            raise RuntimeError(
                f"Error: Model file {compiled_model} not found!"
            )
    else:
        mod, params = get_mod_params(
            model_path=os.environ.get('CM_ML_MODEL_FILE_WITH_PATH', None),
            model_name=os.environ.get('CM_ML_MODEL', '').strip().lower(),
            batch_size=int(os.environ.get('CM_ML_MODEL_MAX_BATCH_SIZE', 1)),
            frontend=os.environ.get("CM_TVM_FRONTEND_FRAMEWORK", None),
            input_shapes_str=os.environ.get('CM_ML_MODEL_INPUT_SHAPES', None),
            input_layer_name=os.environ.get('CM_ML_MODEL_INPUT_LAYER_NAME', None),
            num_channels=int(os.environ.get('CM_ML_MODEL_IMAGE_NUM_CHANNELS', 3)),
            image_width=int(os.environ.get('CM_ML_MODEL_IMAGE_WIDTH', 0)),
            image_height=int(os.environ.get('CM_ML_MODEL_IMAGE_HEIGHT', 0)),
            max_seq_length=int(os.environ.get('CM_ML_MODEL_MAX_SEQ_LENGTH', 0)),
        )
        opt_level = int(os.environ.get('CM_MLPERF_TVM_OPT_LEVEL', 3))
        target = os.environ.get(
            'CM_MLPERF_TVM_TARGET',
            f"llvm -num-cores {os.environ.get('CM_HOST_CPU_TOTAL_CORES', '1')}"
        )
        build_conf = {}
        target_host = None
        tvm_target = tvm.target.Target(target, host=target_host)
        tune_model_flag = os.environ.get('CM_TUNE_TVM_MODEL', 'no') == 'yes'
        work_dir = ''
        database = None
        use_vm = os.environ.get('CM_TVM_USE_VM', 'no') == 'yes'
        if tune_model_flag:
            work_dir, database = tune_model(
                mod=mod, 
                params=params, 
                target=tvm_target, 
            )
        lib = compile_model(
            mod=mod,
            params=params,
            work_dir=work_dir if work_dir != '' else os.environ.get('CM_TUNE_TVM_MODEL_WORKDIR', ''),
            target=tvm_target,
            opt_level=opt_level,
            build_conf=build_conf,
            use_vm=use_vm,
            database=database
        )
        if use_vm:
            lib = serialize_vm(
                vm_exec=lib
            )
            
        with open(os.path.join(os.getcwd(), "tvm_executor"), "w") as file:
            file.write("virtual_machine" if use_vm else "graph_executor")
        lib.export_library(compiled_model)
        print('TVM compiled model: ' + compiled_model)

if __name__ == "__main__":
    main()
