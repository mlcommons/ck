from cmind import utils
import os
import json
import shutil
import subprocess
import cmind as cm
import copy
from tabulate import tabulate

summary_ext = ['.csv', '.json', '.xlsx']

##################################################################################
def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    inp = i['input']
    state = i['state']
    script_path = i['run_script_input']['path']

    if env.get('CM_RUN_DOCKER_CONTAINER', '') == "yes": 
        return {'return':0}

    dump_version_info = env.get('CM_DUMP_VERSION_INFO', True)
    system_meta = state['CM_SUT_META']
    env['CM_SUT_META_EXISTS'] = "yes"

    env['CM_MODEL'] = env['CM_MLPERF_MODEL']

    # Clean MLPerf inference output tar file if non-standard
    x=env.get('MLPERF_INFERENCE_SUBMISSION_TAR_FILE','')
    if x!='' and os.path.isfile(x):
        os.remove(x)

    # Clean MLPerf inference submission summary files
    x=env.get('MLPERF_INFERENCE_SUBMISSION_SUMMARY','')
    if x!='':
        for y in summary_ext:
            z = x+y
            if os.path.isfile(z):
                os.remove(z)

    if str(env.get('CM_MLPERF_USE_DOCKER', '')).lower() in [ "1", "true", "yes"]:
        action = "docker"
    else:
        action = "run"

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

    if str(env.get('CM_SYSTEM_POWER','no')).lower() != "no" or env.get('CM_MLPERF_POWER', '') == "yes":
        power_variation = ",_power"
        env['CM_MLPERF_POWER'] = "yes"
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

    if env.get('OUTPUT_BASE_DIR', '') == '':
        env['OUTPUT_BASE_DIR'] = env.get('CM_MLPERF_INFERENCE_RESULTS_DIR', os.getcwd())

    test_list = ["TEST01",  "TEST05"]
    if env['CM_MODEL']  in ["resnet50"]:
        test_list.append("TEST04")
    if "gpt" in env['CM_MODEL'] or "sdxl" in env['CM_MODEL'] or "llama2-70b" in env['CM_MODEL']:
        test_list.remove("TEST01")
        test_list.remove("TEST05")

    variation_implementation= "_" + env.get("CM_MLPERF_IMPLEMENTATION", "reference")
    variation_model= ",_" + env["CM_MLPERF_MODEL"]
    variation_backend= ",_" + env["CM_MLPERF_BACKEND"] if env.get("CM_MLPERF_BACKEND","") != "" else ""
    variation_device= ",_" + env["CM_MLPERF_DEVICE"] if env.get("CM_MLPERF_DEVICE","") != "" else ""
    variation_run_style= ",_" + env.get("CM_MLPERF_RUN_STYLE", "test")
    variation_reproducibility= ",_" + env["CM_RUN_MLPERF_INFERENCE_APP_DEFAULTS"]

    if env.get("CM_MLPERF_MODEL_PRECISION", '') != '':
        variation_quantization_string= ",_" + env["CM_MLPERF_MODEL_PRECISION"]
    else:
        variation_quantization_string = ""

    tags =  "app,mlperf,inference,generic,"+variation_implementation+variation_model+variation_backend+variation_device+variation_run_style+variation_reproducibility+variation_quantization_string+power_variation
    verbose = inp.get('v', False)
    print_env = inp.get('print_env', False)
    print_deps = inp.get('print_deps', False)
    add_deps_recursive = inp.get('add_deps_recursive', {})
    add_deps = inp.get('add_deps', {})
    ad = inp.get('ad', {})
    adr = inp.get('adr', {})
    adr_from_meta = i['run_script_input'].get('add_deps_recursive')

    for key in adr_from_meta:
        add_deps_recursive[key] = adr_from_meta[key]

    if env.get('CM_MLPERF_LOADGEN_MAX_BATCHSIZE', '') != '':
        add_deps_recursive['mlperf-inference-implementation'] = {}
        add_deps_recursive['mlperf-inference-implementation']['tags'] = "_batch_size."+env['CM_MLPERF_LOADGEN_MAX_BATCHSIZE']

    if env.get('CM_OUTPUT_FOLDER_NAME', '') == '':
        env['CM_OUTPUT_FOLDER_NAME'] =  env['CM_MLPERF_RUN_STYLE'] + "_results"

    output_dir = os.path.join(env['OUTPUT_BASE_DIR'], env['CM_OUTPUT_FOLDER_NAME'])
    if clean:
        path_to_clean = output_dir

        print ('=========================================================')
        print ('Cleaning results in {}'.format(path_to_clean))
        if os.path.exists(path_to_clean):
            shutil.rmtree(path_to_clean)

        print ('=========================================================')

    #local_keys = [ 'CM_MLPERF_SKIP_RUN', 'CM_MLPERF_LOADGEN_QUERY_COUNT', 'CM_MLPERF_LOADGEN_TARGET_QPS', 'CM_MLPERF_LOADGEN_TARGET_LATENCY' ]

    for scenario in env['CM_MLPERF_LOADGEN_SCENARIOS']:
        scenario_tags = tags + ",_"+scenario.lower()
        env['CM_MLPERF_LOADGEN_SCENARIO'] = scenario

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

        for mode in env['CM_MLPERF_LOADGEN_MODES']:
            env['CM_MLPERF_LOADGEN_MODE'] = mode

            print(f"\nRunning loadgen scenario: {scenario} and mode: {mode}")
            ii = {'action':action, 'automation':'script', 'tags': scenario_tags, 'quiet': 'true',
                'env': copy.deepcopy(env), 'input': inp, 'state': state, 'add_deps': copy.deepcopy(add_deps), 'add_deps_recursive':
                copy.deepcopy(add_deps_recursive), 'ad': ad, 'adr': copy.deepcopy(adr), 'v': verbose, 'print_env': print_env, 'print_deps': print_deps, 'dump_version_info': dump_version_info}
            r = cm.access(ii)
            if r['return'] > 0:
                return r

        if env.get("CM_MLPERF_LOADGEN_COMPLIANCE", "") == "yes":
            for test in test_list:
                env['CM_MLPERF_LOADGEN_COMPLIANCE_TEST'] = test
                env['CM_MLPERF_LOADGEN_MODE'] = "compliance"
                r = cm.access({'action':action, 'automation':'script', 'tags': scenario_tags, 'quiet': 'true',
                    'env': copy.deepcopy(env), 'input': inp, 'state': state, 'add_deps': copy.deepcopy(add_deps), 'add_deps_recursive':
                    copy.deepcopy(add_deps_recursive), 'adr': copy.deepcopy(adr), 'ad': ad, 'v': verbose, 'print_env': print_env, 'print_deps': print_deps, 'dump_version_info': dump_version_info})
                if r['return'] > 0:
                    return r

    if state.get("cm-mlperf-inference-results"):
        #print(state["cm-mlperf-inference-results"])
        for sut in state["cm-mlperf-inference-results"]:#only one sut will be there
            # Grigori: that may not work properly since customize may have another Python than MLPerf
            # (for example, if we use virtual env)
            import mlperf_utils

            print(sut)
            result_table, headers = mlperf_utils.get_result_table(state["cm-mlperf-inference-results"][sut])
            print(tabulate(result_table, headers = headers, tablefmt="pretty"))

            print(f"\nThe MLPerf inference results are stored at {output_dir}\n")

    return {'return':0}


