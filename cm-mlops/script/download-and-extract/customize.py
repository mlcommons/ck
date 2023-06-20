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

    return {'return':0}

def postprocess(i):

    env = i['env']
    filepath = env.get('CM_EXTRACT_EXTRACTED_PATH', env.get('CM_DOWNLOAD_DOWNLOADED_PATH'))

    if not os.path.exists(filepath):
        return {'return':1, 'error': 'No extracted path set in "CM_EXTRACT_EXTRACTED_PATH"'}


    if env.get('CM_DAE_FINAL_ENV_NAME'):
        env['CM_DAE_FINAL_ENV_NAME'] = filepath

    env['CM_GET_DEPENDENT_CACHED_PATH'] =  filepath

    return {'return':0}
