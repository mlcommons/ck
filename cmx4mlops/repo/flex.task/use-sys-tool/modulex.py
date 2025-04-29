# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy
import sys

def run(i):

    ###################################################################
    # Prepare flow

    misc = i['misc']
    cmind = i['cmind']
    state = i['state']

    out = misc.get('out', '')
    console = misc.get('console', False)

    self_meta = misc['meta']
    self_path = misc['path']

    # Prepare aux input
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)
    quiet = _input2.get('quiet', False)

    new = _input2.get('new', False)
    renew = _input2.get('renew', False)

    env = _input2.get('env', {})

    dep_alias = _input2.get('alias', '')

    self_task_alias = misc['flex.task_alias']

    # Prepare main input
    _input = i['input']

    if 'use-system-tool-log' not in state['cmx']:
       state['cmx']['use-system-tool-log'] = []

    state['cmx']['use-system-tool-log'].append(_input)

    name = _input.get('name', '')

    package = _input.get('package', '')
    package_ext = _input.get('package_ext', '')
    path = _input.get('path', '')

    skip_search = _input.get('skip_search', False)

    test_version  = _input.get('test_version', False)

    force_version = _input.get('version', '')

    version_min = _input.get('version_min', '')
    if version_min != '':
        version_min2 = [utils.digits(v) for v in version_min.split('.')]

    version_max = _input.get('version_max', '')
    if version_max != '':
        version_max2 = [utils.digits(v) for v in version_max.split('.')]

    install_prefix = _input.get('install_prefix', '')
    install_postfix = _input.get('install_postfix', '')
    install_flags = _input.get('install_flags', '')
    install_url = _input.get('install_url', '')

    reinstall = _input.get('reinstall', False)
    if renew: reinstall = True

    clean = _input.get('clean', False)

    use_compute = _input.get('use_compute', False)
    use_compute_name = _input.get('compute_name', '')
    use_compute_tags = _input.get('compute_tags', '')



    run_cmd = misc['helpers']['run_cmd']
    parse_version = misc['helpers']['parse_version']

    # Check available names
    artifact_tags = _input.get('name', '')

    if verbose:
        print ('')
        print (f'INFO Use sys tool "{artifact_tags}"')

    r = cmind.x({'automation': self_meta['use']['flex.common'],
                 'action': 'select_artifact',
                 'selected_text': 'Select System Tool',
                 'selected_automation': self_meta['use']['flex.sys-tool'],
                 'selected_tags': artifact_tags,
                 'quiet': quiet,
                 'control':{'out':out}})

    if r['return']>0: return cmind.embed_error(r)

    sys_tool_object = r['selected_artifact_object']

    sys_tool_meta = sys_tool_object.meta
    sys_tool_path = sys_tool_object.path

    name = sys_tool_meta.get('name', '')
    if name == '': name = sys_tool_meta['alias']
    desc = sys_tool_meta['desc']

    cmd_prefix_from_state = desc.get('cmd_prefix_from_state', [])


    # Check if has extra processing automation
    # for complex processing of paths and ENVs
    r = utils.load_module(cmind, sys_tool_path, 'modulex.py')
    if r['return'] >0: return cmind.embed_error(r)

    sub_module_obj = r['sub_module_obj']
    sub_module_path = r['sub_module_path']

    ###############################################################
    # Check deps
    deps = desc.get('deps', [])

    sc = {}
    if use_compute or use_compute_name != '' or use_compute_tags != '':
        sc = {'tags':'use,compute', 'alias':'compute'}
        if use_compute_tags != '':
            sc['compute_tags'] = use_compute_tags
        if use_compute_name != '':
            sc['name'] = use_compute_name
        deps.append(sc)

    tmp_deps = {}

    if len(deps)>0:
        process_deps = misc['helpers']['process_deps']

        r = process_deps(cmind, deps, state, misc['flex.task'],
                         verbose = verbose, console = console, quiet = quiet, 
                         tmp = {})
        if r['return'] >0: return r

        tmp_deps = r['tmp']



    ###############################################################
    # Check if in cache
    cache_tags = misc['cache_tags']
    cache_meta = misc['cache_meta']

    sys_tool_tags = sys_tool_meta['tags']
    for tag in sys_tool_tags:
        if cache_tags != '': cache_tags += ','
        cache_tags += f'_name.{tag}'

    tool = ''
    if package != '':
        tool = package
        if cache_tags != '': cache_tags += ','
        cache_tags += f'_package.{package}'

    # If package != ''
    if renew:
        cache_tags = remove_key_from_tags(cache_tags, '_version.')
    elif force_version != '':
        cache_tags = remove_key_from_tags(cache_tags, '_version.')
        if cache_tags != '': cache_tags += ','
        cache_tags += f'_version.{force_version}'


    prepare_work_dir = misc['helpers']['prepare_work_dir']

    if verbose:
        if force_version != '' or version_min != '' or version_max != '':
            x = ''
            if version_min != '':
                x += f' >={version_min}'
            if force_version != '':
                x += f' =={force_version}'
            if version_max != '':
                x += f' <= {version_max}'

            print ('')
            print (f'INFO version requested{x}')

    r = prepare_work_dir(cmind, console, misc['cache_automation'], 
                         True, cache_tags, cache_meta, 
                         quiet = quiet,
                         verbose = verbose,
                         renew = renew,
                         new = new,
                         version = force_version,
                         version_min = version_min,
                         version_max = version_max,
                         cache_name_prefix = self_task_alias)
    if r['return'] > 0: return cmind.embed_error(r)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # If cached, return cached output and workdir
    if len(r.get('output', {})) > 0:
        output = r['output']

        update_state(cmind, output, desc, state, sub_module_obj, name)

        key_tool_version = f'sys_tool_{name}_version'
        key_tool_with_path = f'sys_tool_{name}_with_path'

        tool_with_path = output.get(key_tool_with_path)

        version = output.get(key_tool_version)

        # Test again installed version (useful for PIP that may change)
        finish = True

        if test_version:
            rx = detect_version(cmind, state, env, desc, tmp_deps,
                               tool_with_path, package, console, verbose, 
                               cmd_prefix_from_state, run_cmd, 
                               parse_version, version, 
                               version_min, version_max,
                               sub_module_obj, sub_module_path)
            if rx['return'] > 0: 


                if rx['return'] != 2: return cmind.embed_error(rx)

                finish = False
                reinstall = True
                force_version = version

            if finish and len(rx['found_path_with_version']) == 0:
                new_version = rx['version']
                finish = False
                reinstall = True
                force_version = version

                return cmind.prepare_error(1, f'installed version (V{new_version}) doesn\'t match flex.cache version (V{version})')

                if console and verbose:
                    print ('')
                    print (f'installed version (V{new_version}) didn\'t match flex.cache version (V{version})')


        if finish:
            if console and verbose and version != None and tool_with_path != None:
                print ('')
                print (f'Selected tool "{tool_with_path} (V{version})"')

            x = artifact_tags
            if package != '': x += '--' + package

            add_version_to_state(state, x, version, dep_alias)

            return r




    ##############################################################
    # Resume
    cache_uid = r['cache_uid']

    rr = {'return':0,
          '_update_cache_uid':cache_uid,
          '_update_cache_meta':cache_meta,
          '_update_cache_tags':cache_tags
         }

    if desc.get('skip_if_not_windows', False) and os.name != 'nt':
        # Skip
        return rr

    if desc.get('skip_if_windows', False) and os.name == 'nt':
        # Skip
        return rr





    stdout = ''
    stderr = ''



    # Check if path is specified
    if tool != '': 
        tools = [tool]
    else:
        if 'tool' not in desc:
            return cmind.prepare_error(1, 'tool and package are not specified')

        tools = desc['tool'].split(',')

    tool_with_path = ''
    found_paths = []

    if path != '':
        if path == '{{sys.executable}}':
            path = sys.executable
        else:
            path = os.path.abspath(path)

        if os.path.isfile(path):
            found_paths.append(path)
        else:
            for tool in tools:
                if os.name == 'nt' and not desc.get('skip_windows_exe_prefix', False):
                    tool += '.exe'

                xpath = os.path.join(path, tool)

                if os.path.isfile(xpath) and xpath not in found_paths:
                    found_paths.append(xpath)

    else:
        # Search for tool
        if skip_search or desc.get('skip_search', False):
            if desc.get('skip_search', False):
                # For pip
                found_paths = [tools[0]]

        else:
            for tool in tools:

                tool = tool.strip()

                tool = tool.replace('{{system.os.bits}}', str(state['system']['os']['bits']))

                if os.name == 'nt' and not desc.get('skip_windows_exe_prefix', False):
                    tool += '.exe'

                if os.name == 'nt':
                    where = 'where'
                else:
                    where = 'which'

                cmd = where + ' ' + tool

                where_found = False

                r = run_cmd(cmind, console, cmd, env, None, capture_output = True, 
                            state = state, verbose = verbose,
                            cmd_prefix_from_state = cmd_prefix_from_state)
                if r['return'] == 0:
                    paths = r['stdout'].strip().split('\n')

                    if len(paths) >0:
                        for xpath in paths:
                            if os.path.isfile(xpath):
                                found_paths.append(xpath)

                if os.name == 'nt':
                    suggested_paths = desc.get('suggested_paths_windows', [])
                else:
                    suggested_paths = desc.get('suggested_paths', [])

                if len(suggested_paths)>0:
                    import glob
                    for sp in suggested_paths:
                        if os.name == 'nt':
                           if sp.startswith('/'): 
                               continue
                        elif len(sp)>1 and sp[1] == ':': 
                           continue

                        search_path = sp + os.sep + tool

                        if verbose:
                            print ('')
                            print (f"INFO Searching in {search_path}")

                        elif console and '*' in search_path:
                            print ('')
                            print (f"Warning: potentially long search in {search_path} ..")



                        files = glob.glob(search_path, recursive = True)
                        if len(files) > 0:
                            for f in files:
                                if f not in found_paths:
                                    found_paths.append(f)


    # Check versions
    found_paths_with_versions = []
    call_tool_with_path = ''

    if not reinstall and not renew:
        for tool_with_path in found_paths:
             r = detect_version(cmind, state, env, desc, tmp_deps,
                                tool_with_path, package, console, verbose, 
                                cmd_prefix_from_state, run_cmd, 
                                parse_version, force_version, 
                                version_min, version_max,
                                sub_module_obj, sub_module_path)

             stdout = r.get('stdout', '')
             stderr = r.get('stderr', '')

             if r['return'] > 0:
                 if r['return'] == 2: continue
                 return cmind.embed_error(r)

             if verbose and r.get('version', '') != '':
                 print ('')
                 print (f"INFO detected version: {r['version']}")

             found_path_with_version = r['found_path_with_version']
             call_tool_with_path = r['call_tool_with_path']

             if len(found_path_with_version)>0:
                 found_paths_with_versions.append(found_path_with_version)



    ###########################################################
    # Handle not found
    if len(found_paths_with_versions) == 0:

        x = f' ({package})' if package !='' else ''
        y = '' if force_version == '' else f' with version {force_version}'
        tool_not_found = f'tool "{name}{x}" not found{y}'


        # Check if has install recipe
        if sub_module_obj != None and hasattr(sub_module_obj, 'install'):
            cmind.log(f"use-sys-tool: call 'install' in {sub_module_path}", "info")

            r = sub_module_obj.install({'automation_flex_task_sys_tool':self_meta['use']['flex.sys-tool'],
                                        'cmind': cmind,
                                        'state': state,
                                        'misc': misc,
                                        'env': env,
                                        'tmp': tmp_deps,
                                        'tool': tool,
                                        'package': package,
                                        'package_ext': package_ext,
                                        'version':force_version,
                                        'version_min': version_min,
                                        'version_max': version_max,
                                        'install_prefix': install_prefix,
                                        'install_postfix': install_postfix,
                                        'install_flags': install_flags,
                                        'install_url': install_url,
                                        'reinstall': reinstall,
                                        'out': out,
                                        'verbose': verbose,
                                        'quiet': quiet,
                                        'tool_not_found': tool_not_found,
                                        'self_meta': self_meta,
                                        'clean': clean})
            if r['return'] > 0: return r

            cmds = r.get('cmds', [])
            tool_with_path = r.get('tool_with_path', '')

            if len(cmds)>0 or tool_with_path != '':

                # Run commands
                for cmd in cmds:
                    capture_output = False if verbose else True
                    r = run_cmd(cmind, console, cmd, env, None, capture_output = capture_output, 
                                state = state, verbose = verbose,
                                cmd_prefix_from_state = cmd_prefix_from_state)
                    if r['return'] >0: return r

                # If success, check version again
                r = detect_version(cmind, state, env, desc, tmp_deps,
                                   tool_with_path, package, console, verbose, 
                                   cmd_prefix_from_state, run_cmd, 
                                   parse_version, force_version, 
                                   version_min, version_max,
                                   sub_module_obj, sub_module_path)
                if r['return'] == 0:

                    found_path_with_version = r['found_path_with_version']
                    call_tool_with_path = r['call_tool_with_path']

                    if len(found_path_with_version)>0:
                        found_paths_with_versions.append(found_path_with_version)



    ###########################################################
    # Handle not found

    if len(found_paths_with_versions) == 0:

        if verbose:
            std = '\n' + stdout + '\n' + stderr
            print ('')
            print ('Captured console output from version detection:')
            print (std)

        return cmind.prepare_error(1, tool_not_found)



    ###########################################################
    # Finalize

    if len(found_paths_with_versions) == 1:
        index = 0

    else:
        lst = []

        found_paths_with_versions = sorted(found_paths_with_versions, 
                                           key = lambda x: x['version2'],
                                           reverse = True)

        for found_path in found_paths_with_versions:
            lst.append(f"V{found_path['version']} - {found_path['tool_with_path']}")

        r = cmind.x({'automation': self_meta['use']['flex.common'],
                     'action': 'select_from_list',
                     'text': 'Select a tool',
                     'list': lst,
                     'quiet': quiet,
                     'control':{'out':out}})
        if r['return']>0: return cmind.embed_error(r)

        index = r['index']

    rrr = found_paths_with_versions[index]['parse_version']

    tool_with_path = found_paths_with_versions[index]['tool_with_path']
    x_tool_with_path = found_paths_with_versions[index]['x_tool_with_path']
    tool = os.path.basename(tool_with_path)

    if verbose and package != '':
        print ('')
        print (f"INFO Selected tool with path: {tool_with_path}")

    version = rrr['version']

    cache_meta['version'] = version

