# Collective Mind automation
#
# Written by Grigori Fursin

import os

from cmind import utils
from cmind.artifact import Artifact

self_path = __file__

class Automation:
    """
    CM automation class
    """

    def __init__(self, cmind, automation_file):
        """
        Initialize CM automation class

        Args:
            cmind (CM class)
            automation_file (str): path to the CM automation Python module

        Returns:
            (python class) with the following vars:

            * automation_file_path (str): full path to the CM automation Python module
            * path (str): directory with the CM automation

        """

        self.cmind = cmind

        self.automation_file_path = automation_file
        self.path = os.path.dirname(self.automation_file_path)

    ############################################################
    def version(self, i):
        """
        Print CM version

        Args:
            (CM input dict):

            (out) (str): if 'con', output to console

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

        """

        console = i.get('out') == 'con'

        import cmind
        version = cmind.__version__

        if console:
            print (version)

        return {'return':0, 'version':version}

    ############################################################
    def test(self, i):
        """
        Test CM and print various info

        Args:
            (CM input dict):

            (out) (str): if 'con', output to console

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0
        """

        import sys

        console = i.get('out') == 'con'

        r = self.version({})
        if r['return']>0: return r

        version = r['version']

        print ('CM version: {}'.format(version))

        # Check if repository is broken
        try:
            from cmind import net
            rn = net.request(
                {'get': {'action': 'get-cm-version-notes', 'version': version}})
            if rn['return'] == 0:
                notes = rn.get('dict', {}).get('notes', '')

                if notes !='':
                    print ('')
                    print (notes)
        except Exception as e:
            print ('Warning: {}'.format(e))
            pass

        x = sys.executable
        if x != None and x != '':
            print ('')
            print ('Python executable used by CK: {}'.format(x))


        print ('')
        print ('Path to CM package:         {}'.format(self.cmind.path_to_cmind))
        print ('Path to CM core module:     {}'.format(self.cmind.path_to_cmind_core_module))
        print ('Path to CM internal repo:   {}'.format(self.cmind.repos.path_to_internal_repo))

        print ('')
        print ('Path to CM repositories:    {}'.format(self.cmind.repos_path))

        print ('')
        print ('GitHub for CM developments:        https://github.com/mlcommons/ck/tree/master/cm')
        print ('GitHub for CM automation scripts:  https://github.com/mlcommons/cm4mlops')
        print ('Reporting issues and ideas:        https://github.com/mlcommons/ck/issues')
        print ('MLCommons taskforce developing CM: https://github.com/mlcommons/ck/blob/master/docs/taskforce.md')

        return {'return':0}

    ############################################################
    def search(self, i):
        """
        Find CM artifacts (slow - we plan to accelerate it in the future using different indexing mechanisms)

        Args:
            (CM input dict):

            (out) (str): if 'con', output to console

            parsed_automation (list): prepared in CM CLI or CM access function
                                      [ (automation alias, automation UID) ] or
                                      [ (automation alias, automation UID), (automation repo alias, automation repo UID) ]

            parsed_artifact (list): prepared in CM CLI or CM access function
                                      [ (artifact alias, artifact UID) ] or
                                      [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

            ignore_inheritance (bool): if 'True', ignore artifact meta description inheritance 
                                       and just load meta to match UID/alias


            (skip_index_search) (bool): If True, skip indexing
            (force_index_add) (bool): If True, force index add (for reindexing)

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

            * list (list): list of CM artifact objects

        """

        import copy

        console = i.get('out') == 'con'

        skip_index_search = i.get('skip_index_search', False)
        force_index_add = i.get('force_index_add', False)

        lst = []

        # Check tags
        tags = utils.get_list_from_cli(i, key='tags')

        and_tags = []
        no_tags = []

        for t in tags:
            t=t.strip()
            if t!='':
                if t.startswith('-'):
                    no_tags.append(t[1:])
                else:
                    and_tags.append(t)

        ignore_inheritance = i.get('ignore_inheritance',False) == True

        # Get parsed automation
        # First object in a list is an automation
        # Second optional object in a list is a repo
        parsed_automation = i.get('parsed_automation',[])

        automation_name = parsed_automation[0] if len(parsed_automation)>0 else ('','')

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


        # Check index and bypass search
        if not skip_index_search:
            r = self.cmind.index.find(automation_name, artifact_obj, artifact_repo, pruned_repos, and_tags, no_tags)
            if r['return']==0:
                artifacts = r.get('list',[])
                if len(artifacts)>0:
                    lst = []

                    repo_extra_info = self.cmind.repos.extra_info

                    for artifact in artifacts:
                        artifact_object = Artifact(cmind = self.cmind, path = artifact['path'])

                        for j in [0,1]:
                            x = artifact['repo'][j]
                            if x in repo_extra_info:
                                # Add extra info to artifact about the repo
                                artifact_object.repo_path = repo_extra_info[x].path
                                artifact_object.repo_meta = repo_extra_info[x].meta

                        r = artifact_object.load(ignore_inheritance = ignore_inheritance)
                        if r['return']>0: return r

                        lst.append(artifact_object)

                        # Output to console if forced
                        if console:
                            print (artifact_object.path)

                    return {'return':0, 'list':lst}



        # Iterate over pruned repositories
        for repo in pruned_repos:
            path_repo = repo.path_with_prefix

            repo_meta = copy.deepcopy(repo.meta)

            # May or may not be automation
            automations = sorted(os.listdir(path_repo))

            for automation in automations:
                path_automations = os.path.join(path_repo, automation)

                if os.path.isdir(path_automations):
                    # Pruning by automation
                    # Will need to get first entry to get UID and alias of the automation

                    path_artifacts = os.path.join(path_repo, path_automations)

                    # Potential CM artifacts or just some directories
                    artifacts = sorted(os.listdir(path_artifacts))

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

                                # Add extra info to artifact about the repo
                                artifact_object.repo_path = path_repo
                                artifact_object.repo_meta = repo_meta

                                # Force no inheritance if first artifact just to check automation UID and alias
                                tmp_ignore_inheritance = True if first_artifact else ignore_inheritance

                                # Force no inheritance to get basic info about aliases and UIDs
                                r = artifact_object.load(ignore_inheritance = tmp_ignore_inheritance)
                                if r['return']>0: return r

                                # Check permanent meta
                                meta = artifact_object.meta

                                uid = meta.get('uid', '')
                                if uid==None: uid = ''

                                alias = meta.get('alias', '')
                                if alias==None: alias = ''

                                if first_artifact:
                                    # Need to check if automation matches
                                    r = utils.match_objects(uid = meta.get('automation_uid'), 
                                                            alias = meta.get('automation_alias'),
                                                            uid2 = automation_name[1],
                                                            alias2 = automation_name[0],
                                                            more_strict = True)
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
                                    # Reload object with inheritance if needed before checking tags
                                    if first_artifact:
                                        r = artifact_object.load(ignore_inheritance = ignore_inheritance)
                                        if r['return']>0: return r

                                    meta = artifact_object.meta

                                    # Index
                                    if self.cmind.use_index or force_index_add:
                                        r=self.cmind.index.add(meta, path_artifact, 
                                                                     (repo.meta['alias'], 
                                                                      repo.meta['uid']))
                                        # Ignore index output to continue working if issues

                                    # Check if tags match
                                    if not utils.tags_matched(meta.get('tags',[]), and_tags, no_tags):
                                        continue

                                    lst.append(artifact_object)

                                    # Output to console if forced
                                    if console:
                                        print (artifact_object.path)

                                if first_artifact:
                                    first_artifact = False

        return {'return':0, 'list':lst}


    ############################################################
    def add(self, i):
        """
        Add CM artifact

        Args:
            (CM input dict):

            (out) (str): if 'con', output to console

            parsed_automation (list): prepared in CM CLI or CM access function
                                      [ (automation alias, automation UID) ] or
                                      [ (automation alias, automation UID), (automation repo alias, automation repo UID) ]

            parsed_artifact (list): prepared in CM CLI or CM access function
                                      [ (artifact alias, artifact UID) ] or
                                      [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

            meta (dict): meta description of this artifact

            (tags) (string or list): tags to be added to meta
            (new_tags) (string or list): new tags to be added to meta (the same as tags)
            (yaml) (bool): if True, record YAML instead of JSON

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

            * meta (dict): final meta of the artifact
            * path (str): path to the created artifact

        """

        console = i.get('out') == 'con'

        # Get parsed automation
        if 'parsed_automation' not in i:
           return {'return':1, 'error':'automation is not specified'}

        parsed_automation = i.get('parsed_automation',[])

        automation_name = parsed_automation[0] if len(parsed_automation)>0 else ('','')

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
                               'artifact':artifact_repo[0]+','+artifact_repo[1]})
        if r['return']>0: return r

        lst = r['list']

        if len(lst)==0:
            return {'return':16, 'error':'repository {} not found'.format(artifact_repo)}

        if len(lst)>1:
            return {'return':1, 'error':'more than 1 repository found (ambiguity)'}

        repo = lst[0]

        repo_path = repo.path_with_prefix

        # Check automation (if exists)
        automation_path = os.path.join(repo_path, automation_name[0]) if automation_name[0]!='' else os.path.join(repo_path, automation_name[1])

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
        if meta.get('automation_alias','')=='': meta['automation_alias']=automation_name[0]
        if meta.get('automation_uid','')=='': meta['automation_uid']=automation_name[1]

        existing_tags = meta.get('tags',[])

        new_tags_list = []
        if i.get('new_tags','')!='':
            new_tags_list = i['new_tags'].split(',')

        if len(tags)>0:
            new_tags_list += tags    

        if len(new_tags_list)>0: 
            for xtag in new_tags_list:
                if xtag!='' and xtag not in existing_tags:
                    existing_tags.append(xtag)

            meta['tags'] = existing_tags

        # Record meta
        if i.get('yaml', False):
            r = utils.save_yaml(meta_path_yaml, meta=meta)
        else:
            r = utils.save_json(meta_path_json, meta=meta)
        if r['return']>0: return r

        # Index
        if self.cmind.use_index:
            r=self.cmind.index.add(meta, obj_path, 
                                   (repo.meta['alias'], repo.meta['uid']),
                                   update = True)
            # Ignore index output to continue working if issues

        
        if console:
            print ('Added CM object at {}'.format(obj_path))

        return {'return':0, 'meta':meta, 'path':obj_path}

    ############################################################
    def delete(self, i):
        """
        Delete CM artifact

        Args:
            (CM input dict):

            (out) (str): if 'con', output to console

            parsed_automation (list): prepared in CM CLI or CM access function
                                      [ (automation alias, automation UID) ] or
                                      [ (automation alias, automation UID), (automation repo alias, automation repo UID) ]

            parsed_artifact (list): prepared in CM CLI or CM access function
                                      [ (artifact alias, artifact UID) ] or
                                      [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

            (tags) (string or list): optional tags to find artifacts

            (force) (bool): force deleting CM artifacts without asking a user
            (f) (bool): the same as "force"

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

            * deleted_list (list): a list of deleted CM artifacts

        """

        # Check parsed automation
        if 'parsed_automation' not in i:
           return {'return':1, 'error':'automation is not specified'}

        import shutil

        console = i.get('out') == 'con'

        force = True if i.get('f', False) or i.get('force',False) else False

        # Find CM artifact(s)
        i['out']=None
        r = self.search(i)

        if r['return']>0: return r

        lst = r['list']
        if len(lst)==0:
            return {'return':16, 'error':'artifact(s) not found'}

        deleted_lst = []

        for artifact in lst:
            path_to_artifact = artifact.path

            if console:
                tags = artifact.meta.get('tags',[])
                x = '' if len(tags)=='' else ' with tags "{}"'.format(','.join(tags))
                
                print ('Deleting CM artifact in {}{} ...'.format(path_to_artifact, x))

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

            if os.name == 'nt':
                # To be able to remove .git files
                shutil.rmtree(path_to_artifact, onerror = utils.rm_read_only)
