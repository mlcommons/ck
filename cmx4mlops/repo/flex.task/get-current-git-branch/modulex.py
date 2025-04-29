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

    _input = i['input']

    cur_dir = os.getcwd()

    bin_git = tmp['sys_tool_git_with_path2']

    cmd = bin_git + ' rev-parse --abbrev-ref HEAD'

    r = run_cmd(cmind, console, cmd, {}, None, state = {}, verbose = verbose, capture_output = True)
    if r['return']>0: return r

    git_branch_name = r['stdout'].strip()

    if console:
        print (git_branch_name)

    return {'return':0, 'git_dir':cur_dir, 'git_branch_name':git_branch_name}
