# Collective Mind repositories

import os

from cmind.repo import Repo
from cmind import utils

class Repos:
    """
    CM repositories class
    """

    def __init__(self, path, cfg, path_to_internal_repo = ''):
        """
        Initialize CM repositories class

        Args:
            path (str): path to directory with repos.json where all paths of registered CM repositories are stored
            cfg (dict): CM configuration
            (path_to_internal_repo) (str): path to the internal CM repository (useful during development/debugging)

        Returns:
            (python class) with the following vars:

            * path (str): path to CM repositories and index file
            * full_path_to_repos (str): path to CM repositories
            * path_to_internal_repo (str): path to the internal CM repository
            * full_path_to_repo_paths (str): full path to repos.json
            * lst (list): list of initialized CM repository classes
        """

        self.path = path
        self.cfg = cfg

        self.full_path_to_repos = ''

        # Paths to CM repos
        self.paths = []

        # List of initialized repositories
        self.lst = []

        # Potential path to internal repo
        self.path_to_internal_repo = path_to_internal_repo

        self.full_path_to_repo_paths = ''

    ############################################################
    def load(self, init = False):
        """
        Load or initialize repos.json file with repositories

        Args:
            init (bool): if False do not init individual CM repositories

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

        """

        # If reload after updating repos
        if init:
            self.paths = []
            self.lst = []

        # Check if home directory exists. Create it otherwise.
        if not os.path.isdir(self.path):
            os.makedirs(self.path)
        
        # Check repos holder
        full_path_to_repos = os.path.join(self.path,
                                          self.cfg['dir_repos'])

        self.full_path_to_repos = full_path_to_repos

        # If placeholder for repos doesn't exist, create it
        if not os.path.isdir(full_path_to_repos):
            os.makedirs(full_path_to_repos)

        # Search if there is a file with repos
        full_path_to_repo_paths = os.path.join(self.path, self.cfg['file_repos'])
        self.full_path_to_repo_paths = full_path_to_repo_paths

        if os.path.isfile(full_path_to_repo_paths):
            r = utils.load_json(full_path_to_repo_paths)
            if r['return']>0: return r

            self.paths = r['meta']
        else:
            r = utils.save_json(full_path_to_repo_paths, meta = self.paths)
            if r['return']>0: return r

        # Check internal repo (will be after local)
        if self.path_to_internal_repo != '' and os.path.isdir(self.path_to_internal_repo):
            self.paths.insert(0, self.path_to_internal_repo)

        # Prepare path for local repo (will be the first in the search as a local scratchpad)
        path_local_repo = os.path.join(full_path_to_repos, self.cfg['local_repo_name'])

        if not os.path.isdir(path_local_repo):
            os.makedirs(path_local_repo)

        path_local_repo_meta = os.path.join(path_local_repo, self.cfg['file_meta_repo']+'.yaml')

        if not os.path.isfile(path_local_repo_meta):
            r = utils.save_yaml(path_local_repo_meta, 
                                meta = self.cfg['local_repo_meta'])
            if r['return']>0: return r

        if path_local_repo not in self.paths:
            self.paths.insert(0, path_local_repo)

        # Check that repository exists and load meta description
        for path_to_repo in self.paths:
            # First try concatenated path and then full path (if imported)
            found = False
            for full_path_to_repo in [os.path.join(full_path_to_repos, path_to_repo),
                                      path_to_repo]:
                if os.path.isdir(full_path_to_repo):
                    # Load description
                    repo = Repo(full_path_to_repo, self.cfg)

                    r = repo.load()
                    if r['return']>0: return r
                    
                    # Set only after all initializations
                    self.lst.append(repo)

                    found = True
                    break

            # Repo path exists but repo itself doesn't exist - fail
            if not found:
                return {'return':1, 'error': 'repository path {} not found (check file {})'.format(path_to_repo, full_path_to_repo_paths)}

        return {'return':0}

    ############################################################
    def process(self, repo_path, mode='add'):
        """
        Add or delete CM repository

        Args:
            repo_path (str): path to CM repository
            (mode) (str): "add" (default) 
                          or "delete"

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

        """

        # Load clean file with repo paths
        r = utils.load_json(self.full_path_to_repo_paths)
        if r['return']>0: return r

        paths = r['meta']

        modified = False
        
        if mode == 'add':
            if repo_path not in paths:
                paths.append(repo_path)
                modified = True
        elif mode == 'delete':
            new_paths = []
            for p in paths:
                if p==repo_path:
                    modified = True
                else:
                    new_paths.append(p)
            paths=new_paths

        if modified:
            r = utils.save_json(self.full_path_to_repo_paths, meta = paths)
            if r['return']>0: return r

            # Reload repos
            self.load(init=True)

        return {'return':0}

    ############################################################
    def pull(self, alias, url = '', branch = '', checkout = '', console = False, desc = '', prefix = ''):
        """
        Clone or pull CM repository

        Args:
            alias (str): CM repository alias
            (url) (str): Git repository URL
            (branch) (str): Git repository branch
            (checkout) (str): Git repository checkout
            (console) (bool): if True, print some info to console
            (desc) (str): optional repository description
            (prefix) (str): sub-directory to be used inside this CM repository to store artifacts

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

            * (meta) (dict): meta of the CM repository

        """

        # Prepare path
        path_to_repo = os.path.join(self.full_path_to_repos, alias)
        
        if console:
            print ('Local path: '+path_to_repo)
            print ('')

        cur_dir = os.getcwd()

        clone=False
        if os.path.isdir(path_to_repo):
            # Attempt to update
            os.chdir(path_to_repo)

            cmd = 'git pull'
        else:
            # Attempt to clone
            clone = True

            os.chdir(self.full_path_to_repos)

            cmd = 'git clone '+url+' '+alias
            
        if console:
            print (cmd)
            print ('')

        os.system(cmd)

        if console:
            print ('')

        # Check if repo description exists 
        path_to_repo_desc = os.path.join(path_to_repo, self.cfg['file_meta_repo'])

        r=utils.is_file_json_or_yaml(file_name = path_to_repo_desc)
        if r['return']>0: return r

        must_update_repo_desc = False
        
        if not r['is_file']:
            # Prepare meta
            r=utils.gen_uid()
            if r['return']>0: return r

            repo_uid = r['uid']
            
            meta = {
               'uid': repo_uid,
               'alias': alias,
               'git':True,
            }

            if desc!='': meta['desc']=desc
            if prefix!='': meta['prefix']=prefix

            must_update_repo_desc = True
        else:
            # Load meta from the repository
            r=utils.load_yaml_and_json(file_name_without_ext=path_to_repo_desc)
            if r['return']>0: return r

            meta = r['meta']

            # If alias forced by user is not the same as in meta, update it 
            # https://github.com/mlcommons/ck/issues/196

            if alias != meta.get('alias',''):
                meta['alias']=alias

                must_update_repo_desc = True

        if must_update_repo_desc:
            r=utils.save_yaml(path_to_repo_desc + '.yaml', meta=meta)
            if r['return']>0: return r

        # Check paht to repo with prefix
        path_to_repo_with_prefix = path_to_repo

        if prefix!='':
            path_to_repo_with_prefix = os.path.join(path_to_repo, prefix)

            if not os.path.isdir(path_to_repo_with_prefix):
                os.makedirs(path_to_repo_with_prefix)
        
        # Update repo list
        # TBD: make it more safe (reload and save)
        r = self.process(path_to_repo, 'add')
        if r['return']>0: return r

        # Go back to original directory
        os.chdir(cur_dir)

        return {'return':0, 'meta':meta}

    ############################################################
    def init(self, alias, uid, path = '', console = False, desc = '', prefix = '', only_register = False):
        """
        Init CM repository in a given path

        Args:
            alias (str): CM repository alias
            uid (str): CM repository UID
            (path) (str): local path to a given repository (otherwise use $HOME/CM/repos)
            (desc) (str): optional repository description
            (prefix) (str): sub-directory to be used inside this CM repository to store artifacts
            (only_register) (bool): if True, only register path in the CM index of repositories but do not recreate cmr.yaml

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

            * meta (dict): meta of the CM repository

            * path_to_repo (str): path to repository
            * path_to_repo_desc (str): path to repository description
            * path_to_repo_with_prefix (str): path to repository with prefix (== path_to_repo if prefix == "")

        """

        # Prepare path
        if uid == '':
            r=utils.gen_uid()
            if r['return']>0: return r
            uid = r['uid']

        repo_name=alias if alias!='' else uid
        
        path_to_repo = os.path.join(self.full_path_to_repos, repo_name) if path=='' else path

        # Convert potentially relative path into an absolute path
        # For example, it's needed when we initialize repo in the current directory
        # or use . and ..

        path_to_repo = os.path.abspath(path_to_repo)

        if console:
            print ('Local path to the CM repository: '+path_to_repo)
            print ('')

        # If only register (description already exists), skip meta preparation
        path_to_repo_desc = os.path.join(path_to_repo, self.cfg['file_meta_repo'])

        if not only_register:
            if not os.path.isdir(path_to_repo):
                os.makedirs(path_to_repo)

            # Check if file already exists
            r=utils.is_file_json_or_yaml(file_name=path_to_repo_desc)
            if r['return'] >0: return r

            if r['is_file']:
                return {'return':1, 'error':'Repository description already exists in {}'.format(path_to_repo)}
            
            meta = {
                     'uid': uid,
                     'alias': alias,
                     'git':False,
                   }

            if desc!='': 
                meta['desc']=desc

            if prefix!='': 
                meta['prefix']=prefix

            r=utils.save_yaml(path_to_repo_desc + '.yaml', meta=meta)
            if r['return']>0: return r

            # Check requirements.txt
            path_to_requirements = os.path.join(path_to_repo, 'requirements.txt')

            if not os.path.isfile(path_to_requirements):
                r = utils.save_txt(file_name = path_to_requirements, string = self.cfg['new_repo_requirements'])
                if r['return']>0: return r
        
        else:
            r=utils.load_yaml_and_json(file_name_without_ext=path_to_repo_desc)
            if r['return'] >0: return r
            
            meta = r['meta']

        # Check if exist and create if not
        path_to_repo_with_prefix = path_to_repo

        if prefix!='':
            path_to_repo_with_prefix = os.path.join(path_to_repo, prefix)

            if not os.path.isdir(path_to_repo_with_prefix):
                os.makedirs(path_to_repo_with_prefix)

        # Update repo list
        # TBD: make it more safe (reload and save)
        r = self.process(path_to_repo, 'add')
        if r['return']>0: return r

        return {'return':0, 'meta':meta, 
                            'path_to_repo': path_to_repo, 
                            'path_to_repo_desc': path_to_repo_desc,
                            'path_to_repo_with_prefix': path_to_repo_with_prefix}

    ############################################################
    def delete(self, lst, remove_all = False, console = False, force = False):
        """
        Delete CM repository or repositories with or without content

        Args:
            lst (list of CM repository classes): list of CM repositories
            remove_all (bool): if True, remove the content and unregister CM repository
            console (bool): if True, output some info to console
            force (bool): if True, do not ask questions

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

        """

        # Navigate through repos from the search function
        for repo in lst:
            # Prepare path
            path_to_repo = repo.path

            if console:
                print ('Local path to a CM repository: '+path_to_repo)

            if path_to_repo not in self.paths:
                return {'return':16, 'error':'repository not found in CM index - weird'}

            if console:
                if not force:
                    ask = input('  Are you sure you want to delete this repository (y/N): ')
                    ask = ask.strip().lower()

                    if ask!='y':
                        print ('    Skipped!')
                        continue

            # TBD: make it more safe (reload and save)
            r = self.process(path_to_repo, 'delete')
            if r['return']>0: return r

            # Check if remove all
            if remove_all:
                import shutil

                if console:
                    print ('  Deleting repository content ...')
                
                shutil.rmtree(path_to_repo)
            else:
                if console:
                    print ('  CM repository was unregistered from CM but its content was not deleted ...')

        return {'return':0}
