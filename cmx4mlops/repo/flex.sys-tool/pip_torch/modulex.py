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

    if not cmx.get('skip_pytorch_index_url', False) and not '--index-url' in i.get('install_postfix', ''):
        install_postfix = i['install_postfix']

        target_device = cmx.get('target_device', '')

        if target_device  == 'cuda':
            if len(cmx.get('sys_tool_nvcc', {})) == 0:
                return cmind.prepare_error(1, 'target device "cuda" is selected but NVCC is not detected (use "cuda,nvcc" for compute)')

            nvcc_version_split = cmx['sys_tool_nvcc']['sys_tool_nvcc_version'].split('.')

            v0 = int(nvcc_version_split[0]) # (12)
            v1 = int(nvcc_version_split[1]) # (4)

            cu = ''

            if v0 == 11:
                cu = '118'
            elif v0 == 12:
                if v1<4:
                    cu = '121'
                else:
                    cu = '124'

            if cu != '':
                i['install_postfix'] += ' --index-url https://download.pytorch.org/whl/cu' + cu

        elif target_device == 'rocm':

            if len(cmx.get('sys_tool_rocm', {})) == 0:
                return cmind.prepare_error(1, 'target device "rocm" is selected but dependency is not resolved')

            rocm_version_split = cmx['sys_tool_rocm']['sys_tool_rocm_version'].split('.')

            v0 = int(rocm_version_split[0]) # (12)
            v1 = int(rocm_version_split[1]) # (4)

            rocm = str(v0) + '.' + str(v1)
            i['install_postfix'] += ' --index-url https://download.pytorch.org/whl/rocm' + rocm

    # Call install in pip_generic
    r = cmind.x({'automation': i['automation_flex_task_sys_tool'],
                 'action':'load', 
                 'tags':'pip_generic'})
    if r['return']>0: return cmind.embed_error(r)

    rr = utils.load_module(cmind, r['path'], 'modulex.py')
    if rr['return'] >0: return cmind.embed_error(rr)

    package = 'torch' if i.get('force_package', '') == '' else i['force_package']
    i['package'] = package

    return rr['sub_module_obj'].install(i)
