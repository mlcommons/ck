from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}
    env = i['env']

    if 'CM_MODEL' not in env:
        return {'return': 1, 'error': 'Please select a variation specifying the model to run'}
    if 'CM_MLPERF_DEVICE' not in env:
        return {'return': 1, 'error': 'Please select a variation specifying the device to run on'}

    if env.get('CM_MLPERF_SKIP_RUN', '') == "yes":
        return {'return': 0}

    cmds = []
    scenario = env['CM_MLPERF_LOADGEN_SCENARIO']
    mode = env['CM_MLPERF_LOADGEN_MODE']

    if env['CM_MODEL'] == "resnet50":
        target_data_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'data', 'imagenet')
        if not os.path.exists(target_data_path):
            cmds.append(f"ln -s {env['CM_DATASET_IMAGENET_PATH']} {target_data_path}")

        model_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'models', 'ResNet50', 'resnet50_v1.onnx')
        model_name = "resnet50"

    elif "bert" in env['CM_MODEL']:
        target_data_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'data', 'squad')
        if not os.path.exists(target_data_path):
            cmds.append("make download_data BENCHMARKS='bert'")

        model_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'models', 'bert', 'bert_large_v1_1.onnx')
        model_name = "bert"

    elif env['CM_MODEL'] == "retinanet":
        #print(env)
        dataset_path = env['CM_DATASET_PATH']
        #return {'return': 1, 'error': 'error'}

        annotations_path = env['CM_DATASET_ANNOTATIONS_DIR_PATH']
        target_data_path_dir = os.path.join(env['MLPERF_SCRATCH_PATH'], 'data', 'open-images-v6-mlperf')
        if not os.path.exists(target_data_path_dir):
            cmds.append(f"mkdir -p {target_data_path_dir}")
        target_data_path = os.path.join(target_data_path_dir, 'annotations')
        if not os.path.exists(target_data_path):
            cmds.append(f"ln -s {annotations_path} {target_data_path}")

        target_data_path_dir = os.path.join(env['MLPERF_SCRATCH_PATH'], 'data', 'open-images-v6-mlperf', 'validation')
        if not os.path.exists(target_data_path_dir):
            cmds.append(f"mkdir -p {target_data_path_dir}")
        target_data_path = os.path.join(target_data_path_dir, 'data')
        if not os.path.exists(target_data_path):
            cmds.append(f"ln -s {dataset_path} {target_data_path}")

        calibration_dataset_path=env['CM_CALIBRATION_DATASET_PATH']
        target_data_path_dir = os.path.join(env['MLPERF_SCRATCH_PATH'], 'data', 'open-images-v6-mlperf','calibration', 'train')
        if not os.path.exists(target_data_path_dir):
            cmds.append(f"mkdir -p {target_data_path_dir}")
        target_data_path = os.path.join(target_data_path_dir, 'data')
        if not os.path.exists(target_data_path):
            cmds.append(f"ln -s {calibration_dataset_path} {target_data_path}")

        preprocessed_data_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'preprocessed_data')
        model_path = env['CM_NVIDIA_RETINANET_EFFICIENT_NMS_CONCAT_MODEL_WITH_PATH']
        target_model_path_dir = os.path.join(env['MLPERF_SCRATCH_PATH'], 'models', 'retinanet-resnext50-32x4d', 'submission')
        if not os.path.exists(target_model_path_dir):
            cmds.append(f"mkdir -p {target_model_path_dir}")
        target_model_path = os.path.join(target_model_path_dir, 'retinanet_resnext50_32x4d_efficientNMS.800x800.onnx')
        if not os.path.exists(target_model_path):
            cmds.append(f"ln -sf {model_path} {target_model_path}")
        model_name = "retinanet"

    if not env.get('CM_SKIP_MODEL_DOWNLOAD', 'no') == "yes" and not os.path.exists(model_path):
        cmds.append(f"make download_model BENCHMARKS='{model_name}'")
    if not env.get('CM_SKIP_PREPROCESS_DATASET', 'no') == "yes":
        cmds.append(f"make preprocess_data BENCHMARKS='{model_name}'")
    scenario=env['CM_MLPERF_LOADGEN_SCENARIO'].lower()

    if env['CM_MLPERF_LOADGEN_MODE'] == "accuracy":
        test_mode = "AccuracyOnly"
    elif env['CM_MLPERF_LOADGEN_MODE'] == "performance":
        test_mode = "PerformanceOnly"
    elif env['CM_MLPERF_LOADGEN_MODE'] == "compliance":
        test_mode = ""
        test_name = env.get('CM_MLPERF_LOADGEN_COMPLIANCE_TEST', 'test01').lower()
        env['CM_MLPERF_NVIDIA_RUN_COMMAND'] = "run_audit_{}_once".format(test_name)
    else:
        return {'return': 1, 'error': 'Unsupported mode: {}'.format(env['CM_MLPERF_LOADGEN_MODE'])}

    run_config = ''

    target_qps = env.get('CM_MLPERF_LOADGEN_TARGET_QPS')
    offline_target_qps = env.get('CM_MLPERF_LOADGEN_OFFLINE_TARGET_QPS')
    server_target_qps = env.get('CM_MLPERF_LOADGEN_SERVER_TARGET_QPS')
    if target_qps:
        if scenario == "offline" and not offline_target_qps:
            run_config += f" --offline_expected_qps={target_qps}"
        elif scenario == "server" and not server_target_qps:
            run_config += f" --server_target_qps={target_qps}"

    if offline_target_qps:
        run_config += f" --offline_expected_qps={offline_target_qps}"
    if server_target_qps:
        run_config += f" --server_target_qps={server_target_qps}"

    target_latency = env.get('CM_MLPERF_LOADGEN_TARGET_LATENCY')
    singlestream_target_latency = env.get('CM_MLPERF_LOADGEN_SINGLESTREAM_TARGET_LATENCY')
    multistream_target_latency = env.get('CM_MLPERF_LOADGEN_MULTISTREAM_TARGET_LATENCY')
    if target_latency:
        target_latency_ns = int(target_latency) * 1000000
        if scenario == "singlestream" and not singlestream_target_latency:
            run_config += f" --single_stream_expected_latency_ns={target_latency_ns}"
        elif scenario == "multistream" and not multistream_target_latency:
            run_config += f" --multi_stream_expected_latency_ns={target_latency_ns}"

    if singlestream_target_latency:
        singlestream_target_latency_ns = int(singlestream_target_latency) * 1000000
        run_config += f" --single_stream_expected_latency_ns={singlestream_target_latency_ns}"
    if multistream_target_latency:
        multistream_target_latency_ns = int(multistream_target_latency) * 1000000
        run_config += f" --multi_stream_expected_latency_ns={multistream_target_latency_ns}"

    use_triton = env.get('CM_MLPERF_NVIDIA_HARNESS_USE_TRITON')
    if use_triton:
        run_config += f" --use_triton --config_ver=triton"

    gpu_copy_streams = env.get('CM_MLPERF_NVIDIA_HARNESS_GPU_COPY_STREAMS')
    if gpu_copy_streams:
        run_config += f" --gpu_copy_streams={gpu_copy_streams}"
    gpu_inference_streams = env.get('CM_MLPERF_NVIDIA_HARNESS_GPU_INFERENCE_STREAMS')
    if gpu_inference_streams:
        run_config += f" --gpu_inference_streams={gpu_inference_streams}"
    dla_copy_streams = env.get('CM_MLPERF_NVIDIA_HARNESS_DLA_COPY_STREAMS')
    if dla_copy_streams:
        run_config += f" --dla_copy_streams={dla_copy_streams}"
    dla_inference_streams = env.get('CM_MLPERF_NVIDIA_HARNESS_DLA_INFERENCE_STREAMS')
    if dla_inference_streams:
        run_config += f" --dla_inference_streams={dla_inference_streams}"

    gpu_batch_size = env.get('CM_MLPERF_NVIDIA_HARNESS_GPU_BATCH_SIZE')
    if gpu_batch_size:
        run_config += f" --gpu_batch_size={gpu_batch_size}"
    dla_batch_size = env.get('CM_MLPERF_NVIDIA_HARNESS_DLA_BATCH_SIZE')
    if dla_batch_size:
        run_config += f" --dla_batch_size={dla_batch_size}"

    input_format = env.get('CM_MLPERF_NVIDIA_HARNESS_INPUT_FORMAT')
    if input_format:
        run_config += f" --input_format={input_format}"

    workspace_size = env.get('CM_MLPERF_NVIDIA_HARNESS_WORKSPACE_SIZE')
    if workspace_size:
        run_config += f" --workspace_size={workspace_size}"

    if env.get('CM_MLPERF_LOADGEN_LOGS_DIR'):
        env['MLPERF_LOADGEN_LOGS_DIR'] = env['CM_MLPERF_LOADGEN_LOGS_DIR']

    log_dir = env.get('CM_MLPERF_NVIDIA_HARNESS_LOG_DIR')
    if log_dir:
        run_config += f" --log_dir={log_dir}"

    use_graphs = env.get('CM_MLPERF_NVIDIA_HARNESS_USE_GRAPHS')
    if use_graphs:
        run_config += " --use_graphs"

    run_infer_on_copy_streams = env.get('CM_MLPERF_NVIDIA_HARNESS_RUN_INFER_ON_COPY_STREAMS')
    if run_infer_on_copy_streams:
        run_config += " --run_infer_on_copy_streams"

    start_from_device = env.get('CM_MLPERF_NVIDIA_HARNESS_START_FROM_DEVICE')
    if start_from_device:
        run_config += " --start_from_device"

    end_on_device = env.get('CM_MLPERF_NVIDIA_HARNESS_END_ON_DEVICE')
    if end_on_device:
        run_config += " --end_on_device"

    max_dlas = env.get('CM_MLPERF_MAX_DLAS')
    if max_dlas:
        run_config += f" --max_dlas={max_dlas}"

    make_command = env.get('CM_MLPERF_NVIDIA_RUN_COMMAND', 'run')

    if test_mode:
        test_mode_string = " --test_mode={}".format(test_mode)
    else:
        test_mode_string = ""

    cmds.append(f"make {make_command} RUN_ARGS=' --benchmarks={model_name} --scenarios={scenario} {test_mode_string} {run_config}'")
    #print(cmds)
    run_cmd = " && ".join(cmds)
    env['CM_MLPERF_RUN_CMD'] = run_cmd
    env['CM_RUN_CMD'] = run_cmd
    env['CM_RUN_DIR'] = env['CM_MLPERF_INFERENCE_NVIDIA_CODE_PATH']

#    print(env)

    return {'return':0}

def postprocess(i):

    env = i['env']
    return {'return':0}
