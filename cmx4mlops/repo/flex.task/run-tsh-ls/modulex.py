# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy

def run(i):

    ###################################################################
    # Prepare flow

    cmind = i['cmind']
    state = i['state']
    tmp = i['tmp']

    misc = i['misc']
    out = misc.get('out', '')
    console = misc.get('console', False)
    self_meta = misc['meta']
    run_cmd = misc['helpers']['run_cmd']

    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)
    quiet = _input2.get('quiet', False)

    _input = i['input']

    env = _input2.get('env', {})

    proxy = _input.get('proxy', '')
    if proxy == '':
        r = cmind.x({'automation':self_meta['use']['flex.cfg'],
                     'action':'find',
                     'artifact':'tsh'})
        if r['return'] >0: return cmind.embed_error(r)

        if len(r['list']) == 1:
            proxy = r['list'][0].meta['proxy']

    if proxy == '':
        return cmind.prepare_error(1, 'proxy is not specified')

    bin_tsh = tmp['sys_tool_tsh_with_path2']

    cmd = f'{bin_tsh} ls --proxy={proxy}'

    r = run_cmd(cmind, console, cmd, env, None, state = state, verbose = verbose)
    if r['return']>0: return r

    return {'return':0}
