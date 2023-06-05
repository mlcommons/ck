from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    if env.get("CM_TMP_ML_MODEL_TF2ONNX", "") == "yes":
        outputfile = env.get('CM_ML_MODEL_OUTFILE', 'model_quant.onnx')
        env['CM_RUN_CMD'] = env['CM_PYTHON_BIN_WITH_PATH'] + " -m tf2onnx.convert --tflite " + env['CM_ML_MODEL_FILE_WITH_PATH'] + " --output " + outputfile + " --inputs-as-nchw \"input_1_int8\""
        env['CM_ML_MODEL_FILE_WITH_PATH'] = os.path.join(os.getcwd(), outputfile)

    return {'return':0}

def postprocess(i):

    env = i['env']

    env['CM_ML_MODEL_FILE'] = os.path.basename(env['CM_ML_MODEL_FILE_WITH_PATH'])
    env['CM_GET_DEPENDENT_CACHED_PATH'] = env['CM_ML_MODEL_FILE_WITH_PATH']

    return {'return':0}

