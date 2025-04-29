# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy

def run(i):

    ###################################################################
    # Prepare flow

    cmind = i['cmind']
    misc = i['misc']

    if os.name != 'nt':
        return {'return': 1, 'error': f"this task can run only on Windows: {misc['path']}"}

    out = misc.get('out', '')
    console = misc.get('console', False)

    self_meta = misc['meta']

    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)

    _input = i['input']

    # If on Windows
    #  * check that long file names are on
    #  * download and set up extra tools

    workdir = os.getcwd()

    _vars = self_meta['vars']['downloads']

    urls = _vars['urls']
    md5sums = _vars['md5sums']

    for u in range(0, len(urls)):
        # Call Flex Task to download and cache file
        r = cmind.x({'action':'run',
                     'automation':misc['flex.task'],
                     'control':{'out':out},
                     'verbose': verbose,
                     'tags':'download,file',
                     'url': urls[u],
                     'md5sum': md5sums[u],
                     'tool': 'cmx', # need internal tool
                     'unzip': True,
                     'clean': True,
                     'clean_after_unzip': True,
                    })

        if r['return'] >0 : return r

    path_to_bin = os.path.join(workdir, 'bin')

    if not os.path.isdir(path_to_bin):
        return {'return': 1, 'error': f"path {path_to_bin} was not created by {misc['path']}"}

    return {'return':0, 'path_to_bin': path_to_bin}
