# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy
import shutil


def run(i):

    misc = i['misc']
    cmind = i['cmind']
    state = i['state']
    tmp = i['tmp']

    cmx = state['cmx']

    out = misc.get('out', '')
    console = misc.get('console', False)

    self_meta = misc['meta']
    self_path = misc['path']

    # Get aux input
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)
    quiet = _input2.get('quiet', False)

    # Get main input
    _input = i['input']

    benchmark = _input.get('benchmark', '')

    ii = {"action": "get", "automation": "flex.experiment", "only_files":True}

    if benchmark != '': ii['tags'] = f'_benchmark.{benchmark}'

    print (ii)

    r = cmind.x(ii)
    if r['return'] >0: return cmind.embed_error(r)

    print (r)



    return {'return':0}
