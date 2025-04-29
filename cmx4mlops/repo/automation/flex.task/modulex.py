# Author and developer: Grigori Fursin

import os

from cmind.automation import Automation
from cmind import utils

class CAutomation(Automation):
    """
    Automation actions
    """

    line1 = '*'*60

    ############################################################
    def __init__(self, cmind, automation_file):
        super().__init__(cmind, __file__)

    ############################################################
    def test(self, i):
        """
        Test automation

        Args:
          i (dict): CM input dict

             action (str): CM action
             automation (str): CM automation
             artifact (str): CM artifact
             artifacts (list): list of extra CM artifacts

             control: (dict): various CM control
              (out) (str): if 'con', output to console
              ...

             (flags)
          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          * Output from this automation action

        """

        # Access CM
        print (self.cmind)

        # Print self path
        print (self.path)

        # Print self meta
        print (self.meta)

        # Print self automation module path
        print (self.automation_file_path)

        # Print self automation module path
        print (self.full_path)

        # Print self artifact
        print (self.artifact)

        # Print input

        print ('*'*60)
        print ('Before process_input:')

        import json
        print (json.dumps(i, indent=2))

        print ('*'*60)
        print ('After process_input:')

        r = utils.process_input(i)
        if r['return']>0: return r

        import json
        print (json.dumps(i, indent=2))

        return {'return':0}

    ############################################################
    def add(self, i):
        """
        Add Flex Task (prototype)

        Args:
          i (dict): CMX input
             (artifact): Flex Task artifact name
             (tags): Flex Task tags
             (script): script to add to Flex Task
        """

        import shutil

        control = i['control']

        console = control.get('out', '') == 'con'

        _input = control.get('_input', {})

        tags = str(_input.pop('tags', '')).strip()
        script = _input.pop('script', '')

        r = utils.test_input(_input)
        if r['return']>0: return self.cmind.embed_error(r)

        r = utils.process_input(i)
        if r['return']>0: return self.cmind.embed_error(r)

        # Check Flex Task script
        script_string = ''

        if script != '':
            if not os.path.isfile(script):
                return self.cmind.prepare_error(1, f'file {script} not found')

            r = utils.load_txt(script)
            if r['return'] > 0: self.cmind.embed_error(r)

            script_string = r['string']

        # Check Flex Task arfiact repo and name
        artifact_name = control.get('_artifact', {}).get('name', '')

        if artifact_name == '':
            artifact_name = input('Enter Flex Task name: ').strip()

        if artifact_name == '':
            return self.cmind.prepare_error(1, 'Flex Task name is not specified')

        artifact_repo = control.get('_artifact',{}).get('repo', '')

        artifact = artifact_repo
        if artifact != '': artifact += ':'
        artifact += artifact_name

        # Check task tags
        if tags == '':
            tags = input('Enter Flex Task tags: ').strip()

        if tags == '':
            return self.cmind.prepare_error(1, 'Flex Task unique tags are not specified')

        stags = tags.split(',')

        # Create CMX Flex Task artifact via common action
        i['tags'] = stags
        i['yaml'] = True
        i['control'] = {'common':True}
        # Add 'out':control['out'] to show output

        rr = self.cmind.x(i)
        if rr['return'] >0: return self.cmind.embed_error(rr)

        path = rr['path']

        if console:
            print (f'Flex Task was created in {path}')

        # Copy template and script
        self_path = self.path

        f1 = os.path.join(self_path, 'modulex_template.py')
        f2 = os.path.join(path, 'modulex.py')

        if console:
            print ('* Creating modulex.py ...')

        shutil.copyfile(f1,f2)

        # Checking script
        script_string_win = f'echo Flex Task {artifact_name}'
        script_string_linux = f'echo "Flex Task {artifact_name}"'

        if script_string != '':
            if script.endswith('.bat'):
                script_string_win = script_string
            else:
                script_string_linux = script_string

        if console:
            print ('* Creating run.bat ...')

        r = utils.save_txt(os.path.join(path, 'run.bat'), script_string_win)
        if r['return'] >0: return self.cmind.embed_error(r)

        if console:
            print ('* Creating run.sh ...')

        r = utils.save_txt(os.path.join(path, 'run.sh'), script_string_linux)
        if r['return'] >0: return self.cmind.embed_error(r)

        return rr



    ############################################################
    def rerun(self, i):
        """
        ReRun Flex Task with the last experiment (prototype)
        """

        i['action'] = 'run'

        experiment = i.get('experiment', {})
        if experiment == True:
            experiment = {}

        experiment['rerun'] = True
        experiment['name_date'] = True

        if 'quiet' not in experiment:
            # Always rerun in the last experiment place holder
            experiment['quiet'] = True

        i['experiment'] = experiment

        return self.cmind.x(i)


    ############################################################
    def run(self, i):
        """
        Run Flex Task with experiment wrapping (prototype)

        Args:
          i (dict): CMX input

             (tags) (str): task by tags separated by comma
             (artifact) (str): task by artifact name

             (state) (dict); global task flow state
             (env) (dict): add env to commands

             (output_state) (bool): add state to task output
             (cache_to_state) (str): if !='' cache output to the state with this key
                                     careful that it doesn't take different flags into account!
             (add_to_state) (str): if !='' add output to the state with this key

             (j) (bool): print output json
             (s) (bool): print output json with state
             (v) (bool): print extra info during task flow execution

             (quiet) (bool): if True, make default selections
             (q) (bool): the same as 'quiet'

             (timeout) (bool): TBD: if !=None, timeout

             (cache) (bool): if True, cache task output
             (cache_tags) (str): extra cache tags
             (cache_meta) (dict): extra cache meta

             (renew) (bool): rerun task in existing cache entry
                             (for example, rebuild pytorch)
             (new) (bool): run task in new cache entry

             (experiment) (dict): use and configure flex.experiment


        """

        import copy

        # Check input
        console = i['control'].get('out', '') == 'con'

        _input = i['control'].get('_input', {})

        experiment = _input.pop('experiment', {})
        # If experiment is True and not dict, turn on experiment
        if experiment == True:
            # Get default experiment artifact name (date)
            experiment = {'skip_name':True, 'name_date': True}
            skip_experiment = False
        else:
            skip_experiment = True if len(experiment) == 0 or experiment.get('skip', False) else False

        if skip_experiment:
            i['action'] = 'simple_run'
            return self.cmind.x(i)

        i_copy = copy.deepcopy(i)

        if 'experiment' in i_copy:
            del(i_copy['experiment'])