#    cache_tags = remove_key_from_tags(cache_tags, '_version.')
#    if cache_tags != '': cache_tags += ','
#    cache_tags += f'_version.{version}'

    rr.update({
               '_update_cache_meta':cache_meta,
               '_update_cache_tags':cache_tags,
               f'sys_tool_{name}_with_path': tool_with_path,
               f'sys_tool_{name}_dirname': os.path.dirname(tool_with_path),
               f'sys_tool_{name}_dirname_x': os.path.dirname(os.path.dirname(tool_with_path)),
               # path2 is with "" if there are spaces
               f'sys_tool_{name}_with_path2': x_tool_with_path,
               f'sys_tool_{name}': tool,
               f'sys_tool_{name}_version': version,
               f'sys_tool_{name}_available': rrr['available']
              })

    if desc.get('call', False):
        rr[f'sys_tool_{name}_with_path_call'] = call_tool_with_path

    update_state(cmind, rr, desc, state, sub_module_obj, name)

    if console:
        print ('')
        print (f'Version {version} detected ({tool_with_path}) and registered in flex.cache: {os.getcwd()}')

        add_version_to_state(state, artifact_tags, version, dep_alias)

    return rr

#################################################
def remove_key_from_tags(cache_tags, key):
    cache_tags_list = cache_tags.split(',')

    new_cache_tags = ''

    for tag in cache_tags_list:
        if not tag.startswith(key):
            if new_cache_tags != '':
                new_cache_tags += ','
            new_cache_tags += tag

    return new_cache_tags

