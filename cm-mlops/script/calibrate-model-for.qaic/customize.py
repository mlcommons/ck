from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    if env.get('CM_CREATE_INPUT_BATCH', '') == 'yes':
        r = create_batched_inputs(env)
        if r['return'] > 0:
            return r

    r = construct_calibration_cmd(env)
    if r['return'] > 0:
        return r
    cmd = r['cmd']
    
    print("Profiling from "+ os.getcwd())

    env['CM_RUN_CMD'] = cmd

    return {'return':0}

def create_batched_inputs(env):
    original_images_file = env['CM_DATASET_PREPROCESSED_IMAGES_LIST']
    batchsize = env['CM_QAIC_MODEL_BATCH_SIZE']

    file_paths = []
    with open(original_images_file) as f:
        file_paths = f.read().splitlines()

    i = 0;
    outfile = None
    lastfile = None
    outfiles = []
    os.makedirs(os.path.join(os.getcwd(),"raw"), exist_ok = True)
    for file in file_paths:
        if i%int(batchsize) == 0:
            filename = os.path.basename(file).replace(".rgb32", ".raw")
            outfile = os.path.join(os.getcwd(),"raw", filename)
            outfiles.append(outfile)
            with open(outfile, "wb") as f:
                pass
        with open(outfile, "ab") as f:
            with open(file, "rb") as infile:
                f.write(infile.read())
        i = i+1
        lastfile = file

    while i%int(batchsize) != 0:
        with open(outfile, "ab") as f:
            with open(lastfile, "rb") as infile:
                f.write(infile.read())
        i = i+1
    with open("batched_input_files", "w") as f:
        f.write("\n".join(outfiles))

    return {'return': 0}

def construct_calibration_cmd(env):
    compiler_params = env['CM_QAIC_COMPILER_PARAMS']
    batchsize = env['CM_QAIC_MODEL_BATCH_SIZE']
    cmd = env['CM_QAIC_EXEC_PATH']  + " "
    if env.get('CM_CREATE_INPUT_BATCH', '') == 'yes':
        cmd += " -input-list-file=batched_input_files  -batchsize="+batchsize + " "
    cmd += compiler_params + " -dump-profile=profile.yaml -model=" + env['CM_ML_MODEL_FILE_WITH_PATH']

    return {'return': 0, 'cmd': cmd}

def postprocess(i):

    env = i['env']
    env['CM_QAIC_MODEL_PROFILE_WITH_PATH'] = os.path.join(os.getcwd(), "profile.yaml")

    return {'return':0}
