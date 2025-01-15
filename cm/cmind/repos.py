# Collective Mind repositories
#
# Author(s): Grigori Fursin
# Contributor(s):
#
# Copyright: https://github.com/mlcommons/ck/blob/master/COPYRIGHT.txt
# License: https://github.com/mlcommons/ck/blob/master/LICENSE.md
# History: https://github.com/mlcommons/ck/blob/master/HISTORY.CM.md
# White paper: https://arxiv.org/abs/2406.16791
# Project contributors: https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md

import os

from cmind.repo import Repo
from cmind import utils

class Repos:
    """
    CM repositories class
    """

    def __init__(self, path, cfg, path_to_internal_repo = '', cmx = False):
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

        self.extra_info = {}

        self.cmx = cmx

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

        # Skip internal repos
        skip_internal_repos = os.environ.get('CM_CORE_SKIP_INTERNAL_REPOS','').strip().lower()
        if skip_internal_repos not in ['1', 'true', 'yes']:
            import pkgutil
            for mi, name, ispkg in pkgutil.iter_modules():
                if name.startswith('cm') and name != 'cmind':
                    for x in [None, 'repo']:
                        path = os.path.join(mi.path, name)
                        if x != None: path = os.path.join(path, x)
                        path_cmr = os.path.join(path, 'cmr.yaml')
                        if os.path.isfile(path_cmr) and path not in self.paths:
                            self.paths.insert(0, path)
                            break

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
        checked_self_paths = []
        for path_to_repo in self.paths:
            # First try concatenated path and then full path (if imported)
            found = False
            for full_path_to_repo in [os.path.join(full_path_to_repos, path_to_repo),
                                      path_to_repo]:
                if os.path.isdir(full_path_to_repo):
                    # Load description
                    repo = Repo(full_path_to_repo, self.cfg)

                    r = repo.load(cmx = self.cmx)
                    if r['return']>0 and r['return']!=16: return r

                    # Load only if desc exists
                    if r['return']!=16:
                        # Set only after all initializations
                        self.lst.append(repo)

                        repo_uid = repo.meta['uid']
                        if repo_uid!='':
                            self.extra_info[repo_uid]=repo

                        repo_alias = repo.meta['alias']
                        if repo_alias!='':
                            self.extra_info[repo_alias]=repo

                        found = True
                        break

            # Repo path exists but repo itself doesn't exist - fail
            if found:
                checked_self_paths.append(path_to_repo)
            else:
                print ('WARNING: repository path {} not found (check file {})'.format(path_to_repo, full_path_to_repo_paths))

        # Save with correct paths
        if len(checked_self_paths) != len(self.paths):

            skip_fix_paths = os.environ.get('CM_CORE_SKIP_FIX_REPO_PATH','').strip().lower()
            if skip_fix_paths not in ['1', 'true', 'yes']:
                import copy

                self.paths = copy.deepcopy(checked_self_paths)

                if self.path_to_internal_repo in checked_self_paths:
                    checked_self_paths.remove(self.path_to_internal_repo)

                print ('WARNING: fixed repo list file {}'.format(full_path_to_repo_paths))

                r = utils.save_json(full_path_to_repo_paths, meta = checked_self_paths)
                if r['return']>0: return r

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

            * (warnings) (list of str): warnings to install more CM repositories

        """

        # Load clean file with repo paths
        r = utils.load_json(self.full_path_to_repo_paths)
        if r['return']>0: return r

        paths = r['meta']

        modified = False

        warnings = []

        if mode == 'add':
            if repo_path not in paths:
                # Load meta of the current repo
                path_to_repo_desc = os.path.join(repo_path, self.cfg['file_meta_repo'])

                r=utils.load_yaml_and_json(file_name_without_ext=path_to_repo_desc)
                if r['return']>0: return r

                meta = r['meta']

                alias = meta.get('alias', '')
                uid = meta.get('uid', '')

                deps_on_other_repos = meta.get('deps', {})
                
                # Check that no repos exist with the same alias and/or uid 
                # (to avoid adding forks and original repos)

                for path in paths:
                    path_to_existing_repo_desc = os.path.join(path, self.cfg['file_meta_repo'])
                    r=utils.load_yaml_and_json(file_name_without_ext=path_to_existing_repo_desc)
                    if r['return']>0: return r

                    existing_meta = r['meta']

                    existing_alias = existing_meta.get('alias', '')
                    existing_uid = existing_meta.get('uid', '')

                    # Check if repository already exists under different name
                    exist = False
                    if alias != '' and existing_alias !='' and alias == existing_alias:
                        exist = True

                    if not exist and uid !='' and existing_uid !='' and uid == existing_uid:
                        exist = True

                    if exist:
                        return {'return':1, 'error':'CM repository with the same alias "{}" and/or uid "{}" already exists in {}'.format(alias, uid, path)}

                    # Check if there is a conflict
                    if len(deps_on_other_repos)>0:
                        for d in deps_on_other_repos:
                            d_alias = d.get('alias', '')
                            d_uid = d.get('uid', '')

                            r = utils.match_objects(existing_uid, existing_alias, d_uid, d_alias)
                            if r['return']>0: return r
                            match = r['match']

                            if match:
                                if d.get('conflict', False):
                                    return {'return':1, 'error':'Can\'t install this repository because it conflicts with the already installed one ({}) - you may need to remove it to proceed (cm rm repo {})'.format(d_alias,d_alias)}

                                d['matched'] = True

                                break

                                    
                # Check if has missing deps on other CM repos
                for d in deps_on_other_repos:
                    if not d.get('conflict', False) and not d.get('matched', False):
                        warnings.append('You must install extra CM repository: cm pull repo {}'.format(d['alias']))
                
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

        rr = {'return':0}

        if len(warnings)>0:
            rr['warnings'] = warnings

        return rr

    ############################################################
    def pull(self, alias, url = '', branch = '', checkout = '', _dir = '', console = False, desc = '', prefix = '', depth = None, 
                    path_to_repo = None, checkout_only = False, skip_zip_parent_dir = False,
                    extra_cmd_git = '', extra_cmd_pip = '', new_branch = ''):
        """
        Clone or pull CM repository

        Args:
            alias (str): CM repository alias
            (url) (str): Git repository URL
            (branch) (str): Git repository branch
            (new_branch) (str): Create new  branch
            (checkout) (str): Git repository checkout
            (checkout_only) (bool): only checkout existing repo
            (_dir) (str): use repository in this directory
            (depth) (int): Git repository depth
            (console) (bool): if True, print some info to console
            (desc) (str): optional repository description
            (prefix) (str): sub-directory to be used inside this CM repository to store artifacts
            (path_to_repo) (str): force path to repo (useful to pull imported repos with non-standard path)
            (checkout_only) (bool): only checkout Git repository but don't pull
            (skip_zip_parent_dir) (bool): skip parent dir in CM ZIP repo (useful when 
                                          downloading CM repo archives from GitHub)
            (extra_cmd_git) (str): add this string to git clone
            (extra_cmd_pip) (str): add this string to pip install when installing
                                   requirements from CM repositories

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

            * (meta) (dict): meta of the CM repository

            * (warnings) (list of str): warnings to install more CM repositories

        """

        # Prepare path
        if path_to_repo == None:
            path_to_repo = os.path.join(self.full_path_to_repos, alias)

        if _dir != '': 
            path_to_repo = os.path.join(path_to_repo, _dir)

        if console:
            print ('Local path: '+path_to_repo)
            print ('')

        # Check if repository already exists but corrupted
        path_to_repo_desc = os.path.join(path_to_repo, self.cfg['file_meta_repo'])
        r=utils.is_file_json_or_yaml(file_name = path_to_repo_desc)
        if r['return']>0: return r
        repo_desc_exists=r['is_file']

        if os.path.isdir(path_to_repo) and not repo_desc_exists:
            print ('')
            print ('WARNING: directory {} already exists but without cmr.yaml - maybe clone or download was corrupted!'.format(path_to_repo))

            x = input('Delete this repo (Y/n)? ')
            if x.strip().lower() not in ['n','no']:
                import shutil

                print ('')
                print ('Deleting {} ...'.format(path_to_repo))
                shutil.rmtree(path_to_repo, onerror=utils.rm_read_only)
                print ('')

        cur_dir = os.getcwd()

        clone=False

        download=True if url.find('.zip')>0 else False

        if checkout_only:
            if not os.path.isdir(path_to_repo):
                return {'return':1, 'error':'Trying to checkout repo "{}" that was not pulled'.format(alias)}
        else:
            if download:
                # If CM repo already exists
                if os.path.isdir(path_to_repo):
                    return {'return':1, 'error':'repository is already installed'}

                os.makedirs(path_to_repo)

                os.chdir(path_to_repo)

                cmd = 'wget --no-check-certificate "'+url+'" -O '+alias

            else:
                if os.path.isdir(path_to_repo):
                    # Attempt to update
                    os.chdir(path_to_repo)

                    cmd = 'git pull'
                else:
                    # Attempt to clone
                    clone = True

                    os.chdir(self.full_path_to_repos)

                    cmd = 'git clone ' + url + ' ' + alias

                    # Check if depth is set
                    if depth != None and depth != '':
                        cmd += ' --depth ' + str(depth)

                    if extra_cmd_git !='' :
                        cmd +=' ' + extra_cmd_git

            if console:
                print (cmd)
                print ('')

            r = os.system(cmd)

            if clone and not os.path.isdir(path_to_repo):
                return {'return':1, 'error':'repository was not cloned'}

        os.chdir(path_to_repo)

        if download and not checkout_only:
            import zipfile

            pack_file = os.path.join(path_to_repo, alias)

            # Attempt to read cmr.json 
            repo_pack_file = open(pack_file, 'rb')
            repo_pack_zip = zipfile.ZipFile(repo_pack_file)

            repo_pack_desc = self.cfg['file_meta_repo']

            files=repo_pack_zip.namelist()

            repo_path = path_to_repo

            if console:
                print ('Unpacking {} to {} ...'.format(pack_file, repo_path))

            parent_dir = ''
            
            # Unpacking zip
            for f in files:
                if not f.startswith('..') and not f.startswith('/') and not f.startswith('\\'):

                    if skip_zip_parent_dir and parent_dir == '':
                        parent_dir = f

                    ff = f[len(parent_dir):] if parent_dir != '' else f
                    
                    file_path = os.path.join(repo_path, ff)

                    if f.endswith('/'):
                        # create directory
                        if not os.path.exists(file_path):
                            os.makedirs(file_path)
                    else:
                        dir_name = os.path.dirname(file_path)
                        if not os.path.exists(dir_name):
                            os.makedirs(dir_name)

                        # extract file
                        file_out = open(file_path, 'wb')
                        file_out.write(repo_pack_zip.read(f))
                        file_out.close()

            repo_pack_zip.close()
            repo_pack_file.close()

            # remove original file
            os.remove(pack_file)

        # Check if branch 
        if new_branch != '':
            cmd = 'git checkout -b ' + new_branch

            if console:
                print ('')
                print (cmd)
                print ('')

            r = os.system(cmd)

            if r>0:
                return {'return':1, 'error':'creating new git branch failed'}

        if branch != '' or checkout != '':
            cmd = 'git checkout'

            # When checkout only, we do not need -b for branch
            extra_flag = ' ' if checkout_only else ' -b '

            if branch != '' and checkout != '':
            # if both branch and checkout are specified, we do checkout and set remote branch
                cmd = "git checkout -b " + branch + " " + checkout + " && git branch --set-upstream-to=origin/"+ branch + " " + branch  

            elif branch != '':
                cmd = 'git fetch && git checkout ' + branch

            elif checkout!='':
                cmd += ' ' + checkout

            if console:
                print ('')
                print (cmd)
                print ('')

            r = os.system(cmd)

            if r>0:
                return {'return':1, 'error':'git checkout for repository failed'}

        # Check if repo description exists 
        r=utils.is_file_json_or_yaml(file_name = path_to_repo_desc)
        if r['return']>0: return r

        must_update_repo_desc = False

        if r['is_file']:
            # Load meta from the repository
            r=utils.load_yaml_and_json(file_name_without_ext=path_to_repo_desc)
            if r['return']>0: return r

            meta = r['meta']
        else:
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


# GF blocked the following code because if we create a fork of mlcommons@ck for example to ctuning@mlcommons-ck
# and then pull ctuning@mlcommons-ck, it attempts to rewrite .cmr.yaml with the new alias which we do not want to do!
# We want to keep whatever is in .cmr.yaml to avoid ambiguities ...
#        else:
#            # Load meta from the repository
#            r=utils.load_yaml_and_json(file_name_without_ext=path_to_repo_desc)
#            if r['return']>0: return r
#
#            meta = r['meta']
#
#            # If alias forced by user is not the same as in meta, update it 
#            # https://github.com/mlcommons/ck/issues/196
#
#            if alias != meta.get('alias',''):
#                meta['alias']=alias
#
#                must_update_repo_desc = True

        if must_update_repo_desc:
            r=utils.save_yaml(path_to_repo_desc + '.yaml', meta=meta)
            if r['return']>0: return r

        # Check path to repo with prefix
        path_to_repo_with_prefix = path_to_repo

        if prefix!='':
            path_to_repo_with_prefix = os.path.join(path_to_repo, prefix)

            if not os.path.isdir(path_to_repo_with_prefix):
                os.makedirs(path_to_repo_with_prefix)

        # Check min CM version requirement
        min_cm_version = meta.get('min_cm_version','').strip()
        if min_cm_version != '':
            from cmind import __version__ as current_cm_version
            comparison = utils.compare_versions(current_cm_version, min_cm_version)
            if comparison < 0:
                return {'return':1, 'error':'This repository requires CM version >= {} while current CM version is {} - please update using "pip install cmind -U"'.format(min_cm_version, current_cm_version)}

        # Get final alias
        alias = meta.get('alias', '')

        # Update repo list
        # TBD: make it more safe (reload and save)
        r = self.process(path_to_repo, 'add')
        if r['return']>0: return r

        warnings = r.get('warnings', [])

        # Check if need to install requirements
        install_python_requirements = meta.get('install_python_requirements', False)

        if install_python_requirements:
            import sys

            python_exec = sys.executable

            cmd = python_exec + ' -m pip install -r requirements.txt'

            if extra_cmd_pip !='' :
                cmd +=' ' + extra_cmd_pip

            if console:
                print ('')
                print (cmd)
                print ('')

            r = os.system(cmd)

            if r>0:
                return {'return':1, 'error':'pip install -r requirements failed for this CM repository'}

        # Go back to original directory
        os.chdir(cur_dir)

        if console:
            print ('')
            print ('CM alias for this repository: {}'.format(alias))

        rr = {'return':0, 'meta':meta}
        
        if len(warnings)>0: rr['warnings'] = warnings

        return rr


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

            * (warnings) (list of str): warnings to install more CM repositories
                
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
            # 20241006: Moved the check for min cmind version to _cmr.yaml
#            path_to_requirements = os.path.join(path_to_repo, 'requirements.txt')
#
#            if not os.path.isfile(path_to_requirements):
#                r = utils.save_txt(file_name = path_to_requirements, string = self.cfg['new_repo_requirements'])
#                if r['return']>0: return r

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

        warnings = r.get('warnings', [])

        rr =  {'return':0, 'meta':meta, 
                           'path_to_repo': path_to_repo, 
                           'path_to_repo_desc': path_to_repo_desc,
                           'path_to_repo_with_prefix': path_to_repo_with_prefix}

        if len(warnings)>0: rr['warnings'] = warnings

        return rr

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

                shutil.rmtree(path_to_repo, onerror=utils.rm_read_only)
            else:
                if console:
                    print ('  CM repository was unregistered from CM but its content was not deleted ...')

        return {'return':0}