#        r = utils.parse_cm_object(experiment.get('artifact', ''), 
#                                  decompose = True)
#        if r['return'] >0: return r
#        decomposed_experiment = r['decomposed_object']

        if 'artifact' in experiment:
            experiment['artifact'] = utils.substitute_template(experiment['artifact'], _input)

        experiment['action'] = 'run'
        experiment['automation'] = self.meta['use']['flex.experiment']

        experiment['control'] = {}
        i_copy['control'] = {}

        if console:
            experiment['control']['out'] = 'con'
            i_copy['control']['out'] = 'con'
            i_copy['action'] = 'simple_run'

        experiment['cmx_input'] = i_copy

        return self.cmind.x(experiment)


    ############################################################
    def simple_run(self, i):
        """
        Basic Run Flex Task (prototype)

        Args:
          i (dict): CMX input taken from the 'run' function

        """

        import importlib
        import copy
        import time
        import json

        self_time_start = time.time()

        ###################################################################
        # Process input

        # First level of inputs _input will be passed to associated module
        # Second level of inputs will control the task
        control = i['control']
        _input = control.get('_input', {})

        state = _input.get('state', {})
        alias = _input.get('alias', '')

        check = _input.pop('run_if_state_all', {})
        if check_if_skip(check, state):
            return {'return':0, 'skipped': True}

        update_input_via_alias(alias, state, _input)

        enable = _input.pop('enable', True)
        if not enable: 
            return {'return':0}

        _input2 = {}

        if _input.pop('v', False): _input2['verbose'] = True
        if _input.pop('q', False): _input2['quiet'] = True

        for k in ['env', 'envs', 'genv', 'state', 'tmp', 'run', 'quiet', 'timeout', 
                  'cache', 'cache_tags', 'cache_meta', 'alias',
                  'verbose', 'renew', 'new', 'extra_cmx_output_file']:
            if k in _input:
                _input2[k] = _input.pop(k)

        out = control.get('out', '')
        console = (out == 'con')

        quiet = _input2.get('quiet', False)

        tags = _input.pop('tags', '').strip()
        show_help = _input.pop('help', False)
        output_state = _input.pop('output_state', False)
        cache_to_state = _input.pop('cache_to_state', '')
        add_to_state = _input.pop('add_to_state', '')
        print_state_and_json = _input.pop('s', False)
        print_json = _input.pop('j', False)
        save_versions = _input.pop('save_versions', False)

        extra_cmx_output_file = _input2.get('extra_cmx_output_file', '')
        tmp = _input2.get('tmp', {})
        env = _input2.get('env', {})
        envs = _input2.get('envs', {})
        genv = _input2.get('genv', {})

        ###################################################################
        # Check common vars in the state
        if 'system' not in state: state['system'] = {}
        if 'os' not in state['system']: state['system']['os'] = {}
        if 'cmx' not in state: state['cmx'] = {}
        if 'envs' not in state['cmx']: state['cmx']['envs'] = {}
        if 'genv' not in state['cmx']: state['cmx']['genv'] = {}
        if '+PATH' not in state['cmx']['envs']: state['cmx']['envs']['+PATH'] = []

        if len(envs) > 0:
            state['cmx']['envs'].update(envs)

        # Global env
        if len(genv) > 0:
            state['cmx']['genv'].update(genv)

        windows = True if os.name == 'nt' else False
        state['system']['os']['windows'] = windows
        state['system']['os']['call_script'] = 'call' if windows else '.'
        bat_ext = '.bat' if windows else '.sh'
        state['system']['os']['bat_ext'] = bat_ext
        state['system']['os']['python_os_name'] = os.name

        default_script_name = 'run'
        default_script = f'{default_script_name}{bat_ext}'

        verbose = _input2.get('verbose', False)
        quiet = _input2.get('quiet', False)

        ###################################################################
        # Separate artifact(s) into name and repo
        r = utils.process_input(i)
        if r['return']>0: return self.cmind.embed_error(r)

        self_automation_alias = control['_automation']['name_alias']
        self_automation_name = control['_automation']['name']

        # Select task
        artifact = i.get('artifact', '')

        if tags == '' and ' ' in artifact:
            # Treat artifact as tags separated by space
            tags = artifact.replace(' ', ',')
            artifact = ''

        r = self.cmind.x({'automation': self.meta['use']['flex.common'],
                          'action': 'select_artifact',
                          'selected_text': 'Select Flex Task',
                          'selected_automation': i['automation'],
                          'selected_artifact': artifact,
                          'selected_tags': tags,
                          'quiet': quiet,
                          'control':{'out':out}})
        if r['return']>0: return self.cmind.embed_error(r)

        task_obj = r['selected_artifact_object']
        task_path = task_obj.path
        task_meta = task_obj.meta
        task_alias = task_meta.get('alias', '')
        task_uid = task_meta.get('uid', '')
        task_name = task_alias

        if task_alias == '': 
            task_alias = task_meta.get('uid', '')
        else:
            task_name += ',' + task_meta.get('uid', '')

        default_script_with_path = os.path.join(task_path, "{{script_name}}" + bat_ext)

        call_default_script_with_path = f"{state['system']['os']['call_script']} {default_script_with_path}"

        if verbose:
            print ('')
            print (f'TASK {task_path}')

        ###################################################################
        # Check if help
        input_desc = task_meta.get('input_description', {})
        if show_help:
            if len(input_desc) == 0:
                return {'return':1, 'warning': 'this Flex Task doesn\'t have input description'}

            r = utils.call_internal_module(self, __file__, 'modulex_help', 'print_help', {'meta':task_meta, 'path':task_path})
            if r['return'] > 0: return r

            return {'return':1, 'warning': '', 'error': 'help requested'}


        ###################################################################
        # Check default flags
        for k in input_desc:
            if input_desc[k].get('required', False) and k not in _input:
                x = input_desc[k].get('desc', '')
                if x != '': x = f' ({x})'
                return self.cmind.prepare_error(1, f'Argument "{k}" is required but not provided{x}')

            if 'default' in input_desc[k]:
                if k not in _input:
                    _input[k] = input_desc[k]['default']

            ats = input_desc[k].get('add_to_state', '')
            if ats != '':
                v = _input.get(k)
                if v != None:
                    utils.update_dict_with_flat_key(ats, v, state)

            ate = input_desc[k].get('add_to_env', '')
            if ate != '':
                v = _input.get(k)
                if v != None:
                    env[ate] = v


        ###################################################################
        # Check unknown flags
        if len(input_desc) >0:
            unknown_flags = [k for k in _input if k not in input_desc]

            if len(unknown_flags)>0:
                return {'return':1, 'error': f"unknown flag(s) in {task_path}: {','.join(unknown_flags)}"}

        ###################################################################
        # Check default env
        default_env = task_meta.get('default_env', {})
        if len(default_env) >0:
           for k in default_env:
               if k not in env:
                   env[k] = default_env[k]


        ###################################################################
        # Check if add_output_to_state
        r = {}

        cur_dir = os.getcwd()
        workdir = cur_dir

        if cache_to_state != '':
            v = utils.get_value_from_dict_with_flat_key(cache_to_state, state)

            if v != None and len(v) > 0:
                r['output'] = v

        # If cached in state, skip
        if len(r) == 0:

            ###################################################################
            # Start preparing input to modulex if exists (will be reused in helpers)
            ii = {'cmind': self.cmind,
                  'input': _input,
                  'input2': _input2,
                  'env': env,
                  'state': state,
                  'misc':{'out': out,
                          'control': control,
                          'console': console,
                          'flex.task': self_automation_name,
                          'flex.task_alias': task_alias,
                          'use': self.meta['use'],
                          'meta': task_meta,
                          'path': task_path,
                          'call_default_script_with_path': call_default_script_with_path}
                 }

            ###################################################################
            # Prepare cache and cache tags if needed
            renew = _input2.get('renew', False)
            new = _input2.get('new', False)

            cache_tags = ''
            cache_meta = _input2.get('cache_meta', {})

            cache = task_meta.get('cache', False)
            if 'cache' in _input2:
                cache = _input2['cache']
            ii['misc']['cache'] = cache

            prepare_cache_meta = task_meta.get('prepare_cache_meta', False)

            if cache or prepare_cache_meta:
                cache_uid = ''
                x = task_alias
                if x != task_uid:
                    x += ',' + task_uid
                cache_tags = self_automation_alias + ',' + x

                for t in task_meta.get('tags', []):
                    cache_tags += ',' + t

                extra_cache_tags = _input2.get('cache_tags', '')
                if extra_cache_tags != '':
                    cache_tags += ',' + extra_cache_tags

            if cache:
                # Prepare cache tags from inputs
                add_keys_to_cache_tags = []
                for k in input_desc:
                    if input_desc[k].get('cache_tag', False):
                        add_keys_to_cache_tags.append(k)

                if len(add_keys_to_cache_tags)>0:
                    for k in add_keys_to_cache_tags:
                        v = _input.get(k, '')
                        if v == None: v = ''
                        cache_tags += ',_' + k + '.' + v

            if cache or prepare_cache_meta:
                ii['misc']['cache_tags'] = cache_tags
                ii['misc']['cache_meta'] = cache_meta
                ii['misc']['cache_automation'] = self.meta['use']['flex.cache']

            ###################################################################
            # Prepare workdir including cache if requested
            r = prepare_work_dir(self.cmind, console, self.meta['use']['flex.cache'], 
                                 cache, cache_tags, cache_meta, quiet = quiet,
                                 verbose = verbose, renew = renew, new = new, 
                                 cache_name_prefix = task_alias)
            if r['return'] > 0: return self.cmind.embed_error(r)

        # If cached, return cached output and workdir
        if 'output' in r: 
            rr = r['output']

        else:
            cache_uid = r.get('cache_uid', '')
            workdir = r['workdir']

            ###################################################################
            # Check if simple dependencies
            deps = task_meta.get('deps', [])
            if len(deps) > 0:
                r = process_deps(self.cmind, deps, state, self_automation_name, 
                                 verbose = verbose, console = console, quiet = quiet, 
                                 tmp = tmp)
                if r['return'] >0: return r

                tmp = r['tmp']

            ###################################################################
            # Check if sub-module exists
            r = utils.load_module(self.cmind, task_path, 'modulex.py')
            if r['return'] >0: return self.cmind.embed_error(r)

            sub_module_obj = r['sub_module_obj']
            sub_module_path = r['sub_module_path']

            ###################################################################
            # Check if has module and run function
            rr = {'return':0}

            skip_run_script = False
            update_run_script_env = {}
            update_run_script_name = ''
            update_cache_tags = ''
            finish_cache_from_task = False

            func = 'run'
            if hasattr(sub_module_obj, func):
                call_stack = self.cmind.state.get('call_stack', [])
                call_stack.append({'module':sub_module_path, 'func':func})
                self.cmind.state['call_stack'] = call_stack

                ii['tmp'] = tmp
                ii['misc']['helpers'] = {'prepare_work_dir': prepare_work_dir,
                                         'run_cmd': run_cmd,
                                         'process_deps': process_deps,
                                         'parse_version': parse_version
                                        }

                r = sub_module_obj.run(ii)
                if r['return'] >0:
                    if 'module_path' in r:
                        return r
                    else:
                        return self.cmind.embed_error(r)

                skip_run_script = r.pop('_skip_run_script', False)
                update_run_script_env = r.pop('_update_run_script_env', {})
                update_run_script_name = r.pop('_update_run_script_name', '')
                update_cache_uid = r.pop('_update_cache_uid', '')
                update_cache_meta = r.pop('_update_cache_meta', {})
                update_cache_tags = r.pop('_update_cache_tags', '')

                update_extra_cmx_output_file = r.pop('update_extra_cmx_output_file', '')
                if update_extra_cmx_output_file != '': extra_cmx_output_file = update_extra_cmx_output_file

                if update_cache_uid != '': cache_uid = update_cache_uid
                update_cache_meta = r.pop('_update_cache_meta', {})
                if len(update_cache_meta) >0: cache_meta = update_cache_meta

                # If cache is processed inside a task
                if 'output' in r:
                    rr = r['output']
                    # Already cached
                    if not new and not renew:
                        cache = False
                        prepare_cache_meta = False
                else:
                    rr = r

            ###################################################################
            # Run (default) script
            if not skip_run_script:
                run_script_name = default_script_name if update_run_script_name == '' else update_run_script_name

                default_script_with_path2 = default_script_with_path.replace('{{script_name}}',
                                    run_script_name)

                if update_run_script_name !='' and not os.path.isfile(default_script_with_path2):
                    return self.cmind.prepare_error(1, f'Can\'t find script: {default_script_with_path2}')

                if os.path.os.path.isfile(default_script_with_path2):
                    timeout = _input.get('timeout', None)

                    # Some internal variables
                    env['CMX_PATH_TO_FLEX_TASK'] = task_path

                    if len(update_run_script_env)>0:
                        for k in update_run_script_env:
                            v = update_run_script_env[k]
                            if k in env and k.startswith('+'):
                                env[k][0:0] = v
                            else:
                                env[k] = v

                    cmd_prefix_from_state = task_meta.get('cmd_prefix_from_state', [])

                    r = run_cmd(self.cmind,
                                console,
                                call_default_script_with_path.replace('{{script_name}}',
                                    run_script_name),
                                env,
                                timeout,
                                state = state,
                                verbose = verbose,
                                cmd_prefix_from_state = cmd_prefix_from_state)

                    if r['return']>0: return self.cmind.embed_error(r)

                    file_meta = r.get('tmp-flex-task-output', {})
                    if len(file_meta)>0:
                        utils.merge_dicts({'dict1':rr, 'dict2':file_meta, 'append_lists':True, 'append_unique':True})


            ###################################################################
            # Check if simple post dependencies
            post_deps = task_meta.get('post_deps', [])
            if len(post_deps) > 0:
                r = process_deps(self.cmind, post_deps, state, self_automation_name, 
                                 verbose = verbose, console = console, quiet = quiet, 
                                 tmp = tmp)
                if r['return'] >0: return r

                tmp = r['tmp']

            ###################################################################
            # Finish self time
            self_time = time.time() - self_time_start
            rr['self_flex_task_time_sec'] = '{:.3f}'.format(self_time)

            ###################################################################
            # Finish cache if needed
            if cache or prepare_cache_meta:
                r = self.cmind.x({'action':'finish',
                                  'automation':self.meta['use']['flex.cache'],
                                  'artifact':cache_uid,
                                  'cache_meta':cache_meta,
                                  'cache_tags':update_cache_tags,
                                  'output':rr,
                                  'extra_cmx_output_file': extra_cmx_output_file})
                if r['return'] > 0: return self.cmind.embed_error(r)

        ###################################################################
        # Restore current directory
        os.chdir(cur_dir)

        if cache_to_state != '' or add_to_state != '':
            rrr = copy.deepcopy(rr)
            key = cache_to_state if cache_to_state != '' else add_to_state

            utils.update_dict_with_flat_key(key, rrr, state)

        if output_state:
            rr['state'] = state

        if print_state_and_json:
            rrr = copy.deepcopy(rr)
            rrr['state'] = state

            print ('')
            print (json.dumps(rrr, indent = 2, sort_keys = True))

        elif print_json:
            print ('')
            print (json.dumps(rr, indent = 2, sort_keys = True))

        if save_versions != False:
            if type(save_versions) == bool or save_versions.lower() == 'true': 
                save_versions = 'cmx-rt-versions.yaml'

            versions = {'state':{'flow':state['cmx'].get('flow',{})}}

            r = utils.save_yaml(save_versions, versions)
            if r['return']>0: return r

        return rr

