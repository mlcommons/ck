import os

from cmind.module import Module
from cmind import utils

class CModule(Module):
    """
    OS automation actions
    """

    ############################################################
    def __init__(self, cmind, module_name):
        super().__init__(cmind, module_name)

    ############################################################
    def pull(self, i):
        """
        Pull repo

        Args:
           (artifact) (str) - repository name
           (url) (str) - URL of a repository
           (branch) (str) - Git branch
           (checkout) (str) - Git checkout
           (name) (str) - user-friendly name
           (prefix) (str) - extra directory to keep CM artifacts
           
        """

        alias = i.get('artifact','')
        url = i.get('url','')
        name = i.get('name','')
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

        if self.cmind.con:
            print (self.cmind.cfg['line'])
            print ('Alias:    {}'.format(alias))
            print ('URL:      {}'.format(url))
            print ('Branch:   {}'.format(branch))
            print ('Checkout: {}'.format(checkout))
            print ('')
        
        # Prepare path to repo
        repos = self.cmind.repos

        r = repos.pull(alias = alias, url = url, branch = branch, checkout = checkout, con = self.cmind.con, name=name, prefix=prefix)
        if r['return']>0: return r

        repo_meta = r['meta']

        return {'return':0, 'meta':repo_meta}

    ############################################################
    def search(self, i):
        """
        List repos

        Args:
         (verbose) (bool) - if True show extra info about repositories
           
        """

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
        if self.cmind.con and not i.get('skip_con', False):
            for l in lst:
                meta = l.meta
                alias = meta.get('alias','')

                if i.get('verbose',False):

                   uid = meta['uid']
                   name = meta.get('name','')
                   path = repo.path
                   git = meta.get('git',False)

                   print ('{},{} "{}" {}'.format(alias,uid,name,path))
                else:
                   print ('{} = {}'.format(alias, l.path))

        return {'return':0, 'lst':lst}

    ############################################################
    def update(self, i):
        """
        Update repos

        Args:
         (verbose) (bool) - if True show extra info about repositories
           
        """

        for repo in self.cmind.repos.lst:
            meta = repo.meta
            
            alias = meta.get('alias','')

            git = meta.get('git', False)

            if git:
                if self.cmind.con:
                    print ('Updating "{}" ...'.format(alias))
                    print ('')
                r = self.cmind.repos.pull(alias = alias, con = self.cmind.con)
                if r['return']>0: return r

        return {'return':0, 'lst':self.cmind.repos.lst}

    ############################################################
    def delete(self, i):
        """
        Delete repo (just unlink or remove content too)

        Args:
           (artifact) (str) - repository name
           (all) (bool) - if True, remove with content otherwise just unlink
           
        """

        alias = i.get('artifact', '')
        remove_all = i.get('all', '')

        # Prepare path to repo
        repos = self.cmind.repos

        r = repos.delete(alias = alias, remove_all = remove_all, con = self.cmind.con)

        return r

    ############################################################
    def init(self, i):
        """
        Initialize repo

        Args:
           (artifact) (str) - repository name
           (path) (str) - if !='' use this non-standard path
           (name) (str) - user-friendly name
           (prefix) (str) - extra directory to keep CM artifacts
        """

        con = True if self.cmind.con and not i.get('skip_con', False) else False

        alias = i.get('artifact', '')
        path = i.get('path', '')
        name = i.get('name','')
        prefix = i.get('prefix','')

        uid = i.get('uid','')
        if uid =='':
            r=utils.gen_uid()
            if r['return']>0: return r
            uid = r['uid']

        if alias == '': alias = uid

        if con:
            print (self.cmind.cfg['line'])
            print ('Alias:    {}'.format(alias))
            print ('UID:      {}'.format(uid))
            print ('Name:     {}'.format(name))
            print ('Prefix:   {}'.format(prefix))
            print ('')
        
        # Prepare path to repo
        repos = self.cmind.repos

        r = repos.init(alias = alias, uid = uid, path = path, con = self.cmind.con, name=name, prefix=prefix)
        return r

    ############################################################
    def add(self, i):
        """
        Initialize repo

        Args:
           (artifact) (str) - repository name
           (path) (str) - if !='' use this non-standard path
           (name) (str) - user-friendly name
           (prefix) (str) - extra directory to keep CM artifacts
        """

        return self.init(i)

    ############################################################
    def pack(self, i):
        """
        Pack repo for further distribution

        Args:
           (artifact) (str) - repository name
        """

        import zipfile

        con = True if self.cmind.con and not i.get('skip_con', False) else False
        
        # Search repository
        i['skip_con']=True
        r = self.search(i)
        if r['return']>0: return r

        lst = r['lst']

        if len(lst)==0:
            return {'return':16, 'error':'no repsitories found'}
        elif len(lst)>1:
            return {'return':16, 'error':'more than 1 repository found'}

        repo = lst[0]

        repo_path = repo.path

        pack_file = self.cmind.cfg['default_repo_pack']

        if con:
            print ('Packing repo from {} to {} ...'.format(repo_path, pack_file))

        r = utils.list_all_files({'path': repo_path, 'all': 'yes'})
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
        Unpack repository

        Args:
           (artifact) (str) - CM repo pack file name
        """

        import zipfile

        con = True if self.cmind.con and not i.get('skip_con', False) else False

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
        name = repo_meta.get('name','')
        prefix = repo_meta.get('prefix','')

        # Check if repo exists
        r = self.search({'parsed_artifact':[(alias,uid)], 'skip_con':True})
        if r['return']>0: return r

        lst = r['lst']

        if len(lst)>0:
            return {'return':1, 'error':'Repository already exists'}

        # Initialize repository
        r_new = self.init({'artifact':alias,
                           'uid':uid,
                           'prefix':prefix,
                           'skip_con':True})
        if r_new['return']>0: return r_new

        repo_path = r_new['path_to_repo']

        if con:
            print ('Unpacking {} to {} ...'.format(pack_file, repo_path))

        # Unpacking zip
        for f in files:
            if not f.startswith('.') and not f.startswith('/') and not f.startswith('\\'):
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
    def convert_ck_to_cm(self, i):
        """
        Convert CK repos to CM repos
        
        Input:  {
                }

        Output: {
                  return       - return code =  0, if successful
                                             >  0, if error
                  (error)      - error text if return > 0
                }

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
