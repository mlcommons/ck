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
    variation_reproducibility= ",_" + env["CM_RUN_MLPERF_INFERENCE_APP_DEFAULTS"] if env.get("CM_RUN_MLPERF_INFERENCE_APP_DEFAULTS","") != "" else ""

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
        if not add_deps_recursive.get('mlperf-inference-implementation', {}):
            add_deps_recursive['mlperf-inference-implementation'] = {}
        if add_deps_recursive['mlperf-inference-implementation'].get('tags', '') == '':
            add_deps_recursive['mlperf-inference-implementation']['tags'] = ''
        else:
            add_deps_recursive['mlperf-inference-implementation']['tags'] += ','
        add_deps_recursive['mlperf-inference-implementation']['tags'] += "_batch_size."+env['CM_MLPERF_LOADGEN_MAX_BATCHSIZE']

    if env.get('CM_MLPERF_INFERENCE_SUT_VARIATION', '') != '':
        if not add_deps_recursive.get('mlperf-inference-implementation', {}):
            add_deps_recursive['mlperf-inference-implementation'] = {}
        if add_deps_recursive['mlperf-inference-implementation'].get('tags', '') == '':
            add_deps_recursive['mlperf-inference-implementation']['tags'] = ''
        else:
            add_deps_recursive['mlperf-inference-implementation']['tags'] += ','
        add_deps_recursive['mlperf-inference-implementation']['tags'] += "_"+env['CM_MLPERF_INFERENCE_SUT_VARIATION']

    if env.get('CM_NETWORK_LOADGEN', '') != '':
        if not add_deps_recursive.get('mlperf-inference-implementation', {}):
            add_deps_recursive['mlperf-inference-implementation'] = {}
        network_variation_tag = f"_network-{env['CM_NETWORK_LOADGEN']}"
        if add_deps_recursive['mlperf-inference-implementation'].get('tags', '') == '':
            add_deps_recursive['mlperf-inference-implementation']['tags'] = ''
        else:
            add_deps_recursive['mlperf-inference-implementation']['tags'] += ','
        add_deps_recursive['mlperf-inference-implementation']['tags'] += network_variation_tag

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

    if str(env.get('CM_MLPERF_USE_DOCKER', '')).lower() in [ "1", "true", "yes"]:
        action = "docker"
        del(env['OUTPUT_BASE_DIR'])
        state = {}
        docker_extra_input = {}
        for k in inp:
            if k.startswith("docker_"):
                docker_extra_input[k] = inp[k]
        inp = {}
    else:
        action = "run"

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
            if action == "docker":
                for k in docker_extra_input:
                    ii[k] = docker_extra_input[k]
            r = cm.access(ii)
            if r['return'] > 0:
                return r

        if env.get("CM_MLPERF_LOADGEN_COMPLIANCE", "") == "yes":
            for test in test_list:
                env['CM_MLPERF_LOADGEN_COMPLIANCE_TEST'] = test
                env['CM_MLPERF_LOADGEN_MODE'] = "compliance"
                ii = {'action':action, 'automation':'script', 'tags': scenario_tags, 'quiet': 'true',
                    'env': copy.deepcopy(env), 'input': inp, 'state': state, 'add_deps': copy.deepcopy(add_deps), 'add_deps_recursive':
                    copy.deepcopy(add_deps_recursive), 'adr': copy.deepcopy(adr), 'ad': ad, 'v': verbose, 'print_env': print_env, 'print_deps': print_deps, 'dump_version_info': dump_version_info}
                if action == "docker":
                    for k in docker_extra_input:
                        ii[k] = docker_extra_input[k]
                r = cm.access(ii)
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

    env = i['env']
    state = i['state']

    if env.get('CM_MLPERF_IMPLEMENTATION', '') == 'reference':
        x1 = env.get('CM_MLPERF_INFERENCE_SOURCE','')
        x2 = env.get('CM_MLPERF_INFERENCE_CONF_PATH','')

        if x1 != '' and x2 != '':
            print ('')
            print ('Path to the MLPerf inference benchmark reference sources: {}'.format(x1))
            print ('Path to the MLPerf inference reference configuration file: {}'.format(x2))
            print ('')

    return {'return':0}