############################################################
# Helper function (can be used in Flex Task)

def prepare_work_dir(cmind, console, cache_automation, 
                     cache, cache_tags, cache_meta, quiet = False,
                     verbose = False, renew = False, new = False,
                     version = '', version_min = '', version_max = '',
                     cache_name_prefix = None):

    import os

    workdir = os.getcwd()

    rr = {'return':0}

    if cache:
        ii = {'action': 'prepare',
              'automation': cache_automation,
              'tags': cache_tags,
              'cache_meta': cache_meta}

        if console:
            ii['control'] = {'out': 'con'}

        if renew:
            ii['renew'] = True

        if new:
            ii['new'] = True

        if quiet:
            ii['quiet'] = True

        if version != '':
            ii['version'] = version

        if version_min != '':
            ii['version_min'] = version_min

        if version_max != '':
            ii['version_max'] = version_max

        if cache_name_prefix != None and cache_name_prefix != '':
            ii['artifact_prefix'] = cache_name_prefix

        r = cmind.x(ii)
        if r['return'] > 0: return cmind.embed_error(r)

        cache_uid = r.get('meta',{}).get('uid', '')

        if 'output' in r:
            rr['output'] = r['output']

            if cache_uid != '': rr['cache_uid'] = cache_uid

            path = r.get('path', '')

        else:
            path = r['path']
            workdir = path
            rr['cache_uid'] = r['meta']['uid']

        cmind.log(f"flex.task cachdir: {path}", "info")
        if path != '' and console and verbose:
            print ('')
            print (f'CACHEDIR {path}')


    # Working directory
    cmind.log(f"flex.task workdir: {workdir}", "info")
    os.chdir(workdir)

    rr['workdir'] = workdir

    return rr

