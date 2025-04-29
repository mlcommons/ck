# Author and developer: Grigori Fursin

from cmind import utils

import os
import sys


def install(i):

    cmind = i['cmind']
    cmx = i['state']['cmx']

    r = cmind.x({'automation': i['automation_flex_task_use_dataset'],
                 'action':'load', 
                 'artifact':'_generic-hf,c7d0e7c8d1834eab'})
    if r['return']>0: return cmind.embed_error(r)

    i['template_meta'] = r['meta']
    i['dataset_path'] = r['path']
    i.update(i['dataset_meta']['desc'])

    rr = utils.load_module(cmind, r['path'], 'modulex.py')
    if rr['return'] >0: return cmind.embed_error(rr)

    return rr['sub_module_obj'].install(i)
