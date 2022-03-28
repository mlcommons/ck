# Collective Mind module

import os

from cmind import utils
from cmind.artifact import Artifact

def init(cmind):
    
    module = Module(cmind, __file__)

    module.meta = {'alias':'module',
                   'uid':'087bf3c4403b9573'}
    
    return {'return':0, 'module':module}


class Module:
    ############################################################
    def __init__(self, cmind, module_file):
        """
        Initialize class and reuse initialized cmind class
        """

        self.cmind = cmind

        self.module_path = module_file
        self.path = os.path.dirname(self.module_path)

    ############################################################
    def search(self, i):
        """
        List CM artifacts
        (simple and slow implementation - can be considerably accelerated with on-the-fly indexing as in CK)

        Args:
            i (dict):
                (parsed_automation) - tuple: automation (alias,UID) (repo (alias,UID))

                (ignore_inheritance) - if True, ignore inheritance and just load meta to match UID/alias

        Returns:
            Dictionary:
                return (int): return code == 0 if no error 
                                          >0 if error

                (error) (str): error string if return>0

        """

        con = True if self.cmind.con and not i.get('skip_con', False) else False

        lst = []

        # Check tags
        tags = utils.get_list_from_cli(i, key='tags')

        ignore_inheritance = i.get('ignore_inheritance',False) == True

        # Get parsed automation
        # First object in a list is an automation
        # Second optional object in a list is a repo
        parsed_automation = i.get('parsed_automation',[])

        auto_name = parsed_automation[0] if len(parsed_automation)>0 else ('','')
        
        # Get parsed artifact
        parsed_artifact = i.get('parsed_artifact',[])

        artifact_obj = parsed_artifact[0] if len(parsed_artifact)>0 else ('','')
        artifact_repo = parsed_artifact[1] if len(parsed_artifact)>1 else None

        artifact_repo_wildcards = False
        if artifact_repo is not None:
            if '*' in artifact_repo[0] or '?' in artifact_repo[0]:
                artifact_repo_wildcards = True

        # Prune repos if needed (check wildcards too)
        repos = self.cmind.repos.lst
        pruned_repos = []

        for repo in repos:
            add_repo = True

            if artifact_repo is not None:
                repo_uid = repo.meta['uid']
                if repo_uid == '': repo_uid = None

                repo_alias = repo.meta['alias']
                if repo_alias == '': repo_alias = None

                r = utils.match_objects(uid = repo_uid, 
                                        alias = repo_alias,
                                        uid2 = artifact_repo[1],
                                        alias2 = artifact_repo[0])
                if r['return']>0: return r

                add_repo = r['match']

            if add_repo:
                 pruned_repos.append(repo)

        # Iterate over pruned repositories
        for repo in pruned_repos:
            path_repo = repo.path_with_prefix

            automations = os.listdir(path_repo)
            
            for automation in automations:
                path_automations = os.path.join(path_repo, automation)

                if os.path.isdir(path_automations):
                    # Pruning by automation
                    # Will need to get first entry to get UID and alias of the automation

                    path_artifacts = os.path.join(path_repo, path_automations)

                    artifacts = os.listdir(path_artifacts)

                    # Check if artifact is first to get meta about automation UID/alias
                    first_artifact = True

                    for artifact in artifacts:
                        path_artifact = os.path.join(path_artifacts, artifact)

                        if os.path.isdir(path_artifact):
                            # Check if has CM meta to make sure that it's a CM object
                            path_artifact_meta = os.path.join(path_artifact, self.cmind.cfg['file_cmeta'])

                            r = utils.is_file_json_or_yaml(file_name = path_artifact_meta)
                            if r['return']>0: return r

                            if r['is_file']:
                                # Load artifact class
                                artifact_object = Artifact(cmind = self.cmind, path = path_artifact)

                                r = artifact_object.load(ignore_inheritance = ignore_inheritance)
                                if r['return']>0: return r

                                meta = artifact_object.meta

                                uid = meta.get('uid', '')
                                if uid==None: uid = ''

                                alias = meta.get('alias', '')
                                if alias==None: alias = ''

                                if first_artifact:
                                    # Need to check if automation matches
                                    first_artifact = False
                                    
                                    automation_uid = meta.get('automation_uid')
                                    automation_alias = meta.get('automation_alias')
                                    
                                    r = utils.match_objects(uid = automation_uid, 
                                                            alias = automation_alias,
                                                            uid2 = auto_name[1],
                                                            alias2 = auto_name[0])
                                    if r['return']>0: return r

                                    if not r['match']:
                                        break

                                # Match object
