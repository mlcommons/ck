#
# Collective Knowledge (CK)
#
# See CK LICENSE.txt for licensing details.
# See CK COPYRIGHT.txt for copyright details.
#
# Developer: Grigori Fursin
#

# CK dummy

from ck.kernel import init, err

# Initialize various vars and paths
r = init({})
if r['return'] > 0:
    err(r)
