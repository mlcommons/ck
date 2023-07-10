from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    csv_file = env.get('CM_CSV_FILE', '')
    md_file = env.get('CM_MD_FILE', '')

    env['CM_RUN_CMD'] = '{}  process.py  {} {} '.format(env["CM_PYTHON_BIN_WITH_PATH"], csv_file, md_file) 

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
