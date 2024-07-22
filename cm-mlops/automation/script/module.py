# CM "script" automation that wraps native scripts with a unified CLI, Python API 
# and JSON/YAML meta descriptions.
#
# It is a stable prototype being developed by Grigori Fursin and Arjun Suresh.
# 
# We think to develop a simpler version of this automation at some point
# while keeping full backwards compatibility.
#
# Join the MLCommons taskforce on automation and reproducibility
# to discuss further developments: 
# https://github.com/mlcommons/ck/blob/master/docs/taskforce.md

import os

from cmind.automation import Automation
from cmind import utils

class CAutomation(Automation):
    """
    CM "script" automation actions 
    (making native scripts more portable, deterministic, reusable and reproducible)
    """

    ############################################################
    def __init__(self, cmind, automation_file):
        super().__init__(cmind, __file__)

        self.os_info = {}
        self.run_state = {}
        self.run_state['deps'] = []
        self.run_state['fake_deps'] = False
        self.run_state['parent'] = None
        self.run_state['version_info'] = []

        self.file_with_cached_state = 'cm-cached-state.json'

        self.tmp_file_env = 'tmp-env'
        self.tmp_file_env_all = 'tmp-env-all'
        self.tmp_file_run = 'tmp-run'
        self.tmp_file_state = 'tmp-state.json'

        self.tmp_file_run_state = 'tmp-run-state.json'
        self.tmp_file_run_env = 'tmp-run-env.out'
        self.tmp_file_ver = 'tmp-ver.out'

        self.__version__ = "1.2.1"

        self.local_env_keys = ['CM_VERSION',
                               'CM_VERSION_MIN',
                               'CM_VERSION_MAX',
                               'CM_VERSION_MAX_USABLE',
                               'CM_DETECTED_VERSION',
                               'CM_INPUT',
                               'CM_OUTPUT',
                               'CM_NAME',
                               'CM_EXTRA_CACHE_TAGS',
                               'CM_TMP_*',
                               'CM_GIT_*',
                               'CM_RENEW_CACHE_ENTRY']

        self.input_flags_converted_to_tmp_env = ['path'] 

        self.input_flags_converted_to_env = ['input', 
                                             'output', 
                                             'name', 
                                             'extra_cache_tags', 
                                             'skip_compile', 
                                             'skip_run',
                                             'accept_license',
                                             'skip_system_deps',
                                             'git_ssh',
                                             'gh_token']




    ############################################################
    def run(self, i):
        """
        Run CM script

        Args:
          (CM input dict): 

          (out) (str): if 'con', output to console

          (artifact) (str): specify CM script (CM artifact) explicitly

          (tags) (str): tags to find an CM script (CM artifact)

          (env) (dict): global environment variables (can/will be updated by a given script and dependencies)
          (const) (dict): constant environment variable (will be preserved and persistent for a given script and dependencies)

          (state) (dict): global state dictionary (can/will be updated by a given script and dependencies)
          (const_state) (dict): constant state (will be preserved and persistent for a given script and dependencies)

          (add_deps) (dict): {"name": {"tag": "tag(s)"}, "name": {"version": "version_no"}, ...}
          (add_deps_recursive) (dict): same as add_deps but is passed recursively onto dependencies as well

          (version) (str): version to be added to env.CM_VERSION to specialize this flow
          (version_min) (str): min version to be added to env.CM_VERSION_MIN to specialize this flow
          (version_max) (str): max version to be added to env.CM_VERSION_MAX to specialize this flow
          (version_max_usable) (str): max USABLE version to be added to env.CM_VERSION_MAX_USABLE

          (path) (str): list of paths to be added to env.CM_TMP_PATH to specialize this flow

          (input) (str): converted to env.CM_INPUT  (local env)
          (output) (str): converted to env.CM_OUTPUT (local env)

          (extra_cache_tags) (str): converted to env.CM_EXTRA_CACHE_TAGS and used to add to caching (local env)

          (name) (str): taken from env.CM_NAME and/or converted to env.CM_NAME (local env)
                        Added to extra_cache_tags with "name-" prefix .
                        Useful for python virtual env (to create multiple entries)

          (quiet) (bool): if True, set env.CM_QUIET to "yes" and attempt to skip questions
                          (the developers have to support it in pre/post processing and scripts)

          (skip_cache) (bool): if True, skip caching and run in current directory
          (force_cache) (bool): if True, force caching if can_force_cache=true in script meta

          (skip_remembered_selections) (bool): if True, skip remembered selections
                                               (uses or sets env.CM_TMP_SKIP_REMEMBERED_SELECTIONS to "yes")

          (new) (bool): if True, skip search for cached and run again
          (renew) (bool): if True, rewrite cache entry if exists

          (dirty) (bool): if True, do not clean files

          (save_env) (bool): if True, save env and state to tmp-env.sh/bat and tmp-state.json
          (shell) (bool): if True, save env with cmd/bash and run it

          (recursion) (bool): True if recursive call.
                              Useful when preparing the global bat file or Docker container
                              to save/run it in the end.

          (recursion_spaces) (str, internal): adding '  ' during recursion for debugging

          (remembered_selections) (list): remember selections of cached outputs

          (print_env) (bool): if True, print aggregated env before each run of a native script

          (fake_run) (bool): if True, will run the dependent scripts but will skip the main run script
          (prepare) (bool): the same as fake_run
          (fake_deps) (bool): if True, will fake run the dependent scripts
          (print_deps) (bool): if True, will print the CM run commands of the direct dependent scripts
          (run_state) (dict): Internal run state

          (debug_script_tags) (str): if !='', run cmd/bash before executing a native command 
                                      inside a script specified by these tags

          (debug_script) (bool): if True, debug current script (set debug_script_tags to the tags of a current script)
          (detected_versions) (dict): All the used scripts and their detected_versions

          (verbose) (bool): if True, prints all tech. info about script execution (False by default)
          (v) (bool): the same as verbose

          (time) (bool): if True, print script execution time (or if verbose == True)
          (space) (bool): if True, print used disk space for this script (or if verbose == True)

          (ignore_script_error) (bool): if True, ignore error code in native tools and scripts
                                        and finish a given CM script. Useful to test/debug partial installations

          (json) (bool): if True, print output as JSON
          (j) (bool): if True, print output as JSON

          (pause) (bool): if True, pause at the end of the main script (Press Enter to continue)

          (repro) (bool): if True, dump cm-run-script-input.json, cm-run_script_output.json, 
                          cm-run-script-state.json, cm-run-script-info.json
                          to improve the reproducibility of results

          (repro_prefix) (str): if !='', use it to record above files {repro-prefix)-input.json ...                
          (repro_dir) (str): if !='', use this directory to dump info

          (script_call_prefix) (str): how to call script in logs and READMEs (cm run script)
          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          * (skipped) (bool): if true, this script was skipped

          * new_env (dict): new environment (delta from a collective script)
          * new_state (dict): new state (delta from a collective script)

          * env (dict): global env (updated by this script - includes new_env)
          * state (dict): global state (updated by this script - includes new_state)

        """

        r = self._run(i)

        return r


    ############################################################
    def _run(self, i):

        from cmind import utils
        import copy
        import time
        import shutil

        # Check if save input/output to file
        repro = i.get('repro', False)
        repro_prefix = ''

        if repro:
            repro_prefix = i.get('repro_prefix', '')
            if repro_prefix == '': repro_prefix = 'cm-run-script'

            repro_dir = i.get('repro_dir', '')
            if repro_dir == '': repro_dir = os.getcwd()

            repro_prefix = os.path.join (repro_dir, repro_prefix)

        if repro_prefix!='':
            dump_repro_start(repro_prefix, i)
            
       
        recursion = i.get('recursion', False)

        # If first script run, check if can write to current directory
        if not recursion and not i.get('skip_write_test', False):
            if not can_write_to_current_directory():
                return {'return':1, 'error':'Current directory "{}" is not writable - please change it'.format(os.getcwd())}

        recursion_int = int(i.get('recursion_int',0))+1

        start_time = time.time()

        # Check extra input from environment variable CM_SCRIPT_EXTRA_CMD
        # Useful to set up default flags such as the name of virtual enviroment
        extra_cli = os.environ.get('CM_SCRIPT_EXTRA_CMD', '').strip()
        if extra_cli != '':
            from cmind import cli
            r = cli.parse(extra_cli)
            if r['return']>0: return r

            cm_input = r['cm_input']

            utils.merge_dicts({'dict1':i, 'dict2':cm_input, 'append_lists':True, 'append_unique':True})

        # Check simplified CMD: cm run script "get compiler"
        # If artifact has spaces, treat them as tags!
        artifact = i.get('artifact','')
        if ' ' in artifact: # or ',' in artifact:
            del(i['artifact'])
            if 'parsed_artifact' in i: del(i['parsed_artifact'])
            # Force substitute tags
            i['tags']=artifact.replace(' ',',')

        # Check if has extra tags as a second artifact
        # Example: cmr . "_python _tiny"

        parsed_artifacts = i.get('parsed_artifacts',[])
        if len(parsed_artifacts)>0:
            extra_tags = parsed_artifacts[0][0][0]
            if ' ' in extra_tags or ',' in extra_tags:
                # Add tags
                x=i.get('tags','')
                if x!='': x+=','
                i['tags']=x+extra_tags.replace(' ',',')

        # Recursion spaces needed to format log and print
        recursion_spaces = i.get('recursion_spaces', '')
        # Caching selections to avoid asking users again
        remembered_selections = i.get('remembered_selections', [])

        # Get current env and state before running this script and sub-scripts
        env = i.get('env',{})
        state = i.get('state',{})
        const = i.get('const',{})
        const_state = i.get('const_state',{})

        # Save current env and state to detect new env and state after running a given script
        saved_env = copy.deepcopy(env)
        saved_state = copy.deepcopy(state)

        for key in [ "env", "state", "const", "const_state" ]:
            if i.get("local_"+key):
                if not i.get(key, {}):
                    i[key] = {}
                utils.merge_dicts({'dict1':i[key], 'dict2':i['local_'+key], 'append_lists':True, 'append_unique':True})

        add_deps = i.get('ad',{})
        if not add_deps:
            add_deps = i.get('add_deps',{})
        else:
            utils.merge_dicts({'dict1':add_deps, 'dict2':i.get('add_deps', {}), 'append_lists':True, 'append_unique':True})

        add_deps_recursive = i.get('adr', {})
        if not add_deps_recursive:
            add_deps_recursive = i.get('add_deps_recursive', {})
        else:
            utils.merge_dicts({'dict1':add_deps_recursive, 'dict2':i.get('add_deps_recursive', {}), 'append_lists':True, 'append_unique':True})

        save_env = i.get('save_env', False)

        print_env = i.get('print_env', False)

        verbose = False

        if 'verbose' in i: verbose=i['verbose']
        elif 'v' in i: verbose=i['v']

        if verbose:
           env['CM_VERBOSE']='yes'

        show_time = i.get('time', False)
        show_space = i.get('space', False)

        if not recursion and show_space:
            start_disk_stats = shutil.disk_usage("/")

        extra_recursion_spaces = '  '# if verbose else ''

        skip_cache = i.get('skip_cache', False)
        force_cache = i.get('force_cache', False)

        fake_run = i.get('fake_run', False)
        fake_run = i.get('fake_run', False) if 'fake_run' in i else i.get('prepare', False)
        if fake_run: env['CM_TMP_FAKE_RUN']='yes'
        
        fake_deps = i.get('fake_deps', False)
        if fake_deps: env['CM_TMP_FAKE_DEPS']='yes'

        run_state = i.get('run_state', self.run_state)
        if not run_state.get('version_info', []):
            run_state['version_info'] = []
        if run_state.get('parent', '') == '':
            run_state['parent'] = None
        if fake_deps:
            run_state['fake_deps'] = True

        print_deps = i.get('print_deps', False)
        print_readme = i.get('print_readme', False)

        new_cache_entry = i.get('new', False)
        renew = i.get('renew', False)

        cmd = i.get('cmd', '')
        # Capturing the input command if it is coming from an access function
        if not cmd and 'cmd' in i.get('input',''):
            i['cmd'] = i['input']['cmd']
            cmd = i['cmd']

        debug_script_tags = i.get('debug_script_tags', '')

        detected_versions = i.get('detected_versions', {})

        ignore_script_error = i.get('ignore_script_error', False)

        # Get constant env and state
        const = i.get('const',{})
        const_state = i.get('const_state',{})

        # Detect current path and record in env for further use in native scripts
        current_path = os.path.abspath(os.getcwd())
        env['CM_TMP_CURRENT_PATH'] = current_path

        # Check if quiet mode
        quiet = i.get('quiet', False) if 'quiet' in i else (env.get('CM_QUIET','').lower() == 'yes')
        if quiet: env['CM_QUIET'] = 'yes'

        skip_remembered_selections = i.get('skip_remembered_selections', False) if 'skip_remembered_selections' in i \
            else (env.get('CM_SKIP_REMEMBERED_SELECTIONS','').lower() == 'yes')
        if skip_remembered_selections: env['CM_SKIP_REMEMBERED_SELECTIONS'] = 'yes'

        # Prepare debug info
        parsed_script = i.get('parsed_artifact')
        parsed_script_alias = parsed_script[0][0] if parsed_script is not None else ''





        # Get and cache minimal host OS info to be able to run scripts and manage OS environment
        if len(self.os_info) == 0:
            r = self.cmind.access({'action':'get_host_os_info',
                                   'automation':'utils,dc2743f8450541e3'})
            if r['return']>0: return r

            self.os_info = r['info']

        os_info = self.os_info

        # Bat extension for this host OS
        bat_ext = os_info['bat_ext']

        # Add permanent env from OS (such as CM_WINDOWS:"yes" on Windows)
        env_from_os_info = os_info.get('env',{})
        if len(env_from_os_info)>0:
            env.update(env_from_os_info)

        #take some env from the user environment
        keys = [ "GH_TOKEN", "ftp_proxy", "FTP_PROXY", "http_proxy", "HTTP_PROXY", "https_proxy", "HTTPS_PROXY", "no_proxy", "NO_PROXY", "socks_proxy", "SOCKS_PROXY" ]
        for key in keys:
            if os.environ.get(key, '') != '' and env.get(key, '') == '':
                env[key] = os.environ[key]

        # Check path/input/output in input and pass to env
        for key in self.input_flags_converted_to_tmp_env:
            value = i.get(key, '').strip()
            if value != '':
                env['CM_TMP_' + key.upper()] = value

        for key in self.input_flags_converted_to_env:
            value = i.get(key, '')
            if type(value)==str: value=value.strip()
            if value != '':
                env['CM_' + key.upper()] = value


        ############################################################################################################
        # Check if we want to skip cache (either by skip_cache or by fake_run)
        force_skip_cache = True if skip_cache else False
        force_skip_cache = True if fake_run else force_skip_cache


        ############################################################################################################
        # Find CM script(s) based on their tags and variations to get their meta and customize this workflow.
        # We will need to decide how to select if more than 1 (such as "get compiler")
        #
        # Note: this local search function will separate tags and variations
        #
        # STEP 100 Input: Search sripts by i['tags'] (includes variations starting from _) and/or i['parsed_artifact']
        #                 tags_string = i['tags']

        tags_string = i.get('tags','').strip()

        ii = utils.sub_input(i, self.cmind.cfg['artifact_keys'])

        ii['tags'] = tags_string
        ii['out'] = None


        # if cm run script without tags/artifact and with --help
        if len(ii.get('parsed_artifact',[]))==0 and ii.get('tags','')=='' and i.get('help',False):
            return utils.call_internal_module(self, __file__, 'module_help', 'print_help', {'meta':{}, 'path':''})

        r = self.search(ii)
        if r['return']>0: return r

        # Search function will return 

        list_of_found_scripts = r['list']

        script_tags = r['script_tags']
        script_tags_string = ','.join(script_tags)

        variation_tags = r['variation_tags']

#        # Print what was searched!
#        cm_script_info = 'CM script'
#
#        x = 'with' 
#        if parsed_script_alias !='' :
#            cm_script_info += ' '+x+' alias "{}"'.format(parsed_script_alias)
#            x = 'and'
#
#        if len(script_tags)>0:
#            cm_script_info += ' '+x+' tags "{}"'.format(script_tags_string.replace(',',' '))
#            x = 'and'
#
#        if len(variation_tags)>0:
#            x_variation_tags = ['_'+v for v in variation_tags]
#            cm_script_info += ' '+x+' variations "{}"'.format(" ".join(x_variation_tags))
#
#        if verbose:
#            print ('')
#            print (recursion_spaces + '* Searching for ' + cm_script_info)
#        else:
#            print (recursion_spaces + '* Running ' + cm_script_info)


        cm_script_info = i.get('script_call_prefix', '').strip()
        if cm_script_info == '': cm_script_info = 'cm run script'
        if not cm_script_info.endswith(' '): cm_script_info+=' '

        x = '"'
        y = ' '
        if parsed_script_alias !='' :
            cm_script_info += parsed_script_alias
            x = ' --tags="'
            y = ','

        if len(script_tags)>0 or len(variation_tags)>0:
            cm_script_info += x

            if len(script_tags)>0:
                cm_script_info += script_tags_string.replace(',',y)

            if len(variation_tags)>0:
                if len(script_tags)>0: cm_script_info+=' '

                x_variation_tags = ['_'+v for v in variation_tags]
                cm_script_info += y.join(x_variation_tags)

            cm_script_info += '"'

