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
    results_dir_split = results_dir.split(":")
    for result_dir in results_dir_split:
        CMD = env['CM_PYTHON_BIN'] + " '" + os.path.join(env['CM_MLPERF_INFERENCE_VISION_PATH'], "tools", \
            "accuracy-openimages.py") + "' --mlperf-accuracy-file '" + os.path.join(result_dir, \
                    "mlperf_log_accuracy.json") + "' --openimages-dir '" + env['CM_DATASET_PATH'] + "' > '" + \
            os.path.join(result_dir, "accuracy.txt") + "'"
        run_cmds.append(CMD)

    env['RUN_CMDS'] = "??".join(run_cmds)
    return {'return':0}

def postprocess(i):

    os_info = i['os_info']
    env = i['env']
    results_dir = env.get("CM_MLPERF_ACCURACY_RESULTS_DIR", "")
    for result_dir in results_dir_split:
        with open(os.path.join(result_dir, "accuracy.txt"), "r") as fp:
            print(fp.read())
    return {'return':0}

