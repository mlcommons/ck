#
# Collective Knowledge (CK)
#
# See CK LICENSE.txt for licensing details.
# See CK COPYRIGHT.txt for copyright details.
#
# Developer: Grigori Fursin
#

# CK installation test

import ck.kernel as ck
import sys

a={'dyn_features':{'ft1':'1', 'ft2':'2'}, 'static_features':{'ft3':'3','ft4':'4'}}

print ('Original array:')
print (a)

r=ck.flatten_dict({'dict':a})
if r['return']>0: 
   print ('Error:'+r['error'])
   sys.exit(1)

x=r['dict']
print ('')
print ('Flattened array:')
print (x)

r=ck.restore_flattened_dict({'dict':x})
print ('')
print ('Restored array:')
print (r['dict'])


                             
sys.exit(0)
