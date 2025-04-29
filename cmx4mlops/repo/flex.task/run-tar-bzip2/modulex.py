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

    input_dir = _input.get('input', '')
    md5sum = _input.get('md5sum', False)

    if input_dir == '':
        return cmind.prepare_error(1, 'input directory is not specified')

    if not os.path.isdir(input_dir):
        return cmind.prepare_error(1, f'{input_dir} doesn\'t exist')


    bin_tar = tmp['sys_tool_tar_with_path']
    bin_bzip2 = tmp['sys_tool_bzip2_with_path']

    input_dir2 = utils.path2(input_dir)
    input_dir3 = input_dir + '.tar'
    input_dir4 = utils.path2(input_dir3)
    input_dir5 = input_dir3 + '.bz2'
    input_dir6 = utils.path2(input_dir5)



    cmds = []
    cmds.append(f'{bin_tar} cf {input_dir4} {input_dir2}')
    cmds.append(f'{bin_bzip2} {input_dir4}')

    for cmd in cmds:
        r = run_cmd(cmind, console, cmd, {}, None, state = state, verbose = verbose)
        if r['return']>0: return r

    if md5sum:
        bin_md5sum = tmp['sys_tool_md5sum_with_path2']
        cmd = f'{bin_md5sum} {input_dir6}'

        r = run_cmd(cmind, console, cmd, {}, None, state = state, verbose = verbose, capture_output = True)
        if r['return']>0: return r

        md5sum_output = r['stdout'].strip()

    ###################################################################
    # Check size
    fsize = os.path.getsize(input_dir5)

    rr = {'return':0, 'path_to_tar_bzip2_file': input_dir5,
                      'features':{'size': fsize}}

    if md5sum:
        rr['features']['md5sum'] = md5sum_output

    return rr
