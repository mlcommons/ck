# Author and developer: Grigori Fursin
# Run legacy CM front-ends for MLOps and MLPerf (mlc, mlcr and mlcflow)

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
    control = misc['control']
    unparsed_artifacts = control.get('_unparsed_artifacts',[])
    orig_cmd = control.get('_cmd', [])
    console = misc.get('console', False)
    self_meta = misc['meta']
    run_cmd = misc['helpers']['run_cmd']

    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)

    _input = i['input']

    # Remove flags for flextask
    min_cmd = []
    k = 3
    while k < len(orig_cmd):
        v = orig_cmd[k]
        if not v.startswith('--'):
            break

        k += 1

    # Prepare call to legacy/stripped CM scripts runner from MLCommons (mlcr)
    cmd = 'mlc ' + ' '.join(orig_cmd[k:])

    if not verbose:
       print ('Executing MLC (legacy CM front-end for MLOps and MLPerf):')
       print (f'{cmd}')
       print ('')

    return run_cmd(cmind, console, cmd, {}, None, state = state, verbose = verbose, capture_output = False)
