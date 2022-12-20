import os
import json

# Get path to some CK entry
import ck.kernel as ck
r=ck.access({'action':'load',
             'module_uoa':'kernel',
             'data_uoa':'default'})
if r['return']>0: ck.err(r)
path=r['path']

from cdatabase import cdata

data=cdata.cData(path)

if data.load(force_ck_format=True):
    print ('')
    print ('Old format:')
    print ('')
    print (json.dumps(data.get_meta(), indent=2))

    print (data.ck)

if data.load():
    print ('')
    print ('New format:')
    print ('')
    print (json.dumps(data.get_meta(), indent=2))


print ('')
print ('Save data:')
print ('')
print (data.save())

#data=cdata.cData("D:\\Work")
#data.load()
#data.meta['aaaaa']='bbbbb'
#data.save(force_yaml=True)
