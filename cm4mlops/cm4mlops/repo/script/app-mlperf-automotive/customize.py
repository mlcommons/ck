from cmind import utils
import os
import json
import shutil
import subprocess
import mlperf_utils
from log_parser import MLPerfLog


def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    state = i['state']
    script_path = i['run_script_input']['path']

    if 'cmd' in i['input']:
        state['mlperf_inference_run_cmd'] = "cm run script " + \
            " ".join(i['input']['cmd'])

    state['mlperf-inference-implementation'] = {}

    run_state = i['run_script_input']['run_state']
    state['mlperf-inference-implementation']['script_id'] = run_state['script_id'] + \
        ":" + ",".join(run_state['script_variation_tags'])

    return {'return': 0}


def postprocess(i):

    env = i['env']
    state = i['state']

    inp = i['input']
    os_info = i['os_info']

    xsep = '^' if os_info['platform'] == 'windows' else '\\'

    env['CMD'] = ''

    # if env.get('CM_MLPERF_USER_CONF', '') == '':
    #    return {'return': 0}

    output_dir = env['CM_MLPERF_OUTPUT_DIR']
    mode = env['CM_MLPERF_LOADGEN_MODE']

    model = env['CM_MODEL']
    model_full_name = env.get('CM_ML_MODEL_FULL_NAME', model)

    scenario = env['CM_MLPERF_LOADGEN_SCENARIO']

    if not os.path.exists(output_dir) or not os.path.exists(
            os.path.join(output_dir, "mlperf_log_summary.txt")):
        # No output, fake_run?
        return {'return': 0}

    mlperf_log = MLPerfLog(os.path.join(output_dir, "mlperf_log_detail.txt"))
    if mode == "performance":
        result = mlperf_log['result_mean_latency_ns'] / 1000000
    elif mode == "accuracy":
        if not env.get(
                'CM_COGNATA_ACCURACY_DUMP_FILE'):  # can happen while reusing old runs
            env['CM_COGNATA_ACCURACY_DUMP_FILE'] = os.path.join(
                output_dir, "accuracy.txt")
        acc = ""
        if os.path.exists(env['CM_COGNATA_ACCURACY_DUMP_FILE']):
            with open(env['CM_COGNATA_ACCURACY_DUMP_FILE'], "r") as f:
                acc = f.readline()
        result = acc
    else:
        return {'return': 1, 'error': f"Unknown mode {mode}"}

    valid = {'performance': True, 'accuracy': True}  # its POC
    power_result = None  # No power measurement in POC

    # result, valid, power_result = mlperf_utils.get_result_from_log(env['CM_MLPERF_LAST_RELEASE'], model, scenario, output_dir, mode)

    if not state.get('cm-mlperf-inference-results'):
        state['cm-mlperf-inference-results'] = {}
    if not state.get('cm-mlperf-inference-results-last'):
        state['cm-mlperf-inference-results-last'] = {}
    if not state['cm-mlperf-inference-results'].get(
            state['CM_SUT_CONFIG_NAME']):
        state['cm-mlperf-inference-results'][state['CM_SUT_CONFIG_NAME']] = {}
    if not state['cm-mlperf-inference-results'][state['CM_SUT_CONFIG_NAME']
                                                ].get(model):
        state['cm-mlperf-inference-results'][state['CM_SUT_CONFIG_NAME']][model] = {}
    if not state['cm-mlperf-inference-results'][state['CM_SUT_CONFIG_NAME']
                                                ][model].get(scenario):
        state['cm-mlperf-inference-results'][state['CM_SUT_CONFIG_NAME']
                                             ][model][scenario] = {}

    state['cm-mlperf-inference-results'][state['CM_SUT_CONFIG_NAME']
                                         ][model][scenario][mode] = result
    state['cm-mlperf-inference-results'][state['CM_SUT_CONFIG_NAME']
                                         ][model][scenario][mode + '_valid'] = valid.get(mode, False)

    state['cm-mlperf-inference-results-last'][mode] = result
    state['cm-mlperf-inference-results-last'][mode +
                                              '_valid'] = valid.get(mode, False)

    return {'return': 0}
