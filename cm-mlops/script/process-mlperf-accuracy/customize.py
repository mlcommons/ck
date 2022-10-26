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
            CMD = env['CM_PYTHON_BIN'] + " '" + os.path.join(env['CM_MLPERF_INFERENCE_VISION_PATH'], "tools", \
                "accuracy-openimages.py") + "' --mlperf-accuracy-file '" + os.path.join(result_dir, \
                    "mlperf_log_accuracy.json") + "' --openimages-dir '" + env['CM_DATASET_PATH'] + "' > '" + \
                os.path.join(result_dir, "accuracy.txt") + "'"
        elif dataset == "imagenet":
            CMD = env['CM_PYTHON_BIN'] + " '" + os.path.join(env['CM_MLPERF_INFERENCE_VISION_PATH'], "tools",
                "accuracy-imagenet.py") + "' --mlperf-accuracy-file '" + os.path.join(result_dir,
                    "mlperf_log_accuracy.json") + "' --imagenet-val-file '" + os.path.join(env['CM_DATASET_AUX_PATH'],
                            "val.txt") + "' --dtype " + env['CM_ACCURACY_DTYPE'] +  " > '" + os.path.join(result_dir, "accuracy.txt") + "'"
        elif dataset == "squad":
            CMD = env['CM_PYTHON_BIN'] + " '" + os.path.join(env['CM_MLPERF_INFERENCE_BERT_PATH'],
                "accuracy-squad.py") + "' --val_data '" + env['CM_DATASET_SQUAD_VAL_PATH'] + \
                "' --log_file '" + os.path.join(result_dir, "mlperf_log_accuracy.json") + \
                "' --vocab_file '" + env['CM_ML_MODEL_BERT_VOCAB_FILE_WITH_PATH'] + \
                "' --out_file '" + os.path.join(result_dir, 'predictions.json') + \
                "' --output_dtype " + env['CM_ACCURACY_DTYPE'] + env.get('CM_OUTPUT_TRANSPOSED','') + max_examples_string + " > '" + os.path.join(result_dir, "accuracy.txt") + "'"
   
        run_cmds.append(CMD)

    env['CM_RUN_CMDS'] = "??".join(run_cmds)
    return {'return':0}

def postprocess(i):

    os_info = i['os_info']
    env = i['env']
    results_dir = env.get("CM_MLPERF_ACCURACY_RESULTS_DIR", "")
    results_dir_split = results_dir.split(":")
    for result_dir in results_dir_split:
        with open(os.path.join(result_dir, "accuracy.txt"), "r") as fp:
            print(fp.read())
    return {'return':0}

