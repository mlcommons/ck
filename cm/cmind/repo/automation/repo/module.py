# CM automation to manage CM repositories
#
# Written by Grigori Fursin

import os

from cmind.automation import Automation
from cmind import utils
from cmind import net

class CAutomation(Automation):
    """
    CM "repo" automation actions
    """

    ############################################################
    def __init__(self, cmind, automation_file):
        super().__init__(cmind, __file__)

    ############################################################
    def pull(self, i):
        """
        Clone or pull CM repository.

        Args:
          (CM input dict): 

          (out) (str): if 'con', output to console

          (artifact) (str): repository name (alias)
          (url) (str): URL of a repository
          (pat) (str): Personal Access Token (if supported and url=='')
          (branch) (str): Git branch
          (checkout) (str): Git checkout
          (checkout_only) (bool): only checkout existing repo
          (depth) (int): Git depth
          (desc) (str): brief repository description (1 line)
          (prefix) (str): extra directory to keep CM artifacts
          (skip_zip_parent_dir) (bool): skip parent dir in CM ZIP repo (useful when 
                                        downloading CM repo archives from GitHub)

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          * meta (dict): meta of the CM repository
        """

        console = i.get('out') == 'con'

        alias = i.get('artifact','')
        url = i.get('url','')
        desc = i.get('desc','')
        prefix = i.get('prefix','')
        pat = i.get('pat','')

        checkout_only = i.get('checkout_only', False)
        skip_zip_parent_dir = i.get('skip_zip_parent_dir', False)

        if url == '':
            if alias != '':
                url = self.cmind.cfg['repo_url_prefix']

                if '@' not in alias:
                    alias = self.cmind.cfg['repo_url_org'] + '@' + alias

                url += alias.replace('@','/')

                if pat != '' and url.startswith('https://'):
                    url = url[:8]+pat+'@'+url[8:]
        else:
           if alias == '':
               # Get alias from URL
               alias = url

               # Check if zip file
               j = alias.find('.zip')
               if j>0:
                   j1 = alias.rfind('/')
                   alias = alias[j1+1:j+4]
               else:
                   if alias.endswith('.git'): alias=alias[:-4]

                   j = alias.find('//')
                   if j>=0:
                       j1 = alias.find('/', j+2)
                       if j1>=0:
                           alias = alias[j1+1:].replace('/','@')

        if url == '':
            pull_repos = []

            for repo in sorted(self.cmind.repos.lst, key = lambda x: x.meta.get('alias','')):
                meta = repo.meta

                if meta.get('git', False):
                    # Note that internal repo alias may not be the same as the real pulled alias since it can be a fork
                    # Pick it up from the path

                    repo_path = repo.path

                    pull_repos.append({'alias': os.path.basename(repo_path),
                                       'path_to_repo': repo_path})
        else:
            # We are migrating cm-mlops repo from mlcommons@ck to a clean and new mlcommons@cm4mlops:
            # https://github.com/mlcommons/ck/issues/1215
            # As discussed, we should have a transparent redirect with a warning
            # unless branch/checkout is used - in such case we keep old repository
            # for backwards compatibility and reproducibility

            branch = i.get('branch', '')
            checkout = i.get('checkout', '')

            r = net.request({'get': {'action': 'check-migration-repo-notes', 'repo': url, 'branch': branch, 'checkout': checkout}})
            notes = r.get('dict', {}).get('notes','')
            if notes !='':
                print (notes)

            if alias == 'mlcommons@ck' and branch == '' and checkout == '':
                print ('=========================================================================')
                print ('Warning: mlcommons@ck was automatically changed to mlcommons@cm4mlops.')
                print ('If you want to use older mlcommons@ck repository, use branch or checkout.')
                print ('=========================================================================')

                alias = 'mlcommons@cm4mlops'
                url = url.replace('mlcommons/ck', 'mlcommons/cm4mlops')


            pull_repos = [{'alias':alias,
                           'url':url,
                           'branch': branch,
                           'checkout': checkout,
                           'depth': i.get('depth', '')}]


        # Go through repositories and pull
        repo_meta = {}
        repo_metas = {}

        warnings = []
        
        for repo in pull_repos:
             alias = repo['alias']
             url = repo.get('url', '')
             branch = repo.get('branch','')
             checkout = repo.get('checkout','')
             depth = repo.get('depth','')
             path_to_repo = repo.get('path_to_repo', None)

             if console:
                 print (self.cmind.cfg['line'])
                 print ('Alias:    {}'.format(alias))
                 if url!='':
                     print ('URL:      {}'.format(url))
                 if branch!='':
                     print ('Branch:   {}'.format(branch))
                 if checkout!='':
                     print ('Checkout: {}'.format(checkout))
                 if depth!='' and depth!=None:
                     print ('Depth:    {}'.format(str(depth)))
                 print ('')

             # Prepare path to repo
             repos = self.cmind.repos

             r = repos.pull(alias = alias,
                            url = url,
                            branch = branch,
                            checkout = checkout,
                            console = console,
                            desc=desc,
                            prefix=prefix,
                            depth=depth,
                            path_to_repo=path_to_repo,
                            checkout_only=checkout_only,
                            skip_zip_parent_dir=skip_zip_parent_dir)
             if r['return']>0: return r

             repo_meta = r['meta']

             repo_metas[alias] = repo_meta

             if len(r.get('warnings', []))>0:
                 warnings += r['warnings']

        if len(pull_repos)>0 and self.cmind.use_index:
            if console:
                print (self.cmind.cfg['line'])

            ii = {'out':'con'} if console else {}
            rx = self.reindex(ii)

        print_warnings(warnings)    

        return {'return':0, 'meta':repo_meta, 'metas': repo_metas}



    ############################################################
    def checkout(self, i):
        """
        Checkout repository

        Args:
            (branch) (str): branch name
            (checkout) (str): checkout

            See "pull" action

        Returns: 
            See "pull" action
        """

        i['checkout_only'] = True

        return self.pull(i)


    ############################################################
    def show(self, i):
        """
        Show verbose info about registered CM repos.

        Args:
            See "search" action

        Returns: 
            See "search" action
        """

        i['verbose'] = True

        return self.search(i)


    ############################################################
    def search(self, i):
        """
        List registered CM repos.

        Args:
            (CM input dict):

            (with_prefix) (bool): if True return path to repo artifacts (with prefix if exists)

            (out) (str): if 'con', output to console

            (verbose) (bool): if True show extra info about repositories

            parsed_artifact (list): prepared in CM CLI or CM access function - repository name with wildcards

            (min) (bool): if True, return only path

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

            * list (list): list of CM repository objects
        """

        console = i.get('out') == 'con'

        with_prefix = i.get('with_prefix', False)

        lst = []

        parsed_artifact = i.get('parsed_artifact',[])

        min_out = i.get('min',False)

        artifact_obj = parsed_artifact[0] if len(parsed_artifact)>0 else ('','')
        artifact_repo = parsed_artifact[1] if len(parsed_artifact)>1 else None

        artifact_repo_wildcards = False
        if artifact_repo is not None:
            if '*' in artifact_repo[0] or '?' in artifact_repo[0]:
                artifact_repo_wildcards = True

        for repo in self.cmind.repos.lst:
            meta = repo.meta

            uid = meta['uid']
            alias = meta.get('alias','')

            r = utils.match_objects(uid = uid, 
                                    alias = alias,
                                    uid2 = artifact_obj[1],
                                    alias2 = artifact_obj[0])
            if r['return']>0: return r

            if r['match']:
                lst.append(repo)

        # Output paths to console if CLI or forced
        if console:
            for l in lst:
                meta = l.meta
                alias = meta.get('alias', '')
                uid = meta.get('uid', '')
                prefix = meta.get('prefix', '')

                path = l.path_with_prefix if with_prefix else l.path

                if min_out:
                    print (path)
                else:
                    if i.get('verbose', False):

                       uid = meta['uid']
                       desc = meta.get('desc', '')
                       git = meta.get('git', False)
                       prefix = meta.get('prefix', '')

                       local_alias = os.path.basename(path)

                       if alias == 'local' or alias == 'internal' or local_alias == 'ck':
                           local_alias = ''
                       
                       print (self.cmind.cfg['line'])
                       print ('Path:               {}'.format(path))
                       if prefix != '':
                           print ('  CM sub-directory: {}'.format(prefix))

                       if alias != local_alias:
                           if local_alias!='':
                               print ('  Alias:            {}'.format(local_alias))
                               print ('  Original alias:   {}'.format(alias))
                           else:
                               print ('  Alias:            {}'.format(alias))
                       else:
                           print ('  Alias:            {}'.format(alias))

                       print ('  UID:              {}'.format(uid))
                       if desc != '':
                           print ('Description:        {}'.format(desc))
                       print ('Git:                {}'.format(str(git)))

                       if git:
                           url = ''
                           branch = ''
                           checkout = ''

                           r = self.cmind.access({'action':'system', 'automation':'utils', 'path':path, 'cmd':'git config --get remote.origin.url'})
                           if r['return'] == 0 and r['ret'] == 0:
                               url = r['stdout']

                           r = self.cmind.access({'action':'system', 'automation':'utils', 'path':path, 'cmd':'git rev-parse --abbrev-ref HEAD'})
                           if r['return'] == 0 and r['ret'] == 0:
                               branch = r['stdout']
                               
                           r = self.cmind.access({'action':'system', 'automation':'utils', 'path':path, 'cmd':'git rev-parse HEAD'})
                           if r['return'] == 0 and r['ret'] == 0:
                               checkout = r['stdout']
                           
                           
                           if url!='':
                               print ('  URL:              {}'.format(url))
                           if branch!='':
                               print ('  Branch:           {}'.format(branch))
                           if checkout!='':
                               print ('  Checkout:         {}'.format(checkout))

                    else:
                       print ('{},{} = {}'.format(alias, uid, path))

        return {'return':0, 'list':lst}

    ############################################################
    def where(self, i):
        """
        Print only path to a given repo

        Args:
            (CM input dict):

            The same as "search"

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

            * list (list): list of updated CM repository objects
        """

        i['min']=True

        return self.search(i)

    ############################################################
    def update(self, i):
        """
        Update all Git-based CM repositories (git pull).

        Args:
            (CM input dict):

            (out) (str): if 'con', output to console

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

            * list (list): list of updated CM repository objects
        """

        console = i.get('out') == 'con'

        for repo in self.cmind.repos.lst:
            meta = repo.meta

            alias = meta.get('alias','')

            git = meta.get('git', False)

            if git:
                if console:
                    print ('Updating "{}" ...'.format(alias))
                    print ('')
                r = self.cmind.repos.pull(alias = alias, console = console)
                if r['return']>0: return r

        return {'return':0, 'list':self.cmind.repos.lst}

    ############################################################
    def delete(self, i):
        """
        Delete CM repository (either just unregister it or delete the content too).

        Args:
            (CM input dict):

            (out) (str): if 'con', output to console

            (verbose) (bool) - if True show extra info about repositories

            parsed_artifact (list): prepared in CM CLI or CM access function - repository name with wildcards

            (all) (bool) - if True, remove with content otherwise just unlink

            (force) (bool) - if True, do not ask questions
            (f) (bool) - if True, do not ask questions

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

        """

        console = i.get('out') == 'con'

        force = (i.get('force',False) or i.get('f',False))

        artifact = i.get('artifact','').strip()

        if artifact == '':
            return {'return':1, 'error':'repositories are not specified'}

        # Search CM repository
        i['action']='search'
        i['out']=None
        r=self.cmind.access(i)

        if r['return'] >0 : return r

        lst = r['list']
        if len(lst)==0:
           return {'return':1, 'error':'Repository not found'}

        remove_all = i.get('all', '')

        r = self.cmind.repos.delete(lst, remove_all = remove_all, console = console, force = force)

        if self.cmind.use_index:
            ii = {'out':'con'} if console else {}
            rx = self.reindex(ii)
        
        return r

    ############################################################
    def ximport(self, i):

        if i.get('path','')!='':
            i['here']=True

        return self.init(i)

    ############################################################
    def init(self, i):
        """
        Initialize CM repository.

        Args:
            (CM input dict):

            (out) (str): if 'con', output to console

            (artifact) (str): repository name (alias)
            (uid) (str): force CM UID for this repository
            (path) (str): specify a path where to create this repository
            (here) (str): use current path
            (desc) (str): brief repository description (1 line)
            (prefix) (str): extra directory to keep CM artifacts

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

            * CM repository object
        """

        console = i.get('out') == 'con'

        alias = i.get('artifact', '')
        uid = i.get('uid','')
        path = i.get('path', '')
        desc = i.get('desc','')
        prefix = i.get('prefix','')

        # If path is not specified, initialize in the current directory!
        if (path=='' and alias=='') or (alias!='' and (path=='.' or i.get('here', False))):
           path = os.path.abspath(os.getcwd())

        # Check if there is a repo in a path
        r = self.cmind.access({'action':'detect',
                               'automation':self.meta['alias']+','+self.meta['uid'],
                               'path':path})
        if r['return']>0: return r

        repo_desc_found = r['found']
        repo_registered = r.get('registered',False)

        if repo_desc_found:
            if repo_registered:
                return {'return':1, 'error':'CM repository found in this path and already registered in CM'}

            if console:
                print ('CM repository description found in this path: {}'.format(r['path_to_repo_desc']))

            path= r['path_to_repo']

            repo_meta = r['meta']

            repo_meta_alias = repo_meta.get('alias','')
            repo_meta_uid = repo_meta.get('uid','')
            repo_meta_prefix = repo_meta.get('prefix','')

            # Check if mismatch in alias
            if alias!='':
                if repo_meta_alias!='' and repo_meta_alias!=alias:
                    return {'return':1, 'error':'mismatch between new repo alias and the existing one'}
            else:
                alias = repo_meta_alias

            # Check if mismatch in UID
            if uid!='':
                if repo_meta_uid!='' and repo_meta_uid!=uid:
                    return {'return':1, 'error':'mismatch between new repo UID and the existing one'}
            else:
                uid = repo_meta_uid

            # Check if mismatch in prefix
            if prefix!='':
                if repo_meta_prefix!='' and repo_meta_prefix is not None and repo_meta_prefix!=prefix:
                    return {'return':1, 'error':'mismatch between new repo prefix and the existing one'}
            else:
                prefix = repo_meta_prefix

        # If still no alias, use from the path
        if alias == '':
            # Try to get the name of the directory
            alias = os.path.basename(path).strip().lower()

        # Generate UID
        if uid =='':
            r=utils.gen_uid()
            if r['return']>0: return r
            uid = r['uid']

        if alias == '': alias = uid

        if console:
            print (self.cmind.cfg['line'])
            print ('Alias:    {}'.format(alias))
            print ('UID:      {}'.format(uid))
            print ('Desc:     {}'.format(desc))
            print ('Prefix:   {}'.format(prefix))
            print ('')

        # Check if repository with this alias and UID doesn't exist
        for repo_artifact in [alias, uid]:
            ii={'automation':'repo', 'action':'search', 'artifact':repo_artifact}

            r=self.cmind.access(ii) 
            if r['return']>0: return r

            lst=r['list']

            if len(lst)>0: 
                return {'return':1, 'error':'Repository "{}" is already registered in CM'.format(repo_artifact)}

        # Create repository 
        r = self.cmind.repos.init(alias = alias, uid = uid, path = path, console = console, desc=desc, prefix=prefix, only_register=repo_desc_found)

        if self.cmind.use_index:
            ii = {'out':'con'} if console else {}
            rx = self.reindex(ii)
        
        warnings = r.get('warnings', [])
        print_warnings(warnings)
        
        return r

    ############################################################
    def add(self, i):
        """
        The same as "init".
        """

        return self.init(i)

    ############################################################
    def pack(self, i):
        """
        Pack CM repository to cm.zip file.

        Args:
            (CM input dict):

            (out) (str): if 'con', output to console

            (artifact) (str): repository name (alias)

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

            * CM repository object

        """

        import zipfile

        console = i.get('out') == 'con'

        # Search repository
        i['out']=None
        r = self.search(i)

        if r['return']>0: return r

        lst = r['list']

        if len(lst)==0:
            return {'return':16, 'error':'no repsitories found'}
        elif len(lst)>1:
            return {'return':16, 'error':'more than 1 repository found'}

        repo = lst[0]

        repo_path = repo.path

        pack_file = self.cmind.cfg['default_repo_pack']

        if console:
            print ('Packing repo from {} to {} ...'.format(repo_path, pack_file))

        r = utils.list_all_files({'path': repo_path, 'all': 'yes', 'ignore_names':['.git']})
        if r['return'] > 0: return r

        files = r['list']

        # Prepare zip archive
        try:
            f = open(pack_file, 'wb')
            z = zipfile.ZipFile(f, 'w', zipfile.ZIP_DEFLATED)

            for fn in files:
                path_to_file = os.path.join(repo_path, fn)
                z.write(path_to_file, fn, zipfile.ZIP_DEFLATED)

            z.close()
            f.close()

        except Exception as e:
            return {'return': 1, 'error': 'failed to pack repo: {}'.format(format(e))}

        return {'return':0}

    ############################################################
    def unpack(self, i):
        """
        Unpack cm.zip and create a CM repository.

        Args:
            (CM input dict):

            (out) (str): if 'con', output to console

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

            * CM repository object
        """

        import zipfile

        console = i.get('out') == 'con'

        pack_file = self.cmind.cfg['default_repo_pack']

        if not os.path.isfile(pack_file):
            return {'return':16, 'error':'CM repo pack file not found {}'.format(pack_file)}

        # Attempt to read cmr.json 
        repo_pack_file = open(pack_file, 'rb')
        repo_pack_zip = zipfile.ZipFile(repo_pack_file)

        repo_pack_desc = self.cmind.cfg['file_meta_repo']

        files=repo_pack_zip.namelist()

        repo_meta = {}

        file_yaml = repo_pack_desc + '.yaml'
        if file_yaml in files:
            repo_meta_yaml = repo_pack_zip.read(file_yaml)

            import yaml

            repo_meta.update(yaml.load(repo_meta_yaml, Loader=yaml.FullLoader))

        file_json = repo_pack_desc + '.json'
        if file_json in files:
            repo_meta_json = repo_pack_zip.read(file_json)

            import json

            repo_meta.update(json.load(repo_meta_json))

        # Get meta info
        uid = repo_meta['uid']
        alias = repo_meta['alias']
        desc = repo_meta.get('desc','')
        prefix = repo_meta.get('prefix','')

        # Check if repo exists
        r = self.search({'parsed_artifact':[(alias,uid)]})
        if r['return']>0: return r

        lst = r['list']

        if len(lst)>0:
            return {'return':1, 'error':'Repository already exists'}

        # Initialize repository
        r_new = self.init({'artifact':alias,
                           'uid':uid,
                           'prefix':prefix})
        if r_new['return']>0: return r_new

        repo_path = r_new['path_to_repo']

        if console:
            print ('Unpacking {} to {} ...'.format(pack_file, repo_path))

        # Unpacking zip
        for f in files:
            if not f.startswith('..') and not f.startswith('/') and not f.startswith('\\'):
                file_path = os.path.join(repo_path, f)
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

        if self.cmind.use_index:
            ii = {'out':'con'} if console else {}
            rx = self.reindex(ii)
        
        return r_new

    ##############################################################################
    def import_ck_to_cm(self, i):
        """
        Convert all legacy CK repositories to CM repositories

        Args:
            (CM input dict): None

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

        """

        import ck.kernel as ck
        import cmind
        import os

        r=ck.access({'action':'search',
                     'module_uoa':'repo',
                     'add_meta':'yes'})
        if r['return']>0: return r

        lst=r['lst']

        for l in lst:
            ruoa=l['data_uoa']
            ruid=l['data_uid']

            rmeta=l['meta']

            rpath=rmeta.get('path','')

            if rpath!='' and os.path.isdir(rpath):
                print ('********************************************************')
                print (ruoa)
                print (rpath)

                r=cmind.access({'automation':'repo',
                                'action':'init',
                                'artifact':ruoa,
                                'path':rpath})
                if r['return']>0: return r

                r = convert_ck_dir_to_cm(rpath)
                if r['return']>0: return r

        return {'return':0}

    ##############################################################################
    def convert_ck_to_cm(self, i):
        """
        Convert a CM repository with CK artifacts into CM artifacts

        Args:
            (CM input dict):

            (artifact) (str): CM repository name (alias)

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

        """

        import ck.kernel as ck
        import cmind
        import os


        console = i.get('out') == 'con'

        # Search CM repository
        i['action']='search'
        i['out']=None
        r=self.cmind.access(i)

        if r['return'] >0 : return r

        lst = r['list']
        if len(lst)==0:
           return {'return':1, 'error':'Repository not found'}

        for repo in lst:

            ralias = repo.meta['alias']
            ruid = repo.meta['uid']
            rpath = repo.path

            if rpath!='' and os.path.isdir(rpath):
                print ('********************************************************')
                print (ralias)
                print (ruid)
                print (rpath)

                r = convert_ck_dir_to_cm(rpath)
                if r['return']>0: return r

        return {'return':0}


    ############################################################
    def detect(self, i):
        """
        Detect CM repository in the current path.

        Args:
            (CM input dict):

            (path) (str): specify path where to detect CM repo. 
                          Use current path otherwise.

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

            * found (bool): True if found

            * path_to_repo (str): path to repo if repo found
            * path_to_repo_desc (str): path to repo description if repo found

            * found_in_current_path (bool): if True, found in the current directory

            * meta (dict): meta of the found repo

            * cm_repo (str): CM repo object (alias,UID)

            * registered (bool): True, if this repository is registered in CM

            * artifact_found (bool): True, if CM artifact found in the current path

            * path_to_artifact (str): path to artifact if found
            * path_to_artifact_desc (str): path to artifact description if found

            * artifact_found_in_current_path (str): artifact found in the current directory

            * artifact_meta (dict): artifact meta description

            * cm_artifact (str): CM artifact object (alias,UID)

            * cm_automation (str): CM automation object (alias,UID)

        """

        console = i.get('out') == 'con'

        # Prepare path to repo
        repos = self.cmind.repos

        path = i.get('path')
        if path == '': path = None

        # Search for cmr.yaml or cmr.json in current directory and above
        r=utils.find_file_in_current_directory_or_above([self.cmind.cfg['file_meta_repo']+'.json', 
                                                         self.cmind.cfg['file_meta_repo']+'.yaml'],
                                                         path_to_start = path)
        if r['return']>0: return r

        rr = {'return':0}

        found = r['found']
        rr['found'] = found

        registered = False

        if found:
            path_to_repo_desc = r['path_to_file']
            path_to_repo = r['path']

            rr['path_to_repo_desc'] = path_to_repo_desc
            rr['path_to_repo'] = path_to_repo

            rr['found_in_current_path'] = r['found_in_current_path']

            # Load meta
            r = utils.load_json_or_yaml(path_to_repo_desc)
            if r['return']>0: return r

            repo_meta = r['meta']

            rr['meta'] = repo_meta

            # Check if belongs to installed repo already
            path_to_repo_real = os.path.realpath(path_to_repo)

            if path_to_repo_real == os.path.realpath(repos.path_to_internal_repo):
                registered = True

            if not registered:
                for tmp_path in repos.paths:
                    if path_to_repo_real == os.path.realpath(tmp_path):
                        registered = True

            if registered:
                rr['cm_repo'] = utils.assemble_cm_object(repo_meta['alias'],repo_meta['uid'])

        rr['registered'] = registered

        artifact_found = False
        artifact_found_in_current_path = False

        if found:
            for reverse in [False, True]:
                r=utils.find_file_in_current_directory_or_above([self.cmind.cfg['file_cmeta']+'.json', 
                                                                 self.cmind.cfg['file_cmeta']+'.yaml'],
                                                                 path_to_start = path,
                                                                 reverse = reverse,
                                                                 path_to_stop = path_to_repo_real)
                if r['return']>0: return r

                artifact_found = r['found']
                artifact_found_in_current_path = r.get('found_in_current_path', False)

                rr['artifact_found'] = artifact_found

                if artifact_found:
                    path_to_artifact_desc = r['path_to_file']
                    path_to_artifact = r['path']

                    rr['path_to_artifact_desc'] = path_to_artifact_desc
                    rr['path_to_artifact'] = path_to_artifact

                    rr['artifact_found_in_current_path'] = artifact_found_in_current_path
                    rr['artifact_reverse_search'] = reverse

                    # Load meta
                    path_to_artifact_desc_without_ext = path_to_artifact_desc
                    j = path_to_artifact_desc.rfind('.')
                    if j>=0:
                        path_to_artifact_desc_without_ext=path_to_artifact_desc[:j]

                    r = utils.load_yaml_and_json(path_to_artifact_desc_without_ext)
                    if r['return']>0: return r

                    artifact_meta = r['meta']

                    rr['artifact_meta'] = artifact_meta

                    rr['cm_automation'] = utils.assemble_cm_object(artifact_meta['automation_alias'],artifact_meta['automation_uid'])

                    if not reverse or artifact_found_in_current_path:
                        rr['cm_artifact'] = utils.assemble_cm_object(artifact_meta['alias'],artifact_meta['uid'])

                    break

        # Print
        if console:
            if not found:
                print ('CM repository not found')
            else:
                print ('CM repository found:')

                print ('')
                print ('Path to repo desc file: {}'.format(path_to_repo_desc))
                print ('Path to repo:           {}'.format(path_to_repo))

                if registered:
                    print ('')
                    print ('  This repository is registered in CM')

                    print ('')
                    print ('  Repo alias: {}'.format(repo_meta['alias']))
                    print ('  Repo UID:   {}'.format(repo_meta['uid']))

                if artifact_found:
                    print ('')
                    print ('Current directory has related CM automation:')

                    print ('')
                    print ('  Automation alias: {}'.format(artifact_meta['automation_alias']))
                    print ('  Automation UID:   {}'.format(artifact_meta['automation_uid']))

                if artifact_found_in_current_path:
                    print ('')
                    print ('Current directory has a CM artifact:')

                    print ('')
                    print ('  Artifact alias: {}'.format(artifact_meta['alias']))
                    print ('  Artifact UID:   {}'.format(artifact_meta['uid']))

        return rr


    ############################################################
    def reindex(self, i):
        """
        Reindex all CM repositories

        Args:
            (CM input dict)

            (verbose) (bool): If True, print index

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

        """

        verbose = i.get('verbose', False)

        console = i.get('out') == 'con'

        if console:
            print ('')
            print ('Reindexing all CM artifacts. Can take some time ...')
        
        out = 'con' if verbose else ''
        
        # Clean index
        self.cmind.index.meta = {}
        
        import time
        t1 = time.time()

        r = self.cmind.access({'action':'search',
                               'automation':'*',
                               'out':out,
                               'skip_index_search':True,
                               'force_index_add':True})
        if r['return']>0: return r

        t2 = time.time() - t1

        if console:
            print ('Took {:.1f} sec.'.format(t2))

        # Save
        rx = self.cmind.index.save()

        # Ignore output for now to continue working even if issues ...
        if self.cmind.use_index:
            rx = self.cmind.index.load()
            # Ignore output for now to continue working even if issues ...


        return {'return':0, 'self_time':t2}



