import os
import tempfile
import tvm
from tvm import relay

max_batchsize = os.environ['CM_ML_MODEL_MAX_BATCH_SIZE']
input_shapes = os.environ.get('CM_ML_MODEL_INPUT_SHAPES', '').strip()

if input_shapes == '':
    print('')
    raise RuntimeError(
        "Error: CM_ML_MODEL_INPUT_SHAPES environment variable is not defined!")

input_shapes = input_shapes.replace('BATCH_SIZE', str(max_batchsize))
model_path = os.environ.get('CM_ML_MODEL_FILE_WITH_PATH')

print('TVM model: ' + model_path)

# Check if load precompiled model
compiled_model = os.path.join(os.getcwd(), 'model-tvm.so')
if model_path.endswith('.so') or model_path.endswith('.dylib'):
    compiled_model = model_path

    if not os.path.isfile(compiled_model):
        print('')
        raise RuntimeError(
            f"Error: Model file {compiled_model} not found!")
else:

    build_conf = {}
    params = {}

    if model_path.endswith('.pt') or model_path.endswith('.pth'):
        import torch
        from tvm.relay.build_module import bind_params_by_name
        from torchvision.models import resnet50

        shape_list = eval('[' + input_shapes + ']')

        print('TVM shape list: '+str(shape_list))

        x = os.environ.get('CM_MLPERF_TVM_TORCH_QUANTIZED_ENGINE', '')
        if x != '':
            torch.backends.quantized.engine = x

        if model_path.endswith('.pt'):
            pytorch_model = torch.jit.load(model_path)
        elif model_path.endswith('.pth'):
            pytorch_model = resnet50()
            pytorch_model.load_state_dict(torch.load(model_path))
        pytorch_model.eval()

        input_data = torch.randn(shape_list[0][1])
        pytorch_model = torch.jit.trace(pytorch_model, input_data)

        mod, params = relay.frontend.from_pytorch(pytorch_model, shape_list)

        mod["main"] = bind_params_by_name(mod["main"], params)

        # Some optimizations
        mod = relay.transform.FoldConstant()(mod)

        if os.environ.get('CM_MLPERF_TVM_USE_DNNL', '').strip().lower() == 'yes':
            from tvm.relay.op.contrib.dnnl import partition_for_dnnl
            from tvm.driver.tvmc.common import convert_graph_layout

            #  move to NHWC layout, prerequisite for DNNL partitioning
            mod = convert_graph_layout(mod, "NHWC")
            mod = relay.transform.FoldConstant()(mod)

            mod = partition_for_dnnl(mod)

    elif model_path.endswith('.onnx'):
        import onnx

        shape_dict = eval('{' + input_shapes + '}')

        print('TVM shape dict: '+str(shape_dict))

        onnx_model = onnx.load(model_path)

        mod, params = relay.frontend.from_onnx(
            onnx_model, shape_dict, freeze_params=True
        )

        if os.environ.get('CM_MLPERF_TVM_TRANSFORM_LAYOUT', '').strip().lower() == 'yes':
            kernel_layout = 'NHWC'

            desired_layouts = {
                'qnn.conv2d': [kernel_layout, 'default'],
                'nn.conv2d': [kernel_layout, 'default'],
                'nn.conv2d_transpose': [kernel_layout, 'default'],
                'nn.depthwise_conv2d': [kernel_layout, 'default'],
                'nn.conv3d': [kernel_layout, 'default'],
                'nn.conv3d_transpose': [kernel_layout, 'default'],
            }

            seq = tvm.transform.Sequential([relay.transform.RemoveUnusedFunctions(),
                                            relay.transform.FoldConstant(),
                                            relay.transform.ConvertLayout(
                                                desired_layouts),
                                            ])

            with tvm.transform.PassContext(opt_level=3):
                mod = seq(mod)

    elif model_path.endswith('.tflite'):
        # Grigori used https://tvm.apache.org/docs/tutorials/frontend/deploy_prequantized_tflite.html

        import tflite

        shape_dict = eval('{' + input_shapes + '}')

        print('TVM shape dict: '+str(shape_dict))

        tflite_model_buf = open(model_path, "rb").read()
        tflite_model = tflite.Model.GetRootAsModel(tflite_model_buf, 0)

        mod, params = relay.frontend.from_tflite(tflite_model, shape_dict)

    else:
        print('')
        raise RuntimeError(
            f"Error: model extension is not supported in TVM backend ({model_path})!")

    opt_lvl = int(os.environ.get('CM_MLPERF_TVM_OPT_LEVEL', 3))

    target = os.environ.get('CM_MLPERF_TVM_TARGET',
                            f"llvm -num-cores {os.environ.get('CM_HOST_CPU_TOTAL_CORES', '1')}")

    target_host = None

    tvm_target = tvm.target.Target(target, host=target_host)

    tune_model = os.environ.get('CM_TUNE_TVM_MODEL', 'no') == 'yes'

    work_dir = ''

    use_vm = os.environ.get('CM_TVM_USE_VM', 'no') == 'yes'

    if tune_model:
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

    if work_dir == '':
        work_dir = os.environ.get('CM_TUNE_TVM_MODEL_WORKDIR', '')

    if work_dir != '':
        database = ms.database.JSONDatabase(f"{work_dir}/database_workload.json",
                                            f"{work_dir}/database_tuning_record.json",
                                            allow_missing=False)

        build_conf["relay.backend.use_meta_schedule"] = True

        with tvm.transform.PassContext(opt_level=opt_lvl, config=build_conf):
            if use_vm:
                vm_exec = ms.relay_integration.compile_relay(
                    database=database,
                    mod=mod,
                    target=tvm_target,
                    params=params,
                    backend="vm"
                )
            else:
                lib = ms.relay_integration.compile_relay(
                    database, mod, tvm_target, params)

    else:
        with tvm.transform.PassContext(opt_level=opt_lvl, config=build_conf):
            if use_vm:
                vm_exec = tvm.relay.backend.vm.compile(
                    mod, target, params=params)
            else:
                lib = relay.build(mod, target=tvm_target, params=params)

    if use_vm:
        path_consts = os.path.join(tempfile.mkdtemp(
            dir=os.getcwd(), suffix="-tvm-tmp"), "consts")
        code_path = os.path.join(os.getcwd(), "vm_exec_code.ro")

        vm_exec.move_late_bound_consts(path_consts, byte_limit=256)

        code, lib = vm_exec.save()

        with open(code_path, "wb") as file:
            file.write(code)

    lib.export_library(compiled_model)
    print('TVM compiled model: ' + compiled_model)
