from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']
    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}
    env = i['env']
    script_path=i['run_script_input']['path']
    env["CM_SOURCE_FOLDER_PATH"] = script_path
    env['CM_C_SOURCE_FILES']="susan.c"
    env['CM_BIN_NAME']='image-corner'
    if 'CM_INPUT' not in env:
        env['CM_INPUT'] = os.path.join(script_path, 'data.pgm')
    if 'CM_OUTPUT' not in env:
        env['CM_OUTPUT'] = 'output_image_with_corners.pgm'
    if 'CM_RUN_DIR' not in env:
        env['CM_RUN_DIR'] = os.path.join(script_path, "output")
    env['CM_RUN_SUFFIX']= env['CM_INPUT'] + ' ' + env['CM_OUTPUT'] + ' '

    env['+ LDCFLAGS'] = ["-lm"]

    return {'return':0}

def postprocess(i):

    env = i['env']
    print(env['CM_OUTPUT'] + " generated in " + env['CM_RUN_DIR'])

    return {'return':0}
