from cmind import utils
import os
import json
import shutil

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    script_path = i['run_script_input']['path']
    if 'CM_LOADGEN_EXTRA_OPTIONS' not in env:
        env['CM_LOADGEN_EXTRA_OPTIONS'] = ""
    if 'CM_LOADGEN_MODE' not in env:
        env['CM_LOADGEN_MODE'] = "performance"
    elif env['CM_LOADGEN_MODE'] == "accuracy":
        env['CM_LOADGEN_EXTRA_OPTIONS'] += " --accuracy"

    if 'CM_LOADGEN_QPS' not in env:
        env['CM_LOADGEN_QPS_OPT'] = ""
    else:
        env['CM_LOADGEN_QPS_OPT'] = " --qps " + env['CM_LOADGEN_QPS']
    if 'CM_LOADGEN_SCENARIO' not in env:
        env['CM_LOADGEN_SCENARIO'] = "Offline"
    env['CM_LOADGEN_EXTRA_OPTIONS'] +=  env['CM_LOADGEN_QPS_OPT']
    if 'OUTPUT_BASE_DIR' not in env:
        env['OUTPUT_BASE_DIR'] = env['CM_MLC_INFERENCE_VISION_PATH']
    if 'output_dir' in i['input']:
        env['OUTPUT_BASE_DIR'] = i['input']['output_dir']
    if 'OUTPUT_DIR' not in env:
        env['OUTPUT_DIR'] =  os.path.join(env['OUTPUT_BASE_DIR'], env['CM_OUTPUT_FOLDER_NAME'], env['CM_BACKEND'] + "-" + env['CM_DEVICE'], env['CM_MODEL'],
        env['CM_LOADGEN_SCENARIO'].lower(), env['CM_LOADGEN_MODE'])

    if 'CM_NUM_THREADS' not in env:
        if 'CM_MINIMIZE_THREADS' in env:
            env['CM_NUM_THREADS'] = str(int(env['CM_CPUINFO_CPUs']) // (int(env['CM_CPUINFO_Sockets']) * int(env['CM_CPUINFO_Threads_per_core']) ))
        else:
            env['CM_NUM_THREADS'] = str(int(env['CM_CPUINFO_CPUs']))

    if env['CM_LOADGEN_SCENARIO'] == "SingleStream":
        env['CM_NUM_THREADS'] = "1"
    if env['CM_LOADGEN_SCENARIO'] == "MultiStream":
        if int(env['CM_NUM_THREADS']) > 8:
            env['CM_NUM_THREADS'] = "8"

    if 'threads' in i['input']: #input overrides everything
        env['CM_NUM_THREADS'] = i['input']['threads']

    env['CM_LOADGEN_EXTRA_OPTIONS'] +=  " --threads " + env['CM_NUM_THREADS']

    if 'max-batchsize' in i['input']:
        env['CM_LOADGEN_EXTRA_OPTIONS'] += " --max-batchsize " + i['input']['max-batchsize']

    if 'CM_MLC_MLPERF_CONF' not in env:
        env['CM_MLC_MLPERF_CONF'] = os.path.join(env['CM_MLC_INFERENCE_SOURCE'], "mlperf.conf")

    conf = i['state']['CM_SUT_CONFIG'][env['CM_SUT_NAME']][env['CM_MODEL']][env['CM_LOADGEN_SCENARIO']]
    user_conf = ''
    for metric in conf:
        user_conf += env['CM_MODEL'] + "." + env['CM_LOADGEN_SCENARIO'] + "." + metric + " = " + str(conf[metric]) + "\n"
    if env['CM_LOADGEN_SCENARIO'] == "MultiStream":
        query_count = str(int((8000 / float(conf['target_latency'])) * 630))
        user_conf += env['CM_MODEL'] + "." + env['CM_LOADGEN_SCENARIO'] + ".max_query_count = " + query_count + "\n"
        user_conf += env['CM_MODEL'] + "." + env['CM_LOADGEN_SCENARIO'] + ".min_query_count = " + query_count + "\n"
    print(user_conf)

    import uuid
    key = uuid.uuid4().hex
    user_conf_path = os.path.join(script_path, "tmp", key+".conf")
    from pathlib import Path
    user_conf_file = Path(user_conf_path)
    user_conf_file.parent.mkdir(exist_ok=True, parents=True)
    user_conf_file.write_text(user_conf)
    env['CM_MLC_USER_CONF'] = user_conf_path

    env['CM_LOADGEN_EXTRA_OPTIONS'] +=  " --mlperf_conf " + env['CM_MLC_MLPERF_CONF']
    env['CM_LOADGEN_EXTRA_OPTIONS'] +=  " --user_conf " + env['CM_MLC_USER_CONF']

    return {'return':0}

def postprocess(i):
    env = i['env']
 
    measurements = {}
    measurements['retraining'] = env.get('CM_MODEL_RETRAINING','')
    measurements['starting_weights_filename'] = env.get('CM_STARTING_WEIGHTS_FILENAME', 'none')
    measurements['input_data_types'] = env.get('CM_MODEL_INPUT_DATA_TYPES', 'fp32')
    measurements['weight_data_types'] = env.get('CM_MODEL_WEIGHT_DATA_TYPES', 'fp32')
    measurements['weight_transformations'] = env.get('CM_MODEL_WEIGHT_TRANSFORMATIONS', 'none')
    os.chdir(env['OUTPUT_DIR'])
    with open ("measurements.json", "w") as fp:
        json.dump(measurements, fp, indent=2)
    if os.path.exists(env['CM_MLC_MLPERF_CONF']):
        shutil.copy(env['CM_MLC_MLPERF_CONF'], 'mlperf.conf')
    if os.path.exists(env['CM_MLC_USER_CONF']):
        shutil.copy(env['CM_MLC_USER_CONF'], 'user.conf')
    env['CM_MLC_RESULTS_DIR'] = env['OUTPUT_DIR']
    readme_init = ""
    readme_body = "##\n```\n" + env['CM_MLC_RUN_CMD'] + "\n```"
    readme = readme_init + readme_body
    with open ("README.md", "w") as fp:
        fp.write(readme)


    return {'return':0}