#        if verbose:
#            print ('')

        print ('')
        print (recursion_spaces + '* ' + cm_script_info)


        #############################################################################
        # Report if scripts were not found or there is an ambiguity with UIDs
        if not r['found_scripts']:
            return {'return':1, 'error': 'no scripts were found with above tags (when variations ignored)'}

        if len(list_of_found_scripts) == 0:
            return {'return':16, 'error':'no scripts were found with above tags and variations\n'+r.get('warning', '')}

        # Sometimes there is an ambiguity when someone adds a script 
        # while duplicating a UID. In such case, we will return >1 script
        # and will start searching in the cache ... 
        # We are detecing such cases here:
        if len(list_of_found_scripts)>1 and script_tags_string=='' and parsed_script_alias!='' and '?' not in parsed_script_alias and '*' not in parsed_script_alias:
            x='Ambiguity in the following scripts have the same UID - please change that in _cm.json or _cm.yaml:\n'
            for y in list_of_found_scripts:
                x+=' * '+y.path+'\n'

            return {'return':1, 'error':x}

        # STEP 100 Output: list_of_found_scripts based on tags (with variations) and/or parsed_artifact 
        #                  script_tags [] - contains tags without variations (starting from _ such as _cuda)
        #                  variation_tags [] - contains only variations tags (without _)
        #                  string_tags_string [str] (joined script_tags)








        #############################################################################
        # Sort scripts for better determinism
        list_of_found_scripts = sorted(list_of_found_scripts, key = lambda a: (a.meta.get('sort',0),
                                                                               a.path))
        if verbose:
            print (recursion_spaces + '  - Number of scripts found: {}'.format(len(list_of_found_scripts)))

        # Check if script selection is remembered
        if not skip_remembered_selections and len(list_of_found_scripts) > 1:
            for selection in remembered_selections:
                if selection['type'] == 'script' and set(selection['tags'].split(',')) == set(script_tags_string.split(',')):
                    # Leave 1 entry in the found list
                    list_of_found_scripts = [selection['cached_script']]
                    if verbose:
                        print (recursion_spaces + '  - Found remembered selection with tags: {}'.format(script_tags_string))
                    break


        # STEP 200 Output: potentially pruned list_of_found_scripts if selection of multple scripts was remembered






        # STEP 300: If more than one CM script found (example: "get compiler"), 
        # first, check if selection was already remembered!
        # second, check in cache to prune scripts

        # STEP 300 input: lit_of_found_scripts

        select_script = 0

        # If 1 script found and script_tags == '', pick them from the meta
        if script_tags_string == '' and len(list_of_found_scripts) == 1:
            script_tags_string = ','.join(list_of_found_scripts[0].meta.get('tags',[]))

        # Found 1 or more scripts. Scans cache tags to find at least 1 with cache==True
        preload_cached_scripts = False
        for script in list_of_found_scripts:
            if script.meta.get('cache', False) == True or (script.meta.get('can_force_cache', False) and force_cache):
                preload_cached_scripts = True
                break

        # STEP 300 Output: preload_cached_scripts = True if at least one of the list_of_found_scripts must be cached






        # STEP 400: If not force_skip_cache and at least one script can be cached, find (preload) related cache entries for found scripts
        # STEP 400 input:  script_tags and -tmp (to avoid unfinished scripts particularly when installation fails)

        cache_list = []

        if not force_skip_cache and preload_cached_scripts:
            cache_tags_without_tmp_string = '-tmp'
            if script_tags_string !='':
                cache_tags_without_tmp_string += ',' + script_tags_string
            if variation_tags:
                cache_tags_without_tmp_string += ',_' + ",_".join(variation_tags)
            # variation_tags are prefixed with "_" but the CM search function knows only tags and so we need to change "_-" to "-_" for excluding any variations
            # This change can later be moved to a search function specific to cache
            cache_tags_without_tmp_string = cache_tags_without_tmp_string.replace(",_-", ",-_")

            if verbose:
                print (recursion_spaces + '  - Searching for cached script outputs with the following tags: {}'.format(cache_tags_without_tmp_string))

            search_cache = {'action':'find',
                            'automation':self.meta['deps']['cache'],
                            'tags':cache_tags_without_tmp_string}
            rc = self.cmind.access(search_cache)
            if rc['return']>0: return rc

            cache_list = rc['list']

            if verbose:
                print (recursion_spaces + '    - Number of cached script outputs found: {}'.format(len(cache_list)))

            # STEP 400 output: cache_list






        # STEP 500: At this stage with have cache_list related to either 1 or more scripts (in case of get,compiler)
        #           If more than 1: Check if in cache and reuse it or ask user to select
        # STEP 500 input: list_of_found_scripts

        if len(list_of_found_scripts) > 0:
            # If only tags are used, check if there are no cached scripts with tags - then we will reuse them
            # The use case: cm run script --tags=get,compiler
            #  CM script will always ask to select gcc,llvm,etc even if any of them will be already cached
            if len(cache_list) > 0:
                new_list_of_found_scripts = []

                for cache_entry in cache_list:
                    # Find associated script and add to the list_of_found_scripts
                    associated_script_artifact = cache_entry.meta['associated_script_artifact']

                    x = associated_script_artifact.find(',')
                    if x<0:
                        return {'return':1, 'error':'CM artifact format is wrong "{}" - no comma found'.format(associated_script_artifact)}

                    associated_script_artifact_uid = associated_script_artifact[x+1:]

                    cache_entry.meta['associated_script_artifact_uid'] = associated_script_artifact_uid

                    for script in list_of_found_scripts:
                        script_uid = script.meta['uid']

                        if associated_script_artifact_uid == script_uid:
                            if script not in new_list_of_found_scripts:
                                new_list_of_found_scripts.append(script)

                # Avoid case when all scripts are pruned due to just 1 variation used
                if len(new_list_of_found_scripts)>0:
                    list_of_found_scripts = new_list_of_found_scripts

            # Select scripts
            if len(list_of_found_scripts) > 1:
                select_script = select_script_artifact(list_of_found_scripts, 'script', recursion_spaces, False, script_tags_string, quiet, verbose)

                # Remember selection
                if not skip_remembered_selections:
                    remembered_selections.append({'type': 'script',
                                                  'tags':script_tags_string,
                                                  'cached_script':list_of_found_scripts[select_script]})
            else:
                select_script = 0

            # Prune cache list with the selected script
            if len(list_of_found_scripts) > 0:
                 script_artifact_uid = list_of_found_scripts[select_script].meta['uid']

                 new_cache_list = []
                 for cache_entry in cache_list:
                     if cache_entry.meta['associated_script_artifact_uid'] == script_artifact_uid:
                         new_cache_list.append(cache_entry)

                 cache_list = new_cache_list

        # Here a specific script is found and meta obtained
        # Set some useful local variables
        script_artifact = list_of_found_scripts[select_script]

        meta = script_artifact.meta
        path = script_artifact.path

        # Check path to repo
        script_repo_path = script_artifact.repo_path

        script_repo_path_with_prefix = script_artifact.repo_path
        if script_artifact.repo_meta.get('prefix', '') != '':
            script_repo_path_with_prefix = os.path.join(script_repo_path, script_artifact.repo_meta['prefix'])

        env['CM_TMP_CURRENT_SCRIPT_REPO_PATH'] = script_repo_path
        env['CM_TMP_CURRENT_SCRIPT_REPO_PATH_WITH_PREFIX'] = script_repo_path_with_prefix

        # Check if has --help
        if i.get('help',False):
            return utils.call_internal_module(self, __file__, 'module_help', 'print_help', {'meta':meta, 'path':path})

        run_state['script_id'] = meta['alias'] + "," + meta['uid']
        run_state['script_variation_tags'] = variation_tags

        deps = meta.get('deps',[])
        post_deps = meta.get('post_deps',[])
        prehook_deps = meta.get('prehook_deps',[])
        posthook_deps = meta.get('posthook_deps',[])
        input_mapping = meta.get('input_mapping', {})
        docker_settings = meta.get('docker')
        docker_input_mapping = {}
        if docker_settings:
            docker_input_mapping = docker_settings.get('docker_input_mapping', {})
        new_env_keys_from_meta = meta.get('new_env_keys', [])
        new_state_keys_from_meta = meta.get('new_state_keys', [])

        found_script_artifact = utils.assemble_cm_object(meta['alias'], meta['uid'])

        found_script_tags = meta.get('tags',[])

        if i.get('debug_script', False):
            debug_script_tags=','.join(found_script_tags)

        if verbose:
            print (recursion_spaces+'  - Found script::{} in {}'.format(found_script_artifact, path))


        # STEP 500 output: script_artifact - unique selected script artifact
        #                  (cache_list) pruned for the unique script if cache is used 
        #                  meta - script meta
        #                  path - script path
        #                  found_script_tags [] - all tags of the found script













        # HERE WE HAVE ORIGINAL ENV

        # STEP 600: Continue updating env  
        # Add default env from meta to new env if not empty
        # (env NO OVERWRITE)
        script_artifact_default_env = meta.get('default_env',{})
        for key in script_artifact_default_env:
            env.setdefault(key, script_artifact_default_env[key])


        # Force env from meta['env'] as a CONST
        # (env OVERWRITE)
        script_artifact_env = meta.get('env',{})
        env.update(script_artifact_env)















        # STEP 700: Overwrite env with keys from the script input (to allow user friendly CLI)
        #           IT HAS THE PRIORITY OVER meta['default_env'] and meta['env']
        #           (env OVERWRITE - user enforces it from CLI)
        #           (it becomes const)
        if input_mapping:
            update_env_from_input_mapping(env, i, input_mapping)
            update_env_from_input_mapping(const, i, input_mapping)

        # This mapping is done in module_misc
        #if docker_input_mapping:
        #    update_env_from_input_mapping(env, i, docker_input_mapping)
        #    update_env_from_input_mapping(const, i, docker_input_mapping)






        # STEP 800: Process variations and update env (overwrite from env and update form default_env)
        #           VARIATIONS HAS THE PRIORITY OVER 
        # MULTIPLE VARIATIONS (THAT CAN BE TURNED ON AT THE SAME TIME) SHOULD NOT HAVE CONFLICTING ENV

        # VARIATIONS OVERWRITE current ENV but not input keys (they become const)




        variations = script_artifact.meta.get('variations', {})
        state['docker'] = meta.get('docker', {})

        r = self._update_state_from_variations(i, meta, variation_tags, variations, env, state, deps, post_deps, prehook_deps, posthook_deps, new_env_keys_from_meta, new_state_keys_from_meta, add_deps_recursive, run_state, recursion_spaces, verbose)
        if r['return'] > 0:
            return r

        warnings = meta.get('warnings', [])
        if len(r.get('warnings', [])) >0:
            warnings += r['warnings']

        variation_tags_string = r['variation_tags_string']
        explicit_variation_tags = r['explicit_variation_tags']

        # USE CASE:
        #  HERE we may have versions in script input and env['CM_VERSION_*']

        # STEP 900: Get version, min, max, usable from env (priority if passed from another script to force version), 
        #           then script input, then script meta

        #           VERSIONS SHOULD NOT BE USED INSIDE VARIATIONS (in meta)!

        # First, take version from input
        version = i.get('version', '').strip()
        version_min = i.get('version_min', '').strip()
        version_max = i.get('version_max', '').strip()
        version_max_usable = i.get('version_max_usable', '').strip()

        # Second, take from env
        if version == '': version = env.get('CM_VERSION','')
        if version_min == '': version_min = env.get('CM_VERSION_MIN','')
        if version_max == '': version_max = env.get('CM_VERSION_MAX','')
        if version_max_usable == '': version_max_usable = env.get('CM_VERSION_MAX_USABLE','')


        # Third, take from meta
        if version == '': version = meta.get('version', '')
        if version_min == '': version_min = meta.get('version_min', '')
        if version_max == '': version_max = meta.get('version_max', '')
        if version_max_usable == '': version_max_usable = meta.get('version_max_usable', '')

        # Update env with resolved versions
        notes = []
        for version_index in [(version, 'CM_VERSION', ' == {}'),
                              (version_min, 'CM_VERSION_MIN', ' >= {}'),
                              (version_max, 'CM_VERSION_MAX', ' <= {}'),
                              (version_max_usable, 'CM_VERSION_MAX_USABLE', '({})')]:
            version_value = version_index[0]
            key = version_index[1]
            note = version_index[2]

            if version_value !='': 
                env[key] = version_value

                notes.append(note.format(version_value))
