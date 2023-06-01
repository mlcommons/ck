from cmind import utils
import cmind as cm
import os

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    results_dir = env.get("CM_MLPERF_ACCURACY_RESULTS_DIR", "")
    if results_dir == "":
        print("Please set CM_MLPERF_ACCURACY_RESULTS_DIR")
        return {'return':-1}
    run_cmds = []
    if 'CM_MAX_EXAMPLES' in env:
        max_examples_string = " --max_examples " + env['CM_MAX_EXAMPLES']
    else:
        max_examples_string = ""
    results_dir_split = results_dir.split(":")
    dataset = env['CM_DATASET']

    for result_dir in results_dir_split:

        if dataset == "openimages":
            env['DATASET_ANNOTATIONS_FILE_PATH'] = env['CM_DATASET_ANNOTATIONS_FILE_PATH']
            dataset_dir = env['CM_DATASET_PATH']
            CMD = env['CM_PYTHON_BIN_WITH_PATH'] + " '" + os.path.join(env['CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH'], "tools", \
                "accuracy-openimages.py") + "' --mlperf-accuracy-file '" + os.path.join(result_dir, \
                    "mlperf_log_accuracy.json") + "' --openimages-dir '" + dataset_dir + "' --verbose > '" + \
                os.path.join(result_dir, "accuracy.txt") + "'"

        elif dataset == "imagenet":
            CMD = env['CM_PYTHON_BIN_WITH_PATH'] + " '" + os.path.join(env['CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH'], "tools",
                "accuracy-imagenet.py") + "' --mlperf-accuracy-file '" + os.path.join(result_dir,
                    "mlperf_log_accuracy.json") + "' --imagenet-val-file '" + os.path.join(env['CM_DATASET_AUX_PATH'],
                            "val.txt") + "' --dtype " + env.get('CM_ACCURACY_DTYPE', "float32") +  " > '" + os.path.join(result_dir, "accuracy.txt") + "'"

        elif dataset == "squad":
            CMD = env['CM_PYTHON_BIN_WITH_PATH'] + " '" + os.path.join(env['CM_MLPERF_INFERENCE_BERT_PATH'],
                "accuracy-squad.py") + "' --val_data '" + env['CM_DATASET_SQUAD_VAL_PATH'] + \
                "' --log_file '" + os.path.join(result_dir, "mlperf_log_accuracy.json") + \
                "' --vocab_file '" + env['CM_ML_MODEL_BERT_VOCAB_FILE_WITH_PATH'] + \
                "' --out_file '" + os.path.join(result_dir, 'predictions.json') + \
                "' --output_dtype " + env['CM_ACCURACY_DTYPE'] + env.get('CM_OUTPUT_TRANSPOSED','') + max_examples_string + " > '" + os.path.join(result_dir, "accuracy.txt") + "'"

        elif dataset == "cnndm":
            CMD = env['CM_PYTHON_BIN_WITH_PATH'] + " '" + os.path.join(env['CM_MLPERF_INFERENCE_SOURCE'], "language", "gpt-j",
                "evaluation.py") + "' --mlperf-accuracy-file '" + os.path.join(result_dir, "mlperf_log_accuracy.json") + \
                "' --dataset-file '" + env['CM_DATASET_EVAL_PATH'] + "'"


        elif dataset == "kits19":
            CMD = env['CM_PYTHON_BIN_WITH_PATH'] + " '" + os.path.join(env['CM_MLPERF_INFERENCE_3DUNET_PATH'],
                "accuracy_kits.py") + \
                "' --preprocessed_data_dir '" + env['CM_DATASET_PREPROCESSED_PATH'] +\
                "' --postprocessed_data_dir '" + result_dir +\
                "' --log_file '" + os.path.join(result_dir, "mlperf_log_accuracy.json") + \
                "' --output_dtype " + env['CM_ACCURACY_DTYPE'] +" > '" + os.path.join(result_dir, "accuracy.txt") + "'"

        elif dataset == "librispeech":
            CMD = env['CM_PYTHON_BIN_WITH_PATH'] + " '" + os.path.join(env['CM_MLPERF_INFERENCE_RNNT_PATH'],
                "accuracy_eval.py") + \
                "' --dataset_dir '" + os.path.join(env['CM_DATASET_PREPROCESSED_PATH'], "..") +\
                "' --manifest '" + env['CM_DATASET_PREPROCESSED_JSON'] +\
                "' --log_dir '" + result_dir + \
                "' --output_dtype " + env['CM_ACCURACY_DTYPE'] +" > '" + os.path.join(result_dir, "accuracy.txt") + "'"

        elif dataset == "terabyte":
            CMD = env['CM_PYTHON_BIN_WITH_PATH'] + " '" + os.path.join(env['CM_MLPERF_INFERENCE_DLRM_PATH'], "tools",
                "accuracy-dlrm.py") + "' --mlperf-accuracy-file '" + os.path.join(result_dir,
                    "mlperf_log_accuracy.json") + \
                    "' --dtype " + env.get('CM_ACCURACY_DTYPE', "float32") +  " > '" + os.path.join(result_dir, "accuracy.txt") + "'"

        else:
            return {'return': 1, 'error': 'Unsupported dataset'}

        outfile = os.path.join(result_dir, "accuracy.txt")
        if not os.path.exists(outfile) or os.stat(outfile).st_size == 0 or env.get("CM_REGENERATE_MEASURE_FILES", False):
            run_cmds.append(CMD)

    env['CM_RUN_CMDS'] = "??".join(run_cmds)
    return {'return':0}

def postprocess(i):

    os_info = i['os_info']
    env = i['env']
    results_dir = env.get("CM_MLPERF_ACCURACY_RESULTS_DIR", "")
    results_dir_split = results_dir.split(":")
    for result_dir in results_dir_split:
        accuracy_file = os.path.join(result_dir, "accuracy.txt")
        if os.path.exists(accuracy_file):
            with open(accuracy_file, "r") as fp:
                print(fp.read())
    return {'return':0}

