from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}
    env = i['env']

    if env.get('CM_MODEL', '') == '':
        return {'return': 1, 'error': 'Please select a variation specifying the model to run'}

    make_command = env['MLPERF_NVIDIA_RUN_COMMAND']

    if env.get('CM_MLPERF_DEVICE', '') == '':
        return {'return': 1, 'error': 'Please select a variation specifying the device to run on'}

    if env.get('CM_MLPERF_SKIP_RUN', '') == "yes" and make_command == "run_harness":
        return {'return': 0}

    env['MLPERF_SCRATCH_PATH'] = env['CM_NVIDIA_MLPERF_SCRATCH_PATH']

    cmds = []
    scenario = env['CM_MLPERF_LOADGEN_SCENARIO']
    mode = env['CM_MLPERF_LOADGEN_MODE']

    make_command = env['MLPERF_NVIDIA_RUN_COMMAND']

    if make_command == "prebuild":
        cmds.append(f"make prebuild NETWORK_NODE=SUT")

    if env['CM_MODEL'] == "resnet50":
        target_data_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'data', 'imagenet')
        if not os.path.exists(target_data_path):
            cmds.append(f"ln -sf {env['CM_DATASET_IMAGENET_PATH']} {target_data_path}")

        model_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'models', 'ResNet50', 'resnet50_v1.onnx')

        if not os.path.exists(os.path.dirname(model_path)):
          cmds.append(f"mkdir -p {os.path.dirname(model_path)}")

        if not os.path.exists(model_path):
            cmds.append(f"ln -sf {env['CM_ML_MODEL_FILE_WITH_PATH']} {model_path}")
        model_name = "resnet50"

    elif "bert" in env['CM_MODEL']:
        target_data_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'data', 'squad')
        if not os.path.exists(target_data_path):
            cmds.append("make download_data BENCHMARKS='bert'")

        fp32_model_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'models', 'bert', 'bert_large_v1_1.onnx')
        int8_model_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'models', 'bert', 'bert_large_v1_1_fake_quant.onnx')
        vocab_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'models', 'bert', 'vocab.txt')

        if not os.path.exists(os.path.dirname(fp32_model_path)):
          cmds.append(f"mkdir -p {os.path.dirname(fp32_model_path)}")

        if not os.path.exists(fp32_model_path):
            cmds.append(f"ln -sf {env['CM_ML_MODEL_BERT_LARGE_FP32_PATH']} {fp32_model_path}")
        if not os.path.exists(int8_model_path):
            cmds.append(f"ln -sf {env['CM_ML_MODEL_BERT_LARGE_INT8_PATH']} {int8_model_path}")
        if not os.path.exists(vocab_path):
            cmds.append(f"ln -sf {env['CM_ML_MODEL_BERT_VOCAB_FILE_WITH_PATH']} {vocab_path}")
        model_name = "bert"
        model_path = fp32_model_path

    elif "3d-unet" in env['CM_MODEL']:
        target_data_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'data', 'KiTS19', 'kits19', 'data')
        target_data_path_base_dir = os.path.dirname(target_data_path)
        if not os.path.exists(target_data_path_base_dir):
            cmds.append(f"mkdir -p {target_data_path_base_dir}")
 
        if not os.path.exists(target_data_path):
            #cmds.append(f"ln -sf {env['CM_DATASET_PATH']} {target_data_path}")
            cmds.append("make download_data BENCHMARKS='3d-unet'")

        model_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'models', '3d-unet-kits19', '3dUNetKiTS19.onnx')
        model_name = "3d-unet"

    elif "rnnt" in env['CM_MODEL']:
        target_data_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'data', 'LibriSpeech', 'dev-clean')
        target_data_path_base_dir = os.path.dirname(target_data_path)
        if not os.path.exists(target_data_path_base_dir):
            cmds.append(f"mkdir -p {target_data_path_base_dir}")
        if not os.path.exists(target_data_path):
            #cmds.append(f"ln -sf {env['CM_DATASET_LIBRISPEECH_PATH']} {target_data_path}")
            cmds.append("make download_data BENCHMARKS='rnnt'")

        model_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'models', 'rnn-t', 'DistributedDataParallel_1576581068.9962234-epoch-100.pt')
        model_name = "rnnt"

    elif "pdlrm" in env['CM_MODEL']:
        target_data_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'data', 'criteo')
        if not os.path.exists(target_data_path):
            cmds.append(f"ln -sf {env['CM_DATASET_PREPROCESSED_PATH']} {target_data_path}")

        model_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'models', 'dlrm', 'tb00_40M.pt')
        if not os.path.exists(os.path.dirname(model_path)):
          cmds.append(f"mkdir -p {os.path.dirname(model_path)}")

        if not os.path.exists(model_path):
            cmds.append(f"ln -sf {env['CM_ML_MODEL_FILE_WITH_PATH']} {model_path}")
        model_name = "dlrm"

    elif "dlrm-v2" in env['CM_MODEL']:
        model_name = "dlrm-v2"

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
            cmds.append(f"ln -sf {annotations_path} {target_data_path}")

        target_data_path_dir = os.path.join(env['MLPERF_SCRATCH_PATH'], 'data', 'open-images-v6-mlperf', 'validation')
        if not os.path.exists(target_data_path_dir):
            cmds.append(f"mkdir -p {target_data_path_dir}")
        target_data_path = os.path.join(target_data_path_dir, 'data')
        if not os.path.exists(target_data_path):
            cmds.append(f"ln -sf {dataset_path} {target_data_path}")

        calibration_dataset_path=env['CM_CALIBRATION_DATASET_PATH']
        target_data_path_dir = os.path.join(env['MLPERF_SCRATCH_PATH'], 'data', 'open-images-v6-mlperf','calibration', 'train')
        if not os.path.exists(target_data_path_dir):
            cmds.append(f"mkdir -p {target_data_path_dir}")
        target_data_path = os.path.join(target_data_path_dir, 'data')
        if not os.path.exists(target_data_path):
            cmds.append(f"ln -sf {calibration_dataset_path} {target_data_path}")

        preprocessed_data_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'preprocessed_data')
        target_model_path_dir = os.path.join(env['MLPERF_SCRATCH_PATH'], 'models', 'retinanet-resnext50-32x4d')
        if not os.path.exists(target_model_path_dir):
            cmds.append(f"mkdir -p {target_model_path_dir}")
        model_path = os.path.join(target_model_path_dir, 'retinanet-fpn-torch2.1-postprocessed.onnx')
        alt_model_path = os.path.join(target_model_path_dir, 'retinanet-fpn-torch2.2-postprocessed.onnx')
        if not os.path.exists(model_path) and os.path.exists(alt_model_path):
            cmds.append(f"ln -s {alt_model_path} {model_path}")

        model_name = "retinanet"

    elif "gptj" in env['CM_MODEL']:
        target_data_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'data', 'cnn-daily-mail', 'cnn_eval.json')
        if not os.path.exists(target_data_path):
            cmds.append("make download_data BENCHMARKS='gptj'")

        fp32_model_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'models', 'GPTJ-6B', 'checkpoint-final')
        fp8_model_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'models', 'GPTJ-6B', 'fp8-quantized-ammo', 'GPTJ-07142023.pth')
        vocab_path = os.path.join(env['MLPERF_SCRATCH_PATH'], 'models', 'bert', 'vocab.txt')

        if not os.path.exists(os.path.dirname(fp32_model_path)):
          cmds.append(f"mkdir -p {os.path.dirname(fp32_model_path)}")
        if not os.path.exists(os.path.dirname(fp8_model_path)):
          cmds.append(f"mkdir -p {os.path.dirname(fp8_model_path)}")

        if not os.path.exists(fp32_model_path):
            env['CM_REQUIRE_GPTJ_MODEL_DOWNLOAD'] = 'yes' # download via prehook_deps
            cmds.append(f"cp -r $CM_ML_MODEL_FILE_WITH_PATH {fp32_model_path}")

        model_name = "gptj"
        model_path = fp8_model_path
    #cmds.append(f"make prebuild")
    if make_command == "download_model":
        if not os.path.exists(model_path):
            cmds.append(f"make download_model BENCHMARKS='{model_name}'")
        else:
            return {'return':0}

    elif make_command == "preprocess_data":
        if env['CM_MODEL'] == "rnnt":
            cmds.append(f"rm -rf {os.path.join(env['MLPERF_SCRATCH_PATH'], 'preprocessed_data', 'rnnt_dev_clean_500_raw')}")
            cmds.append(f"rm -rf {os.path.join(env['MLPERF_SCRATCH_PATH'], 'preprocessed_data', 'rnnt_train_clean_512_wav')}")
        cmds.append(f"make preprocess_data BENCHMARKS='{model_name}'")

    else:
        scenario=env['CM_MLPERF_LOADGEN_SCENARIO'].lower()

        if env['CM_MLPERF_LOADGEN_MODE'] == "accuracy":
            test_mode = "AccuracyOnly"
        elif env['CM_MLPERF_LOADGEN_MODE'] == "performance":
            test_mode = "PerformanceOnly"
        elif env['CM_MLPERF_LOADGEN_MODE'] == "compliance":
            test_mode = ""
            test_name = env.get('CM_MLPERF_LOADGEN_COMPLIANCE_TEST', 'test01').lower()
            env['CM_MLPERF_NVIDIA_RUN_COMMAND'] = "run_audit_{}_once".format(test_name)
            make_command = "run_audit_{}_once".format(test_name)
        else:
            return {'return': 1, 'error': 'Unsupported mode: {}'.format(env['CM_MLPERF_LOADGEN_MODE'])}

        run_config = ''

        target_qps = env.get('CM_MLPERF_LOADGEN_TARGET_QPS')
        offline_target_qps = env.get('CM_MLPERF_LOADGEN_OFFLINE_TARGET_QPS')
        server_target_qps = env.get('CM_MLPERF_LOADGEN_SERVER_TARGET_QPS')
        if target_qps:
            target_qps = int(float(target_qps))
            if scenario == "offline" and not offline_target_qps:
                run_config += f" --offline_expected_qps={target_qps}"
            elif scenario == "server" and not server_target_qps:
                run_config += f" --server_target_qps={target_qps}"

        if offline_target_qps:
            offline_target_qps = int(float(offline_target_qps))
            run_config += f" --offline_expected_qps={offline_target_qps}"
        if server_target_qps:
            server_target_qps = int(float(server_target_qps))
            run_config += f" --server_target_qps={server_target_qps}"

        target_latency = env.get('CM_MLPERF_LOADGEN_TARGET_LATENCY')
        singlestream_target_latency = env.get('CM_MLPERF_LOADGEN_SINGLESTREAM_TARGET_LATENCY')
        multistream_target_latency = env.get('CM_MLPERF_LOADGEN_MULTISTREAM_TARGET_LATENCY')
        if target_latency:
            target_latency_ns = int(float(target_latency) * 1000000)
            if scenario == "singlestream" and not singlestream_target_latency:
                run_config += f" --single_stream_expected_latency_ns={target_latency_ns}"
            elif scenario == "multistream" and not multistream_target_latency:
                run_config += f" --multi_stream_expected_latency_ns={target_latency_ns}"

        if singlestream_target_latency:
            singlestream_target_latency_ns = int(float(singlestream_target_latency) * 1000000)
            run_config += f" --single_stream_expected_latency_ns={singlestream_target_latency_ns}"
        if multistream_target_latency:
            multistream_target_latency_ns = int(float(multistream_target_latency) * 1000000)
            run_config += f" --multi_stream_expected_latency_ns={multistream_target_latency_ns}"

        high_accuracy = "99.9" in env['CM_MODEL']

        config_ver_list = []

        use_lon = env.get('CM_MLPERF_NVIDIA_HARNESS_LON')
        if use_lon:
            config_ver_list.append( "lon_node")
            #run_config += " --lon_node"

        maxq = env.get('CM_MLPERF_NVIDIA_HARNESS_MAXQ')
        if maxq:
            config_ver_list.append( "maxq")

        if high_accuracy:
            config_ver_list.append( "high_accuracy")

        use_triton = env.get('CM_MLPERF_NVIDIA_HARNESS_USE_TRITON')
        if use_triton:
            run_config += " --use_triton "
            config_ver_list.append( "triton")

        if config_ver_list:
            run_config += f" --config_ver={'_'.join(config_ver_list)}"

        user_conf_path = env.get('CM_MLPERF_USER_CONF')
        if user_conf_path and env['CM_MLPERF_NVIDIA_HARNESS_RUN_MODE'] == "run_harness":
            run_config += f" --user_conf_path={user_conf_path}"

        mlperf_conf_path = env.get('CM_MLPERF_INFERENCE_CONF_PATH')
        if mlperf_conf_path and env['CM_MLPERF_NVIDIA_HARNESS_RUN_MODE'] == "run_harness":
            run_config += f" --mlperf_conf_path={mlperf_conf_path}"

        power_setting = env.get('CM_MLPERF_NVIDIA_HARNESS_POWER_SETTING')
        if power_setting and env['CM_MLPERF_NVIDIA_HARNESS_RUN_MODE'] == "run_harness":
            run_config += f" --power_setting={power_setting}"

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

        performance_sample_count = env.get('CM_MLPERF_PERFORMANCE_SAMPLE_COUNT')
        if performance_sample_count:
            run_config += f" --performance_sample_count={performance_sample_count}"

        devices = env.get('CM_MLPERF_NVIDIA_HARNESS_DEVICES')
        if devices:
            run_config += f" --devices={devices}"

        audio_batch_size = env.get('CM_MLPERF_NVIDIA_HARNESS_AUDIO_BATCH_SIZE')
        if audio_batch_size:
            run_config += f" --audio_batch_size={audio_batch_size}"

        disable_encoder_plugin = env.get('CM_MLPERF_NVIDIA_HARNESS_DISABLE_ENCODER_PLUGIN')
        if disable_encoder_plugin and disable_encoder_plugin.lower() not in [ "no", "false" ]:
            run_config += " --disable_encoder_plugin"

        workspace_size = env.get('CM_MLPERF_NVIDIA_HARNESS_WORKSPACE_SIZE')
        if workspace_size:
            run_config += f" --workspace_size={workspace_size}"

        if env.get('CM_MLPERF_LOADGEN_LOGS_DIR'):
            env['MLPERF_LOADGEN_LOGS_DIR'] = env['CM_MLPERF_LOADGEN_LOGS_DIR']

        log_dir = env.get('CM_MLPERF_NVIDIA_HARNESS_LOG_DIR')
        if log_dir:
            run_config += f" --log_dir={log_dir}"

        use_graphs = env.get('CM_MLPERF_NVIDIA_HARNESS_USE_GRAPHS')
        if use_graphs  and use_graphs.lower() not in [ "no", "false" ]:
            run_config += " --use_graphs"

        use_deque_limit = env.get('CM_MLPERF_NVIDIA_HARNESS_USE_DEQUE_LIMIT')
        if use_deque_limit  and use_deque_limit.lower() not in [ "no", "false" ]:
            run_config += " --use_deque_limit"

            deque_timeout_usec = env.get('CM_MLPERF_NVIDIA_HARNESS_DEQUE_TIMEOUT_USEC')
            if deque_timeout_usec:
                run_config += f" --deque_timeout_usec={deque_timeout_usec}"

        use_cuda_thread_per_device = env.get('CM_MLPERF_NVIDIA_HARNESS_USE_CUDA_THREAD_PER_DEVICE')
        if use_cuda_thread_per_device  and use_cuda_thread_per_device.lower() not in [ "no", "false" ]:
            run_config += " --use_cuda_thread_per_device"

        run_infer_on_copy_streams = env.get('CM_MLPERF_NVIDIA_HARNESS_RUN_INFER_ON_COPY_STREAMS')
        if run_infer_on_copy_streams  and run_infer_on_copy_streams.lower() not in [ "no", "false" ]:
            run_config += " --run_infer_on_copy_streams"

        start_from_device = env.get('CM_MLPERF_NVIDIA_HARNESS_START_FROM_DEVICE')
        if start_from_device  and start_from_device.lower() not in [ "no", "false" ]:
            run_config += " --start_from_device"

        end_on_device = env.get('CM_MLPERF_NVIDIA_HARNESS_END_ON_DEVICE')
        if end_on_device  and end_on_device.lower() not in [ "no", "false" ]:
            run_config += " --end_on_device"

        max_dlas = env.get('CM_MLPERF_NVIDIA_HARNESS_MAX_DLAS')
        if max_dlas:
            run_config += f" --max_dlas={max_dlas}"

        graphs_max_seqlen = env.get('CM_MLPERF_NVIDIA_HARNESS_GRAPHS_MAX_SEQLEN')
        if graphs_max_seqlen:
            run_config += f" --graphs_max_seqlen={graphs_max_seqlen}"

        num_issue_query_threads = env.get('CM_MLPERF_NVIDIA_HARNESS_NUM_ISSUE_QUERY_THREADS')
        if num_issue_query_threads:
            run_config += f" --num_issue_query_threads={num_issue_query_threads}"

        soft_drop = env.get('CM_MLPERF_NVIDIA_HARNESS_SOFT_DROP')
        if soft_drop:
            run_config += f" --soft_drop={soft_drop}"

        use_small_tile_gemm_plugin = env.get('CM_MLPERF_NVIDIA_HARNESS_USE_SMALL_TILE_GEMM_PLUGIN')
        if use_small_tile_gemm_plugin  and use_small_tile_gemm_plugin.lower() not in [ "no", "false" ]:
            run_config += f" --use_small_tile_gemm_plugin"

        audio_buffer_num_lines = env.get('CM_MLPERF_NVIDIA_HARNESS_AUDIO_BUFFER_NUM_LINES')
        if audio_buffer_num_lines:
            run_config += f" --audio_buffer_num_lines={audio_buffer_num_lines}"

        use_fp8 = env.get('CM_MLPERF_NVIDIA_HARNESS_USE_FP8')
        if use_fp8 and use_fp8.lower() not in [ "no", "false" ]:
            run_config += f" --use_fp8"

        enable_sort = env.get('CM_MLPERF_NVIDIA_HARNESS_ENABLE_SORT')
        if enable_sort and enable_sort.lower() not in [ "no", "false" ]:
            run_config += f" --enable_sort"

        num_sort_segments = env.get('CM_MLPERF_NVIDIA_HARNESS_NUM_SORT_SEGMENTS')
        if num_sort_segments:
            run_config += f" --num_sort_segments={num_sort_segments}"

        embedding_weights_on_gpu_part = env.get('CM_MLPERF_NVIDIA_HARNESS_EMBEDDING_WEIGHTS_ON_GPU_PART', '')
        if embedding_weights_on_gpu_part != '':
            run_config += f" --embedding_weights_on_gpu_part={embedding_weights_on_gpu_part}"

        num_warmups = env.get('CM_MLPERF_NVIDIA_HARNESS_NUM_WARMUPS', '')
        if num_warmups != '':
            run_config += f" --num_warmups={num_warmups}"

        skip_postprocess = env.get('CM_MLPERF_NVIDIA_HARNESS_SKIP_POSTPROCESS')
        if skip_postprocess and skip_postprocess.lower() not in [ "no", "false" ]:
            run_config += f" --skip_postprocess"

        if test_mode:
            test_mode_string = " --test_mode={}".format(test_mode)
        else:
            test_mode_string = ""

        extra_build_engine_options_string = env.get('CM_MLPERF_NVIDIA_HARNESS_EXTRA_BUILD_ENGINE_OPTIONS', '')

        extra_run_options_string = env.get('CM_MLPERF_NVIDIA_HARNESS_EXTRA_RUN_OPTIONS', '') #will be ignored during build engine

        run_config += " --no_audit_verify"

        cmds.append(f"make {make_command} RUN_ARGS=' --benchmarks={model_name} --scenarios={scenario} {test_mode_string} {run_config} {extra_build_engine_options_string} {extra_run_options_string}'")

    run_cmd = " && ".join(cmds)
    env['CM_MLPERF_RUN_CMD'] = run_cmd
    env['CM_RUN_CMD'] = run_cmd
    env['CM_RUN_DIR'] = env['CM_MLPERF_INFERENCE_NVIDIA_CODE_PATH']

#    print(env)

    return {'return':0}

def postprocess(i):

    env = i['env']
    state = i['state']

    return {'return':0}