#            elif key in env: 
#                # If version_X is "", remove related key from ENV ...
#                del(env[key])

        if len(notes)>0:
            if verbose:
                print (recursion_spaces+'    - Requested version: ' + '  '.join(notes))

        # STEP 900 output: version* set
        #                  env['CM_VERSION*] set



        # STEP 1000: Update version only if in "versions" (not obligatory)
        # can be useful when handling complex Git revisions
        versions = script_artifact.meta.get('versions', {})

        if version!='' and version in versions:
            versions_meta = versions[version]
            r = update_state_from_meta(versions_meta, env, state, deps, post_deps, prehook_deps, posthook_deps, new_env_keys_from_meta, new_state_keys_from_meta, i)
            if r['return']>0: return r
            adr=get_adr(versions_meta)
            if adr:
                self._merge_dicts_with_tags(add_deps_recursive, adr)
                #Processing them again using updated deps for add_deps_recursive
                r = update_adr_from_meta(deps, post_deps, prehook_deps, posthook_deps, add_deps_recursive)

 
        # STEP 1100: Update deps from input
        r = update_deps_from_input(deps, post_deps, prehook_deps, posthook_deps, i)
        if r['return']>0: return r


        r = update_env_with_values(env)
        if r['return']>0: return r 

        if str(env.get('CM_RUN_STATE_DOCKER', False)).lower() in ['true', '1', 'yes']:
            if state.get('docker'):
                if str(state['docker'].get('run', True)).lower() in ['false', '0', 'no']:
                    print (recursion_spaces+'  - Skipping script::{} run as we are inside docker'.format(found_script_artifact))
                    return {'return': 0}
                elif str(state['docker'].get('docker_real_run', True)).lower() in ['false', '0', 'no']:
                    print (recursion_spaces+'  - Doing fake run for script::{} as we are inside docker'.format(found_script_artifact))
                    fake_run = True
                    env['CM_TMP_FAKE_RUN']='yes'



        ############################################################################################################
        # Check extra cache tags
        x = env.get('CM_EXTRA_CACHE_TAGS','').strip()
        extra_cache_tags = [] if x=='' else x.split(',')

        if i.get('extra_cache_tags','')!='':
            for x in i['extra_cache_tags'].strip().split(','):
                if x!='':
                    if '<<<' in x:
                        import re
                        tmp_values = re.findall(r'<<<(.*?)>>>', str(x))
                        for tmp_value in tmp_values:
                            xx = str(env.get(tmp_value,''))
                            x = x.replace("<<<"+tmp_value+">>>", xx)
                    if x not in extra_cache_tags:
                        extra_cache_tags.append(x)

        if env.get('CM_NAME','')!='':
            extra_cache_tags.append('name-'+env['CM_NAME'].strip().lower())

        
        
        ############################################################################################################
        # Check if need to clean output files
        clean_output_files = meta.get('clean_output_files', [])

        if len(clean_output_files)>0:
            clean_tmp_files(clean_output_files, recursion_spaces)






        ############################################################################################################
        # Check if the output of a selected script should be cached
        cache = False if i.get('skip_cache', False) else meta.get('cache', False)
        cache = False if fake_run else cache
        cache = cache or (i.get('force_cache', False) and meta.get('can_force_cache', False))

        cached_uid = ''
        cached_tags = []
        cached_meta = {}

        remove_tmp_tag = False
        reuse_cached = False

        found_cached = False
        cached_path = ''

        local_env_keys_from_meta = meta.get('local_env_keys', [])





        ############################################################################################################
        # Check if script is cached if we need to skip deps from cached entries
        this_script_cached = False

        ############################################################################################################
        # Check if the output of a selected script should be cached
        if cache:
            # TBD - need to reuse and prune cache_list instead of a new CM search inside find_cached_script

            r = find_cached_script({'self':self,
                                    'recursion_spaces':recursion_spaces,
                                    'script_tags':script_tags,
                                    'found_script_tags':found_script_tags,
                                    'variation_tags':variation_tags,
                                    'explicit_variation_tags':explicit_variation_tags,
                                    'version':version,
                                    'version_min':version_min,
                                    'version_max':version_max,
                                    'extra_cache_tags':extra_cache_tags,
                                    'new_cache_entry':new_cache_entry,
                                    'meta':meta,
                                    'env':env,
                                    'skip_remembered_selections':skip_remembered_selections,
                                    'remembered_selections':remembered_selections,
                                    'quiet':quiet,
                                    'verbose':verbose
                                   })
            if r['return'] >0: return r

            # Sort by tags to ensure determinism in order (and later add versions)
            found_cached_scripts = sorted(r['found_cached_scripts'], key = lambda x: sorted(x.meta['tags']))

            cached_tags = r['cached_tags']
            search_tags = r['search_tags']

            num_found_cached_scripts = len(found_cached_scripts)

            if num_found_cached_scripts > 0:
                selection = 0

                # Check if quiet mode
                if num_found_cached_scripts > 1:
                    if quiet:
                        num_found_cached_scripts = 1

                if num_found_cached_scripts > 1:
                    selection = select_script_artifact(found_cached_scripts, 'cached script output', recursion_spaces, True, script_tags_string, quiet, verbose)

                    if selection >= 0:
                        if not skip_remembered_selections:
                            # Remember selection
                            remembered_selections.append({'type': 'cache',
                                                          'tags':search_tags,
                                                          'cached_script':found_cached_scripts[selection]})
                    else:
                        num_found_cached_scripts = 0


                elif num_found_cached_scripts == 1:
                    if verbose:
                        print (recursion_spaces+'    - Found cached script output: {}'.format(found_cached_scripts[0].path))


                if num_found_cached_scripts > 0:
                    found_cached = True

                    # Check chain of dynamic dependencies on other CM scripts
                    if len(deps)>0:
                        if verbose:
                            print (recursion_spaces + '  - Checking dynamic dependencies on other CM scripts:')

                        r = self._call_run_deps(deps, self.local_env_keys, local_env_keys_from_meta, env, state, const, const_state, add_deps_recursive, 
                            recursion_spaces + extra_recursion_spaces,
                            remembered_selections, variation_tags_string, True, debug_script_tags, verbose, show_time, extra_recursion_spaces, run_state)
                        if r['return']>0: return r

                        if verbose:
                            print (recursion_spaces + '  - Processing env after dependencies ...')

                        r = update_env_with_values(env)
                        if r['return']>0: return r 


                    # Check chain of prehook dependencies on other CM scripts. (No execution of customize.py for cached scripts)
                    if verbose:
                        print (recursion_spaces + '    - Checking prehook dependencies on other CM scripts:')

                    r = self._call_run_deps(prehook_deps, self.local_env_keys, local_env_keys_from_meta, env, state, const, const_state, add_deps_recursive, 
                            recursion_spaces + extra_recursion_spaces,
                            remembered_selections, variation_tags_string, found_cached, debug_script_tags, verbose, show_time, extra_recursion_spaces, run_state)
                    if r['return']>0: return r

                    # Continue with the selected cached script
                    cached_script = found_cached_scripts[selection]

                    if verbose:
                        print (recursion_spaces+'      - Loading state from cached entry ...')

                    path_to_cached_state_file = os.path.join(cached_script.path,
                        self.file_with_cached_state)

                    r =  utils.load_json(file_name = path_to_cached_state_file)
                    if r['return']>0: return r
                    version = r['meta'].get('version')

                    print (recursion_spaces + '     ! load {}'.format(path_to_cached_state_file))


                    ################################################################################################
                    # IF REUSE FROM CACHE - update env and state from cache!
                    cached_state = r['meta']

                    new_env = cached_state['new_env']
                    utils.merge_dicts({'dict1':env, 'dict2':new_env, 'append_lists':True, 'append_unique':True})

                    new_state = cached_state['new_state']
                    utils.merge_dicts({'dict1':state, 'dict2':new_state, 'append_lists':True, 'append_unique':True})

                    utils.merge_dicts({'dict1':new_env, 'dict2':const, 'append_lists':True, 'append_unique':True})
                    utils.merge_dicts({'dict1':new_state, 'dict2':const_state, 'append_lists':True, 'append_unique':True})






                    # Check chain of posthook dependencies on other CM scripts. We consider them same as postdeps when
                    # script is in cache
                    if verbose:
                        print (recursion_spaces + '    - Checking posthook dependencies on other CM scripts:')

                    clean_env_keys_post_deps = meta.get('clean_env_keys_post_deps',[])

                    r = self._call_run_deps(posthook_deps, self.local_env_keys, clean_env_keys_post_deps, env, state, const, const_state, add_deps_recursive, 
                            recursion_spaces + extra_recursion_spaces,
                            remembered_selections, variation_tags_string, found_cached, debug_script_tags, verbose, show_time, extra_recursion_spaces, run_state)
                    if r['return']>0: return r

                    if verbose:
                        print (recursion_spaces + '    - Checking post dependencies on other CM scripts:')

                    # Check chain of post dependencies on other CM scripts
                    r = self._call_run_deps(post_deps, self.local_env_keys, clean_env_keys_post_deps, env, state, const, const_state, add_deps_recursive, 
                            recursion_spaces + extra_recursion_spaces,
                            remembered_selections, variation_tags_string, found_cached, debug_script_tags, verbose, show_time, extra_recursion_spaces, run_state)
                    if r['return']>0: return r





            if renew or (not found_cached and num_found_cached_scripts == 0):
                # Add more tags to cached tags
                # based on meta information of the found script
                x = 'script-artifact-' + meta['uid']
                if x not in cached_tags: 
                    cached_tags.append(x)

                # Add all tags from the original CM script
                for x in meta.get('tags', []):
                    if x not in cached_tags: 
                        cached_tags.append(x)


            if not found_cached and num_found_cached_scripts == 0:

                # If not cached, create cached script artifact and mark as tmp (remove if cache successful)
                tmp_tags = ['tmp']

                # Finalize tmp tags
                tmp_tags += [ t for t in cached_tags if not t.startswith("-") ]

                # Check if some variations are missing 
                # though it should not happen!
                for t in variation_tags:
                    if t.startswith("-"):
                        continue
                    x = '_' + t
                    if x not in tmp_tags:
                        tmp_tags.append(x)

                # Use update to update the tmp one if already exists
                if verbose:
                    print (recursion_spaces+'  - Creating new "cache" script artifact in the CM local repository ...')
                    print (recursion_spaces+'    - Tags: {}'.format(','.join(tmp_tags)))

                if version != '': 
                    cached_meta['version'] = version

                ii = {'action':'update',
                      'automation': self.meta['deps']['cache'],
                      'search_tags':tmp_tags,
                      'tags':','.join(tmp_tags),
                      'meta':cached_meta,
                      'force':True}

                r = self.cmind.access(ii)
                if r['return'] > 0: return r

                remove_tmp_tag = True

                cached_script = r['list'][0]

                cached_path = cached_script.path
                cached_meta = cached_script.meta

                cached_uid = cached_meta['uid']

                # Changing path to CM script artifact for cached output
                # to record data and files there
                if verbose:
                    print (recursion_spaces+'  - Changing to {}'.format(cached_path))

                os.chdir(cached_path)



            # If found cached and we want to renew it
            if found_cached and renew:
                cached_path = cached_script.path
                cached_meta = cached_script.meta

                cached_uid = cached_meta['uid']

                # Changing path to CM script artifact for cached output
                # to record data and files there
                if verbose:
                    print (recursion_spaces+'  - Changing to {}'.format(cached_path))

                os.chdir(cached_path)

                # Force to finalize script inside cached entry
                found_cached = False
                remove_tmp_tag = True

                env['CM_RENEW_CACHE_ENTRY']='yes'

        # Prepare files to be cleaned
        clean_files = [self.tmp_file_run_state, 
                       self.tmp_file_run_env, 
                       self.tmp_file_ver,
                       self.tmp_file_env + bat_ext,
                       self.tmp_file_env_all + bat_ext,
                       self.tmp_file_state,
                       self.tmp_file_run + bat_ext]

        if not found_cached and len(meta.get('clean_files', [])) >0:
            clean_files = meta['clean_files'] + clean_files

        ################################ 
        if not found_cached:
            if len(warnings)>0:
                print ('=================================================')
                print ('WARNINGS:')
                print ('')
                for w in warnings:
                    print ('  '+w)
                print ('=================================================')

            # Update default version meta if version is not set
            if version == '':
                default_version = meta.get('default_version', '')
                if default_version != '':
                    version = default_version

                    if version_min != '':
                        ry = self.cmind.access({'action':'compare_versions',
                                                'automation':'utils,dc2743f8450541e3',
                                                'version1':version,
                                                'version2':version_min})
                        if ry['return']>0: return ry

                        if ry['comparison'] < 0:
                            version = version_min

                    if version_max != '':
                        ry = self.cmind.access({'action':'compare_versions',
                                                'automation':'utils,dc2743f8450541e3',
                                                'version1':version,
                                                'version2':version_max})
                        if ry['return']>0: return ry

                        if ry['comparison'] > 0:
                            if version_max_usable!='': 
                                version = version_max_usable
                            else:
                                version = version_max

                    if verbose:
                        print (recursion_spaces+'  - Version is not specified - use either default_version from meta or min/max/usable: {}'.format(version))

                    env['CM_VERSION'] = version

                    if 'version-'+version not in cached_tags: cached_tags.append('version-'+version)

                    if default_version in versions:
                        versions_meta = versions[default_version]
                        r = update_state_from_meta(versions_meta, env, state, deps, post_deps, prehook_deps, posthook_deps, new_env_keys_from_meta, new_state_keys_from_meta, i)
                        if r['return']>0: return r

                        if "add_deps_recursive" in versions_meta:
                            self._merge_dicts_with_tags(add_deps_recursive, versions_meta['add_deps_recursive'])

            # Run chain of docker dependencies if current run cmd is from inside a docker container
            docker_deps = []
            if i.get('docker_run_deps'):
                docker_meta = meta.get('docker')
                if docker_meta:
                    docker_deps = docker_meta.get('deps', [])
                    if docker_deps:
                        docker_deps = [ dep for dep in docker_deps if not dep.get('skip_inside_docker', False) ]

                if len(docker_deps)>0:

                    if verbose:
                        print (recursion_spaces + '  - Checking docker run dependencies on other CM scripts:')

                    r = self._call_run_deps(docker_deps, self.local_env_keys, local_env_keys_from_meta, env, state, const, const_state, add_deps_recursive, 
                        recursion_spaces + extra_recursion_spaces,
                        remembered_selections, variation_tags_string, False, debug_script_tags, verbose, show_time, extra_recursion_spaces, run_state)
                    if r['return']>0: return r

                    if verbose:
                        print (recursion_spaces + '  - Processing env after docker run dependencies ...')

                    r = update_env_with_values(env)
                    if r['return']>0: return r 

            # Check chain of dependencies on other CM scripts
            if len(deps)>0:
                if verbose:
                    print (recursion_spaces + '  - Checking dependencies on other CM scripts:')

                r = self._call_run_deps(deps, self.local_env_keys, local_env_keys_from_meta, env, state, const, const_state, add_deps_recursive, 
                        recursion_spaces + extra_recursion_spaces,
                        remembered_selections, variation_tags_string, False, debug_script_tags, verbose, show_time, extra_recursion_spaces, run_state)
                if r['return']>0: return r

                if verbose:
                    print (recursion_spaces + '  - Processing env after dependencies ...')

                r = update_env_with_values(env)
                if r['return']>0: return r 

            # Clean some output files
            clean_tmp_files(clean_files, recursion_spaces)

            # Check if has customize.py
            path_to_customize_py = os.path.join(path, 'customize.py')
            customize_code = None

            # Prepare common input to prepare and run script
            run_script_input = {
                   'path': path,
                   'bat_ext': bat_ext,
                   'os_info': os_info,
                   'const': const,
                   'state': state,
                   'const_state': const_state,
                   'reuse_cached': reuse_cached,
                   'recursion': recursion,
                   'recursion_spaces': recursion_spaces,
                   'remembered_selections': remembered_selections,
                   'tmp_file_run_state': self.tmp_file_run_state,
                   'tmp_file_run_env': self.tmp_file_run_env,
                   'tmp_file_state': self.tmp_file_state,
                   'tmp_file_run': self.tmp_file_run,
                   'local_env_keys': self.local_env_keys,
                   'local_env_keys_from_meta': local_env_keys_from_meta,
                   'posthook_deps': posthook_deps,
                   'add_deps_recursive': add_deps_recursive,
                   'remembered_selections': remembered_selections,
                   'found_script_tags': found_script_tags,
                   'variation_tags_string': variation_tags_string,
                   'found_cached': False,
                   'debug_script_tags': debug_script_tags,
                   'verbose': verbose,
                   'meta':meta,
                   'self': self
            }

            if repro_prefix != '': run_script_input['repro_prefix'] = repro_prefix
            if ignore_script_error: run_script_input['ignore_script_error'] = True

            if os.path.isfile(path_to_customize_py):
                r=utils.load_python_module({'path':path, 'name':'customize'})
                if r['return']>0: return r

                customize_code = r['code']

                customize_common_input = {
                   'input':i,
                   'automation':self,
                   'artifact':script_artifact,
                   'customize':script_artifact.meta.get('customize',{}),
                   'os_info':os_info,
                   'recursion_spaces':recursion_spaces,
                   'script_tags':script_tags,
                   'variation_tags':variation_tags
                }

                run_script_input['customize_code'] = customize_code
                run_script_input['customize_common_input'] = customize_common_input

            # Assemble PIP versions
            pip_version_string = ''

            pip_version = env.get('CM_VERSION', '')
            pip_version_min = env.get('CM_VERSION_MIN', '')
            pip_version_max = env.get('CM_VERSION_MAX', '')

            if pip_version != '':
                pip_version_string = '=='+pip_version
            elif pip_version_min != '' and pip_version_max != '':
                pip_version_string = '>='+pip_version_min+',<='+pip_version_max
            elif pip_version_min != '':
                pip_version_string = '>='+pip_version_min
            elif pip_version_max != '':
                pip_version_string = '<='+pip_version_max

            env['CM_TMP_PIP_VERSION_STRING'] = pip_version_string
            if pip_version_string != '':
                if verbose:
                    print (recursion_spaces+'    # potential PIP version string (if needed): '+pip_version_string)

            # Check if pre-process and detect
            if 'preprocess' in dir(customize_code) and not fake_run:

                if verbose:
                    print (recursion_spaces+'  - Running preprocess ...')

                # Update env and state with const
                utils.merge_dicts({'dict1':env, 'dict2':const, 'append_lists':True, 'append_unique':True})
                utils.merge_dicts({'dict1':state, 'dict2':const_state, 'append_lists':True, 'append_unique':True})

                run_script_input['run_state'] = run_state

                ii = copy.deepcopy(customize_common_input)
                ii['env'] = env
                ii['state'] = state
                ii['meta'] = meta
                ii['run_script_input'] = run_script_input # may need to detect versions in multiple paths

                r = customize_code.preprocess(ii)
                if r['return']>0: return r

                # Check if preprocess says to skip this component
                skip = r.get('skip', False)

                if skip:
                    if verbose:
                        print (recursion_spaces+'  - this script is skipped!')

                    # Check if script asks to run other dependencies instead of the skipped one
                    another_script = r.get('script', {})

                    if len(another_script) == 0:
                        return {'return':0, 'skipped': True}

                    if verbose:
                        print (recursion_spaces+'  - another script is executed instead!')

                    ii = {
                           'action':'run',
                           'automation':utils.assemble_cm_object(self.meta['alias'], self.meta['uid']),
                           'recursion_spaces':recursion_spaces + extra_recursion_spaces,
                           'recursion':True,
                           'remembered_selections': remembered_selections,
                           'env':env,
                           'state':state,
                           'const':const,
                           'const_state':const_state,
                           'save_env':save_env,
                           'add_deps_recursive':add_deps_recursive
                         }

                    ii.update(another_script)

                    # Return to current path
                    os.chdir(current_path)

                    ############################################################################################################
                    return self.cmind.access(ii)

                # If return version
                if cache:
                    if r.get('version','') != '':
                        cached_tags = [x for x in cached_tags if not x.startswith('version-')]
                        cached_tags.append('version-' + r['version'])

                    if len(r.get('add_extra_cache_tags',[]))>0:
                       for t in r['add_extra_cache_tags']:
                           if t not in cached_tags:
                               cached_tags.append(t) 


            if print_env:
                import json
                if verbose:
                    print (json.dumps(env, indent=2, sort_keys=True))

            # Check chain of pre hook dependencies on other CM scripts
            if len(prehook_deps)>0:
                if verbose:
                    print (recursion_spaces + '  - Checking prehook dependencies on other CM scripts:')

                r = self._call_run_deps(prehook_deps, self.local_env_keys, local_env_keys_from_meta,  env, state, const, const_state, add_deps_recursive, 
                    recursion_spaces + extra_recursion_spaces,
                    remembered_selections, variation_tags_string, found_cached, debug_script_tags, verbose, show_time, extra_recursion_spaces, run_state)
                if r['return']>0: return r

            if not fake_run:
                env_key_mappings = meta.get("env_key_mappings", {})
                if env_key_mappings:
                    update_env_keys(env, env_key_mappings)

                run_script_input['meta'] = meta
                run_script_input['env'] = env
                run_script_input['run_state'] = run_state
                run_script_input['recursion'] = recursion

                r = prepare_and_run_script_with_postprocessing(run_script_input)
                if r['return']>0: return r

                # If return version
                if r.get('version','') != '':
                    version = r.get('version')
                    if cache:
                        cached_tags = [x for x in cached_tags if not x.startswith('version-')]
                        cached_tags.append('version-' + r['version'])

                if len(r.get('add_extra_cache_tags',[]))>0 and cache:
                    for t in r['add_extra_cache_tags']:
                        if t not in cached_tags:
                            cached_tags.append(t) 

                # Check chain of post dependencies on other CM scripts
                clean_env_keys_post_deps = meta.get('clean_env_keys_post_deps',[])

                r = self._run_deps(post_deps, clean_env_keys_post_deps, env, state, const, const_state, add_deps_recursive, recursion_spaces,
                    remembered_selections, variation_tags_string, found_cached, debug_script_tags, verbose, show_time, extra_recursion_spaces, run_state)
                if r['return']>0: return r

            # Add extra tags from env updated by deps (such as python version and compiler version, etc)
            extra_cache_tags_from_env = meta.get('extra_cache_tags_from_env',[])
            for extra_cache_tags in extra_cache_tags_from_env:
                key = extra_cache_tags['env']
                prefix = extra_cache_tags.get('prefix','')

                v = env.get(key,'').strip()
                if v!='':
                    for t in v.split(','):
                        x = 'deps-' + prefix + t
                        if x not in cached_tags: 
                            cached_tags.append(x)


        detected_version = env.get('CM_DETECTED_VERSION', env.get('CM_VERSION',''))
        dependent_cached_path = env.get('CM_GET_DEPENDENT_CACHED_PATH','')

        ############################################################################################################
        ##################################### Finalize script

        # Force consts in the final new env and state
        utils.merge_dicts({'dict1':env, 'dict2':const, 'append_lists':True, 'append_unique':True})
        utils.merge_dicts({'dict1':state, 'dict2':const_state, 'append_lists':True, 'append_unique':True})

        if i.get('force_new_env_keys', []):
            new_env_keys = i['force_new_env_keys']
        else:
            new_env_keys = new_env_keys_from_meta

        if i.get('force_new_state_keys', []):
            new_state_keys = i['force_new_state_keys']
        else:
            new_state_keys = new_state_keys_from_meta

        r = detect_state_diff(env, saved_env, new_env_keys, new_state_keys, state, saved_state)
        if r['return']>0: return r

        new_env = r['new_env']
        new_state = r['new_state']

        utils.merge_dicts({'dict1':saved_env, 'dict2':new_env, 'append_lists':True, 'append_unique':True})
        utils.merge_dicts({'dict1':saved_state, 'dict2':new_state, 'append_lists':True, 'append_unique':True})



        # Restore original env/state and merge env/state
        # This is needed since we want to keep original env/state outside this script 
        # If we delete env and create a new dict, the original one outside this script will be detached
        # That's why we just clean all keys in original env/state (used oustide)
        # And then copy saved_env (with new_env merged) and saved_state (with new_state merged)
        # while getting rid of all temporal updates in env and state inside this script

        for k in list(env.keys()):
            del(env[k])
        for k in list(state.keys()):
            del(state[k])

        env.update(saved_env)
        state.update(saved_state)



        # Prepare env script content (to be saved in cache and in the current path if needed)
        env_script = convert_env_to_script(new_env, os_info, start_script = os_info['start_script'])

        # If using cached script artifact, return to default path and then update the cache script artifact
        if cache and cached_path!='':
            # Check if need to remove tag
            if remove_tmp_tag:
                # Save state, env and deps for reuse
                r =  utils.save_json(file_name = os.path.join(cached_path, self.file_with_cached_state), 
                        meta={'new_state':new_state, 'new_env':new_env, 'deps':deps, 'version': version})
                if r['return']>0: return r

                # Save all env
                env_all_script = convert_env_to_script(env, os_info, start_script = os_info['start_script'])

                r = record_script(os.path.join(cached_path, self.tmp_file_env_all + bat_ext),
                                  env_all_script, os_info)
                if r['return']>0: return r

                # Save env
                r = record_script(os.path.join(cached_path, self.tmp_file_env + bat_ext),
                                  env_script, os_info)
                if r['return']>0: return r

                # Remove tmp tag from the "cached" arifact to finalize caching
                if verbose:
                    print (recursion_spaces+'  - Removing tmp tag in the script cached output {} ...'.format(cached_uid))

                # Check if version was detected and record in meta)
                if detected_version != '':
                    cached_meta['version'] = detected_version

                if found_script_artifact != '':
                    cached_meta['associated_script_artifact'] = found_script_artifact

                    x = found_script_artifact.find(',')
                    if x<0:
                        return {'return':1, 'error':'CM artifact format is wrong "{}" - no comma found'.format(found_script_artifact)}

                    cached_meta['associated_script_artifact_uid'] = found_script_artifact[x+1:]


                # Check if the cached entry is dependent on any other cached entry
                if dependent_cached_path != '':
                    if os.path.isdir(cached_path) and os.path.isdir(dependent_cached_path):
                        if not os.path.samefile(cached_path, dependent_cached_path):
                            cached_meta['dependent_cached_path'] = dependent_cached_path

                ii = {'action': 'update',
                      'automation': self.meta['deps']['cache'],
                      'artifact': cached_uid,
                      'meta':cached_meta,
                      'replace_lists': True, # To replace tags
                      'tags':','.join(cached_tags)}

                r = self.cmind.access(ii)
                if r['return']>0: return r

        # Clean tmp files only in current path (do not touch cache - we keep all info there)
        script_path = os.getcwd()
        os.chdir(current_path)

        shell = i.get('shell', False)