#                                print ("'{}','{}','{}','{}'".format(uid,alias,artifact_obj[1],artifact_obj[0]))
                                r = utils.match_objects(uid = uid,
                                                        alias = alias,
                                                        uid2 = artifact_obj[1],
                                                        alias2 = artifact_obj[0])
                                if r['return']>0: return r

                                if r['match']:

                                    if len(tags)>0:
                                        tags_in_meta = meta.get('tags',[])

                                        if not all(t in tags_in_meta for t in tags):
                                            continue

                                    lst.append(artifact_object)



        # Output paths to console if CLI or forced
        if con:
            for l in lst:
                print (l.path)

        return {'return':0, 'list':lst}


    ############################################################
    def add(self, i):
        """
        Add Collective Mind object

           parsed_automation
           parsed_artifact
           meta
           tags
           skip_con


        """

        con = True if self.cmind.con and not i.get('skip_con', False) else False

        # Get parsed automation
        parsed_automation = i.get('parsed_automation',[])

        auto_name = parsed_automation[0] if len(parsed_automation)>0 else ('','')

        # Get parsed artifact
        parsed_artifact = i.get('parsed_artifact',[])

        artifact_obj = parsed_artifact[0] if len(parsed_artifact)>0 else ('','')
        artifact_repo = parsed_artifact[1] if len(parsed_artifact)>1 else None

        # If artifact repo is not defined, use "local" (like scratchpad)
        if artifact_repo == None:
            artifact_repo = (self.cmind.cfg['local_repo_meta']['alias'],
                             self.cmind.cfg['local_repo_meta']['uid'])

        # Find repository
        r = self.cmind.access({'automation':'repo',
                               'action':'find',
                               'artifact':artifact_repo[0]+','+artifact_repo[1],
                               'skip_con':True})
        if r['return']>0: return r

        lst = r['lst']

        if len(lst)==0:
            return {'return':16, 'error':'repository {} not found'.format(artifact_repo)}

        if len(lst)>1:
            return {'return':1, 'error':'more than 1 repository found'}

        repo = lst[0]

        repo_path = repo.path_with_prefix

        # Check automation (if exists)
        automation_path = os.path.join(repo_path, auto_name[0]) if auto_name[0]!='' else os.path.join(repo_path, auto_name[1])

        if not os.path.isdir(automation_path):
            os.makedirs(automation_path)

        # Check object UID
        if artifact_obj[1]=='' or artifact_obj[1] is None:
            r=utils.gen_uid()
            if r['return']>0: return r

            artifact_obj=(artifact_obj[0],r['uid'])

        obj_path = os.path.join(automation_path, artifact_obj[0]) if artifact_obj[0]!='' else os.path.join(automation_path, artifact_obj[1])

        meta_path_yaml = os.path.join(obj_path, self.cmind.cfg['file_cmeta']+'.yaml')
        meta_path_json = os.path.join(obj_path, self.cmind.cfg['file_cmeta']+'.json')

        # Check if artifact meta exists - then object already exists
        if os.path.isfile(meta_path_yaml) or os.path.isfile(meta_path_json):
            return {'return':8, 'error':'artifact already exists in the path {}'.format(obj_path)}

        if not os.path.isdir(obj_path):
            os.makedirs(obj_path)

        # Prepare meta
        meta = i.get('meta',{})
        tags = utils.get_list_from_cli(i, key='tags')

        if meta.get('alias','')=='': meta['alias']=artifact_obj[0]
        if meta.get('uid','')=='': meta['uid']=artifact_obj[1]
        if meta.get('automation_alias','')=='': meta['automation_alias']=auto_name[0]
        if meta.get('automation_uid','')=='': meta['automation_uid']=auto_name[1]

        existing_tags = meta.get('tags',[])
        if len(tags)>0: 
            existing_tags.append(tags)
        meta['tags']=existing_tags

        # Record meta
        r = utils.save_json(meta_path_json, meta=meta)
        if r['return']>0: return r

        if con:
            print ('Added CM object at {}'.format(obj_path))

        return {'return':0, 'meta':meta, 'path':obj_path}

    ############################################################
    def delete(self, i):
        """
        Delete Collective Mind artifact

           parsed_automation
           parsed_artifact
           skip_con
           f or force (bool) - if True do not ask for confirmation


        """

        import shutil
        
        con = True if self.cmind.con and not i.get('skip_con', False) else False
        force = True if i.get('f', False) or i.get('force',False) else False

        # Find an object
        i['skip_con']=True

        r = self.search(i)
        if r['return']>0: return r

        lst = r['list']
        if len(lst)==0:
            return {'return':16, 'error':'artifact(s) not found'}

        deleted_lst = []
        
        for artifact in lst:
            path_to_artifact = artifact.path

            if con:
                print ('Deleting CM artifact in {} ...'.format(path_to_artifact))

                if not force:
                    ask = input('  Are you sure you want to delete this artifact (y/N): ')
                    ask = ask.strip().lower()

                    if ask!='y':
                        print ('    Skipped!')
                        continue
            elif not force:
                # If not console mode skip unless forced
                continue
               
            # Deleting artifact
            deleted_lst.append(artifact)

            shutil.rmtree(path_to_artifact)
            
            if con:
                print ('    Deleted!')

        return {'return':0, 'deleted_list':deleted_lst}

    ############################################################
    def load(self, i):
        """
        Load Collective Mind artifact

           parsed_automation
           parsed_artifact
           skip_con

        """

        con = True if self.cmind.con and not i.get('skip_con', False) else False

        # Find an object
        i['skip_con']=True

        r = self.search(i)
        if r['return']>0: return r

        lst = r['list']
        if len(lst)==0:
            return {'return':16, 'error':'artifact not found: {}'.format(i)}
        elif len(lst)>1:
            return {'return':1, 'error':'more than 1 artifact found', 'lst':lst}

        artifact = lst[0]

        path = artifact.path
        meta = artifact.meta

        # Output if con
        if con:
            import json
            print (json.dumps(meta, indent=2, sort_keys=True))

        return {'return':0, 'path':path, 'meta':meta, 'artifact':artifact}
