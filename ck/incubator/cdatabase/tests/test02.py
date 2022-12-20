import os
import json

# Get path to some CK entry
import ck.kernel as ck
r=ck.access({'action':'load',
             'module_uoa':'kernel',
             'data_uoa':'default'})
if r['return']>0: ck.err(r)
path=r['path']

path_obj=os.path.dirname(path)

from cdatabase import cobject

obj=cobject.cObject(path_obj)

obj.list(load_entries=True, object_id='b1e99f6461424276')
entries=obj.get_entries()
for d in entries:
    entry=entries[d]

    print ('')
    print (entry.object_id)
    print (entry.object_name)
    print (entry.data_id)
    print (entry.data_name)
    print (entry.title)