#        if not shell:
#            shell = i.get('debug', False)

        if not shell and not i.get('dirty', False) and not cache:
            clean_tmp_files(clean_files, recursion_spaces)

        # Record new env and new state in the current dir if needed
        if save_env or shell:
            # Check if script_prefix in the state from other components
            where_to_add = len(os_info['start_script'])

            script_prefix = state.get('script_prefix',[])
            if len(script_prefix)>0:
                env_script.insert(where_to_add, '\n')
                for x in reversed(script_prefix):
                     env_script.insert(where_to_add, x)

            if shell:
                x=['cmd', '.', '','.bat',''] if os_info['platform'] == 'windows' else ['bash', ' ""', '"','.sh','. ./']

                env_script.append('\n')
                env_script.append('echo{}\n'.format(x[1]))
                env_script.append('echo {}Working path: {}{}'.format(x[2], script_path, x[2]))
                xtmp_run_file = ''
                tmp_run_file = 'tmp-run{}'.format(x[3])
                if os.path.isfile(tmp_run_file):
                    xtmp_run_file = 'Change and run "{}". '.format(tmp_run_file)
                
                env_script.append('echo {}Running debug shell. {}Type exit to quit ...{}\n'.format(x[2], xtmp_run_file, x[2]))
                env_script.append('echo{}\n'.format(x[1]))
                env_script.append('\n')
                env_script.append(x[0])

            env_file = self.tmp_file_env + bat_ext

            r = record_script(env_file, env_script, os_info)
            if r['return']>0: return r

            if shell:
                x = env_file if os_info['platform'] == 'windows' else '. ./'+env_file
                os.system(x)

        if not version and detected_version:
          version = detected_version

        if version:
            script_uid = script_artifact.meta.get('uid')
            script_alias = script_artifact.meta.get('alias')
            script_tags = script_artifact.meta.get('tags')
            version_info = {}
            version_info_tags = ",".join(script_tags + variation_tags)
            version_info[version_info_tags] = {}
            version_info[version_info_tags]['script_uid'] = script_uid
            version_info[version_info_tags]['script_alias'] = script_alias
            version_info[version_info_tags]['version'] = version
            version_info[version_info_tags]['parent'] = run_state['parent']
            run_state['version_info'].append(version_info)
            script_versions = detected_versions.get(meta['uid'], [])
            if not script_versions:
                detected_versions[meta['uid']] = [ version ]
            else:
                script_versions.append(version)
        else:
            pass # these scripts don't have versions. Should we use cm mlops version here?

        ############################# RETURN
        elapsed_time = time.time() - start_time

        if verbose and cached_uid!='':
            print (recursion_spaces+'  - cache UID: {}'.format(cached_uid))

        if print_deps:
            print_deps_data = self._print_deps(run_state['deps'])
            new_state['print_deps'] = print_deps_data

        if print_readme:
            readme = self._get_readme(i.get('cmd', ''), run_state['deps'])
            with open('readme.md', 'w') as f:
                f.write(readme)

        if i.get('dump_version_info'):
            r = self._dump_version_info_for_script()
            if r['return'] > 0:
                return r

        rr = {'return':0, 'env':env, 'new_env':new_env, 'state':state, 'new_state':new_state, 'deps': run_state['deps']}
        
        # Print output as json to console
        if i.get('json', False) or i.get('j', False):
            import json

            print ('')
            print (json.dumps(rr, indent=2))


        
        # Check if save json to file
        if repro_prefix !='':
            dump_repro(repro_prefix, rr, run_state)

        if verbose or show_time:
            print (recursion_spaces+'  - running time of script "{}": {:.2f} sec.'.format(','.join(found_script_tags), elapsed_time))


        if not recursion and show_space:
            stop_disk_stats = shutil.disk_usage("/")

            used_disk_space_in_mb = int((start_disk_stats.free - stop_disk_stats.free) / (1024*1024))

            if used_disk_space_in_mb > 0:
                print (recursion_spaces+'  - used disk space: {} MB'.format(used_disk_space_in_mb))


        # Check if pause (useful if running a given script in a new terminal that may close automatically)
        if i.get('pause', False):
            print ('')
            input ('Press Enter to continue ...')

        # Check if need to print some final info such as path to model, etc
        print_env_at_the_end = meta.get('print_env_at_the_end',{})
        if len(print_env_at_the_end)>0:
            print ('')

            for p in sorted(print_env_at_the_end):
                t = print_env_at_the_end[p]
                if t == '': t = 'ENV[{}]'.format(p)

                v = new_env.get(p, None)

                print ('{}: {}'.format(t, str(v)))

            print ('')

        return rr

    ######################################################################################
    def _dump_version_info_for_script(self, output_dir = os.getcwd()):
        import json
        with open(os.path.join(output_dir, 'version_info.json'), 'w') as f:
            f.write(json.dumps(self.run_state['version_info'], indent=2))
        return {'return': 0}

    ######################################################################################
    def _update_state_from_variations(self, i, meta, variation_tags, variations, env, state, deps, post_deps, prehook_deps, posthook_deps, new_env_keys_from_meta, new_state_keys_from_meta, add_deps_recursive, run_state, recursion_spaces, verbose):

        # Save current explicit variations
        import copy
        explicit_variation_tags=copy.deepcopy(variation_tags)

        # Calculate space
        required_disk_space = {}

        # Check if warning
        warnings = []

        # variation_tags get appended by any aliases
        r = self._get_variations_with_aliases(variation_tags, variations)
        if r['return'] > 0:
            return r
        variation_tags = r['variation_tags']
        excluded_variation_tags = r['excluded_variation_tags']

        # Get a dictionary of variation groups
        r = self._get_variation_groups(variations)
        if r['return'] > 0:
            return r

        variation_groups = r['variation_groups']

        run_state['variation_groups'] = variation_groups

        # Add variation(s) if specified in the "tags" input prefixed by _
          # If there is only 1 default variation, then just use it or substitute from CMD

        default_variation = meta.get('default_variation', '')

        if default_variation and default_variation not in variations:
            return {'return': 1, 'error': 'Default variation "{}" is not in the list of variations: "{}" '.format(default_variation, variations.keys())}

        if len(variation_tags) == 0:
            if default_variation != '' and default_variation not in excluded_variation_tags:
                variation_tags = [default_variation]

        r = self._update_variation_tags_from_variations(variation_tags, variations, variation_groups, excluded_variation_tags)
        if r['return'] > 0:
            return r

        # variation_tags get appended by any default on variation in groups
        r = self._process_variation_tags_in_groups(variation_tags, variation_groups, excluded_variation_tags, variations)
        if r['return'] > 0:
            return r
        if variation_tags != r['variation_tags']:
            variation_tags = r['variation_tags']

            # we need to again process variation tags if any new default variation is added
            r = self._update_variation_tags_from_variations(variation_tags, variations, variation_groups, excluded_variation_tags)
            if r['return'] > 0:
                return r


        valid_variation_combinations = meta.get('valid_variation_combinations', [])
        if valid_variation_combinations:
            if not any ( all(t in variation_tags for t in s) for s in valid_variation_combinations):
                return {'return': 1, 'error': 'Invalid variation combination "{}" prepared. Valid combinations: "{}" '.format(variation_tags, valid_variation_combinations)}

        invalid_variation_combinations = meta.get('invalid_variation_combinations', [])
        if invalid_variation_combinations:
            if any ( all(t in variation_tags for t in s) for s in invalid_variation_combinations):
                return {'return': 1, 'error': 'Invalid variation combination "{}" prepared. Invalid combinations: "{}" '.format(variation_tags, invalid_variation_combinations)}

        variation_tags_string = ''
        if len(variation_tags)>0:
            for t in variation_tags:
                if variation_tags_string != '':
                    variation_tags_string += ','

                x = '_' + t
                variation_tags_string += x

            if verbose:
                print (recursion_spaces+'    Prepared variations: {}'.format(variation_tags_string))

        # Update env and other keys if variations
        if len(variation_tags)>0:
            for variation_tag in variation_tags:
                if variation_tag.startswith('~'):
                    # ignore such tag (needed for caching only to differentiate variations)
                    continue

                if variation_tag.startswith('-'):
                    # ignore such tag (needed for caching only to eliminate variations)
                    continue

                variation_tag_dynamic_suffix = None
                if variation_tag not in variations:
                    if '.' in variation_tag and variation_tag[-1] != '.':
                        variation_tag_dynamic_suffix = variation_tag[variation_tag.index(".")+1:]
                        if not variation_tag_dynamic_suffix:
                            return {'return':1, 'error':'tag {} is not in variations {}'.format(variation_tag, variations.keys())}
                        variation_tag = self._get_name_for_dynamic_variation_tag(variation_tag)
                    if variation_tag not in variations:
                        return {'return':1, 'error':'tag {} is not in variations {}'.format(variation_tag, variations.keys())}

                variation_meta = variations[variation_tag]
                if variation_tag_dynamic_suffix:
                    self._update_variation_meta_with_dynamic_suffix(variation_meta, variation_tag_dynamic_suffix)

                r = update_state_from_meta(variation_meta, env, state, deps, post_deps, prehook_deps, posthook_deps, new_env_keys_from_meta, new_state_keys_from_meta, i)
                if r['return']>0: return r

                if variation_meta.get('script_name', '')!='':
                    meta['script_name'] = variation_meta['script_name']

                if variation_meta.get('required_disk_space', 0) > 0 and variation_tag not in required_disk_space:
                    required_disk_space[variation_tag] = variation_meta['required_disk_space']

                if variation_meta.get('warning', '') != '':
                    x = variation_meta['warning']
                    if x not in warnings: warnings.append()

                adr=get_adr(variation_meta)
                if adr:
                    self._merge_dicts_with_tags(add_deps_recursive, adr)

                combined_variations = [ t for t in variations if ',' in t ]

                combined_variations.sort(key=lambda x: x.count(','))
                ''' By sorting based on the number of variations users can safely override
                env and state in a larger combined variation
                '''

                for combined_variation in combined_variations:
                    v = combined_variation.split(",")
                    all_present = set(v).issubset(set(variation_tags))
                    if all_present:

                        combined_variation_meta = variations[combined_variation]

                        r = update_state_from_meta(combined_variation_meta, env, state, deps, post_deps, prehook_deps, posthook_deps, new_env_keys_from_meta, new_state_keys_from_meta, i)
                        if r['return']>0: return r

                        adr=get_adr(combined_variation_meta)
                        if adr:
                            self._merge_dicts_with_tags(add_deps_recursive, adr)

                        if combined_variation_meta.get('script_name', '')!='':
                            meta['script_name'] = combined_variation_meta['script_name']

                        if combined_variation_meta.get('required_disk_space', 0) > 0 and combined_variation not in required_disk_space:
                            required_disk_space[combined_variation] = combined_variation_meta['required_disk_space']

                        if combined_variation_meta.get('warning', '') != '':
                            x = combined_variation_meta['warning']
                            if x not in warnings: warnings.append(x)

            #Processing them again using updated deps for add_deps_recursive
            r = update_adr_from_meta(deps, post_deps, prehook_deps, posthook_deps, add_deps_recursive)
            if r['return']>0: return r

        if len(required_disk_space)>0:
            required_disk_space_sum_mb = sum(list(required_disk_space.values()))

            warnings.append('Required disk space: {} MB'.format(required_disk_space_sum_mb))

        return {'return': 0, 'variation_tags_string': variation_tags_string, 'explicit_variation_tags': explicit_variation_tags, 'warnings':warnings}

    ######################################################################################
    def _update_variation_tags_from_variations(self, variation_tags, variations, variation_groups, excluded_variation_tags):

        import copy
        tmp_variation_tags_static = copy.deepcopy(variation_tags)
        for v_i in range(len(tmp_variation_tags_static)):
            v = tmp_variation_tags_static[v_i]

            if v not in variations:
                v_static = self._get_name_for_dynamic_variation_tag(v)
                tmp_variation_tags_static[v_i] = v_static

        combined_variations = [ t for t in variations if ',' in t ]
        # We support default_variations in the meta of cmbined_variations
        combined_variations.sort(key=lambda x: x.count(','))
        ''' By sorting based on the number of variations users can safely override
            env and state in a larger combined variation
        '''
        tmp_combined_variations = {k: False for k in combined_variations}

        # Recursively add any base variations specified
        if len(variation_tags) > 0:
            tmp_variations = {k: False for k in variation_tags}
            while True:
                for variation_name in variation_tags:
                    tag_to_append = None

                    #ignore the excluded variations
                    if variation_name.startswith("~") or variation_name.startswith("-"):
                        tmp_variations[variation_name] = True
                        continue

                    if variation_name not in variations:
                        variation_name = self._get_name_for_dynamic_variation_tag(variation_name)

                    # base variations are automatically turned on. Only variations outside of any variation group can be added as a base_variation
                    if "base" in variations[variation_name]:
                        base_variations = variations[variation_name]["base"]
                        for base_variation in base_variations:
                            dynamic_base_variation = False
                            dynamic_base_variation_already_added = False
                            if base_variation not in variations:
                                base_variation_dynamic = self._get_name_for_dynamic_variation_tag(base_variation)
                                if not base_variation_dynamic or base_variation_dynamic not in variations:
                                    return {'return': 1, 'error': 'Variation "{}" specified as base variation of "{}" is not existing'.format(base_variation, variation_name)}
                                else:
                                    dynamic_base_variation = True
                                    base_prefix = base_variation_dynamic.split(".")[0]+"."
                                    for x in variation_tags:
                                        if x.startswith(base_prefix):
                                            dynamic_base_variation_already_added = True

                            if base_variation not in variation_tags and not dynamic_base_variation_already_added:
                                tag_to_append = base_variation

                            if tag_to_append:
                                if tag_to_append in excluded_variation_tags:
                                    return {'return': 1, 'error': 'Variation "{}" specified as base variation for the variation is in the excluded list "{}" '.format(tag_to_append, variation_name)}
                                variation_tags.append(tag_to_append)
                                tmp_variations[tag_to_append] = False

                            tag_to_append = None

                    # default_variations dictionary specifies the default_variation for each variation group. A default variation in a group is turned on if no other variation from that group is turned on and it is not excluded using the '-' prefix
                    r = self._get_variation_tags_from_default_variations(variations[variation_name], variations, variation_groups, tmp_variation_tags_static, excluded_variation_tags)
                    if r['return'] > 0:
                        return r

                    variations_to_add = r['variations_to_add']
                    for t in variations_to_add:
                        tmp_variations[t] = False
                        variation_tags.append(t)

                    tmp_variations[variation_name] = True

                    for combined_variation in combined_variations:
                        if tmp_combined_variations[combined_variation]:
                            continue
                        v = combined_variation.split(",")
                        all_present = set(v).issubset(set(variation_tags))
                        if all_present:
                            combined_variation_meta = variations[combined_variation]
                            tmp_combined_variations[combined_variation] = True

                            r = self._get_variation_tags_from_default_variations(combined_variation_meta, variations, variation_groups, tmp_variation_tags_static, excluded_variation_tags)
                            if r['return'] > 0:
                                return r

                            variations_to_add = r['variations_to_add']
                            for t in variations_to_add:
                                tmp_variations[t] = False
                                variation_tags.append(t)

                all_base_processed = True
                for variation_name in variation_tags:
                    if variation_name.startswith("-"):
                        continue
                    if variation_name not in variations:
                        variation_name = self._get_name_for_dynamic_variation_tag(variation_name)
                    if tmp_variations[variation_name] == False:
                        all_base_processed = False
                        break
                if all_base_processed:
                    break
        return {'return': 0}

    ######################################################################################
    def _get_variation_tags_from_default_variations(self, variation_meta, variations, variation_groups, tmp_variation_tags_static, excluded_variation_tags):
    # default_variations dictionary specifies the default_variation for each variation group. A default variation in a group is turned on if no other variation from that group is turned on and it is not excluded using the '-' prefix

        tmp_variation_tags = []
        if "default_variations" in variation_meta:
            default_base_variations = variation_meta["default_variations"]
            for default_base_variation in default_base_variations:
                tag_to_append = None

                if default_base_variation not in variation_groups:
                    return {'return': 1, 'error': 'Default variation "{}" is not a valid group. Valid groups are "{}" '.format(default_base_variation, variation_groups)}

                unique_allowed_variations = variation_groups[default_base_variation]['variations']
                # add the default only if none of the variations from the current group is selected and it is not being excluded with - prefix
                if len(set(unique_allowed_variations) & set(tmp_variation_tags_static)) == 0 and default_base_variations[default_base_variation] not in excluded_variation_tags and default_base_variations[default_base_variation] not in tmp_variation_tags_static:
                    tag_to_append = default_base_variations[default_base_variation]

                if tag_to_append:
                    if tag_to_append not in variations:
                        variation_tag_static = self._get_name_for_dynamic_variation_tag(tag_to_append)
                        if not variation_tag_static or variation_tag_static not in variations:
                            return {'return': 1, 'error': 'Invalid variation "{}" specified in default variations for the variation "{}" '.format(tag_to_append, variation_meta)}
                    tmp_variation_tags.append(tag_to_append)

        return {'return': 0, 'variations_to_add': tmp_variation_tags}

    ############################################################
    def version(self, i):
        """
        Print version

        Args:
            (CM input dict):

            (out) (str): if 'con', output to console

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

        """

        console = i.get('out') == 'con'

        version = self.__version__

        if console:
            print (version)

        return {'return':0, 'version':version}


    ############################################################
    def search(self, i):
        """
        Overriding the automation search function to filter out scripts not matching the given variation tags

        TBD: add input/output description
        """

        console = i.get('out') == 'con'

        # Check simplified CMD: cm run script "get compiler"
        # If artifact has spaces, treat them as tags!
        artifact = i.get('artifact','')
        if ' ' in artifact: # or ',' in artifact:
            del(i['artifact'])
            if 'parsed_artifact' in i: del(i['parsed_artifact'])
            # Force substitute tags
            i['tags']=artifact.replace(' ',',')
        
        ############################################################################################################
        # Process tags to find script(s) and separate variations 
        # (not needed to find scripts)
        tags_string = i.get('tags','').strip()

        tags = [] if tags_string == '' else tags_string.split(',')

        script_tags = []
        variation_tags = []

        for t in tags:
            t = t.strip()
            if t != '':
                if t.startswith('_'):
                    tx = t[1:]
                    if tx not in variation_tags:
                        variation_tags.append(tx)
                elif t.startswith('-_'):
                    tx = '-' + t[2:]
                    if tx not in variation_tags:
                        variation_tags.append(tx)
                else:
                    script_tags.append(t)

        excluded_tags =  [ v[1:] for v in script_tags if v.startswith("-") ]
        common = set(script_tags).intersection(set(excluded_tags))
        if common:
            return {'return':1, 'error': 'There is common tags {} in the included and excluded lists'.format(common)}

        excluded_variation_tags =  [ v[1:] for v in variation_tags if v.startswith("-") ]
        common = set(variation_tags).intersection(set(excluded_variation_tags))
        if common:
            return {'return':1, 'error': 'There is common variation tags {} in the included and excluded lists'.format(common)}

        ############################################################################################################
        # Find CM script(s) based on thier tags to get their meta (can be more than 1)
        # Then check if variations exists inside meta

        i['tags'] = ','.join(script_tags)

        i['out'] = None
        i['common'] = True

        r = super(CAutomation,self).search(i)
        if r['return']>0: return r

        lst = r['list']

        r['unfiltered_list'] = lst

        found_scripts = False if len(lst) == 0 else True

        if found_scripts and len(variation_tags)>0:
            filtered = []

            for script_artifact in lst:
                meta = script_artifact.meta
                variations = meta.get('variations', {})

                matched = True
                for t in variation_tags:
                    if t.startswith('-'):
                        t = t[1:]
                    if t in variations:
                        continue
                    matched = False
                    for s in variations:
                        if s.endswith('.#'):
                            if t.startswith(s[:-1]) and t[-1] != '.':
                                matched = True
                                break
                    if not matched:
                        break
                if not matched:
                    continue

                filtered.append(script_artifact)

            if len(lst) > 0 and not filtered:
                warning = [""]
                for script in lst:
                    meta = script.meta
                    variations = meta.get('variations', {})
                    warning.append('variation tags {} are not matching for the found script {} with variations {}\n'.format(variation_tags, meta.get('alias'), variations.keys()))
                r['warning'] = "\n".join(warning)

            r['list'] = filtered

        # Print filtered paths if console
        if console:
            for script in r['list']:
                print (script.path)

        # Finalize output
        r['script_tags'] = script_tags
        r['variation_tags'] = variation_tags
        r['found_scripts'] = found_scripts

        return r

    ############################################################
    def test(self, i):
        """
        Test automation (TBD)

        Args:
          (CM input dict): 

          (out) (str): if 'con', output to console

          automation (str): automation as CM string object

          parsed_automation (list): prepared in CM CLI or CM access function
                                    [ (automation alias, automation UID) ] or
                                    [ (automation alias, automation UID), (automation repo alias, automation repo UID) ]

          (artifact) (str): artifact as CM string object

          (parsed_artifact) (list): prepared in CM CLI or CM access function
                                    [ (artifact alias, artifact UID) ] or
                                    [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          * Output from this automation action

        """

        import json

        # Check parsed automation
        if 'parsed_automation' not in i:
           return {'return':1, 'error':'automation is not specified'}

        console = i.get('out') == 'con'

        # Find CM artifact(s)
        i['out'] = None
        r = self.search(i)

        if r['return']>0: return r

        lst = r['list']
        for script_artifact in lst:
            path = script_artifact.path
            meta = script_artifact.meta
            original_meta = script_artifact.original_meta

            alias = meta.get('alias','')
            uid = meta.get('uid','')

            if console:
                print ('')
                print (path)
                print ('  Test: TBD')


        return {'return':0, 'list': lst}


    ############################################################
    def native_run(self, i):
        """
        Add CM script

        Args:
          (CM input dict): 

          env (dict): environment
          command (str): string
          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

        """

        env = i.get('env', {})
        cmd = i.get('command', '')

        script = i.get('script',[])

        # Create temporary script name
        script_name = i.get('script_name','')
        if script_name=='': 
            script_name='tmp-native-run.'

            if os.name == 'nt':
                script_name+='bat'
            else:
                script_name+='sh'

        if os.name == 'nt':
            xcmd = 'call '+script_name

            if len(script)==0:
                script.append('@echo off')
                script.append('')
        else:
            xcmd = 'chmod 755 '+script_name+' ; ./'+script_name

            if len(script)==0:
                script.append('#!/bin/bash')
                script.append('')

        # Assemble env
        if len(env)>0:
            for k in env:
                v=env[k]

                if os.name == 'nt':
                    script.append('set '+k+'='+v)
                else:
                    if ' ' in v: v='"'+v+'"'
                    script.append('export '+k+'='+v)

            script.append('')

        # Add CMD        
        script.append(cmd)

        # Record script
        r = utils.save_txt(file_name=script_name, string='\n'.join(script))
        if r['return']>0: return r

        # Run script
        rc = os.system(xcmd)

        return {'return':0, 'return_code':rc}

    ############################################################
    def add(self, i):
        """
        Add CM script

        Args:
          (CM input dict): 

          (out) (str): if 'con', output to console

          parsed_artifact (list): prepared in CM CLI or CM access function
                                    [ (artifact alias, artifact UID) ] or
                                    [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

          (tags) (str): tags to find an CM script (CM artifact)

          (script_name) (str): name of script (it will be copied to the new entry and added to the meta)

          (tags) (string or list): tags to be added to meta

          (new_tags) (string or list): new tags to be added to meta (the same as tags)

          (json) (bool): if True, record JSON meta instead of YAML

          (meta) (dict): preloaded meta

          (template) (string): template to use (python)
          (python) (bool): template=python
          (pytorch) (bool): template=pytorch
          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

        """

        import shutil

        console = i.get('out') == 'con'

        # Try to find script artifact by alias and/or tags
        ii = utils.sub_input(i, self.cmind.cfg['artifact_keys'])

        parsed_artifact = i.get('parsed_artifact',[])

        artifact_obj = parsed_artifact[0] if len(parsed_artifact)>0 else None
        artifact_repo = parsed_artifact[1] if len(parsed_artifact)>1 else None

        script_name = ''
        if 'script_name' in i:
           script_name = i.get('script_name','').strip()
           del(i['script_name'])

           if script_name != '' and not os.path.isfile(script_name):
               return {'return':1, 'error':'file {} not found'.format(script_name)}

        # Move tags from input to meta of the newly created script artifact
        tags_list = utils.convert_tags_to_list(i)
        if 'tags' in i: del(i['tags'])

        if len(tags_list)==0:
            if console:
                x=input('Please specify a combination of unique tags separated by comma for this script: ')
                x = x.strip()
                if x!='':
                    tags_list = x.split(',')

        if len(tags_list)==0:
            return {'return':1, 'error':'you must specify a combination of unique tags separate by comman using "--new_tags"'}

        # Add placeholder (use common action)
        ii['out']='con'
        ii['common']=True # Avoid recursion - use internal CM add function to add the script artifact

        # Check template path
        template_dir = 'template'

        template = i.get('template','')

        if template == '':
           if i.get('python', False):
               template = 'python'
           elif i.get('pytorch', False):
               template = 'pytorch'

        if template!='':
            template_dir += '-'+template

        template_path = os.path.join(self.path, template_dir)

        if not os.path.isdir(template_path):
            return {'return':1, 'error':'template path {} not found'.format(template_path)}

        # Check if preloaded meta exists
        meta = {
                 'cache':False
# 20240127: Grigori commented that because newly created script meta looks ugly
#                 'new_env_keys':[],
#                 'new_state_keys':[],
#                 'input_mapping':{},
#                 'docker_input_mapping':{},
#                 'deps':[],
#                 'prehook_deps':[],
#                 'posthook_deps':[],
#                 'post_deps':[],
#                 'versions':{},
#                 'variations':{},
#                 'input_description':{}
               }

        fmeta = os.path.join(template_path, self.cmind.cfg['file_cmeta'])

        r = utils.load_yaml_and_json(fmeta)
        if r['return']==0:
            utils.merge_dicts({'dict1':meta, 'dict2':r['meta'], 'append_lists':True, 'append_unique':True})

        # Check meta from CMD
        xmeta = i.get('meta',{})

        if len(xmeta)>0:
            utils.merge_dicts({'dict1':meta, 'dict2':xmeta, 'append_lists':True, 'append_unique':True})

        meta['automation_alias']=self.meta['alias']
        meta['automation_uid']=self.meta['uid']
        meta['tags']=tags_list

        script_name_base = script_name
        script_name_ext = ''
        if script_name!='':
            # separate name and extension
            j=script_name.rfind('.')
            if j>=0:
                script_name_base = script_name[:j]
                script_name_ext = script_name[j:]

            meta['script_name'] = script_name_base

        ii['meta']=meta
        ii['action']='add'

        use_yaml = True if not i.get('json',False) else False

        if use_yaml:
            ii['yaml']=True

        ii['automation']='script,5b4e0237da074764'

        for k in ['parsed_automation', 'parsed_artifact']:
            if k in ii: del ii[k]

        if artifact_repo != None:
            artifact = ii.get('artifact','')
            ii['artifact'] = utils.assemble_cm_object2(artifact_repo) + ':' + artifact

        r_obj=self.cmind.access(ii)
        if r_obj['return']>0: return r_obj

        new_script_path = r_obj['path']

        if console:
            print ('Created script in {}'.format(new_script_path))

        # Copy files from template (only if exist)
        files = [
                 (template_path, 'README-extra.md', ''),
                 (template_path, 'customize.py', ''),
                 (template_path, 'main.py', ''),
                 (template_path, 'requirements.txt', ''),
                 (template_path, 'install_deps.bat', ''),
                 (template_path, 'install_deps.sh', ''),
                 (template_path, 'plot.bat', ''),
                 (template_path, 'plot.sh', ''),
                 (template_path, 'analyze.bat', ''),
                 (template_path, 'analyze.sh', ''),
                 (template_path, 'validate.bat', ''),
                 (template_path, 'validate.sh', '')
                ]

        if script_name == '':
            files += [(template_path, 'run.bat', ''),
                      (template_path, 'run.sh',  '')]
        else:
            if script_name_ext == '.bat':
                files += [(template_path, 'run.sh', script_name_base+'.sh')]
                files += [('', script_name, script_name)]

            else:
                files += [(template_path, 'run.bat', script_name_base+'.bat')]
                files += [('', script_name, script_name_base+'.sh')]


        for x in files:
            path = x[0]
            f1 = x[1]
            f2 = x[2]

            if f2 == '':
                f2 = f1

            if path!='':
                f1 = os.path.join(path, f1)

            if os.path.isfile(f1):
                f2 = os.path.join(new_script_path, f2)

                if console:
                    print ('  * Copying {} to {}'.format(f1, f2))

                shutil.copyfile(f1,f2)

        return r_obj

    ##############################################################################
    def _get_name_for_dynamic_variation_tag(script, variation_tag):
        '''
        Returns the variation name in meta for the dynamic_variation_tag
        '''
        if "." not in variation_tag or variation_tag[-1] == ".":
            return None
        return variation_tag[:variation_tag.index(".")+1]+"#"


    ##############################################################################
    def _update_variation_meta_with_dynamic_suffix(script, variation_meta, variation_tag_dynamic_suffix):
        '''
        Updates the variation meta with dynamic suffix
        '''
        for key in variation_meta:
            value = variation_meta[key]

            if type(value) is list: #deps,pre_deps...
                for item in value:
                    if type(item) is dict:
                        for item_key in item:
                            item_value = item[item_key]
                            if type(item_value) is dict: #env,default_env inside deps
                                for item_key2 in item_value:
                                    item_value[item_key2] = item_value[item_key2].replace("#", variation_tag_dynamic_suffix)
                            elif type(item_value) is list: #names for example
                                for i,l_item in enumerate(item_value):
                                    if type(l_item) is str:
                                        item_value[i] = l_item.replace("#", variation_tag_dynamic_suffix)
                            else:
                                item[item_key] = item[item_key].replace("#", variation_tag_dynamic_suffix)

            elif type(value) is dict: #add_deps, env, ..
                for item in value:
                    item_value = value[item]
                    if type(item_value) is dict: #deps
                        for item_key in item_value:
                            item_value2 = item_value[item_key]
                            if type(item_value2) is dict: #env,default_env inside deps
                                for item_key2 in item_value2:
                                    item_value2[item_key2] = item_value2[item_key2].replace("#", variation_tag_dynamic_suffix)
                            else:
                                item_value[item_key] = item_value[item_key].replace("#", variation_tag_dynamic_suffix)
                    else:
                        if type(item_value) is list: # lists inside env...
                            for i,l_item in enumerate(item_value):
                                if type(l_item) is str:
                                    item_value[i] = l_item.replace("#", variation_tag_dynamic_suffix)
                        else:
                            value[item] = value[item].replace("#", variation_tag_dynamic_suffix)

            else: #scalar value
                pass #no dynamic update for now


    ##############################################################################
    def _get_variations_with_aliases(script, variation_tags, variations):
        '''
        Automatically turn on variation tags which are aliased by any given tag
        '''
        import copy
        tmp_variation_tags=copy.deepcopy(variation_tags)

        excluded_variations = [ k[1:] for k in variation_tags if k.startswith("-") ]
        for i,e in enumerate(excluded_variations):
            if e not in variations:
                dynamic_tag = script._get_name_for_dynamic_variation_tag(e)
                if dynamic_tag and dynamic_tag in variations:
                    excluded_variations[i] = dynamic_tag

        for k in variation_tags:
            if k.startswith("-"):
                continue
            if k in variations:
                variation = variations[k]
            else:
                variation = variations[script._get_name_for_dynamic_variation_tag(k)]
            if 'alias' in variation:

                if variation['alias'] in excluded_variations:
                    return {'return': 1, 'error': 'Alias "{}" specified for the variation "{}" is conflicting with the excluded variation "-{}" '.format(variation['alias'], k, variation['alias'])}

                if variation['alias'] not in variations:
                    return {'return': 1, 'error': 'Alias "{}" specified for the variation "{}" is not existing '.format(variation['alias'], k)}

                if 'group' in variation:
                    return {'return': 1, 'error': 'Incompatible combinations: (alias, group) specified for the variation "{}" '.format(k)}

                if 'default' in variation:
                    return {'return': 1, 'error': 'Incompatible combinations: (default, group) specified for the variation "{}" '.format(k)}

                if variation['alias'] not in tmp_variation_tags:
                    tmp_variation_tags.append(variation['alias'])

        return {'return':0, 'variation_tags': tmp_variation_tags, 'excluded_variation_tags': excluded_variations}



    ##############################################################################
    def _get_variation_groups(script, variations):

        groups = {}

        for k in variations:
            variation = variations[k]
            if not variation:
                continue
            if 'group' in variation:
                if variation['group'] not in groups:
                    groups[variation['group']] = {}
                    groups[variation['group']]['variations'] = []
                groups[variation['group']]['variations'].append(k)
                if 'default' in variation:
                    if 'default' in groups[variation['group']]:
                        return {'return': 1, 'error': 'Multiple defaults specied for the variation group "{}": "{},{}" '.format(variation['group'], k, groups[variation['group']]['default'])}
                    groups[variation['group']]['default'] = k

        return {'return': 0, 'variation_groups': groups}


    ##############################################################################
    def _process_variation_tags_in_groups(script, variation_tags, groups, excluded_variations, variations):
        import copy
        tmp_variation_tags = copy.deepcopy(variation_tags)
        tmp_variation_tags_static = copy.deepcopy(variation_tags)

        for v_i in range(len(tmp_variation_tags_static)):
            v = tmp_variation_tags_static[v_i]

            if v not in variations:
                v_static = script._get_name_for_dynamic_variation_tag(v)
                tmp_variation_tags_static[v_i] = v_static

        for k in groups:
            group = groups[k]
            unique_allowed_variations = group['variations']

            if len(set(unique_allowed_variations) & set(tmp_variation_tags_static)) > 1:
                return {'return': 1, 'error': 'Multiple variation tags selected for the variation group "{}": {} '.format(k, str(set(unique_allowed_variations) & set(tmp_variation_tags_static)))}
            if len(set(unique_allowed_variations) & set(tmp_variation_tags_static)) == 0:
                if 'default' in group and group['default'] not in excluded_variations:
                    tmp_variation_tags.append(group['default'])

        return {'return':0, 'variation_tags': tmp_variation_tags}






    ##############################################################################
    def _call_run_deps(script, deps, local_env_keys, local_env_keys_from_meta, env, state, const, const_state,
            add_deps_recursive, recursion_spaces, remembered_selections, variation_tags_string, found_cached, debug_script_tags='', 
            verbose=False, show_time=False, extra_recursion_spaces='  ', run_state={'deps':[], 'fake_deps':[], 'parent': None}):
        if len(deps) == 0:
            return {'return': 0}

        # Check chain of post hook dependencies on other CM scripts
        import copy

        # Get local env keys
        local_env_keys = copy.deepcopy(local_env_keys)

        if len(local_env_keys_from_meta)>0:
            local_env_keys += local_env_keys_from_meta

        r = script._run_deps(deps, local_env_keys, env, state, const, const_state, add_deps_recursive, recursion_spaces,
            remembered_selections, variation_tags_string, found_cached, debug_script_tags, 
            verbose, show_time, extra_recursion_spaces, run_state)
        if r['return']>0: return r

        return {'return': 0}

    ##############################################################################
    def _run_deps(self, deps, clean_env_keys_deps, env, state, const, const_state, add_deps_recursive, recursion_spaces, 
                    remembered_selections, variation_tags_string='', from_cache=False, debug_script_tags='', 
                  verbose=False, show_time=False, extra_recursion_spaces='  ', run_state={'deps':[], 'fake_deps':[], 'parent': None}):
        """
        Runs all the enabled dependencies and pass them env minus local env
        """

        if len(deps)>0:
            # Preserve local env
            tmp_env = {}

            variation_groups = run_state.get('variation_groups')

            for d in deps:

                if not d.get('tags'):
                    continue

                if d.get('skip_if_fake_run', False) and env.get('CM_TMP_FAKE_RUN','')=='yes':
                    continue
                
                if "enable_if_env" in d:
                    if not enable_or_skip_script(d["enable_if_env"], env):
                        continue

                if "skip_if_env" in d:
                    if enable_or_skip_script(d["skip_if_env"], env):
                        continue

                if from_cache and not d.get("dynamic", None):
                    continue

                update_tags_from_env_with_prefix = d.get("update_tags_from_env_with_prefix", {})
                for t in update_tags_from_env_with_prefix:
                    for key in update_tags_from_env_with_prefix[t]:
                        if str(env.get(key, '')).strip() != '':
                            d['tags']+=","+t+str(env[key])

                for key in clean_env_keys_deps:
                    if '?' in key or '*' in key:
                        import fnmatch
                        for kk in list(env.keys()):
                            if fnmatch.fnmatch(kk, key):
                                tmp_env[kk] = env[kk]
                                del(env[kk])
                    elif key in env:
                        tmp_env[key] = env[key]
                        del(env[key])

                import re
                for key in list(env.keys()):
                    value = env[key]
                    tmp_values = re.findall(r'<<<(.*?)>>>', str(value))
                    if tmp_values == []: continue
                    tmp_env[key] = env[key]
                    del(env[key])

                force_env_keys_deps = d.get("force_env_keys", [])
                for key in force_env_keys_deps:
                    if '?' in key or '*' in key:
                        import fnmatch
                        for kk in list(tmp_env.keys()):
                            if fnmatch.fnmatch(kk, key):
                                env[kk] = tmp_env[kk]
                    elif key in tmp_env:
                        env[key] = tmp_env[key]

                if d.get("reuse_version", False):
                    for k in tmp_env:
                        if k.startswith('CM_VERSION'):
                            env[k] = tmp_env[k]

                update_tags_from_env = d.get("update_tags_from_env", [])
                for t in update_tags_from_env:
                    if env.get(t, '').strip() != '':
                        d['tags']+=","+env[t]

                inherit_variation_tags = d.get("inherit_variation_tags", False)
                skip_inherit_variation_groups = d.get("skip_inherit_variation_groups", [])
                variation_tags_to_be_skipped = []
                if inherit_variation_tags:
                    if skip_inherit_variation_groups: #skips inheriting variations belonging to given groups
                        for group in variation_groups:
                            if group in skip_inherit_variation_groups:
                                variation_tags_to_be_skipped += variation_groups[group]['variations']

                    variation_tags = variation_tags_string.split(",")
                    variation_tags =  [ x for x in variation_tags if not x.startswith("_") or x[1:] not in set(variation_tags_to_be_skipped) ]

                    # handle group in case of dynamic variations
                    for t_variation in variation_tags_to_be_skipped:
                        if t_variation.endswith(".#"):
                            beg = t_variation[:-1]
                            for m_tag in variation_tags:
                                if m_tag.startswith("_"+beg):
                                    variation_tags.remove(m_tag)

                    deps_tags = d['tags'].split(",")
                    for tag in deps_tags:
                        if tag.startswith("-_") or tag.startswith("_-"):
                            variation_tag = "_" + tag[2:]
                            if variation_tag in variation_tags:
                                variation_tags.remove(variation_tag)
                    new_variation_tags_string = ",".join(variation_tags)
                    d['tags']+=","+new_variation_tags_string #deps should have non-empty tags

                run_state['deps'].append(d['tags'])

                if not run_state['fake_deps']:
                    import copy
                    tmp_run_state_deps = copy.deepcopy(run_state['deps'])
                    run_state['deps'] = []
                    tmp_parent = run_state['parent']
                    run_state['parent'] = run_state['script_id']+":"+",".join(run_state['script_variation_tags'])
                    tmp_script_id = run_state['script_id']
                    tmp_script_variation_tags = run_state['script_variation_tags']

                    # Run collective script via CM API:
                    # Not very efficient but allows logging - can be optimized later
                    ii = {
                            'action':'run',
                            'automation':utils.assemble_cm_object(self.meta['alias'], self.meta['uid']),
                            'recursion_spaces':recursion_spaces, # + extra_recursion_spaces,
                            'recursion':True,
                            'remembered_selections': remembered_selections,
                            'env':env,
                            'state':state,
                            'const':const,
                            'const_state':const_state,
                            'add_deps_recursive':add_deps_recursive,
                            'debug_script_tags':debug_script_tags,
                            'verbose':verbose,
                            'time':show_time,
                            'run_state':run_state

                        }

                    for key in [ "env", "state", "const", "const_state" ]:
                        ii['local_'+key] = d.get(key, {})
                        if d.get(key):
                            d[key] = {}

                    utils.merge_dicts({'dict1':ii, 'dict2':d, 'append_lists':True, 'append_unique':True})

                    r = update_env_with_values(ii['env']) #to update env local to a dependency
                    if r['return']>0: return r 

                    r = self.cmind.access(ii)
                    if r['return']>0: return r

                    run_state['deps'] = tmp_run_state_deps
                    run_state['parent'] = tmp_parent
                    run_state['script_id'] = tmp_script_id
                    run_state['script_variation_tags'] = tmp_script_variation_tags

                    # Restore local env
                    env.update(tmp_env)
                    r = update_env_with_values(env)
                    if r['return']>0: return r 

        return {'return': 0}

    ##############################################################################
    def _merge_dicts_with_tags(self, dict1, dict2):
        """
        Merges two dictionaries and append any tag strings in them
        """
        if dict1 == dict2:
            return {'return': 0}
        for dep in dict1:
            if 'tags' in dict1[dep]:
                dict1[dep]['tags_list'] = utils.convert_tags_to_list(dict1[dep])
        for dep in dict2:
            if 'tags' in dict2[dep]:
                dict2[dep]['tags_list'] = utils.convert_tags_to_list(dict2[dep])
        utils.merge_dicts({'dict1':dict1, 'dict2':dict2, 'append_lists':True, 'append_unique':True})
        for dep in dict1:
            if 'tags_list' in dict1[dep]:
                dict1[dep]['tags'] = ",".join(dict1[dep]['tags_list'])
                del(dict1[dep]['tags_list'])
        for dep in dict2:
            if 'tags_list' in dict2[dep]:
                del(dict2[dep]['tags_list'])

    ##############################################################################
    def _get_readme(self, cmd_parts, deps):
        """
        Outputs a Markdown README file listing the CM run commands for the dependencies
        """
        pre = ''
        content = pre
        heading2 = "## Command to Run\n"
        content += heading2
        cmd="cm run script "
        for cmd_part in cmd_parts:
            cmd = cmd+ " "+cmd_part
        content += "\n"
        cmd = self._markdown_cmd(cmd)
        content = content + cmd + "\n\n"
        deps_heading = "## Dependent CM scripts\n"
        deps_ = ""
        run_cmds = self._get_deps_run_cmds(deps)
        i = 1
        for cmd in run_cmds:
            deps_ = deps_+ str(i) + ". " + self._markdown_cmd(cmd)+"\n"
            i = i+1
        if deps_:
            content += deps_heading
            content += deps_
        return content

    ##############################################################################
    def _markdown_cmd(self, cmd):
        """
        Returns a CM command in markdown format
        """
        return '```bash\n '+cmd+' \n ```'


    ##############################################################################
    def _print_deps(self, deps):
        """
        Prints the CM run commands for the list of CM script dependencies
        """
        print_deps_data = []
        run_cmds = self._get_deps_run_cmds(deps)
        for cmd in run_cmds:
            print_deps_data.append(cmd)
            print(cmd)
        return print_deps_data


    ##############################################################################
    def _get_deps_run_cmds(self, deps):
        """
        Returns the CM run commands for the list of CM script dependencies
        """
        run_cmds = []
        for dep_tags in deps:
            run_cmds.append("cm run script --tags="+dep_tags)
        return run_cmds





    ##############################################################################
    def run_native_script(self, i):
        """
        Run native script in a CM script entry
        (wrapper around "prepare_and_run_script_with_postprocessing" function)

        Args:
          (dict):

            run_script_input (dict): saved input for "prepare_and_run_script_with_postprocessing" function
            env (dict): the latest environment for the script
            script_name (str): native script name

        Returns:
          (dict): Output from "prepare_and_run_script_with_postprocessing" function


        """

        import copy

        run_script_input = i['run_script_input']
        script_name = i['script_name']
        env = i.get('env','')

        # Create and work on a copy to avoid contamination
        env_copy = copy.deepcopy(run_script_input.get('env',{}))
        run_script_input_state_copy = copy.deepcopy(run_script_input.get('state',{}))
        script_name_copy = run_script_input.get('script_name','')

        run_script_input['script_name'] = script_name
        run_script_input['env'] = env

        r = prepare_and_run_script_with_postprocessing(run_script_input, postprocess="")

        env_tmp = copy.deepcopy(run_script_input['env'])
        r['env_tmp'] = env_tmp

        run_script_input['state'] = run_script_input_state_copy
        run_script_input['env'] = env_copy
        run_script_input['script_name'] = script_name_copy

        return r

    ##############################################################################
    def find_file_in_paths(self, i):
        """
        Find file name in a list of paths

        Args:
          (CM input dict):

          paths (list): list of paths
          file_name (str): filename pattern to find
          (select) (bool): if True and more than 1 path found, select
          (select_default) (bool): if True, select the default one
          (recursion_spaces) (str): add space to print
          (run_script_input) (dict): prepared dict to run script and detect version

          (detect_version) (bool): if True, attempt to detect version
          (env_path) (str): env key to pass path to the script to detect version
          (run_script_input) (dict): use this input to run script to detect version
          (env) (dict): env to check/force version

          (hook) (func): call this func to skip some artifacts

        Returns:
           (CM return dict):

           * return (int): return code == 0 if no error and >0 if error
           * (error) (str): error string if return>0

           (found_files) (list): paths to files when found

        """
        import copy

        paths = i['paths']
        select = i.get('select',False)
        select_default = i.get('select_default', False)
        recursion_spaces = i.get('recursion_spaces','')

        hook = i.get('hook', None)

        verbose = i.get('verbose', False)
        if not verbose: verbose = i.get('v', False)

        file_name = i.get('file_name', '')
        file_name_re = i.get('file_name_re', '')
        file_is_re = False

        if file_name_re != '':
            file_name = file_name_re
            file_is_re = True

        if file_name == '':
            raise Exception('file_name or file_name_re not specified in find_artifact')

        found_files = []

        import glob
        import re

        for path in paths:
            # May happen that path is in variable but it doesn't exist anymore
            if os.path.isdir(path):
                if file_is_re:
                    file_list = [os.path.join(path,f)  for f in os.listdir(path) if re.match(file_name, f)]

                    for f in file_list:
                        duplicate = False
                        for existing in found_files:
                            if os.path.samefile(existing, f):
                                duplicate = True
                                break
                        if not duplicate:
                            skip = False
                            if hook!=None:
                               r=hook({'file':f})
                               if r['return']>0: return r
                               skip = r['skip']
                            if not skip:
                                found_files.append(f)

                else:
                    path_to_file = os.path.join(path, file_name)

                    file_pattern_suffixes = [
                            "",
                            ".[0-9]",
                            ".[0-9][0-9]",
                            "-[0-9]",
                            "-[0-9][0-9]",
                            "[0-9]",
                            "[0-9][0-9]",
                            "[0-9].[0-9]",
                            "[0-9][0-9].[0-9]",
                            "[0-9][0-9].[0-9][0-9]"
                            ]

                    for suff in file_pattern_suffixes:
                        file_list = glob.glob(path_to_file + suff)
                        for f in file_list:
                            duplicate = False

                            for existing in found_files:
                                try:
                                    if os.path.samefile(existing, f):
                                        duplicate = True
                                        break
                                except Exception as e:
                                    # This function fails on Windows sometimes 
                                    # because some files can't be accessed
                                    pass

                            if not duplicate:
                                skip = False
                                if hook!=None:
                                   r=hook({'file':f})
                                   if r['return']>0: return r
                                   skip = r['skip']
                                if not skip:
                                    found_files.append(f)


        if select:
            # Check and prune versions
            if i.get('detect_version', False):
                found_paths_with_good_version = []
                found_files_with_good_version = []

                env = i.get('env', {})

                run_script_input = i['run_script_input']
                env_path_key = i['env_path_key']

                version = env.get('CM_VERSION', '')
                version_min = env.get('CM_VERSION_MIN', '')
                version_max = env.get('CM_VERSION_MAX', '')

                x = ''

                if version != '': x += ' == {}'.format(version)
                if version_min != '': x += ' >= {}'.format(version_min)
                if version_max != '': x += ' <= {}'.format(version_max)

                if x!='':
                    print (recursion_spaces + '  - Searching for versions: {}'.format(x))

                new_recursion_spaces = recursion_spaces + '    '


                for path_to_file in found_files:

                    print ('')
                    print (recursion_spaces + '    * ' + path_to_file)

                    run_script_input['env'] = env
                    run_script_input['env'][env_path_key] = path_to_file
                    run_script_input['recursion_spaces'] = new_recursion_spaces

                    rx = prepare_and_run_script_with_postprocessing(run_script_input, postprocess="detect_version")

                    run_script_input['recursion_spaces'] = recursion_spaces

                    if rx['return']>0:
                       if rx['return'] != 2:
                           return rx
                    else:
                       # Version was detected
                       detected_version = rx.get('version','')

                       if detected_version != '':
                           if detected_version == -1:
                               print (recursion_spaces + '    SKIPPED due to incompatibility ...')
                           else:
                               ry = check_version_constraints({'detected_version': detected_version,
                                                               'version': version,
                                                               'version_min': version_min,
                                                               'version_max': version_max,
                                                               'cmind':self.cmind})
                               if ry['return']>0: return ry

                               if not ry['skip']:
                                   found_files_with_good_version.append(path_to_file)
                               else:
                                   print (recursion_spaces + '    SKIPPED due to version constraints ...')

                found_files = found_files_with_good_version

            # Continue with selection
            if len(found_files)>1:
                if len(found_files) == 1 or select_default:
                    selection = 0
                else:
                    # Select 1 and proceed
                    print (recursion_spaces+'  - More than 1 path found:')

                    print ('')
                    num = 0

                    for file in found_files:
                        print (recursion_spaces+'  {}) {}'.format(num, file))
                        num += 1

                    print ('')
                    x=input(recursion_spaces+'  Make your selection or press Enter for 0: ')

                    x=x.strip()
                    if x=='': x='0'

                    selection = int(x)

                    if selection < 0 or selection >= num:
                        selection = 0

                print ('')
                print (recursion_spaces+'  Selected {}: {}'.format(selection, found_files[selection]))

                found_files = [found_files[selection]]

        return {'return':0, 'found_files':found_files}

    ##############################################################################
    def detect_version_using_script(self, i):
        """
        Detect version using script

        Args:
          (CM input dict): 

          (recursion_spaces) (str): add space to print

          run_script_input (dict): use this input to run script to detect version
          (env) (dict): env to check/force version

        Returns:
           (CM return dict):

           * return (int): return code == 0 if no error and >0 if error
                                             16 if not detected
           * (error) (str): error string if return>0

           (detected_version) (str): detected version

        """
        recursion_spaces = i.get('recursion_spaces','')

        import copy

        detected = False

        env = i.get('env', {})

        run_script_input = i['run_script_input']

        version = env.get('CM_VERSION', '')
        version_min = env.get('CM_VERSION_MIN', '')
        version_max = env.get('CM_VERSION_MAX', '')

        x = ''

        if version != '': x += ' == {}'.format(version)
        if version_min != '': x += ' >= {}'.format(version_min)
        if version_max != '': x += ' <= {}'.format(version_max)

        if x!='':
            print (recursion_spaces + '  - Searching for versions: {}'.format(x))

        new_recursion_spaces = recursion_spaces + '    '

        run_script_input['recursion_spaces'] = new_recursion_spaces
        run_script_input['env'] = env

        # Prepare run script
        rx = prepare_and_run_script_with_postprocessing(run_script_input, postprocess="detect_version")

        run_script_input['recursion_spaces'] = recursion_spaces

        if rx['return'] == 0: 
           # Version was detected 
           detected_version = rx.get('version','')

           if detected_version != '':
               ry = check_version_constraints({'detected_version': detected_version,
                                               'version': version,
                                               'version_min': version_min,
                                               'version_max': version_max,
                                               'cmind':self.cmind})
               if ry['return']>0: return ry

               if not ry['skip']:
                   return {'return':0, 'detected_version':detected_version}

        return {'return':16, 'error':'version was not detected'}

    ##############################################################################
    def find_artifact(self, i):
        """
        Find some artifact (file) by name

        Args:
          (CM input dict): 

          file_name (str): filename to find

          env (dict): global env
          os_info (dict): OS info

          (detect_version) (bool): if True, attempt to detect version
          (env_path) (str): env key to pass path to the script to detect version
          (run_script_input) (dict): use this input to run script to detect version

          (default_path_env_key) (str): check in default paths from global env 
                                        (PATH, PYTHONPATH, LD_LIBRARY_PATH ...)

          (recursion_spaces) (str): add space to print

          (hook) (func): call this func to skip some artifacts

        Returns:
           (CM return dict):

           * return (int): return code == 0 if no error and >0 if error
           * (error) (str): error string if return>0
                            error = 16 if artifact not found but no problem

           found_path (list): found path to an artifact
           full_path (str): full path to a found artifact
           default_path_list (list): list of default paths 

        """

        import copy

        file_name = i['file_name']

        os_info = i['os_info']

        env = i['env']

        env_path_key = i.get('env_path_key', '')

        run_script_input = i.get('run_script_input', {})
        extra_paths = i.get('extra_paths', {})

        # Create and work on a copy to avoid contamination
        env_copy = copy.deepcopy(env)
        run_script_input_state_copy = copy.deepcopy(run_script_input.get('state',{}))

        default_path_env_key = i.get('default_path_env_key', '')
        recursion_spaces = i.get('recursion_spaces', '')

        hook = i.get('hook', None)

        # Check if forced to search in a specific path or multiple paths 
        # separated by OS var separator (usually : or ;)
        path = env.get('CM_TMP_PATH','')

        if path!='' and env.get('CM_TMP_PATH_IGNORE_NON_EXISTANT','')!='yes':
            # Can be a list of paths
            path_list_tmp = path.split(os_info['env_separator'])
            for path_tmp in path_list_tmp:
                if path_tmp.strip()!='' and not os.path.isdir(path_tmp):
                    return {'return':1, 'error':'path {} doesn\'t exist'.format(path_tmp)}

        # Check if forced path and file name from --input (CM_INPUT - local env - will not be visible for higher-level script)
        forced_file = env.get('CM_INPUT','').strip()
        if forced_file != '':
            if not os.path.isfile(forced_file):
                return {'return':1, 'error':'file {} doesn\'t exist'.format(forced_file)}

            file_name = os.path.basename(forced_file)
            path = os.path.dirname(forced_file)

        default_path_list = self.get_default_path_list(i)
        #[] if default_path_env_key == '' else \
        #   os.environ.get(default_path_env_key,'').split(os_info['env_separator'])


        if path == '':
            path_list_tmp = default_path_list
        else:
            print (recursion_spaces + '    # Requested paths: {}'.format(path))
            path_list_tmp = path.split(os_info['env_separator'])

        # Check soft links
        path_list_tmp2 = []
        for path_tmp in path_list_tmp:
