# Author and developer: Grigori Fursin

from cmind import utils

import os

def run(i):

    ###################################################################
    # Prepare flow
    state = i['state']

    rt_cached = state['cmx'].get('use_compute', {})
    if len(rt_cached)>0: return rt_cached

    host_os = state['system']['os']

    cmind = i['cmind']
    misc = i['misc']

    out = misc.get('out', '')
    console = misc.get('console', False)

    self_meta = misc['meta']

    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)
    quiet = _input2.get('quiet', False)

    renew = _input2.get('renew', False)
    new = _input2.get('new', False)

    _input = i['input']

    env = _input2.get('env', {})

    # Check available names
    artifact = _input.get('name', '')

    tags = _input.get('compute_tags', '')

    if tags != '': tags += ','
    tags += '_sys_platform.' + host_os['python_sys_platform']

    r = cmind.x({'automation': self_meta['use']['flex.common'],
                 'action': 'select_artifact',
                 'selected_text': 'Select Target Compute',
                 'selected_automation': self_meta['use']['flex.compute'],
                 'selected_artifact': artifact,
                 'selected_tags': tags,
                 'quiet': quiet,
                 'show_tags': True,
                 'control':{'out':out}})

    if r['return']>0: return cmind.embed_error(r)

    compute_object = r['selected_artifact_object']

    compute_meta = compute_object.meta

    device = compute_meta['device']
    pytorch_device = compute_meta.get('pytorch_device', '')
    if pytorch_device == '': pytorch_device = device

    rrr = {'return':0}

    rrr['target_device'] = device
    rrr['target_pytorch_device'] = pytorch_device

    state['cmx']['target_device'] = device
    state['cmx']['target_pytorch_device'] = pytorch_device

    state['cmx']['use_compute'] = rrr

    # Check extra environment variables
    compute_env = compute_meta.get('env', {})
    if len(compute_env) >0:
        state['cmx']['envs'].update(compute_env)

    # Check extra dependencies
    # However, we need to set state['cmx']['use_compute'] 
    # to avoid going to infinite loop if other sub-deps call use-compute ...

    deps = compute_meta.get('deps', {})

    if len(deps)>0:
        process_deps = misc['helpers']['process_deps']

        r = process_deps(cmind, deps, state, misc['flex.task'],
                         verbose = verbose, console = console, quiet = quiet, 
                         tmp = {})
        if r['return'] >0: return r

        rrr['processed_deps'] = r

    # Finalizing use_compute state

    state['cmx']['use_compute'] = rrr

    return rrr
