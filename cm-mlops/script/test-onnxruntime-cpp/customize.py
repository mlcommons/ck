from cmind import utils
import os
import shutil

def preprocess(i):
    os_info = i['os_info']

    env = i['env']
    script_path=i['run_script_input']['path']

    env["CM_SOURCE_FOLDER_PATH"] = script_path
    env['CM_CXX_SOURCE_FILES'] = "main.cpp"
    env['CM_SOURCE_FOLDER_PATH'] = os.path.join(script_path, "src")

    if 'CM_RUN_DIR' not in env:
        env['CM_RUN_DIR'] = os.path.join(script_path, "output")
    
    if os_info['platform'] == 'windows':
        env['CM_BIN_NAME']='test-ort.exe'
    else:
        env['CM_BIN_NAME']='test-ort'
        env['+ LDCFLAGS'] = ["-lm"]

    # e.g. -lonnxruntime
    if env.get('CM_BACKEND','')=='onnxruntime':
        if '+ LDCXXFLAGS' not in env:
            env['+ LDCXXFLAGS'] = []
        env['+ LDCXXFLAGS'].append('-lonnxruntime')

    # On Windows we may need to copy onnxruntime.dll to the bin directory
    # otherwise the one from Windows sytem directory is always taken
    # even if we update the PATH!
    if os_info['platform'] == 'windows':
        path_to_onnx_dll = os.path.join(env['CM_ONNXRUNTIME_LIB_PATH'], 'onnxruntime.dll')

        shutil.copy(path_to_onnx_dll, 'output/onnxruntime.dll')

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