############################################################
# Helper function (can be used in flex.task)

def run_cmd(cmind,
            console,
            cmd,
            env = {},
            timeout = None,
            capture_output = False,
            state = {},
            verbose = False,
            cmd_prefix_from_state = [],
            hide_in_cmd = [],
            save_script = '',
            script_prefix = '',
            skip_run = False,
            run_script = False,
            print_cmd = False):

    # Clean tmp json file if needed
    foutput = 'tmp-flex-task-output.json'

    if os.path.isfile(foutput):
        os.remove(foutput)

    # Check prefix from state['cmx']
    cmx = state.get('cmx', {})

    x_cmd_prefix = ''
    for key in cmd_prefix_from_state:
        value = ''

        if '.' in key:
           keys = key.split('.')
           new_state = state
           for key in keys[:-1]:
               if key in new_state:
                  new_state = new_state[key]
           value = new_state.get(keys[-1])
        else:
           value = state.get(key)

        if value != None and value != '':
            if type(value) != list:
                value = [value]

            for v in value:
                x_cmd_prefix += v + ' && '

    cmd = x_cmd_prefix + cmd

    cmind.log(f'flex.task run_cmd: {cmd}')

    # Prepare input
    ii = {'action':'cmd',
          'automation':'flex.common,21286240620d4ef6',
          'env':env,
          'genv':cmx.get('genv', {}),
          'cmd':cmd,
          'timeout':timeout,
          'capture_output':capture_output,
          'control':{},
          'verbose':verbose,
          'hide_in_cmd':hide_in_cmd,
          'save_script':save_script,
          'script_prefix':script_prefix,
          'skip_run':skip_run,
          'run_script':run_script}

    if len(cmx.get('envs', {})) > 0:
        ii['envs'] = cmx['envs']

    if console:
        ii['control']['out'] = 'con'

    if print_cmd:
        ii['print_cmd'] = True

    r = cmind.x(ii)
    if r['return']>0: return r

    if r['returncode']>0:
        r['return'] = 1
        stderr = r['stderr']
        if stderr == None: stderr = ''
        if stderr != '': stderr = '\n' + stderr.strip()
        r['error'] = f"OS command return code: {r['returncode']}{stderr}"

    if os.path.isfile(foutput):
        rx = utils.load_json(foutput)
        if rx['return'] == 0:
            r['tmp-flex-task-output'] = rx['meta']
            os.remove(foutput)

    return r

