# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy

def run(i):

    ###################################################################
    # Prepare flow

    cmind = i['cmind']

    if os.name == 'nt':
        return cmind.prepare_error(1, 'parent flex.task does not support Windows yet')

    return {'return':0}