##################################################################################
def load_md(path, path2, name):

    fn = os.path.join(path, path2, name+'.md')

    s = ''

    if os.path.isfile(fn):
        r = utils.load_txt(fn)
        if r['return']>0: return r

        s = r['string']

    return {'return':0, 'string':s}

##################################################################################
def get_url(url, path, path2, name, text):

    name_md = name+'.md'
    fn = os.path.join(path, path2, name_md)

    urlx = ''
    url_online = ''
    if os.path.isfile(fn):
        if not url.endswith('/'): url+='/'
        urlx = url + path2 + '/' + name_md

        url_online = '[{}]({})'.format(text, urlx)

    return {'return':0, 'url_online':url_online}

##################################################################################
def gui(i):

    params = i['params']
    st = i['st']

    script_meta = i['meta']

    misc = i['misc_module']

    script_path = i['script_path']
    script_url = i.get('script_url','')
    script_tags = i.get('script_tags', '')

    compute_meta = i.get('compute_meta',{})
    compute_tags = compute_meta.get('tags', [])
    bench_meta = i.get('bench_meta',{})

    compute_uid = compute_meta.get('uid','')
    bench_uid = bench_meta.get('uid','')

    st_inputs_custom = {}
    
    bench_input = bench_meta.get('bench_input', {})

    end_html = ''

    extra = {}
    add_to_st_inputs = {}

    inp = script_meta['input_description']

    # Here we can update params
    v = compute_meta.get('mlperf_inference_device')
    if v!=None and v!='': 
        inp['device']['force'] = v

        if v in ['tpu', 'gaudi']:
            st.markdown('----')
            st.markdown('**WARNING: unified CM workflow support for this hardware is pending - please [feel free to help](https://discord.gg/JjWNWXKxwT)!**')
            return {'return':0, 'skip': True, 'end_html':end_html}

        elif 'orin' in compute_tags:
            st.markdown('----')
            st.markdown('**WARNING: we need to encode CM knowledge from [this Orin setp](https://github.com/mlcommons/ck/blob/master/docs/mlperf/setup/setup-nvidia-jetson-orin.md) to this GUI!**')
            return {'return':0, 'skip': True, 'end_html':end_html}

    st.markdown('---')
    st.markdown('**How would you like to run the MLPerf inference benchmark?**')

    r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_device', 'desc':inp['device']})
    device = r.get('value2')
    inp['device']['force'] = device

    

    if device == 'cpu':
        inp['implementation']['choices']=['mlcommons-python', 'mlcommons-cpp', 'intel', 'ctuning-cpp-tflite']
        if 'intel' in compute_tags:
            inp['implementation']['default']='intel'
        else:
            inp['implementation']['default']='mlcommons-python'
            inp['backend']['choices']=['onnxruntime','deepsparse','pytorch','tf','tvm-onnx']
            inp['backend']['default']='onnxruntime'
    elif device == 'rocm':
        inp['implementation']['force']='mlcommons-python'
        inp['precision']['force']=''
        inp['backend']['force']='onnxruntime'
        st.markdown('*WARNING: CM-MLPerf inference workflow was not tested thoroughly for AMD GPU - please feel free to test and improve!*')
    elif device == 'qaic':
        inp['implementation']['force']='qualcomm'
        inp['precision']['force']=''
        inp['backend']['force']='glow'


    r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_division', 'desc':inp['division']})
    division = r.get('value2')
    inp['division']['force'] = division


    y = 'compliance'
    if division=='closed':
        inp[y]['default'] = 'yes'
        r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_compliance', 'desc':inp[y]})
        compliance = r.get('value2')
        inp[y]['force'] = compliance

        if compliance == 'yes':
            st.markdown('*:red[See [online table with required compliance tests](https://github.com/mlcommons/policies/blob/master/submission_rules.adoc#5132-inference)].*')
        
    else:
        inp[y]['force'] = 'no'


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
            inp['implementation']['choices']=['nvidia','mlcommons-python','mlcommons-cpp']
            inp['implementation']['default']='nvidia'
            inp['backend']['choices']=['tensorrt','onnxruntime','pytorch']
            inp['backend']['default']='tensorrt'

    r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_implementation', 'desc':inp['implementation']})
    implementation = r.get('value2')
    inp['implementation']['force'] = implementation

    implementation_setup = ''
    r = load_md(script_path, 'setup', 'i-'+implementation)
    if r['return'] == 0: implementation_setup = r['string']

    url_faq_implementation = ''
    r = get_url(script_url, script_path, 'faq', implementation, 'FAQ online')
    if r['return'] == 0: url_faq_implementation = r['url_online']

    can_have_docker_flag = False

    if implementation == 'mlcommons-cpp':
