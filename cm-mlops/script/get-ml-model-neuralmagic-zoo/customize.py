from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']
   
    automation = i['automation']

    cm = automation.cmind

    path = os.getcwd()

    model_stub = env.get('CM_MODEL_ZOO_STUB', '')
    if model_stub == '':

        variations = list(i.get('meta', {}).get('variations',{}).keys())

        variation_models = []
        for v in variations:
            if '#' not in v:
                variation_models.append(v)
        
        return {'return':1, 'error':'ENV CM_MODEL_ZOO_STUB is not set. Please select variation from {}'.format(str(variation_models))}

    return {'return':0}

def postprocess(i):

    os_info = i['os_info']

    env = i['env']
    
    env['CM_GET_DEPENDENT_CACHED_PATH'] = env['CM_ML_MODEL_FILE_WITH_PATH']

    onnx_path = os.path.join(env['CM_ML_MODEL_FILE_WITH_PATH'], "model.onnx")

    if os.path.exists(onnx_path):
        env['CM_MLPERF_CUSTOM_MODEL_PATH'] = onnx_path

    return {'return':0}
