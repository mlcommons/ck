# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy

def run(i):

    ###################################################################
    # Prepare flow

    cmind = i['cmind']
    state = i['state']

    misc = i['misc']
    tmp = i['tmp']

    console = misc.get('console', False)

    self_meta = misc['meta']
    self_path = misc['path']

    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)

    _input = i['input']

    env = _input2.get('env', {})
    timeout = _input.get('timeout', None)

    run_cmd = misc['helpers']['run_cmd']

    ###################################################################
    # Check tmp directory
    self_path_tmp = os.path.join(self_path, 'tmp')
    if not os.path.isdir(self_path_tmp):
        os.makedirs(self_path_tmp)

    os.chdir(self_path_tmp)

    # Prepare target file
    if state['cmx'].get('cpp_compiler_non_default_bin_name', False):
        # Usually Visual C++ on Windows but not clang
        target_bin = 'test.exe' 
    else:
        target_bin = 'a.exe' if os.name == 'nt' else 'a.out'

    if os.path.isfile(target_bin):
        os.remove(target_bin)

    ###################################################################
    # Prepare compiler
    cmd_prefix_from_state_compile = self_meta.get('cmd_prefix_from_state_compile', [])

    cpp_compiler = state['cmx']['cpp_compiler_with_path']

    cmd = cpp_compiler + ' ../src/test.cpp'

    print ('')
    print (cmd)

    r = run_cmd(cmind, console, cmd, env, timeout, 
                state = state, verbose = verbose,
                cmd_prefix_from_state = cmd_prefix_from_state_compile)
    if r['return']>0: return r

    ###################################################################
    # Run

    cmd = target_bin if os.name == 'nt' else './'+target_bin

    print ('')
    print (cmd)

    r = run_cmd(cmind, console, cmd, env, timeout,
                state = state, verbose = verbose,
                cmd_prefix_from_state = [])

    return r