##############################################################################
def convert_ck_dir_to_cm(rpath):
    """
    Convert CK directory to the CM format (internal function).

    Args:
        rpath (str): path to a CK repository.

    Returns: 
        (CM return dict):

        * return (int): return code == 0 if no error and >0 if error
        * (error) (str): error string if return>0

    """

    import ck.kernel as ck
    import os

    dir1 = os.listdir(rpath)

    for d1 in dir1:
        if d1!='.cm':
            dd1=os.path.join(rpath, d1)
            if os.path.isdir(dd1):

                dir2 = os.listdir(dd1)

                for d2 in dir2:
                    if d2!='.cm':
                        dd2=os.path.join(dd1, d2, '.cm')
                        if os.path.isdir(dd2):
                            dmeta = {}

                            broken = False
                            for f in ['info.json','meta.json']:
                                dd2a=os.path.join(dd2, f)

                                if os.path.isfile(dd2a):

                                    r=ck.load_json_file({'json_file':dd2a})
                                    if r['return']>0: return r

                                    dmeta.update(r['dict'])
                                else:
                                    broken=True
                                    break

                            if broken or \
                               'backup_data_uid' not in dmeta or \
                               'backup_module_uid' not in dmeta or \
                               'backup_module_uoa' not in dmeta:

                               print ('Ignored: '+dd2)
                            else:
                               backup_data_uid = dmeta['backup_data_uid']

                               backup_module_uid = dmeta['backup_module_uid']
                               backup_module_uoa = dmeta['backup_module_uoa']

                               dmeta2 = {}
                               for k in dmeta:
                                   if not k.startswith('backup_') and not k.startswith('cm_'):
                                       dmeta2[k]=dmeta[k]

                               dmeta2['uid']=backup_data_uid

                               if not ck.is_uid(d2):
                                  dmeta2['alias']=d2

                               dmeta2['automation_alias']=backup_module_uoa
                               dmeta2['automation_uid']=backup_module_uid

                               cm_meta_file = os.path.join(dd1, d2, '_cm.json')

                               print (cm_meta_file)

                               r=ck.save_json_to_file({'json_file':cm_meta_file, 'dict': dmeta2, 'sort_keys':'yes'})
                               if r['return']>0: return r

    return {'return':0}

def print_warnings(warnings):

    if len(warnings)>0:
        print ('')
        print ('WARNINGS:')
        print ('')
        for w in warnings:
            print ('  {}'.format(w))
                                                                            
    return