#        inp['backend']['choices'] = ['onnxruntime']
        inp['precision']['force']='float32'
        inp['backend']['force'] = 'onnxruntime'
        inp['model']['choices'] = ['resnet50', 'retinanet']
        st.markdown('*:red[[CM automation recipe for this implementation](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-mlcommons-cpp)]*')
    elif implementation == 'mlcommons-python':
        inp['precision']['force']='float32'
        if device == 'cuda':
            inp['backend']['choices']=['onnxruntime','pytorch','tf']
            inp['backend']['default'] = 'onnxruntime'
        st.markdown('*:red[[CM automation recipe for this implementation](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-mlcommons-python)]*')
    elif implementation == 'ctuning-cpp-tflite':
        inp['precision']['force']='float32'
        inp['model']['force']='resnet50'
        st.markdown('*:red[[CM automation recipe for this implementation](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-ctuning-cpp-tflite)]*')
    elif implementation == 'nvidia':
        inp['backend']['force'] = 'tensorrt'
        extra['skip_script_docker_func'] = True
        can_have_docker_flag = True
        st.markdown('*:red[[CM automation recipe for this implementation](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-nvidia)]*')
    elif implementation == 'intel':
        inp['model']['choices'] = ['bert-99', 'gptj-99']
        inp['model']['default'] = 'bert-99'
        inp['precision']['choices'] = ['int8', 'int4']
        inp['precision']['default'] = 'int8'
        inp['category']['force'] = 'datacenter'
        inp['backend']['force'] = 'pytorch'
        inp['sut']['default'] = 'sapphire-rapids.112c'
        can_have_docker_flag = True
        extra['skip_script_docker_func'] = True
