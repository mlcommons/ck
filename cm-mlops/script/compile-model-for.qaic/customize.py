from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    if env.get('CM_REGISTER_CACHE', '') == '':

        r = construct_compilation_cmd(env)
        if r['return'] > 0:
            return r
        cmd = r['cmd']
    
        print("Compiling from "+ os.getcwd())

        env['CM_QAIC_MODEL_FINAL_COMPILATION_CMD'] = cmd

        env['CM_RUN_CMD'] = cmd
    else:
        import shutil
        print("Creating cache entry from " + env['CM_REGISTER_CACHE'] + " to "  + os.getcwd())
        r = shutil.copytree(env['CM_REGISTER_CACHE'], os.path.join(os.getcwd(), "elfs"))
        print(r)

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

    percentile_calibration_params = env.get('CM_QAIC_MODEL_COMPILER_QUANTIZATION_PARAMS')
    if percentile_calibration_params:
        compiler_params += " " + percentile_calibration_params

    aic_binary_dir = os.path.join(os.getcwd(), "elfs")

    cmd = env['CM_QAIC_EXEC_PATH']  + \
       " -model=" + env['CM_ML_MODEL_FILE_WITH_PATH'] + \
       profile_string + ' -aic-binary-dir=' + aic_binary_dir + ' ' \
       + compiler_params

    return {'return': 0, 'cmd': cmd}

def postprocess(i):

    env = i['env']
    env['CM_QAIC_MODEL_COMPILED_BINARY_WITH_PATH'] = os.path.join(os.getcwd(), "elfs", "programqpc.bin")
    if not os.path.isdir(os.path.join(os.getcwd(), "elfs")):
        return {'return': 1, 'error': 'elfs directory not found inside the compiled directory'}

    env['CM_ML_MODEL_FILE_WITH_PATH'] = env['CM_QAIC_MODEL_COMPILED_BINARY_WITH_PATH']

    return {'return':0}
