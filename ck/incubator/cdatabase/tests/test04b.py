import os
import json
import sys
import time

from cdatabase import crepo
import ck.kernel as ck


import gc
import sys

def get_obj_size(obj):
    marked = {id(obj)}
    obj_q = [obj]
    sz = 0

    while obj_q:
        sz += sum(map(sys.getsizeof, obj_q))

        # Lookup all the object referred to by the object in obj_q.
        # See: https://docs.python.org/3.7/library/gc.html#gc.get_referents
        all_refr = ((id(o), o) for o in gc.get_referents(*obj_q))

        # Filter object that are already marked.
        # Using dict notation will prevent repeated objects.
        new_refr = {o_id: o for o_id, o in all_refr if o_id not in marked and not isinstance(o, type)}

        # The new obj_q will be the ones that were not marked,
        # and we will update marked with their ids so we will
        # not traverse them again.
        obj_q = new_refr.values()
        marked.update(new_refr.keys())

    return sz


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
        
        tmp_entries=repo.list(load_entries=True, object_name='package',
                              data_id='04622c746f287473')
        entries+=tmp_entries

        end = time.time()

        print ('  Entries: {}'.format(len(tmp_entries)))
        print ('  Total time: {:.2f}'.format(end-start))

print ('')
for entry in entries:
    print (entry.get_path())

print ('')
print ('Number of entries: {}'.format(len(entries)))

print ('Size: {}'.format(sys.getsizeof(entries)))
print ('Size2: {}'.format(get_obj_size(entries)))
