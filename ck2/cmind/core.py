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

        # Common automation
        self.common_automation = None

        # Output of the first access
        self.output = None

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
    def access_from_cli(self, i):
        """
        Access from CLI and print error if needed
        """

        r = self.access(i, out='con')

        if r['return']>0:
            if (self.output is None and out) or self.output=='con':
                self.error(r)
        
        return r

    ############################################################
    def access(self, i, out = None):
        """
        Access customized Collective Mind object

        Args:
            i (dict | str | argv): CM input
            out (str) - =='con' -> force output to console

            (common) (bool) - if True force common automation action

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

        # Parse as command line if string or list
        if type(i) == str or type(i) == list:
            import cmind.cli
            
            r = cmind.cli.parse(i)
            if r['return'] >0 : return r

            i = r['cm_input']

        # Check if force out programmatically (such as from CLI)
        if 'out' not in i and out is not None:
            i['out'] = out

        output = i.get('out','')
        
        # Set self.output to the output of the very first access 
        # to print error in the end if needed
        if self.output is None:
            self.output = output

        # Check if console
        console = (output == 'con')

        # Check if has help flag
        cm_help = i.get(self.cfg['flag_help'], False) or i.get(self.cfg['flag_help2'], False)
        
        # Initialized common automation with collective database actions
        if self.common_automation == None:
           self.common_automation = Automation(self, __file__)

        # Check automation action
        action = i.get('action','')

        # Check automation
        automation = i.get('automation','')

        # Print basic help if action == ''
        extra_help = True if action == 'help' and automation =='' else False
        
        if action == '' or extra_help:
            if console:
                print (self.cfg['info_cli'])

                if cm_help or extra_help:
                   print_db_actions(self.common_automation)
                   
            return {'return':0, 'warning':'no action'}


        # Load info about all CM repositories (to enable search for automations and artifacts)
        if self.repos == None:
            repos = Repos(path = self.home_path, cfg = self.cfg, 
                          path_to_internal_repo = self.path_to_cmind_repo)

            r = repos.load()
            if r['return'] >0 : return r

            # Set only after all initializations
            self.repos = repos

        # Check if forced common automation
        use_common_automation = True if i.get('common',False) else False

        automation_lst = []
        use_any_action = False
        
        # If automation!='', attempt to find it and load
        # Otherwise use the common automation
        if automation != '' and not use_common_automation:
            # Parse automation potentially with a repository
            # and convert it into CM object [(artifact,UID) (,(repo,UID))]
            r = utils.parse_cm_object(automation)
            if r['return'] >0 : return r

            parsed_automation = r['cm_object']
            i['parsed_automation'] = parsed_automation

            # If wildcards in automation, use the common one (usually for search across different automations)
            # However, still need above "parse_automation" for proper search
            if '*' in automation or '?' in automation:
                use_common_automation = True
            else:
                # First object in a list is an automation
                # Second optional object in a list is a repo
                auto_name = parsed_automation[0] if len(parsed_automation)>0 else ('','')
                auto_repo = parsed_automation[1] if len(parsed_automation)>1 else None


                # Search for automations in repos (local, internal, other) TBD: maybe should be local, other, internal?
                r = self.common_automation.search({'parsed_automation':[('automation','bbeb15d8f0a944a4')],
                                                   'parsed_artifact':parsed_automation})
                if r['return']>0: return r
                automation_lst = r['list']

                if len(automation_lst)==1:
                    automation = automation_lst[0]
                    
                    automation_path = automation.path
                    automation_name = self.cfg['common_automation_module_name']
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
                
        # If no automation was found or we force common automation
        if use_common_automation or len(automation_lst)==0:
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
        
        print_automation = automation_meta.get('alias','') + ',' + automation_meta.get('uid','')
        
        # Check if help about automation actions
        if action == 'help':
            import types
            
            print (self.cfg['info_cli'])

            r = print_db_actions(self.common_automation)
            if r['return']>0: return r

            db_actions = r['db_actions']


            actions = []
            for d in sorted(dir(initialized_automation)):
                if d not in db_actions and type(getattr(initialized_automation, d))==types.MethodType and not d.startswith('_'):
                    actions.append(d)

            if len(actions)>0:
                print ('')
                print ('Automation actions:')
                print ('')

                for d in actions:
                    print ('* '+d)

            return {'return':0, 'warning':'no automation action'}

        # Check if action exists
        if not hasattr(initialized_automation, action):
            return {'return':4, 'error':'action "{}" not found in automation "{}"'.format(action, print_automation)}
        
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

        return r

############################################################
def print_db_actions(automation):

    import types

    print ('')
    print ('Collective database actions:')
    print ('')

    db_actions=[]

    for d in sorted(dir(automation)):
        if type(getattr(automation, d))==types.MethodType and not d.startswith('_'):

            db_actions.append(d)

            print ('  * '+d)

    return {'return':0, 'db_actions':db_actions}


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
def get_version(skip_check_status = False):
    """
    Get version and check status
    """

    r = {'return':0}

    import cmind
    version = cmind.__version__
    r['version'] = version

    return r
