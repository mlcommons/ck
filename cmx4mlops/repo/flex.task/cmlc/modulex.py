# Author and developer: Grigori Fursin
# Run legacy CM front-ends for MLOps and MLPerf (mlc, mlcr and mlcflow)

from cmind import utils

import os
import copy

def run(i):

    ###################################################################
    # Prepare flow

    cmind = i['cmind']

    misc = i['misc']

    control = misc['control']

    orig_cmd = control.get('_cmd', [])

    out = misc.get('out', '')

    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)

    import copy
    ii = copy.deepcopy(i['input'])

    ii['action'] = 'run'
    ii['automation'] = misc['flex.task']
    ii['tags'] = 'run,mlc'
    ii['control'] = {'out':out, '_cmd':orig_cmd}
    ii['verbose'] = verbose

    return cmind.x(ii)
