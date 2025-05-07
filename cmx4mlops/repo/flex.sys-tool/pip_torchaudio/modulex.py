# Author and developer: Grigori Fursin

from cmind import utils

import os
import sys


def install(i):

    env = i['env']

    # We should be able to override installation of packages 
    # TBD: do it cleaner via cfg ...
    if 'PIP_BREAK_SYSTEM_PACKAGES' not in env: env['PIP_BREAK_SYSTEM_PACKAGES'] = 1

    cmind = i['cmind']
    cmx = i['state']['cmx']

    # Reuse install in pip_torch
    r = cmind.x({'automation': i['automation_flex_task_sys_tool'],
                 'action':'load', 
                 'tags':'pip_torch'})
    if r['return']>0: return cmind.embed_error(r)

    rr = utils.load_module(cmind, r['path'], 'modulex.py')
    if rr['return'] >0: return cmind.embed_error(rr)

    i['force_package'] = 'torchaudio'

    return rr['sub_module_obj'].install(i)
