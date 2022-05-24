# Collective Mind artifact

import os

from cmind import utils

class Artifact:
    """
    CM artifact class
    """

    def __init__(self, cmind, path):
        """
        Initialize CM artifact class

        Args:
            cmind (CM class)
            path (str): path to a CM artifact

        Returns:
            (python class) with the following vars:

            * path (str): path to CM artifact

            * original_meta (dict): original meta description of this artifact without inheritance

            * meta (dict): meta description of this artifact after inheritance


        """

        self.cmind = cmind

        self.cfg = cmind.cfg

        self.path = path

        self.original_meta = {} # without inheritance
        self.meta = {}          # with inheritance

    ############################################################
    def load(self, ignore_inheritance = False, base_recursion = 0):
        """
        Load CM artifact

        Args:    
                 ignore_inheritance (bool): if True ignore artifact meta description inheritance
                 base_recursion (int): internal to avoid infinite recursion during inheritance

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0
        """

        import copy

        path_artifact_meta = os.path.join(self.path, self.cfg['file_cmeta'])

        r = utils.is_file_json_or_yaml(path_artifact_meta)
        if r['return'] >0 : return r

        if not r['is_file']:                      
            return {'return':16, 'error': 'CM artifact not found in path {}'.format(self.path)}

        # Search if there is a repo in this path
        r = utils.load_yaml_and_json(file_name_without_ext = path_artifact_meta)
        if r['return'] >0: return r

        original_meta = r['meta']
        self.original_meta = copy.deepcopy(original_meta)

        meta = original_meta

        if not ignore_inheritance:
            automation_uid = meta.get('automation_uid', '')
            automation_alias = meta.get('automation_alias', '')
            automation = automation_alias
            if automation_uid!='': automation+=','+automation_uid

            # Check inheritance
            r = utils.process_meta_for_inheritance({'automation':automation, 
                                                    'meta':meta, 
                                                    'cmind':self.cmind, 
                                                    'base_recursion':base_recursion})
            if r['return']>0: return r

            meta = r['meta']

        self.meta = meta

        return {'return':0}

    ############################################################
    def update(self, meta, append_lists = True, replace = False, tags = []):
        """
        Update CM artifact

        Args:
             meta (dict): new meta description
             replace (bool): if True, replace original meta description instead of merging
             append_lists (bool): if True and replace is False, append lists when merging meta descriptions instead of substituting
             tags (list): replace tags in meta

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

        """

        from cmind import utils

        # Without inheritance
        current_meta = self.original_meta

        if len(meta)>0:

            if replace:
                self.original_meta = meta
            else:
                r = utils.merge_dicts({'dict1':current_meta, 'dict2':meta, 'append_lists':append_lists})
                if r['return'] >0: return 

                self.original_meta = r['dict1']

        if len(tags)>0:
            self.original_meta['tags']=tags

        # Save file with orignal meta without inheritance

        # Updates are always in JSON (on top of YAML if needed or only JSON)
        path_artifact_meta_json = os.path.join(self.path, self.cfg['file_cmeta'] + '.json')

        r = utils.save_json(file_name = path_artifact_meta_json, meta=self.original_meta)
        if r['return'] >0: return r

        # Reload with inheritance
        r = self.load()

        return r
