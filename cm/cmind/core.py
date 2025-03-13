# Collective Mind core functions
#
# Author(s): Grigori Fursin
# Contributor(s):
#
# Copyright: https://github.com/mlcommons/ck/blob/master/COPYRIGHT.txt
# License: https://github.com/mlcommons/ck/blob/master/LICENSE.md
# History: https://github.com/mlcommons/ck/blob/master/HISTORY.CM.md
# White paper: https://arxiv.org/abs/2406.16791
# Project contributors: https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md

from cmind.config import Config
from cmind.repos import Repos
from cmind.index import Index
from cmind.automation import Automation
#from cmind.automation import AutomationDummy
from cmind import utils

import sys
import os
#    Outdated in Python 3.12+
#import imp
import importlib
import pkgutil
import inspect
import logging

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
        if debug or os.environ.get(self.cfg['env_debug'],'').strip().lower() in ['yes','on','true']:
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

        # Check Python version
        self.python_version = list(sys.version_info)

        # Save output to json or yaml(only from CLI)
        self.save_to_json = ''
        self.save_to_yaml = ''

        # Logging
        self.logger = None
        self.xlogger = None

        # Index
        self.index = None

        self.use_index = True
        if os.environ.get(self.cfg['env_index'],'').strip().lower() in ['no','off','false']:
            self.use_index = False

        # Check if CM v3+ was called (to avoid mixing up older versions and make them co-exist)
        self.x_was_called = False

        # Misc state 
        self.state = {}

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

            text = self.cfg['error_prefix'] + ' ' + r['error'] + '!\n'

            sys.stderr.write(f'\n{text}')

        return r

    ############################################################
    def errorx(self, r):
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

            if 'warning' in r:
                message = r.get('warning', '')
                if message != '':
                    message = message[0].upper() + message[1:]
                    message = '\nCMX warning: ' + message + '!\n'
            else:
                module_path = r.get('module_path', '')
                lineno = r.get('lineno', '')

                message = ''

                if not self.xlogger == None or (module_path != '' and lineno != ''):
                    call_stack = self.state.get('call_stack', [])

                    if not self.xlogger == None:

                        self.log(f"x error call stack: {call_stack}", "debug")
                        self.log(f"x error: {r}", "debug")

