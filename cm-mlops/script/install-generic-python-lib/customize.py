from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    meta = i['meta']
    automation = i['automation']

    package_name = env.get('CM_GENERIC_PYTHON_PACKAGE_NAME', '').strip()
    if package_name == '':
        return automation._available_variations({'meta':meta})

    return {'return':0}
