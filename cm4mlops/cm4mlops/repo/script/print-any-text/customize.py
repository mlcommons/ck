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

# Developer(s): Grigori Fursin

from cmind import utils
import os


def postprocess(i):

    env = i['env']

    cm_env_keys = env.get('CM_PRINT_ANY_CM_ENV_KEYS', '').strip()
    os_env_keys = env.get('CM_PRINT_ANY_OS_ENV_KEYS', '').strip()

    printed = False
    for k, e, t in [(cm_env_keys, env, 'CM_ENV'),
                    (os_env_keys, os.environ, 'OS_ENV')]:

        if k != '':
            for kk in k.split(','):
                kk = kk.strip()
                if kk != '':
                    vv = e.get(kk)

                    print('{}[{}]: {}'.format(t, kk, vv))
                    printed = True

    if printed:
        print('')

    return {'return': 0}
