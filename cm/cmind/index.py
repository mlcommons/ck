# Collective Mind index
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
import json

from cmind import utils

class Index:
    """
    CM index class
    """

    def __init__(self, path, cfg, meta = {}):
        """
        Initialize CM index class

        Args:
            path (str): path to directory with repos and index file
            cfg (dict): CM configuration
            (meta) (dict): CM index meta

        Returns:
            (python class) with the following vars:

            * path (str): path to CM repositories and index file
            * meta (dict): CM index meta
        """

        self.path = path
        self.meta = meta
        self.cfg = cfg

        self.full_path_to_index = os.path.join(path, cfg['file_index'])

        self.updated = False

    ############################################################
    def load(self):
        """
        Load or initialize CM index

        Args:
            None

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

        """

        # Check if home directory exists. Create it otherwise.
        if not os.path.isdir(self.path):
            os.makedirs(self.path)

        # Check repos holder
        full_path_to_index = os.path.join(self.path, self.cfg['file_index'])

        self.full_path_to_index = full_path_to_index

        exists = False
        if os.path.isfile(self.full_path_to_index):
            exists = True
            r = utils.load_json(self.full_path_to_index)
            if r['return']==0:
                self.meta = r['meta']

        return {'return':0, 'exists':exists}

    ############################################################
    def save(self):
        """
        Save CM index
        TBD: it's not thread safe and we should provide better handling if CM is used in parallel
             we need to reload 

        Args:
            None

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

        """

        # Check if home directory exists. Create it otherwise.
        if not os.path.isdir(self.path):
            os.makedirs(self.path)

        import json

        s = json.dumps(self.meta, indent=2)

        r = utils.save_txt(self.full_path_to_index, s)

        return r

    ############################################################
    def add(self, meta, path, repo, update = False, delete = False):
        """
        Add to CM index

        Args:
            meta (dict): artifact meta
            path (str): artifact path
            repo (tuple of str): (alias, uid) of repo
            update (bool): force update
            delete (bool): delete instead of adding

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

        """

        index_meta = self.meta

        for y in [meta.get('automation_uid',''), meta.get('automation_alias','')]:
            if y!='' and y not in index_meta: 
                index_meta[y]={}

            uid = True

            meta_uid = meta.get('uid','')
            meta_alias = meta.get('alias','')

            for z in [meta_uid, meta_alias]:
                if z!='':
                    if delete:
                        if z in index_meta[y]:
                            for k in [index_meta[y][z].get('alias',''),
                                      index_meta[y][z].get('uid','')]:
                                if k!='' and k in index_meta[y]:
                                    del(index_meta[y][k])
                                    self.updated = True
                            if z in index_meta[y]:
                                del(index_meta[y][z])
                                self.updated = True

                    elif y !='' and z not in index_meta[y] or update:
                        blob = {'tags': meta.get('tags',[]),
                                'repo': repo,
                                'path': path}

                        if uid:
                            blob['alias'] = meta_alias
                        else:
                            blob['uid'] = meta_uid

                        index_meta[y][z] = blob

                        self.updated = True

                uid = False

        return {'return':0}

    ############################################################
    def find(self, automation_name,
                   artifact_obj,
                   artifact_repo,
                   pruned_repos,
                   and_tags,
                   no_tags):

        """
        Find in CM index

        Args:
            automation_name (tuple of str): (alias, uid) of automation
            artifact_obj (tuple of str): (alias, uid) of artifact obj
            artifact_repo (tuple of str of None): if not None, use pruned_repos
            pruned_repos (list of Repo classes): pruned repos
            and_tags (list of str): AND tags
            no_tags (list of str): NO tags

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

        """

        index_meta = self.meta

        ret = {'return':0, 'list':[]}

        # Check automation from UID to alias with wild cards
        automations = []
        if automation_name[1]!='' and automation_name[1] in index_meta:
            automations.append(automation_name[1])
        else:
           if ('*' in automation_name[0] or '?' in automation_name[0]):
               import fnmatch
               for automation in index_meta:
                   if not utils.is_cm_uid(automation) and fnmatch.fnmatch(automation, automation_name[0]):
                       automations.append(automation)
           elif automation_name[0]!='' and automation_name[0] in index_meta:
               automations.append(automation_name[0])

        if len(automations)==0:
            return ret

        # Check artifacts
        artifacts = []

        for automation in automations:
            index_meta_automation = index_meta[automation]

            keys_to_delete = []

            check_unique_ids = []
            
            # First check UID
            if artifact_obj[1]!='':
                if artifact_obj[1] in index_meta_automation:
                    self._add_if_exists(index_meta_automation, artifact_obj[1], artifacts, keys_to_delete, check_unique_ids)
            else:
               if ('*' in artifact_obj[0] or '?' in artifact_obj[0]):
                   import fnmatch
                   for artifact in index_meta_automation:
                       if fnmatch.fnmatch(artifact, artifact_obj[0]):
                           self._add_if_exists(index_meta_automation, artifact, artifacts, keys_to_delete, check_unique_ids)
               elif artifact_obj[0]=='':
                   for artifact in index_meta_automation:
                       # Add only 1 (UID) to avoid adding 2 duplicates
                       self._add_if_exists(index_meta_automation, artifact, artifacts, keys_to_delete, check_unique_ids)
               elif artifact_obj[0] in index_meta_automation:
                   self._add_if_exists(index_meta_automation, artifact_obj[0], artifacts, keys_to_delete, check_unique_ids)

            if len(keys_to_delete)>0:
                for key in keys_to_delete:
                    if key in index_meta_automation:
                        del(index_meta_automation[key])

                self.updated = True

        if len(artifacts)==0:
            return ret

        # Check repo and tags
        lst = []

        for artifact in artifacts:
            # Check repo if needed
            if artifact_repo is not None:
                repo = artifact['repo']

                repo_uid = repo[1]
                repo_alias = repo[0]
 
                repo_matched = False

                for pruned_repo in pruned_repos:
                    pruned_repo_uid = pruned_repo.meta['uid']
                    pruned_repo_alias = pruned_repo.meta['alias']

                    if repo_uid == pruned_repo_uid and repo_alias == pruned_repo_alias:
                        repo_matched = True
                        break

                if not repo_matched:
                    continue

            # Check tags
            if not utils.tags_matched(artifact['tags'], and_tags, no_tags):
                continue

            lst.append(artifact)

        return {'return':0, 'list':lst}

    ############################################################
    # Internal support function
    def _add_if_exists(self, meta, key, artifacts, keys_to_delete, check_unique_ids):

        # Check that UID was not already added
        uid = meta[key].get('uid','')
        if uid =='':
            uid = key

        if uid in check_unique_ids:
            return

        check_unique_ids.append(uid)

        # Continue processing

        x = meta[key]

        if os.path.isdir(x['path']):
            artifacts.append(x)
        else:
            keys_to_delete.append(key)
            # Add related key to delete (UID or alias)
            if x.get('uid','')!='': keys_to_delete.append(x['uid'])
            if x.get('alias','')!='': keys_to_delete.append(x['alias'])

        return
