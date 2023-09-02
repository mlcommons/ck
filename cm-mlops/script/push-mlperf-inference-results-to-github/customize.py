from cmind import utils
import cmind as cm
import os

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    meta = i['meta']
    automation = i['automation']

    repo = env.get('CM_MLPERF_RESULTS_GIT_REPO_URL', '')
    if repo.strip() == '':
        return {'return': 1, 'error': 'Invalid GIT_REPO_URL for MLPERF results'}

    branch = env.get('CM_GIT_BRANCH', '')
    if branch:
        extra_tags_string = f",_branch.{branch}"
    else:
        extra_tags_string = ""

    r = automation.update_deps({'deps':meta['prehook_deps'],
        'update_deps':{
            'get-git-repo':{
                'tags':"_repo."+repo+extra_tags_string
                }
            }
        })
    if r['return']>0: return r
    env['CM_MLPERF_RESULTS_REPO_COMMIT_MESSAGE'] = env.get('CM_MLPERF_RESULTS_REPO_COMMIT_MESSAGE', 'Added new results')

    return {'return':0}

def postprocess(i):
    return {'return':0}
