from cmind import utils
import cmind as cm
import os

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    meta = i['meta']
    automation = i['automation']

    repo = env.get('CM_GIT_REPO_URL')
    r = automation.update_deps({'deps':meta['prehook_deps'],
                                'update_deps':{
                                    'get-git-repo':{
                                       'tags':"_repo."+repo
                                        }
                                    }
                                })
    if r['return']>0: return r

    return {'return':0}

def postprocess(i):
    return {'return':0}
