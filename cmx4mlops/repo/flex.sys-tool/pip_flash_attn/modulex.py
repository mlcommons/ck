# Author and developer: Grigori Fursin

from cmind import utils

import os
import sys


def install(i):

    cmind = i['cmind']
    cmx = i['state']['cmx']
    env = i['env']

    # We should be able to override installation of packages 
    # TBD: do it cleaner via cfg ...
    if 'PIP_BREAK_SYSTEM_PACKAGES' not in env: env['PIP_BREAK_SYSTEM_PACKAGES'] = 1

    install_postfix = i['install_postfix']

    target_device = cmx.get('target_device', '')

    version = i['version']

    ###################################################################
    if target_device == 'rocm' and cmx.get('pip_flash_attn_rocm_use_github', False):
        # https://huggingface.co/docs/optimum/en/amd/amdgpu/overview#flash-attention-2
        # https://github.com/ROCm/flash-attention/issues/42#issuecomment-1928999643
        # https://github.com/ROCm/flash-attention/blob/main/setup.py#L330-L333

        gfx = cmx['detect_rocm_info']['gfx']

        if 'GPU_ARCHS' not in env: env['GPU_ARCHS'] = gfx
        if 'PYTORCH_ROCM_ARCH' not in env: env['PYTORCH_ROCM_ARCH'] = gfx

        xversion = f'@v{version}-cktile' if version != '' else ''

        install_url = install_postfix + f' git+https://github.com/ROCm/flash-attention.git{xversion}'

        i['install_url'] = install_url
        i['install_postfix'] = ''

    ###################################################################
    # Call install in pip_generic
    r = cmind.x({'automation': i['automation_flex_task_sys_tool'],
                 'action':'load', 
                 'tags':'pip_generic'})
    if r['return']>0: return cmind.embed_error(r)

    rr = utils.load_module(cmind, r['path'], 'modulex.py')
    if rr['return'] >0: return cmind.embed_error(rr)

    i['package'] = 'flash_attn'

    return rr['sub_module_obj'].install(i)
