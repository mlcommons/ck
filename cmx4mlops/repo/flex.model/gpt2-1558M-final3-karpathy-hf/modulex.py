# Author and developer: Grigori Fursin

from cmind import utils

import os
import sys


def install(i):

    cmind = i['cmind']
    cmx = i['state']['cmx']

    r = cmind.x({'automation': i['automation_flex_task_use_model'],
                 'action':'load', 
                 'artifact':'_generic-hf,9e714821f84c4be3'})
    if r['return']>0: return cmind.embed_error(r)

    i['template_meta'] = r['meta']
    i['model_path'] = r['path']
    i.update(i['model_meta']['desc'])

    rr = utils.load_module(cmind, r['path'], 'modulex.py')
    if rr['return'] >0: return cmind.embed_error(rr)

    return rr['sub_module_obj'].install(i)
