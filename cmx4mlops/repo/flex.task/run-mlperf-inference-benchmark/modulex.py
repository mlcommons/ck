# Author and developer: Grigori Fursin

from cmind import utils
from cmind import __version__ as cmind_version

import os
import copy
import shutil

def run(i):

    misc = i['misc']
    cmind = i['cmind']
    state = i['state']
    tmp = i['tmp']

    run_cmd = misc['helpers']['run_cmd']

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

    _input = i['input']

    scenario = _input.get('scenario', '')
    mode = _input.get('mode', '')

    model = _input.get('model', '')

    model2 = model
    j = model2.find('/')
    if j > 0:
        model2 = model2[j+1:]
#    model2 = model.replace('/', '--')

    dataset = _input.get('dataset', '')

    submitter = _input.get('submitter', '')
    division = _input.get('division', '')

    system_desc = _input.get('system_desc', {})

    tmp_dir_postfix = _input.get('tmp_dir_postfix', '')

    # Prepare MLPerf structure
    ii = {'action': 'run',
          'automation': misc['flex.task'],
          'artifact':'create-mlperf-inference-dir-structure,cefd155abe2440ea',
          'quiet': quiet,
          'verbose': verbose,
          'control':{'out':out}}

    for k in ['clean', 'path', 'division', 'submitter', 'sut', 'mlperf_model', 'system_desc_file']:
        v = _input.get(k)
        if v != None: ii[k] = v

    ii['model'] = model2

    print ('')
    print (f'Creating MLPerf directory structure in {os.getcwd()}')

    rd = cmind.x(ii)
    if rd['return']>0: return rd

    path_results = rd['path_results_sut_model']
    sut_file = rd['sut_file']
    path_measurements_sut_model = rd['path_measurements_sut_model']

    path_sut_config = rd['path_sut_config']

    r = utils.load_json(path_sut_config)
    if r['return'] > 0: return r
    sut_config = r['meta']

    if len(system_desc)>0:
        sut_config.update(system_desc)

    sut_config['submitter'] = submitter
    sut_config['division'] = division
    sut_config['operating_system'] = state['cmx']['detect_host_info_min']['host_os'].get('release_name_with_kernel','')

    r = utils.save_json(path_sut_config, sut_config)
    if r['return'] >0: return r

    # Check scenarios and 
    scenarios = [scenario] if scenario != '' else ['Offline', 'Server']
    modes = [mode] if mode != '' else ['performance', 'accuracy']

    cur_dir = os.getcwd()

    for scenario in scenarios:
        for mode in modes:

             print ('='*80)

             path_results_scenario = os.path.join(path_results, scenario, mode)
             if mode == 'performance':
                 path_results_scenario = os.path.join(path_results_scenario, 'run_1')
             os.makedirs(path_results_scenario, exist_ok = True)

             path_measurements = rd['path_measurements_sut_model']
             path_measurements_scenario = os.path.join(path_measurements, scenario)
             os.makedirs(path_measurements_scenario, exist_ok = True)

             # Create model config file with the same name as SUT
             modelx = model if '/' not in model else 'https://huggingface.co/' + model
             model_conf = {"starting_weights_filename": modelx,
                           "retraining": "no",
                           "input_data_types": "int32",
                           "weight_data_types": "bfloat16",
                           "weight_transformations": "none"}
             path_model_conf = os.path.join(path_measurements_scenario, sut_file)
             r = utils.save_json(path_model_conf, model_conf)
             if r['return'] >0: return r

             path_measurements_readme = os.path.join(path_measurements_scenario, 'README.md')
             r = utils.save_txt(path_measurements_readme, 'TBD\n')
             if r['return'] >0: return r

             print (f'MLPerf scenario: {scenario}')
             print (f'MLPerf mode: {mode}') 

             print ('')
             print (f'Current path: {cur_dir}')
             print (f'Path to results: {path_results_scenario}')
             print (f'Path to measurements: {path_measurements_scenario}')

             print ('')

             x = f'tmp-results-{scenario}-{mode}'
             if tmp_dir_postfix != '': x += str(tmp_dir_postfix)
             cur_dir_tmp_results = os.path.join(cur_dir, x)
             if ii.get('output', '') != '': cur_dir_tmp_results = ii['output']

             # Prepare input to run benchmark
             ii = copy.deepcopy(_input.get('bench', {}))

             ii['output'] = cur_dir_tmp_results

             ii['model_path'] = model
             ii['dataset_path'] = dataset

             ii['scenario'] = scenario

             if mode == 'accuracy':
                 ii['accuracy'] = True

             cmx_mlperf_state = {}

             ii.update({'action': 'run',
                        'automation': misc['flex.task'],
                        'tags':'benchmark,vllm,huggingface,mlperf,loadgen',
                        'state': cmx_mlperf_state,
                        'quiet': quiet,
                        'verbose': verbose,
                        'control':{'out':out}})

             rb = cmind.x(ii)
             if rb['return']>0: return rb

             src_dir = rb['src_dir']

