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

          (script) (list): list of commands (grows with recursive calls to "run ic")

          (recursion) (bool): True if recursive call. 
                              Useful when preparing the global bat file or Docker container
                              to save/run it in the end.

          (recursion_spaces) (str, internal): adding '  ' during recursion for debugging

          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          * Output from this automation action

        """

        from cmind import utils

        recursion_spaces = i.get('recursion_spaces','')
        recursion = i.get('recursion', False)

        # Debug
        parsed_artifact = i.get('parsed_artifact')
        parsed_artifact_alias = parsed_artifact[0][0] if parsed_artifact is not None else ''
        artifact_tags = i.get('tags','')

        cm_ic_info = 'CM intelligent component "{}" with tags "{}"'.format(parsed_artifact_alias, artifact_tags)

        print (recursion_spaces + '* Running ' + cm_ic_info)

        # Get and cache host OS info
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

        script = i.get('script',[])

        for k in env:
            v = os_info['set_env'].replace('${key}', k).replace('${value}', env[k])
            script.append(v)
        script.append('\n')

        # Find artifact
        r = self.find(i)
        if r['return']>0: return r

        artifact = r['list'][0]

        meta = artifact.meta

        # Check chain of dependencies on other "intelligent components"
        deps = meta.get('deps',{})

        if len(deps)>0:
            for d in deps:
                # Run IC component via CM API:
                # Not very efficient but allows logging - can be optimized later
                ii = {
                       'action':'run',
                       'automation':utils.assemble_cm_object(self.meta['alias'],self.meta['uid']),
                       'script':script,
                       'recursion_spaces':recursion_spaces+'  ',
                       'recursion':True
                     }

                ii.update(d)

                r = self.cmind.access(ii)
                if r['return']>0: return r



        # Prepare run script
        path = artifact.path
        bat_ext = os_info['bat_ext']
        run_script = 'run' + bat_ext

        path_to_run_script = os.path.join(path, run_script)

#       Currently ignore if batch file not found (thus not supported on a given OS)
#        if not os.path.isfile(path_to_run_script):
#            return {'return':1, 'error':'Script ' + run_script + ' not found in '+path}

        # If bat file exists, add it ...
        if os.path.isfile(path_to_run_script):
            # Load file and append to script
            r = utils.load_txt(file_name=path_to_run_script)
            if r['return']>0: return r

            s = r['string']

            s = os_info['bat_rem'].replace('${rem}', cm_ic_info) + '\n' + s

            script += s.split('\n')

        # If in root, prepare and run the final script
        if not recursion:
            run_script = 'tmp-run' + bat_ext

            final_script = '\n'.join(script)

            r = utils.save_txt(file_name=run_script, string=final_script)
            if r['return']>0: return r

            if os_info.get('set_exec_file','')!='':
                cmd = os_info['set_exec_file'].replace('${file_name}', run_script)

                rc = os.system(cmd)

            # Run final command
            print ('')

            cmd = os_info['run_local_bat'].replace('${bat_file}', run_script)

            rc = os.system(cmd)

            print ('')
            print ('Exit code: {}'.format(rc))





        return {'return':0}


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
