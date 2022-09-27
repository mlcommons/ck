#
# Low-level object abstraction in cDatabase
#

import os
import json
import yaml

from cdatabase.config import cfg
from cdatabase.cdata import cData

import cdatabase.utils as utils

class cObject(object):
    ###########################################################################
    def __init__(self, path: str):

        """
        Initialize cObject in a given path

        Args:
            path (str): Path to cObject..
        """

        self.path = path
        self.entries = {}

    ###########################################################################
    def list(self, load_entries: bool = False,
                   object_id: str = "",
                   data_name: str = "",
                   data_id: str = ""):

        """
        List cData objects in a cObject directory

        Args:
            None
        """

        if not os.path.isdir(self.path):
            raise RuntimeError("Path to cObject ("+self.path+") doesn't exit")

        # List directories
        dir_list = utils.dir_list(self.path, data_name, data_id)

        for name in dir_list:
            # Attempt to load data
            p = os.path.join(self.path, name)

            data = cData(p)

            # Check if valid format
            if data.is_valid():
                add_data = False
                
                if load_entries:
                    data.load(ignore_errors=True)

                    # Check if belongs to a requested object using ID
                    if data.is_loaded() and (object_id == '' or data.belongs_to_object(object_id)) \
                        and (data_id == '' or data.belongs_to_id(data_id)):
                        add_data = True

                if add_data:
                    self.entries[name] = data

        return True

    ###########################################################################
    def get_entries(self):

        """
        Get cData objects

        Args:
            None
        """

        return self.entries
