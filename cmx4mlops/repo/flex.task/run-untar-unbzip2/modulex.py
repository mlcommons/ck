# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy

def run(i):

    ###################################################################
    # Prepare flow

    cmind = i['cmind']
    state = i['state']
    tmp = i['tmp']

    misc = i['misc']
    console = misc.get('console', False)
    self_meta = misc['meta']
    run_cmd = misc['helpers']['run_cmd']

    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)

    _input = i['input']

    _file = _input.get('file', '')
    clean = _input.get('clean', False)

    if _file == '':
        return cmind.prepare_error(1, 'file is not specified')

    if not os.path.isfile(_file):
        return cmind.prepare_error(1, f'{_file} doesn\'t exist')

    bin_tar = tmp['sys_tool_tar_with_path2']
    bin_bzip2 = tmp['sys_tool_bzip2_with_path2']

    _file1 = _file[:-8]

    input_dir2 = utils.path2(_file1)
    input_dir3 = _file1 + '.tar'
    input_dir4 = utils.path2(input_dir3)
    input_dir5 = input_dir3 + '.bz2'
    input_dir6 = utils.path2(input_dir5)



    cmds = []
    cmds.append(f'{bin_bzip2} -d {input_dir6}')
    cmds.append(f'{bin_tar} xvf {input_dir4}')

    for cmd in cmds:
        r = run_cmd(cmind, console, cmd, {}, None, state = state, verbose = verbose)
        if r['return']>0: return r

    if clean:
        os.remove(input_dir3)

    return {'return':0}
