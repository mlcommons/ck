from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']
    env = i['env']
    if env.get('CM_MLPERF_POWER', '') == "yes":
        if env.get('CM_MLPERF_SHORT_RANGING_RUN', '') == 'yes':
            os.system("echo '0' > count.txt")
            env['CM_MLPERF_RUN_CMD'] = "CM_MLPERF_RUN_COUNT=\$(cat count.txt); echo \${CM_MLPERF_RUN_COUNT};  CM_MLPERF_RUN_COUNT=\$((CM_MLPERF_RUN_COUNT+1));   echo \${CM_MLPERF_RUN_COUNT} > count.txt && if [ \${CM_MLPERF_RUN_COUNT} -eq \'1\' ]; then export CM_MLPERF_USER_CONF_PREFIX=\'ranging_\'; else export CM_MLPERF_USER_CONF_PREFIX=\'\'; fi && "+env['CM_RUN_CMD'].strip()
        else:
            env['CM_MLPERF_RUN_CMD'] = env['CM_RUN_CMD'].strip()

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
