from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    name = env.get('CM_NAME','')
    if name != '':
        name = name.strip().lower()

        r = automation.update_deps({'deps':meta['prehook_deps'],
                                    'update_deps':{
                                      'python-venv':{
                                        'name':name
                                        }
                                      }
                                   })
        if r['return']>0: return r

    return {'return':0}
