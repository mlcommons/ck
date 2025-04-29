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
    console = misc.get('console', False)
    self_meta = misc['meta']
    run_cmd = misc['helpers']['run_cmd']

    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)
    env = _input2.get('env', {})

    _input = i['input']

    proxy = _input.get('proxy', '')
    if proxy == '':
        return cmind.prepare_error(1, 'proxy is not specified')

    ttl = _input.get('ttl', '')

    # Update flex.cfg
    r = cmind.x({'automation':self_meta['use']['flex.cfg'],
                 'action':'update',
                 'artifact':'tsh',
                 'meta':{'proxy':proxy, 'ttl':ttl}})
    if r['return'] >0: return cmind.embed_error(r)

    # Update SSH
    bin_tsh = tmp['sys_tool_tsh_with_path2']

    cmd_login = f'{bin_tsh} login --proxy={proxy} --auth=new_github_connector'

    if ttl != '':
        cmd_login += f' --ttl={ttl}'

    if os.name == 'nt':
        cmds = [ cmd_login,
                 'echo. >> %userprofile%/.ssh/config',
                 f'{bin_tsh} config -k no --proxy {proxy} >> %userprofile%/.ssh/config' ]
    else:
        cmds = [ cmd_login,
                 'echo >> ~/.ssh/config',
                 f'{bin_tsh} config -k no --proxy {proxy} >> ~/.ssh/config' ]

    for cmd in cmds:
        r = run_cmd(cmind, console, cmd, env, None, state = state, verbose = verbose)
        if r['return']>0: return r

    return {'return':0}
