# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy

def run(i):

    ###################################################################
    # Prepare flow

    misc = i['misc']
    cmind = i['cmind']
    state = i['state']
    tmp = i['tmp']
    env = i['env']
 
    cmx = state['cmx']

    envs = cmx['envs']
 
    out = misc.get('out', '')
    console = misc.get('console', False)

    self_meta = misc['meta']


    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)

    _input = i['input']

    _wait = _input.get('wait', False)
    print_env = _input.get('print_env', False)
    print_state = _input.get('print_state', False)

    import json
 
    if print_env:
        print ('=' * 32)
        print ('CMX envs:')
        print ('')
        print (json.dumps(envs, indent=2))

        print ('=' * 32)
        print ('CMX env:')
        print ('')
        print (json.dumps(env, indent=2))

    if print_state:
        print ('=' * 32)
        print ('CMX state:')
        print ('')

        print (json.dumps(state, indent=2))

    if _wait:
        print ('')
        input ('Press Enter to continue ...')

    print ('=' * 32)

    return {'return':0}
