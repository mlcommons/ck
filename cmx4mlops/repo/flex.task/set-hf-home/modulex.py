# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy

def run(i):

    ###################################################################
    # Prepare flow

    cmind = i['cmind']
    misc = i['misc']
    state = i['state']

    out = misc.get('out', '')
    console = misc.get('console', False)

    self_meta = misc['meta']

    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)

    _input = i['input']

    path = _input.get('path', '')

    # Since this task will be cached, we need to pass environment variables further
    # via dynamic 'envs' key

    return {'return':0, 'envs':{'HF_HOME':path}, 'huggingface_home_path': path}
