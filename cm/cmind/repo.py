# Collective Mind repository
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

from cmind import utils

class Repo:
    """
    CM repository class
    """

    def __init__(self, path, cfg):
        """
        Initialize CM repository class

        Args:
            path (str): path to a CM repository
            cfg (dict): CM configuration

        Returns:
            (python class) with the following vars:

            * path (str): path to a CM repository
            * path_prefix (str): use extra directory inside CM repository to keep CM artifacts
            * path_with_prefix (str): path to a CM repository if directory prefix is used

            * meta (dict): CM repository meta description

        """

        self.cfg = cfg

        self.path = path
        self.path_with_prefix = path

        self.path_prefix = ''

        # Repo meta
        self.meta = {}
        self.original_meta = {} # for compatibility with CM/CMX universal search

    ############################################################
    def load(self, cmx = False):
        """
        Load CM repository

        Args:
            None

        Returns: 
            (CM return dict):

            * return (int): return code == 0 if no error and >0 if error
            * (error) (str): error string if return>0

        """

        # Check if home directory exists. Create it otherwise.
        if not os.path.isdir(self.path):
            return {'return':1, 'error': 'repository path {} not found'.format(self.path)}

        # Search if there is a repo in this path
        full_path = os.path.join(self.path, self.cfg['file_meta_repo'])

        r = utils.load_yaml_and_json(file_name_without_ext = full_path)
        if r['return'] >0: 
           r['error'] = 'CM repository is broken ({})'.format(r['error'])
           r['return'] = 16
           return r

        self.meta = r['meta']
        self.original_meta = self.meta

        if cmx and self.meta.get('prefix_cmx', '') != '':
            self.path_prefix = self.meta.get('prefix_cmx','')
        else:
            self.path_prefix = self.meta.get('prefix','')

        if self.path_prefix is not None and self.path_prefix.strip() !='':
            self.path_with_prefix = os.path.join(self.path, self.path_prefix)

        if os.path.isdir(self.path) and not os.path.isdir(self.path_with_prefix):
            os.makedirs(self.path_with_prefix)

        return {'return':0}
