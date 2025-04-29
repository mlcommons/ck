# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy

def run(i):

    ###################################################################
    # Prepare flow

    tmp = i['tmp']

    cmind = i['cmind']

    misc = i['misc']

    out = misc.get('out', '')
    console = misc.get('console', False)

    self_meta = misc['meta']

    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)

    _input = i['input']

    device = _input.get('device', '')

    # Check device (either from select-compute or forced)
    if device == '':
        device = tmp['target_pytorch_device']

    rrr={'return':0}
    rrr['_update_run_script_env'] = {
                                      'CMX_PYTORCH_DEVICE': device
                                    }

    return rrr
