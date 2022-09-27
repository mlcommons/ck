#
# Collective Knowledge (CK)
#
# See CK LICENSE.txt for licensing details.
# See CK COPYRIGHT.txt for copyright details.
#
# Developer: Grigori Fursin
#

# Entry point for running CK tests for CI and coverage measurement tools

# TBD: check all tests for Python 3.8+

from __future__ import print_function

try:
    import ck.kernel as ck

    r = ck.access(['run', 'test'])
    if 'return' not in r:
        raise Exception('CK access function should always return key \'return\'!')
    exit(int(r['return']))

except ImportError as e:
    from sys import stderr
    from subprocess import call

    print('WARNING: CK kernel module for python is not installed & jupyter notebooks will not be supported', file=stderr)
    retcode = call(['ck', 'run', 'test'])
    exit(retcode)
