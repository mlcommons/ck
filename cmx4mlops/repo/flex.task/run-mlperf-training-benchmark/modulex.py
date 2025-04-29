# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy
import shutil

def run(i):

    misc = i['misc']
    cmind = i['cmind']
    state = i['state']
    tmp = i['tmp']

    cmx = state['cmx']

    out = misc.get('out', '')
    console = misc.get('console', False)

    self_meta = misc['meta']
    self_path = misc['path']

    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)
    quiet = _input2.get('quiet', False)

    new = _input2.get('new', False)
    renew = _input2.get('renew', False)

    env = _input2.get('env', {})

    _input = i['input']

    code_tags = _input.get('code_tags', '')
    code_artifact = _input.get('code_name', '')

    code_version = _input.get('code_version', '')
    mlperf_version = _input.get('mlperf_version', '')

    model_tags = _input.get('model_tags', '')
    model_artifact = _input.get('model_name', '')

    dataset_tags = _input.get('dataset_tags', '')
    dataset_artifact = _input.get('dataset_name', '')

    params = _input.get('params', {})

    config_name = _input.get('config_name', '')
    config = _input.get('config', {})

    build = _input.get('build', False)

    path_to_output = _input.get('output_dir', 'output')
    path_to_results = _input.get('results_dir', 'results')
    path_to_code = _input.get('code_dir', 'benchmarks')
    path_to_systems = _input.get('systems_dir', 'systems')

    target_device = state['cmx']['use_compute']['target_device']
    pytorch_target_device = state['cmx']['use_compute']['target_pytorch_device']

    cmd_prefix_from_state_compile = self_meta.get('cmd_prefix_from_state_compile', [])

    max_experiments = _input.get('max_experiments', None)
    if max_experiments == '': max_experiments = None

    clean = _input.get('clean', False)

    clean_os_kernel_cache = _input.get('clean_os_kernel_cache', False)

    target_system_extra_name = _input.get('target_system_extra_name', '')

    seed = _input.get('seed', '')
    random_seed = _input.get('random_seed', False)

    package_checker_extra_flags = _input.get('package_checker_extra_flags', '')

    mllog_stop_if_fail = _input.get('mllog_stop_if_fail', False)

    system_division = _input.get('system_division', '')
    system_status = _input.get('system_status', '')
    submitter = _input.get('submitter', '')

    system_desc = _input.get('system_desc', {})

    ######################################################
    # Select flex.code

    code_choices = {}
    if code_version != '': code_choices['code_version'] = code_version
    code_choices['target_compute'] = target_device
    code_choices['target_pytorch_device'] = pytorch_target_device

    if code_tags == '': code_tags = self_meta.get('code_tags', '')
    if code_artifact == '': code_artifact = self_meta.get('code_name', '')

    r = cmind.x({'automation': self_meta['use']['flex.common'],
                 'action': 'select_artifact',
                 'selected_text': 'Select benchmark implementation',
                 'selected_automation': self_meta['use']['flex.code'],
                 'selected_artifact': code_artifact,
                 'selected_tags': code_tags,
                 'selected_choices': code_choices,
                 'quiet': quiet,
                 'control':{'out':out}})

    if r['return']>0: return cmind.embed_error(r)

    code_object = r['selected_artifact_object']

    code_meta = code_object.meta
    code_path = code_object.path

    if code_version == '' and code_meta.get('default_code_version', '') != '':
        code_version = code_meta['default_code_version']

    code_path_with_version = code_path if code_version == '' else os.path.join(code_path, code_version)

    # Check if there is extra meta code
    code_extra_meta_file = os.path.join(code_path_with_version, '_desc.yaml')
    if os.path.isfile(code_extra_meta_file):
        r = utils.load_yaml(code_extra_meta_file)
        if r['return']>0: return cmind.embed_error(r)
        utils.merge_dicts({'dict1':code_meta, 'dict2':r['meta']})#, 'append_lists':True, 'append_unique':True})

    copy_code = code_meta.get('copy_code', False)

    mlperf_implementation = code_meta.get('mlperf_implementation', 'ref')

    if verbose:
        print ('')
        print (f'Selected flex.code in {code_path}')

    ######################################################
    # Check code deps
    deps = code_meta.get('deps', {})

    tmp = {}
    if len(deps)>0:
        process_deps = misc['helpers']['process_deps']

        r = process_deps(cmind, deps, state, misc['flex.task'],
                         verbose = verbose, console = console, quiet = quiet,
                         tmp = tmp)
        if r['return'] >0: return r

    ######################################################
    # Use model
    model_deps = [{'tags':'use,flex,model',
                   'name':model_artifact,
                   'model_tags':model_tags,
                   'alias':'use-model'}]

    model_tmp = {}
    r = process_deps(cmind, model_deps, state, misc['flex.task'],
                     verbose = verbose, console = console, quiet = quiet,
                     tmp = {})
    if r['return'] >0: return r
    model_tmp = r['tmp']

    model_meta = model_tmp['_cmx_model_meta']

    mlperf_model_name = model_meta['mlperf_model_name']

    path_to_model = model_tmp['path_to_model']

    ######################################################
    # Use dataset
    ii = {'tags':'use,flex,dataset',
          'alias':'use-dataset'}

    if 'dataset_meta' in model_meta:
        ii.update(model_meta['dataset_meta'])

    if dataset_artifact != '': ii['name'] = dataset_artifact
    if dataset_tags != '': ii['dataset_tags'] = dataset_tags

    dataset_deps = [ii]

    dataset_tmp = {}
    r = process_deps(cmind, dataset_deps, state, misc['flex.task'],
                     verbose = verbose, console = console, quiet = quiet,
                     tmp = {})
    if r['return'] >0: return r
    dataset_tmp = r['tmp']

    dataset_meta = dataset_tmp['_cmx_dataset_meta']

    path_to_dataset = dataset_tmp['path_to_dataset']



    ########################################################
    # Prepare/copy benchmark code
    path_to_code_implementation = os.path.join(path_to_code, mlperf_model_name, 'implementations', mlperf_implementation)

    if not os.path.isdir(path_to_code_implementation):
        if copy_code:
            if verbose:
                print ('')
                print (f'Copying benchmark code to {path_to_code_implementation}')

            shutil.copytree(code_path_with_version, path_to_code_implementation)

            code_path_with_version = path_to_code_implementation

        else:
            if verbose:
                print ('')
                print (f'Creating benchmark code dir: {path_to_code_implementation}')

            os.makedirs(path_to_code_implementation)

    ######################################################
    # Extra paths

    train_code = code_meta.get('train_code','')
    if train_code == '': train_code = os.path.join('scripts', 'train.py')
    train_code_path_with_version = os.path.join(code_path_with_version, train_code)

    if config_name == '': config_name = code_meta.get('default_config_name', '')

    x = 'train.yaml' if config_name == '' else f'train_{config_name}.yaml'
    config_path_with_version = os.path.join(code_path_with_version, 'configs', x)

    x = 'cmd.yaml' if config_name == '' else f'cmd_{config_name}.yaml'
    cmd_path_with_version = os.path.join(code_path_with_version, 'configs', x)

    ######################################################
    # Attempt to load default configs

    r = utils.load_yaml(config_path_with_version)
    if r['return'] >0: return cmind.embed_error(r)
    config_meta = r['meta']

    if len(config)>0:
        config_meta.update(config)

    r = utils.load_yaml(cmd_path_with_version)
    if r['return'] >0: return cmind.embed_error(r)
    cmd_meta = r['meta']

    if len(params)>0:
        cmd_meta.update(params)

    if seed != '':
        cmd_meta['seed'] = seed


    ######################################################
    # Save config and state
    rt_config_file = 'cmx-rt-config.yaml'
    r = utils.save_yaml(rt_config_file, config_meta)
    if r['return']>0: return cmind.embed_error(r)

    # Save config and state
    r = utils.save_json('cmx-rt-state.json', {'state':state})
    if r['return']>0: return cmind.embed_error(r)

    # Save versions from the state
    r = utils.save_json('cmx-rt-versions.json', {'state':{'flow':state['cmx']['flow']}})
    if r['return']>0: return cmind.embed_error(r)

    ######################################################
    # Check working directories
    if clean:
        # Clean only once!
        clean = False

        if os.path.isdir(path_to_output):
            if verbose:
                print ('')
                print ('INFO Cleaning {path_to_output}')
            shutil.rmtree(path_to_output)

        if os.path.isdir(path_to_results):
            if verbose:
                print ('')
                print ('INFO Cleaning {path_to_results}')
            shutil.rmtree(path_to_results)

    for path in [path_to_output, path_to_results, path_to_code, path_to_systems]:
        if not os.path.isdir(path):
            os.makedirs(path)

    ########################################################
    # Prepare systems and results in MLPerf format
    target_system_name = cmx['use_system']['target_system_name']
    if target_system_extra_name !='': target_system_name += target_system_extra_name
    system_json_file = os.path.join(path_to_systems, target_system_name + '.json')





    # xyz
    target_system_desc = cmx['use_system']['desc']

    target_system_desc['system_name'] = target_system_name

    if system_division != '': target_system_desc['division'] = system_division
    if system_status != '': target_system_desc['status'] = system_status
    if submitter != '': target_system_desc['submitter'] = submitter

    if len(system_desc) > 0:
        utils.merge_dicts({'dict1':target_system_desc, 'dict2':system_desc, 'append_lists':False})

    if verbose:
        print ('')
        print (f'INFO saving system meta to {system_json_file}')

    r = utils.save_json(system_json_file, target_system_desc)
    if r['return']>0: return cmind.embed_error(r)


    ######################################################
    # Generate CMD
    cmd_run = code_meta['cmd_run'].strip()

    script_prefix = ''

    experiment = 0

    experiments = max_experiments
    if experiments == None: experiments = code_meta.get('max_experiments', None)
    if experiments == None: experiments = 10
    experiments = int(experiments)

    rrr  = {'return':0, 'experiments':[]}

    while experiment < experiments:
        experiment += 1

        print ('==============================================')
        print (f'Experiment {experiment} out of {experiments}')
        print ('')
        print (f'Current directory: {os.getcwd()}')
        print ('')
        get_memory_use('Memory use:')
        print ('')

        skip_run = False
        if build:
            skip_run = True

        log_file_processed = os.path.join(path_to_results, f'result_{experiment}.txt')
        log_file = f'cmx_mlperf_training_raw_{experiment}.log'
        log2_path = os.path.join(path_to_output, f'cmx_mlperf_training_compliance_{experiment}.log')

        if os.name == 'nt':
            eol = '^'
            ext = '.bat'
            cmd_postfix = ''
        else:
            eol = '\\'
            ext = '.sh'
            script_prefix = 'set +x\nset -e\n'
            cmd_postfix = f' 2>&1 |& tee "{path_to_output}/{log_file}"'

        save_script = f'cmx-rt-run' + ext

        cmd = cmd_run.format(
                eol=eol,
                rt_config_file=rt_config_file,
                train_code_path_with_version=train_code_path_with_version,
                path_to_dataset=path_to_dataset,
                path_to_model=path_to_model,
                path_to_output=path_to_output)

        if random_seed:
            import random
            if seed != '':
                random.seed(int(seed))
            cmd_meta['seed'] = str(int(random.random()*1000000))

        for k in cmd_meta:
            v = str(cmd_meta[k]).strip()
            cmd += f' {eol}\n  --{k} "{v}"'

        if cmd_postfix!='':
            cmd += cmd_postfix


        if os.path.isfile(log_file_processed):
            skip_run = True

        ######################################################
        # Run or record run script
        log_path = os.path.join(path_to_output, log_file)
        if os.path.isfile(log_path):
            skip_run = True

        run_cmd = misc['helpers']['run_cmd']

        if clean_os_kernel_cache:
            ii = {'action':'run',
                  'automation':misc['flex.task'],
                  'control':{'out':out},
                  'tags':'clean,os,kernel,cache',
                  'verbose': verbose
                 }

            r = cmind.x(ii)
            if r['return'] > 0: return cmind.embed_error(r)

        # Run benchmark
        r = run_cmd(cmind, console, cmd, env, None,
                    state = state, verbose = verbose,
                    cmd_prefix_from_state = cmd_prefix_from_state_compile,
                    save_script = save_script, script_prefix = script_prefix, 
                    skip_run = skip_run,
                    run_script = True)
        if r['return']>0: return cmind.embed_error(r)

        if save_script != '':
            print ('')
            print (f'INFO CMX generated script to run MLPerf training benchmark: {save_script}')

        if os.path.isfile('mlperf_compliance.log'):
            if os.path.isfile(log2_path):
                os.remove(log2_path)

            shutil.move('mlperf_compliance.log', log2_path)

        ######################################################
        # Process results
        if os.path.isfile(log_path) and not os.path.isfile(log_file_processed):
            r = process_raw_result(verbose, log_path, log_file_processed)
            if r['return']>0: return cmind.embed_error(r)

    ######################################################
    # Process all results
    experiment = 0

    time_raw_min = 0
    time_raw_max = 0
    time_raw_total = 0
    time_raw_index = 0

    path_to_python = cmx['sys_tool_python']['sys_tool_python_with_path2']

    package_checker_log = 'package_checker.log'

    mllog_errors = []

    while True:
        experiment += 1

        log_file_processed = os.path.join(path_to_results, f'result_{experiment}.txt')
        if not os.path.isfile(log_file_processed):
            break

        if os.path.isfile(package_checker_log):
            os.remove(package_checker_log)

        print ('===================================')
        print (f'Processing log {log_file_processed}')

        log_file_json_processed = os.path.join(path_to_results, f'result_{experiment}.json')

        rr ={}
        if os.path.isfile(log_file_json_processed):
            r = utils.load_json(log_file_json_processed)
            if r['return']>0: return cmind.embed_error(r)

            rr = r['meta']

        rr2 = get_basic_time(log_file_processed)
        if rr2['return']>0: return cmind.embed_error(rr2)

        if 'mllog' in rr2: del(rr2['mllog'])

        rr.update(rr2)

        rtt = rr.get('raw_total_time_minutes', 0)
        if rtt != 0:
            if time_raw_min == 0: time_raw_min = rtt
            elif rtt < time_raw_min: time_raw_min = rtt

            if time_raw_max == 0: time_raw_max = rtt
            elif rtt > time_raw_max: time_raw_max = rtt

            time_raw_total += rtt
            time_raw_index += 1

        compliance_file = os.path.join(path_to_results, f'result_{experiment}_compliance.txt')

        cmds = []

        xpackage_checker_extra_flags = ' ' + package_checker_extra_flags if package_checker_extra_flags != '' else ''

        if mlperf_version == '': mlperf_version = code_meta.get('mlperf_version', '')
        if mlperf_version == '': mlperf_version = code_version

        cmd = f'{path_to_python} -m mlperf_logging.compliance_checker --usage training --ruleset "{mlperf_version}.0" --log_output {compliance_file} {log_file_processed}'

        print ('**********************************************************************')
        r = run_cmd(cmind, console, cmd, env, None,
                    state = state, verbose = verbose,
                    cmd_prefix_from_state = cmd_prefix_from_state_compile,
                    save_script = '', script_prefix = script_prefix,
                    capture_output = True,
                    skip_run = False,
                    run_script = False)

        std = r.get('stdout', '') + r.get('stderr', '')

        if r['return']>0 or r.get('returncode', 0)>0:
            err = f'mlperf_logging.compliance_checker failed:\n{std}'
            if mllog_stop_if_fail:
                return cmind.prepare_error(1, err)

            mllog_errors.append(err)
            std = 'WARNING: problem with MLPerf benchmark results detected:\n' + std

        print (std)

        rrr['experiments'].append(rr)

    ########################################################
    # Prepare results in MLPerf format
    path_to_target_mlperf_results = os.path.join(path_to_results, target_system_name, mlperf_model_name)

    if verbose:
        print ('')
        print (f'INFO preparing results in {path_to_target_mlperf_results}')

    if not os.path.isdir(path_to_target_mlperf_results):
        os.makedirs(path_to_target_mlperf_results)

    experiment = 0
    while True:
        experiment += 1

        log_file_processed = os.path.join(path_to_results, f'result_{experiment}.txt')
        if not os.path.isfile(log_file_processed):
            break

        log_file_processed_final = os.path.join(path_to_target_mlperf_results, f'result_{experiment}.txt')
        if not os.path.isfile(log_file_processed_final):
            shutil.copy(log_file_processed, log_file_processed_final)

    ########################################################
    print ('**********************************************************************')
    if verbose:
        print ('')
        print (f'INFO checking package')

    cmd = f'{path_to_python} -m mlperf_logging.package_checker . training "{mlperf_version}.0"{xpackage_checker_extra_flags}'

    r = run_cmd(cmind, console, cmd, env, None,
                state = state, verbose = verbose,
                cmd_prefix_from_state = cmd_prefix_from_state_compile,
                save_script = '', script_prefix = script_prefix,
                skip_run = False,
                capture_output = True,
                run_script = False)

    std = r.get('stdout', '') + r.get('stderr', '')

    if r['return']>0 or r.get('returncode', 0)>0:
        err = f'mlperf_logging.package_checker failed:\n{std}'
        if mllog_stop_if_fail:
            return cmind.prepare_error(1, err)

        mllog_errors.append(err)
        std = 'WARNING: problem with MLPerf benchmark results detected:\n' + std

    print (std)

    # Read package log
    package_checker_log = 'package_checker.log'

    if not os.path.isfile(package_checker_log) and mllog_stop_if_fail:
        return cmind.prepare_error(1, f'file {package_checker_log} was not created')

    if os.path.isfile(package_checker_log):
        r = utils.load_txt(package_checker_log)
        if r['return'] >0: return cmind.embed_error(r)

        lines = r['string'].split('\n')

        err = ''
        for l in lines:
            l = l.strip()
            if l.lower().startswith('error '):
                err += l + '\n'

        if err != '' and mllog_stop_if_fail:
            err = err.strip('\n')
            return cmind.prepare_error(1, f'file {package_checker_log} has errors:\n{err}')

    ########################################################
    print ('**********************************************************************')
    if verbose:
        print ('')
        print (f'INFO summarize results')

    summary_csv_file = 'cmx-rt-mlperf-training-summary.csv'

    cmd = f'{path_to_python} -m mlperf_logging.result_summarizer . training "{mlperf_version}.0" --csv {summary_csv_file}'

    r = run_cmd(cmind, console, cmd, env, None,
                state = state, verbose = verbose,
                cmd_prefix_from_state = cmd_prefix_from_state_compile,
                save_script = '', script_prefix = script_prefix,
                capture_output = True,
                skip_run = False,
                run_script = False)

    std = r.get('stdout', '') + r.get('stderr', '')

    if r['return']>0 or r.get('returncode', 0)>0:
        err = f'mlperf_logging.result_summarizer failed:\n{std}'
        if mllog_stop_if_fail:
            return cmind.prepare_error(1, err)

        mllog_errors.append(err)
        std = 'WARNING: problem with MLPerf benchmark results detected:\n' + std

    print (std)

    ########################################################
    mlperf_time_to_accuracy = None

    if os.path.isfile(summary_csv_file):
        if verbose:
            print ('')
            print (f'INFO processing CSV file')

        ii = {'action':'run',
              'automation':misc['flex.task'],
              'control':{'out':out},
              'tags':'process,mlperf,csv,results',
              'verbose': verbose,
              'csv_file': summary_csv_file,
              'benchmark': 'training',
              'system_desc': target_system_desc,
              'result_extra': {
                'benchmark_name': f'mlperf-training',
                'benchmark_version': mlperf_version,
                'benchmark_version_alias': code_version
              }
             }

        r = cmind.x(ii)
        if r['return'] > 0: return cmind.embed_error(r)

        results_summary = r['summary']

        # Search for model with result
        found_result = {}

        for result in results_summary:
            if result.get('mlperf_training_model', '') == mlperf_model_name:
                found_result = result
                break

        if len(found_result)>0:
            v = result['result']
            if v != None and v != '':
                try:
                    mlperf_time_to_accuracy = float(v)
                except:
                    pass

    ########################################################

    if len(mllog_errors)>0:
        rrr['mllog_errors'] = mllog_errors

    rrr['result_summary'] = found_result

    rrrr = {
       'raw_time_to_accuracy_minutes_min': time_raw_min,
       'raw_time_to_accuracy_minutes_max': time_raw_max,
       'raw_time_to_accuracy_minutes_avg': (time_raw_total / time_raw_index),
       'time_to_accuracy_minutes': mlperf_time_to_accuracy,
       'result':  mlperf_time_to_accuracy
    }

    rrr.update(rrrr)

    print ('=======================================================')
    print ('Raw average MLPerf time to accuracy (minutes): {:.5f}'.format(time_raw_total / time_raw_index))
    if mlperf_time_to_accuracy == None:
        print ('Official MLPerf time to accuracy was not obtained - please check outputs and logs')
        print (f'Current directory: {os.getcwd()}')
    else:
        print ('Official MLPerf time to accuracy (minutes): {:.5f}'.format(mlperf_time_to_accuracy))
    print ('=======================================================')

    # Save raw output
    r = utils.save_json('cmx-raw-output.json', rrr)
    if r['return'] >0 : return cmind.embed_error(r)

    rrr['use_raw_experiment_output_file'] = True

    # Prepare MLPerf standard output
    output = found_result
    output.update(rrrr)

    # Add flattened system desc to results if needed and if it was not processed by CSV
    # Usually if official result was not obatined
    fd = {}
    utils.flatten_dict(target_system_desc, fd, 'system.')

    for k in fd:
         if k not in output:
             output[k] = fd[k]






    r = utils.save_json('cmx-output.json', output)
    if r['return'] >0 : return cmind.embed_error(r)

    return rrr