#                shutil.rmtree(path_to_artifact, ignore_errors = False, onerror = delete_helper)
            else:
                shutil.rmtree(path_to_artifact)

            # Index
            if self.cmind.use_index:
                r=self.cmind.index.add(artifact.meta, artifact.path, 
                                       (artifact.repo_meta['alias'], artifact.repo_meta['uid']),
                                       update = True, delete = True)
                # Ignore index output to continue working if issues
            
            if console:
                print ('    Deleted!')

        return {'return':0, 'deleted_list':deleted_lst}

    ############################################################
    def load(self, i):
        """
        Load CM artifact

        Args:
            (CM input dict):

            (out) (str): if 'con', output to console

            parsed_automation (list): prepared in CM CLI or CM access function
                                      [ (automation alias, automation UID) ] or
                                      [ (automation alias, automation UID), (automation repo alias, automation repo UID) ]

            parsed_artifact (list): prepared in CM CLI or CM access function
                                      [ (artifact alias, artifact UID) ] or
                                      [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

            (tags) (string or list): optional tags to find artifacts

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

            * path (str): path to a loaded CM artifact
            * original_meta (dict): meta description of the loaded CM artifact before inheritance
            * meta (dict): meta description of the loaded CM artifact after inheritance
            * artifact (CM artifact object)
        """

        # Check parsed automation
        if 'parsed_automation' not in i:
           return {'return':1, 'error':'automation is not specified'}

        console = i.get('out') == 'con'

        # Find CM artifact(s)
        i['out'] = None
        r = self.search(i)

        if r['return']>0: return r

        lst = r['list']
        if len(lst)==0:
            return {'return':16, 'error':'artifact not found: {}'.format(i)}
        elif len(lst)>1:
            return {'return':1, 'error':'more than 1 artifact found', 'list':lst}

        artifact = lst[0]

        path = artifact.path
        meta = artifact.meta
        original_meta = artifact.original_meta

        # Output if console
        if console:
            if str(i.get('yaml','')).lower() in ['true','yes']:
                import yaml
                print (yaml.dump(meta))
            else:
                import json
                print (json.dumps(meta, indent=2, sort_keys=True))

        return {'return':0, 'path':path, 'meta':meta, 'original_meta':original_meta, 'artifact':artifact}

    ############################################################
    def update(self, i):
        """
        Update CM artifact.

        Note: not thread safe - we expect one pipeline running on a system
              can make it thread safe when needed (similar to CK)

        Args:
            (CM input dict):

            (out) (str): if 'con', output to console

            parsed_automation (list): prepared in CM CLI or CM access function
                                      [ (automation alias, automation UID) ] or
                                      [ (automation alias, automation UID), (automation repo alias, automation repo UID) ]

            parsed_artifact (list): prepared in CM CLI or CM access function
                                      [ (artifact alias, artifact UID) ] or
                                      [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

            (search_tags) (string or list): optional tags to find artifacts

            (meta) (dict): new meta description to be merged or to replace the original meta description of a CM artifact

            (tags) (string or list): tags to be added to meta

            (replace) (bool): if True, replace original meta description (False by default)
            (force) (bool): if True, force updates if more than 1 artifact found (False by default)
            (replace_lists) (bool): if True, replace lists in meta description rather than appending them (False by default)

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

            * list (list): list of updated CM artifacts

        """

        console = i.get('out') == 'con'

        meta = i.get('meta',{})

        tags = utils.get_list_from_cli(i, key='tags')

        replace = i.get('replace', False)
        replace_lists = i.get('replace_lists', False)

        # Find CM artifact(s)
        ii=utils.sub_input(i, self.cmind.cfg['artifact_keys'])

        if 'search_tags' in i: ii['tags']=i['search_tags']

        ii['out'] = None

        r = self.search(ii)
        if r['return']>0: return r

        lst = r['list']
        if len(lst)==0:
            # Attempt to add if doesn't exist
            r = self.add(i)
            if r['return']>0: return r

            # Load this artifact
            r = self.load(i)
            if r['return']>0: return r

            lst = [r['artifact']]

            return {'return':0, 'list':lst}

        # If more than one ask if update all or force
        if len(lst)>1:
            force = True if i.get('f', False) or i.get('force',False) else False

            if not force:
                ask = input('More than 1 artifact found. Are you sure you want to update them all (y/N): ')
                ask = ask.strip().lower()

                if ask!='y':
                    return {'return':1, 'error':'more than 1 artifact found', 'list':lst}

                print ('')

        # Updating artifacts
        for artifact in lst:

            # Check if need to update tags
            meta_tags = []

            if not replace and not replace_lists:
                meta_tags = artifact.meta.get('tags',[])

            if len(tags)>0:
                for t in tags:
                    if t not in meta_tags:
                        meta_tags.append(t)

            r = artifact.update(meta, replace = replace, append_lists = not replace_lists, tags = meta_tags)

            # Index
            if self.cmind.use_index:
                r=self.cmind.index.add(artifact.meta, artifact.path, 
                                       (artifact.repo_meta['alias'], artifact.repo_meta['uid']),
                                       update = True)
                # Ignore index output to continue working if issues

            # Output if console
            if console:
                print ('Updated {}'.format(artifact.path))

        return {'return':0, 'list':lst}

    ############################################################
    def move(self, i):
        """
        Rename CM artifacts and/or move them to another CM repository.

        Args:
            (CM input dict):

            (out) (str): if 'con', output to console

            parsed_automation (list): prepared in CM CLI or CM access function
                                      [ (automation alias, automation UID) ] or
                                      [ (automation alias, automation UID), (automation repo alias, automation repo UID) ]

            parsed_artifact (list): prepared in CM CLI or CM access function
                                      [ (artifact alias, artifact UID) ] or
                                      [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

            parsed_artifacts (list): prepared in CM CLI or CM access function - 1st entry has a new artifact name and repository:
                                      [ (artifact alias, artifact UID) ] or
                                      [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

            * list (list): list of renamed/moved CM artifacts

        """

        import shutil

        console = i.get('out') == 'con'

        parsed_artifacts = i.get('parsed_artifacts',[])

        if len(parsed_artifacts)==0:
           return {'return':1, 'error':'artifact is not specified'}
        elif len(parsed_artifacts)>1:
           return {'return':1, 'error':'more than 1 artifact specified'}

        # Find CM artifact(s)
        i['out'] = None
        r = self.search(i)
        if r['return']>0: return r

        lst = r['list']
        if len(lst)==0:
            return {'return':16, 'error':'artifact not found: {}'}

        # Check target artifact
        target_artifact = parsed_artifacts[0]

        target_artifact_obj = target_artifact[0]
        target_artifact_obj_alias = target_artifact_obj[0]
        target_artifact_obj_uid = target_artifact_obj[1].lower()

        # Check target repo
        target_artifact_repo = target_artifact[1] if len(target_artifact)>1 else None
        target_artifact_repo_obj = None

        target_repo_path = None

        if target_artifact_repo is not None:
            r = self.cmind.access({'action':'search',
                                   'automation':'repo',
                                   'artifact': utils.assemble_cm_object2(target_artifact_repo)})
            if r['return']>0: return r

            target_repo_list = r['list']

            if len(target_repo_list) == 0:
                return {'return':1, 'error':'target repo "{}" not found'.format(target_artifact_repo)}
            elif len(target_repo_list) >1:
                return {'return':1, 'error':'more than 1 target repo found "{}"'.format(target_artifact_repo)}

            target_artifact_repo_obj = target_repo_list[0]
            target_repo_path = os.path.abspath(target_artifact_repo_obj.path_with_prefix)

        # Updating artifacts
        for artifact in lst:

            # Index
            if self.cmind.use_index:
                r=self.cmind.index.add(artifact.meta, artifact.path, 
                                       (artifact.repo_meta['alias'], artifact.repo_meta['uid']),
                                       update = True, delete = True)
                # Ignore index output to continue working if issues

            artifact_path = os.path.abspath(artifact.path)

            artifact_meta = artifact.original_meta

            artifact_alias = artifact_meta.get('alias','')
            artifact_uid = artifact_meta.get('uid','')

            artifact_dir_name = os.path.basename(artifact_path)
            artifact_automation_dir = os.path.dirname(artifact_path)
            artifact_automation = os.path.basename(artifact_automation_dir)

            must_update_meta = False

            # Prepare new path
            new_name = artifact_dir_name
            if target_artifact_obj_alias != '':
                new_name = target_artifact_obj_alias

            # Use either new repo or the repo of the original artifact
            new_artifact_path = os.path.join(target_repo_path, artifact_automation, new_name) if target_repo_path is not None \
                else os.path.join(artifact_automation_dir, new_name)

            # Check if need to update meta
            if target_artifact_obj_alias != '' and artifact_alias.lower() != target_artifact_obj_alias.lower():
                must_update_meta = True
                artifact_meta['alias']=target_artifact_obj_alias

            if target_artifact_obj_uid != '' and artifact_uid.lower() != target_artifact_obj_uid:
                must_update_meta = True
                artifact_meta['uid']=target_artifact_obj_uid

            artifact.path = new_artifact_path

            # Move
            if artifact_path != new_artifact_path:
                if console:
                    print ('* Moving "{}" to'.format(artifact_path))
                    print ('         "{}"'.format(new_artifact_path))

                if os.path.isdir(new_artifact_path):
                    return {'return':1, 'error':'target artifact (directory) already exists'}

                shutil.move(artifact_path, new_artifact_path)

            # Update meta
            if must_update_meta:
                if console:
                    print ('- Updating meta in "{}"'.format(new_artifact_path))

                # If only yaml, update yaml and not json
                meta_path_yaml = os.path.join(new_artifact_path, self.cmind.cfg['file_cmeta']+'.yaml')
                meta_path_json = os.path.join(new_artifact_path, self.cmind.cfg['file_cmeta']+'.json')
                if os.path.isfile(meta_path_yaml) and not os.path.isfile(meta_path_json):
                    update_meta={'alias':artifact_meta['alias'],
                                 'uid':artifact_meta['uid']}
                    
                    r = utils.update_yaml(meta_path_yaml, update_meta)
                    if r['return']>0: return r

                else:
                    r = artifact.update({})
                    if r['return'] >0: return r

            # Index
            if self.cmind.use_index:
                if target_artifact_repo_obj is not None:
                    tmp_repo_index = (target_artifact_repo_obj.meta['alias'], 
                                      target_artifact_repo_obj.meta['uid'])
                else:
                   tmp_repo_index = (artifact.repo_meta['alias'], 
                                     artifact.repo_meta['uid'])
                
                r=self.cmind.index.add(artifact.meta, artifact.path, 
                                       tmp_repo_index, update = True)
                # Ignore index output to continue working if issues

        return {'return':0, 'list':lst}

    ############################################################
    def copy(self, i):
        """
        Copy CM artifact(s) either to a new artifact or to a new repository

        Args:
            (CM input dict):

            (out) (str): if 'con', output to console

            parsed_automation (list): prepared in CM CLI or CM access function
                                      [ (automation alias, automation UID) ] or
                                      [ (automation alias, automation UID), (automation repo alias, automation repo UID) ]

            parsed_artifact (list): prepared in CM CLI or CM access function
                                      [ (artifact alias, artifact UID) ] or
                                      [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

            parsed_artifacts (list): prepared in CM CLI or CM access function - 1st entry has a new artifact name and repository:
                                      [ (artifact alias, artifact UID) ] or
                                      [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

            new_tags (string): add new tags (separated by comma) to new artifacts
        
        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

            * list (list): list of copied CM artifacts

        """

        import shutil

        console = i.get('out') == 'con'

        parsed_artifacts = i.get('parsed_artifacts',[])

        if len(parsed_artifacts)==0:
           return {'return':1, 'error':'artifact is not specified'}
        elif len(parsed_artifacts)>1:
           return {'return':1, 'error':'more than 1 artifact specified'}

        # Find CM artifact(s)
        i['out'] = None
        r = self.search(i)
        if r['return']>0: return r

        lst = r['list']
        if len(lst)==0:
            return {'return':16, 'error':'artifact(s) not found: {}'}

        # Check target artifact
        target_artifact = parsed_artifacts[0]

        target_artifact_obj = target_artifact[0]
        target_artifact_obj_alias = target_artifact_obj[0]
        target_artifact_obj_uid = target_artifact_obj[1].lower()

        # Check target repo
        target_artifact_repo = target_artifact[1] if len(target_artifact)>1 else None
        target_artifact_repo_obj = None

        target_repo_path = None

        if target_artifact_repo is not None:
            r = self.cmind.access({'action':'search',
                                   'automation':'repo',
                                   'artifact': utils.assemble_cm_object2(target_artifact_repo)})
            if r['return']>0: return r

            target_repo_list = r['list']

            if len(target_repo_list) == 0:
                return {'return':1, 'error':'target repo "{}" not found'.format(target_artifact_repo)}
            elif len(target_repo_list) >1:
                return {'return':1, 'error':'more than 1 target repo found "{}"'.format(target_artifact_repo)}

            target_artifact_repo_obj = target_repo_list[0]
            target_repo_path = os.path.abspath(target_artifact_repo_obj.path_with_prefix)

        # Updating artifacts
        new_tags_list = []
        if i.get('new_tags','')!='':
            new_tags_list = i['new_tags'].split(',')

        
        for artifact in lst:

            artifact_path = os.path.abspath(artifact.path)

            artifact_meta = artifact.original_meta

            artifact_alias = artifact_meta.get('alias','')
            r=utils.gen_uid()
            if r['return']>0: return r

            target_artifact_obj_uid=r['uid']

            artifact_dir_name = os.path.basename(artifact_path)
            artifact_automation_dir = os.path.dirname(artifact_path)
            artifact_automation = os.path.basename(artifact_automation_dir)

            # Prepare new path
            new_name = artifact_dir_name
            if target_artifact_obj_alias != '':
                new_name = target_artifact_obj_alias

            # Use either new repo or the repo of the original artifact
            new_artifact_path = os.path.join(target_repo_path, artifact_automation, new_name) if target_repo_path is not None \
                else os.path.join(artifact_automation_dir, new_name)

            if target_artifact_obj_alias != '' and artifact_alias.lower() != target_artifact_obj_alias.lower():
                artifact_meta['alias']=target_artifact_obj_alias

            artifact_meta['uid']=target_artifact_obj_uid
            if len(new_tags_list)>0:
                xtags = artifact_meta.get('tags',[])
                for xtag in new_tags_list:
                    if xtag!='' and xtag not in xtags:
                        xtags.append(xtag)
                artifact_meta['tags'] = xtags

            artifact.path = new_artifact_path

            # Copy
            if artifact_path != new_artifact_path:
                if console:
                    print ('* Copying "{}" to'.format(artifact_path))
                    print ('         "{}"'.format(new_artifact_path))

                if os.path.isdir(new_artifact_path):
                    return {'return':1, 'error':'target artifact (directory) already exists'}

                shutil.copytree(artifact_path, new_artifact_path)

            # Update meta
            if console:
                print ('- Updating meta in "{}"'.format(new_artifact_path))

            # If only yaml, update yaml and not json
            meta_path_yaml = os.path.join(new_artifact_path, self.cmind.cfg['file_cmeta']+'.yaml')
            meta_path_json = os.path.join(new_artifact_path, self.cmind.cfg['file_cmeta']+'.json')

            if os.path.isfile(meta_path_yaml) and not os.path.isfile(meta_path_json):
                update_meta={'alias':artifact_meta['alias'],
                             'uid':artifact_meta['uid']}
                
                r = utils.update_yaml(meta_path_yaml, update_meta)
                if r['return']>0: return r

            else:
                r = artifact.update({})
                if r['return'] >0: return r

            # Index added artifact
            if self.cmind.use_index:
                # Old
                if target_artifact_repo_obj is not None:
                    tmp_repo_index = (target_artifact_repo_obj.meta['alias'], 
                                      target_artifact_repo_obj.meta['uid'])                    
                else:
                    tmp_repo_index = (artifact.repo_meta['alias'], 
                                      artifact.repo_meta['uid'])
                                      
                r=self.cmind.index.add(artifact.meta, artifact.path, 
                                       tmp_repo_index, update = True)
                # Ignore index output to continue working if issues


        return {'return':0, 'list':lst}

    ############################################################
    def info(self, i):
        """
        Get info about artifacts

        Args:
            (CM input dict):

            (out) (str): if 'con', output to console

            parsed_automation (list): prepared in CM CLI or CM access function
                                      [ (automation alias, automation UID) ] or
                                      [ (automation alias, automation UID), (automation repo alias, automation repo UID) ]

            parsed_artifact (list): prepared in CM CLI or CM access function
                                      [ (artifact alias, artifact UID) ] or
                                      [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

            parsed_artifacts (list): prepared in CM CLI or CM access function - 1st entry has a new artifact name and repository:
                                      [ (artifact alias, artifact UID) ] or
                                      [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

            (uid) (bool): if True, copy CID in UID::UID format to clipboard
            (md) (bool): if True, copy CID in [](UID::UID) format to clipboard

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

            * list (list): list of CM artifacts

        """

        # Check parsed automation
        if 'parsed_automation' not in i:
           return {'return':1, 'error':'automation is not specified'}

        console = i.get('out') == 'con'

        # Find CM artifact(s)
        i['out'] = None
        r = self.search(i)

        if r['return']>0: return r

        lst = r['list']
        if len(lst)==0:
            return {'return':16, 'error':'artifact not found: {}'.format(i)}

        cid1 = ''
        
        for artifact in lst:
            if console and len(lst)>1:
                print ('****************************************************')

            path = artifact.path
            meta = artifact.meta
            original_meta = artifact.original_meta

            alias = meta.get('alias','')
            uid = meta.get('uid','')
            automation_alias = meta.get('automation_alias','')
            automation_uid = meta.get('automation_uid','')

            x = utils.assemble_cm_object(alias,uid)
            if ' ' in x: x = '"' + x + '"'
            
            cid = utils.assemble_cm_object(automation_alias,automation_uid) + \
                  '::' + \
                  x

            cid1 = automation_uid+'::'+uid

