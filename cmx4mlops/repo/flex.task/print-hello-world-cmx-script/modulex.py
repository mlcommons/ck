# Author and developer: Grigori Fursin

from cmind import utils

def run(i):
    ###################################################################
    # Prepare flow

    cmind = i['cmind']
    state = i['state']

    misc = i['misc']
    console = misc.get('console', False)

    _input2 = i['input2']
    verbose = _input2.get('verbose', False)

    _input = i['input']

    env = _input2.get('env', {})
    timeout = _input.get('timeout', None)

    run_cmd = misc['helpers']['run_cmd']

    cmd = misc['call_default_script_with_path']

    cmd = cmd.replace('{{script_name}}', 'run2')

    r = run_cmd(cmind, console, cmd, env, timeout, state = state, verbose = verbose)
    if r['return']>0: return r

    return {'return':0, 'test':'abc'}
