from cmind import utils
import os
import json
import shutil
import subprocess
import cmind as cm

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    inp = i['input']
    state = i['state']
    script_path = i['run_script_input']['path']

    if env.get('CM_RUN_DOCKER_CONTAINER', '') == "yes": 
        return {'return':0}

    system_meta = state['CM_SUT_META']
    env['CM_SUT_META_EXISTS'] = "yes"

    if env.get('CM_MLPERF_SUBMISSION_SYSTEM_TYPE', '') != '':
        system_type = env['CM_MLPERF_SUBMISSION_SYSTEM_TYPE']
        system_meta['system_type'] = system_type

    if env.get('CM_MLPERF_SUBMISSION_DIVISION', '') != '':
        division = env['CM_MLPERF_SUBMISSION_DIVISION']
        system_meta['division'] = division

    if system_meta.get('division', '') != "closed":
        env["CM_MLPERF_LOADGEN_COMPLIANCE"] = "no" #no compliance runs needed for open division

    clean = False
    if 'CM_MLPERF_CLEAN_ALL' in env:
        clean = True
        if 'CM_MLPERF_CLEAN_SUBMISSION_DIR' not in env:
            env['CM_MLPERF_CLEAN_SUBMISSION_DIR'] = "yes"
        if 'CM_RERUN' not in env:
            env['CM_RERUN'] = "yes"

    if str(env.get('CM_SYSTEM_POWER','no')).lower() != "no":
        power_variation = ",_power"
        env['CM_SYSTEM_POWER'] = "yes"
    else:
        power_variation = ""

    if env.get('CM_RUN_STYLE', '') == "valid" and 'CM_RUN_MLPERF_ACCURACY' not in env:
        env['CM_RUN_MLPERF_ACCURACY'] = "on"

    print("Using MLCommons Inference source from " + env['CM_MLPERF_INFERENCE_SOURCE'])


    if 'CM_MLPERF_LOADGEN_EXTRA_OPTIONS' not in env:
        env['CM_MLPERF_LOADGEN_EXTRA_OPTIONS'] = ""

    if 'CM_MLPERF_LOADGEN_MODES' not in env:
        if 'CM_MLPERF_LOADGEN_MODE' not in env:
            env['CM_MLPERF_LOADGEN_MODE'] = "performance"

    if 'CM_MLPERF_LOADGEN_SCENARIOS' not in env:
        if 'CM_MLPERF_LOADGEN_SCENARIO' not in env:
            env['CM_MLPERF_LOADGEN_SCENARIO'] = "Offline"

    if env.get('CM_MLPERF_LOADGEN_ALL_SCENARIOS', '') == "yes":
        env['CM_MLPERF_LOADGEN_SCENARIOS'] = get_valid_scenarios(env['CM_MODEL'], system_meta['system_type'], env['CM_MLPERF_LAST_RELEASE'], env['CM_MLPERF_INFERENCE_SOURCE'])
    else:
        system_meta = {}
        env['CM_MLPERF_LOADGEN_SCENARIOS'] = [ env['CM_MLPERF_LOADGEN_SCENARIO'] ]

    if env.get('CM_MLPERF_LOADGEN_ALL_MODES', '') == "yes":
        env['CM_MLPERF_LOADGEN_MODES'] = [ "performance", "accuracy" ]
    else:
        env['CM_MLPERF_LOADGEN_MODES'] = [ env['CM_MLPERF_LOADGEN_MODE'] ]


    if 'OUTPUT_BASE_DIR' not in env:
        env['OUTPUT_BASE_DIR'] = os.getcwd()

    test_list = ["TEST01",  "TEST05"]
    if env['CM_MODEL']  in ["resnet50"]:
        test_list.append("TEST04")

    env['CM_MLPERF_DEVICE'] = env.get('CM_MLPERF_DEVICE', 'cpu')
    variation_implementation= "_" + env.get("CM_MLPERF_IMPLEMENTATION", "reference")
    variation_model= ",_" + env.get("CM_MLPERF_MODEL") if env.get("CM_MLPERF_MODEL","") != "" else ""
    variation_backend= ",_" + env.get("CM_MLPERF_BACKEND") if env.get("CM_MLPERF_BACKEND","") != "" else ""
    variation_device= ",_" + env.get("CM_MLPERF_DEVICE", "cpu") if env.get("CM_MLPERF_DEVICE","") != "" else ""
    variation_run_style= ",_" + env.get("CM_MLPERF_EXECUTION_MODE", "test")

    if env.get("CM_MLPERF_MODEL_PRECISION", '') != '':
        variation_quantization_string= ",_" + env["CM_MLPERF_MODEL_PRECISION"]
    else:
        variation_quantization_string = ""

    tags =  "app,mlperf,inference,generic,"+variation_implementation+variation_model+variation_backend+variation_device+variation_run_style+variation_quantization_string+power_variation
    silent = inp.get('silent', False)
    print_env = inp.get('print_env', False)
    print_deps = inp.get('print_deps', False)
    add_deps_recursive = i['run_script_input']['add_deps_recursive']
    add_deps = i.get('ad', {})

    if not add_deps:
        add_deps = i.get('add_deps')

    if clean and 'OUTPUT_BASE_DIR' in env:
        path_to_clean = os.path.join(env['OUTPUT_BASE_DIR'], env['CM_OUTPUT_FOLDER_NAME'])

        print ('=========================================================')
        print ('Cleaning results in {}'.format(path_to_clean))
        if os.path.exists(path_to_clean):
            shutil.rmtree(path_to_clean)

        print ('=========================================================')


    for scenario in env['CM_MLPERF_LOADGEN_SCENARIOS']:
        for mode in env['CM_MLPERF_LOADGEN_MODES']:
            env['CM_MLPERF_LOADGEN_SCENARIO'] = scenario
            env['CM_MLPERF_LOADGEN_MODE'] = mode

            if scenario == "Offline":
                if env.get('CM_MLPERF_LOADGEN_OFFLINE_TARGET_QPS'):
                    env['CM_MLPERF_LOADGEN_TARGET_QPS'] = env['CM_MLPERF_LOADGEN_OFFLINE_TARGET_QPS']
            elif scenario == "Server":
                if env.get('CM_MLPERF_LOADGEN_SERVER_TARGET_QPS'):
                    env['CM_MLPERF_LOADGEN_TARGET_QPS'] = env['CM_MLPERF_LOADGEN_SERVER_TARGET_QPS']
            elif scenario == "SingleStream":
                if env.get('CM_MLPERF_LOADGEN_SINGLESTREAM_TARGET_LATENCY'):
                    env['CM_MLPERF_LOADGEN_TARGET_LATENCY'] = env['CM_MLPERF_LOADGEN_SINGLESTREAM_TARGET_LATENCY']
            elif scenario == "MultiStream":
                if env.get('CM_MLPERF_LOADGEN_MULTISTREAM_TARGET_LATENCY'):
                    env['CM_MLPERF_LOADGEN_TARGET_LATENCY'] = env['CM_MLPERF_LOADGEN_MULTISTREAM_TARGET_LATENCY']

            r = cm.access({'action':'run', 'automation':'script', 'tags': tags, 'quiet': 'true',
                'env': env, 'input': inp, 'state': state, 'add_deps': add_deps, 'add_deps_recursive':
                add_deps_recursive, 'silent': silent, 'print_env': print_env, 'print_deps': print_deps})
            if r['return'] > 0:
                return r
            if 'CM_MLPERF_RESULTS_DIR' in r['new_env']:
                env['CM_MLPERF_RESULTS_DIR'] = r['new_env']['CM_MLPERF_RESULTS_DIR']
            if 'CM_MLPERF_BACKEND_VERSION' in r['new_env']:
                env['CM_MLPERF_BACKEND_VERSION'] = r['new_env']['CM_MLPERF_BACKEND_VERSION']

        if env.get("CM_MLPERF_LOADGEN_COMPLIANCE", "") == "yes":
            for test in test_list:
                env['CM_MLPERF_LOADGEN_COMPLIANCE_TEST'] = test
                env['CM_MLPERF_LOADGEN_MODE'] = "compliance"
                r = cm.access({'action':'run', 'automation':'script', 'tags': tags, 'quiet': 'true',
                    'env': env, 'input': inp, 'state': state, 'add_deps': add_deps, 'add_deps_recursive':
                    add_deps_recursive,'silent': silent, 'print_env': print_env, 'print_deps': print_deps})
                if r['return'] > 0:
                    return r

    return {'return':0}


def get_valid_scenarios(model, category, mlperf_version, mlperf_path):

    import sys
    
    submission_checker_dir = os.path.join(mlperf_path, "tools", "submission")

    sys.path.append(submission_checker_dir)
    if not os.path.exists(os.path.join(submission_checker_dir, "submission_checker.py")):
        shutil.copy(os.path.join(submission_checker_dir,"submission-checker.py"), os.path.join(submission_checker_dir,
        "submission_checker.py"))

    import submission_checker as checker

    config = checker.MODEL_CONFIG
    internal_model_name = config[mlperf_version]["model_mapping"].get(model, model)
    valid_scenarios = config[mlperf_version]["required-scenarios-"+category][internal_model_name]

    print("Valid Scenarios for " + model + " in " + category + " category are :" +  str(valid_scenarios))

    return valid_scenarios

def postprocess(i):
    return {'return':0}
