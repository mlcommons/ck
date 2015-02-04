#
# Collective Knowledge (CK)
#
# See CK LICENSE.txt for licensing details.
# See CK Copyright.txt for copyright details.
#
# Developer: Grigori Fursin
#

# CK installation test

import ck.kernel as ck
import sys
import json

##############################################
print('Calling CK ...')
print('')

r=ck.test()

if r.get('return',0)!=123:
   print('')
   print('Test FAILED (output!=123) !')
   sys.exit(1)

##############################################
print('Getting CK version ...')
print('')

r=ck.get_version()
if r.get('return',-1)!=0:
   ck.out('')
   ck.out('Test FAILED!')
   sys.exit(1)

ck.out('')
ck.out('CK version: '+r.get('ver_str',''))

##############################################
ck.out('Parsing CK command line ...')
ck.out('')
cmd="mv data cid1 cid2 key1=value1 key2=value2 key3 key4=value4 -key10 -key11=value11 --key12 --key13=value13 @test1.json @test2.json @test2unicode.json @@{'a':['b','c']} -- abc"
i=cmd.split(' ')

r=ck.list2dict(i)
if r['return']>0:
   ck.out('Test FAILED ('+r['error']+')!')
   sys.exit(1)

ck.out(json.dumps(r, indent=2))
                             
##############################################
ck.out('')
ck.out('Test passed successfully!')

sys.exit(0)
