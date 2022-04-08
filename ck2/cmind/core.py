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

    # Force console
    con_tmp = cm.con

    cm.con=True

    r = cm.error(i)

    cm.con = con_tmp

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
    def __init__(self, home_path = '', debug = False, out = ''):
        """
        Initialize Collective Mind class
        """

#        print ('************************************************')
#        print ('Initialize CM ...')
#        print ('************************************************')

        # Check output (for now support con but can be json or file, etc)
        self.out = out
        self.con = False
        if out == 'con':
            self.con = True

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

        for key in ['automation', 'action']:
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

            if self.con:
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
        self.con=True

        self.error(r)
        
        sys.exit(r['return'])

    ############################################################
    def access(self, i):
        """
        Access customized Collective Mind object

        Args:
            i (dict | str | argv): CM input
        
        Returns:
            Dictionary:
                return (int): return code == 0 if no error 
                                          >0 if error

                (error) (str): error string if return>0

                data from a given action
        
        """

        # Pass to internal access
        r = self.internal_access(i)

        return r

    
    ############################################################
    def internal_access(self, i):
        """
        Access customized Collective Mind object

        Args:
            i (dict | str | argv): CM input

               default (bool) - if True, call default automation without any specialization
                                (usually for pure CM database actions)

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

        # Check CM flag for CM output
        if self.cfg['flag_out'] in i:
           self.out = i[self.cfg['flag_out']]

           if self.out == 'con':
               self.con = True
        
        # Check if has help flag
        cm_help = i.get(self.cfg['flag_help'], False) or i.get(self.cfg['flag_help2'], False)
        
        # Initialized default module
        if self.default_automation == None:
           self.default_automation = Automation(self, __file__)
        
        # Check automation
        automation = i.get('automation','')
        if automation == '': automation = i.get('a','')

        if automation == '':
            if self.con:
                print (self.cfg['info_cli'])

                if cm_help:
                   print ('')
                   print ('Collective database actions for this artifact:')
                   print ('')

                   for d in sorted(dir(self.default_automation)):
                       if not d.startswith('_') and d not in ['cmind']:
                           print ('* '+d)

            return {'return':0, 'help':'help about database actions'}

        # Check if general help
        r = utils.parse_cm_object(automation)
        if r['return'] >0 : return r

        # A list of CM objects
        parsed_automation = r['cm_object']

        i['parsed_automation'] = parsed_automation

        # First object in a list is an automation
        # Second optional object in a list is a repo
        auto_name = parsed_automation[0] if len(parsed_automation)>0 else ('','')
        auto_repo = parsed_automation[1] if len(parsed_automation)>1 else None

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

        # Load repositories
        if self.repos == None:
            repos = Repos(path = self.home_path, cfg = self.cfg, 
                          path_to_default_repo = self.path_to_cmind_repo)

            r = repos.load()
            if r['return'] >0 : return r

            # Set only after all initializations
            self.repos = repos

        # Find automation 
        # TBD: need to move order to configuration

        # Search for automation in CM repositories
        automation_lst = []

        use_default_automation = True if i.get('default',False) else False

        use_any_func = False

        if not use_default_automation:
            # Search for automations in repos (local, default, other) TBD: maybe should be local, other, default?
            r = self.default_automation.search({'parsed_automation':[('automation','bbeb15d8f0a944a4')],
                                            'parsed_artifact':parsed_automation,
                                            'skip_con':True})
            if r['return']>0: return r
            automation_lst = r['list']

            if len(automation_lst)==1:
                automation = automation_lst[0]
                
                automation_path = automation.path
                automation_name = self.cfg['default_automation_module_name']
                automation_meta = automation.meta

                use_any_func = automation_meta.get('use_any_func',False)
                
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
                
        if use_default_automation or len(automation_lst)==0:
            # TBD: work for basic functions even if automation is not installed
            # Maybe should be something else (internal keyword that can't be used)
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

        # Check automation action
        action = i.get('action','')

        if action == '':
            if self.con:
                print ('')
                print ('Collective database actions:')
                print ('')

                database_actions=dir(self.default_automation)
                
                for d in sorted(database_actions):
                    if not d.startswith('_') and d not in ['automation_path', 'path', 'cmind']:
                        x = '* '+d

                        if d in self.cfg['action_substitutions_reverse']:
                            x += ' ('+', '.join(self.cfg['action_substitutions_reverse'][d])+')'

                        print (x)
                
                print ('')
                print ('Automation actions:')
                print ('')

                for d in sorted(dir(initialized_automation)):
                    if not d.startswith('_') and d not in ['cmind', 'meta'] and d not in database_actions:
                        print ('* '+d)

                return {'return':0, 'help':''}

        # Convert action into function (substitute internal words)
        func = action.replace('-','_')

        if func in self.cfg['action_substitutions']:
            func = self.cfg['action_substitutions'][func]
        
        # Check func in a class when importing
        if use_any_func:
            func = 'any'
        
        if not hasattr(initialized_automation, func):
            return {'return':4, 'error':'action "{}" not found in automation {}'.format(func, auto_name)}

        # Check if help for automation
        if cm_help:
            print ('')
            print ('Action help:')
            print ('')

            import inspect
            path_to_automation = inspect.getfile(inspect.getmodule(initialized_automation))
            print ('(path: {})'.format(path_to_automation))

            print ('')
            print ('TBD')

            return {'return':0}

        # Call automation action
        func_addr=getattr(initialized_automation, func)
        r = func_addr(i)

        return r
