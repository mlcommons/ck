# Author and developer: Grigori Fursin

from cmind import utils

import os
import sys


def detect_version(i):

    cmind = i['cmind']

    pre_version = i['pre_version']

    tool_with_path = i['tool_with_path']

    version = ''
    if os.name == 'nt':
        j = tool_with_path.lower().find('nsight systems ')
        if j>0:
            version = tool_with_path[j+15:]

            j = version.find(os.sep)
            if j>0:
                version = version[:j]

    if version != '':
        pre_version['version'] = version

    return {'return':0}