#        st.markdown('*:red[Note: Intel implementation require extra CM command to build and run Docker container - you will run CM commands to run MLPerf benchmarks there!]*')
        st.markdown('*:red[[CM automation recipe for this implementation](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-intel)]*')
    elif implementation == 'qualcomm':
        inp['model']['choices'] = ['resnet50', 'retinanet', 'bert-99']
        inp['model']['default'] = 'bert-99'
        inp['precision']['default'] = 'float16'
        extra['skip_script_docker_func'] = True
        st.markdown('*:red[[CM automation recipe for this implementation](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/reproduce-mlperf-inference-qualcomm)]*')


    #############################################################################
    # Backend

    r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_backend', 'desc':inp['backend']})
    backend = r.get('value2')
    inp['backend']['force'] = backend

    backend_setup = ''
    r = load_md(script_path, 'setup', 'b-'+backend)
    if r['return'] == 0: backend_setup = r['string']

    if backend == 'deepsparse':
        inp['model']['choices'] = ['resnet50', 'retinanet', 'bert-99', 'bert-99.9']
        inp['model']['default'] = 'bert-99'
        inp['precision']['choices'] = ['float32', 'int8']
        inp['precision']['default'] = 'int8'
        if 'force' in inp['precision']: del(inp['precision']['force'])



    #############################################################################
    # Model
    r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_model', 'desc':inp['model']})
    model = r.get('value2')
    inp['model']['force'] = model

    github_doc_model = ''

    if model == 'retinanet':
        x = '50'
        if implementation == 'mlcommons-python':
            x= '200'
        st.markdown(':red[This model requires ~{}GB of free disk space for preprocessed dataset in a full/submission run!]\n'.format(x))

    elif model.startswith('bert-'):
        github_doc_model = 'bert'

    elif model.startswith('3d-unet-'):
        github_doc_model = '3d-unet'

    elif model == 'rnnt':
        github_doc_model = 'rnnt'
    
    elif model.startswith('dlrm-v2-'):
        github_doc_model = 'dlrm_v2'
    
    elif model.startswith('gptj-'):
        github_doc_model = 'gpt-j'
    
    elif model == 'sdxl':
        github_doc_model = 'stable-diffusion-xl'
    
    elif model.startswith('llama2-'):
        github_doc_model = 'llama2-70b'

    if github_doc_model == '': github_doc_model = model
    
    model_cm_url='https://github.com/mlcommons/ck/tree/master/docs/mlperf/inference/{}'.format(github_doc_model)
    extra_notes_online = '[Extra notes online]({})\n'.format(model_cm_url)

    st.markdown('*[CM-MLPerf GitHub docs for this model]({})*'.format(model_cm_url))

    #############################################################################
    # Precision
    if implementation == 'intel':
        if model == 'bert-99':
            inp['precision']['force'] = 'int8'
        elif model == 'gptj-99':
            inp['precision']['force'] = 'int4'
    elif implementation == 'qualcomm':
        if model == 'resnet50':
            inp['precision']['print'] = 'int8'
        elif model == 'retinanet':
            inp['precision']['print'] = 'int8'
        elif model == 'bert-99':
            inp['precision']['print'] = 'int8/float16'

    if inp['precision'].get('force','')=='':
        x = inp['precision'].get('print','')
        if x!='':
            st.markdown('**{}**: {}'.format(inp['precision']['desc'], x))
    else:
        r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_precision', 'desc':inp['precision']})
        precision = r.get('value2')
        inp['precision']['force'] = precision

    #############################################################################
    # Benchmark version

    script_meta_variations = script_meta['variations']
    
    choices = [''] + [k for k in script_meta_variations if script_meta_variations[k].get('group','') == 'benchmark-version']
    desc = {'choices': choices, 'default':choices[0], 'desc':'Force specific benchmark version?'}
    r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_version', 'desc':desc})
    benchmark_version = r.get('value2')

    if benchmark_version!='':
        params['~~benchmark-version']=[benchmark_version]

    #############################################################################
    # Run via Docker container
    if can_have_docker_flag:

        default_choice = 'yes - run in container'
        
        choices = [default_choice, 'no - run natively'] 
        desc = {'choices': choices, 'default':choices[0], 'desc':'Should CM script prepare and run Docker container in interactive mode to run MLPerf? You can then copy/paste CM commands generated by this GUI to benchmark different models.'}
        r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_docker', 'desc':desc})
        benchmark_docker = r.get('value2')

        if benchmark_docker == 'yes - run in container':
            add_to_st_inputs['@docker']=True
            add_to_st_inputs['@docker_cache']='no'
    
    #############################################################################
    # Prepare submission
    st.markdown('---')

    submission = st.toggle('Would you like to prepare official submission?', value = False)
    if submission:
        r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_hw_name', 'desc':inp['hw_name']})
        inp['hw_name']['force'] = r.get('value2')

        r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_submitter', 'desc':inp['submitter']})
        submitter = r.get('value2')
        inp['submitter']['force'] = submitter

        params['~~submission-generation'] = ['submission']
        params['~all-scenarios'] = ['true']
        inp['scenario']['force'] = ''
        inp['clean']['default'] = False
        inp['repro']['force'] = True

        x  = '*:red[Use the following command to find local directory with the submission tree and results:]*\n```bash\ncm find cache --tags=submission,dir\n```\n'

        x += '*:red[You will also find results in `mlperf-inference-submission.tar.gz` file that you can submit to MLPerf!]*\n\n'

        x += '*:red[Note that if some results are INVALID due to too short run, you can rerun the same CM command and it should increase the length of the benchmark until you get valid result!]*\n'

        st.markdown(x)
    
        st.markdown('---')
    
    else:
        inp['submitter']['force']=''
        inp['clean']['default']=True
        params['~submission']=['false']

        choices = ['Performance', 'Accuracy', 'Find Performance from a short run', 'Performance and Accuracy']
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
        elif measure == 'Performance and Accuracy': 
            x = 'submission'
        
        params['~~submission-generation']=[x]

    
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



    #############################################################################
    # Power

