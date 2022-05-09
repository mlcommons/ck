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

          * Output from this automation action

        """

        from cmind import utils
        import copy

        recursion_spaces = i.get('recursion_spaces','')
        recursion = i.get('recursion', False)

        # Prepare state of the IC component and subcomponents
        state = i.get('state',{})

        # Debug
        parsed_artifact = i.get('parsed_artifact')
        parsed_artifact_alias = parsed_artifact[0][0] if parsed_artifact is not None else ''
        artifact_tags = i.get('tags','')

        cm_ic_info = 'CM intelligent component "{}" with tags "{}"'.format(parsed_artifact_alias, artifact_tags)

        print (recursion_spaces + '* Searching ' + cm_ic_info)

        # Get and cache minimal host OS info
        if len(self.os_info) == 0:
            r = self.cmind.access({'action':'get_host_os_info',
                                   'automation':'utils,dc2743f8450541e3'})
            if r['return']>0: return r

            os_info = r['info']
        else:
            os_info = self.os_info

        # Get env vars
        action = i.get('action','')
        env = i.get('env',{})

        # Find artifact
        r = self.find(i)
        if r['return']>0: return r

        artifact = r['list'][0]

        meta = artifact.meta
        path = artifact.path

        found_artifact = utils.assemble_cm_object(meta['alias'],meta['uid'])

        print (recursion_spaces+'  - Found ic::{} in {}'.format(found_artifact, path))

        # Update env from meta without overwriting current env
        artifact_env = meta.get('env',{})
        for k in artifact_env:
            utils.update_dict_if_empty(env, k, artifact_env[k])

        # Check chain of dependencies on other "intelligent components"
        deps = meta.get('deps',[])

        if len(deps)>0:
            for d in deps:
                # Run IC component via CM API:
                # Not very efficient but allows logging - can be optimized later
                ii = {
                       'action':'run',
                       'automation':utils.assemble_cm_object(self.meta['alias'],self.meta['uid']),
                       'recursion_spaces':recursion_spaces+'  ',
                       'recursion':True,
                       'deps':deps,
                       'env':env,
                       'state':state
                     }

                ii.update(d)

                r = self.cmind.access(ii)
                if r['return']>0: return r

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
               'os_info':os_info
            }

        # Check if pre-process
        if 'preprocess' in dir(customize_code):

            print (recursion_spaces+'  - run preprocess ...')

            ii=copy.deepcopy(customize_common_input)
            for keys in [('deps',deps), ('env',env), ('state',state)]:
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
        if os.path.isfile(path_to_run_script):

            print (recursion_spaces+'  - run script ...')

            # Update env with the current path
            env['CM_CURRENT_IC_PATH']=path

            # Record state
            r = utils.save_json(file_name = 'tmp-run.json', meta = state)
            if r['return']>0: return r

            # Prepare env variables
            script = []

            # Check if script_prefix in the state from other components
            script_prefix = state.get('script_prefix',[])
            if len(script_prefix)>0:
                script = script_prefix + ['\n'] + script
            
            for k in sorted(env):
                env_value = env[k]

                # Process special env 
                if k == 'CM_PATH_LIST':
                    k = 'PATH'
                    env_value = os_info['env_separator'].join(env_value) + \
                        os_info['env_separator'] + \
                        os_info['env_var'].replace('env_var',k)

                v = os_info['set_env'].replace('${key}', k).replace('${value}', env_value)
                script.append(v)

            # Append batch file to the tmp script
            script.append('\n')
            script.append(os_info['run_bat'].replace('${bat_file}', path_to_run_script) + '\n')

            # Prepare and run script
            run_script = 'tmp-run' + bat_ext

            final_script = '\n'.join(script)

            r = utils.save_txt(file_name=run_script, string=final_script)
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
            r = utils.load_json(file_name = 'tmp-run.json')
            if r['return']>0: return r

            state = r['meta']

            # Load env if exists
#           if os.path.isfile('tmp-run-env.out'):
#               r = utils.load_txt(file_name = 'tmp-run-env.out')
#               if r['return']>0: return r
#
#               r = utils.convert_env_to_dict(r['string'], env)
#               if r['return']>0: return r
#
#               new_env = r['dict']

            # Check if post-process
            if 'postprocess' in dir(customize_code):

               print (recursion_spaces+'  - run postprocess ...')

               ii=copy.deepcopy(customize_common_input)
               for keys in [('deps',deps), ('env',env), ('state',state)]:
                   ii[keys[0]]=keys[1]

               r = customize_code.postprocess(ii)
               if r['return']>0: return r


        return {'return':0, 'state':state, 'env':env, 'deps':deps}


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
            return {'return':32, 'error':'more than 1 component found'}

        return r



# Demo to show how to use CM components independently if needed
if __name__ == "__main__":
    import cmind
    auto = CAutomation(cmind, __file__)

    r=auto.test({'x':'y'})

    print (r)
