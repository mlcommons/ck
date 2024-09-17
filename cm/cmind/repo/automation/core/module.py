# CM core automation with a few universal functions
#
# Written by Grigori Fursin

import os

from cmind.automation import Automation
from cmind import utils

# This is just an example of how to import extra files from such a package
# We need to make it unique!
#import sys
#sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
#from cm_60cb625a46b38610 import misc

class CMInit():
    ###############################################################
    def run(self, quiet = False, repo_name = 'mlcommons@cm4mlops', repo_branch = ''):
        import cmind

        print ('Checking platform information ...')
        self.get_sys_platform()

        print ('')
        print ('Checking system dependencies ...')
        r = self.install_system_packages(quiet)
        if r['return']>0 or r.get('warning','') !='' :
            return r

        print ('')
        print ('Obtaining default automation repository ...')

        print ('')
        ii = {'action':'pull', 
              'automation':'repo',
              'artifact':repo_name,
              'out':'con'}

        if repo_branch !='':
            ii['branch'] = repo_branch

        return cmind.access(ii)

    ###############################################################
    def install_system_packages(self, quiet):

        import sys
        import importlib.util

        # List of packages to install via system package manager
        packages = []
        
        git_status = self.command_exists('git')
        if not git_status:
            packages.append("git")


        # wget and curl are managed via CM scripts on Windows
        if os.name != 'nt':

            wget_status = self.command_exists('wget')
            if not wget_status:
                packages.append("wget")

            curl_status = self.command_exists('curl')
            if not curl_status:
                packages.append("curl")

        name='venv'

        if name in sys.modules:
            pass #nothing needed
        else:
            spec = importlib.util.find_spec(name)
            if spec is not None:
                module = importlib.util.module_from_spec(spec)
                sys.modules[name] = module
                spec.loader.exec_module(module)
            else:
                packages.append("python3-venv")
        
        warning = ''

        if packages:

            install_cmd = ''

            if self.system == 'Linux' or self.system == 'Darwin':
                manager, details = self.get_package_manager_details()
                if manager:
                    if manager == "apt-get":
                        install_cmd = '{}apt-get update && apt-get install -y {}'

            if install_cmd == '':
                warning = "You must install the following system packages manually: {}".format(', '.join(packages))
            else:
                print ('')
                print ('The following system packages will be installed:')
                print ('')
                print (install_cmd.format('sudo', ' '.join(packages)))

                sudo = 'sudo '
                if not quiet:
                    print ('')
                    x = input ('Would you like to skip "sudo" from above command (y/N)? ')

                    if x.lower() in ['y','yes']:
                        sudo = ''

                install_cmd = install_cmd.format(sudo, ' '.join(packages))

                print ('')
                print ('Running system command:')
                print (install_cmd)

                r = os.system(install_cmd)
                if r>0:
                    return {'return':1, 'error':f'Command {install_cmd} failed with return code {r}'}

        rr = {'return':0}

        if warning != '': rr['warning'] = warning

        return rr

    ###############################################################
    def detect_package_manager(self):
        package_managers = {
            'apt-get': '/usr/bin/apt-get',
            'yum': '/usr/bin/yum',
            'dnf': '/usr/bin/dnf',
            'pacman': '/usr/bin/pacman',
            'zypper': '/usr/bin/zypper',
            'brew': '/usr/local/bin/brew'
        }

        for name, path in package_managers.items():
            if os.path.exists(path):
                return name

        return None

    ###############################################################
    def get_package_manager_details(self):
        import subprocess

        manager = self.detect_package_manager()
        if manager:
            try:
                version_output = subprocess.check_output([manager, '--version'], stderr=subprocess.STDOUT).decode('utf-8')
                return manager, version_output.split('\n')[0]
            except subprocess.CalledProcessError:
                return manager, 'Version information not available'
        else:
            return None, 'No supported package manager found'

    ###############################################################
    # Checks if command exists(for installing required packages).
    # If the command exists, which returns 0, making the function return True.
    # If the command does not exist, which returns a non-zero value, making the function return False.
    # NOTE: The standard output and standard error streams are redirected to PIPES so that it could be captured in future if needed.    
    def command_exists(self, command):
        import subprocess

        if self.system == "Linux" or self.system == 'Darwin':
            return subprocess.call(['which', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

        elif self.system == "Windows":
            return subprocess.call([command, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) == 0

    
    ###############################################################
    def get_sys_platform(self):
        import platform

        self.system =  platform.system() 



class CAutomation(Automation):
    """
    CM "core" automation actions
    """

    ############################################################
    def __init__(self, cmind, automation_file):
        super().__init__(cmind, __file__)


    ############################################################
    def uid(self, i):
        """
        Generate CM UID.

        Args:
          (CM input dict): empty dict

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          * uid (str): CM UID
        """

        return utils.call_internal_module(self, __file__, 'module_misc', 'uid', i)

    ############################################################
    def init(self, i):
        """
        Init CM

        Args:
          (CM input dict):

          (quiet) (bool): if True, skip asking questions about sudo, etc
          (repo) (str): automation repository to pull ('mlcommons@cm4mlops' by default) 
          (branch) (str): branch to use ('' by default)


        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0
        """

        cm_init = CMInit()

        quiet = i.get('quiet', False)

        repo_name = i.get('repo', '')
        if repo_name == '': repo_name = 'mlcommons@cm4mlops'

        repo_branch = i.get('branch', '')

        r = cm_init.run(quiet = quiet, repo_name = repo_name, repo_branch = repo_branch)
        if r['return']>0: return r

        warning = r.get('warning', '')
        if warning != '':
            print ('')
            print (warning)

        return {'return':0}