#            path_tmp_abs = os.path.realpath(os.path.join(path_tmp, file_name))
#            GF: I remarked above code because it doesn't work correcly
#                for virtual python - it unsoftlinks virtual python and picks up
#                native one from /usr/bin thus making workflows work incorrectly ...
            path_tmp_abs = os.path.join(path_tmp, file_name)

            if not path_tmp_abs in path_list_tmp2:
                path_list_tmp2.append(path_tmp_abs)

        path_list = []
        for path_tmp in path_list_tmp2:
            path_list.append(os.path.dirname(path_tmp))

        # Check if quiet
        select_default = True if env.get('CM_QUIET','') == 'yes' else False

        # Prepare paths to search
        r = self.find_file_in_paths({'paths': path_list,
                                     'file_name': file_name, 
                                     'select': True,
                                     'select_default': select_default,
                                     'detect_version': i.get('detect_version', False),
                                     'env_path_key': env_path_key,
                                     'env':env_copy,
                                     'hook':hook,
                                     'run_script_input': run_script_input,
                                     'recursion_spaces': recursion_spaces})

        run_script_input['state'] = run_script_input_state_copy

        if r['return']>0: return r

        found_files = r['found_files']

        if len(found_files)==0:
            return {'return':16, 'error':'{} not found'.format(file_name)}

        # Finalize output
        file_path = found_files[0]
        found_path = os.path.dirname(file_path)

        if found_path not in default_path_list:
            env_key = '+'+default_path_env_key

            paths = env.get(env_key, [])
            if found_path not in paths:
                paths.insert(0, found_path)
                env[env_key] = paths
            for extra_path in extra_paths:
                epath = os.path.normpath(os.path.join(found_path, "..", extra_path))
                if os.path.exists(epath):
                    if extra_paths[extra_path] not in env:
                        env[extra_paths[extra_path]] = []
                    env[extra_paths[extra_path]].append(epath)
        print ()
        print (recursion_spaces + '    # Found artifact in {}'.format(file_path))

        if env_path_key != '':
            env[env_path_key] = file_path

        return {'return':0, 'found_path':found_path, 
                            'found_file_path':file_path,
                            'found_file_name':os.path.basename(file_path),
                            'default_path_list': default_path_list}

    ##############################################################################
    def find_file_deep(self, i):
        """
        Find file name in a list of paths

        Args:
          (CM input dict):

            paths (list): list of paths
            file_name (str): filename pattern to find
            (restrict_paths) (list): restrict found paths to these combinations

        Returns:
           (CM return dict):

           * return (int): return code == 0 if no error and >0 if error
           * (error) (str): error string if return>0

           (found_paths) (list): paths to files when found

        """

        paths = i['paths']
        file_name = i['file_name']

        restrict_paths = i.get('restrict_paths',[])

        found_paths = []

        for p in paths:
            if os.path.isdir(p):
                p1 = os.listdir(p)
                for f in p1:
                    p2 = os.path.join(p, f)

                    if os.path.isdir(p2):
                       r = self.find_file_deep({'paths':[p2], 'file_name': file_name, 'restrict_paths':restrict_paths})
                       if r['return']>0: return r

                       found_paths += r['found_paths']
                    else:
                       if f == file_name:
                           found_paths.append(p)
                           break

        if len(found_paths) > 0 and len(restrict_paths) > 0:
            filtered_found_paths = []

            for p in found_paths:
                for f in restrict_paths:
                    if f in p:
                        filtered_found_paths.append(p)
                        break

            found_paths = filtered_found_paths

        return {'return':0, 'found_paths':found_paths}

    ##############################################################################
    def find_file_back(self, i):
        """
        Find file name backwards

        Args:
          (CM input dict):

            path (str): path to start with
            file_name (str): filename or directory to find

        Returns:
           (CM return dict):

           * return (int): return code == 0 if no error and >0 if error
           * (error) (str): error string if return>0

           (found_path) (str): path if found or empty

        """

        path = i['path']
        file_name = i['file_name']

        found_path = ''

        while path != '':
            path_to_file = os.path.join(path, file_name)
            if os.path.isfile(path_to_file):
                break

            path2 = os.path.dirname(path)

            if path2 == path:
                path = ''
                break
            else:
                path = path2

        return {'return':0, 'found_path':path}

    ##############################################################################
    def parse_version(self, i):
        """
        Parse version (used in post processing functions)

        Args:
          (CM input dict): 

            (file_name) (str): filename to get version from (tmp-ver.out by default)
            match_text (str): RE match text string
            group_number (int): RE group number to get version from
            env_key (str): which env key to update
            which_env (dict): which env to update
            (debug) (boolean): if True, print some debug info

        Returns:
           (CM return dict):

           * return (int): return code == 0 if no error and >0 if error
           * (error) (str): error string if return>0

           version (str): detected version
           string (str): full file string

        """

        file_name = i.get('file_name','')
        if file_name == '': file_name = self.tmp_file_ver

        match_text = i['match_text']
        group_number = i['group_number']
        env_key = i['env_key']
        which_env = i['which_env']
        debug = i.get('debug', False)

        r = utils.load_txt(file_name = file_name,
                           check_if_exists = True, 
                           split = True,
                           match_text = match_text,
                           fail_if_no_match = 'version was not detected')
        if r['return']>0: 
           if r.get('string','')!='':
              r['error'] += ' ({})'.format(r['string'])
           return r

        string = r['string']

        version = r['match'].group(group_number)

        which_env[env_key] = version
        which_env['CM_DETECTED_VERSION'] = version # to be recorded in the cache meta

        return {'return':0, 'version':version, 'string':string}

    ##############################################################################
    def update_deps(self, i):
        """
        Update deps from pre/post processing
        Args:
          (CM input dict):
          deps (dict): deps dict
          update_deps (dict): key matches "names" in deps
        Returns:
           (CM return dict):
           * return (int): return code == 0 if no error and >0 if error
           * (error) (str): error string if return>0
        """

        deps = i['deps']
        add_deps = i['update_deps']
        update_deps(deps, add_deps, False)

        return {'return':0}

    ##############################################################################
    def get_default_path_list(self, i):
        default_path_env_key = i.get('default_path_env_key', '')
        os_info = i['os_info']
        default_path_list = [] if default_path_env_key == '' else \
        os.environ.get(default_path_env_key,'').split(os_info['env_separator'])

        return default_path_list



    ############################################################
    def doc(self, i):
        """
        Document CM script.

        Args:
          (CM input dict): 

          (out) (str): if 'con', output to console

          parsed_artifact (list): prepared in CM CLI or CM access function
                                    [ (artifact alias, artifact UID) ] or
                                    [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

          (repos) (str): list of repositories to search for automations (internal & mlcommons@ck by default)

          (output_dir) (str): output directory (../docs by default)

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

        """

        return utils.call_internal_module(self, __file__, 'module_misc', 'doc', i)

    ############################################################
    def gui(self, i):
        """
        Run GUI for CM script.

        Args:
          (CM input dict):

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

        """

        artifact = i.get('artifact', '')
        tags = ''
        if artifact != '':
            if ' ' in artifact:
                tags = artifact.replace(' ',',')
             
        if tags=='':
            tags = i.get('tags','')

        if 'tags' in i:
            del(i['tags'])

        i['action']='run'
        i['artifact']='gui'
        i['parsed_artifact']=[('gui','605cac42514a4c69')]
        i['script']=tags.replace(',',' ')

        return self.cmind.access(i)



    ############################################################
    def dockerfile(self, i):
        """
        Generate Dockerfile for CM script.

        Args:
          (CM input dict):

          (out) (str): if 'con', output to console

          parsed_artifact (list): prepared in CM CLI or CM access function
                                    [ (artifact alias, artifact UID) ] or
                                    [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

          (repos) (str): list of repositories to search for automations (internal & mlcommons@ck by default)

          (output_dir) (str): output directory (./ by default)

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

        """

        return utils.call_internal_module(self, __file__, 'module_misc', 'dockerfile', i)

    ############################################################
    def docker(self, i):
        """
        Run CM script in an automatically-generated container.

        Args:
          (CM input dict):

          (out) (str): if 'con', output to console

          parsed_artifact (list): prepared in CM CLI or CM access function
                                    [ (artifact alias, artifact UID) ] or
                                    [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

          (repos) (str): list of repositories to search for automations (internal & mlcommons@ck by default)

          (output_dir) (str): output directory (./ by default)

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

        """

        return utils.call_internal_module(self, __file__, 'module_misc', 'docker', i)


    ##############################################################################
    def _available_variations(self, i):
        """
        return error with available variations

        Args:
          (CM input dict): 

          meta (dict): meta of the script

        Returns:
           (CM return dict):

           * return (int): return code == 0 if no error and >0 if error
                                             16 if not detected
           * (error) (str): error string if return>0

        """

        meta = i['meta']

        list_of_variations = sorted(['_'+v for v in list(meta.get('variations',{}.keys()))])

        return {'return':1, 'error':'python package variation is not defined in "{}". Available: {}'.format(meta['alias'],' '.join(list_of_variations))}

    ############################################################
    def prepare(self, i):
        """
        Run CM script with --fake_run only to resolve deps
        """

        i['fake_run']=True

        return self.run(i)

    ############################################################
    # Reusable blocks for some scripts
    def clean_some_tmp_files(self, i):
        """
        Clean tmp files
        """

        env = i.get('env',{})

        cur_work_dir = env.get('CM_TMP_CURRENT_SCRIPT_WORK_PATH','')
        if cur_work_dir !='' and os.path.isdir(cur_work_dir):
           for x in ['tmp-run.bat', 'tmp-state.json']:
               xx = os.path.join(cur_work_dir, x)
               if os.path.isfile(xx):
                   os.remove(xx)

        return {'return':0}



