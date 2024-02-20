from cmind import utils
import os
import hashlib

def preprocess(i):

    variation_tags = i.get('variation_tags',[])

    os_info = i['os_info']

    windows = os_info['platform'] == 'windows'

#    xsep = '^&^&' if windows else '&&'
    xsep = '&&'
   
    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    filename = env.get('CM_EXTRACT_FILEPATH','')
    if filename == '':
        return {'return': 1, 'error': 'Extract with no download requested and CM_EXTRACT_FILEPATH is not set'}

    env['CM_EXTRACT_FILENAME'] = filename

    # Check if extract to some path outside CM cache (to reuse large files later if cache is cleaned)
    extract_path = env.get('CM_EXTRACT_PATH', '')
    if extract_path != '':
        if not os.path.exists(extract_path):
            os.makedirs(extract_path, exist_ok = True)

        os.chdir(extract_path)

    # By default remove archive after extraction
    remove_extracted = False if env.get('CM_EXTRACT_REMOVE_EXTRACTED','').lower() == 'no' else True

    if filename.endswith(".zip"):
        env['CM_EXTRACT_TOOL'] = "unzip"
    elif filename.endswith(".tar.gz"):
        if windows:
            x = '"' if ' ' in filename else ''
            env['CM_EXTRACT_CMD0'] = 'gzip -d ' + x + filename + x
            filename = filename[:-3] # leave only .tar
            env['CM_EXTRACT_TOOL_OPTIONS'] = ' -xvf'
            env['CM_EXTRACT_TOOL'] = 'tar '
        else:
            env['CM_EXTRACT_TOOL_OPTIONS'] = ' --skip-old-files -xvzf '
            env['CM_EXTRACT_TOOL'] = 'tar '
    elif filename.endswith(".tar.xz"):
        if windows:
            x = '"' if ' ' in filename else ''
            env['CM_EXTRACT_CMD0'] = 'xz -d ' + x + filename + x
            filename = filename[:-3] # leave only .tar
            env['CM_EXTRACT_TOOL_OPTIONS'] = ' -xvf'
            env['CM_EXTRACT_TOOL'] = 'tar '
        else:
            env['CM_EXTRACT_TOOL_OPTIONS'] = ' -xvJf'
            env['CM_EXTRACT_TOOL'] = 'tar '
    elif filename.endswith(".tar"):
        env['CM_EXTRACT_TOOL_OPTIONS'] = ' -xvf'
        env['CM_EXTRACT_TOOL'] = 'tar '
    elif filename.endswith(".gz"):
        # Check target filename
        extracted_filename = env.get('CM_EXTRACT_EXTRACTED_FILENAME','')
        if extracted_filename == '':
            extracted_filename = os.path.basename(filename)[:-3]
            env['CM_EXTRACT_EXTRACTED_FILENAME'] = extracted_filename

        x = '-c' if windows else '-k'
        env['CM_EXTRACT_TOOL_OPTIONS'] = ' -d '+ (x + ' ' if not remove_extracted else '') + ' > ' + extracted_filename + ' < '

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

    env['CM_EXTRACT_PRE_CMD'] = ''
    
    extract_to_folder = env.get('CM_EXTRACT_TO_FOLDER', '')

    # Check if extract to additional folder in the current directory (or external path)
    # to avoid messing up other files and keep clean directory structure
    # particularly if archive has many sub-directories and files
    if extract_to_folder != '':
        if 'tar ' in env['CM_EXTRACT_TOOL']:
            x = '' if windows else '-p'

            #env['CM_EXTRACT_TOOL_OPTIONS'] = ' --one-top-level='+ env['CM_EXTRACT_TO_FOLDER'] + env.get('CM_EXTRACT_TOOL_OPTIONS', '')
            env['CM_EXTRACT_TOOL_OPTIONS'] = ' -C '+ extract_to_folder + ' ' + env.get('CM_EXTRACT_TOOL_OPTIONS', '')
            env['CM_EXTRACT_PRE_CMD'] = 'mkdir '+x+' '+ extract_to_folder +  ' ' + xsep + ' '
            env['CM_EXTRACT_EXTRACTED_FILENAME'] = extract_to_folder

        elif 'unzip' in env['CM_EXTRACT_TOOL']:
            env['CM_EXTRACT_TOOL_OPTIONS'] = ' -d '+ extract_to_folder
            env['CM_EXTRACT_EXTRACTED_FILENAME'] = extract_to_folder


    x = '"' if ' ' in filename else ''
    env['CM_EXTRACT_CMD'] = env['CM_EXTRACT_PRE_CMD'] + env['CM_EXTRACT_TOOL'] + ' ' + \
                            env.get('CM_EXTRACT_TOOL_EXTRA_OPTIONS', '') + \
                            ' ' + env.get('CM_EXTRACT_TOOL_OPTIONS', '')+ ' '+ x + filename + x

    print ('')
    print ('Current directory: {}'.format(os.getcwd()))
    print ('Command line: "{}"'.format(env['CM_EXTRACT_CMD']))
    print ('')
    
    final_file = env.get('CM_EXTRACT_EXTRACTED_FILENAME', '')

    if final_file!='':
        if env.get('CM_EXTRACT_EXTRACTED_CHECKSUM_FILE', '') != '':
            env['CM_EXTRACT_EXTRACTED_CHECKSUM_CMD'] = ("cd {}  " + xsep + "  md5sum -c {}").format(final_file, env.get('CM_EXTRACT_EXTRACTED_CHECKSUM_FILE'))
        elif env.get('CM_EXTRACT_EXTRACTED_CHECKSUM', '') != '':
            x='*' if os_info['platform'] == 'windows' else ''
            env['CM_EXTRACT_EXTRACTED_CHECKSUM_CMD'] = "echo {} {}{} | md5sum -c".format(env.get('CM_EXTRACT_EXTRACTED_CHECKSUM'), x, env['CM_EXTRACT_EXTRACTED_FILENAME'])
        else:
            env['CM_EXTRACT_EXTRACTED_CHECKSUM_CMD'] = ""
    else:
        env['CM_EXTRACT_EXTRACTED_CHECKSUM_CMD'] = ""

