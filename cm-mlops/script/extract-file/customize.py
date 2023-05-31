from cmind import utils
import os
import hashlib

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    if 'CM_EXTRACT_FILEPATH' not in env:
        return {'return': 1, 'error': 'Extract with no download requested and CM_EXTRACT_FILEPATH is not set'}

    filename = env['CM_EXTRACT_FILEPATH']
    env['CM_EXTRACT_FILENAME'] = filename

    if env.get('CM_EXTRACT_REMOVE_EXTRACTED','') == 'yes':
        remove_extracted = True
    else:
        remove_extracted = False

    if filename.endswith(".zip"):
        env['CM_EXTRACT_TOOL'] = "unzip"
    elif filename.endswith(".tar.gz"):
        env['CM_EXTRACT_TOOL_OPTIONS'] = ' -xvzf'
        env['CM_EXTRACT_TOOL'] = 'tar '
    elif filename.endswith(".tar"):
        env['CM_EXTRACT_TOOL_OPTIONS'] = ' -xvf'
        env['CM_EXTRACT_TOOL'] = 'tar '
    elif filename.endswith(".gz"):
        env['CM_EXTRACT_TOOL_OPTIONS'] = ' -d '+ ('-k ' if not remove_extracted else '') + ' > $PWD/' + env['CM_EXTRACT_EXTRACTED_FILENAME'] + '<'
        env['CM_EXTRACT_TOOL'] = 'gzip '
    elif env.get('CM_EXTRACT_UNZIP','') == 'yes':
        env['CM_EXTRACT_TOOL'] = 'unzip '
    elif env.get('CM_EXTRACT_UNTAR','') == 'yes':
        env['CM_EXTRACT_TOOL_OPTIONS'] = ' -xvf'
        env['CM_EXTRACT_TOOL'] = 'tar '
    elif env.get('CM_EXTRACT_GZIP','') == 'yes':
        env['CM_EXTRACT_CMD'] = 'gzip '
        env['CM_EXTRACT_TOOL_OPTIONS'] = ' -d '+ ('-k ' if not remove_extracted else '')
    else:
        return {'return': 1, 'error': 'Neither CM_EXTRACT_UNZIP nor CM_EXTRACT_UNTAR is yes'}

    if 'tar ' in env['CM_EXTRACT_TOOL'] and env.get('CM_EXTRACT_TO_FOLDER', '') != '':
        env['CM_EXTRACT_TOOL_OPTIONS'] = ' --one-top-level='+ env['CM_EXTRACT_TO_FOLDER'] + env.get('CM_EXTRACT_TOOL_OPTIONS', '')
        env['CM_EXTRACT_EXTRACTED_FILENAME'] = env['CM_EXTRACT_TO_FOLDER']


    env['CM_EXTRACT_CMD'] = env['CM_EXTRACT_TOOL'] + ' ' + env.get('CM_EXTRACT_TOOL_EXTRA_OPTIONS', '') + ' ' + env.get('CM_EXTRACT_TOOL_OPTIONS', '')+ ' '+ filename

    if env.get('CM_EXTRACT_EXTRACTED_CHECKSUM'):
        env['CM_EXTRACT_EXTRACTED_CHECKSUM_CMD'] = "echo {} {} | md5sum -c".format(env.get('CM_EXTRACT_EXTRACTED_CHECKSUM'), env['CM_EXTRACT_EXTRACTED_FILENAME'])
    else:
        env['CM_EXTRACT_EXTRACTED_CHECKSUM_CMD'] = ""

    return {'return':0}

def postprocess(i):

    env = i['env']

    extracted_filename = os.path.basename(env.get('CM_EXTRACT_EXTRACTED_FILENAME')) if env.get('CM_EXTRACT_EXTRACTED_FILENAME') else env.get('CM_EXTRACT_EXTRACT_TO_FOLDER')
    extracted_file = env.get('CM_EXTRACT_EXTRACTED_FILENAME') if env.get('CM_EXTRACT_EXTRACTED_FILENAME') else env.get('CM_EXTRACT_EXTRACT_TO_FOLDER')
    if extracted_file:
        filename = os.path.basename(extracted_file)
        folderpath = env.get('CM_EXTRACT_EXTRACT_TO_PATH', os.getcwd())
        filepath = os.path.join(folderpath, filename)
    else:
        filename = os.getcwd()
        filepath = os.getcwd() #extracted to the root cache folder

    if os.path.exists(filepath):
        env['CM_EXTRACT_EXTRACTED_PATH'] = filepath
    else:
        return {'return':1, 'error': 'CM_EXTRACT_EXTRACTED_FILENAME and CM_EXTRACT_TO_FOLDER are not set'}

    env['CM_EXTRACT_EXTRACTED_PATH'] = filepath

    if env.get('CM_EXTRACT_FINAL_ENV_NAME'):
        env[env['CM_EXTRACT_FINAL_ENV_NAME']] = filepath

    env['CM_GET_DEPENDENT_CACHED_PATH'] =  filepath

    return {'return':0}