##############################################################################
def find_cached_script(i):
    """
    Internal automation function: find cached script

    Args:
      (CM input dict):

      deps (dict): deps dict
      update_deps (dict): key matches "names" in deps

    Returns:
       (CM return dict):
       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0
    """

    import copy
    
    recursion_spaces = i['recursion_spaces']
    script_tags = i['script_tags']
    cached_tags = []
    found_script_tags = i['found_script_tags']
    variation_tags = i['variation_tags']
    explicit_variation_tags = i['explicit_variation_tags']
    version = i['version']
    version_min = i['version_min']
    version_max = i['version_max']
    extra_cache_tags = i['extra_cache_tags']
    new_cache_entry = i['new_cache_entry']
    meta = i['meta']
    env = i['env']
    self_obj = i['self']
    skip_remembered_selections = i['skip_remembered_selections']
    remembered_selections = i['remembered_selections']
    quiet = i['quiet']
    search_tags = ''

    verbose = i.get('verbose', False)
    if not verbose: verbose = i.get('v', False)

    found_cached_scripts = []

    if verbose:
        print (recursion_spaces + '  - Checking if script execution is already cached ...')

    # Create a search query to find that we already ran this script with the same or similar input
    # It will be gradually enhanced with more "knowledge"  ...
    if len(script_tags)>0:
        for x in script_tags:
            if x not in cached_tags:
                cached_tags.append(x)

    if len(found_script_tags)>0:
        for x in found_script_tags:
            if x not in cached_tags: 
                cached_tags.append(x)

    explicit_cached_tags=copy.deepcopy(cached_tags)

    if len(explicit_variation_tags)>0:
        explicit_variation_tags_string = ''

        for t in explicit_variation_tags:
            if explicit_variation_tags_string != '': 
                explicit_variation_tags_string += ','
            if t.startswith("-"):
                x = "-_" + t[1:]
            else:
                x = '_' + t
            explicit_variation_tags_string += x

            if x not in explicit_cached_tags: 
                explicit_cached_tags.append(x)

        if verbose:
            print (recursion_spaces+'    - Prepared explicit variations: {}'.format(explicit_variation_tags_string))
    
    if len(variation_tags)>0:
        variation_tags_string = ''

        for t in variation_tags:
            if variation_tags_string != '': 
                variation_tags_string += ','
            if t.startswith("-"):
                x = "-_" + t[1:]
            else:
                x = '_' + t
            variation_tags_string += x

            if x not in cached_tags: 
                cached_tags.append(x)

        if verbose:
            print (recursion_spaces+'    - Prepared variations: {}'.format(variation_tags_string))

    # Add version
    if version !='':
        if 'version-'+version not in cached_tags: 
            cached_tags.append('version-'+version)
            explicit_cached_tags.append('version-'+version)

    # Add extra cache tags (such as "virtual" for python)
    if len(extra_cache_tags)>0:
        for t in extra_cache_tags:
            if t not in cached_tags: 
                cached_tags.append(t)
                explicit_cached_tags.append(t)

    # Add tags from deps (will be also duplicated when creating new cache entry)
    extra_cache_tags_from_env = meta.get('extra_cache_tags_from_env',[])
    for extra_cache_tags in extra_cache_tags_from_env:
        key = extra_cache_tags['env']
        prefix = extra_cache_tags.get('prefix','')

        v = env.get(key,'').strip()
        if v!='':
            for t in v.split(','):
                x = 'deps-' + prefix + t
                if x not in cached_tags: 
                    cached_tags.append(x)
                    explicit_cached_tags.append(x)

    # Check if already cached
    if not new_cache_entry:
        search_tags = '-tmp'
        if len(cached_tags) >0 : 
            search_tags += ',' + ','.join(explicit_cached_tags)

        if verbose:
            print (recursion_spaces+'    - Searching for cached script outputs with the following tags: {}'.format(search_tags))

        r = self_obj.cmind.access({'action':'find',
                                   'automation':self_obj.meta['deps']['cache'],
                                   'tags':search_tags})
        if r['return']>0: return r

        found_cached_scripts = r['list']

        # Check if selection is remembered
        if not skip_remembered_selections and len(found_cached_scripts) > 1:
            # Need to add extra cached tags here (since recorded later)
            for selection in remembered_selections:
                if selection['type'] == 'cache' and set(selection['tags'].split(',')) == set(search_tags.split(',')):
                    tmp_version_in_cached_script = selection['cached_script'].meta.get('version','')

                    skip_cached_script = check_versions(self_obj.cmind, tmp_version_in_cached_script, version_min, version_max)

                    if skip_cached_script:
                        return {'return':2, 'error':'The version of the previously remembered selection for a given script ({}) mismatches the newly requested one'.format(tmp_version_in_cached_script)}
                    else:
                        found_cached_scripts = [selection['cached_script']]
                        if verbose:
                            print (recursion_spaces + '  - Found remembered selection with tags "{}"!'.format(search_tags))
                        break


    if len(found_cached_scripts) > 0:
        selection = 0

        # Check version ranges ...
        new_found_cached_scripts = []

        for cached_script in found_cached_scripts:
            skip_cached_script = False
            dependent_cached_path = cached_script.meta.get('dependent_cached_path', '')
            if dependent_cached_path:
                if not os.path.exists(dependent_cached_path):
                    #Need to rm this cache entry
                    skip_cached_script = True
                    continue

            if not skip_cached_script:
                cached_script_version = cached_script.meta.get('version', '')

                skip_cached_script = check_versions(self_obj.cmind, cached_script_version, version_min, version_max)

            if not skip_cached_script:
                new_found_cached_scripts.append(cached_script)

        found_cached_scripts = new_found_cached_scripts

    return {'return':0, 'cached_tags':cached_tags, 'search_tags':search_tags, 'found_cached_scripts':found_cached_scripts}


