#
# Low-level repository abstraction in cDatabase
#

import os
import json
import yaml

from cdatabase.config import cfg
from cdatabase.cobject import cObject

import cdatabase.utils as utils

class cRepo(object):
    ###########################################################################
    def __init__(self, path: str):

        """
        Initialize cObject in a given path

        Args:
            path (str): Path to cDataBase
        """

        self.path = path

    ###########################################################################
    def list(self, load_entries: bool = False,
                   object_name: str = "",
                   object_id: str = "",
                   data_name: str = "",
                   data_id: str = ""):

        """
        List cData objects in a cObject directory

        Args:
        """

        if not os.path.isdir(self.path):
            raise RuntimeError("Path to cDatabase ("+self.path+") doesn't exit")

        entries = []
        
        # List directories
        dir_list = utils.dir_list(self.path, object_name, object_id)

        for obj_name in dir_list:
            # Attempt to load data
            p = os.path.join(self.path, obj_name)

            if os.path.isdir(p):
                obj = cObject(p)

                if obj.list(load_entries=load_entries, 
                            object_id=object_id,
                            data_name=data_name,
                            data_id=data_id):

                    tmp_entries=obj.get_entries()

                    for k in tmp_entries:
                        entries.append(tmp_entries[k])

        return entries        
