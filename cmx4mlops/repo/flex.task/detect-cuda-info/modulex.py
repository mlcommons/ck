# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy

def run(i):

    ###################################################################
    # Prepare flow

    cmind = i['cmind']
    state = i['state']

#    rt_cached = state['cmx'].get('detect_cuda_info', {})
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
    nvcc_version = state['cmx']['sys_tool_nvcc']['sys_tool_nvcc_version']

    cache_tags = misc['cache_tags']
    cache_meta = misc['cache_meta']

    tag = f'_version.{nvcc_version}'
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
        state['cmx']['detect_cuda_info'] = r['output']
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

    nvidia_smi = state['cmx']['sys_tool_nvidia_smi']['sys_tool_nvidia_smi_with_path2']

    cmd = f'{nvidia_smi} --version'

    r = run_cmd(cmind, console, cmd, env, timeout, 
                state = state, verbose = verbose, capture_output = True,
                cmd_prefix_from_state = cmd_prefix_from_state_compile)
    if r['return']>0: return r

    stdout = r['stdout'].split('\n')

    rrr['versions'] = {}
    for l in stdout:
        l1 = l.strip().lower()
        l2 = l1.split(' : ')
        if len(l2) == 2:
            key = l2[0].strip().replace(' ','_')
            value = l2[1].strip()
            rrr['versions'][key] = value

    cmd = f'{nvidia_smi} -L'

    r = run_cmd(cmind, console, cmd, env, timeout, 
                state = state, verbose = verbose, capture_output = True,
                cmd_prefix_from_state = cmd_prefix_from_state_compile)
    if r['return']>0: return r

    stdout = r['stdout'].split('\n')

    devices = []
    name = ''

    for l in stdout:
        if l.lower().startswith('gpu '):
            j1 = l.find(':')
            j2 = l.find('(')
            if j1>0 and j2>j1:
                name = l[j1+1:j2].strip()
                device = {'_name':name}
                devices.append(device)

    rrr['devices'] = devices
    rrr['name'] = name

    ###################################################################
    if not _min:
        self_path_tmp = os.path.join(self_path, 'tmp')
        if not os.path.isdir(self_path_tmp):
            os.makedirs(self_path_tmp)

        os.chdir(self_path_tmp)

        # Prepare target file
        target_exe = 'a.exe' if os.name == 'nt' else 'a.out'

        if os.path.isfile(target_exe):
            os.remove(target_exe)

        # Compile
        nvcc = state['cmx']['sys_tool_nvcc']['sys_tool_nvcc_with_path2']
        source = os.path.join(self_path, 'src', 'print_cuda_devices.cu')



        flags = '-allow-unsupported-compiler'
        if os.name == 'nt': flags += ' -DWINDOWS'

        cmd = f'{nvcc} {source} {flags}'

        print ('')
        print (cmd)

        r = run_cmd(cmind, console, cmd, env, timeout, 
                    state = state, verbose = verbose,
                    cmd_prefix_from_state = cmd_prefix_from_state_compile)
        if r['return']>0: return r

        cmd = target_exe if os.name == 'nt' else './' + target_exe

        print ('')
        print (cmd)

        r = run_cmd(cmind, console, cmd, env, timeout,
                    state = state, verbose = verbose,
                    cmd_prefix_from_state = [])

        rrr['raw_output'] = r

    state['cmx']['detect_cuda_info'] = rrr
    rr.update(rrr)

    return rr
