from cmind import utils
import cmind as cm
import os

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    results_dir = env.get("CM_MLC_RESULTS_DIR", "")
    if results_dir == "":
        print("Please set CM_MLC_RESULTS_DIR")
        exit(-1)
    CMD = env['CM_PYTHON_BIN'] + ' ' + os.path.join(env['CM_MLC_INFERENCE_VISION_PATH'], "tools",
            "accuracy-imagenet.py") + " --mlperf-accuracy-file " + os.path.join(results_dir, "mlperf_log_accuracy.json") + " --imagenet-val-file " + os.path.join(env['CM_DATASET_AUX_PATH'], "val.txt") + " > " + os.path.join(results_dir, "accuracy.txt")
    print(CMD)
    os.system(CMD)

    return {'return':0}
