from cmind import utils
import cmind as cm
import os

def postprocess(i):

    os_info = i['os_info']
    env = i['env']
    results_dir = env.get("CM_MLC_ACCURACY_RESULTS_DIR", "")
    if results_dir == "":
        print("Please set CM_MLC_ACCURACY_RESULTS_DIR")
        return {'return':-1}

    results_dir_split = results_dir.split(":")
    if 'CM_MAX_EXAMPLES' in env:
        max_examples_string = " --max_examples " + env['CM_MAX_EXAMPLES']
    else:
        max_examples_string = ""
    #"' --out_file '" + os.path.join(result_dir, env['CM_MLC_ACCURACY_OUTPUT_FILE']) + \
    for result_dir in results_dir_split:
        CMD = env['CM_PYTHON_BIN'] + " '" + os.path.join(env['CM_MLC_INFERENCE_BERT_PATH'],
            "accuracy-squad.py") + "' --val_data '" + env['CM_DATASET_SQUAD_VAL_PATH'] + \
            "' --log_file '" + os.path.join(result_dir, "mlperf_log_accuracy.json") + \
            "' --vocab_file '" + env['CM_ML_MODEL_BERT_VOCAB_FILE_WITH_PATH'] + \
            "' --out_file '" + os.path.join(result_dir, 'predictions.json') + \
            "' --output_dtype " + env['CM_ACCURACY_DTYPE'] + env.get('CM_OUTPUT_TRANSPOSED','') + max_examples_string + " > '" + os.path.join(result_dir, "accuracy.txt") + "'"
        print(CMD)
        ret = os.system(CMD)
        print("\n")
        with open(os.path.join(result_dir, "accuracy.txt"), "r") as fp:
            print(fp.read())

    return {'return':ret}