#    desc = {'boolean':True, 'default':False, 'desc':'Measure power?'}
#    r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_power', 'desc':desc})
#    power = r.get('value2', False)

    power = st.toggle('Measure power consumption?', value = False)

    if power:
        inp['power']['force'] = 'yes'

        y = 'adr.mlperf-power-client.power_server'
        r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_power_server', 'desc':inp[y]})
        inp[y]['force'] = r.get('value2')

        y = 'adr.mlperf-power-client.port'
        r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_power_port', 'desc':inp[y]})
        inp[y]['force'] = r.get('value2')

        st.markdown('*:red[See [online notes](https://github.com/mlcommons/ck/blob/master/docs/tutorials/mlperf-inference-power-measurement.md)] to setup power meter and server.*')

    else:
        inp['power']['force'] = 'no'
        inp['adr.mlperf-power-client.power_server']['force']=''
        inp['adr.mlperf-power-client.port']['force']=''


    #############################################################################
    # Dashboard

#    desc = {'boolean':True, 'default':False, 'desc':'Output results to W&B dashboard?'}
#    r = misc.make_selector({'st':st, 'st_inputs':st_inputs_custom, 'params':params, 'key': 'mlperf_inference_dashboard', 'desc':desc})
#    dashboard = r.get('value2', False)

    dashboard = st.toggle('Output results to W&B dashboard?', value = False)
    
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



    
    # Hide customization by default
    params['hide_script_customization'] = True

    x = implementation_setup
    if backend_setup!='':
        if x != '': x+='\n\n'
        x+=backend_setup

    extra['extra_notes_online'] = extra_notes_online
    extra['extra_faq_online'] = url_faq_implementation
    extra['extra_setup'] = x

    #############################################################################
    value_reproduce = inp.get('repro',{}).get('force', False)
    reproduce = st.toggle('Record extra info for reproducibility?', value = value_reproduce)

    explore = st.toggle('Explore/tune benchmark (batch size, threads, etc)?', value = False)

    if reproduce or explore:
        add_to_st_inputs.update({
          "@repro_extra.run-mlperf-inference-app.bench_uid": bench_uid,
          "@repro_extra.run-mlperf-inference-app.compute_uid": compute_uid,
          '@results_dir':'{{CM_EXPERIMENT_PATH3}}',
          '@submission_dir':'{{CM_EXPERIMENT_PATH3}}'
        })
        
        inp['repro']['force'] = True
        extra['use_experiment'] = True

    if explore:
        add_to_st_inputs['@batch_size']='{{CM_EXPLORE_BATCH_SIZE{[1,2,4,8]}}}'

    #############################################################################
    debug = st.toggle('Debug and run MLPerf benchmark natively from command line after CM auto-generates CMD?', value=False)
    if debug:
        inp['debug']['force'] = True
      

    extra['add_to_st_inputs'] = add_to_st_inputs

    return {'return':0, 'end_html':end_html, 'extra':extra}
