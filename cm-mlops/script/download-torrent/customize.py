from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    if env.get('CM_TORRENT_WAIT_UNTIL_COMPLETED','') == 'yes':
        if not env.get('CM_TORRENT_DOWNLOADED_FILE_NAME'):
            return {'return':1, 'error': 'CM_TORRENT_WAIT_UNTIL_COMPLETED is given but CM_TORRENT_DOWNLOADED_FILE_NAME is not set' }

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
