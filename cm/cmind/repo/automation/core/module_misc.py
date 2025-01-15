# Generate CM UID
#
# Authors: Grigori Fursin
# Contributors:
#
# Copyright: https://github.com/mlcommons/ck/blob/master/COPYRIGHT.txt
# License: https://github.com/mlcommons/ck/blob/master/LICENSE.md
# History: https://github.com/mlcommons/ck/blob/master/HISTORY.CM.md
# White paper: https://arxiv.org/abs/2406.16791
# Project contributors: https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md

import cmind.utils as utils

############################################################


def uid(i):

    console = i.get('out') == 'con'

    r = utils.gen_uid()

    if console:
        print(r['uid'])

    return r
