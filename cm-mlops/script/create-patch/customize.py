from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    new_dir = env.get('CM_CREATE_PATCH_NEW', '')
    if new_dir == '':
        return {'return':1, 'error':'specify NEW directory using --new'}
    if not os.path.isdir(new_dir):
        return {'return':1, 'error':'NEW directory doesn\'t exist {}'.format(new_dir)}

    old_dir = env.get('CM_CREATE_PATCH_OLD', '')
    if old_dir == '':
        return {'return':1, 'error':'specify OLD directory using --old'}
    if not os.path.isdir(old_dir):
        return {'return':1, 'error':'OLD directory doesn\'t exist {}'.format(old_dir)}

    cmd = 'diff -Naur {} {} > patch.patch'.format(old_dir, new_dir)

    print ('Running command:')
    print (cmd)

    os.system(cmd)


    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
