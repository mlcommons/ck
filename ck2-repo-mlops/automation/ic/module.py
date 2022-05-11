import os

from cmind.automation import Automation
from cmind import utils

class CAutomation(Automation):
    """
    CM "ic" automation actions (intelligent components)
    """

    ############################################################
    def __init__(self, cmind, automation_file):
        super().__init__(cmind, __file__)

        self.os_info = {}

        self.file_with_cached_state = 'cm-cached-state.json'

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
        Run intelligent component

        Args:
          (CM input dict): 

          (out) (str): if 'con', output to console

          (artifact) (str): specify intelligent component (CM artifact) explicitly

          (tags) (str): tags to find an intelligent component (CM artifact)

          (env) (dict): environment files

          (recursion) (bool): True if recursive call. 
                              Useful when preparing the global bat file or Docker container
                              to save/run it in the end.

          (recursion_spaces) (str, internal): adding '  ' during recursion for debugging

          (state) (dict, mostly internal): the state of the intelligent component

          (forced_env) (dict, internal): forced environment (taken from env during the first call)
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

        # Prepare updated state by this component (delta)
        new_state = {}
        new_env = {}

        # Prepare debug info
        parsed_artifact = i.get('parsed_artifact')
        parsed_artifact_alias = parsed_artifact[0][0] if parsed_artifact is not None else ''
        artifact_tags = i.get('tags','')

        cm_ic_info = 'CM intelligent component "{}" with tags "{}"'.format(parsed_artifact_alias, artifact_tags)

        print (recursion_spaces + '* Searching ' + cm_ic_info)

        # Get and cache minimal host OS info to be able to run scripts and manage OS environment
        if len(self.os_info) == 0:
            r = self.cmind.access({'action':'get_host_os_info',
                                   'automation':'utils,dc2743f8450541e3'})
            if r['return']>0: return r

            os_info = r['info']
        else:
            os_info = self.os_info

        # Find artifact
        ii=utils.sub_input(i, self.cmind.cfg['artifact_keys'])

        # Extract variations from input
        tags = ii.get('tags','').strip().split(',')

        artifact_tags = [t for t in tags if not t.startswith('v')]
        
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
            if t.startswith('v'):
                if t not in variation_tags:
                    variation_tags.append(t)

        # Check if needs to be installed
        # In such case, need to check if already installed
        install = meta.get('install', False)

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

            # Check if already installed
            search_tags = '-tmp,'+installed_tags
            print (recursion_spaces+'    - Tags: {}'.format(search_tags))
            r = self.cmind.access({'action':'find',
                                   'automation':'installed,2bb0f56a197145d5',
                                   'tags':search_tags})
            if r['return']>0: return r

            found_installed_artifacts = r['list']
            num_found_installed_artifacts = len(r['list'])

            installed_path = ''

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

        # Check chain of dependencies on other "intelligent components"
        deps = meta.get('deps',[])

        if len(deps)>0:
            for d in deps:
                tmp_env = merge_ic_env(env, new_env)
                tmp_state = merge_ic_state(state, new_state)

                # Run IC component via CM API:
                # Not very efficient but allows logging - can be optimized later
                ii = {
                       'action':'run',
                       'automation':utils.assemble_cm_object(self.meta['alias'],self.meta['uid']),
                       'recursion_spaces':recursion_spaces+'  ',
                       'recursion':True,
                       'env':tmp_env,
                       'state':tmp_state
                     }

                ii.update(d)

                r = self.cmind.access(ii)
                if r['return']>0: return r

                new_env = merge_ic_env(new_env, r['new_env'])
                new_state = merge_ic_state(new_state, r['new_state'])

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

        # Prepare run script
        bat_ext = os_info['bat_ext']
        run_script = 'run' + bat_ext

        path_to_run_script = os.path.join(path, run_script)

#       Currently ignore if batch file not found (thus not supported on a given OS)
#        if not os.path.isfile(path_to_run_script):
#            return {'return':1, 'error':'Script ' + run_script + ' not found in '+path}

        # If batch file exists, run it with current env and state
        if os.path.isfile(path_to_run_script) and not reuse_installed:

            print (recursion_spaces+'  - run script ...')

            # Update env with the current path
            env['CM_CURRENT_IC_PATH']=path

            # Record state
            r = utils.save_json(file_name = 'tmp-state.json', meta = state)
            if r['return']>0: return r
            r = utils.save_json(file_name = 'tmp-state-new.json', meta = new_state)
            if r['return']>0: return r

            # Prepare env variables
            script = []

            # Check if script_prefix in the state from other components
            script_prefix = new_state.get('script_prefix',[])
            if len(script_prefix)>0:
                script = script_prefix + ['\n'] + script

            tmp_env = merge_ic_env(env, new_env)

            script_only_with_env = []
            for k in sorted(tmp_env):
                env_value = tmp_env[k]

                # Process special env 
                key = k
                if k == 'CM_PATH_LIST':
                    key = 'PATH'
                    env_value = os_info['env_separator'].join(env_value) + \
                        os_info['env_separator'] + \
                        os_info['env_var'].replace('env_var',key)

                v = os_info['set_env'].replace('${key}', key).replace('${value}', env_value)
                script.append(v)

                # Add only new env
                if k in new_env:
                    script_only_with_env.append(v)

            # Append batch file to the tmp script
            script.append('\n')
            script.append(os_info['run_bat'].replace('${bat_file}', path_to_run_script) + '\n')

            # Prepare and run script
            run_script = 'tmp-run' + bat_ext
            run_script_only_with_env = 'tmp-env' + bat_ext

            final_script = '\n'.join(script)
            final_script_only_with_env = '\n'.join(script_only_with_env)

            r = utils.save_txt(file_name=run_script, string=final_script)
            if r['return']>0: return r

            r = utils.save_txt(file_name=run_script_only_with_env, string=final_script_only_with_env)
            if r['return']>0: return r

            if os_info.get('set_exec_file','')!='':
                cmd = os_info['set_exec_file'].replace('${file_name}', run_script)
                rc = os.system(cmd)

            # Run final command
            cmd = os_info['run_local_bat'].replace('${bat_file}', run_script)

            rc = os.system(cmd)

            if rc>0:
                return {'return':1, 'error':'Component failed (return code = {})'.format(rc)}

            # Load state
            if os.path.isfile('tmp-run-new.json'):
                r = utils.load_json(file_name = 'tmp-run-new.json')
                if r['return']>0: return r

            # Load env if exists
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
                print (recursion_spaces+'  - Removing tmp tag ...')

                ii = {'action': 'update',
                      'automation': 'installed,2bb0f56a197145d5',
                      'artifact': installed_uid,
                      'tags':installed_tags}
                r = self.cmind.access(ii)
                if r['return']>0: return r

            os.chdir(current_path)

        return {'return':0, 'new_state':new_state, 'new_env':new_env}


    ############################################################
    def find(self, i):
        """
        Find intelligent components

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
def merge_ic_env(d, new_d):
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
def merge_ic_state(d, new_d):
    """
    Internal: merge IC global and new states
    """

    import copy

    tmp_d = copy.deepcopy(d)

    utils.merge_dicts({'dict1':tmp_d, 'dict2':new_d, 'append_lists':True, 'append_unique':True})

    return tmp_d

##############################################################################
# Demo to show how to use CM components independently if needed
if __name__ == "__main__":
    import cmind
    auto = CAutomation(cmind, __file__)

    r=auto.test({'x':'y'})

    print (r)
