# Author and developer: Grigori Fursin

from cmind import utils
import os

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

    # Check device (either from select-compute or forced)
    device = _input.get('device', '')

    if device == '':
        device = state['cmx']['use_compute']['target_device']

    hf_model_path = _input.get('model_path', '')

    port = _input.get('port', '')
    use_gpus = _input.get('use_gpus', '')
    tensor_parallel_size = _input.get('tensor_parallel_size', '')
    extra_cmd = _input.get('extra_cmd', '')

    if use_gpus != '':
        num_use_gpus = int(use_gpus)
        env['CUDA_VISIBLE_DEVICES'] = ",".join(str(i) for i in range(num_use_gpus))

        if tensor_parallel_size == '':
            tensor_parallel_size = num_use_gpus

    cur_dir = os.getcwd()

    # Prepare cmd
    python_path = state['cmx']['sys_tool_python']['sys_tool_python_with_path2']

    cmd = f'vllm serve {hf_model_path}'

    if device != '':
        cmd += f' --device {device}'

    if port != '':
         cmd += f' --port {port}'

    if tensor_parallel_size != '':
        cmd += f' --tensor-parallel-size {tensor_parallel_size}'

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

    # Check device (either from select-compute or forced)
    profile = _input.get('profile', False)

    cmd_prefix = ''
    if profile:
        profile_nsys = _input.get('profile_nsys', False)

        if profile_nsys:
            cmd_prefix = tmp['nsys_profile_cmd_prefix'] + ' '

    cmd = f"""{cmd_prefix}{cmd}"""

    r = run_cmd(cmind, console, cmd, env, None, state = state, verbose = verbose, print_cmd = True)
    if r['return']>0: return r


    return {'return':0}
