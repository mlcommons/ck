#
# Collective Knowledge (CK)
#
# See CK LICENSE.txt for licensing details.
# See CK COPYRIGHT.txt for copyright details.
#
# Developer: Grigori Fursin
#

# Entry point for running CK tests for CI and coverage measurement tools

import ck.kernel as ck

r = ck.access(['run', 'test'])

if 'return' not in r:
  raise Exception('CK access function should always return key \'return\'!')

exit(int(r['return']))
