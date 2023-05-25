from cmind import utils
import os
import hashlib

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    skip_download = env.get('CM_DAE_ONLY_EXTRACT', 'no')

    if skip_download != 'yes':
        if not env.get('CM_DAE_FILENAME'):
            urltail = os.path.basename(env['CM_DAE_URL'])
            urlhead = os.path.dirname(env['CM_DAE_URL'])
            if "." in urltail and "/" in urlhead:
                env['CM_DAE_FILENAME'] = urltail
            else:
                env['CM_DAE_FILENAME'] = "index.html"

        filename = env['CM_DAE_FILENAME']

        url = env['CM_DAE_URL']

        if env['CM_DAE_DOWNLOAD_TOOL'] == "wget":
            env['CM_DAE_DOWNLOAD_CMD'] = f"wget -nc {url}"
        if env['CM_DAE_DOWNLOAD_TOOL'] == "curl":
            env['CM_DAE_DOWNLOAD_CMD'] = f"curl {url}"

    else:
        env['CM_DAE_DOWNLOAD_CMD'] = ""
        if 'CM_DAE_FILEPATH' not in env:
            return {'return': 1, 'error': 'Extract with no download requested and CM_DAE_FILEPATH is not set'}
        filename = env['CM_DAE_FILEPATH']
        env['CM_DAE_FILENAME'] = filename
        env['CM_DAE_DOWNLOADED_FILENAME'] = filename

    if env.get('CM_DAE_REMOVE_EXTRACTED','') == 'yes':
        remove_extracted = True
    else:
        remove_extracted = False

    #verify checksum if file already present
    if env.get('CM_DAE_DOWNLOADED_CHECKSUM'):
        env['CM_DAE_DOWNLOADED_CHECKSUM_CMD'] = "echo {} {} | md5sum -c".format(env.get('CM_DAE_DOWNLOADED_CHECKSUM'), env['CM_DAE_FILENAME'])
    else:
        env['CM_DAE_DOWNLOADED_CHECKSUM_CMD'] = ""


    if env.get('CM_DAE_EXTRACT_DOWNLOADED','') == 'yes':
        if filename.endswith(".zip"):
            env['CM_DAE_EXTRACT_TOOL'] = "unzip"
        elif filename.endswith(".tar.gz"):
            env['CM_DAE_EXTRACT_TOOL'] = "tar -xvzf"
        elif filename.endswith(".tar"):
            env['CM_DAE_EXTRACT_TOOL'] = "tar -xvf"
        elif filename.endswith(".gz"):
            env['CM_DAE_EXTRACT_TOOL'] = 'gzip -d '+ ('-k ' if not remove_extracted else '')
            env['CM_DAE_GZIP'] = "gzip -d"
        elif env.get('CM_DAE_UNZIP','') == 'yes':
            env['CM_DAE_EXTRACT_TOOL'] = 'unzip '
        elif env.get('CM_DAE_UNTAR','') == 'yes':
            env['CM_DAE_EXTRACT_TOOL'] = 'tar -xvf '
        elif env.get('CM_DAE_GZIP','') == 'yes':
            env['CM_DAE_EXTRACT_CMD'] = 'gzip -d '+ ('-k ' if not remove_extracted else '')
        else:
            return {'return': 1, 'error': 'CM_DAE_EXTRACT_DOWNLOADED is yes but neither CM_DAE_UNZIP nor CM_DAE_UNTAR is yes'}

        env['CM_DAE_EXTRACT_CMD'] = env['CM_DAE_EXTRACT_TOOL'] + ' ' + filename

        if env.get('CM_DAE_EXTRACTED_FILENAME'):
            env['CM_DAE_FILENAME'] = env['CM_DAE_EXTRACTED_FILENAME']

        if env.get('CM_DAE_EXTRACTED_CHECKSUM'):
            env['CM_DAE_EXTRACTED_CHECKSUM_CMD'] = "echo {} {} | md5sum -c".format(env.get('CM_DAE_EXTRACTED_CHECKSUM'), env['CM_DAE_EXTRACTED_FILENAME'])
        else:
            env['CM_DAE_EXTRACTED_CHECKSUM_CMD'] = ""

    return {'return':0}

def postprocess(i):

    env = i['env']

    filename = os.path.basename(env['CM_DAE_FILENAME'])
    filepath = os.path.join(os.getcwd(), filename)

    if os.path.exists(filepath):
        env['CM_DAE_FILE_DOWNLOADED_PATH'] = filepath
    else:
        return {'return':1, 'error': 'CM_DAE_FILENAME is not set and CM_DAE_URL given is not pointing to a file'}

    return {'return':0}