############################################################
# Process deps

def process_deps(cmind, deps, state, flex_automation, 
                 verbose = False, console = False, quiet = False,
                 tmp = {}):

    import copy

    for d in deps:
        # Check if should run or skip
        check = d.get('_run_if_state_all', {})
        if check_if_skip(check, state):
            continue

        if 'automation' not in d:
            d['automation'] = flex_automation

        if d.get('action', '') == '':
            d['action'] = 'run'

        ii = copy.deepcopy(d)
        ii['state'] = state

        if 'control' not in ii:
            ii['control'] = {}
            if console:
                ii['control']['out'] = 'con'

        if verbose:
            ii['verbose'] = True

        if quiet:
            ii['quiet'] = True

        alias = d.get('alias', '')

        update_input_via_alias(alias, state, ii)

        r = cmind.x(ii)
        if r['return'] > 0: return r

        utils.merge_dicts({'dict1':tmp, 'dict2':r, 'append_lists':True, 'append_unique':True})

    return {'return':0, 'tmp':tmp}


############################################################
# Parse version

def parse_version(r, match_text, match_group):
    """
    """

    stdout = r.get('stdout', '').strip().lower()
    stderr = r.get('stderr', '').strip().lower()

    stdout += stderr

    import re
    match = re.search(match_text, stdout)

    rrr = {'return':0}

    available = False
    if match != None:
        version = match.group(match_group)
        available = True

    rrr['available'] = available
    if available and version != '':
        rrr['version'] = version

    rrr['output'] = stdout

    return rrr

############################################################
# Update input via alias

def update_input_via_alias(alias, state, i):

    if alias != '':
        aliases = alias.split(',')

        configure = state.get('flow', {})
        if len(configure) > 0:
            for a in aliases:
                if a in configure:
                    utils.merge_dicts({'dict1':i, 'dict2':configure[a], 'append_lists':True, 'append_unique':True})

    return {'return':0}

############################################################

# Check if should run flex.task

def check_if_skip(check, state):

    skip = False

    if len(check) > 0:

        for k in check:
            v = check[k]

            vv = utils.get_value_from_dict_with_flat_key(k, state)

            if type(v) == list:
                if vv not in v:
                    skip = True
                    break
            else:
                if vv != v and str(vv).lower() != str(v).lower():
                    skip = True
                    break

    return skip