#################################################
def update_state(cmind, i, desc, state, sub_module_obj, name):

    # Complex processing via Python if needed
    if sub_module_obj != None and hasattr(sub_module_obj, 'process'):
        r = sub_module_obj.process({'cmind': cmind,
                                    'output':i,
                                    'desc': desc,
                                    'state': state})
        if r['return'] > 0: 
            i['return'] = r['return']
            i['error'] = r['error']
            return

    # Finish updating state
    update_state = desc.get('update_state', {})

    if len(update_state)>0:
        for key in update_state:

            xvalue = update_state[key]

            if type(xvalue) is str and xvalue.startswith('{{') and xvalue.endswith('}}'):
                value = i.get(xvalue[2:-2])
            else:
                value = xvalue

            if '.' in key:
               keys = key.split('.')
               new_state = state

               first = True

               for key in keys[:-1]:
                   if first:
                       first = False

                   if key not in new_state:
                      new_state[key] = {}

                   new_state = new_state[key]

               key = keys[-1]

               target_state = new_state
            else:
               target_state = state

            if key.startswith('+'):
               values = target_state.get(key, [])
               values.append(value)
               target_state[key] = values
            else:
               target_state[key] = value

    # Update output
    state['cmx'][f'sys_tool_{name}'] = i

    return

