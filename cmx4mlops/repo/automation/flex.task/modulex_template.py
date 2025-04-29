# Flex Task template
# Developer(s): 

from cmind import utils

def run(i):
    ###################################################################
    # Prepare flow

    cmind = i['cmind']
    state = i['state']

    misc = i['misc']
    console = misc.get('console', False)

    _input = i['input']

    env = _input.get('env', {})
    timeout = _input.get('timeout', None)

    run_cmd = misc['helpers']['run_cmd']

#    cmd = misc['call_default_script_with_path']
#    cmd = cmd.replace('{{script_name}}', 'run2')
#
#    r = run_cmd(cmind, console, cmd, env, timeout, state = state)
#    if r['return']>0: return r

    return {'return':0, 'new_key':'new_var'}
