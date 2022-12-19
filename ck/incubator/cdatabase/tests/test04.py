import os
import json
import sys
import time

from cdatabase import crepo

# Get path to some CK entry
import ck.kernel as ck

r=ck.access({'action':'list',
             'module_uoa':'repo',
             'add_meta':'yes'})
if r['return']>0: ck.err(r)

lst=r['lst']

entries=[]

start = time.time()
for l in lst:
    m=l['meta']
    p=m.get('path','')
    
    if p!='' and os.path.isdir(p):
        print (p)
        repo=crepo.cRepo(p)
        
        tmp_entries=repo.list(load_entries=True) #, object_name='program') #, object_id='b1e99f6461424276')
        entries+=tmp_entries

        end = time.time()

        print ('  Entries: {}'.format(len(tmp_entries)))
        print ('  Total time: {:.2f}'.format(end-start))

print ('')
print ('Number of entries: {}'.format(len(entries)))

print ('Size: {}'.format(sys.getsizeof(entries)))
