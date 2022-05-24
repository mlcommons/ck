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
    Main CM class
    """

    ############################################################
    def __init__(self, repos_path = '', debug = False):
        """
        Initialize CM configuration class

        Args:
            (repos_path) (str) - path to CM repositories and other information.
            (debug) (bool) - if True, raise errors in internal functions 
                             instead of returning a dictionary with "return">0.

        Returns:
            (python class) with the following vars:

            * cfg (dict): internal CM configuration
            * debug (bool): debug state

            * repos_path (str): path to CM repositories and other information

            * path_to_cmind (str): path to the used CM toolkit
            * path_to_cmind_core_module (str): path to CM core module
            * path_to_cmind_repo (str): path to the "internal" CM repo

            * repos (list): list of initialized CM repository objects
            
            * common_automation (Automation class): initialized common automation with actions when a given automation is not found or doesn't exist

            * output (str): value of --out during the first access to CM (to print errors, etc)

        """

        # Initialize and update CM configuration
        self.cfg = Config().cfg

        # Check if debug (raise error instead of soft error)
        self.debug = False
        if debug or os.environ.get(self.cfg['env_debug'],'').strip().lower()=='yes':
            self.debug = True

        # Explicit path to direcory with CM repositories and other internals
        self.repos_path = repos_path
        if self.repos_path == '':
            s = os.environ.get(self.cfg['env_repos'],'').strip()
            if s != '':
                self.repos_path = s

        if self.repos_path == '':
           from os.path import expanduser
           self.repos_path = os.path.join(expanduser("~"), self.cfg['default_home_dir'])

        path_to_cmind = os.environ.get(self.cfg['env_home'],'').strip()
        if path_to_cmind != '':
            self.path_to_cmind = path_to_cmind
            self.path_to_cmind_core_module = os.path.join(self.path_to_cmind, 'core.py')
        else:
            self.path_to_cmind_core_module = inspect.getfile(inspect.currentframe())
            self.path_to_cmind = os.path.dirname(self.path_to_cmind_core_module)

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
        If r['return']>0: print CM error and raise error if in debugging mode

        Args:
           r (dict): output from CM function with "return" and "error"
               
        Returns:
           (dict): r

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
        If r['return']>0: print CM error and raise error if in debugging mode or halt with "return" code

        Args:
           r (dict): output from CM function with "return" and "error"
               
        Returns:
           (dict): r
        """

        # Force console
        self.error(r)
        
        sys.exit(r['return'])

    ############################################################
    def access(self, i, out = None):
        """
        Access CM automation actions in a unified way similar to micro-services.

        i (dict | str | argv): unified CM input

        Args:
            (action) (str): automation action
            (automation (CM object): CM automation in format (alias | UID | alias,UID) 
                                       or (repo alias | repo UID | repo alias,UID):(alias | UID | alias,UID) 
            (artifact) (CM object): CM artifact
            (artifacts) (list of CM objects): extra CM artifacts

            (common) (bool): if True, use common automation action from Automation class

            (help) (bool): if True, print CM automation action API

            (ignore_inheritance) (bool): if True, ignore inheritance when searching for artifacts and automations
            
            (out) (str): if 'out', tell automations and CM to output extra information to console

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

            * Output from a CM automation action
        
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
                   print_db_actions(self.common_automation, self.cfg['action_substitutions'])
                   
            return {'return':0, 'warning':'no action'}

        # Load info about all CM repositories (to enable search for automations and artifacts)
        if self.repos == None:
            repos = Repos(path = self.repos_path, cfg = self.cfg, 
                          path_to_internal_repo = self.path_to_cmind_repo)

            r = repos.load()
            if r['return'] >0 : return r

            # Set only after all initializations
            self.repos = repos

        # Check if forced common automation
        use_common_automation = True if i.get('common',False) else False

        automation_lst = []
        use_any_action = False

        artifact = i.get('artifact','').strip()
        artifacts = i.get('artifacts',[]) # Only if more than 1 artifact
                                          # First element is == artifact

        # Check if automation is "." - then attempt to detect repo, automation and artifact from the current directory
        if automation == '' or automation == '.':
            r = self.access({'action':'detect',
                             'automation':'repo,55c3e27e8a140e48'})
            if r['return']>0: return r

            # Check and substitute automation
            automation = ''
            if r.get('artifact_found', False):
                if not r.get('found_in_current_path',False):
                    # If not in the root directory (otherwise search through all automations)
                    automation = r['cm_automation']

            # Check and make an artifact (only if artifacts are not specified)
            if r.get('artifact_found_in_current_path', False) and artifact == '' and i.get('tags','') == '':
                artifact = r['cm_artifact']

            if r.get('registered', False):
                cm_repo = r['cm_repo']

                if ':' not in artifact:
                   artifact = cm_repo + ':' + artifact
   
                for ia in range(0,len(artifacts)):
                    a = artifacts[ia]
                    if ':' not in a:
                        a = cm_repo + ':' + a
                        artifacts[ia] = a

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
                ii={'parsed_automation':[('automation','bbeb15d8f0a944a4')],
                    'parsed_artifact':parsed_automation}
                # Ignore inheritance when called recursively
                if i.get('ignore_inheritance',False):
                   ii['ignore_inheritance']=True 
                r = self.common_automation.search(ii)
                if r['return']>0: return r
                automation_lst = r['list']

                if len(automation_lst)==1:
                    automation = automation_lst[0]
                    
                    automation_path = automation.path
                    automation_name = self.cfg['common_automation_module_name']
                    automation_meta = automation.meta

                    use_any_action = automation_meta.get('use_any_action',False)
                    
                    # Update parsed_automation with UID and alias
                    parsed_automation[0] = (automation_meta.get('alias',''),
                                            automation_meta.get('uid',''))
                    
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

            print ('')
            print ('Automation python module: {}'.format(automation_full_path))

            r = print_db_actions(self.common_automation, self.cfg['action_substitutions'])
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
            if r['return']>0: 
                if r['return']==16:
                    # Check in default automation
                    path_to_common_automation = inspect.getfile(inspect.getmodule(self.common_automation))
                    if path_to_common_automation == path_to_automation:
                        return r

                    r=utils.find_api(path_to_common_automation, original_action)
                    if r['return']>0: return r

            api = r['api']

            print (api)
            
            return {'return':0, 'help':api}

        # Process artifacts for this automation action
        if len(artifacts)>0:
            parsed_artifacts = []

            for extra_artifact in artifacts:
                # Parse artifact
                r = parse_cm_object_and_check_current_dir(self, extra_artifact)
                if r['return'] >0 : return r

                parsed_artifacts.append(r['cm_object'])

            i['parsed_artifacts'] = parsed_artifacts

        # Check artifact and artifacts
        if artifact != '':
            # Parse artifact
            r = parse_cm_object_and_check_current_dir(self, artifact)
            if r['return'] >0 : return r

            i['parsed_artifact'] = r['cm_object']

        # Call automation action
        action_addr=getattr(initialized_automation, action)

        r = action_addr(i)

        return r

############################################################
def parse_cm_object_and_check_current_dir(cmind, artifact):
    """
    Internal function: parses CM object and check if there is '.' 
    to detect CM repository in a current directory.

    """

    if artifact.startswith('.:'):

        r = cmind.access({'action':'detect',
                       'automation':'repo,55c3e27e8a140e48'})
        if r['return']>0: return r

        if r.get('registered', False):
            cm_repo = r['cm_repo']

            artifact = cm_repo + artifact[1:]
    
    return utils.parse_cm_object(artifact)

############################################################
def print_db_actions(automation, equivalent_actions):

    """
    Internal function: prints CM database actions.

    """

    import types

    print ('')
    print ('Collective database actions:')
    print ('')

    db_actions=[]

    for d in sorted(dir(automation)):
        if type(getattr(automation, d))==types.MethodType and not d.startswith('_'):
            
            db_actions.append(d)

            s = d
            se = ''

            # Check equivalent actions
            for k in sorted(equivalent_actions.keys()):
                v = equivalent_actions[k]

                if v==d:
                    if se!='': se+=', '
                    se+=k

                    db_actions.append(k)

            if se!='':
                s+=' (' + se + ')'

            print ('  * ' + s)

    return {'return':0, 'db_actions':db_actions}


############################################################
def access(i):
    """
    Automatically initialize CM and run automations 
    without the need to initialize and customize CM class.
    Useful for Python automation scripts.

    See CM.access function for more details.
    """

    global cm

    if cm is None:
       cm=CM()

    return cm.access(i)

############################################################
def error(i):
    """
    Automatically initialize CM and print error if needed
    without the need to initialize and customize CM class.
    Useful for Python automation scripts.

    See CM.error function for more details.
    """

    return cm.error(i)

############################################################
def halt(i):
    """
    Automatically initialize CM, print error and halt if needed
    without the need to initialize and customize CM class.
    Useful for Python automation scripts.

    See CM.halt function for more details.

    """

    return cm.halt(i)

############################################################
def get_version():
    """
    Get CM version.

    Args:

    Returns: 
        (CM return dict):

        * return (int): return code == 0 if no error and >0 if error
        * (error) (str): error string if return>0

        * version (str): CM version
    """

    r = {'return':0}

    import cmind
    version = cmind.__version__
    r['version'] = version

    return r