# Not needed - can be simpler with cmd /c {empty}
#    if os_info['platform'] == 'windows':
#        # Check that if empty CMD, should add ""
#        for x in ['CM_EXTRACT_CMD', 'CM_EXTRACT_EXTRACTED_CHECKSUM_CMD']:
#            env[x+'_USED']='YES' if env.get(x,'')!='' else 'NO'

    
    # If force cache, add filepath to tag unless _path is used ...
    path_tag = 'path.'+filename

    add_extra_cache_tags = []
    if path_tag not in variation_tags:
        add_extra_cache_tags.append(path_tag)

    return {'return':0, 'add_extra_cache_tags':add_extra_cache_tags}


def postprocess(i):

    automation = i['automation']

    env = i['env']

    extract_to_folder = env.get('CM_EXTRACT_TO_FOLDER', '')
    extract_path = env.get('CM_EXTRACT_PATH', '')
    
    extracted_file = env.get('CM_EXTRACT_EXTRACTED_FILENAME', '')

    # Preparing filepath
    #   Can be either full extracted filename (such as model) or folder
    
    if extracted_file != '':
        filename = os.path.basename(extracted_file)

# We do not use this env variable anymore
#        folderpath = env.get('CM_EXTRACT_EXTRACT_TO_PATH', '')
        folderpath = extract_path if extract_path!='' else os.getcwd()

        filepath = os.path.join(folderpath, filename)
    else:

        filepath = os.getcwd() # Extracted to the root cache folder

    if not os.path.exists(filepath):
        return {'return':1, 'error': 'Path {} was not created or doesn\'t exist'.format(filepath)}
#        return {'return':1, 'error': 'CM_EXTRACT_EXTRACTED_FILENAME and CM_EXTRACT_TO_FOLDER are not set'}

    env['CM_EXTRACT_EXTRACTED_PATH'] = filepath

    # Set external environment variable with the final path
    if env.get('CM_EXTRACT_FINAL_ENV_NAME', '')!='':
        env[env['CM_EXTRACT_FINAL_ENV_NAME']] = filepath

    # Detect if this file will be deleted or moved 
    env['CM_GET_DEPENDENT_CACHED_PATH'] =  filepath

    # Check if need to remove archive after extraction
    if env.get('CM_EXTRACT_REMOVE_EXTRACTED','').lower() != 'no':
        archive_filepath=env.get('CM_EXTRACT_FILEPATH','')
        if archive_filepath!='' and os.path.isfile(archive_filepath):
            os.remove(archive_filepath)

    # Since may change directory, check if need to clean some temporal files
    automation.clean_some_tmp_files({'env':env})

    return {'return':0}
