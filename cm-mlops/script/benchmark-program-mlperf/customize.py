from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']
    env = i['env']

    return {'return':0}

def postprocess(i):

    os_info = i['os_info']
    env = i['env']

    env['CM_MLPERF_RUN_CMD'] = env.get('CM_RUN_CMD')

    
    if env.get('CM_MLPERF_POWER', '') == "yes":
        if os_info['platform'] == 'windows':
            return {'return':1, 'error':'TBD: this script is not yet supported on Windows'}
        
        if env.get('CM_MLPERF_SHORT_RANGING_RUN', '') != 'no':
            os.system("echo '0' > "+env.get('CM_RUN_DIR','')+ "/count.txt")
            env['CM_MLPERF_RUN_CMD'] = "CM_MLPERF_RUN_COUNT=\$(cat \${CM_RUN_DIR}/count.txt); echo \${CM_MLPERF_RUN_COUNT};  CM_MLPERF_RUN_COUNT=\$((CM_MLPERF_RUN_COUNT+1));   echo \${CM_MLPERF_RUN_COUNT} > \${CM_RUN_DIR}/count.txt && if [ \${CM_MLPERF_RUN_COUNT} -eq \'1\' ]; then export CM_MLPERF_USER_CONF=\${CM_MLPERF_RANGING_USER_CONF}; else export CM_MLPERF_USER_CONF=\${CM_MLPERF_TESTING_USER_CONF}; fi && "+env.get('CM_RUN_CMD','').strip()
        else:
            env['CM_MLPERF_RUN_CMD'] = env.get('CM_RUN_CMD','').strip()

    return {'return':0}
