import os
import json

# Get path to some CK entry
import ck.kernel as ck

path_repo=ck.work['dir_local_repo']

print (path_repo)

from cdatabase import crepo

repo=crepo.cRepo(path_repo)

entries=repo.list(load_entries=True, object_name='kernel', object_id='b1e99f6461424276')
for entry in entries:

    print ('')
    print (entry.object_id)
    print (entry.object_name)
    print (entry.data_id)
    print (entry.data_name)
    print (entry.title)

