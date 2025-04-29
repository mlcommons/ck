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

    env = _input2.get('env', {})
    drive = _input.get('drive', '')
    skip_reconnect = _input.get('skip_reconnect', False)

    root_folder_id = tmp['rclone_mlcommons_cfg']['rclone_root_folder_id']

    # Configure
    bin_rclone = tmp['sys_tool_rclone_with_path2']

    cmd = f'{bin_rclone} config create {drive} drive config_is_local=false scope=drive.readonly root_folder_id={root_folder_id}'

    print ('')
    r = run_cmd(cmind, console, cmd, env, None, state = state, verbose = verbose)
    if r['return']>0: return r

    # Check flex.cfg:mlperf
#    r = cmind.x({'automation':self_meta['use']['flex.cfg'],
#                 'action':'load',
#                 'artifact':'mlperf'})
#    if r['return'] >0 or not r['meta'].get('rclone_connected', False):
#        reconnect = True

    if not skip_reconnect:
        print ('')

        cmd = f'{bin_rclone} config reconnect {drive}:'

        r = run_cmd(cmind, console, cmd, env, None, state = state, verbose = verbose)
        if r['return']>0: return r

#        r = cmind.x({'automation':self_meta['use']['flex.cfg'],
#                     'action':'update',
#                     'artifact':'mlperf',
#                     'meta':{'rclone_connected':True}})
#        if r['return'] >0: return r

    return {'return':0, 'use_rclone_mlcommons_drive': drive}
