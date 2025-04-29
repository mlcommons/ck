# Developer(s): Grigori Fursin

from cmind import utils

import os
import sys

def process(inp):

    i = inp['input']
    object_key = inp['key']

    cmind = i['cmind']
    state = i['state']
    misc = i['misc']
    verbose = i['verbose']
    console = i['console']
    out = 'con' if console else ''
    quiet = i['quiet']

    new = i.get('new', False)
    renew = i.get('renew', False)

    object_meta = i[object_key + '_meta']

    # Check meta and if exists
    path = i.get('path', '')

    rclone_drive = object_meta['rclone_drive']
    rclone_filename = object_meta['rclone_filename']

    files = object_meta.get('files', '')

    if path == '': path = os.getcwd()

    final_path = os.path.join(path, os.path.basename(rclone_filename))

    cmx_file = os.path.join(final_path, 'cmx-status.json')

    exists = False

    if not renew and os.path.isfile(cmx_file):
        exists = True

        r = utils.load_json(cmx_file)
        if r['return'] > 0: return cmind.embed_error(r)

        return r['meta']

    # Check if has deps
    deps = object_meta.get('deps', {})

    if len(deps) == 0:
       deps = [{'tags': 'use,rclone,mlcommons',
                'alias': 'use_rclone_mlcommons'}]

    if len(deps)>0:
        process_deps = misc['helpers']['process_deps']

        r = process_deps(cmind, deps, state, misc['flex.task'],
                         verbose = verbose, console = console, quiet = quiet, 
                         tmp = {})
        if r['return'] >0: return r


    # Download
    new_files = {}

    if not exists or renew:
        if verbose:
            print ('')
            print (f'INFO Downloading {object_key} to {final_path} ...')

        cmd = f'copy {rclone_drive}:{rclone_filename} {final_path} -P'

        ii = {'automation': misc['flex.task'],
              'tags': 'run,rclone',
              'action': 'run',
              'cmd': cmd,
              'verbose': verbose,
              'quiet': quiet,
              'control':{'out':out}}

        r = cmind.x(ii)
        if r['return'] > 0: return cmind.embed_error(r)

        if len(files) > 0:
            for f in files:
                new_files[os.path.join(final_path, f)] = files[f]

            r = cmind.x({'automation': misc['flex.task'],
                         'action': 'run',
                         'tags': 'run,md5sum',
                         'files': new_files,
                         'verbose': verbose,
                         'quiet': quiet,
                         'control':{'out':out}})
            if r['return'] > 0: return cmind.embed_error(r)

    rr = {'return':0, 'rclone_drive': rclone_drive, 'rclone_filename': rclone_filename,
                      f'path_to_{object_key}': final_path, 'files': files}

    r = utils.save_json(cmx_file, rr)
    if r['return'] >0: return cmind.embed_error(r)

    return rr
