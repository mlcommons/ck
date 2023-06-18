import cmind as cm
from cmind import utils

import os
import subprocess
import json
import shutil

def preprocess(i):

    env = i['env']

    cur_dir = os.getcwd()

    # Query cache for results dirs
    env_repo_tags=env.get('CM_IMPORT_TINYMLPERF_REPO_TAGS','').strip()
    xtags='' if env_repo_tags =='' else ',version-'+env_repo_tags
    
    r = cm.access({'action':'find',
                   'automation':'cache,541d6f712a6b464e',
                   'tags':'get,repo,mlperf-tiny-results'+xtags})
    if r['return']>0: return r

    lst = r['list']

    if len(lst)==0:
        return {'return':1, 'error':'no repository with TinyMLPerf results found'}

    for c in lst:
        path = os.path.join(c.path, 'repo')

        if os.path.isdir(path):
            meta = c.meta

            tags = meta['tags']

            version = ''
            for t in tags:
                if t.startswith('version-'):
                    version = 'v'+t[8:]
                    break

            # Run local script
            run_script_input = i['run_script_input']
            automation = i['automation']

            env['CM_TINYMLPERF_REPO_PATH'] = path
            env['CM_TINYMLPERF_CURRENT_DIR'] = cur_dir
            env['CM_TINYMLPERF_REPO_VERSION'] = version

            print ('')
            print ('Repo path: {}'.format(path))

            r = automation.run_native_script({'run_script_input':run_script_input, 
                                              'env':env, 
                                              'script_name':'run_submission_checker'})
            if r['return']>0:
                return r

    return {'return':0}

def postprocess(i):

    env = i['env']

    path = env['CM_TINYMLPERF_REPO_PATH']
    cur_dir = env['CM_TINYMLPERF_CURRENT_DIR']
    version = env['CM_TINYMLPERF_REPO_VERSION']

    for ext in ['.csv', '.xlsx']:
        
        p1 = os.path.join (path, 'summary'+ext)
        p2 = os.path.join (cur_dir, 'summary-{}{}'.format(version,ext))

        if not os.path.isfile(p1):
            return {'return':1, 'error':'summary.csv file was not created'}

        if os.path.isfile(p2):
            os.remove(p2)

        shutil.copy(p1,p2)

    return {'return':0}
