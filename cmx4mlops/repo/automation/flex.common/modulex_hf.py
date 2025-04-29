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
    env = i['env']

    new = i.get('new', False)
    renew = i.get('renew', False)

    self_meta = i['self_meta']

    object_meta = i[object_key + '_meta']
    object_path = i[object_key + '_path']

    template_meta = i.get('template_meta', {})
    if len(template_meta) >0:
        object_meta['deps'] = template_meta['deps']

    # Check meta and if exists
    path = i.get('path', '')
    if path == '': path = os.getcwd()

    hf_repo = ''
    repo = i.get('repo', '')
    _dir = i.get('directory', '')
    _extra_dir = i.get('extra_directory', '')
    connect = i.get('connect', False)

    if repo != '':
        repo_split = repo.split('/')
        if len(repo_split) != 2:
            return cmind.prepare_error(1, 'unknown HF repo format')

        user = repo_split[0]
        sub_directory = repo_split[1]

        hf_repo = user + '/' + sub_directory

        directory = user + '_' + sub_directory

    else:
        # Just get list of all HF objects (dataset/model)
        directory = 'all'

    final_path = os.path.join(path, directory)

    if _dir != '':
        final_path = os.path.join(final_path, _dir)

    cmx_file = os.path.join(final_path, 'cmx-status.json')

    exists = False

    if not renew and os.path.isfile(cmx_file):
        exists = True

        r = utils.load_json(cmx_file)
        if r['return'] > 0: return cmind.embed_error(r)

        return r['meta']

    # Check if has deps
    deps = object_meta['deps']

    process_deps = misc['helpers']['process_deps']

    tmp = {}
    r = process_deps(cmind, deps, state, misc['flex.task'],
                     verbose = verbose, console = console, quiet = quiet, 
                     tmp = tmp)
    if r['return'] >0: return r

    tmp = r['tmp']

    python_path = state['cmx']['sys_tool_python']['sys_tool_python_with_path2']

    run_cmd = misc['helpers']['run_cmd']

    # Check if need to connect
    if connect:
        # https://huggingface.co/docs/huggingface_hub/en/guides/cli
        cmd = 'huggingface-cli login'

        secret_token = ''
        r = cmind.x({'automation':self_meta['use']['flex.cfg'],
                     'action':'load',
                     'artifact':'huggingface'})
        if r['return'] == 0:
            secret_token = r['meta'].get('token', '')
            if secret_token != '':
                cmd += f' --token {secret_token}'

        r = run_cmd(cmind, console, cmd, env, None, state = state, verbose = verbose, hide_in_cmd = ['--token '])
        if r['return'] > 0: return cmind.embed_error(r)

    # Call download script

    xrepo = f' --repo {hf_repo}' if hf_repo != '' else ''
    cmd = f'{python_path} {object_path}{os.sep}download.py --data_dir {final_path}{xrepo}'

    r = run_cmd(cmind, console, cmd, env, None, state = state, verbose = verbose)
    if r['return'] > 0: return cmind.embed_error(r)

    final_path_with_extra_dir = os.path.join(final_path, _extra_dir) if _extra_dir != '' else final_path

    rr = {'return':0, f'path_to_{object_key}': final_path_with_extra_dir, 'hf_repo': hf_repo}

    r = utils.save_json(cmx_file, rr)
    if r['return'] >0: return cmind.embed_error(r)

    return rr
