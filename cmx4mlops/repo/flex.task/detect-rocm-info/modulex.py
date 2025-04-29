# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy

def run(i):

    ###################################################################
    # Prepare flow

    cmind = i['cmind']
    state = i['state']

#    rt_cached = state['cmx'].get('detect_rocm_info', {})
#    if len(rt_cached)>0: return rt_cached

    misc = i['misc']
    tmp = i['tmp']

    console = misc.get('console', False)

    self_meta = misc['meta']
    self_path = misc['path']

    cmd_prefix_from_state_compile = self_meta.get('cmd_prefix_from_state_compile', [])

    prepare_work_dir = misc['helpers']['prepare_work_dir']
    run_cmd = misc['helpers']['run_cmd']

    self_task_alias = misc['flex.task_alias']

    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)
    quiet = _input2.get('quiet', False)
    new = _input2.get('new', False)
    renew = _input2.get('renew', False)
    env = _input2.get('env', {})

    _input = i['input']

    timeout = _input.get('timeout', None)
    _min = _input.get('min', False)

    ###############################################################
    # Check if in cache
    rocm_version = state['cmx']['sys_tool_rocm']['sys_tool_rocm_version']

    cache_tags = misc['cache_tags']
    cache_meta = misc['cache_meta']

    tag = f'_version.{rocm_version}'
    if tag not in cache_tags:
        cache_tags += ','+tag

    r = prepare_work_dir(cmind, console, misc['cache_automation'], 
                         True, cache_tags, cache_meta, 
                         quiet = quiet,
                         verbose = verbose,
                         renew = renew,
                         new = new,
                         cache_name_prefix = self_task_alias)
    if r['return'] > 0: return cmind.embed_error(r)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # If cached, return cached output and workdir
    if len(r.get('output', {})) > 0:
        # Update state
        state['cmx']['detect_rocm_info'] = r['output']
        return r

    ##############################################################
    # Resume
    cache_uid = r['cache_uid']

    rr = {'return':0,
          '_update_cache_uid': cache_uid,
          '_update_cache_meta': cache_meta,
          '_update_cache_tags': cache_tags
         }

    rrr = {'return':0}

    ###################################################################
    rocminfo = state['cmx']['sys_tool_rocm']['sys_tool_rocm_with_path2']

    cmd = f'{rocminfo}'

    r = run_cmd(cmind, console, cmd, env, timeout, 
                state = state, verbose = verbose, capture_output = True,
                cmd_prefix_from_state = cmd_prefix_from_state_compile)
    if r['return']>0: return r

    stdout = r['stdout'].split('\n')

    devices = []

    name = ''
    gfx = ''

    device = {}
    gpu_detected = False

    for l in stdout:
        l = l.strip()
        l1 = l.lower()

        if l1.startswith('uuid') and 'gpu-' in l1:
            gpu_detected = True

        if l1.startswith('agent '): 
            if len(device)>0 and gpu_detected:
                devices.append(device)
            device = {}
            gpu_detected = False

        if gpu_detected:
            if l1.startswith('marketing name: '):
                name = l[16:].strip()
                device['_name'] = name

        j = l1.find(' gfx')
        if j>=0: 
            gfx = l1[j+1:]
            device['_gfx'] = gfx

    if len(device)>0 and gpu_detected:
        devices.append(device)

    rrr = {'return':0}

    rrr['devices'] = devices
    rrr['name'] = name
    rrr['gfx'] = gfx

    state['cmx']['detect_rocm_info'] = rrr
    rr.update(rrr)

    return rr
