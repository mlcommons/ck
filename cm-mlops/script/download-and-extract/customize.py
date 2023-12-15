from cmind import utils
import os
import hashlib

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    if i['input'].get('force_cache'):
        extra_cache_tags = i['input'].get('extra_cache_tags', '')
        r = automation.update_deps({
            'deps': meta['prehook_deps'] + meta['posthook_deps'],
            'update_deps':{
                'download-script': {
                    'extra_cache_tags': extra_cache_tags,
                    'force_cache': True
                    },
                'extract-script':{
                    'extra_cache_tags': extra_cache_tags,
                    'force_cache': True
                    }
                }
            })
        if r['return']>0: return r

    if env.get('CM_DOWNLOAD_LOCAL_FILE_PATH'):
        filepath = env['CM_DOWNLOAD_LOCAL_FILE_PATH']

        if not os.path.exists(filepath):
            return {'return':1, 'error':'Local file {} doesn\'t exist'.format(filepath)}

        env['CM_EXTRACT_REMOVE_EXTRACTED']='no'
    
    return {'return':0}

def postprocess(i):

    env = i['env']
    filepath = env.get('CM_EXTRACT_EXTRACTED_PATH', '')
    if filepath == '':
        filepath = env.get('CM_DOWNLOAD_DOWNLOADED_PATH', '')

    if filepath == '':
        return {'return':1, 'error': 'No extracted path set in "CM_EXTRACT_EXTRACTED_PATH"'}
    if not os.path.exists(filepath):
        return {'return':1, 'error': 'Extracted path doesn\'t exist: {}'.format(filepath)}

    if env.get('CM_DAE_FINAL_ENV_NAME'):
        env[env['CM_DAE_FINAL_ENV_NAME']] = filepath

    env['CM_GET_DEPENDENT_CACHED_PATH'] =  filepath

    return {'return':0}