##############################################################################
def enable_or_skip_script(meta, env):
    """
    Internal: enable a dependency based on enable_if_env and skip_if_env meta information
    """
    for key in meta:
        if key in env:
            value = str(env[key]).lower()

            meta_key = [str(v).lower() for v in meta[key]]

            if set(meta_key) & set(["yes", "on", "true", "1"]):
                if value not in ["no", "off", "false", "0"]:
                    continue
            elif set(meta_key) & set(["no", "off", "false", "0"]):
                if value in ["no", "off", "false", "0"]:
                    continue
            elif value in meta_key:
                continue
        return False
    return True

############################################################################################################
def update_env_with_values(env, fail_on_not_found=False):
    """
    Update any env key used as part of values in meta
    """
    import re
    for key in env:
        if key.startswith("+") and type(env[key]) != list:
            return {'return': 1, 'error': 'List value expected for {} in env'.format(key)}

        value = env[key]

        # Check cases such as --env.CM_SKIP_COMPILE
        if type(value)==bool:
            env[key] = str(value)
            continue

        tmp_values = re.findall(r'<<<(.*?)>>>', str(value))

        if not tmp_values:
            if key == 'CM_GIT_URL' and env.get('CM_GIT_AUTH', "no") == "yes":
                if 'CM_GH_TOKEN' in env and '@' not in env['CM_GIT_URL']:
                    params = {}
                    params["token"] = env['CM_GH_TOKEN']
                    value = get_git_url("token", value, params)
                elif 'CM_GIT_SSH' in env:
                    value = get_git_url("ssh", value)
                env[key] = value

            continue

        for tmp_value in tmp_values:
            if tmp_value not in env and fail_on_not_found:
                return {'return':1, 'error':'variable {} is not in env'.format(tmp_value)}
            if tmp_value in env:
                value = value.replace("<<<"+tmp_value+">>>", str(env[tmp_value]))

        env[key] = value

    return {'return': 0}


##############################################################################
def check_version_constraints(i):
    """
    Internal: check version constaints and skip script artifact if constraints are not met
    """

    detected_version = i['detected_version']

    version = i.get('version', '')
    version_min = i.get('version_min', '')
    version_max = i.get('version_max', '')

    cmind = i['cmind']

    skip = False

    if version != '' and version != detected_version:
        skip = True

    if not skip and detected_version != '' and version_min != '':
        ry = cmind.access({'action':'compare_versions',
                           'automation':'utils,dc2743f8450541e3',
                           'version1':detected_version,
                           'version2':version_min})
        if ry['return']>0: return ry

        if ry['comparison'] < 0:
            skip = True

    if not skip and detected_version != '' and version_max != '':
        ry = cmind.access({'action':'compare_versions',
                           'automation':'utils,dc2743f8450541e3',
                           'version1':detected_version,
                           'version2':version_max})
        if ry['return']>0: return ry

        if ry['comparison'] > 0:
            skip = True

    return {'return':0, 'skip':skip}


##############################################################################
def prepare_and_run_script_with_postprocessing(i, postprocess="postprocess"):
    """
    Internal: prepare and run script with postprocessing that can be reused for version check
    """

    path = i['path']
    bat_ext = i['bat_ext']
    os_info = i['os_info']
    customize_code = i.get('customize_code', None)
    customize_common_input = i.get('customize_common_input',{})

    env = i.get('env', {})
    const = i.get('const', {})
    state = i.get('state', {})
    const_state = i.get('const_state', {})
    run_state = i.get('run_state', {})
    verbose = i.get('verbose', False)
    if not verbose: verbose = i.get('v', False)

    show_time = i.get('time', False)

    recursion = i.get('recursion', False)
    found_script_tags = i.get('found_script_tags', [])
    debug_script_tags = i.get('debug_script_tags', '')

    meta = i.get('meta',{})

    reuse_cached = i.get('reused_cached', False)
    recursion_spaces = i.get('recursion_spaces', '')

    tmp_file_run_state = i.get('tmp_file_run_state', '')
    tmp_file_run_env = i.get('tmp_file_run_env', '')
    tmp_file_state = i.get('tmp_file_state', '')
    tmp_file_run = i['tmp_file_run']
    local_env_keys = i.get('local_env_keys', [])
    local_env_keys_from_meta = i.get('local_env_keys_from_meta', [])
    posthook_deps = i.get('posthook_deps', [])
    add_deps_recursive = i.get('add_deps_recursive', {})
    recursion_spaces = i['recursion_spaces']
    remembered_selections = i.get('remembered_selections', {})
    variation_tags_string = i.get('variation_tags_string', '')
    found_cached = i.get('found_cached', False)
    script_automation = i['self']

    repro_prefix = i.get('repro_prefix', '')

    # Prepare script name
    check_if_run_script_exists = False
    script_name = i.get('script_name','').strip()
    if script_name == '':
        script_name = meta.get('script_name','').strip()
        if script_name !='':
            # Script name was added by user - we need to check that it really exists (on Linux or Windows)
            check_if_run_script_exists = True
    if script_name == '':
        # Here is the default script name - if it doesn't exist, we skip it. 
        # However, if it's explicitly specified, we check it and report
        # if it's missing ...
        script_name = 'run'

    if bat_ext == '.sh':
        run_script = get_script_name(env, path, script_name)
    else:
        run_script = script_name + bat_ext

    path_to_run_script = os.path.join(path, run_script)

    if check_if_run_script_exists and not os.path.isfile(path_to_run_script):
        return {'return':16, 'error':'script {} not found - please add one'.format(path_to_run_script)}

    # Update env and state with const
    utils.merge_dicts({'dict1':env, 'dict2':const, 'append_lists':True, 'append_unique':True})
    utils.merge_dicts({'dict1':state, 'dict2':const_state, 'append_lists':True, 'append_unique':True})

    # Update env with the current path
    if os_info['platform'] == 'windows' and ' ' in path:
        path = '"' + path + '"'

    cur_dir = os.getcwd()
    
    env['CM_TMP_CURRENT_SCRIPT_PATH'] = path
    env['CM_TMP_CURRENT_SCRIPT_WORK_PATH'] = cur_dir

    # Record state
    if tmp_file_state != '':
        r = utils.save_json(file_name = tmp_file_state, meta = state)
        if r['return']>0: return r

    rr = {'return':0}

    # If batch file exists, run it with current env and state
    if os.path.isfile(path_to_run_script) and not reuse_cached:
        if tmp_file_run_state != '' and os.path.isfile(tmp_file_run_state):
            os.remove(tmp_file_run_state)
        if tmp_file_run_env != '' and os.path.isfile(tmp_file_run_env):
            os.remove(tmp_file_run_env)

        run_script = tmp_file_run + bat_ext

        if verbose:
            print ('')
            print (recursion_spaces + '  - Running native script "{}" from temporal script "{}" in "{}" ...'.format(path_to_run_script, run_script, cur_dir))
            print ('')

        print (recursion_spaces + '       ! cd {}'.format(cur_dir))
        print (recursion_spaces + '       ! call {} from {}'.format(path_to_run_script, run_script))


        # Prepare env variables
        import copy
        script = copy.deepcopy(os_info['start_script'])

        # Check if script_prefix in the state from other components
        script_prefix = state.get('script_prefix',[])
        if len(script_prefix)>0:
#            script = script_prefix + ['\n'] + script
            script += script_prefix + ['\n']

        script += convert_env_to_script(env, os_info)

        # Check if run bash/cmd before running the command (for debugging)
        if debug_script_tags !='' and all(item in found_script_tags for item in debug_script_tags.split(',')):
            x=['cmd', '.', '','.bat'] if os_info['platform'] == 'windows' else ['bash', ' ""', '"','.sh']

            script.append('\n')
            script.append('echo{}\n'.format(x[1]))
            script.append('echo {}Running debug shell. Type exit to resume script execution ...{}\n'.format(x[2],x[3],x[2]))
            script.append('echo{}\n'.format(x[1]))
            script.append('\n')
            script.append(x[0])

        # Append batch file to the tmp script
        script.append('\n')
        script.append(os_info['run_bat'].replace('${bat_file}', '"'+path_to_run_script+'"') + '\n')

        # Prepare and run script
        r = record_script(run_script, script, os_info)
        if r['return']>0: return r

        # Run final command
        cmd = os_info['run_local_bat_from_python'].replace('${bat_file}', run_script)

        rc = os.system(cmd)

        if rc>0 and not i.get('ignore_script_error', False):
            # Check if print files when error
            print_files = meta.get('print_files_if_script_error', [])
            if len(print_files)>0:
               for pr in print_files:
                   if os.path.isfile(pr):
                       r = utils.load_txt(file_name = pr)
                       if r['return'] == 0:
                           print ("========================================================")
                           print ("Print file {}:".format(pr))
                           print ("")
                           print (r['string'])
                           print ("")

            note = '''
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Note that it may be a portability issue of a third-party tool or a native script 
wrapped and unified by this automation recipe (CM script). In such case, 
please report this issue with a full log at "https://github.com/mlcommons/ck". 
The CM concept is to collaboratively fix such issues inside portable CM scripts 
to make existing tools and native scripts more portable, interoperable 
and deterministic. Thank you'''

            rr = {'return':2, 'error':'Portable CM script failed (name = {}, return code = {})\n\n{}'.format(meta['alias'], rc, note)}

            if repro_prefix != '':
                dump_repro(repro_prefix, rr, run_state)
            
            return rr

        # Load updated state if exists
        if tmp_file_run_state != '' and os.path.isfile(tmp_file_run_state):
            r = utils.load_json(file_name = tmp_file_run_state)
            if r['return']>0: return r

            updated_state = r['meta']

            utils.merge_dicts({'dict1':state, 'dict2':updated_state, 'append_lists':True, 'append_unique':True})

        # Load updated env if exists
        if tmp_file_run_env != '' and os.path.isfile(tmp_file_run_env):
            r = utils.load_txt(file_name = tmp_file_run_env)
            if r['return']>0: return r

            r = utils.convert_env_to_dict(r['string'])
            if r['return']>0: return r

            updated_env = r['dict']

            utils.merge_dicts({'dict1':env, 'dict2':updated_env, 'append_lists':True, 'append_unique':True})
 

    if postprocess != '' and customize_code is not None:
        print (recursion_spaces+'       ! call "{}" from {}'.format(postprocess, customize_code.__file__))
    
    if len(posthook_deps)>0 and (postprocess == "postprocess"):
        r = script_automation._call_run_deps(posthook_deps, local_env_keys, local_env_keys_from_meta, env, state, const, const_state,
            add_deps_recursive, recursion_spaces, remembered_selections, variation_tags_string, found_cached, debug_script_tags, verbose, show_time, ' ', run_state)
        if r['return']>0: return r

    if (postprocess == "postprocess") and customize_code is not None and 'postprocess' in dir(customize_code):
        rr = run_postprocess(customize_code, customize_common_input, recursion_spaces, env, state, const,
                const_state, meta, verbose, i) # i as run_script_input
    elif (postprocess == "detect_version") and customize_code is not None and 'detect_version' in dir(customize_code):
        rr = run_detect_version(customize_code, customize_common_input, recursion_spaces, env, state, const,
                const_state, meta, verbose)

    return rr

##############################################################################
def run_detect_version(customize_code, customize_common_input, recursion_spaces, env, state, const, const_state, meta, verbose=False):

    if customize_code is not None and 'detect_version' in dir(customize_code):
        import copy

        if verbose:
            print (recursion_spaces+'  - Running detect_version ...')

        # Update env and state with const
        utils.merge_dicts({'dict1':env, 'dict2':const, 'append_lists':True, 'append_unique':True})
        utils.merge_dicts({'dict1':state, 'dict2':const_state, 'append_lists':True, 'append_unique':True})

        ii = copy.deepcopy(customize_common_input)
        ii['env'] = env
        ii['state'] = state
        ii['meta'] = meta

        r = customize_code.detect_version(ii)
        return r

    return {'return': 0}

##############################################################################
def run_postprocess(customize_code, customize_common_input, recursion_spaces, env, state, const, const_state, meta, verbose=False, run_script_input=None):

    if customize_code is not None and 'postprocess' in dir(customize_code):
        import copy

        if verbose:
            print (recursion_spaces+'  - Running postprocess ...')

        # Update env and state with const
        utils.merge_dicts({'dict1':env, 'dict2':const, 'append_lists':True, 'append_unique':True})
        utils.merge_dicts({'dict1':state, 'dict2':const_state, 'append_lists':True, 'append_unique':True})

        ii = copy.deepcopy(customize_common_input)
        ii['env'] = env
        ii['state'] = state
        ii['meta'] = meta

        if run_script_input != None:
            ii['run_script_input'] = run_script_input 

        r = customize_code.postprocess(ii)
        return r

    return {'return': 0}

