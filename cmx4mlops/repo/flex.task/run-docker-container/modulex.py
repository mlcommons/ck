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
    out = misc.get('out', '')
    console = misc.get('console', False)
    self_meta = misc['meta']
    run_cmd = misc['helpers']['run_cmd']

    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)

    _input = i['input']

    env = _input2.get('env', {})

    cmd = _input.get('cmd', '')

    container_meta = _input.get('container_meta', '')
    container_file = _input.get('container_file', '')

    clean = _input.get('clean', False)

    native = _input.get('native', False)

    if container_file == '':
        container_file = 'Dockerfile' if native else 'cmx-rt-container.Dockerfile'

    it = _input.get('it', False)

    ###########################################################
    # Check if has container meta
    if clean:
        if os.path.isfile(container_meta):
            os.remove(container_meta)

    if not os.path.isfile(container_meta):
        ii = {'action': 'run',
              'automation': misc['flex.task'],
              'tags': f'build,docker,image',
              'control': {'out':out},
              'state': state,
              'verbose': verbose,
              'clean': clean,
              'native': native,
              'container_file': container_file
             }

        for k in ['container_meta', 'target', 'native']:
            if k in _input:
                ii[k] = _input[k]

        r = cmind.x(ii)
        if r['return']>0: return r

    if not os.path.isfile(container_meta):
        return cmind.prepare_error(1, f'Cannot find container meta file: {container_meta}')

    r = utils.load_yaml(container_meta)
    if r['return']>0: return cmind.embed_error(r)

    container_meta = r['meta']

    if it:
        cmd += ' -it'

    target = _input.get('target', '')
    if target == '': target = container_meta.get('target', '')

    if target != '':
        cmd += f' {target}'

    if it:
        cmd += ' /bin/bash'

    bin_docker = tmp['sys_tool_docker_with_path2']

    xcmd = f'{bin_docker} run {cmd}'

    r = run_cmd(cmind, console, xcmd, env, None, state = state, verbose = verbose)
    if r['return']>0: return cmind.embed_error(r)

    return {'return':0}
