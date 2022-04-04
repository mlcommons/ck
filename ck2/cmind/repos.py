# Collective Mind repositories

import os

from cmind.repo import Repo
from cmind import utils

class Repos:
    ############################################################
    def __init__(self, path, cfg, path_to_default_repo = ''):
        """
        Initialize class 
        """

        self.path = path
        self.cfg = cfg

        self.full_path_to_repos = ''

        # Paths to CM repos
        self.paths = []

        # List of initialized repositories
        self.lst = []

        # Potential path to default repo
        self.path_to_default_repo = path_to_default_repo

        self.full_path_to_repo_paths = ''

    ############################################################
    def load(self, init = False):
        """
        Load or initialize file with repositories

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

        # Prepare path for local repo
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

        # Check default repo
        if self.path_to_default_repo != '' and os.path.isdir(self.path_to_default_repo):
            self.paths.insert(0, self.path_to_default_repo)

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
                    if r['return'] >0 : return r

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
        Process file with repo list

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
    def pull(self, alias, url = '', branch = '', checkout = '', con = False, name = '', prefix = ''):
        """
        Pull or clone repository

        """

        # Prepare path
        path_to_repo = os.path.join(self.full_path_to_repos, alias)
        
        if con:
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
            
        if con:
            print (cmd)
            print ('')

        os.system(cmd)

        if con:
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

            if name!='': meta['name']=name
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


        # Update repo list
        # TBD: make it more safe (reload and save)
        r = self.process(path_to_repo, 'add')
        if r['return']>0: return r

        # Go back to original directory
        os.chdir(cur_dir)

        return {'return':0, 'meta':meta}

    ############################################################
    def init(self, alias, uid, path = '', con = False, name = '', prefix = ''):
        """
        Init or clone repository

        """

        # Prepare path
        if uid == '':
            r=utils.gen_uid()
            if r['return']>0: return r
            uid = r['uid']

        repo_name=alias if alias!='' else uid
        
        path_to_repo = os.path.join(self.full_path_to_repos, repo_name) if path=='' else path
        path_to_repo_desc = os.path.join(path_to_repo, self.cfg['file_meta_repo'])
        
        if con:
            print ('Local path: '+path_to_repo)
            print ('')

        if not os.path.isdir(path_to_repo):
            os.makedirs(path_to_repo)

        meta = {
                 'uid': uid,
                 'alias': alias,
                 'git':False,
               }

        if name!='': meta['name']=name
        if prefix!='': meta['prefix']=prefix

        r=utils.save_yaml(path_to_repo_desc + '.yaml', meta=meta)
        if r['return']>0: return r

        # Update repo list
        # TBD: make it more safe (reload and save)
        r = self.process(path_to_repo, 'add')
        if r['return']>0: return r

        return {'return':0, 'meta':meta, 'path_to_repo': path_to_repo, 'path_to_repo_desc': path_to_repo_desc}

    ############################################################
    def delete(self, alias, remove_all = False, con = False):
        """
        Delete repository with or without content

        """

        # Prepare path
        path_to_repo = os.path.join(self.full_path_to_repos, alias)
        
        if con:
            print ('Local path: '+path_to_repo)
            print ('')

        if path_to_repo not in self.paths:
            return {'return':16, 'error':'repository not found'}
        
        # TBD: make it more safe (reload and save)
        r = self.process(path_to_repo, 'delete')
        if r['return']>0: return r

        # Check if remove all
        if remove_all:
            import shutil

            if con:
                print ('Deleting repository content ...')
            
            shutil.rmtree(path_to_repo)
        else:
            if con:
                print ('Repository was unlinked from CM but the content was not deleted.')

        return {'return':0}
