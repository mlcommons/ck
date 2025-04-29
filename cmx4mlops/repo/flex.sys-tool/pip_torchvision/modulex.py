# Author and developer: Grigori Fursin

from cmind import utils

import os
import sys


def install(i):

    cmind = i['cmind']
    cmx = i['state']['cmx']

    # Reuse install in pip_torch
    r = cmind.x({'automation': i['automation_flex_task_sys_tool'],
                 'action':'load', 
                 'tags':'pip_torch'})
    if r['return']>0: return cmind.embed_error(r)

    rr = utils.load_module(cmind, r['path'], 'modulex.py')
    if rr['return'] >0: return cmind.embed_error(rr)

    i['force_package'] = 'torchvision'

    return rr['sub_module_obj'].install(i)
