# Author and developer: Grigori Fursin

from cmind import utils
import os
import shutil

def run(i):

    ###################################################################
    # Prepare flow

    cmind = i['cmind']

    misc = i['misc']
    run_cmd = misc['helpers']['run_cmd']

    state = i['state']
    tmp = i['tmp']

    cmx = state['cmx']

    out = misc.get('out', '')
    console = misc.get('console', False)

    self_meta = misc['meta']
    self_path = misc['path']

    # Prepare aux inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)
    quiet = _input2.get('quiet', False)

    # Prepare main input
    _input = i['input']

    clean = _input.get('clean', False)
    path = _input.get('path', '')
    division = _input.get('division', '')
    submitter = _input.get('submitter', '')
    sut = _input.get('sut', '')
    model = _input.get('model', '')
    mlperf_model = _input.get('mlperf_model', '')
    system_desc_file = _input.get('system_desc_file', '')

    # Check system desc file
    system_desc = {}
    if system_desc_file != '':
        r = utils.load_json(system_desc_file)
        if r['return'] >0 : return cmind.embed_error(r)

        system_desc = r['meta']

    # Prepare paths
    rr = {'return': 0}

    if path == '': path = os.getcwd()
    os.makedirs(path, exist_ok = True)

    rr['path'] = path

    # Check division
    path_division = os.path.join(path, division)

    if clean and os.path.isdir(path_division):
        shutil.rmtree(path_division)
    os.makedirs(path_division, exist_ok = True)

    rr['path_division'] = path_division

    # Check submitter
    path_submitter = os.path.join(path_division, submitter)
    os.makedirs(path_submitter, exist_ok = True)

    rr['path_submitter'] = path_submitter

    # Main structure
    for d in ['code', 'measurements', 'results', 'systems']:
        dd = f'path_{d}'
        rr[dd] = os.path.join(path_submitter, d)
        os.makedirs(rr[dd], exist_ok = True)

    # SUT config
    rr['sut_file'] = sut + '.json'
    rr['path_sut_config'] = os.path.join(rr['path_systems'], rr['sut_file'])
    if not os.path.isfile(rr['path_sut_config']):
        r = utils.save_json(rr['path_sut_config'], system_desc)
        if r['return'] > 0: return cmind.embedd_error(r)

    # Measurements with SUT
    rr['path_measurements_sut'] = os.path.join(rr['path_measurements'], sut)
    os.makedirs(rr['path_measurements_sut'], exist_ok = True)

    # Results with SUT
    rr['path_results_sut'] = os.path.join(rr['path_results'], sut)
    os.makedirs(rr['path_results_sut'], exist_ok = True)

    # Code with model
    rr['path_code_model'] = os.path.join(rr['path_code'], model)
    os.makedirs(rr['path_code_model'], exist_ok = True)

    # Code with model and README
    rr['path_code_model_readme'] = os.path.join(rr['path_code_model'], 'README.md')

    r = utils.save_txt(rr['path_code_model_readme'], 'TBD\n')
    if r['return'] >0: return r

    # Measurements with SUT and model
    rr['path_measurements_sut_model'] = os.path.join(rr['path_measurements_sut'], model)
    os.makedirs(rr['path_measurements_sut_model'], exist_ok = True)

    # Results with SUT and model
    rr['path_results_sut_model'] = os.path.join(rr['path_results_sut'], model)
    os.makedirs(rr['path_results_sut_model'], exist_ok = True)

    # If model is not the same as mlperf_model, create model mapping
    if mlperf_model !='' and model != mlperf_model:
        rr['path_model_mapping'] = os.path.join(path_submitter, 'model_mapping.json')

        model_mapping = {}
        if os.path.isfile(rr['path_model_mapping']):
            r = utils.load_json(rr['path_model_mapping'])
            if r['return'] >0: return r

            model_mapping = r['meta']

        model_mapping[model] = mlperf_model

        r = utils.save_json(rr['path_model_mapping'], model_mapping)
        if r['return'] >0: return r


    return rr
