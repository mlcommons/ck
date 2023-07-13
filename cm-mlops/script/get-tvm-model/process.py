import os
import tempfile
import tvm
from tvm import relay
from tvm.driver.tvmc.model import TVMCModel
from tvm.driver.tvmc.frontends import load_model
from typing import Dict, Tuple, Optional, List, Any, Union

def get_shape_dict_from_onnx(
    shape: List[int],
    model_path: str
) -> Dict[str, List[int]]:
    import onnx
    onnx_model = onnx.load(model_path)
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
    num_channels: Optional[int] = None,
    image_width: Optional[int] = None,
    image_height: Optional[int] = None,
    max_seq_length: Optional[int] = None
) -> Tuple[tvm.IRModule, Dict[str, tvm.nd.NDArray]]:
    if not input_shapes_str and ((not width or not height) or not max_seq_length):
        raise RuntimeError(
            "Error: None of environment variables storing shape is set!"
        )
    if input_shapes_str:
        shape_dict = eval('{' + input_shapes_str.replace('BATCH_SIZE', str(batch_size)) + '}')
    else:
        if image_width and image_height:
            shape = [batch_size, num_channels, image_height, image_width]
        elif max_seq_length:
            shape = [batch_size, max_seq_length]
        if frontend == "onnx":
            shape_dict = get_shape_dict_from_onnx(shape, model_path)
        else:
            raise RuntimeError(
                "Error: Cannot find proper shapes in environment variables"
            )
    tvmc_model = load_model(path=model_path, shape_dict=shape_dict)
    mod, params = relay.transform.DynamicToStatic()(tvmc_model.mod), tvmc_model.params
    
    return mod, params

def tune_model(
    mod: tvm.IRModule,
    params: Dict[str, tvm.nd.NDArray],
    target: tvm.target.Target,
) -> Tuple[str, tvm.meta_schedule.database.Database]:
    from tvm import meta_schedule as ms
    work_dir = os.path.join(os.getcwd(), "metaschedule_workdir")
    if not os.path.exists(work_dir):
        os.mkdir(work_dir)
    print("Extracting tasks...")
    extracted_tasks = ms.relay_integration.extract_tasks(
        mod, tvm_target, params
    )
    tasks, task_weights = ms.relay_integration.extracted_tasks_to_tune_contexts(
        extracted_tasks, work_dir, strategy="evolutionary"
    )

    print("Begin tuning...")
    evaluator_config = ms.runner.config.EvaluatorConfig(
        number=1,
        repeat=10,
        enable_cpu_cache_flush=True
    )
    database = ms.tune.tune_tasks(
        tasks=tasks,
        task_weights=task_weights,
        work_dir=work_dir,
        max_trials_global=20000,
        num_trials_per_iter=64,
        max_trials_per_task=512,
        builder=ms.builder.LocalBuilder(),
        runner=ms.runner.LocalRunner(
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
    database: Optional[tvm.meta_schedule.database.Database] = None,
) -> Union[tvm.runtime.Module, tvm.runtime.vm.Executable]:
    if work_dir != '':
        if not database:
            database = ms.database.JSONDatabase(
                f"{work_dir}/database_workload.json",
                f"{work_dir}/database_tuning_record.json",
                allow_missing=False
            )
        build_conf["relay.backend.use_meta_schedule"] = True
        with tvm.transform.PassContext(
            opt_level=opt_level, 
            config=build_conf
        ):
            lib = ms.relay_integration.compile_relay(
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
                lib = relay.build(
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
            batch_size=os.environ.get('CM_ML_MODEL_MAX_BATCH_SIZE', 1),
            frontend=os.environ.get("CM_TVM_FRONTEND_FRAMEWORK", None),
            input_shapes_str=os.environ.get('CM_ML_MODEL_INPUT_SHAPES', None),
            num_channels=os.environ.get('CM_ML_MODEL_IMAGE_NUM_CHANNELS', 3),
            image_width=os.environ.get('CM_ML_MODEL_IMAGE_WIDTH', None),
            image_height=os.environ.get('CM_ML_MODEL_IMAGE_HEIGHT', None),
            max_seq_length=os.environ.get('CM_ML_MODEL_MAX_SEQ_LENGTH', None),
        )
        opt_level = int(os.environ.get('CM_MLPERF_TVM_OPT_LEVEL', 3))
        target = os.environ.get(
            'CM_MLPERF_TVM_TARGET',
            f"llvm -num-cores {os.environ.get('CM_HOST_CPU_TOTAL_CORES', '1')}"
        )
        build_conf = {}
        target_host = None
        tvm_target = tvm.target.Target(target, host=target_host)
        tune_model = os.environ.get('CM_TUNE_TVM_MODEL', 'no') == 'yes'
        work_dir = ''
        database = None
        use_vm = os.environ.get('CM_TVM_USE_VM', 'no') == 'yes'
        if tune_model:
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