#            cid_user_friendly = automation_alias if automation_alias != '' else automation_uid
#            cid_user_friendly += '::' + (alias if alias != '' else uid)
#            cid_misc = automation_alias if automation_alias != '' else automation_uid
#            cid_misc += '::' + uid
#            cid = automation_uid + '::' + uid

            # Output if console
            full_cid = '(' + cid + ')'
            if console:
                print ('CID = ' + cid)
                print ('CID1 = ' + cid1)
                print ('CID2 = ' + full_cid)
                print ('')
                print ('Path = ' + path)

                p_dirs=[]
                p_files=[]
                for p in os.listdir(path):
                    p_dirs.append(p) if os.path.isdir(os.path.join(path,p)) else p_files.append(p)
                        
                if len(p_dirs)>0 or len(p_files)>0:
                    for x in [('Directories',p_dirs), 
                              ('Files',p_files)]:
                        x0 = x[0]
                        x1 = x[1]
                        if len(x1)>0:
                            print ('')
                            print ('  '+x0+':')
                            for p in sorted(x1):
                                print ('    ' + p)

       # Attempt to copy to clipboard the last CID
        if cid1 !='':
            clipboard = full_cid
            if i.get('uid', False): clipboard = cid1
            if i.get('md', False): clipboard = '[]'+full_cid

            r = utils.copy_to_clipboard({'string':clipboard, 'skip_fail':True})
            # Skip output


        return {'return':0, 'list': lst}

#############################################################
#def delete_helper(func, path, ret):
#    import stat, errno
#
#    if ret[1].errno != errno.EACCES:
#        raise
#    else:
#        clean_attr = stat.S_IRWXG | stat.S_IRWXO | stat.S_IRWXU
#        os.chmod(path, clean_attr)
#        func(path)
#
#    return