def get_valid_scenarios(model, category, mlperf_version, mlperf_path):

    import sys
    
    submission_checker_dir = os.path.join(mlperf_path, "tools", "submission")

    sys.path.append(submission_checker_dir)
    if not os.path.exists(os.path.join(submission_checker_dir, "submission_checker.py")):
        shutil.copy(os.path.join(submission_checker_dir,"submission-checker.py"), os.path.join(submission_checker_dir,
        "submission_checker.py"))

    import submission_checker as checker

    if "dlrm-99" in model:
      model = model.replace("dlrm-99", "dlrm-v2-99")
    if "sdxl" in model:
      model = "stable-diffusion-xl"

    config = checker.MODEL_CONFIG

    internal_model_name = config[mlperf_version]["model_mapping"].get(model, model)

    valid_scenarios = config[mlperf_version]["required-scenarios-"+category][internal_model_name]

    print("Valid Scenarios for " + model + " in " + category + " category are :" +  str(valid_scenarios))

    return valid_scenarios

##################################################################################
def postprocess(i):

    return {'return':0}


##################################################################################
def gui(i):

    params = i['params']
    st = i['st']

    script_meta = i['meta']

    misc = i['misc_module']

    compute_meta = i.get('compute_meta',{})
    bench_meta = i.get('bench_meta',{})

    st_inputs_custom = {}
    
    bench_input = bench_meta.get('bench_input', {})

    end_html = ''

    inp = script_meta['input_description']

    # Here we can update params
    st.markdown('---')
    st.markdown('**How would you like to run the MLPerf inference benchmark?**')

    
    v = compute_meta.get('mlperf_inference_device')
    if v!=None and v!='': 
        inp['device']['force'] = v
    r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_device', 'desc':inp['device']})
    device = r.get('value2')
    inp['device']['force'] = device

    if device == 'cpu':
        inp['implementation']['choices']=['reference', 'intel-original','mil', 'tflite-cpp']
        inp['implementation']['default']='reference'
        inp['backend']['choices']=['onnxruntime','deepsparse','pytorch','tf','tvm-onnx']
        inp['backend']['default']='onnxruntime'
    elif device == 'rocm':
        inp['implementation']['force']='reference'
        inp['backend']['force']='onnxruntime'
    elif device == 'qaic':
        inp['implementation']['force']='qualcomm'
        inp['backend']['force']='glow'
       


    r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_division', 'desc':inp['division']})
    division = r.get('value2')
    inp['division']['force'] = division


    r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_category', 'desc':inp['category']})
    category = r.get('value2')
    inp['category']['force'] = category

    


    #############################################################################
    # Implementation
    v = bench_input.get('mlperf_inference_implementation')
    if v!=None and v!='': 
        inp['implementation']['force'] = v
    else:
        if device == 'cuda':
            inp['implementation']['choices']=['nvidia-original','reference','mil']
            inp['implementation']['default']='nvidia-original'
            inp['backend']['choices']=['tensorrt','onnxruntime','pytorch']
            inp['backend']['default']='tensorrt'

    r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_implementation', 'desc':inp['implementation']})
    implementation = r.get('value2')
    inp['implementation']['force'] = implementation

    if implementation == 'mil':
