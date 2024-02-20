from cmind import utils
import os
import cmind
import sys


def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    add_deps_recursive = i['input'].get('add_deps_recursive')

    adr = i['input'].get('adr')

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')
    verbose = (env.get('CM_VERBOSE', False) == 'yes')

    models = {
        "mobilenet": {
            "v1": {
                "multiplier": [ "multiplier-1.0", "multiplier-0.75", "multiplier-0.5", "multiplier-0.25" ],
                "resolution": [ "resolution-224", "resolution-192", "resolution-160", "resolution-128" ],
                "kind": [""]
                },
            "v2": {
                "multiplier": [ "multiplier-1.0", "multiplier-0.75", "multiplier-0.5", "multiplier-0.35" ],
                "resolution": [ "resolution-224", "resolution-192", "resolution-160", "resolution-128" ],
                "kind": [""]
                },
            "v3": {
                "multiplier": [""],
                "resolution": [""],
                "kind": [ "large", "large-minimalistic", "small", "small-minimalistic" ]
                }
            },
        "efficientnet": {
            "": {
                "multiplier": [""],
                "resolution": [""],
                "kind": [ "lite0", "lite1", "lite2", "lite3", "lite4" ]
                }
            }
        }
    variation_strings = {}
    for t1 in models:
        variation_strings[t1] = []
        variation_list = []
        variation_list.append(t1)
        for version in models[t1]:
            variation_list = []
            if version.strip():
                variation_list.append("_"+version)
            variation_list_saved = variation_list.copy()
            for k1 in models[t1][version]["multiplier"]:
                variation_list = variation_list_saved.copy()
                if k1.strip():
                    variation_list.append("_"+k1)
                variation_list_saved_2 = variation_list.copy()
                for k2 in models[t1][version]["resolution"]:
                    variation_list = variation_list_saved_2.copy()
                    if k2.strip():
                        variation_list.append("_"+k2)
                    variation_list_saved_3 = variation_list.copy()
                    for k3 in models[t1][version]["kind"]:
                        variation_list = variation_list_saved_3.copy()
                        if k3.strip():
                            variation_list.append("_"+k3)
                        variation_strings[t1].append(",".join(variation_list))

    if env.get('CM_MLPERF_POPULATE_README','') == "yes":
        var="_populate-readme"
        execution_mode="valid"
    elif env.get('CM_MLPERF_SUBMISSION_MODE','') == "yes":
        var="_submission"
        execution_mode="valid"
    elif env.get('CM_MLPERF_ACCURACY_MODE','') == "yes":
        var="_full,_accuracy-only"
        execution_mode="valid"
    elif env.get('CM_MLPERF_PERFORMANCE_MODE','') == "yes":
        var="_full,_performance-only"
        execution_mode="valid"
    else:
        var="_find-performance"
        execution_mode="test"

    precisions = [ ]
    if env.get('CM_MLPERF_RUN_FP32', '') == "yes":
        precisions.append("fp32")
    if env.get('CM_MLPERF_RUN_INT8', '') == "yes":
        precisions.append("uint8")

    implementation_tags = []
    if env.get('CM_MLPERF_USE_ARMNN_LIBRARY', '') == "yes":
        implementation_tags.append("_armnn")
    if env.get('CM_MLPERF_TFLITE_ARMNN_NEON', '') == "yes":
        implementation_tags.append("_use-neon")
    if env.get('CM_MLPERF_TFLITE_ARMNN_OPENCL', '') == "yes":
        implementation_tags.append("_use-opencl")
    implementation_tags_string = ",".join(implementation_tags)

    inp = i['input']

    for model in variation_strings:
        for v in variation_strings[model]:
            for precision in precisions:

                if "small-minimalistic" in v and precision == "uint8":
                    continue

                if model == "efficientnet" and precision == "uint8":
                    precision = "int8"

                cm_input = {
                    'action': 'run',
                    'automation': 'script',
                    'tags': f'generate-run-cmds,mlperf,inference,{var}',
                    'quiet': True,
                    'env': env,
                    'input': inp,
                    'v': verbose,
                    'implementation': 'tflite-cpp',
                    'precision': precision,
                    'model': model,
                    'scenario': 'SingleStream',
                    'execution_mode': execution_mode,
                    'test_query_count': '100',
                    'adr': {
                        'tflite-model': {
                            'tags': v
                        },
                        'mlperf-inference-implementation': {
                            'tags': implementation_tags_string
                        }
                    }
                }
                if add_deps_recursive:
                    cm_input['add_deps_recursive'] = add_deps_recursive #script automation will merge adr and add_deps_recursive

                if adr:
                    utils.merge_dicts({'dict1':cm_input['adr'], 'dict2':adr, 'append_lists':True, 'append_unique':True})

                if env.get('CM_MLPERF_INFERENCE_RESULTS_DIR', '') != '':
                    cm_input['results_dir'] = env['CM_MLPERF_INFERENCE_RESULTS_DIR']

                if env.get('CM_MLPERF_INFERENCE_SUBMISSION_DIR', '') != '':
                    cm_input['submission_dir'] = env['CM_MLPERF_INFERENCE_SUBMISSION_DIR']

                if env.get('CM_MLPERF_ACCURACY_MODE','') == "yes":
                    cm_input['mode'] = 'accuracy'

                if env.get('CM_MLPERF_PERFORMANCE_MODE','') == "yes":
                    cm_input['mode'] = 'performance'

                if env.get('CM_MLPERF_FIND_PERFORMANCE_MODE','') == "yes" and env.get('CM_MLPERF_NO_RERUN','') != 'yes':
                    cm_input['rerun'] = True

                if env.get('CM_MLPERF_POWER','') == "yes":
                    cm_input['power'] = 'yes'

                print(cm_input)
                r = cmind.access(cm_input)
                if r['return'] > 0:
                    return r

                if env.get('CM_TEST_ONE_RUN', '') == "yes":
                    return {'return':0}

        clean_input = {
                    'action': 'rm',
                    'automation': 'cache',
                    'tags': 'get,preprocessed,dataset,_for.mobilenet',
                    'quiet': True,
                    'v': verbose,
                    'f': 'True'
                }
        r = cmind.access(clean_input)
        #if r['return'] > 0:
        #    return r
    return {'return':0}

def postprocess(i):

    return {'return':0}
