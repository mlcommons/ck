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
    quiet = _input2.get('quiet', False)
    env = _input2.get('env', {})

    _input = i['input']

    cmd = _input.get('cmd', '')

    container_meta = _input.get('container_meta', '')
    container_file = _input.get('container_file', '')

    docker_tags = _input.get('docker_tags', '')
    docker_artifact = _input.get('docker_name', '')
    docker_uid = _input.get('docker_uid', '')

    target = _input.get('target', '')

    clean = _input.get('clean', False)

    native = _input.get('native', False)

    if container_file == '':
        container_file = 'Dockerfile' if native else 'cmx-rt-container.Dockerfile'

    ###########################################################
    # Prepare container file
    if clean:
        if os.path.isfile(container_meta):
            os.remove(container_meta)
        if os.path.isfile(container_file):
            os.remove(container_file)
  
    docker_sub_file = ''
    if not native and not os.path.isfile(container_meta):

        if docker_tags == '': docker_tags = self_meta.get('docker_tags', '')
        if docker_artifact == '': docker_artifact = self_meta.get('docker_name', '')

        r = cmind.x({'automation': self_meta['use']['flex.common'],
                     'action': 'select_artifact',
                     'selected_text': 'Select docker base',
                     'selected_automation': self_meta['use']['flex.docker'],
                     'selected_artifact': docker_artifact,
                     'selected_tags': docker_tags,
                     'selected_uid': docker_uid,
                     'sub_meta': True,
                     'quiet': quiet,
                     'control':{'out':out}})

        if r['return']>0: return cmind.embed_error(r)

        docker_object = r['selected_artifact_object']

        docker_meta = docker_object.meta
        docker_path = docker_object.path

        docker_sub_file_meta = docker_meta.get('sub_file', {})
        if verbose:
            print ('')
            print (f'DOCKER META FILE: {docker_sub_file_meta}')

        # Check if associated Dockerfile exists for Docker meta
        docker_sub_file = docker_sub_file_meta[:-5] + '.Dockerfile'

    if not os.path.isfile(container_file):
        if not os.path.isfile(docker_sub_file):
            docker_sub_file = os.path.join(misc['path'], 'template.Dockerfile') 

        # Load Dockerfile
        r = utils.load_txt(docker_sub_file)
        if r['return']>0: return cmind.embed_error(r)

        src = r['string']

        # Update Dockerfile src
        docker_meta_desc = docker_meta.get('desc', {})
        for k in self_meta['template_desc']:
            v = self_meta['template_desc'][k] if k not in docker_meta_desc else docker_meta_desc[k]
            kk = '{{' + k + '}}'
            src = src.replace(kk, v)
            
        # Save Dockerfile
        r = utils.save_txt(container_file, src)
        if r['return']>0: return cmind.embed_error(r)

    ###########################################################
    # Prepare docker build CMD

    cmd += f' -f {container_file}'

    target = _input.get('target', '')
    if target != '':
        cmd += f' -t {target}'

    cmd += ' .'

    bin_docker = tmp['sys_tool_docker_with_path2']

    xcmd = f'{bin_docker} build {cmd}'

    ###########################################################
    # Save yaml description
    meta = {'container_file':container_file, 'build_cmd':xcmd, 'target': target}

    r = utils.save_yaml(container_meta, meta)
    if r['return']>0: return cmind.embed_error(r)

    ###########################################################
    # Run docker build

    r = run_cmd(cmind, console, xcmd, env, None, state = state, verbose = verbose)
    if r['return']>0: return cmind.embed_error(r)

    return {'return':0, 'docker_build_cmd':xcmd}