#        inp['backend']['choices'] = ['onnxruntime']
        inp['precision']['force']='float32'
        inp['backend']['force'] = 'onnxruntime'
        inp['model']['choices'] = ['resnet50', 'retinanet']
        st.markdown('*:red[[CM automation recipe for this implementation](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-cpp)]*')
    elif implementation == 'reference':
        inp['precision']['force']='float32'
        if device == 'cuda':
            inp['backend']['choices']=['onnxruntime','pytorch','tf']
            inp['backend']['default'] = 'onnxruntime'
        st.markdown('*:red[[CM automation recipe for this implementation](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-reference)]*')
    elif implementation == 'tflite-cpp':
        inp['precision']['force']='float32'
        inp['model']['force']='resnet50'
        st.markdown('*:red[[CM automation recipe for this implementation](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-tflite-cpp)]*')

    elif implementation == 'nvidia-original':
        inp['backend']['force'] = 'tensorrt'
        st.markdown("""
---
:red[Note: Nvidia implementation require extra CM command to build and run Docker container:]
```bash
cm docker script --tags=build,nvidia,inference,server
```
:red[You can then copy/paste CM commands generated by this GUI to run MLPerf benchmarks.]

:red[You can also benchmark all models in one go using this command:]
```bash
cmr "benchmark any _phoenix"
```

:red[Container will require around 60GB of free disk space.]
:red[Docker cache and running all models (without DLRM) will require ~600 GB free disk space.]

:red[Check these [notes](https://github.com/mlcommons/ck/blob/master/docs/mlperf/inference/bert/README_nvidia.md) for more details.]]

---
""")
        st.markdown('*:red[[CM automation recipe for this implementation](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-nvidia)]*')
    elif implementation == 'intel-original':
        inp['model']['choices'] = ['bert-99', 'bert-99.9', 'gptj-99']
        inp['model']['default'] = 'bert-99'
        inp['precision']['force'] = 'int8'
        inp['category']['force'] = 'datacenter'
        inp['backend']['force'] = 'pytorch'
        st.markdown('*:red[Note: Intel implementation require extra CM command to build and run Docker container - you will run CM commands to run MLPerf benchmarks there!]*')
        st.markdown('*:red[[CM automation recipe for this implementation](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-intel)]*')
    elif implementation == 'qualcomm':
        inp['model']['choices'] = ['resnet-50', 'retinanet', 'bert-99', 'bert-99.9']
        inp['model']['default'] = 'bert-99.9'
        inp['precision']['default'] = 'float16'
        st.markdown('*:red[[CM automation recipe for this implementation](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-qualcomm)]*')


    #############################################################################
    # Backend

    r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_backend', 'desc':inp['backend']})
    backend = r.get('value2')
    inp['backend']['force'] = backend


    if backend == 'deepsparse':
        inp['model']['choices'] = ['resnet50', 'retinanet', 'bert-99', 'bert-99.9']
        inp['model']['default'] = 'bert-99'
        inp['precision']['default'] = 'int8'



    r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_model', 'desc':inp['model']})
    model = r.get('value2')
    inp['model']['force'] = model

    if model == 'resnet50':
        st.markdown(':red[See [extra online notes](https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference/resnet50)]\n')

    elif model == 'retinanet':
        x = '50'
        if implementation == 'reference':
            x= '200'
        st.markdown(':red[This model requires ~{}GB of free disk space for preprocessed dataset in a full/submission run!]\n'.format(x))
        st.markdown(':red[See [extra online notes](https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference/retinanet)]\n')

    elif model.startswith('bert-'):
        st.markdown(':red[See [extra online notes](https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference/bert)]\n')

    elif model.startswith('3d-unet-'):
        st.markdown(':red[See [extra online notes](https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference/3d-unet)]\n')

    elif model == 'rnnt':
        st.markdown(':red[See [extra online notes](https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference/rnnt)]\n')
    
    elif model.startswith('dlrm-v2-'):
        st.markdown(':red[See [extra online notes](https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference/dlrm_v2)]\n')
    
    elif model.startswith('gptj-'):
        st.markdown(':red[See [extra online notes](https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference/gpt-j)]\n')
    
    elif model == 'sdxl':
        st.markdown(':red[See [extra online notes](https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference/stable-diffusion-xl)]\n')
    
    elif model.startswith('llama2-'):
        st.markdown(':red[See [extra online notes](https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference/llama2-70b)]\n')



    r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_precision', 'desc':inp['precision']})
    precision = r.get('value2')
    inp['precision']['force'] = precision


    #############################################################################
    # Prepare scenario

    xall = 'All applicable'
    choices = ['Offline', 'Server', 'SingleStream', 'MultiStream', xall]
    desc = {'choices':choices, 'default':choices[0], 'desc':'Which scenario(s)?'}
    r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_scenario', 'desc':desc})
    scenario = r.get('value2')


    if scenario == xall:
        params['~all-scenarios']=['true']
        inp['scenario']['force']=''
    else:
        inp['scenario']['force']=scenario



    #############################################################################
    # Prepare submission

    desc = {'boolean':True, 'default':False, 'desc':'Prepare submission?'}
    r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_submission', 'desc':desc})
    submission = r.get('value2')

    if submission:
        r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_submitter', 'desc':inp['submitter']})
        submitter = r.get('value2')
        inp['submitter']['force']=submitter
        params['~~submission-generation']=['submission']

        x = '*Use the following command to find local directory with the submission tree and results:*\n```bash\ncm find cache --tags=submission,dir\n```\n'

        x += '*You will also find results in `mlperf-inference-submission.tar.gz` file that you can submit to MLPerf!*'

        st.markdown(x)
    
    else:
        inp['submitter']['force']=''
        params['~submission']=['false']

        choices = ['Performance', 'Accuracy', 'Find Performance from a short run']
        desc = {'choices': choices, 'default':choices[0], 'desc':'What to measure?'}
        r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_measure', 'desc':desc})
        measure = r.get('value2')

        x = ''
        if measure == 'Performance': 
            x = 'performance-only'
        elif measure == 'Accuracy': 
            x = 'accuracy-only'
        elif measure == 'Find Performance from a short run': 
            x = 'find-performance'
        
        params['~~submission-generation']=[x]

        
    #############################################################################
    # Short or full run

    x = ['Full run', 'Short run']
    if submission:
        choices = [x[0], x[1]]
    else:
        choices = [x[1], x[0]]

    desc = {'choices':choices, 'default':choices[0], 'desc':'Short (test) or full (valid) run?'}
    r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_how', 'desc':desc})
    how = r.get('value2')

    if how == x[0]:
        params['~~submission-generation-style']=['full']
        inp['execution_mode']['force'] = 'valid'
    else:
        params['~~submission-generation-style']=['short']
        inp['execution_mode']['force'] = 'test'


    y = 'compliance'
    if division=='closed':
        r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_compliance', 'desc':inp[y]})
        inp[y]['force'] = r.get('value2')
    else:
        inp[y]['force'] = 'no'


    #############################################################################
    # Power

    desc = {'boolean':True, 'default':False, 'desc':'Measure power?'}
    r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_power', 'desc':desc})
    power = r.get('value2', False)

    if power:
        inp['power']['force'] = 'yes'

        y = 'adr.mlperf-power-client.power_server'
        r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_power_server', 'desc':inp[y]})
        inp[y]['force'] = r.get('value2')

        y = 'adr.mlperf-power-client.port'
        r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_power_port', 'desc':inp[y]})
        inp[y]['force'] = r.get('value2')

    else:
        inp['power']['force'] = 'no'
        inp['adr.mlperf-power-client.power_server']['force']=''
        inp['adr.mlperf-power-client.port']['force']=''


    #############################################################################
    # Dashboard

    desc = {'boolean':True, 'default':False, 'desc':'Output results to W&B dashboard?'}
    r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_dashboard', 'desc':desc})
    dashboard = r.get('value2', False)

    if dashboard:
        params['~dashboard']=['true']

        y = 'dashboard_wb_project'
        r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_power_wb_project', 'desc':inp[y]})
        inp[y]['force'] = r.get('value2')

        y = 'dashboard_wb_user'
        r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_power_wb_user', 'desc':inp[y]})
        inp[y]['force'] = r.get('value2')

    else:
        params['~dashboard']=['false']
        inp['dashboard_wb_project']['force']=''
        inp['dashboard_wb_user']['force']=''


#    params['@adr.mlperf-power-client.port']=['']
#    inp['device']['choices']=['rocm','qaic']
#    inp['device']['default']='qaic'
    
    return {'return':0, 'end_html':end_html}
