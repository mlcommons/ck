from cmind import utils
import os
import sys
import yaml

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
    batchsize = env.get('CM_QAIC_MODEL_BATCH_SIZE', "1")
    cmd = env['CM_QAIC_EXEC_PATH']  + " "
    if env.get('CM_CREATE_INPUT_BATCH', '') == 'yes':
        cmd += " -input-list-file=batched_input_files  -batchsize="+batchsize + " "
    cmd += compiler_params + " -dump-profile=profile.yaml -model=" + env['CM_ML_MODEL_FILE_WITH_PATH']

    return {'return': 0, 'cmd': cmd}

def postprocess(i):

    env = i['env']
    profile_file_path = os.path.join(os.getcwd(), "profile.yaml")
    env['CM_QAIC_MODEL_PROFILE_WITH_PATH'] = profile_file_path

    if env.get('CM_ML_MODEL_INPUT_LAYER_NAME', '') != '':
        input_layer_names = [ env.get('CM_ML_MODEL_INPUT_LAYER_NAME') ]
    else:
        input_layer_names = [ "images:0", "images/:0" ]

    output_layer_names_conf = [ [], [] ]
    output_layer_names_loc = [ [], [] ]

    output_layer_names_loc[0] = [
        "/GatherElements/:0",
        "/GatherElements_1/:0",
        "/GatherElements_2/:0",
        "/GatherElements_3/:0",
        "/GatherElements_4/:0"
        ]

    output_layer_names_conf[0] = [
        "/TopK/:0",
        "/TopK_1/:0",
        "/TopK_2/:0",
        "/TopK_3/:0",
        "/TopK_4/:0"
        ]

    output_layer_names_loc[1] = [
    "GatherElements_588/:0",
    "GatherElements_598/:0",
    "GatherElements_608/:0",
    "GatherElements_618/:0",
    "GatherElements_628/:0"
    ]

    output_layer_names_conf[1] = [
            "TopK_570/:0",
            "TopK_572/:0",
            "TopK_574/:0",
            "TopK_576/:0",
            "TopK_578/:0"
            ]

    if env.get('CM_QAIC_MODEL_NAME', '') == "retinanet":
        with open(profile_file_path, "r") as stream:
            try:
                output_min_val_loc = sys.maxsize
                output_max_val_loc = -sys.maxsize
                output_min_val_conf = sys.maxsize
                output_max_val_conf = -sys.maxsize
                docs = yaml.load_all(stream, yaml.FullLoader)
                for doc in docs:
                    if type(doc) == list:

                        node_names = [ k['NodeOutputName'] for k in doc]
                        oindex = None

                        for output in output_layer_names_loc:
                            if output[0] in node_names:
                                oindex = output_layer_names_loc.index(output)
                                break

                        if oindex is None:
                            return {'return': 1, 'error': 'Output node names not found for the given retinanet model'}

                        for k in doc:
                            if k["NodeOutputName"] in input_layer_names:
                                min_val = k['Min']
                                max_val = k['Max']
                                scale, offset = get_scale_offset(min_val, max_val)
                                env['CM_QAIC_MODEL_RETINANET_IMAGE_SCALE'] = scale
                                env['CM_QAIC_MODEL_RETINANET_IMAGE_OFFSET'] = offset

                            if k["NodeOutputName"] in output_layer_names_loc[oindex]:
                                min_val = k['Min']
                                max_val = k['Max']
                                if min_val < output_min_val_loc:
                                    output_min_val_loc = min_val
                                if max_val > output_max_val_loc:
                                    output_max_val_loc = max_val
                                loc_scale, loc_offset = get_scale_offset(min_val, max_val)
                                index = output_layer_names_loc[oindex].index(k["NodeOutputName"])
                                env[f'CM_QAIC_MODEL_RETINANET_LOC_SCALE{index}'] = loc_scale
                                env[f'CM_QAIC_MODEL_RETINANET_LOC_OFFSET{index}'] = loc_offset - 128 # to uint8 is done in NMS code

                                total_range = max_val - min_val
                                scale = total_range/256.0
                                offset = round(-min_val / scale)

                            if k["NodeOutputName"] in output_layer_names_conf[oindex]:
                                min_val = k['Min']
                                max_val = k['Max']
                                if min_val < output_min_val_conf:
                                    output_min_val_conf = min_val
                                if max_val > output_max_val_conf:
                                    output_max_val_conf = max_val
                                conf_scale, conf_offset = get_scale_offset(min_val, max_val)
                                index = output_layer_names_conf[oindex].index(k["NodeOutputName"])
                                env[f'CM_QAIC_MODEL_RETINANET_CONF_SCALE{index}'] = conf_scale
                                env[f'CM_QAIC_MODEL_RETINANET_CONF_OFFSET{index}'] = conf_offset - 128 # to uint8 is done in NMS code
                                total_range = max_val - min_val
                                scale = total_range/256.0
                                offset = round(-min_val / scale)

                loc_scale, loc_offset = get_scale_offset(output_min_val_loc, output_max_val_loc)
                conf_scale, conf_offset = get_scale_offset(output_min_val_conf, output_max_val_conf)
                env['CM_QAIC_MODEL_RETINANET_LOC_SCALE'] = loc_scale
                env['CM_QAIC_MODEL_RETINANET_LOC_OFFSET'] = loc_offset - 128 # to uint8 is done in NMS code
                env['CM_QAIC_MODEL_RETINANET_CONF_SCALE'] = conf_scale
                env['CM_QAIC_MODEL_RETINANET_CONF_OFFSET'] = conf_offset - 128 # to uint8 is done in NMS code

            except yaml.YAMLError as exc:
                return {'return': 1, 'error': exc}

    return {'return':0}

def get_scale_offset(min_val, max_val):
    total_range = max_val - min_val
    scale = total_range/256.0
    offset = round(-min_val / scale)
    return scale, offset

