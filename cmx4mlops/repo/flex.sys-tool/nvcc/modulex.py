# Author and developer: Grigori Fursin

from cmind import utils

import os
import sys

def process(i):

    cmind = i['cmind']
    output = i['output']
    state = i['state']

    nvcc_bin = output['sys_tool_nvcc_dirname']
    nvcc_home = output['sys_tool_nvcc_dirname_x']

    paths = state['cmx']['envs'].get('+PATH', [])

    if os.name == 'nt':
        nvcc_libnvvp = os.path.join(nvcc_home, 'libnvvp')
        if nvcc_libnvvp not in paths and nvcc_libnvvp not in os.environ.get('PATH', ''):
            paths.insert(0, nvcc_libnvvp)

    if nvcc_bin not in paths and nvcc_bin not in os.environ.get('PATH', ''):
        paths.insert(0, nvcc_bin)

    if len(paths)>0:
        state['cmx']['envs']['+PATH'] = paths

    return {'return':0}