#                    sys.stderr.write('^'*60 + '\n')
                    sys.stderr.write('\n')

                    if not self.xlogger == None:
                        sys.stderr.write('CMX call stack:\n')

                        for cs in call_stack:
                            sys.stderr.write(f' * {cs}\n')

                        message += '\n'
                else:
                    message += '\n'

                message += self.cfg['error_prefix2']

                if module_path != '' and lineno !='':
                    message += f' while running automation {module_path} ({lineno}):\n\n'
                    text = r['error']
                    text = text[0].upper() + text[1:]

                else:
                    message += ': '
                    text = r['error']

                if not text.endswith('!'): text += '!'

                message += text + '\n'

            sys.stderr.write(message)

        return r

    ############################################################
    def prepare_error(self, returncode, error):
        """
        Prepare error dictionary with the module and line number of an error

        Args:
           returncode (int): CMX returncode
           error (str): error message

        Returns:
           (dict): r
              return (int)
              error (str)
              module_path (str): path to module
              lineno (int): line number

        """

        from inspect import getframeinfo, stack

        caller = getframeinfo(stack()[1][0])

        return {'return': returncode,
                'error': error,
                'module_path': caller.filename,
                'lineno': caller.lineno}

    ############################################################
    def embed_error(self, r):
        """
        Embed module and line number to an error

        Args:
           r (dict): CM return dict

        Returns:
           (dict): r
              return (int)
              error (str)
              module_path (str): path to module
              lineno (int): line number

        """

        from inspect import getframeinfo, stack

        caller = getframeinfo(stack()[1][0])

        r['module_path'] = caller.filename
        r['lineno'] = caller.lineno

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
    def log(self, s, t = 'info'):
        """
        Args:
           s (str): log string
           t (str): log type - "info" (default)
                               "debug"
                               "warning"
                               "error"

        Returns:
           None
        """

        logger = self.xlogger

        if logger != None:
            if t == 'debug':
                logger.debug(s)
            elif t == 'warning':
                logger.warning(s)
            elif t == 'error':
                logger.error(s)
            # info
            else:
                logger.info(s)

        return


    ############################################################
    def access(self, i, out = None):
        """
        Access CM automation actions in a unified way similar to micro-services.
        (Legacy. Further development in the new "x" function).

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

            (out) (str): if 'con', tell automations and CM to output extra information to console

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

        # Check if log
        if self.logger is None:
            self.logger = logging.getLogger("cm")

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

        # Check if save to json
        if 'save_to_json' in i and i['save_to_json']!='':
            self.save_to_json = i['save_to_json']

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

        # Check if asked for "version" and no automation
        if action == 'version' and automation == '':
            automation = 'core'
        elif action == '' and automation == '' and i.get('version',False):
            action = 'version'
            automation = 'core'
        elif action == 'init' and automation == '':
            automation = 'core'


        # Print basic help if action == ''
        extra_help = True if action == 'help' and automation == '' else False

        if action == '' or extra_help:
            if console:
                print (self.cfg['info_cli'])

                if cm_help or extra_help:
                   print_db_actions(self.common_automation, self.cfg['action_substitutions'], '')

            return {'return':0, 'warning':'no action specified'}

        # Load info about all CM repositories (to enable search for automations and artifacts)
        if self.repos == None:
            repos = Repos(path = self.repos_path, cfg = self.cfg, 
                          path_to_internal_repo = self.path_to_cmind_repo)

            r = repos.load()
            if r['return'] >0 : return r

            # Set only after all initializations
            self.repos = repos

        # Load index
        if self.index is None:
            self.index = Index(self.repos_path, self.cfg)

            if self.use_index:
                r = self.index.load()
                if r['return']>0: return r

                if not r['exists']:
                    # First time
                    if console:
                        print ('Warning: CM index is used for the first time. CM will reindex all artifacts now - it may take some time ...')

                    r = self.access({'action':'reindex',
                                     'automation':'repo,55c3e27e8a140e48'})
                    if r['return']>0: return r

        # Check if forced common automation
        use_common_automation = True if i.get('common',False) else False

        automation_lst = []
        use_any_action = False

        artifact = i.get('artifact','').strip()
        artifacts = i.get('artifacts',[]) # Only if more than 1 artifact

        # Check if automation is "." - then attempt to detect repo, automation and artifact from the current directory
        if automation == '.' or artifact == '.':
            r = self.access({'action':'detect',
                             'automation':'repo,55c3e27e8a140e48'})
            if r['return']>0: return r

            # Check and substitute automation
            if automation == '.':
                automation = ''
                if r.get('artifact_found', False):
                    if not r.get('found_in_current_path',False):
                        # If not in the root directory (otherwise search through all automations)
                        automation = r['cm_automation']

            # Check and make an artifact (only if artifacts are not specified)
            if artifact == '.' or artifact == '':
                artifact = ''
                if r.get('cm_artifact','')!='':
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
        if automation != '':
            # Parse automation potentially with a repository
            # and convert it into CM object [(artifact,UID) (,(repo,UID))]
            r = utils.parse_cm_object(automation)
            if r['return'] >0 : return r

            parsed_automation = r['cm_object']
            i['parsed_automation'] = parsed_automation

            if use_common_automation:
                # Check that UID is set otherwise don't know how to add
                xuid=parsed_automation[0][1]
                if xuid == '':
                    return {'return':1, 'error':'you must add `,CM UID` for automation {} when using --common'.format(parsed_automation[0][0])}
                elif not utils.is_cm_uid(xuid):
                    return {'return':1, 'error':'you must use CM UID after automation {} when using --common'.format(parsed_automation[0][0])}
                    
        automation_meta = {}
        
        if automation != '' and not use_common_automation:
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

                    # Find Python module for this automation: should also work with 3.12+
                    automation_full_path = os.path.join(automation_path, automation_name + '.py')

                    if not os.path.isfile(automation_full_path):
                        return {'return': 1, 'error': 'can\'t find Python module file {}'.format(automation_full_path)}
                    
#                    Oudated
#                    try:
#                        found_automation = imp.find_module(automation_name, [automation_path])
#                    except ImportError as e:  # pragma: no cover
#                        return {'return': 1, 'error': 'can\'t find Python module code (path={}, name={}, err={})'.format(automation_path, automation_name, format(e))}

                    found_automation_spec = importlib.util.spec_from_file_location(automation_name, automation_full_path)
                    if found_automation_spec == None:
                        return {'return': 1, 'error': 'can\'t find Python module file {}'.format(automation_full_path)}

#                    Outdated
#                    automation_handler = found_automation[0]

                    # Generate uid for the run-time extension of the loaded Python module
                    # otherwise Python modules with the same extension (key.py for example)
                    # will be reloaded ...

#                    r = utils.gen_uid()
#                    if r['return'] > 0: return r
#                    automation_run_time_uid = 'rt-'+r['uid']

                    try:
#                       Outdated
#                       loaded_automation = imp.load_module(automation_run_time_uid, automation_handler, automation_full_path, found_automation[2])
                       loaded_automation = importlib.util.module_from_spec(found_automation_spec)
                       found_automation_spec.loader.exec_module(loaded_automation)
                    except Exception as e:  # pragma: no cover
                        return {'return': 1, 'error': 'can\'t load Python module code (path={}, name={}, err={})'.format(automation_path, automation_name, format(e))}

#                    Outdated
#                    if automation_handler is not None:
#                        automation_handler.close()

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
                    return {'return':3, 'error':'automation was not found in a specified repo {}'.format(auto_repo)}

        # Convert action into function (substitute internal words)
        original_action = action
        action = action.replace('-','_')

        if action in self.cfg['action_substitutions']:
            action = self.cfg['action_substitutions'][action]
        elif action in automation_meta.get('action_substitutions',{}):
            action = automation_meta['action_substitutions'][action]

        # Check if common automation and --help
        if (use_common_automation or automation=='') and cm_help:
            return print_action_help(self.common_automation, 
                                     self.common_automation, 
                                     'common',
                                     action,
                                     original_action)

        # If no automation was found we do not force common automation, check if should fail or continue
        if not use_common_automation and len(automation_lst)==0:
            if self.cfg['fail_if_automation_not_found']:
                # Quit with error
                if automation=='':
                    return {'return':4, 'error':'automation was not specified'}
                else:
                    return {'return':4, 'error':'automation "{}" not found'.format(automation)}

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
        initialized_automation.full_path = automation_full_path

        # Check action in a class when importing
        if use_any_action:
            action = 'any'

        print_automation = automation_meta.get('alias','') + ',' + automation_meta.get('uid','')
        initialized_automation.artfact = print_automation

        # Check if help about automation actions
        if action == 'help':
            import types

            print (self.cfg['info_cli'])

            print ('')
            print ('Automation python module: {}'.format(automation_full_path))

            r = print_db_actions(self.common_automation, self.cfg['action_substitutions'], automation_meta.get('alias',''))
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
                    print ('  * cm  ' + d + '  ' + automation_meta.get('alias',''))

            return {'return':0, 'warning':'no automation action'}

        # Check if action exists
        if not hasattr(initialized_automation, action):
            return {'return':4, 'error':'action "{}" not found in automation "{}"'.format(action, print_automation)}

        # Check if help for a given automation action
        delayed_help = False
        delayed_help_api = ''
        delayed_help_api_prefix = ''
        delayed_help_api_prefix_0 = ''

        if cm_help:
            # Find path to automation
            rr = print_action_help(initialized_automation, 
                                   self.common_automation, 
                                   print_automation,
                                   action, 
                                   original_action)

            if rr['return']>0: return rr

            if not rr.get('delayed_help', False):
                return rr

            delayed_help = True
            delayed_help_api = rr['help']
            delayed_help_api_prefix = rr['help_prefix']
            delayed_help_api_prefix_0 = rr['help_prefix_0']

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

        # Check min CM version requirement
        min_cm_version = automation_meta.get('min_cm_version','').strip()
        if min_cm_version != '':
            from cmind import __version__ as current_cm_version
            comparison = utils.compare_versions(current_cm_version, min_cm_version)
            if comparison < 0:
                return {'return':1, 'error':'CM automation requires CM version >= {} while current CM version is {} - please update using "pip install cmind -U"'.format(min_cm_version, current_cm_version)}



        # Call automation action
        action_addr=getattr(initialized_automation, action)

        r = action_addr(i)

        # Check if need to save index
        if self.use_index and self.index.updated:
            rx = self.index.save()
            # Ignore output for now to continue working even if issues ...

            self.index.updated=False

        # If delayed help
        if delayed_help and not r.get('skip_delayed_help', False):
            print ('')
            print (delayed_help_api_prefix_0)
            print ('')
            print (delayed_help_api_prefix)
            print ('')
            print (delayed_help_api)
        
        return r

    ############################################################
    def x(self, i, out = None):
        """
        New unified access to CM automation actions

        Args:
          i (dict | str | argv): unified CM input

            * (action) (str): automation action
            * (automation (CM object): CM automation in format (alias | UID | alias,UID) 
                                       or (repo alias | repo UID | repo alias,UID):(alias | UID | alias,UID) 
            * (artifact) (CM object): CM artifact
            * (artifacts) (list of CM objects): extra CM artifacts


            Control flags starting with - :

            * (out) (str): if 'con', tell automations and CM to output extra information to console

            * (common) (bool): if True, use common automation action from Automation class

            * (help) (bool): if True, print CM automation action API

            * (ignore_inheritance) (bool): if True, ignore inheritance when searching for artifacts and automations


        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

            * Output from a given CM automation action
        """

        import copy

        # Check if very first access call
        x_was_called = self.x_was_called
        self.x_was_called = True

        cur_dir = os.getcwd()

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

            r = cmind.cli.parsex(i)
            if r['return'] >0 : return r

            i = r['cmx_input']

        # Assemble input flags for extra checks in automations
        if 'control' not in i:
           i['control'] = {}

        i['control']['_input'] = {}

        for k in i:
            if k not in ['control', 'action', 'automation', 'artifact', 'artifacts']:
                i['control']['_input'][k] = i[k]
            
        control = i['control']

        # Expose only control flags
        control_flags = {}
        for flag in control:
            if not flag.startswith('_'):
                control_flags[flag] = control[flag]

        # Check if unknown flags
        # f should be deprecated in the future - used for backwards
        # compatibility with older commands like cm/cmx rm cache -f

        unknown_control_flags = [flag for flag in control_flags if flag not in [
          'h', 'help', 'v', 'version', 'out', 'j', 'json', 
          'save_to_json_file', 'save_to_yaml_file', 'common', 
          'ignore_inheritance', 'log', 'logfile', 'raise', 'repro',
          'i', 'f', 'time', 'profile']]

        delayed_error = ''
        
        if len(unknown_control_flags)>0:
            unknown_control_flags_str = ','.join(unknown_control_flags)

            delayed_error = f'Unknown control flag(s): {unknown_control_flags_str}'

            # Force print help
            control['h'] = True

        if control.pop('f', ''):
            i['f'] = True

        output_json = (control.get('j', False) or control.get('json', False))

        self_time = control.get('time', False)
        if not x_was_called and self_time:
            import time
            self_time1 = time.time()

        self_profile = control.get('profile', False)

        self_info = control.get('i', False)

        # Check repro
        use_log = str(control_flags.pop('log', '')).strip().lower()
        log_file = control_flags.pop('logfile', '')

        if control.get('repro', '') != '':
            if not os.path.isdir('cmx-repro'):
                os.mkdir('cmx-repro')

            if log_file == '':
                log_file = os.path.join(cur_dir, 'cmx-repro', 'cmx.log')
            if use_log == '':
                use_log = 'debug'

            ii = copy.deepcopy(i)
            ii['control'] = {}
            for k in control:
                if not k.startswith('_') and k not in ['repro']:
                    ii['control'][k] = control[k]

            utils.save_json(os.path.join('cmx-repro', 'cmx-input.json'), 
                            meta = ii)

        # Check logging
        if self.xlogger is None:
            log_level = None

            if use_log == "false": 
                use_log = ''
            elif use_log == "true": 
                use_log = 'info'

            if log_file == '': 
                log_file = None
            else:
                if use_log == '':
                    use_log = 'debug'

            if use_log != '':
                if use_log == 'debug':
                    log_level = logging.DEBUG
                elif use_log == 'warning':
                    log_level = logging.WARNING
                elif use_log == 'error':
                    log_level = logging.ERROR
                else:
                    # info by default
                    log_level = logging.INFO

                # Configure
                self.xlogger = logging.getLogger("cmx")
                logging.basicConfig(filename = log_file, filemode = 'w', level = log_level)

        # Check if force out programmatically (such as from CLI)
        if 'out' not in control and out is not None:
            control['out'] = out

        use_raise = control.get('raise', False)

        # Log access
        recursion = self.state.get('recursion', 0)
        self.state['recursion'] = recursion + 1

        if not self.xlogger == None:
            log_action = i.get('action', '')
            log_automation = i.get('automation', '')
            log_artifact = i.get('artifact', '')

            spaces = ' ' * recursion

            self.log(f"x log: {spaces} {log_action} {log_automation} {log_artifact}", "info")
            self.log(f"x input: {spaces} ({i})", "debug")

        # Call access helper
        if not x_was_called and self_info:
            utils.get_memory_use(True)
            print ('')
            utils.get_disk_use('/', True)
            print ('')


        if not x_was_called and self_profile:
            # https://docs.python.org/3/library/profile.html#module-cProfile
            import cProfile, pstats, io
            from pstats import SortKey
            profile = cProfile.Profile()
            profile.enable()

        r = self._x(i, control)

        if delayed_error != '' and r['return'] == 0:
            r['return'] = 1
            r['error'] = delayed_error

        if not self.xlogger == None:
            self.log(f"x output: {r}", "debug")

        self.state['recursion'] = recursion

        if not x_was_called:
            if self_profile:
                profile.disable()
                s = io.StringIO()
                sortby = SortKey.CUMULATIVE
                ps = pstats.Stats(profile, stream=s).sort_stats(sortby)
                ps.print_stats(32)
                print ('')
                print ('CMX profile:')
                print ('')
                print (s.getvalue())

            # Very first call (not recursive)
            # Check if output to json and save file

            if self_time:
                self_time = time.time() - self_time1
                r['self_time'] = self_time

                if self.output == 'con':
                    print ('')
                    print ('CMX elapsed time: {:.3f} sec.'.format(self_time))

            if output_json:
               utils.dump_safe_json(r)

            # Restore directory of call
            os.chdir(cur_dir)

            # Check if save to json
            if control.get('save_to_json_file', '') != '':
               utils.save_json(control['save_to_json_file'], meta = r)

            if control.get('save_to_yaml_file', '') != '':
               utils.save_yaml(control['save_to_yaml_file'], meta = r)

            if control.get('repro', '') != '':
                if not os.path.isdir('cmx-repro'):
                    os.mkdir('cmx-repro')
                utils.save_json(os.path.join('cmx-repro', 'cmx-output.json'), 
                                meta = r)

            if r['return'] >0:
                if use_raise:
                    raise Exception(r['error'])

        return r

    ############################################################
    def _x(self, i, control):
        """
        CMX access helper
        """

        output = control.get('out', '')

        if output == True:
            output = 'con'

# Changed in v3.2.5
#        # Check and force json console output
#        if control.get('j', False) or control.get('json', False):
#            output = 'json'

        # Set self.output to the output of the very first access 
        # to print error in the end if needed
        if self.output is None:
            self.output = output

        control['out'] = output

        # Check if console
        console = (output == 'con')

        # Check if has help flag
        cm_help = control.get(self.cfg['flag_help'], False) or control.get(self.cfg['flag_help2'], False)

        # Initialized common automation with collective database actions
        if self.common_automation == None:
           self.common_automation = Automation(self, __file__)

        # Check automation action
        action = i.get('action','')

        # Check automation
        automation = i.get('automation','')

        # Check if asked for "version" and no automation
        if action == 'version' and automation == '':
            automation = 'core'
        elif action == '' and automation == '' and (control.get('version', False) or control.get('v', False) or control.get('_input',{}).get('version', False)):
            action = 'version'
            automation = 'core'
        elif action == 'init' and automation == '':
            automation = 'core'

        # Can add popular shortcuts
        elif action == 'ff':
            task = ''
            if automation != '' and (' ' in automation or ',' in automation):
                task = automation
                if ' ' in automation: task = automation.replace(' ',',')
                i['task'] = task
            automation = 'flex.flow'
            action = 'run'
            i['automation'] = automation
            i['action'] = action

        # Print basic help if action == ''
        extra_help = True if action == 'help' and automation == '' else False

        if action == '' or extra_help:
            if console:
                print (self.cfg['info_clix'])

                if cm_help or extra_help:
                   print_db_actions(self.common_automation, self.cfg['action_substitutions'], '', cmx = True)

                   print ('')
                   print ('Control flags:')
                   print ('')
                   print ('  -h | -help - print this help')
                   print ('  -v | -version - print version')
                   print ('  -out (default) - output to console')
                   print ('  -out=con (default) - output to console')
                   print ('  -j | -json - print output of the automation action to console as JSON')
                   print ('  -save_to_json_file={file} - save output of the automation action to file as JSON')
                   print ('  -save_to_yaml_file={file} - save output of the automation action to file as YAML')
                   print ('  -common - force call default common CMX automation action')
                   print ('  -ignore_inheritance - ignore CMX meta inheritance')
                   print ('  -log - log internal CMX information to console')
                   print ('  -log={info (default) | debug | warning | error} - log level')
                   print ('  -logfile={path to log file} - record log to file instead of console')
                   print ('  -raise - raise Python error when automation action fails')
                   print ('  -time - print elapsed time for a given automation')
                   print ('  -profile - profile a given automation')
                   print ('  -i - print info about available memory and disk space')
                   print ('  -repro - record various info to the cmx-repro directory to replay CMX command')
                   print ('')
                   print ('Check https://github.com/mlcommons/ck/tree/master/cm/docs/cmx for more details.')
                                                                                                  
            return {'return':1, 'warning':'', 'error':'help requested'}

        # Load info about all CM repositories (to enable search for automations and artifacts)
        if self.repos == None:
            repos = Repos(path = self.repos_path, cfg = self.cfg, 
                          path_to_internal_repo = self.path_to_cmind_repo,
                          cmx = True)

            r = repos.load()
            if r['return'] >0 : return r

            # Set only after all initializations
            self.repos = repos

        # Load index
        if self.index is None:
            self.index = Index(self.repos_path, self.cfg)

            if self.use_index:
                r = self.index.load()
                if r['return']>0: return r

                if not r['exists']:
                    # First time
                    if console:
                        print ('Warning: CM index is used for the first time. CM will reindex all artifacts now - it may take some time ...')

                    r = self.access({'action':'reindex',
                                     'automation':'repo,55c3e27e8a140e48'})
                    if r['return']>0: return r

        # Check if forced common automation
        use_common_automation = True if control.get('common', False) else False

        automation_lst = []
        use_any_action = False

        artifact = i.get('artifact', '').strip()
        artifacts = i.get('artifacts', []) # Only if more than 1 artifact

        # Check if automation is "." - then attempt to detect repo, automation and artifact from the current directory
        if automation == '.' or artifact == '.':
            r = self.access({'action':'detect',
                             'automation':'repo,55c3e27e8a140e48'})
            if r['return']>0: return r

            # Check and substitute automation
            if automation == '.':
                automation = ''
                if r.get('artifact_found', False):
                    if not r.get('found_in_current_path',False):
                        # If not in the root directory (otherwise search through all automations)
                        automation = r['cm_automation']

            # Check and make an artifact (only if artifacts are not specified)
            if artifact == '.' or artifact == '':
                artifact = ''
                if r.get('cm_artifact','')!='':
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
        if automation != '':
            # Parse automation potentially with a repository
            # and convert it into CM object [(artifact,UID) (,(repo,UID))]
            r = utils.parse_cm_object(automation)
            if r['return'] >0 : return r

            parsed_automation = r['cm_object']
            control['_parsed_automation'] = parsed_automation

            if use_common_automation:
                # Check that UID is set otherwise don't know how to add
                xuid = parsed_automation[0][1]
                if xuid == '':
                    return {'return':1, 'error':'you must add `,CM UID` for automation {} when using --common'.format(parsed_automation[0][0])}
                elif not utils.is_cm_uid(xuid):
                    return {'return':1, 'error':'you must use CM UID after automation {} when using --common'.format(parsed_automation[0][0])}
                    
        automation_meta = {}
        automation_use_x = True
        automation_found = False

        if automation != '' and not use_common_automation:
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
                if control.get('ignore_inheritance', False):
                   ii['ignore_inheritance'] = True 

                r = self.common_automation.search(ii)
                if r['return']>0: return r

# TBD: Fill in alias automatically from the name in search ...

                automation_lst = r['list']

                if len(automation_lst)==1:
                    automation = automation_lst[0]

                    automation_path = automation.path
                    automation_meta = automation.meta

                    use_any_action = automation_meta.get('use_any_action',False)

                    # Update parsed_automation with UID and alias
                    parsed_automation[0] = (automation_meta.get('alias',''),
                                            automation_meta.get('uid',''))

                    # Find Python module for this automation: should also work with 3.12+
                    found_module = False
                    for automation_name in [self.cfg['common_automation_module_namex'], self.cfg['common_automation_module_name']]:
                        automation_full_path = os.path.join(automation_path, automation_name + '.py')

                        if os.path.isfile(automation_full_path):
                            found_module = True
                            break

                        automation_use_x = False

                    if not found_module:
                        return {'return': 1, 'error': f"can\'t find CM Python module file in \"{automation_path}\""}

                    found_automation_spec = importlib.util.spec_from_file_location(automation_name, automation_full_path)
                    if found_automation_spec == None:
                        return {'return': 1, 'error': 'can\'t find Python module file {}'.format(automation_full_path)}

                    try:
                       loaded_automation = importlib.util.module_from_spec(found_automation_spec)
                       found_automation_spec.loader.exec_module(loaded_automation)
                    except Exception as e:  # pragma: no cover
                        return {'return': 1, 'error': 'can\'t load Python module code (path={}, name={}, err={})'.format(automation_path, automation_name, format(e))}

                    loaded_automation_class = loaded_automation.CAutomation

                    # Try to load meta description
                    automation_path_meta = os.path.join(automation_path, self.cfg['file_cmeta'])

                    r = utils.is_file_json_or_yaml(file_name = automation_path_meta)
                    if r['return']>0: return r

                    if not r['is_file']:
                        return {'return':4, 'error':'automation meta not found in {}'.format(automation_path)}

                    # Load artifact class
                    r = utils.load_yaml_and_json(automation_path_meta)
                    if r['return']>0: return r

                    automation_meta = r['meta']
                    automation_found = True

                elif len(automation_lst)>1:
                    return {'return':2, 'error':'ambiguity because several automations were found for {}'.format(auto_name)}

                # Report an error if a repo is specified for a given automation action but it's not found there
                if len(automation_lst)==0 and auto_repo is not None:
                    return {'return':3, 'error':'automation was not found in a specified repo {}'.format(auto_repo)}



        # Convert action into function (substitute internal words)
        original_action = action
        action = action.replace('-','_')

        if action in self.cfg['action_substitutions']:
            action = self.cfg['action_substitutions'][action]
        elif action in automation_meta.get('action_substitutions',{}):
            action = automation_meta['action_substitutions'][action]

        # Check if common automation and --help
        if (use_common_automation or automation == '') and cm_help:
            r = print_action_help(self.common_automation, 
                                  self.common_automation, 
                                  'common',
                                  action,
                                  original_action)

            return {'return':1, 'warning':'', 'error':'help requested'}

        # If no automation was found we do not force common automation, check if should fail or continue
        if not use_common_automation and len(automation_lst)==0:
            if self.cfg['fail_if_automation_not_found']:
                # Quit with error
                if automation=='':
                    return {'return':4, 'error':'automation was not specified'}
                else:
                    return {'return':4, 'error':f'automation "{automation}" not found'}

        # If no automation was found or we force common automation
        loaded_common_automation = False
        if use_common_automation or len(automation_lst)==0:
            auto=('automation','bbeb15d8f0a944a4')
            from . import automation as loaded_automation

            loaded_automation_class = loaded_automation.Automation

            automation_full_path = loaded_automation.self_path

            automation_meta = {
                               'alias':'automation',
                               'uid':'bbeb15d8f0a944a4'
                              }

            loaded_common_automation = True

        # Finalize automation class initialization
        if not self.xlogger == None:
            self.log(f"x automation_full_path: {automation_full_path}", "info")

        initialized_automation = loaded_automation_class(self, automation_full_path)
        initialized_automation.meta = automation_meta
        initialized_automation.full_path = automation_full_path

        # Check if action is not present in the class (inheritance)
        if automation_use_x and automation_found:
            # In such case, use old CM API <3+
            v = vars(initialized_automation.__class__)
            if action not in v or not inspect.isroutine(v[action]):
                automation_use_x = False

        # Check if action exists
        print_automation = automation_meta.get('alias','') + ',' + automation_meta.get('uid','')
        initialized_automation.artifact = print_automation

        # Check action in a class when importing
        if use_any_action:
            action = 'any'

        # Check if help about automation actions
        if action == 'help':
            import types

            print (self.cfg['info_clix'])

            print ('')
            print ('Automation python module: {}'.format(automation_full_path))

            r = print_db_actions(self.common_automation, self.cfg['action_substitutions'], automation_meta.get('alias',''), cmx = True)
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
                    print ('  * cmx ' + d + '  ' + automation_meta.get('alias','') + ' -h')

            return {'return':1, 'warning':'', 'error':'help requested'}


        if not hasattr(initialized_automation, action):
            return {'return':4, 'error':f'action "{action}" not found in automation "{print_automation}"'}
        else:
            # Check if has _cmx extension
            if loaded_common_automation:
                # By default don't use CMX in the common automation unless has _cmx extension
                # (checked later)
                automation_use_x = False

            if not automation_use_x and hasattr(initialized_automation, action + '_cmx'):
                action_addr = getattr(initialized_automation, action + '_cmx')
                automation_use_x = True
            else:
                action_addr = getattr(initialized_automation, action)


        # Check if help for a given automation action
        delayed_help = False
        delayed_help_api = ''
        delayed_help_api_prefix = ''
        delayed_help_api_prefix_0 = ''

        if cm_help:
            # Find path to automation
            rr = print_action_help(initialized_automation, 
                                   self.common_automation, 
                                   print_automation,
                                   action, 
                                   original_action)

            if rr['return']>0: return rr

            if not rr.get('delayed_help', False):
                return rr

            delayed_help = True
            delayed_help_api = rr['help']
            delayed_help_api_prefix = rr['help_prefix']
            delayed_help_api_prefix_0 = rr['help_prefix_0']

        # Process artifacts for this automation action
        if len(artifacts)>0:
            parsed_artifacts = []
            unparsed_artifacts = []

            for extra_artifact in artifacts:
                # Parse artifact
                r = parse_cm_object_and_check_current_dir(self, extra_artifact)
# Adding compatibility for the legacy cmlcr
#                if r['return'] >0 : return r
                if r['return'] == 0 : 
                    parsed_artifacts.append(r['cm_object'])
                else:
                    unparsed_artifacts.append(extra_artifact)
      
            control['_parsed_artifacts'] = parsed_artifacts

            if len(unparsed_artifacts)>0:
                control['_unparsed_artifacts'] = unparsed_artifacts

        # Check artifact and artifacts
        if artifact != '':
            # Parse artifact
            r = parse_cm_object_and_check_current_dir(self, artifact)
# Adding compatibility for the legacy cmlcr
#            if r['return'] >0 : return r
            if r['return'] == 0 : 
                control['_parsed_artifact'] = r['cm_object']
            else:
                control['_unparsed_artifact'] = artifact

        # Check min CM version requirement
        min_cm_version = automation_meta.get('min_cm_version','').strip()
        if min_cm_version != '':
            from cmind import __version__ as current_cm_version
            comparison = utils.compare_versions(current_cm_version, min_cm_version)
            if comparison < 0:
                return {'return':1, 'error':'CM automation requires CM version >= {} while current CM version is {} - please update using "pip install cmind -U"'.format(min_cm_version, current_cm_version)}



        # Roll back to older input for older CM versions < 3
        ii = i
        if not automation_use_x:
            for k in ['_parsed_automation', '_parsed_artifact', '_parsed_artifacts', '_cmd', '_unparsed_cmd']:
                if k in control:
                    ii[k[1:]] = control[k]

            for k in control:
                if not k.startswith('_'):
                    ii[k] = control[k]


        # Add call stack
        call_stack = self.state.get('call_stack', [])
        call_stack.append({'module':automation_full_path, 'func':action})
        self.state['call_stack'] = call_stack

        # Call automation action
        r = action_addr(i)

        # Remove from stack if no error
        if r['return'] == 0:
            call_stack = self.state.get('call_stack', [])
            if len(call_stack)>0:
                call_stack.pop()
                self.state['call_stack'] = call_stack

        # Check if need to save index
        if self.use_index and self.index.updated:
            rx = self.index.save()
            # Ignore output for now to continue working even if issues ...

            self.index.updated = False

        # If delayed help
        if delayed_help and not r.get('skip_delayed_help', False):
            print ('')
            print (delayed_help_api_prefix_0)
            print ('')
            print (delayed_help_api_prefix)
            print ('')
            print (delayed_help_api)

            return {'return':1, 'warning':'', 'error':'help requested'}

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
def print_db_actions(automation, equivalent_actions, automation_name, cmx = False):

    """
    Internal function: prints CM database actions.

    """

    import types

    print ('')
    print ('Common actions to manage CM repositories (use -h | -help to see the API):')
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

            x = '  ' + automation_name if automation_name!='' else ''
            
            if cmx:
                postfix = 'x' 
                extra = ' -h'
            else:
                postfix = ''
                extra = '' 

            print (f'  * cm{postfix}  ' + s + x + extra)

    return {'return':0, 'db_actions':db_actions}

############################################################
def print_action_help(automation, common_automation, print_automation, action, original_action):

     # 20240202: 
     # Check if already have full path to automation and if not, try to detect it

     import inspect

     delayed_help = False
     
     try:
         path_to_automation = automation.full_path
     except:
         automation_module = inspect.getmodule(automation)
         path_to_automation = inspect.getfile(automation_module)

     try:
         actions_with_help = automation.meta.get('actions_with_help', [])
         if action in actions_with_help:
             delayed_help = True
     except:
         pass
     
     api_prefix_0 = 'Path to the internal CM automation code: {}'.format(path_to_automation)
     
     r=utils.find_api(path_to_automation, action)
     if r['return']>0: 
         if r['return']==16:
             # Check in default automation
             path_to_common_automation = inspect.getfile(inspect.getmodule(common_automation))
             if path_to_common_automation == path_to_automation:
                 print (api_prefix_0)
                 return r

             r=utils.find_api(path_to_common_automation, original_action)
             if r['return']>0: 
                 print (api_prefix_0)
                 return r

     api = r['api']
     api_prefix = 'Python API (add -- to keys if used from the command line):'

     if not delayed_help:
         print (api_prefix_0)
         print ('')
         print (api_prefix)
         print ('')
         print (api)

     rr = {'return':0, 'help':api}

     if delayed_help:
         rr['delayed_help'] = True
         rr['help_prefix'] = api_prefix
         rr['help_prefix_0'] = api_prefix_0

     return rr

############################################################
def access(i):
    """
    Automatically initialize CM and run automations 
    without the need to initialize and customize CM class.
    Useful for Python automation scripts.

    See cmind.CM.access function for more details.
    """

    global cm

    if cm is None:
       cm=CM()

    return cm.access(i)

############################################################
def x(i, out = None):
    """
    Automatically initialize CM and run automations 
    without the need to initialize and customize CM class.
    Useful for Python automation scripts.

    See cmind.CM.x function for more details.
    """

    global cm

    if cm is None:
       cm = CM()

    return cm.x(i, out = out)

############################################################
def error(i):
    """
    Automatically initialize CM and print error if needed
    without the need to initialize and customize CM class.
    Useful for Python automation scripts.

    See CM.error function for more details.
    """

    global cm

    if cm is None:
       cm=CM()

    return cm.error(i)

############################################################
def errorx(i):
    """
    Automatically initialize CM and print error if needed
    without the need to initialize and customize CM class.
    Useful for Python automation scripts.

    See CM.error function for more details.
    """

    global cm

    if cm is None:
       cm=CM()

    return cm.errorx(i)

############################################################
def halt(i):
    """
    Automatically initialize CM, print error and halt if needed
    without the need to initialize and customize CM class.
    Useful for Python automation scripts.

    See CM.halt function for more details.

    """

    global cm

    if cm is None:
       cm=CM()

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

##############################################################################
def debug(path_to_cm_automation_module):

    import cmind

    import os
    automation = os.path.basename(os.path.dirname(path_to_cm_automation_module))

    import sys
    argv = sys.argv[1:]

    # If run from VS, length == 1

    # else normal argv

    if len(argv) == 0:
       cmd = 'test ' + automation
    elif len(argv) == 1:
       cmd = argv[0]

       if ' ' not in cmd:
           cmd += ' ' + automation
       else:
           space_index = cmd.find(' ')
           cmd = cmd[:space_index] + ' ' + automation + ' ' + cmd[space_index+1:]
    else:
       cmd = argv
       cmd.insert(1, automation)

    print ('')
    print ('Envoking CM command:')
    print (f'{cmd}')

    print ('')
    return cmind.access(cmd)
