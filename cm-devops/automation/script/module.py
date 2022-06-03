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
        self.variation_prefix = '_'

        self.__version__ = "0.5.0"

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

          (env) (dict): environment files

          (version) (str): version to be added to env.CM_NEED_VERSION to specialize this flow
          (take_version_from_env) (bool): use version from env.CM_NEED_VERSION

          (path) (str): list of paths to be added to env.CM_PATH to specialize this flow

          (skip_install) (bool): if True, skip installation into "installed" artifacts
                                 and run in current directory

          (new) (bool): if True, skip search for installed and run again

          (recursion) (bool): True if recursive call.
                              Useful when preparing the global bat file or Docker container
                              to save/run it in the end.

          (recursion_spaces) (str, internal): adding '  ' during recursion for debugging

          (state) (dict): mostly internal - the state of the CM script

          (forced_env) (dict): internal - forced environment (taken from env during the first call)
          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          * new_env (dict): new environment (delta from this IC)
          * new_state (dict): new state (delta from this IC)

        """

        from cmind import utils
        import copy

        recursion_spaces = i.get('recursion_spaces','')
        recursion = i.get('recursion', False)

        # Get current state of the IC component and subcomponents
        state = i.get('state',{})
        env = i.get('env',{})

        # Set current path
        if 'CM_CURRENT_PATH' not in env: env['CM_CURRENT_PATH']=os.path.abspath(os.getcwd())

        # Prepare updated state by this component (delta)
        new_state = {}
        new_env = {}

        # Prepare debug info
        parsed_artifact = i.get('parsed_artifact')
        parsed_artifact_alias = parsed_artifact[0][0] if parsed_artifact is not None else ''
        artifact_tags = i.get('tags','')

        cm_script_info = 'CM script(s)'
        if parsed_artifact_alias!='':
            cm_script_info += ' "{}"'.format(parsed_artifact_alias)
        if artifact_tags!='':
            cm_script_info += ' with tags "{}"'.format(artifact_tags)

        print ('')
        print (recursion_spaces + '* Searching ' + cm_script_info)

        # Get and cache minimal host OS info to be able to run scripts and manage OS environment
        if len(self.os_info) == 0:
            r = self.cmind.access({'action':'get_host_os_info',
                                   'automation':'utils,dc2743f8450541e3'})
            if r['return']>0: return r

            os_info = r['info']
        else:
            os_info = self.os_info

        # Find artifact
        ii=utils.sub_input(i, self.cmind.cfg['artifact_keys'] + ['tags'])

        # Extract variations from input
        tags = ii.get('tags','').strip().split(',')

        artifact_tags = [t for t in tags if not t.startswith(self.variation_prefix)]

        ii['tags']=','.join(artifact_tags)

        r = self.find(ii)
        if r['return']>0: return r

        artifact = r['list'][0]

        meta = artifact.meta
        path = artifact.path

        found_artifact = utils.assemble_cm_object(meta['alias'],meta['uid'])

        print (recursion_spaces+'  - Found ic::{} in {}'.format(found_artifact, path))

        current_path = os.getcwd()

        # Check variations in input tags
        variation_tags = []
        for t in tags:
            t=t.strip()
            if t.startswith(self.variation_prefix):
                t_without_prefix = t[len(self.variation_prefix):]
                if t_without_prefix not in variation_tags:
                    variation_tags.append(t_without_prefix)

        # Check version
        version = i.get('version','').strip()

        if i.get('take_version_from_env', False):
            version = env.get('CM_NEED_VERSION','')

        if version == '':
            version = meta.get('default_version','')

        if version != '':
            # We record in env and not in new env because the component 
            # must detect and record the correct version in new_env
            env['CM_NEED_VERSION'] = version

        # Check paths
        paths = i.get('path','').strip()

        if paths != '':
            env['CM_PATH'] = paths

        # Check if needs to be installed
        # In such case, need to check if already installed
        install = meta.get('install', False)
        if i.get('skip_install', False): 
            install = False

        installed_artifact_uid = ''

        remove_tmp_tag = False
        reuse_installed = False

        if install:
            print (recursion_spaces+'  - Checking if already installed ...')

            # Create a search query to find that we already ran this components with the same or similar input
            # It will be gradually enhanced with more knowledge ...

            # For simplicity, we use tags for the search in "installed" components
            # TBD: we will need to add variations/versions later
            installed_tags = 'ic-artifact-'+meta['uid']

            # Add tags from the original component
            if len(meta.get('tags',[]))>0:
                installed_tags += ',' + ','.join(meta['tags'])

            # Add variation
            if len(variation_tags)>0:
                installed_tags += ',' + ','.join(variation_tags)

            # Add version
            if version!='':
                installed_tags += ',version-' + version

            # Check if already installed
            if i.get('new', False):
                search_tags = 'tmp,'+installed_tags
            else:
                search_tags = '-tmp,'+installed_tags

            print (recursion_spaces+'    - Tags: {}'.format(search_tags))

            r = self.cmind.access({'action':'find',
                                   'automation':'installed,2bb0f56a197145d5',
                                   'tags':search_tags})
            if r['return']>0: return r

            found_installed_artifacts = r['list']

            num_found_installed_artifacts = len(found_installed_artifacts)

            installed_path = ''

            if num_found_installed_artifacts > 0:
                selection = 0

                if num_found_installed_artifacts > 1:
                    # Select 1 and proceed
                    print (recursion_spaces+'  - More than 1 installed artifact found:')

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
                    print (recursion_spaces+'    Selected {}: {}'.format(selection, found_installed_artifacts[selection].path))

                else:
                    print (recursion_spaces+'  - Found installed artifact: {}'.format(found_installed_artifacts[0].path))

                # Continue with the selected installed artifact
                installed_artifact = r['list'][selection]

                print (recursion_spaces+'  - Loading "cached" state ...')

                path_to_cached_state_file = os.path.join(installed_artifact.path,
                    self.file_with_cached_state)

                r =  utils.load_json(file_name = path_to_cached_state_file)
                if r['return']>0: return r

                cached_state = r['meta']

                # Return cached delta
                return {'return':0, 'new_state':cached_state['new_state'], 'new_env':cached_state['new_env']}

            if num_found_installed_artifacts == 0:
                # If not installed:
                # Create installed artifact and mark as tmp (remove if install successful)
                if len(variation_tags)==0:
                    # Check if artifact meta has default variation tags and add
                    variation_tags = meta.get('default_variations',[])

                    if len(variation_tags)>0:
                        installed_tags += ',' + ','.join(variation_tags)

                tmp_tags = 'tmp,'+installed_tags

                # Use update to update the tmp one if already exists
                print (recursion_spaces+'  - Creating new "installed" artifact ...')
                print (recursion_spaces+'    - Tags: {}'.format(tmp_tags))
                ii = {'action':'update',
                      'automation': 'installed,2bb0f56a197145d5',
                      'search_tags':tmp_tags,
                      'tags':tmp_tags,
                      'force':True}

                r = self.cmind.access(ii)
                if r['return'] > 0: return r

                remove_tmp_tag = True

                installed_artifact = r['list'][0]

                installed_path = installed_artifact.path
                installed_meta = installed_artifact.meta

                installed_uid = installed_meta['uid']

                print (recursion_spaces+'  - Changing to {}'.format(installed_path))
                os.chdir(installed_path)

            else:
                selection = 0

                if num_found_installed_artifacts > 1:
                    # Select 1 and proceed
                    print (recursion_spaces+'  - More than 1 installed artifact found:')

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
                    print (recursion_spaces+'    Selected {}: {}'.format(selection, found_installed_artifacts[selection].path))

                else:
                    print (recursion_spaces+'  - Found installed artifact: {}'.format(found_installed_artifacts[0].path))

                # Continue with the selected installed artifact
                installed_artifact = r['list'][selection]

                print (recursion_spaces+'  - Loading "cached" state ...')

                path_to_cached_state_file = os.path.join(installed_artifact.path,
                    self.file_with_cached_state)

                r =  utils.load_json(file_name = path_to_cached_state_file)
                if r['return']>0: return r

                cached_state = r['meta']

                # Return cached delta
                return {'return':0, 'new_state':cached_state['new_state'], 'new_env':cached_state['new_env']}

        # Add env from meta to new env if not empty
        artifact_env = meta.get('env',{})
        for k in artifact_env:
            utils.update_dict_if_empty(env, k, artifact_env[k])
        artifact_new_env = meta.get('new_env',{})
        for k in artifact_new_env:
            utils.update_dict_if_empty(new_env, k, artifact_new_env[k])

        # Update env if variations
        if len(variation_tags)>0:
            variations = artifact.meta['variations']

            for variation_tag in variation_tags:
                variation_meta = variations[variation_tag]

                variation_env = variation_meta.get('env',{})
                for k in variation_env:
                    utils.update_dict_if_empty(env, k, variation_env[k])

                variation_new_env = variation_meta.get('new_env',{})
                for k in variation_new_env:
                    utils.update_dict_if_empty(new_env, k, variation_new_env[k])

        # Check chain of dependencies on other CM scripts
        deps = meta.get('deps',[])

        if len(deps)>0:
            for d in deps:
                tmp_env = merge_script_env(env, new_env)
                tmp_state = merge_script_state(state, new_state)

                # Run IC component via CM API:
                # Not very efficient but allows logging - can be optimized later
                ii = {
                       'action':'run',
                       'automation':utils.assemble_cm_object(self.meta['alias'], self.meta['uid']),
                       'recursion_spaces':recursion_spaces + '  ',
                       'recursion':True,
                       'env':tmp_env,
                       'state':tmp_state
                     }

                ii.update(d)

                r = self.cmind.access(ii)
                if r['return']>0: return r

                new_env = merge_script_env(new_env, r['new_env'])
                new_state = merge_script_state(new_state, r['new_state'])

        # Clean some output files
        clean_files = meta.get('clean_files', []) + ['tmp-run-state.json', 'tmp-run-env.out', 'tmp-ver.out']

        print ('')
        print (recursion_spaces+'  - cleaning files {} ...'.format(clean_files))

        for tmp_file in clean_files:
            if os.path.isfile(tmp_file):
                os.remove(tmp_file)

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

            ii=copy.deepcopy(customize_common_input)
            for keys in [('env',env), ('state',state), ('new_env',new_env), ('new_state',new_state)]:
                ii[keys[0]]=keys[1]

            r = customize_code.preprocess(ii)
            if r['return']>0: return r

            # Check if preprocess says to skip this component
            skip = r.get('skip', False)

            if skip:
                print (recursion_spaces+'  - Skiped')

                after_deps = r.get('deps',[])

                r = {'return':0}

                if len(after_deps)==0:
                    r['skipped'] = True
                else:
                    for d in after_deps:
                        tmp_env = merge_script_env(env, new_env)
                        tmp_state = merge_script_state(state, new_state)

                        # Run IC component via CM API:
                        # Not very efficient but allows logging - can be optimized later
                        ii = {
                               'action':'run',
                               'automation':utils.assemble_cm_object(self.meta['alias'], self.meta['uid']),
                               'recursion_spaces':recursion_spaces + '  ',
                               'recursion':True,
                               'env':tmp_env,
                               'state':tmp_state
                             }

                        ii.update(d)

                        r = self.cmind.access(ii)
                        if r['return']>0: return r

                        new_env = merge_script_env(new_env, r['new_env'])
                        new_state = merge_script_state(new_state, r['new_state'])

                r.update({'new_state':new_state, 'new_env':new_env})        

                return r

            # If return version
            if r.get('version','') != '':
                installed_tags += ',version-' + r['version']

        # Prepare run script
        bat_ext = os_info['bat_ext']
        if bat_ext == '.sh':
            run_script = get_script_name(new_env, path)
        else:
            run_script = 'run' + bat_ext

        path_to_run_script = os.path.join(path, run_script)

#       Currently ignore if batch file not found (thus not supported on a given OS)
#        if not os.path.isfile(path_to_run_script):
#            return {'return':1, 'error':'Script ' + run_script + ' not found in '+path}

        # Update env with the current path
        env['CM_CURRENT_SCRIPT_PATH']=path

        # Record state
        r = utils.save_json(file_name = 'tmp-state.json', meta = state)
        if r['return']>0: return r
        r = utils.save_json(file_name = 'tmp-state-new.json', meta = new_state)
        if r['return']>0: return r

        # If batch file exists, run it with current env and state
        if os.path.isfile(path_to_run_script) and not reuse_installed:
            print ('')
            print (recursion_spaces+'  - run script ...')

            # Prepare env variables
            import copy
            script = copy.deepcopy(os_info['start_script'])

            # Check if script_prefix in the state from other components
            script_prefix = new_state.get('script_prefix',[])
            if len(script_prefix)>0:
                script = script_prefix + ['\n'] + script

            tmp_env = merge_script_env(env, new_env)

            script += convert_env_to_script(tmp_env, os_info)

            # Append batch file to the tmp script
            script.append('\n')
            script.append(os_info['run_bat'].replace('${bat_file}', path_to_run_script) + '\n')

            # Prepare and run script
            run_script = 'tmp-run' + bat_ext

            r = record_script(run_script, script, os_info)
            if r['return']>0: return r

            # Run final command
            cmd = os_info['run_local_bat_from_python'].replace('${bat_file}', run_script)

            rc = os.system(cmd)

            if rc>0:
                return {'return':1, 'error':'Component failed (return code = {})'.format(rc)}

            # Load updated state if exists
            if os.path.isfile('tmp-run-state.json'):
                r = utils.load_json(file_name = 'tmp-run-state.json')
                if r['return']>0: return r

                new_state = merge_script_state(new_state, r['meta'])

            # Load updated env if exists
            if os.path.isfile('tmp-run-env.out'):
                r = utils.load_txt(file_name = 'tmp-run-env.out')
                if r['return']>0: return r

                r = utils.convert_env_to_dict(r['string'])
                if r['return']>0: return r
 
                env_from_run = r['dict']

                for k in env_from_run:
                    utils.update_dict_if_empty(new_env, k, env_from_run[k])

            # Check if post-process
            if 'postprocess' in dir(customize_code):
                print (recursion_spaces+'  - run postprocess ...')

                ii=copy.deepcopy(customize_common_input)
                for keys in [('env',env), ('state',state), ('new_env',new_env), ('new_state',new_state)]:
                    ii[keys[0]]=keys[1]

                r = customize_code.postprocess(ii)
                if r['return']>0: return r

                # If return version
                if r.get('version','') != '':
                    installed_tags += ',version-' + r['version']


        # Check chain of post dependencies on other CM scripts
        post_deps = meta.get('post_deps',[])

        if len(post_deps)>0:
            for d in post_deps:
                tmp_env = merge_script_env(env, new_env)
                tmp_state = merge_script_state(state, new_state)

                # Run IC component via CM API:
                # Not very efficient but allows logging - can be optimized later
                ii = {
                       'action':'run',
                       'automation':utils.assemble_cm_object(self.meta['alias'], self.meta['uid']),
                       'recursion_spaces':recursion_spaces + '  ',
                       'recursion':True,
                       'env':tmp_env,
                       'state':tmp_state
                     }

                ii.update(d)

                r = self.cmind.access(ii)
                if r['return']>0: return r

                new_env = merge_script_env(new_env, r['new_env'])
                new_state = merge_script_state(new_state, r['new_state'])

        # Record new env 
        new_env_script = convert_env_to_script(new_env, os_info, start_script = os_info['start_script'])

        r = record_script('tmp-env' + bat_ext, new_env_script, os_info)
        if r['return']>0: return r

        # If using installed artifact, return to default path
        if install and installed_path!='':
            # Check if need to remove tag
            if remove_tmp_tag:
                # Save state, env and deps for reuse
                path_to_cached_state_file = os.path.join(installed_path,
                    self.file_with_cached_state)

                r =  utils.save_json(file_name = path_to_cached_state_file, 
                       meta={'new_state':state,
                             'new_env':new_env,
                             'deps':deps})
                if r['return']>0: return r

                # Remove tmp tag from the "installed" arifact to finalize installation
                print (recursion_spaces+'  - Removing tmp tag in CM entry installed::{} ...'.format(installed_uid))

                ii = {'action': 'update',
                      'automation': 'installed,2bb0f56a197145d5',
                      'artifact': installed_uid,
                      'replace_lists': True, # To replace tags
                      'tags':installed_tags}
                r = self.cmind.access(ii)
                if r['return']>0: return r

            os.chdir(current_path)

        return {'return':0, 'new_state':new_state, 'new_env':new_env}


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
        recursion_spaces = i.get('recursion_spaces','')

        found_paths = []

        for path in paths:
            path_to_file = os.path.join(path, file_name)

            if os.path.isfile(path_to_file):
                if path not in found_paths:
                    found_paths.append(path)

        if select and len(found_paths)>1:
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
          new_env (dict): local env
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
        new_env = i['new_env']
        os_info = i['os_info']

        default_path_env_key = i.get('default_path_env_key', '')
        recursion_spaces = i.get('recursion_spaces', '')

        # Check if forced to search in a specific path
        path = env.get('CM_PATH','')

        default_path_list = [] if default_path_env_key == '' else \
           os.environ.get(default_path_env_key,'').split(os_info['env_separator'])

        if path == '':
            path_list = default_path_list
        else:
            print (recursion_spaces + '    # Requested paths: {}'.format(path))
            path_list = path.split(os_info['env_separator'])

        # Prepare paths to search
        r = self.find_file_in_paths({'paths':path_list,
                                     'file_name':file_name, 
                                     'select':True,
                                     'recursion_spaces':recursion_spaces})
        if r['return']>0: return r

        found_paths = r['found_paths']

        if len(found_paths)==0:
            return {'return':16, 'error':'{} not found'.format(file_name)}

        # Prepare env
        found_path = found_paths[0]

        if found_path not in default_path_list:
            new_env['+'+default_path_env_key] = [found_path]

        full_path = os.path.join(found_path, file_name)
        print (recursion_spaces + '    # Found component: {}'.format(full_path))

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
        if file_name == '': file_name = 'tmp-ver.out'

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
def merge_script_env(d, new_d):
    """
    Internal: merge IC global and new environments
    """

    import copy

    tmp_d = copy.deepcopy(d)

    for k in new_d:
        if type(new_d[k])==list:
            if k not in d:
                tmp_d[k]=[]
            for v in new_d[k]:
                if v not in tmp_d[k]:
                    tmp_d[k].append(v)

        elif tmp_d.get(k) is None or tmp_d.get(k)=='':
            tmp_d[k] = new_d[k]

    return tmp_d

##############################################################################
def merge_script_state(d, new_d):
    """
    Internal: merge IC global and new states
    """

    import copy

    tmp_d = copy.deepcopy(d)

    utils.merge_dicts({'dict1':tmp_d, 'dict2':new_d, 'append_lists':True, 'append_unique':True})

    return tmp_d

##############################################################################
def get_script_name(new_env, path):
    """
    Internal: find the most appropriate run script name for the detected OS
    """

    from os.path import exists

    tmp_suff1 = new_env['CM_HOST_OS_FLAVOR'] if 'CM_HOST_OS_FLAVOR' in new_env else ''
    tmp_suff2 = new_env['CM_HOST_OS_VERSION'] if 'CM_HOST_OS_VERSION' in new_env else ''
    tmp_suff3 = new_env['CM_HOST_PLATFORM_FLAVOR'] if 'CM_HOST_PLATFORM_FLAVOR' in new_env else ''

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
# Demo to show how to use CM components independently if needed
if __name__ == "__main__":
    import cmind
    auto = CAutomation(cmind, __file__)

    r=auto.test({'x':'y'})

    print (r)
