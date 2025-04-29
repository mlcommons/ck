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

    env = _input2.get('env', {})

    # Prepare main input
    _input = i['input']

    clean = _input.get('clean', False)
    hf_model_path = _input.get('model_path', '')
    hf_dataset_path = _input.get('dataset_path', '')
    dataset_split = _input.get('dataset_split', '')
    total_sample_count = _input.get('total_sample_count', '')
    scenario = _input.get('scenario', '')
    target_qps = _input.get('target_qps', '')
    api_server = _input.get('api_server', '')
    accuracy = _input.get('accuracy', False)
    output = _input.get('output', '')
    test = _input.get('test', False)
    compliance = _input.get('compliance', '')
    extra_cmd = _input.get('extra_cmd', '')
    _dir = _input.get('dir', '')

    # Prepare directory
    cur_dir = os.getcwd()

    src_dir = os.path.join(self_path, _dir)
#    tmp_dir = os.path.join(self_path, 'tmp')
#
#    if clean:
#        if os.path.isdir(tmp_dir):
#            shutil.rmtree(tmp_dir)
#    else:
#        shutil.copytree(src_dir, tmp_dir, dirs_exist_ok = True)
#
    os.chdir(src_dir)

    # Check audit.conf
    # Check audit.conf and user.conf
    for f in ['audit.config', 'user.conf']:
        if os.path.isfile(f):
            os.remove(f)

    if compliance != '':
        conf_out_file = 'audit.config'
        conf_in_file = os.path.join('compliance', compliance, conf_out_file)
        shutil.copy(conf_in_file, conf_out_file)

    conf_out_file = 'user.conf'
    conf_in_file = 'user-test.conf' if test else 'user-valid.conf'

    shutil.copy(conf_in_file, conf_out_file)

    # Prepare CMD
    python_path = state['cmx']['sys_tool_python']['sys_tool_python_with_path2']

    cmd = f'{python_path} main.py'
    cmd += f' --model-path "{hf_model_path}"'
    cmd += f' --dataset-path "{hf_dataset_path}"'
    cmd += f' --dataset-split {dataset_split}'
    if total_sample_count != '':
        cmd += f' --total-sample-count {total_sample_count}'
    cmd += f' --scenario {scenario}'
    cmd += f' --target-qps {target_qps}'
    cmd += f' --api-server {api_server}'
    if accuracy:
        cmd += ' --accuracy'
    if output != '':
        cmd += f' --output {output}'
    if extra_cmd != '':
        cmd += f' {extra_cmd}'

    # Add HF_HOME from flex.cfg
    hf_home = ''
    r = cmind.x({'automation':self_meta['use']['flex.cfg'],
                 'action':'load',
                 'artifact':'huggingface'})
    if r['return'] == 0:
        hf_home = r['meta'].get('env', {}).get('hf_home', '')
    if hf_home != '':
        state['cmx']['envs']['HF_HOME'] = hf_home

    r = run_cmd(cmind, console, cmd, env, None, state = state, verbose = verbose, print_cmd = True)
    if r['return']>0: return r

    return {'return':0, 'src_dir': src_dir}
