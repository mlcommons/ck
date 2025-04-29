# Author and developer: Grigori Fursin

from cmind import utils

import os
import sys


def install(i):

    quiet = i['quiet']
    verbose = i['verbose']
    out = i['out']
    clean = i['clean']

    tool_not_found = i['tool_not_found']

    if not quiet:
        print ('')
        y = f'WARNING {tool_not_found} - attempt to install (Y/n): '
        x = input(y).strip().lower()

        if x in ['n', 'no']:
            return {'return':0}

    state = i['state']
    cmind = i['cmind']
    self_meta = i['self_meta']
    misc = i['misc']

    version = i.get('version', '')
# TBD: version ranges
#    version_min = i.get('version_min', '')
#    version_max = i.get('version_max', '')

    uname = state['system']['os']['uname']
    uarch = state['system']['os']['uarch']

    if uarch == 'x86_64': uarch = 'amd64'
    elif uarch == 'aarch64': uarch = 'arm64'

    if uname == 'darwin': uname = 'osx'

    ext = f'{uname}-{uarch}'

    if version == '':
        filename0 = f'rclone-current-{ext}'
        url0 = '/'
    else:
        filename0 = f'rclone-v{version}-{ext}'
        url0 = f'/v{version}/'

    filename = filename0 + '.zip'

    url = 'https://downloads.rclone.org' + url0 + filename

    if verbose:
        print ('')
        print (f'URL {url}')

    # Download and clone
    r = cmind.x({'action': 'run',
                 'automation': misc['flex.task'],
                 'tags': 'download,file',
#                 'cache': True,
#                 'cache_tags': 'install_sys_tool',
                 'url': url,
                 'filename': filename,
                 'unzip': True,
                 'strip_folders': 1,
                 'clean': clean,
                 'clean_after_unzip': True,
                 'verbose': verbose,
                 'control':{'out':out}})
    if r['return'] >0 : return cmind.embed_error(r)

    path_to_files = r['path_to_files']

    tool = 'rclone.exe' if os.name == 'nt' else 'rclone'

    tool_with_path = os.path.join(path_to_files, tool)

    return {'return':0, 'tool_with_path': tool_with_path}
