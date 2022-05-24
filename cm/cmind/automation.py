# Collective Mind automation

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
            print ('error: {}'.format(e))
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
        print ('GitHub for CM development:  https://github.com/mlcommons/ck/tree/master/cm')
        print ('Reporting issues and ideas: https://github.com/mlcommons/ck/issues')

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


        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

            * list (list): list of CM artifact objects

        """

        console = i.get('out') == 'con'

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

                                # Force no inheritance if first artifact just to check automation UID and alias
                                tmp_ignore_inheritance = True if first_artifact else ignore_inheritance

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
                                                            uid2 = auto_name[1],
                                                            alias2 = auto_name[0],
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

                                    tags_in_meta = meta.get('tags',[])

                                    if len(and_tags)>0:
                                        if not all(t in tags_in_meta for t in and_tags):
                                            continue

                                    if len(no_tags)>0:
                                        skip = False
                                        for t in no_tags:
                                            if t in tags_in_meta:
                                                skip = True
                                                break
                                        if skip:
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
                               'artifact':artifact_repo[0]+','+artifact_repo[1]})
        if r['return']>0: return r

        lst = r['list']

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
            existing_tags+=tags
        meta['tags']=existing_tags

        # Record meta
        r = utils.save_json(meta_path_json, meta=meta)
        if r['return']>0: return r

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

            (tags) (string or list): optional tags to find artifacts

            meta (dict): new meta description to be merged or to replace the original meta description of a CM artifact

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

        replace_lists = i.get('replace_lists', False)

        # Find CM artifact(s)
        i['out'] = None
        r = self.search(i)
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

            r = artifact.update(meta, append_lists = not replace_lists, tags = tags)

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

        # Check target repo
        target_artifact = parsed_artifacts[0]

        target_artifact_obj = target_artifact[0]
        target_artifact_repo = target_artifact[1] if len(target_artifact)>0 else None

        r = self.cmind.access({'action':'search',
                               'automation':'repo',
                               'artifact': utils.assemble_cm_object2(target_artifact_repo)})
        if r['return']>0: return r

        target_repo_list = r['list']

        if len(target_repo_list) == 0:
            return {'return':1, 'error':'target repo "{}" not found'.format(target_artifact_repo)}
        elif len(target_repo_list) >1:
            return {'return':1, 'error':'more than 1 target repo found "{}"'.format(target_artifact_repo)}

        target_repo_path = os.path.abspath(target_repo_list[0].path)

        target_artifact_obj_alias = target_artifact_obj[0]
        target_artifact_obj_uid = target_artifact_obj[1].lower()


        # Updating artifacts
        for artifact in lst:

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

            new_artifact_path = os.path.join(target_repo_path, artifact_automation, new_name)

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

                shutil.move(artifact_path, new_artifact_path)

            # Update meta
            if must_update_meta:
                if console:
                    print ('- Updating meta in "{}"'.format(new_artifact_path))

                r = artifact.update({})
                if r['return'] >0: return r

        return {'return':0, 'list':lst}