#             import json
#             print (json.dumps(cmx_mlperf_state, indent=2))
#             input('xyz')

             update_sut_config = {}

             xcmx = cmx_mlperf_state.get('cmx', {})

             detect_host_info_min = xcmx.get('detect_hots_info_min', {})
             target_device = xcmx.get('target_device', '')

             flow = xcmx.get('flow', {})
             versions = {}
             other_software_stack = ''

             for k in flow:
                 v = flow[k].get('version', '')
                 if v != '':
                     versions[k] = v

                     if other_software_stack != '': other_software_stack += ', '

                     other_software_stack = k + ': ' + v

             if other_software_stack !='':
                 update_sut_config['other_software_stack'] = other_software_stack

             if sut_config.get('sw_notes', '') == '':
                 update_sut_config['sw_notes'] = f'Automated by MLCommons CMX v{cmind_version}'

             if len(update_sut_config)>0:
                 tmp_sut_config = copy.deepcopy(sut_config)
                 tmp_sut_config.update(update_sut_config)

                 r = utils.save_json(path_sut_config, tmp_sut_config)
                 if r['return'] >0: return r
 
             cmx_version_info_file = os.path.join(path_measurements_scenario, 'cmx_version_info.json')
             r = utils.save_json(cmx_version_info_file, versions)

             cmx_host_os_info_file = os.path.join(path_measurements_scenario, 'cmx_host_os_info.json')
             r = utils.save_json(cmx_host_os_info_file, detect_host_info_min)


             if target_device == 'cuda':
                 detect_cuda_info = xcmx.get('detect_cuda_info', {})
                 if len(detect_cuda_info) > 0:
                     cmx_detect_cuda_info_file = os.path.join(path_measurements_scenario, 'cmx_cuda_info.json')
                     r = utils.save_json(cmx_detect_cuda_info_file, detect_cuda_info)

                     acc_name = detect_cuda_info.get('name', '')
                     if acc_name != '':
                         update_sut_config['accelerator_model_name'] = acc_name




             # Pip freeze 
             pip_freeze_file = os.path.join(path_measurements_scenario, 'pip_freeze.txt')
             cmd = f'pip freeze > {pip_freeze_file}'

             r = run_cmd(cmind, console, cmd, {}, None, state = state, verbose = verbose, capture_output = False)
             if r['return']>0: return r



             # Copy mlperf.conf and use.conf
             for f in ['mlperf.conf', 'user.conf', 'audit.config']:
                 fin = os.path.join(src_dir, f)
                 if os.path.isfile(fin):
                     fout = os.path.join(path_measurements_scenario, f)
                     shutil.copy(fin, fout)

             for f in ['system_info.json']:
                 fin = os.path.join(cur_dir_tmp_results, f)
                 if os.path.isfile(fin):
                     fout = os.path.join(path_measurements_scenario, f)
                     shutil.copy(fin, fout)

             for f in ['accuracy.txt', 'mlperf_log_accuracy.json', 'mlperf_log_detail.txt', 'mlperf_log_summary.txt']:
                 fin = os.path.join(cur_dir_tmp_results, 'mlperf-logs', f)
                 if os.path.isfile(fin):
                     fout = os.path.join(path_results_scenario, f)
                     shutil.copy(fin, fout)


    return {'return':0}