#################################################
def add_version_to_state(state, tags, version, dep_alias):
    if version != None and version != '':
        if 'versions' not in state['cmx']: state['cmx']['versions'] = {}
        state['cmx']['versions'][f'use-sys-tool--{tags}'] = version

        if 'flow' not in state['cmx']: state['cmx']['flow'] = {}
        if dep_alias != '':
            for alias in dep_alias.split(','):
                if alias not in state['cmx']['flow']: state['cmx']['flow'][alias] = {}
                state['cmx']['flow'][alias]['version'] = version

    return

#################################################
def detect_version(cmind, state, env, desc, tmp_deps,
                   tool_with_path, package, console, verbose, 
                   cmd_prefix_from_state, run_cmd, 
                   parse_version, force_version, 
                   version_min, version_max,
                   sub_module_obj, sub_module_path):


    x_tool_with_path = f'"{tool_with_path}"' if not tool_with_path.startswith('"') \
       and ' ' in tool_with_path else tool_with_path

    call_tool_with_path = ''
    if desc.get('call', False):
        call_tool_with_path = state['system']['os']['call_script'] + ' ' + x_tool_with_path

    version_min2 = [] if version_min == '' else [utils.digits(v) for v in version_min.split('.')]
    version_max2 = [] if version_max == '' else [utils.digits(v) for v in version_max.split('.')]

    if desc.get('tool_version', '') == '':
        rrr = {'available':True, 'version':'skip'}
        stdout = ''
        stderr = ''

    else:
        tool_version = desc['tool_version'].replace('{{tool}}', x_tool_with_path)
        tool_version = tool_version.replace('{{package}}', package)

        j = tool_version.find('{{deps.')
        if j>=0:
           j1 = tool_version.find('}}')
           if j1>=0:
              k = tool_version[j+7:j1]
              v = tmp_deps[k]

              tool_version = tool_version[:j] + v + tool_version[j1+2:]

        if desc.get('call', False):
            tool_version = call_tool_with_path + ' && ' + tool_version 

        r = run_cmd(cmind, console, tool_version, 
                    env, None, capture_output = True, 
                    state = state, verbose = verbose, 
                    cmd_prefix_from_state = cmd_prefix_from_state)

        stdout = r.get('stdout', '')
        stderr = r.get('stderr', '')

        if r['return']>0: 
            return {'return':2, 'error':'version not detected', 
                    'stdout':stdout, 
                    'stderr':stderr}

