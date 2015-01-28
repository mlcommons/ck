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

x=sys.argv

if len(x)<2:
   print ('Add some command line parameter')
   exit(1)

print ('Console stdin encoding:', sys.stdin.encoding)
print ('Console stdout encoding:', sys.stdout.encoding)
print ('Python default encoding:', sys.getdefaultencoding())

print ('')

ss=x[1]

#print (repr(ss))

#print (" ".join(hex(ord(n)) for n in ss))
#sx=unicode(ss)
#print (repr(sx))

#print (" ".join(hex(ord(n)) for n in sx))


#print (repr(ss))

#if sys.version_info[0]<3:
#   ss=ss.decode('utf8')#sys.stdin.encoding) #sys.stdin.encoding).encode('utf-8')
#   print (ss)


if sys.version_info[0]>2:
   b1=ss.encode('utf-8')
#   b1=s.encode(sys.stdin.encoding)
   sys.stdout.buffer.write(b1) # will write proper unicode
   sys.stdout.buffer.write(b'\n')
else:
   print(ss)



if sys.version_info[0]>2:
   f=open('test2unicode.json', 'r', encoding='utf-8')
else:
   f=open('test2unicode.json', 'r')
s=f.read() # read as string
f.close()

if sys.version_info[0]>2:
   d=json.loads(s)
else:
   d=json.loads(s, encoding='utf-8')

d['x']=ss

b1=d['languages'][1].encode('utf-8')
if sys.version_info[0]>2:
   sys.stdout.buffer.write(b1) # will write proper unicode
   sys.stdout.buffer.write(b'\n')
else:
   print(b1)




if sys.version_info[0]>2:
   de=json.dumps(d, indent=2, ensure_ascii=False)
else:
   de=json.dumps(d, indent=2, ensure_ascii=False, encoding='utf-8')

print('')
b=de.encode('utf-8')

if sys.version_info[0]>2:
   sys.stdout.buffer.write(b) # will write proper unicode
else:
   print(b)

if sys.version_info[0]>2:
   f=open('test2unicode_out.json','wb')
else:
   f=open('test2unicode_out.json','w')
f.write(de.encode('utf-8'))
f.close()
