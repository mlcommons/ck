# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy

def run(i):

    ###################################################################
    # Prepare flow

    cmind = i['cmind']
    state = i['state']

    misc = i['misc']

    console = misc.get('console', False)

    self_meta = misc['meta']

    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)

    _input = i['input']

    env = _input2.get('env', {})
    url = _input.get('url', '')
    directory = _input.get('directory', '')
    branch = _input.get('branch', '')
    new_branch = _input.get('new_branch', '')
    fetch = _input.get('fetch', '')
    checkout = _input.get('checkout', '')
    update_submodules = _input.get('update_submodules', False)
    clean = _input.get('clean', False)
    timeout = _input.get('timeout', None)
    depth = _input.get('depth', '')

    # Check input correctness
    if url == '':
        return cmind.prepare_error(1, 'URL is empty')

    if directory == '':
        url1 = url
        if url1.endswith('.git'):
            url1 = url1[:-4]

        directory = os.path.basename(url1)

    if timeout == '': timeout = None

    new = False
    if new_branch != '':
        branch = new_branch
        new = True

    ###################################################################
    workdir = os.getcwd()

    if os.path.isabs(directory):
        path_to_git_repo = directory
    else:
        path_to_git_repo = os.path.join(workdir, directory)

    if os.path.isdir(path_to_git_repo):
        if clean:
            if verbose:
                print ('')
                print (f'RUN rm {path_to_dir_repo}')

            import shutil
            shutil.rmtree(path_to_dir_repo)

    ########\###########################################################
    # Prepare CMDs
    run_cmd = misc['helpers']['run_cmd']

    xdepth = f' --depth {depth}' if depth != '' else ''

    if not os.path.isdir(path_to_git_repo):
        cmd = f'git clone {url} {directory}{xdepth}'

        r = run_cmd(cmind, console, cmd, env, timeout, state = state, verbose = verbose)
        if r['return']>0: return r

        ###################################################################
        # Prepare output
        if not os.path.isdir(path_to_git_repo):
            return cmind.prepare_error(1, f'Git repo directory was not created: {path_to_git_repo}')

        ###################################################################
        # Fetch, branch and checkout
        cmds = []

        if fetch != '' or branch != '' or checkout != '':
            cmd = f'cd {directory} && git fetch'

            if fetch != '':
                cmd += ' ' + fetch

            if branch != '' or checkout != '':
                cmd += ' && git checkout'

                if new:
                    cmd +=' -b'

                if branch != '':
                    cmd += ' ' + branch

                if checkout != '':
                    cmd += ' ' + checkout

            cmds.append(cmd)

        ###################################################################
        # Submodules update

        if update_submodules:
            cmds.append(f'cd {directory} && git submodule sync')
            cmds.append(f'cd {directory} && git submodule update --init --recursive')

        ###################################################################
        # Run commands
        if len(cmds)>0:
            for cmd in cmds:
                r = run_cmd(cmind, console, cmd, env, timeout, state = state, verbose = verbose)
                if r['return']>0: return r

    ###################################################################
    # Check size
    r = cmind.x({'action':'get_dir_size',
                 'automation':self_meta['use']['flex.common'],
                 'path':path_to_git_repo})
    if r['return']>0: return cmind.embed_error(r)

    return {'return':0, 'path_to_git_repo': path_to_git_repo,
                        'features':{'git_repo_size': r['dir_size']}}
