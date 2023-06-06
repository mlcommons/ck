from cmind import utils
import os
import shutil

def preprocess(i):

    os_info = i['os_info']

#    if os_info['platform'] == 'windows':
#        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']
    meta = i['meta']

    if 'CM_GIT_DEPTH' not in env:
        env['CM_GIT_DEPTH'] = ''

    return {'return':0}


def postprocess(i):

    env = i['env']
    state = i['state']

    env['CM_EEMBC_ENERGY_RUNNER_SRC'] = os.path.join(os.getcwd(), 'src')
    datasets_src_path = os.path.join(os.getcwd(), 'src', 'datasets')
    env['CM_EEMBC_ENERGY_RUNNER_SRC_DATASETS'] = datasets_src_path

    # Get user directory for EEMBC runner path
    home_directory = os.path.expanduser( '~' )

    sessions_path = os.path.join(home_directory, 'eembc', 'runner', 'sessions')

    print ('')
    print ('Path to EEMBC runner sessions: {}'.format(sessions_path))

    env['CM_EEMBC_ENERGY_RUNNER_SESSIONS'] = sessions_path

    if not os.path.isdir(sessions_path):
        os.makedirs(sessions_path)

    datasets_path = os.path.join(home_directory, 'eembc', 'runner', 'benchmarks', 'ulp-mlperf', 'datasets')

    print ('')
    print ('Path to EEMBC runner datasets: {}'.format(datasets_path))

    if not os.path.isdir(datasets_path):
        os.makedirs(datasets_path)

    env['CM_EEMBC_ENERGY_RUNNER_DATASETS'] = datasets_path

    print ('')
    print ('Copying datasets to EEMBC user space ...')

    shutil.copytree(datasets_src_path, datasets_path, dirs_exist_ok=True)

    return {'return':0}
