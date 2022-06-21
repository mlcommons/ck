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

        self.file_with_cached_state = 'cm-cached-state.json'

        self.tmp_file_env = 'tmp-env'
        self.tmp_file_env_all = 'tmp-env-all'
        self.tmp_file_run = 'tmp-run'
        self.tmp_file_state = 'tmp-state.json'

        self.tmp_file_run_state = 'tmp-run-state.json'
        self.tmp_file_run_env = 'tmp-run-env.out'
        self.tmp_file_ver = 'tmp-ver.out'

        self.__version__ = "0.5.0"

        self.local_env_keys = ['CM_NEED_VERSION', 'CM_NEED_VERSION_MIN', 'CM_NEED_VERSION_MAX']

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
    def test(self, i):
        """
        Test automation

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
        print (json.dumps(i, indent=2))

        return {'return':0}

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

          (add_deps_tags) (dict): {"name":"tag(s)"}

          (version) (str): version to be added to env.CM_NEED_VERSION to specialize this flow
          (take_version_from_env) (bool): use version from env.CM_NEED_VERSION

          (version_min) (str): min version to be added to env.CM_NEED_VERSION_MIN to specialize this flow
          (version_max) (str): max version to be added to env.CM_NEED_VERSION_MAX to specialize this flo

          (path) (str): list of paths to be added to env.CM_TMP_PATH to specialize this flow

          (quiet) (bool): if True, set env.CM_TMP_QUIET to "yes" and attempt to skip questions
                          (the developers have to support it in pre/post processing and scripts)

          (skip_cache) (bool): if True, skip caching and run in current directory

          (new) (bool): if True, skip search for cached and run again

          (dirty) (bool): if True, do not clean files

          (save_state) (bool): if True, save env and state to tmp-env.sh/bat and tmp-state.json

          (recursion) (bool): True if recursive call.
                              Useful when preparing the global bat file or Docker container
                              to save/run it in the end.

          (recursion_spaces) (str, internal): adding '  ' during recursion for debugging


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

        from cmind import utils
        import copy

        recursion_spaces = i.get('recursion_spaces','')
        recursion = i.get('recursion', False)

        # Get current env and state before running this script and sub-scripts
        env = i.get('env',{})
        state = i.get('state',{})

        # Save current env and state to detect new env and state after this script
        saved_env = copy.deepcopy(env)
        saved_state = copy.deepcopy(state)

        save_state = i.get('save_state', False)

        # Get constant env and state
        const = i.get('const',{})
        const_state = i.get('const_state',{})

        # Force current path
        current_path = os.path.abspath(os.getcwd())
        env['CM_TMP_CURRENT_PATH'] = current_path

        # Check if quiet
        quiet = i.get('quiet', False) if 'quiet' in i else (env.get('CM_TMP_QUIET','') == 'yes')
        if quiet: env['CM_TMP_QUIET'] = 'yes'

        # Prepare debug info
        parsed_artifact = i.get('parsed_artifact')
        parsed_artifact_alias = parsed_artifact[0][0] if parsed_artifact is not None else ''

        # Get and cache minimal host OS info to be able to run scripts and manage OS environment
        if len(self.os_info) == 0:
            r = self.cmind.access({'action':'get_host_os_info',
                                   'automation':'utils,dc2743f8450541e3'})
            if r['return']>0: return r

            os_info = r['info']
        else:
            os_info = self.os_info

        # Bat extension for this host OS
        bat_ext = os_info['bat_ext']

        # Extract variations from the input
        tags = i.get('tags','').strip().split(',')

        artifact_tags = []
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
                    artifact_tags.append(t)

        # Find artifact (use only artifact tags without variations)
        ii = utils.sub_input(i, self.cmind.cfg['artifact_keys'])

        artifact_tags_string = ','.join(artifact_tags)

        ii['tags'] = artifact_tags_string

        cm_script_info = 'collective script(s)'

        if parsed_artifact_alias !='' :
            cm_script_info += ' "{}"'.format(parsed_artifact_alias)

        if len(artifact_tags)>0:
            cm_script_info += ' with tags without variation "{}"'.format(artifact_tags_string)

        print ('')
        print (recursion_spaces + '* Searching for ' + cm_script_info)

        r = self.find(ii)
        if r['return']>0: return r

        artifact = r['list'][0]

        meta = artifact.meta
        path = artifact.path

        found_artifact = utils.assemble_cm_object(meta['alias'],meta['uid'])

        print (recursion_spaces+'  - Found script::{} in {}'.format(found_artifact, path))

        # Check version from env (priority if passed from another script) or input (version)
        # Version is local for a given script and is not passed further
        # not to influence versions of dependencies
        if 'CM_NEED_VERSION' in env: 
            version = env['CM_NEED_VERSION']
        else:
            version = i.get('version','').strip()
            if version !='': env['CM_NEED_VERSION'] = version

        if 'CM_NEED_VERSION_MIN' in env: 
            version_min = env['CM_NEED_VERSION_MIN']
        else:
            version_min = i.get('version_min','').strip()
            if version_min !='': env['CM_NEED_VERSION_MIN'] = version_min

        if 'CM_NEED_VERSION_MAX' in env: 
            version_max = env['CM_NEED_VERSION_MAX']
        else:
            version_max = i.get('version_max','').strip()
            if version_max !='': env['CM_NEED_VERSION_MAX'] = version_max

        # Check input/output/paths
        for key in ['path', 'input', 'output']:
            value = i.get(key, '').strip()
            if value != '':
                env['CM_' + key.upper()] = value

        # Prepare files to be cleaned
        clean_files = meta.get('clean_files', []) + \
                      [self.tmp_file_run_state, 
                       self.tmp_file_run_env, 
                       self.tmp_file_ver,
                       self.tmp_file_env + bat_ext,
                       self.tmp_file_env_all + bat_ext,
                       self.tmp_file_state,
                       self.tmp_file_run + bat_ext]

        # Check if needs to be cached
        # In such case, need to check if already cached
        cache = meta.get('cache', False)
        if i.get('skip_cache', False): 
            cache = False

        cached_artifact_uid = ''

        remove_tmp_tag = False
        reuse_cached = False

        variations = artifact.meta.get('variations', {})
        versions = artifact.meta.get('versions', {})

        found_cached = False

        if cache:
            print (recursion_spaces + '  - Checking if already cached ...')

            # Create a search query to find that we already ran this components with the same or similar input
            # It will be gradually enhanced with more "knowledge"  ...

            # For simplicity, we use tags for the search in "cached" components
            # TBD: we will need to add variations/versions later
            cached_tags = 'script-artifact-' + meta['uid']

            # Add all tags from the original CM script
            if len(meta.get('tags', []))>0:
                cached_tags += ',' + ','.join(meta['tags'])

            # Add variation(s) if specified in the "tags" input prefixed by _
              # If there is only 1 default variation, then just use it or substitute from CMD

            default_variation = meta.get('default_variation', '')
            default_variations = meta.get('default_variations', [])  

            if len(variation_tags) == 0:
                if default_variation != '':
                    variation_tags = [default_variation]
                elif len(default_variations)>0:
                    variation_tags = default_variations

            else:
                if len(default_variations)>0:
                    tmp_variation_tags = copy.deepcopy(default_variations)

                    for t in variation_tags:
                        if t.startswith('-'):
                            t = t[1:]
                            if t in tmp_variation_tags:
                                del(tmp_variation_tags)
                            else:
                                return {'return':1, 'error':'tag {} is not in default tags {}'.format(t, tmp_variation_tags)}
                        else:
                            if t not in default_variations:
                                tmp_variation_tags.append(t)

                    variation_tags = tmp_variation_tags

            # Add the ones that are not on!
            if len(default_variations)>0:
                for t in variations:
                    if t not in variation_tags:
                        variation_tags.append('~' + t)

            if len(variation_tags)>0:
                variation_tags_string = ''

                for t in variation_tags:
                    if variation_tags_string != '': 
                        variation_tags_string += ','

                    variation_tags_string += '_'+t

                print (recursion_spaces+'    Prepared variations: {}'.format(variation_tags_string))

                cached_tags += ',' + variation_tags_string

            # Add version
            if version!='':
                cached_tags += ',version-' + version

            # Check if already cached
            if i.get('new', False):
                search_tags = 'tmp,' + cached_tags
            else:
                search_tags = '-tmp,' + cached_tags

            print (recursion_spaces+'    - Tags: {}'.format(search_tags))

            r = self.cmind.access({'action':'find',
                                   'automation':self.meta['deps']['cache'],
                                   'tags':search_tags})
            if r['return']>0: return r

            found_cached_artifacts = r['list']

            num_found_cached_artifacts = len(found_cached_artifacts)

            cached_path = ''

            if num_found_cached_artifacts > 0:
                selection = 0

                if num_found_cached_artifacts > 1:
                    # Select 1 and proceed
                    print (recursion_spaces+'  - More than 1 cached script output found:')

                    print ('')
                    num = 0

                    for a in r['list']:
                        print (recursion_spaces+'    {}) {} ({})'.format(num, a.path, ','.join(a.meta['tags'])))
                        num+=1

                    print ('')
                    x=input(recursion_spaces+'    Select one or press Enter for 0: ')

                    x=x.strip()
                    if x=='': x='0'

                    selection = int(x)

                    if selection < 0 or selection >= num:
                        selection = 0

                    print ('')
                    print (recursion_spaces+'    Selected {}: {}'.format(selection, found_cached_artifacts[selection].path))

                else:
                    print (recursion_spaces+'  - Found cached script output: {}'.format(found_cached_artifacts[0].path))

                # Continue with the selected cached artifact
                cached_artifact = r['list'][selection]

                print (recursion_spaces+'  - Loading "cached" state ...')

                path_to_cached_state_file = os.path.join(cached_artifact.path,
                    self.file_with_cached_state)

                r =  utils.load_json(file_name = path_to_cached_state_file)
                if r['return']>0: return r

                # Update env and state from cache!
                cached_state = r['meta']

                new_env = cached_state['new_env']
                utils.merge_dicts({'dict1':env, 'dict2':new_env, 'append_lists':True, 'append_unique':True})

                new_state = cached_state['new_state']
                utils.merge_dicts({'dict1':state, 'dict2':new_state, 'append_lists':True, 'append_unique':True})

                utils.merge_dicts({'dict1':new_env, 'dict2':const, 'append_lists':True, 'append_unique':True})
                utils.merge_dicts({'dict1':new_state, 'dict2':const_state, 'append_lists':True, 'append_unique':True})

                found_cached = True

            if not found_cached and num_found_cached_artifacts == 0:
                # If not cached, create cached artifact and mark as tmp (remove if cache successful)
                tmp_tags = 'tmp,'+cached_tags

                # Use update to update the tmp one if already exists
                print (recursion_spaces+'  - Creating new "cached" artifact in the CM local repository ...')
                print (recursion_spaces+'    - Tags: {}'.format(tmp_tags))

                cache_meta = {}

                if version != '': cache_meta['version'] = version
                if version_min != '': cache_meta['version_min'] = version_min
                if version_max != '': cache_meta['version_max'] = version_max

                ii = {'action':'update',
                      'automation': self.meta['deps']['cache'],
                      'search_tags':tmp_tags,
                      'tags':tmp_tags,
                      'meta':cache_meta,
                      'force':True}

                r = self.cmind.access(ii)
                if r['return'] > 0: return r

                remove_tmp_tag = True

                cached_artifact = r['list'][0]

                cached_path = cached_artifact.path
                cached_meta = cached_artifact.meta

                cached_uid = cached_meta['uid']

                # Changing path to CM artifact for cached output
                # to record data and files there
                print (recursion_spaces+'  - Changing to {}'.format(cached_path))
                os.chdir(cached_path)

        ################################ 
        if not found_cached:
            # Add env from meta to new env if not empty
            artifact_env = meta.get('env',{})
            env.update(artifact_env)

            # Get dependencies on other scripts
            deps = meta.get('deps',[])

            # Update version only if in "versions" (not obligatory)
            # can be useful when handling complex Git revisions
            if version!='' and version in versions:
                versions_meta = versions[version]
                update_state_from_meta(versions_meta, env, state, deps, i)

            # Update env and other keys if variations
            if len(variation_tags)>0:
                for variation_tag in variation_tags:
                    if variation_tag.startswith('~'):
                        # ignore such tag (needed for caching only to differentiate variations)
                        continue

                    if variation_tag not in variations:
                        return {'return':1, 'error':'tag {} is not in variations {}'.format(variation_tag, variations.keys())}

                    variation_meta = variations[variation_tag]

                    update_state_from_meta(variation_meta, env, state, deps, i)

            #######################################################################
            # Check chain of dependencies on other CM scripts
            if len(deps)>0:
                # Go through dependencies list and run scripts
                for d in deps:
                    # Run script via CM API:
                    # Not very efficient but allows logging - can be optimized later
                    ii = {
                           'action':'run',
                           'automation':utils.assemble_cm_object(self.meta['alias'], self.meta['uid']),
                           'recursion_spaces':recursion_spaces + '  ',
                           'recursion':True,
                           'env':env,
                           'state':state,
                           'const':const,
                           'const_state':const_state
                         }

                    # Update input from dependency (extensible)
                    ii.update(d)

                    r = self.cmind.access(ii)
                    if r['return']>0: return r

            # Clean some output files
            clean_tmp_files(clean_files, recursion_spaces)

            # Check if has customize.py
            path_to_customize_py = os.path.join(path, 'customize.py')
            customize_code = None

            if os.path.isfile(path_to_customize_py):
                r=utils.load_python_module({'path':path, 'name':'customize'})
                if r['return']>0: return r

                customize_code = r['code']

                customize_common_input = {
                   'input':i,
                   'automation':self,
                   'artifact':artifact,
                   'customize':artifact.meta.get('customize',{}),
                   'os_info':os_info,
                   'recursion_spaces':recursion_spaces
                }

            # Check if pre-process and detect
            if 'preprocess' in dir(customize_code):

                print (recursion_spaces+'  - run preprocess ...')

                # Update env and state with const
                utils.merge_dicts({'dict1':env, 'dict2':const, 'append_lists':True, 'append_unique':True})
                utils.merge_dicts({'dict1':state, 'dict2':const_state, 'append_lists':True, 'append_unique':True})

                ii = copy.deepcopy(customize_common_input)
                ii['env'] = env
                ii['state'] = state

                r = customize_code.preprocess(ii)
                if r['return']>0: return r

                # Check if preprocess says to skip this component
                skip = r.get('skip', False)

                if skip:
                    print (recursion_spaces+'  - this script is skipped!')

                    # Check if script asks to run other dependencies instead of the skiped one
                    another_script = r.get('script', {})

                    if len(another_script) == 0:
                        return {'return':0, 'skipped': True}

                    print (recursion_spaces+'  - another script is executed instead!')
                    ii = {
                           'action':'run',
                           'automation':utils.assemble_cm_object(self.meta['alias'], self.meta['uid']),
                           'recursion_spaces':recursion_spaces + '  ',
                           'recursion':True,
                           'env':env,
                           'state':state,
                           'const':const,
                           'const_state':const_state,
                           'save_state':save_state
                         }

                    ii.update(another_script)

                    return self.cmind.access(ii)

                # If return version
                if cache and r.get('version','') != '':
                    cached_tags += ',version-' + r['version']

            # Prepare run script
            if bat_ext == '.sh':
                run_script = get_script_name(env, path)
            else:
                run_script = 'run' + bat_ext

            path_to_run_script = os.path.join(path, run_script)

            # Update env and state with const
            utils.merge_dicts({'dict1':env, 'dict2':const, 'append_lists':True, 'append_unique':True})
            utils.merge_dicts({'dict1':state, 'dict2':const_state, 'append_lists':True, 'append_unique':True})

            # Update env with the current path
            env['CM_TMP_CURRENT_SCRIPT_PATH'] = path

            # Record state
            r = utils.save_json(file_name = self.tmp_file_state, meta = state)
            if r['return']>0: return r

            # If batch file exists, run it with current env and state
            if os.path.isfile(path_to_run_script) and not reuse_cached:
                print ('')
                print (recursion_spaces+'  - run script ...')

                # Prepare env variables
                import copy
                script = copy.deepcopy(os_info['start_script'])

                # Check if script_prefix in the state from other components
                script_prefix = state.get('script_prefix',[])
                if len(script_prefix)>0:
                    script = script_prefix + ['\n'] + script

                script += convert_env_to_script(env, os_info)

                # Append batch file to the tmp script
                script.append('\n')
                script.append(os_info['run_bat'].replace('${bat_file}', path_to_run_script) + '\n')

                # Prepare and run script
                run_script = self.tmp_file_run + bat_ext

                r = record_script(run_script, script, os_info)
                if r['return']>0: return r

                # Run final command
                cmd = os_info['run_local_bat_from_python'].replace('${bat_file}', run_script)

                rc = os.system(cmd)

                if rc>0:
                    return {'return':1, 'error':'Component failed (return code = {})'.format(rc)}

                # Load updated state if exists
                if os.path.isfile(self.tmp_file_run_state):
                    r = utils.load_json(file_name = self.tmp_file_run_state)
                    if r['return']>0: return r

                    updated_state = r['meta']

                    utils.merge_dicts({'dict1':state, 'dict2':updated_state, 'append_lists':True, 'append_unique':True})

                # Load updated env if exists
                if os.path.isfile(self.tmp_file_run_env):
                    r = utils.load_txt(file_name = self.tmp_file_run_env)
                    if r['return']>0: return r

                    r = utils.convert_env_to_dict(r['string'])
                    if r['return']>0: return r
 
                    updated_env = r['dict']

                    utils.merge_dicts({'dict1':env, 'dict2':updated_env, 'append_lists':True, 'append_unique':True})

                # Check if post-process
                if 'postprocess' in dir(customize_code):

                    print (recursion_spaces+'  - run postprocess ...')

                    # Update env and state with const
                    utils.merge_dicts({'dict1':env, 'dict2':const, 'append_lists':True, 'append_unique':True})
                    utils.merge_dicts({'dict1':state, 'dict2':const_state, 'append_lists':True, 'append_unique':True})

                    ii = copy.deepcopy(customize_common_input)
                    ii['env'] = env
                    ii['state'] = state

                    r = customize_code.postprocess(ii)
                    if r['return']>0: return r

                    # If return version
                    if cache and r.get('version','') != '':
                        cached_tags += ',version-' + r['version']


            # Check chain of post dependencies on other CM scripts
            post_deps = meta.get('post_deps',[])

            if len(post_deps)>0:
                for d in post_deps:
                    # Run collective script via CM API:
                    # Not very efficient but allows logging - can be optimized later
                    ii = {
                           'action':'run',
                           'automation':utils.assemble_cm_object(self.meta['alias'], self.meta['uid']),
                           'recursion_spaces':recursion_spaces + '  ',
                           'recursion':True,
                           'env':env,
                           'state':state,
                           'const':const,
                           'const_state':const_state
                         }

                    ii.update(d)

                    r = self.cmind.access(ii)
                    if r['return']>0: return r


        ##################################### Finalize script
        # Force consts in the final new env and state
        utils.merge_dicts({'dict1':env, 'dict2':const, 'append_lists':True, 'append_unique':True})
        utils.merge_dicts({'dict1':state, 'dict2':const_state, 'append_lists':True, 'append_unique':True})

        # Detect env and state diff
        r = detect_state_diff(env, saved_env, state, saved_state)
        if r['return']>0: return r

        new_env = r['new_env']
        new_state = r['new_state']

        # Record all env
        env_all_script = convert_env_to_script(env, os_info, start_script = os_info['start_script'])
        r = record_script(self.tmp_file_env + bat_ext, env_all_script, os_info)
        if r['return']>0: return r

        env_script = convert_env_to_script(new_env, os_info, start_script = os_info['start_script'])
        r = record_script(self.tmp_file_env + bat_ext, env_script, os_info)
        if r['return']>0: return r

        # If using cached artifact, return to default path
        if cache and cached_path!='':
            # Check if need to remove tag
            if remove_tmp_tag:
                # Save state, env and deps for reuse
                path_to_cached_state_file = os.path.join(cached_path,
                    self.file_with_cached_state)

                r =  utils.save_json(file_name = path_to_cached_state_file, 
                       meta={'new_state':new_state,
                             'new_env':new_env,
                             'deps':deps})
                if r['return']>0: return r

                # Remove tmp tag from the "cached" arifact to finalize caching
                print (recursion_spaces+'  - Removing tmp tag in the script cached output {} ...'.format(cached_uid))

                ii = {'action': 'update',
                      'automation': self.meta['deps']['cache'],
                      'artifact': cached_uid,
                      'replace_lists': True, # To replace tags
                      'tags':cached_tags}
                r = self.cmind.access(ii)
                if r['return']>0: return r

        # Clean tmp files only in current path (do not touch cache - we keep all info there)
        os.chdir(current_path)

        if not i.get('dirty', False):
            clean_tmp_files(clean_files, recursion_spaces)

        # Record new env and new state in the current dir if needed
        if save_state:
#            r = utils.save_json(file_name = self.tmp_file_state, meta = new_state)
#            if r['return']>0: return r

            r = record_script(self.tmp_file_env + bat_ext, env_script, os_info)
            if r['return']>0: return r

        ############################# RETURN
        return {'return':0, 'env':env, 'new_env':new_env, 'state':state, 'new_state':new_state}

    ############################################################
    def find(self, i):
        """
        Find CM scripts

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

        tmp_out = i.get('out')
        console = tmp_out == 'con'

        # Search repository
        i['out'] = None
        i['common'] = True

        r = self.search(i)

        i['out'] = tmp_out

        if r['return']>0: return r

        lst = r['list']

        if len(lst)==0:
            return {'return':16, 'error':'no components found'}
        elif len(lst)>1:
            x=''
            for l in lst:
                x+='\n'+l.path

            return {'return':32, 'error':'more than 1 component found: {}'.format(x)}

        return r

    ##############################################################################
    def find_file_in_paths(self, i):
        """
        Find file name in a list of paths

        Args:
          (CM input dict): 

          paths (list): list of paths
          file_name (str): filename to find
          (select) (bool): if True and more than 1 path found, select
          (select_default) (bool): if True, select the default one
          (recursion_spaces) (str): add space to print

        Returns:
           (CM return dict):

           * return (int): return code == 0 if no error and >0 if error
           * (error) (str): error string if return>0

           (found_paths) (list): paths to file when found

        """

        paths = i['paths']
        file_name = i['file_name']
        select = i.get('select',False)
        select_default = i.get('select_default', False)
        recursion_spaces = i.get('recursion_spaces','')

        found_paths = []

        for path in paths:
            path_to_file = os.path.join(path, file_name)

            if os.path.isfile(path_to_file):
                if path not in found_paths:
                    found_paths.append(path)

        if select:
            if len(found_paths) == 1 or select_default:
                selection = 0
            else:
                # Select 1 and proceed
                print (recursion_spaces+'  - More than 1 path found:')

                print ('')
                num = 0

                for path in found_paths:
                    print (recursion_spaces+'  {}) {}'.format(num, path))
                    num+=1

                print ('')
                x=input(recursion_spaces+'  Select one or press Enter for 0: ')

                x=x.strip()
                if x=='': x='0'

                selection = int(x)

                if selection < 0 or selection >= num:
                    selection = 0

            print ('')
            print (recursion_spaces+'  Selected {}: {}'.format(selection, found_paths[selection]))

            found_paths = [found_paths[selection]]

        return {'return':0, 'found_paths':found_paths}

    ##############################################################################
    def find_artifact(self, i):
        """
        Find artifact

        Args:
          (CM input dict): 

          file_name (str): filename to find

          env (dict): global env
          os_info (dict): OS info

          (default_path_env_key) (str): check in default paths from global env 
                                        (PATH, PYTHONPATH, LD_LIBRARY_PATH ...)

          (recursion_spaces) (str): add space to print

        Returns:
           (CM return dict):

           * return (int): return code == 0 if no error and >0 if error
           * (error) (str): error string if return>0
                            error = 16 if artifact not found but no problem

           found_path (list): found path to an artifact
           full_path (str): full path to a found artifact
           default_path_list (list): list of default paths 

        """

        file_name = i['file_name']

        env = i['env']
        os_info = i['os_info']

        default_path_env_key = i.get('default_path_env_key', '')
        recursion_spaces = i.get('recursion_spaces', '')

        # Check if forced to search in a specific path
        path = env.get('CM_TMP_PATH','')

        default_path_list = [] if default_path_env_key == '' else \
           os.environ.get(default_path_env_key,'').split(os_info['env_separator'])

        if path == '':
            path_list = default_path_list
        else:
            print (recursion_spaces + '    # Requested paths: {}'.format(path))
            path_list = path.split(os_info['env_separator'])

        # Check if quiet
        select_default = True if env.get('CM_TMP_QUIET','') == 'yes' else False
        
        # Prepare paths to search
        r = self.find_file_in_paths({'paths':path_list,
                                     'file_name':file_name, 
                                     'select':True,
                                     'select_default': select_default,
                                     'recursion_spaces':recursion_spaces})
        if r['return']>0: return r

        found_paths = r['found_paths']

        if len(found_paths)==0:
            return {'return':16, 'error':'{} not found'.format(file_name)}

        # Prepare env
        found_path = found_paths[0]

        if found_path not in default_path_list:
            env_key = '+'+default_path_env_key

            paths = env.get(env_key, [])
            if found_path not in paths:
                paths.insert(0, found_path)
                env[env_key] = paths

        full_path = os.path.join(found_path, file_name)
        print (recursion_spaces + '    # Found object: {}'.format(full_path))

        return {'return':0, 'found_path':found_path, 
                            'full_path':full_path,
                            'default_path_list': default_path_list}

    ##############################################################################
    def parse_version(self, i):
        """
        Parse version

        Args:
          (CM input dict): 

          (file_name) (str): filename to get version from (tmp-ver.out by default)
          match_text (str): RE match text string
          group_number (int): RE group number to get version from
          env_key (str): which env key to update
          which_env (dict): which env to update

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

        r = utils.load_txt(file_name = file_name,
                           check_if_exists = True, 
                           split = True,
                           match_text = match_text,
                           fail_if_no_match = 'version was not detected')
        if r['return']>0: return r

        string = r['string']

        version = r['match'].group(group_number)

        which_env[env_key] = version

        return {'return':0, 'version':version, 'string':string}

##############################################################################
def get_script_name(env, path):
    """
    Internal: find the most appropriate run script name for the detected OS
    """

    from os.path import exists

    tmp_suff1 = env['CM_HOST_OS_FLAVOR'] if 'CM_HOST_OS_FLAVOR' in env else ''
    tmp_suff2 = env['CM_HOST_OS_VERSION'] if 'CM_HOST_OS_VERSION' in env else ''
    tmp_suff3 = env['CM_HOST_PLATFORM_FLAVOR'] if 'CM_HOST_PLATFORM_FLAVOR' in env else ''

    if exists(os.path.join(path, 'run-' + tmp_suff1 + tmp_suff2 + tmp_suff3 + '.sh')):
        return 'run-' + tmp_suff1 + tmp_suff2 + tmp_suff3 + '.sh'
    elif exists(os.path.join(path, 'run-' + tmp_suff1 + tmp_suff2 + '.sh')):
        return 'run-' + tmp_suff1 + tmp_suff2 + '.sh'
    elif exists(os.path.join(path, 'run-' + tmp_suff1 + '.sh')):
        return 'run-' + tmp_suff1 + '.sh'
    else:
        return 'run.sh';

##############################################################################
def convert_env_to_script(env, os_info, start_script = []):
    """
    Internal: convert env to script for a given platform
    """

    import copy
    script = copy.deepcopy(start_script)

    for k in sorted(env):
        env_value = env[k]

        # Process special env 
        key = k

        if k.startswith('+'):
            # List and append the same key at the end (+PATH, +LD_LIBRARY_PATH, +PYTHONPATH)
            key=k[1:]

            env_value = os_info['env_separator'].join(env_value) + \
                os_info['env_separator'] + \
                os_info['env_var'].replace('env_var',key)

        v = os_info['set_env'].replace('${key}', key).replace('${value}', env_value)

        script.append(v)

    return script

##############################################################################
def record_script(run_script, script, os_info):
    """
    Internal: record script and chmod 755 on Linux
    """

    final_script = '\n'.join(script)

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

    print ('')
    print (recursion_spaces+'  - cleaning files {} ...'.format(clean_files))

    for tmp_file in clean_files:
        if os.path.isfile(tmp_file):
            os.remove(tmp_file)

    return {'return':0}

##############################################################################
def update_deps_tags(deps, add_deps_tags):
    """
    Internal: add deps tags by name
    """

    for deps_name in add_deps_tags:
        deps_tags = add_deps_tags[deps_name].strip()

        if deps_tags != '':
            for dep in deps:
                names = dep.get('names',[])
                if len(names)>0 and deps_name in names:
                    tags = dep.get('tags','')
                    if tags!='': tags += ','
                    tags += deps_tags
                    dep['tags'] = tags

                    break

    return {'return':0}


##############################################################################
def update_state_from_meta(meta, env, state, deps, i):
    """
    Internal: update env and state from meta
    """

    update_env = meta.get('env', {})
    env.update(update_env)

    update_state = meta.get('state', {})
    utils.merge_dicts({'dict1':state, 'dict2':update_state, 'append_lists':True, 'append_unique':True})

    update_deps = meta.get('deps', [])
    if len(update_deps)>0:
        deps += update_deps

    add_deps_tags = meta.get('add_deps_tags', {})
    if len(add_deps_tags) >0 :
        update_deps_tags(deps, add_deps_tags)

    add_deps_tags_from_input = i.get('add_deps_tags', {})
    if len(add_deps_tags_from_input) >0 :
        update_deps_tags(deps, add_deps_tags_from_input)

    return {'return':0}

##############################################################################
def detect_state_diff(env, saved_env, state, saved_state):
    """
    Internal: detect diff in env and state
    """

    new_env = {}
    new_state = {}

    # Env is flat so no recursion
    for k in env:
        if k.startswith('CM_TMP_'):
            continue

        v = env[k]

        if k not in saved_env:
           new_env[k] = v
        elif type(v) == list:
           if v not in saved_env[k]:
               diff_list = [e for e in v if e not in saved_env[k]]
               if len(diff_list)>0:
                   new_env[k] = diff_list

    # Temporal solution for state - need to add recursion
    for k in state:
        v = state[k]

        if k not in saved_state:
           new_state[k] = v
        elif type(v) == list:
           if v not in saved_state[k]:
               diff_list = [e for e in v if e not in saved_state[k]]
               if len(diff_list)>0:
                   new_state[k] = diff_list

    return {'return':0, 'env':env, 'new_env':new_env, 'state':state, 'new_state':new_state}

##############################################################################
# Demo to show how to use CM components independently if needed
if __name__ == "__main__":
    import cmind
    auto = CAutomation(cmind, __file__)

    r=auto.test({'x':'y'})

    print (r)
