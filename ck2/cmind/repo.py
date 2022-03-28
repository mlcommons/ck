# Collective Mind repository

import os

from cmind import utils

class Repo:
    ############################################################
    def __init__(self, path, cfg):
        """
        Initialize class 
        """

        self.cfg = cfg

        self.path = path
        self.path_with_prefix = path

        self.path_prefix = ''

        # Repo meta
        self.meta = {}

    ############################################################
    def load(self):
        """
        Load repository file

        """

        # Check if home directory exists. Create it otherwise.
        if not os.path.isdir(self.path):
            return {'return':1, 'error': 'repository path {} not found'.format(self.path)}
        
        # Search if there is a repo in this path
        full_path = os.path.join(self.path, self.cfg['file_meta_repo'])

        r = utils.load_yaml_and_json(file_name_without_ext = full_path)
        if r['return'] >0: return r

        self.meta = r['meta']

        self.path_prefix = self.meta.get('prefix','')
        if self.path_prefix !='':
            self.path_with_prefix = os.path.join(self.path, self.path_prefix)

        return {'return':0}
