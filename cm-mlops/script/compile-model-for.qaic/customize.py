from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    r = construct_compilation_cmd(env)
    if r['return'] > 0:
        return r
    cmd = r['cmd']
    
    print("Compiling from "+ os.getcwd())

    env['CM_RUN_CMD'] = cmd

    return {'return':0}

def construct_compilation_cmd(env):
    compiler_params_base = env['CM_QAIC_MODEL_COMPILER_PARAMS_BASE']
    compiler_args = env['CM_QAIC_MODEL_COMPILER_ARGS'] + ' ' + env.get('CM_QAIC_MODEL_COMPILER_ARGS_SUT', '')
    batchsize = env.get('CM_QAIC_MODEL_BATCH_SIZE')

    if env.get('CM_QAIC_MODEL_QUANTIZATION', '') == 'yes':
        profile_string = " -load-profile=" + env['CM_QAIC_MODEL_PROFILE_WITH_PATH']
    else:
        profile_string = ''

    compiler_params = compiler_params_base + ' ' + compiler_args
    if batchsize:
        compiler_params += " -batchsize="+batchsize

    aic_binary_dir = os.path.join(os.getcwd(), "elfs")

    cmd = env['CM_QAIC_EXEC_PATH']  + \
       " -model=" + env['CM_ML_MODEL_FILE_WITH_PATH'] + \
       profile_string + ' -aic-binary-dir=' + aic_binary_dir + ' ' \
       + compiler_params

    return {'return': 0, 'cmd': cmd}

def postprocess(i):

    env = i['env']
    env['CM_QAIC_MODEL_COMPILED_BINARY_WITH_PATH'] = os.path.join(os.getcwd(), "elfs", "programqpc.bin")
    env['CM_ML_MODEL_FILE_WITH_PATH'] = env['CM_QAIC_MODEL_COMPILED_BINARY_WITH_PATH']

    return {'return':0}
