#
# Collective Knowledge (CK)
#
# See CK LICENSE.txt for licensing details.
# See CK COPYRIGHT.txt for copyright details.
#
# Developer: Grigori Fursin
#

# CK dummy

import sys
import ck.kernel as ck

r = ck.access(sys.argv[1:])

if 'return' not in r:
    raise Exception('CK access function should always return key \'return\'!')

exit(int(r['return']))
