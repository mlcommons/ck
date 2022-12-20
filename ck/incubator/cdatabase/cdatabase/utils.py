#
# Utils for cDatabase
#

from cdatabase.config import cfg

###########################################################################
def dir_list(path: str, name: str, xid: str = ""):

    import os

    wildcards = '*' in name or '?' in name

    # List directories
    dir_list = []

    if xid != '':
        # REDO will global cache
        # Check if UID for more than 1 name - inconsistency
        
        # Check if in cache (.cm)
        cache_dir = os.path.join(path, cfg['cache_id_dir'])
        if os.path.isdir(cache_dir):
            cache_file = os.path.join(cache_dir, cfg['cache_id_prefix']+xid)
            if os.path.isfile(cache_file):
                with open(cache_file, 'r') as cf:
                    name = cf.read().strip()
                    wildcards = False

                # Check if entry exists
                path2 = os.path.join(path, name)
                if not os.path.isdir(path2):
                    name = ''
                    os.remove(cache_file)

    if name != '' and not wildcards:
        dir_list = [name]

    if len(dir_list)==0:
        dir_list = os.listdir(path)

        if wildcards:
            import fnmatch

            new_dir_list = []

            for d in dir_list:
                if fnmatch.fnmatch(d, name):
                    new_dir_list.append(d)

            dir_list = new_dir_list

    return dir_list
