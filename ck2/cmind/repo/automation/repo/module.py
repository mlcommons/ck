import os

from cmind.automation import Automation
from cmind import utils

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
          (branch) (str): Git branch
          (checkout) (str): Git checkout
          (desc) (str): brief repository description (1 line)
          (prefix) (str): extra directory to keep CM artifacts

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

        if url == '':
            if alias != '':
                url = self.cmind.cfg['repo_url_prefix']

                if '@' not in alias:
                    alias = self.cmind.cfg['repo_url_org'] + '@' + alias

                url += alias.replace('@','/')
        else:
           if alias == '':
               # Get alias from URL
               alias = url
               if alias.endswith('.git'): alias=alias[:-4]

               j = alias.find('//')
               if j>=0:
                   j1 = alias.find('/', j+2)
                   if j1>=0:
                       alias = alias[j1+1:].replace('/','@')

        if url == '':
            return {'return':1, 'error':'TBD: no URL - need to update all Git repos'}

        # Branch and checkout
        branch = i.get('branch','')
        checkout = i.get('checkout','')

        if console:
            print (self.cmind.cfg['line'])
            print ('Alias:    {}'.format(alias))
            print ('URL:      {}'.format(url))
            print ('Branch:   {}'.format(branch))
            print ('Checkout: {}'.format(checkout))
            print ('')

        # Prepare path to repo
        repos = self.cmind.repos

        r = repos.pull(alias = alias, url = url, branch = branch, checkout = checkout, console = console, desc=desc, prefix=prefix)
        if r['return']>0: return r

        repo_meta = r['meta']

        return {'return':0, 'meta':repo_meta}

    ############################################################
    def search(self, i):
        """
        List registered CM repos.

        Args:
            (CM input dict):

            (out) (str): if 'con', output to console

            (verbose) (bool) - if True show extra info about repositories

            parsed_artifact (list): prepared in CM CLI or CM access function - repository name with wildcards

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

            * list (list): list of CM repository objects
        """

        console = i.get('out') == 'con'

        lst = []

        parsed_artifact = i.get('parsed_artifact',[])

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
                alias = meta.get('alias','')
                uid = meta.get('uid','')

                if i.get('verbose',False):

                   uid = meta['uid']
                   desc = meta.get('desc','')
                   path = repo.path
                   git = meta.get('git',False)

                   print ('{},{} "{}" {}'.format(alias, uid, desc, path))
                else:
                   print ('{},{} = {}'.format(alias, uid, l.path))

        return {'return':0, 'list':lst}

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

        return r

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
        if (path=='' and alias=='') or (alias!='' and path=='.'):
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
            r = utils.load_json_or_yaml(file_name = path_to_repo_desc)
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

        # If repository found, search for _cm.yaml or _cm.json in current directory and below
        artifact_found = False
        artifact_found_in_current_path = False

        if found:
            r=utils.find_file_in_current_directory_or_above([self.cmind.cfg['file_cmeta']+'.json', 
                                                             self.cmind.cfg['file_cmeta']+'.yaml'],
                                                             path_to_start = path,
                                                             reverse = True)
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

                # Load meta
                r = utils.load_json_or_yaml(file_name = path_to_artifact_desc)
                if r['return']>0: return r

                artifact_meta = r['meta']

                rr['artifact_meta'] = artifact_meta

                rr['cm_automation'] = utils.assemble_cm_object(artifact_meta['automation_alias'],artifact_meta['automation_uid'])

                if artifact_found_in_current_path:
                    rr['cm_artifact'] = utils.assemble_cm_object(artifact_meta['alias'],artifact_meta['uid'])

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
