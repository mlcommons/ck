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
import json


print ('Console encoding:', sys.stdin.encoding)
print ('Python default encoding:', sys.getdefaultencoding())

print ('')

#s1=s.encode()
#s2=s.encode(sys.stdin.encoding)
#print(s2)
#print(s) #.encode(sys.stdin.encoding))
#print ('')

##############################################
print ('Processing test2unicode.txt ...')
print ('')

f=open('test2unicode.txt', 'rb')
b=f.read() # Python2: 8bits string (not unicode)
f.close()

s=b.decode('utf-8') # make it unicode (from utf-8 -> to default terminal encoding)
print (type(s))

s1=s.encode('utf-8')
print (type(s1))

#s2=u'\u0420\u043e\u0441\u0441\u0438\u044f'
#
#for l in range(0, len(s1)):
#    print (hex(ord(s1[l])))

s2=s.encode(sys.stdin.encoding, errors='ignore')
print (type(s2))

if sys.version_info[0]>2:
   sys.stdout.buffer.write(s2) # will write proper unicode
   sys.stdout.buffer.write(b'\n')
else:
   print (s2)

f=open('test2unicode_out_bin.txt','wb')
f.write(b)
f.close()

##############################################
print ('Processing test2unicode.json ...')
print ('')

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

##############################################
print ('Processing input ...')
print ('')

if sys.version_info[0]>2:
   s=input('Input string: ')
else:
   s=raw_input('Input string: ').decode(sys.stdin.encoding).encode('utf-8')
   print (s)
if sys.version_info[0]>2:
   b1=s.encode('utf-8')
#   b1=s.encode(sys.stdin.encoding)
   sys.stdout.buffer.write(b1) # will write proper unicode
   sys.stdout.buffer.write(b'\n')
else:
   print(s)

if sys.version_info[0]>2:
   f=open('test2input.txt','wb')
   f.write(s.encode('utf-8'))
else:
   f=open('test2input.txt','w')
   f.write(s)
f.close()