##############################################################################
def get_script_name(env, path, script_name = 'run'):
    """
    Internal: find the most appropriate run script name for the detected OS
    """

    from os.path import exists

    tmp_suff1 = env.get('CM_HOST_OS_FLAVOR', '')
    tmp_suff2 = env.get('CM_HOST_OS_VERSION', '')
    tmp_suff3 = env.get('CM_HOST_PLATFORM_FLAVOR', '')

    if exists(os.path.join(path, script_name+'-' + tmp_suff1 + '-'+ tmp_suff2 + '-' + tmp_suff3 + '.sh')):
        return script_name+'-' + tmp_suff1 + '-' + tmp_suff2 + '-' + tmp_suff3 + '.sh'
    elif exists(os.path.join(path, script_name+'-' + tmp_suff1 + '-' + tmp_suff3 + '.sh')):
        return script_name+'-' + tmp_suff1 + '-' + tmp_suff3 + '.sh'
    elif exists(os.path.join(path, script_name+'-' + tmp_suff1 + '-' + tmp_suff2 + '.sh')):
        return script_name+'-' + tmp_suff1 + '-' + tmp_suff2 + '.sh'
    elif exists(os.path.join(path, script_name+'-' + tmp_suff1 + '.sh')):
        return script_name+'-' + tmp_suff1 + '.sh'
    elif exists(os.path.join(path, script_name+'-' + tmp_suff3 + '.sh')):
        return script_name+'-' + tmp_suff3 + '.sh'
    else:
        return script_name+'.sh';

##############################################################################
def update_env_keys(env, env_key_mappings):
    """
    Internal: convert env keys as per the given mapping
    """

    for key_prefix in env_key_mappings:
        for key in list(env):
            if key.startswith(key_prefix):
                new_key = key.replace(key_prefix, env_key_mappings[key_prefix])
                env[new_key] = env[key]
                #del(env[key])

##############################################################################
def convert_env_to_script(env, os_info, start_script = []):
    """
    Internal: convert env to script for a given platform
    """

    import copy
    script = copy.deepcopy(start_script)

    windows = True if os_info['platform'] == 'windows' else False

    for k in sorted(env):
        env_value = env[k]

        if windows:
            x = env_value
            if type(env_value)!=list:
                x = [x]

            xx = []
            for v in x:
                # If " is already in env value, it means that there was some custom processing to consider special characters

                y=str(v)

                if '"' not in y:
                    for z in ['|', '&', '>', '<']:
                        if z in y:
                            y = '"'+y+'"'
                            break
                xx.append(y)

            env_value = xx if type(env_value)==list else xx[0]

        # Process special env 
        key = k

        if k.startswith('+'):
            # List and append the same key at the end (+PATH, +LD_LIBRARY_PATH, +PYTHONPATH)
            key=k[1:]
            first = key[0]
            env_separator = os_info['env_separator']
            # If key starts with a symbol use it as the list separator (+ CFLAG will use ' ' the 
            # list separator while +;TEMP will use ';' as the separator)
            if not first.isalnum():
                env_separator = first
                key=key[1:]

            env_value = env_separator.join(env_value) + \
                env_separator + \
                os_info['env_var'].replace('env_var', key)

        v = os_info['set_env'].replace('${key}', key).replace('${value}', str(env_value))

        script.append(v)

    return script

##############################################################################
def record_script(run_script, script, os_info):
    """
    Internal: record script and chmod 755 on Linux
    """

    final_script = '\n'.join(script)

    if not final_script.endswith('\n'):
        final_script += '\n'

    r = utils.save_txt(file_name=run_script, string=final_script)
    if r['return']>0: return r

    if os_info.get('set_exec_file','')!='':
        cmd = os_info['set_exec_file'].replace('${file_name}', run_script)
        rc = os.system(cmd)

    return {'return':0}

##############################################################################
def clean_tmp_files(clean_files, recursion_spaces):
    """
    Internal: clean tmp files
    """

#    print ('')
#    print (recursion_spaces+'  - cleaning files {} ...'.format(clean_files))

    for tmp_file in clean_files:
        if os.path.isfile(tmp_file):
            os.remove(tmp_file)

    return {'return':0}

##############################################################################
def update_dep_info(dep, new_info):
    """
    Internal: add additional info to a dependency
    """
    for info in new_info:
        if info == "tags":
            tags = dep.get('tags', '')
            tags_list = tags.split(",")
            new_tags_list = new_info["tags"].split(",")
            combined_tags = tags_list + list(set(new_tags_list) - set(tags_list))
            dep['tags'] = ",".join(combined_tags)
        else:
            dep[info] = new_info[info]

##############################################################################
def update_deps(deps, add_deps, fail_error=False):
    """
    Internal: add deps tags, version etc. by name
    """
    #deps_info_to_add = [ "version", "version_min", "version_max", "version_max_usable", "path" ]
    new_deps_info = {}
    for new_deps_name in add_deps:
        dep_found = False
        for dep in deps:
            names = dep.get('names',[])
            if new_deps_name in names:
                update_dep_info(dep, add_deps[new_deps_name])
                dep_found = True
        if not dep_found and fail_error:
            return {'return':1, 'error':new_deps_name + ' is not one of the dependency'}

    return {'return':0}


##############################################################################
def append_deps(deps, new_deps):
    """
    Internal: add deps from meta
    """

    for new_dep in new_deps:
        existing = False
        new_dep_names = new_dep.get('names',[])
        if len(new_dep_names)>0:
            for i in range(len(deps)):
                dep = deps[i]
                dep_names = dep.get('names',[])
                if len(dep_names)>0:
                    if set(new_dep_names) == set(dep_names):
                        deps[i] = new_dep
                        existing = True
                        break
        else: #when no name, check for tags
            new_dep_tags = new_dep.get('tags')
            new_dep_tags_list = new_dep_tags.split(",")
            for i in range(len(deps)):
                dep = deps[i]
                dep_tags_list = dep.get('tags').split(",")
                if set(new_dep_tags_list) == set (dep_tags_list):
                    deps[i] = new_dep
                    existing = True
                    break

        if not existing:
            deps.append(new_dep)

    return {'return':0}

##############################################################################
def update_deps_from_input(deps, post_deps, prehook_deps, posthook_deps, i):
    """
    Internal: update deps from meta
    """
    add_deps_info_from_input = i.get('ad',{})
    if not add_deps_info_from_input:
        add_deps_info_from_input = i.get('add_deps',{})
    else:
        utils.merge_dicts({'dict1':add_deps_info_from_input, 'dict2':i.get('add_deps', {}), 'append_lists':True, 'append_unique':True})

    add_deps_recursive_info_from_input = i.get('adr', {})
    if not add_deps_recursive_info_from_input:
        add_deps_recursive_info_from_input = i.get('add_deps_recursive', {})
    else:
        utils.merge_dicts({'dict1':add_deps_recursive_info_from_input, 'dict2':i.get('add_deps_recursive', {}), 'append_lists':True, 'append_unique':True})

    if add_deps_info_from_input:
        r1 = update_deps(deps, add_deps_info_from_input, True)
        r2 = update_deps(post_deps, add_deps_info_from_input, True)
        r3 = update_deps(prehook_deps, add_deps_info_from_input, True)
        r4 = update_deps(posthook_deps, add_deps_info_from_input, True)
        if r1['return']>0 and r2['return']>0 and r3['return']>0 and r4['return']>0: return r1
    if add_deps_recursive_info_from_input:
        update_deps(deps, add_deps_recursive_info_from_input)
        update_deps(post_deps, add_deps_recursive_info_from_input)
        update_deps(prehook_deps, add_deps_recursive_info_from_input)
        update_deps(posthook_deps, add_deps_recursive_info_from_input)

    return {'return':0}


##############################################################################
def update_env_from_input_mapping(env, inp, input_mapping):
    """
    Internal: update env from input and input_mapping
    """
    for key in input_mapping:
        if key in inp:
            env[input_mapping[key]] = inp[key]

##############################################################################
def update_state_from_meta(meta, env, state, deps, post_deps, prehook_deps, posthook_deps, new_env_keys, new_state_keys, i):
    """
    Internal: update env and state from meta
    """

    default_env = meta.get('default_env',{})
    for key in default_env:
        env.setdefault(key, default_env[key])
    update_env = meta.get('env', {})
    env.update(update_env)

    update_state = meta.get('state', {})
    utils.merge_dicts({'dict1':state, 'dict2':update_state, 'append_lists':True, 'append_unique':True})

    new_deps = meta.get('deps', [])
    if len(new_deps)>0:
        append_deps(deps, new_deps)

    new_post_deps = meta.get("post_deps", [])
    if len(new_post_deps) > 0:
        append_deps(post_deps, new_post_deps)

    new_prehook_deps = meta.get("prehook_deps", [])
    if len(new_prehook_deps) > 0:
        append_deps(prehook_deps, new_prehook_deps)

    new_posthook_deps = meta.get("posthook_deps", [])
    if len(new_posthook_deps) > 0:
        append_deps(posthook_deps, new_posthook_deps)

    add_deps_info = meta.get('ad', {})
    if not add_deps_info:
        add_deps_info = meta.get('add_deps',{})
    else:
        utils.merge_dicts({'dict1':add_deps_info, 'dict2':meta.get('add_deps', {}), 'append_lists':True, 'append_unique':True})
    if add_deps_info:
        r1 = update_deps(deps, add_deps_info, True)
        r2 = update_deps(post_deps, add_deps_info, True)
        r3 = update_deps(prehook_deps, add_deps_info, True)
        r4 = update_deps(posthook_deps, add_deps_info, True)
        if r1['return']>0 and r2['return']>0 and r3['return'] > 0 and r4['return'] > 0: return r1

    input_mapping = meta.get('input_mapping', {})
    if input_mapping:
        update_env_from_input_mapping(env, i['input'], input_mapping)

    # Possibly restrict this to within docker environment
    new_docker_settings = meta.get('docker')
    if new_docker_settings:
        docker_settings = state.get('docker', {})
        #docker_input_mapping = docker_settings.get('docker_input_mapping', {})
        #new_docker_input_mapping = new_docker_settings.get('docker_input_mapping', {})
        #if new_docker_input_mapping:
        #    #    update_env_from_input_mapping(env, i['input'], docker_input_mapping)
        #    utils.merge_dicts({'dict1':docker_input_mapping, 'dict2':new_docker_input_mapping, 'append_lists':True, 'append_unique':True})
        utils.merge_dicts({'dict1':docker_settings, 'dict2':new_docker_settings, 'append_lists':True, 'append_unique':True})
        state['docker'] = docker_settings

    new_env_keys_from_meta = meta.get('new_env_keys', [])
    if new_env_keys_from_meta:
        new_env_keys += new_env_keys_from_meta

    new_state_keys_from_meta = meta.get('new_state_keys', [])
    if new_state_keys_from_meta:
        new_state_keys += new_state_keys_from_meta

    return {'return':0}

##############################################################################
def update_adr_from_meta(deps, post_deps, prehook_deps, posthook_deps, add_deps_recursive_info):
    """
    Internal: update add_deps_recursive from meta
    """
    if add_deps_recursive_info:
        update_deps(deps, add_deps_recursive_info)
        update_deps(post_deps, add_deps_recursive_info)
        update_deps(prehook_deps, add_deps_recursive_info)
        update_deps(posthook_deps, add_deps_recursive_info)

    return {'return':0}

##############################################################################
def get_adr(meta):
    add_deps_recursive_info = meta.get('adr', {})
    if not add_deps_recursive_info:
        add_deps_recursive_info = meta.get('add_deps_recursive',{})
    else:
        utils.merge_dicts({'dict1':add_deps_recursive_info, 'dict2':meta.get('add_deps_recursive', {}), 'append_lists':True, 'append_unique':True})
    return add_deps_recursive_info

##############################################################################
def detect_state_diff(env, saved_env, new_env_keys, new_state_keys, state, saved_state):
    """
    Internal: detect diff in env and state
    """

    new_env = {}
    new_state = {}

    # Check if leave only specific keys or detect diff automatically
    for k in new_env_keys:
        if '?' in k or '*' in k:
            import fnmatch
            for kk in env:
                if fnmatch.fnmatch(kk, k):
                    new_env[kk] = env[kk]
        elif k in env:
            new_env[k] = env[k]
        elif "<<<" in k:
            import re
            tmp_values = re.findall(r'<<<(.*?)>>>', k)
            for tmp_value in tmp_values:
                if tmp_value in env:
                    value = env[tmp_value]
                    if value in env:
                        new_env[value] = env[value]

    for k in new_state_keys:
        if '?' in k or '*' in k:
            import fnmatch
            for kk in state:
                if fnmatch.fnmatch(kk, k):
                    new_state[kk] = state[kk]
        elif k in state:
            new_state[k] = state[k]
        elif "<<<" in k:
            import re
            tmp_values = re.findall(r'<<<(.*?)>>>', k)
            for tmp_value in tmp_values:
                if tmp_value in state:
                    value = state[tmp_value]
                    if value in state:
                        new_state[value] = state[value]

    return {'return':0, 'env':env, 'new_env':new_env, 'state':state, 'new_state':new_state}

##############################################################################
def select_script_artifact(lst, text, recursion_spaces, can_skip, script_tags_string, quiet, verbose):
    """
    Internal: select script
    """

    string1 = recursion_spaces+'    - More than 1 {} found for "{}":'.format(text,script_tags_string)

    # If quiet, select 0 (can be sorted for determinism)
    if quiet:
        if verbose:
            print (string1)
            print ('')
            print ('Selected default due to "quiet" mode')

        return 0

    # Select 1 and proceed
    print (string1)

    print ('')
    num = 0

    for a in lst:
        meta = a.meta

        name = meta.get('name', '')

        s = a.path
        if name !='': s = '"'+name+'" '+s

        x = recursion_spaces+'      {}) {} ({})'.format(num, s, ','.join(meta['tags']))

        version = meta.get('version','')
        if version!='':
            x+=' (Version {})'.format(version)

        print (x)
        num+=1

    print ('')

    s = 'Make your selection or press Enter for 0'
    if can_skip:
        s += ' or use -1 to skip'

    x = input(recursion_spaces+'      '+s+': ')
    x = x.strip()
    if x == '': x = '0'

    selection = int(x)

    if selection <0 and not can_skip:
        selection = 0

    if selection <0:

        print ('')
        print (recursion_spaces+'      Skipped')
    else:
        if selection >= num:
            selection = 0

        print ('')
        print (recursion_spaces+'      Selected {}: {}'.format(selection, lst[selection].path))

    return selection

##############################################################################
def check_versions(cmind, cached_script_version, version_min, version_max):
    """
    Internal: check versions of the cached script
    """
    skip_cached_script = False

    if cached_script_version != '':
        if version_min != '':
            ry = cmind.access({'action':'compare_versions',
                                    'automation':'utils,dc2743f8450541e3',
                                    'version1':cached_script_version,
                                    'version2':version_min})
            if ry['return']>0: return ry

            if ry['comparison'] < 0:
                skip_cached_script = True

        if not skip_cached_script and version_max != '':
            ry = cmind.access({'action':'compare_versions',
                               'automation':'utils,dc2743f8450541e3',
                               'version1':cached_script_version,
                               'version2':version_max})
            if ry['return']>0: return ry

            if ry['comparison'] > 0:
                skip_cached_script = True

    return skip_cached_script

##############################################################################
def get_git_url(get_type, url, params = {}):
    from giturlparse import parse
    p = parse(url)
    if get_type == "ssh":
        return p.url2ssh
    elif get_type == "token":
        token = params['token']
        return "https://git:" + token + "@" + p.host + "/" + p.owner + "/" + p.repo
    return url

##############################################################################
def can_write_to_current_directory():

    import tempfile

    cur_dir = os.getcwd()

#    try:
#        tmp_file = tempfile.NamedTemporaryFile(dir = cur_dir)
#    except Exception as e:
#        return False

    tmp_file_name = next(tempfile._get_candidate_names())+'.tmp'

    tmp_path = os.path.join(cur_dir, tmp_file_name)

    try:
        tmp_file = open(tmp_file_name, 'w')
    except Exception as e:
        return False

    tmp_file.close()

    os.remove(tmp_file_name)

    return True

######################################################################################
def dump_repro_start(repro_prefix, ii):
    import json

    # Clean reproducibility and experiment files
    for f in ['cm-output.json', 'version_info.json', '-input.json', '-info.json', '-output.json', '-run-state.json']:
        ff = repro_prefix+f if f.startswith('-') else f
        if os.path.isfile(ff):
            try:
                os.remove(ff)
            except:
                pass

    try:
        with open(repro_prefix+'-input.json', 'w', encoding='utf-8') as f:
            json.dump(ii, f, ensure_ascii=False, indent=2)
    except:
        pass

    # Get some info
    info = {}

    try:
        import platform
        import sys

        info['host_os_name'] = os.name
        info['host_system'] = platform.system()
        info['host_os_release'] = platform.release()
        info['host_machine'] = platform.machine()
        info['host_architecture'] = platform.architecture()
        info['host_python_version'] = platform.python_version()
        info['host_sys_version'] = sys.version

        r = utils.gen_uid()
        if r['return']==0:
            info['run_uid'] = r['uid']

        r = utils.get_current_date_time({})
        if r['return']==0: 
            info['run_iso_datetime'] = r['iso_datetime']

        with open(repro_prefix+'-info.json', 'w', encoding='utf-8') as f:
            json.dump(info, f, ensure_ascii=False, indent=2)
    except:
        pass


    # For experiment
    cm_output = {}

    cm_output['tmp_test_value']=10.0

    cm_output['info']=info
    cm_output['input']=ii

    try:
        with open('cm-output.json', 'w', encoding='utf-8') as f:
            json.dump(cm_output, f, ensure_ascii=False, indent=2)
    except:
        pass

    return {'return': 0}

######################################################################################
def dump_repro(repro_prefix, rr, run_state):
    import json
    import copy

    try:
        with open(repro_prefix+'-output.json', 'w', encoding='utf-8') as f:
            json.dump(rr, f, ensure_ascii=False, indent=2)
    except:
        pass

    try:
        with open(repro_prefix+'-run-state.json', 'w', encoding='utf-8') as f:
            json.dump(run_state, f, ensure_ascii=False, indent=2)
    except:
        pass

    # For experiment
    cm_output = {}

    # Attempt to read
    try:
        r =  utils.load_json('cm-output.json')
        if r['return']==0:
            cm_output = r['meta']
    except:
        pass

    cm_output['output'] = rr
    cm_output['state'] = copy.deepcopy(run_state)

    # Try to load version_info.json
    version_info = {}

    version_info_orig = {}

    if 'version_info' in cm_output['state']:
        version_info_orig = cm_output['state']['version_info']
        del(cm_output['state']['version_info'])

    try:
        r =  utils.load_json('version_info.json')
        if r['return']==0:
            version_info_orig += r['meta']

            for v in version_info_orig:
                for key in v:
                    dep = v[key]
                    version_info[key] = dep

    except:
        pass

    if len(version_info)>0:
        cm_output['version_info'] = version_info

    if rr['return'] == 0:
        cm_output['acm_ctuning_repro_badge_available'] = True
        cm_output['acm_ctuning_repro_badge_functional'] = True

    try:
        with open('cm-output.json', 'w', encoding='utf-8') as f:
            json.dump(cm_output, f, ensure_ascii=False, indent=2, sort_keys=True)
    except:
        pass


    return {'return': 0}


##############################################################################
# Demo to show how to use CM components independently if needed
if __name__ == "__main__":
    import cmind
    auto = CAutomation(cmind, __file__)

    r=auto.test({'x':'y'})

    print (r)
