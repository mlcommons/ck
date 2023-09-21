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
    process_file = os.path.join(i['run_script_input']['path'], "process.py")

    env['CM_RUN_CMD'] = '{} {} {} {} '.format(env["CM_PYTHON_BIN_WITH_PATH"], process_file, csv_file, md_file) 

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
