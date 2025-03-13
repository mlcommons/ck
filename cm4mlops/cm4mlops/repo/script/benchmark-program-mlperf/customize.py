#
# Copyright: https://github.com/mlcommons/ck/blob/master/cm-mlops/COPYRIGHT.md
# License: https://github.com/mlcommons/ck/blob/master/cm-mlops/LICENSE.md
#
# White paper: https://arxiv.org/abs/2406.16791
# History: https://github.com/mlcommons/ck/blob/master/HISTORY.CM.md
# Original repository: https://github.com/mlcommons/ck/tree/master/cm-mlops
#
# CK and CM project contributors: https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md
#

from cmind import utils
import os


def preprocess(i):
    os_info = i['os_info']
    env = i['env']

    return {'return': 0}


def postprocess(i):

    os_info = i['os_info']
    env = i['env']

    env['CM_MLPERF_RUN_CMD'] = env.get('CM_RUN_CMD')

    if env.get('CM_MLPERF_POWER', '') == "yes":

        if env.get('CM_MLPERF_SHORT_RANGING_RUN', '') != 'no':
            # Write '0' to the count.txt file in CM_RUN_DIR
            count_file = os.path.join(env.get('CM_RUN_DIR', ''), 'count.txt')
            with open(count_file, 'w') as f:
                f.write('0')

            if os_info['platform'] != 'windows':
                # Construct the shell command with proper escaping
                env['CM_MLPERF_RUN_CMD'] = r"""
CM_MLPERF_RUN_COUNT=\$(cat \${CM_RUN_DIR}/count.txt);
echo \${CM_MLPERF_RUN_COUNT};
CM_MLPERF_RUN_COUNT=\$((CM_MLPERF_RUN_COUNT+1));
echo \${CM_MLPERF_RUN_COUNT} > \${CM_RUN_DIR}/count.txt;

if [ \${CM_MLPERF_RUN_COUNT} -eq 1 ]; then
export CM_MLPERF_USER_CONF="${CM_MLPERF_RANGING_USER_CONF}";
else
export CM_MLPERF_USER_CONF="${CM_MLPERF_TESTING_USER_CONF}";
fi
;

                """ + env.get('CM_RUN_CMD', '').strip()
            else:
                env['CM_MLPERF_RUN_CMD'] = r"""
:: Read the current count from the file
set /p CM_MLPERF_RUN_COUNT=<%CM_RUN_DIR%\count.txt
echo !CM_MLPERF_RUN_COUNT!

:: Increment the count
set /a CM_MLPERF_RUN_COUNT=!CM_MLPERF_RUN_COUNT! + 1
echo !CM_MLPERF_RUN_COUNT! > %CM_RUN_DIR%\count.txt

:: Check the value and set the environment variable accordingly
if !CM_MLPERF_RUN_COUNT! EQU 1 (
    set CM_MLPERF_USER_CONF=%CM_MLPERF_RANGING_USER_CONF%
) else (
    set CM_MLPERF_USER_CONF=%CM_MLPERF_TESTING_USER_CONF%
)
                """ + env.get('CM_RUN_CMD', '').strip()
        else:
            # Just use the existing CM_RUN_CMD if no ranging run is needed
            env['CM_MLPERF_RUN_CMD'] = env.get('CM_RUN_CMD', '').strip()

    return {'return': 0}
