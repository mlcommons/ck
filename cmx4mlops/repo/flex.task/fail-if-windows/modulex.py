# Author and developer: Grigori Fursin


import os

def run(i):

    ###################################################################
    # Prepare flow

    cmind = i['cmind']

    if os.name == 'nt':
        return cmind.prepare_error(1, 'parent flex.task does not support Windows yet')

    return {'return':0}
