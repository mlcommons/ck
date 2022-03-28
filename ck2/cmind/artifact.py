# Collective Mind artifact

import os

from cmind import utils

class Artifact:
    ############################################################
    def __init__(self, cmind, path):
        """
        Initialize artifact class
        """

        self.cmind = cmind

        self.cfg = cmind.cfg

        self.path = path
        self.meta = {}

    ############################################################
    def load(self, ignore_inheritance = False, base_recursion = 0):
        """
        Load artifact

        """

        path_artifact_meta = os.path.join(self.path, self.cfg['file_cmeta'])

        r = utils.is_file_json_or_yaml(path_artifact_meta)
        if r['return'] >0 : return r

        if not r['is_file']:                      
            return {'return':16, 'error': 'CM artifact not found in path {}'.format(self.path)}
        
        # Search if there is a repo in this path
        r = utils.load_yaml_and_json(file_name_without_ext = path_artifact_meta)
        if r['return'] >0: return r

        meta = r['meta']

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

        self.meta = r['meta']

        return {'return':0}
