# Collective Mind core functions

from cmind.config import Config
from cmind.repos import Repos
from cmind.automation import Automation
from cmind import utils

import sys
import os
import imp
import importlib
import pkgutil
import inspect

cm = None

############################################################
def access(i):
    """
    Initialize and access Collective Mind without customization
    """

    global cm

    if cm is None:
       cm=CM()

    return cm.access(i)

############################################################
def error(i):
    """
    Print error
    """

    return cm.error(i)

############################################################
def halt(i):
    """
    Print error and halt
    """

    return cm.halt(i)

############################################################
class CM(object):
    """
    Main Collective Mind class
    """

    ############################################################
    def __init__(self, home_path = '', debug = False):
        """
        Initialize Collective Mind class
        """

#        print ('************************************************')
#        print ('Initialize CM ...')
#        print ('************************************************')

        # Initialize and update CM configuration
        self.cfg = Config().cfg

        # Check if debug (raise error instead of soft error)
        self.debug = False
        if debug or os.environ.get(self.cfg['env_debug'],'').strip().lower()=='yes':
            self.debug = True

        # Explicit path to direcory with CM repositories and other internals
        self.home_path = home_path
        if self.home_path == '':
            s = os.environ.get(self.cfg['env_home'],'').strip()
            if s != '':
                self.home_path = s

        if self.home_path == '':
           from os.path import expanduser
           self.home_path = os.path.join(expanduser("~"), self.cfg['default_home_dir'])

        self.path_to_cmind_kernel = inspect.getfile(inspect.currentframe())
        self.path_to_cmind = os.path.dirname(self.path_to_cmind_kernel)
        self.path_to_cmind_repo = os.path.join(self.path_to_cmind, self.cfg['cmind_repo'])

        # Repositories
        self.repos = None

        # Default automation
        self.default_automation = None

    ############################################################
    def parse_cli(self, cmd):
        """
        Parse CM command line.

        Args:
            cmd (str | list) : arguments as a string or list

        Returns:
            Dictionary:
                return (int): return code == 0 if no error 
                                          >0 if error

                (error) (str): error string if return>0

                cm_input (dict): CM input
        """

        # If input is string, convert to argv
        # We use shlex to properly convert ""
        if cmd is None:
            argv = []

        elif type(cmd) == str:
            import shlex
            argv = shlex.split(cmd)
        
        else:
            argv = cmd

        # Positional arguments
        cm_input = {}

        # First argument: automation
        special_cli_characters=['-', '@']

        for key in ['action', 'automation']:
            if len(argv) > 0 and argv[0].strip()[0] not in special_cli_characters:
                cm_input[key] = argv.pop(0)

        # Check if just one artifact or multiple ones
        artifact=''
        artifacts=[] # Only added if more than 1 artifact!
        
        for a in argv:
            if a.startswith('@'):
                # Load JSON or YAML file
                from cmind.utils import io
                r = utils.load_json_or_yaml(file_name = a[1:], check_if_exists=True)
                if r['return'] >0 : return r

                meta = r['meta']
                
                cm_input.update(meta)

            elif not a.startswith('-'):
                # artifact
                if artifact=='':
                    artifact=a
                    cm_input['artifact']=a

                artifacts.append(a)
            else:
                # flags
                if '=' in a:
                   key,value = a.split('=')
                   value=value.strip()
                else:
                   key=a
                   value=True

                if key.startswith('-'): key=key[1:]
                if key.startswith('-'): key=key[1:]

                if key.endswith(','): 
                   key = key[:-1]
                   value = value.split(',') if value!="" else []
               
                if '.' in key:
                   keys = key.split('.')
                   new_cm_input = cm_input
                   for key in keys[:-1]:
                       if key not in new_cm_input:
                          new_cm_input[key] = {}
                       new_cm_input = new_cm_input[key]

                   new_cm_input[keys[-1]]=value
                else:
                   cm_input[key] = value

        # Add artifacts if > 1
        if len(artifacts) > 1:
            cm_input['artifacts'] = artifacts

        return {'return':0, 'cm_input':cm_input}

    ############################################################
    def error(self, r):
        """
        Process CM error (print or raise and exit)

            Args:
               r (dict)        - output from CM function
               debug (Boolean) - if True, call raise
               
        Returns:
            None or raise

        """

        import os
        
        if r['return']>0:
            if self.debug:
                raise Exception(r['error'])

            sys.stderr.write(self.cfg['error_prefix']+' '+r['error']+'!\n')

        return r

    ############################################################
    def halt(self, r):
        """
        Process CM error and halt (useful for scripts)

            Args:
               r (dict)        - output from CM function
               debug (Boolean) - if True, call raise
               
        Returns:
            None or raise

        """

        # Force console
        self.error(r)
        
        sys.exit(r['return'])

    ############################################################
    def access(self, i, out = None):
        """
        Access customized Collective Mind object

        Args:
            i (dict | str | argv): CM input
            out (str) - =='con' -> force output to console

        Returns:
            Dictionary:
                return (int): return code == 0 if no error 
                                          >0 if error

                (error) (str): error string if return>0

                data from a given action
        
        """

        # Check the type of input
        if i is None:
           i = {}

        # Attempt to detect debug flag early (though suggest to use environment)
        # If error in parse_cli, it will raise error
        if self.cfg['flag_debug'] in i:
            self.debug = True

        # Extra parse if string or list
        if type(i) == str or type(i) == list:
            r = self.parse_cli(i)
            if r['return'] >0 : return r

            i = r['cm_input']

        # Check if force out programmatically (such as from CLI)
        if 'out' not in i and out is not None:
            i['out'] = out

        # Check if console
        console = i.get('out') == 'con'

        # Check if has help flag
        cm_help = i.get(self.cfg['flag_help'], False) or i.get(self.cfg['flag_help2'], False)
        
        # Initialized default automation with default database actions
        if self.default_automation == None:
           self.default_automation = Automation(self, __file__)

        # Check automation action
        action = i.get('action','')

        # Print basic help if action == ''
        if action == '':
            if console:
                print (self.cfg['info_cli'])

                if cm_help:
                   import types

                   print ('')
                   print ('Common automation actions for all CM artifacts:')
                   print ('')

                   for d in sorted(dir(self.default_automation)):
                       if type(getattr(self.default_automation, d))==types.MethodType and not d.startswith('_'):
                           print ('* '+d)

            return {'return':0, 'warning':'no action'}

        # Check automation
        automation = i.get('automation','')

        # Load info about all CM repositories (to enable search for automations and artifacts)
        if self.repos == None:
            repos = Repos(path = self.home_path, cfg = self.cfg, 
                          path_to_default_repo = self.path_to_cmind_repo)

            r = repos.load()
            if r['return'] >0 : return r

            # Set only after all initializations
            self.repos = repos

        # Check if forced default automation
        use_default_automation = True if i.get('default',False) else False

        automation_lst = []
        use_any_action = False
        
        # If automation!='', attempt to find it and load
        # Otherwise use the default automation
        if automation != '' and not use_default_automation:
            # Parse automation potentially with a repository
            # and convert it into CM object [(artifact,UID) (,(repo,UID))]
            r = utils.parse_cm_object(automation)
            if r['return'] >0 : return r

            parsed_automation = r['cm_object']
            i['parsed_automation'] = parsed_automation

            # First object in a list is an automation
            # Second optional object in a list is a repo
            auto_name = parsed_automation[0] if len(parsed_automation)>0 else ('','')
            auto_repo = parsed_automation[1] if len(parsed_automation)>1 else None


            # Search for automations in repos (local, default, other) TBD: maybe should be local, other, default?
            r = self.default_automation.search({'parsed_automation':[('automation','bbeb15d8f0a944a4')],
                                                'parsed_artifact':parsed_automation})
            if r['return']>0: return r
            automation_lst = r['list']

            if len(automation_lst)==1:
                automation = automation_lst[0]
                
                automation_path = automation.path
                automation_name = self.cfg['default_automation_module_name']
                automation_meta = automation.meta

                use_any_action = automation_meta.get('use_any_action',False)
                
                # Find Python module for this automation
                try:
                    found_automation = imp.find_module(automation_name, [automation_path])
                except ImportError as e:  # pragma: no cover
                    return {'return': 1, 'error': 'can\'t find Python module code (path={}, name={}, err={})'.format(automation_path, automation_name, format(e))}

                automation_handler = found_automation[0]
                automation_full_path = found_automation[1]

                # Generate uid for the run-time extension of the loaded Python module
                # otherwise Python modules with the same extension (key.py for example)
                # will be reloaded ...

                r = utils.gen_uid()
                if r['return'] > 0: return r
                automation_run_time_uid = 'rt-'+r['uid']

                try:
                   loaded_automation = imp.load_module(automation_run_time_uid, automation_handler, automation_full_path, found_automation[2])
                except ImportError as e:  # pragma: no cover
                    return {'return': 1, 'error': 'can\'t load Python module code (path={}, name={}, err={})'.format(automation_path, automation_name, format(e))}

                if automation_handler is not None:
                    automation_handler.close()

                loaded_automation_class = loaded_automation.CAutomation
                
                # Try to load meta description
                automation_path_meta = os.path.join(automation_path, self.cfg['file_cmeta'])

                r = utils.is_file_json_or_yaml(file_name = automation_path_meta)
                if r['return']>0: return r

                if not r['is_file']:
                    return {'return':4, 'error':'automation meta not found in {}'.format(automation_path)}

                # Load artifact class
                r=utils.load_yaml_and_json(automation_path_meta)
                if r['return']>0: return r

                automation_meta = r['meta']

            elif len(automation_lst)>1:
                return {'return':2, 'error':'ambiguity because several automations were found for {}'.format(auto_name)}

            # Report an error if a repo is specified for a given automation action but it's not found there
            if len(automation_lst)==0 and auto_repo is not None:
                return {'return':3, 'error':'automation is not found in a specified repo {}'.format(auto_repo)}
                
        # If no automation was found or we force default automation
        if use_default_automation or len(automation_lst)==0:
            auto=('automation','bbeb15d8f0a944a4')
            from . import automation as loaded_automation

            loaded_automation_class = loaded_automation.Automation

            automation_full_path = loaded_automation.self_path

            automation_meta = {
                            'alias':'automation',
                            'uid':'bbeb15d8f0a944a4'
                          }

        # Finalize automation class initialization
        initialized_automation = loaded_automation_class(self, automation_full_path)
        initialized_automation.meta = automation_meta

        # Convert action into function (substitute internal words)
        original_action = action
        action = action.replace('-','_')

        if action in self.cfg['action_substitutions']:
            action = self.cfg['action_substitutions'][action]
        
        # Check action in a class when importing
        if use_any_action:
            action = 'any'
        
        print_automation = automation_meta.get('alias','')+','+automation_meta.get('uid','')
        
        if not hasattr(initialized_automation, action):
            return {'return':4, 'error':'action "{}" not found in automation "{},{}"'.format(action, print_automation)}

        # Check if help about automation actions
        if action == 'help':
            print (self.cfg['info_cli'])

            import types

            print ('')
            print ('Automation actions:')
            print ('')

            for d in sorted(dir(initialized_automation)):
                if type(getattr(initialized_automation, d))==types.MethodType and not d.startswith('_'):
                    print ('* '+d)

            return {'return':0, 'warning':'no automation action'}

        
        # Check if help for a given automation action
        if cm_help:
            # Find path to automation

            import inspect
            path_to_automation = inspect.getfile(inspect.getmodule(initialized_automation))

            print ('')
            print ('Automation:      {}'.format(print_automation))
            print ('Action:          {}'.format(action))
            print ('')
            print ('Automation path: {}:'.format(path_to_automation))
            print ('')

            print ('API:')
            print ('')

            r=utils.find_api(path_to_automation, original_action)
            if r['return']>0: return r

            api = r['api']

            print (api)
            
            return {'return':0, 'help':api}

        # Process artifacts for this automation action
        artifacts = i.get('artifacts',[])
        if len(artifacts)>0:
            parsed_artifacts = []

            for artifact in artifacts:
                # Parse artifact
                r = utils.parse_cm_object(artifact)
                if r['return'] >0 : return r

                parsed_artifacts.append(r['cm_object'])

            i['parsed_artifacts'] = parsed_artifacts

        # Check artifact and artifacts
        artifact = i.get('artifact','')
        if artifact != '':
            # Parse artifact
            r = utils.parse_cm_object(artifact)
            if r['return'] >0 : return r

            i['parsed_artifact'] = r['cm_object']

        # Call automation action
        action_addr=getattr(initialized_automation, action)

#        import json
#        print ('')
#        print (json.dumps(i, indent=2))    
#        print ('')        
#        
        r = action_addr(i)

        if r['return']>0 and console:
            error(r)

        return r
