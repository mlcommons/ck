from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    return {'return':0}

def postprocess(i):

    os_info = i['os_info']
    
    script_path = i['artifact'].path

    env = i['env']

    path = env['CM_AXS_PATH']
    env['+PATH'] = [ path ]

    if os_info['platform'] == 'windows':
        os.chdir(path)

        # Applying patch
        cmd = 'patch -p1 < {}'.format(os.path.join(script_path, 'patch', 'fix-python-name-on-windows.patch'))

        print ('Patching code: {}'.format(cmd))
        os.system(cmd)

    return {'return':0}
