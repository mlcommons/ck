from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_TMP_QUIET', False) == 'yes')

    name = env.get('CM_NAME','')
    if name != '':
        name_tag = name.lower()

        r = automation.update_deps({'deps':meta['post_deps'],
                                    'update_deps':{
                                      'python-venv':{
                                        'extra_cache_tags':name
                                        }
                                      }
                                   })
        if r['return']>0: return r

    return {'return':0}