#        print (stdout)
#        print (stderr)

        # Parse version
        match_version = desc.get('match_version', '')

        match_versions = desc.get('match_versions', [])
        if match_version != '':
            match_versions.append(match_version)

        match_group = desc['match_group']

        for match_version in match_versions:
            rrr = parse_version(r, match_version, match_group)

            cmind.log(f"x flex.task parse_version output: {rrr}", "debug")

            if rrr['return'] == 0 and rrr.get('available', False):
                break

        found_path_with_version = {}

    # Check if has specialization function
    if sub_module_obj != None and hasattr(sub_module_obj, 'detect_version'):
        cmind.log(f"use-sys-tool: call 'detect_version' in {sub_module_path}", "info")

        r = sub_module_obj.detect_version({'cmind': cmind,
                                           'state': state,
                                           'env': env,
                                           'desc': desc,
                                           'tool_with_path': tool_with_path,
                                           'pre_version': rrr})
        if r['return'] > 0: return r

    version = ''
    if rrr.get('available', False):
        version = rrr['version']

        version2 = [utils.digits(v) for v in version.split('.')]

        # Check versions
        add = True

        if force_version != '' and force_version != version:
            add = False

        if add and len(version_min2)>0 and version2 < version_min2:
            add = False

        if add and len(version_max)>0 and version2 > version_max2:
            add = False

        if add:
            found_path_with_version = {'tool_with_path': tool_with_path,
                                       'x_tool_with_path': x_tool_with_path,
                                       'version': version,
                                       'version2': version2,
                                       'parse_version': rrr}


    return {'return':0, 
            'found_path_with_version': found_path_with_version, 
            'call_tool_with_path': call_tool_with_path,
            'version': version,
            'stdout': stdout,
            'stderr': stderr}