######################################################################
def process_raw_result(verbose, log_path, log_file_processed):
    if verbose:
        print ('')
        print (f'INFO Processing log file {log_path}')

    rr = get_basic_time(log_path)
    if rr['return']>0: return rr

    mllog = rr['mllog']

    r = utils.save_txt(log_file_processed, '\n'.join(mllog))
    if r['return']>0: return r

    r = utils.save_json(log_file_processed[:-4] + '.json', rr)
    if r['return']>0: return r

    return rr

######################################################################
def get_basic_time(log_file):
    import json
    import ast

    rr = {'return':0}

    r = utils.load_txt(log_file)
    if r['return']>0: return r

    lines = r['string'].split('\n')
    lines2 = []
    steps = []

    for l in lines:
        l = l.strip()
        j = l.find(':::MLLOG')
        if j>=0:
            lines2.append(l[j:])
        else:
            j = l.find("{'")
            if j>=0:
                try:
                    raw_result = ast.literal_eval(l[j:])
                    steps.append(raw_result)
                except Exception as e:
                    pass

    try:
        start_time_ms = json.loads(lines2[0].split(":::MLLOG ")[1])["time_ms"]
        end_time_ms = json.loads(lines2[-1].split(":::MLLOG ")[1])["time_ms"]

        total_time_ms = end_time_ms - start_time_ms
        total_time_minutes = total_time_ms / (1000 * 60)

        rr['raw_total_time_ms'] = total_time_ms
        rr['raw_total_time_minutes'] = total_time_minutes
    except Exception as e:
        pass

    if len(steps)>0: rr['steps'] = steps

    rr['mllog'] = lines2

    return rr

######################################################################
def get_memory_use(text = None):

    import os
    import psutil

    pid = os.getpid()

    python_process = psutil.Process(pid)

    memory_use = python_process.memory_info()[0] # in bytes
    memory_use_gb = memory_use / (1024 ** 3) 

    memory_info = psutil.virtual_memory()

    available_memory = memory_info.available  # in bytes
    total_memory = memory_info.total  # in bytes

    available_memory_gb = available_memory / (1024 ** 3)
    total_memory_gb = total_memory / (1024 ** 3)

    if text != None:
        print (text)
        print (f"* Total Memory: {total_memory_gb:.2f} GB")
        print (f"* Available Memory: {available_memory_gb:.2f} GB")
        print (f"* Used Python Memory: {memory_use_gb:.2f} GB")

    return {'return':0, 'memory_use': memory_use,
                        'memory_use_gb': memory_use_gb,
                        'available_memory': available_memory,
                        'available_memory_gb': available_memory_gb,
                        'total_memory': total_memory,
                        'total_memory_gb': total_memory_gb}

