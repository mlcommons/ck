# Author and developer: Grigori Fursin

from cmind import utils

import os
import sys


def install(i):

    tmp = i['tmp']
    python_with_path2 = tmp['sys_tool_python_with_path2']

    package = i['package']
    package_ext = i.get('package_ext', '')

    version = i.get('version', '')
    version_min = i.get('version_min', '')
    version_max = i.get('version_max', '')

    install_prefix = i.get('install_prefix', '')
    install_postfix = i.get('install_postfix', '')
    install_flags = i.get('install_flags', '')
    install_url = i.get('install_url', '')

    reinstall = i.get('reinstall', False)

    cmds = []

    # Check if reinstall
    if reinstall:
        cmd = f'{python_with_path2} -m pip uninstall -y {package}'
        cmds.append(cmd)

    # Prepare install
    xprefix = '' if install_prefix == '' else install_prefix + ' '
    xpostfix = '' if install_postfix == '' else ' ' + install_postfix

    xversion = ''
    if version != '':
        xversion = f'=={version}'
    else:
       if version_min != '':
           xversion += f'>={version_min}'
       if version_max != '':
           if xversion != '': xversion += ','
           xversion += f'<={version_max}'

    xinstall_flags = '' if install_flags == '' else ' ' + install_flags

    cmd = f'{xprefix}{python_with_path2} -m pip install'

    if install_url != '':
        cmd += ' ' + install_url
    else:
        cmd += f'{xinstall_flags} "{package}{package_ext}{xversion}"{xpostfix}'

    cmds.append(cmd)

    return {'return':0, 'cmds':cmds, 'tool_with_path':package}
