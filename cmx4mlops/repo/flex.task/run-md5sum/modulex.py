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
    _md5sum = _input.get('md5sum', '')

    files = _input.get('files', {})

    if _file != '':
       files[_file] = {}
       if _md5sum != '':
          files[_file]['md5sum'] = _md5sum

    if len(files) == 0:
        return cmind.prepare_error(1, 'file is not specified')

    bin_md5sum = tmp['sys_tool_md5sum_with_path2']

    files_output = {}

    if verbose:
        print ('')
        print ('INFO Checking MD5SUM ...')

    for f in files:

        print (f'INFO File {f}')

        _file2 = utils.path2(f)
        md5sum = files[f].get('md5sum', '')

        cmd = f'{bin_md5sum} {_file2}'

        r = run_cmd(cmind, console, cmd, {}, None, state = state, verbose = verbose, capture_output = True)
        if r['return']>0: return r

        md5sum_output = r['stdout'].strip()

        if md5sum_output.startswith('\\'): md5sum_output = md5sum_output[1:]

        j = md5sum_output.find(' ')
        if j>0: md5sum_output = md5sum_output[:j]

        if md5sum != '' and md5sum_output != md5sum:
            return cmind.prepare_error(1, f'file {f} failed md5sum checksum ({md5sum} != new {md5sum_output})')

        fsize = os.path.getsize(f)

        files_output[f] = {'md5sum': md5sum_output, 'size': fsize}

        if console:
            print (md5sum_output)

    ###################################################################
    # Check size

    rr = {'return':0, 'md5sum':md5sum_output, 'size': fsize, 'files': files_output}

    return rr
