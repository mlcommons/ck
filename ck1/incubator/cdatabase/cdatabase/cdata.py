#
# Low-level data abstraction in cDatabase
#

import os
import json
import yaml

from cdatabase.config import cfg

class cData(object):
    ###########################################################################
    def __init__(self, path: str):

        """
        Initialize cData

        Args:
            path (str): Path to cData.
        """

        self.path = path
        self.valid = False
        self.loaded = False
        self.meta = {}

        # If a data was loaded in the old CK format
        self.ck = {}
        self.ck_format = False

        # Extra info
        self.object_id = ''
        self.object_name = ''
        self.data_id = ''
        self.data_name = ''
        self.title = ''

        self.error = ''

    ###########################################################################
    def is_valid(self):

        """
        Check if there is a valid cData object in a given path

        Args:
            None

        Returns
            (bool) : True if valid or False otherwise
        """

        valid = False
        
        if os.path.isdir(self.path):
            p_yaml = os.path.join(self.path, cfg['cdb_meta_desc_yaml'])
            if os.path.isfile(p_yaml):
                valid = True
            else:
                p_json = os.path.join(self.path, cfg['cdb_meta_desc_json'])
                if os.path.isfile(p_json):
                    valid = True
                else:
                    p_old = os.path.join(self.path, cfg['ck_dir'])
                    if os.path.isdir(p_old):
                        valid = True
                        self.ck_format = True

        self.valid = valid
        
        return valid

    ###########################################################################
    def load(self, force_ck_format: bool = False,
                   ignore_errors: bool = False):

        """
        Load cData from a given path.

        Args:
           force_ck_format (bool) = False - if True, load data in the old CK format.
           ignore_errors (bool) = False - if True, ignore file errors
        """

        if not os.path.isdir(self.path):
            raise RuntimeError("Path to cData ("+self.path+") doesn't exit")

        self.meta = {}

        p_yaml = os.path.join(self.path, cfg['cdb_meta_desc_yaml'])
        p_json = os.path.join(self.path, cfg['cdb_meta_desc_json'])

        if not force_ck_format and (os.path.isfile(p_yaml) or os.path.isfile(p_json)):
            # First load YAML as a base (optional)
            if os.path.isfile(p_yaml):
                try:
                    with open(p_yaml, 'rt' , encoding='utf8') as yaml_file:
                       tmp_data = yaml.load(yaml_file, Loader=yaml.FullLoader)
                       self.meta.update(tmp_data)
                       self.loaded = True
                except Exception as e:
                    self.error = e
                    if not ignore_errors:
                        raise e

            if os.path.isfile(p_json):
                try:
                    with open(p_json, 'rt' , encoding='utf8') as json_file:
                       tmp_data = json.load(json_file)
                       self.meta.update(tmp_data)
                       self.loaded = True
                except Exception as e:
                    self.error = e
                    if not ignore_errors:
                        raise e

        else:
            p_old = os.path.join(self.path, cfg['ck_dir'])

            # Check old CK version
            if os.path.isdir(p_old):
                files = [(cfg['ck_desc_file'], 'desc'),
                         (cfg['ck_info_file'], 'info'),
                         (cfg['ck_meta_file'], 'meta')]

                for f in files:
                    ck_file = os.path.join(p_old, f[0])
                    if os.path.isfile(ck_file):
                        try:
                            with open(ck_file, 'rt' , encoding='utf8') as json_file:
                                tmp_data = json.load(json_file)
                                self.meta.update(tmp_data)

                                self.ck[f[1]]=tmp_data

                                self.loaded = True
                                self.ck_format = True
                        except Exception as e:
                            self.error = e
                            if not ignore_errors:
                                raise e

        if self.loaded:
            self.valid = True

            # Check special meta information
            self.data_name = os.path.basename(self.path)    
            
            self.object_id = self.meta.get('object_id', '')
            if self.object_id == '':
                self.object_id = self.meta.get('backup_module_uid','')

            self.object_name = self.meta.get('object_name', '')
            if self.object_name == '':
                self.object_name = self.meta.get('backup_module_uoa','')
      
            self.data_id = self.meta.get('data_id', '')
            if self.data_id == '':
                self.data_id = self.meta.get('backup_data_uid','')
            
            self.title = self.meta.get('title', '')
            if self.title == '':
                self.title = self.meta.get('data_name','')
            if self.title !='' and self.title == self.data_name:
                self.title = ''
                
        return self.loaded

    ###########################################################################
    def is_loaded(self):

        """
        Args:
            None

        Returns:
            True if loaded or False otherwise.
        """

        return self.loaded

    ###########################################################################
    def is_ck_format(self):

        """
        Args:
            None

        Returns:
            True if loaded in the old CK format.
        """

        return self.ck_format

    ###########################################################################
    def get_meta(self):

        """
        Args:
            None

        Returns:
            (dict) : cData meta
        """

        return self.meta

    ###########################################################################
    def get_path(self):

        """
        Delete cData from a given path.

        Args:
            None
        """

        return self.path

    ###########################################################################
    def save(self, force_yaml: bool = False):

        """
        Save cData to a given path.
        Note that by default we record the whole meta into JSON file and not YAML.
        If we force YAML, we delete JSON (if exists).

        Args:
            None
        """

        if not os.path.isdir(self.path):
            os.makedirs(self.path)

        p_json = os.path.join(self.path, cfg['cdb_meta_desc_json'])

        if force_yaml:
            p_yaml = os.path.join(self.path, cfg['cdb_meta_desc_yaml'])

            with open(p_yaml, 'w' , encoding='utf8') as yaml_file:
                 yaml.dump(self. meta, yaml_file, sort_keys=True)

            if os.path.isfile(p_json):
                os.remove(p_json)

        else:
            with open(p_json, 'w' , encoding='utf8') as json_file:
                 json.dump(self. meta, json_file, indent=2, sort_keys=True)

        return True

    ###########################################################################
    def belongs_to_object(self, object_id: str):

        """
        Check if data belong to a given object

        Args:
            object_id (str) - ID of an cDB object
        """

        return self.object_id == object_id

    ###########################################################################
    def belongs_to_id(self, data_id: str):

        """
        Check if data belong to a given ID

        Args:
            data_id (str) - ID of an cDB object
        """

        return self.data_id == data_id
    
    ###########################################################################
    def delete(self):

        """
        Delete cData from a given path.

        Args:
            None
        """

        if os.path.isdir(self.path):
            import shutil
            shutil.rmtree(self.path)

        return True

