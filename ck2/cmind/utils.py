# Some functionality may be reused from the CK framework

import os

ERROR_UNKNOWN_FILE_EXTENSION = 1
ERROR_PATH_NOT_FOUND = 2
ERROR_FILE_NOT_FOUND = 16

###########################################################################
def load_yaml_and_json(file_name_without_ext, check_if_exists = False, encoding = 'utf8'):

    meta = {}

    for file_ext in [('.yaml', load_yaml), 
                     ('.json', load_json)]:
        file_name = file_name_without_ext + file_ext[0]

        r = file_ext[1](file_name, check_if_exists = True, encoding = encoding) # To avoid failing if doesn't exist
        if r['return'] > 0 and r['return'] != ERROR_FILE_NOT_FOUND: return r

        meta.update(r.get('meta', {}))

    return {'return':0, 'meta':meta}

###########################################################################
def is_file_json_or_yaml(file_name):

    for file_ext in ['.yaml', '.json']:
        file_path = file_name + file_ext

        if os.path.isfile(file_path):
            return {'return':0, 'is_file':True, 'path':file_path}

    return {'return':0, 'is_file':False}

###########################################################################
def load_json_or_yaml(file_name, check_if_exists = False, encoding = 'utf8'):

    if file_name.endswith('.json'):
        return load_json(file_name, check_if_exists = check_if_exists, encoding = encoding)
    elif file_name.endswith('.yaml'):
        return load_yaml(file_name, check_if_exists = check_if_exists, encoding = encoding)

    return {'return':ERROR_UNKNOWN_FILE_EXTENSION, 'error':'file extension must be .json or .yaml in {}'.format(file_name)}

###########################################################################
def save_json_or_yaml(file_name, meta, sort_keys=False, encoding = 'utf8'):
    if file_name.endswith('.json'):
        return save_json(file_name, meta, sort_keys, encoding = encoding)
    elif file_name.endswith('.yaml'):
        return save_yaml(file_name, meta, sort_keys, encoding = encoding)

    return {'return':ERROR_UNKNOWN_FILE_EXTENSION, 'error':'unknown file extension'}

###########################################################################
def load_json(file_name, check_if_exists = False, encoding='utf8'):

    if check_if_exists:
        import os
        if not os.path.isfile(file_name):
            return {'return':ERROR_FILE_NOT_FOUND, 'error':'File {} not found'.format(file_name)}
    
    import json
    
    with open(file_name, encoding=encoding) as jf:
        meta = json.load(jf)

    return {'return':0,
            'meta': meta}

###########################################################################
def save_json(file_name, meta={}, indent=2, sort_keys=True, encoding = 'utf8'):

    import json
    
    with open(file_name, 'w', encoding = encoding) as jf:
        jf.write(json.dumps(meta, indent=indent, sort_keys=sort_keys))

    return {'return':0}

###########################################################################
def load_yaml(file_name, check_if_exists = False, encoding = 'utf8'):

    if check_if_exists:
        import os
        if not os.path.isfile(file_name):
            return {'return':ERROR_FILE_NOT_FOUND, 'error':'File {} not found'.format(file_name)}

    import yaml
    
    with open(file_name, 'rt', encoding = encoding) as yf:
        meta = yaml.load(yf, Loader=yaml.FullLoader)

    return {'return':0,
            'meta': meta}

###########################################################################
def save_yaml(file_name, meta={}, sort_keys=True, encoding = 'utf8'):

    import yaml
    
    with open(file_name, 'w', encoding = encoding) as yf:
        meta = yaml.dump(meta, yf)

    return {'return':0}

###########################################################################
def check_and_create_dir(path):
    """
    Create directories if path doesn't exist
    """

    if not os.path.isdir(path):
       os.makedirs(path)

    return {'return':0}

###########################################################################
def find_file_in_dir_and_above(filename,
                               path=""):
    """
    Find file in the current directory or above

    Args:
        filename (str)
        path (str)

    Returns:
        (dict) return (int): 0 - if found
                             16 - if not found
               (error) (str)

               path (str): path where file is found

               path_to_file (str): path to file
    """

    if path == "":
        path = os.getcwd()

    if not os.path.isdir(path):
        return {'return':ERROR_PATH_NOT_FOUND, 'error': 'path not found'}

    path = os.path.realpath(path)

    while True:
        test_path = os.path.join(path, filename)

        if os.path.isfile(test_path):
            return {'return':0, 'path': path, 'path_to_file': test_path}

        new_path, skip = os.path.split(path)

        if new_path == path:
            break

        path = new_path    

    return {'return':ERROR_FILE_NOT_FOUND, 'error': 'path not found'}

##############################################################################
def list_all_files(i):
    """List all files recursively in a given directory
       (from CK framework)

    Args:    
              path (str): top level path
              (file_name) (str): search for a specific file name
              (pattern) (str): return only files with this pattern
              (path_ext) (str): path extension (needed for recursion)
              (limit) (str): limit number of files (if directories with a large number of files)
              (number) (int): current number of files
              (all) (str): if 'yes' do not ignore special directories (like .cm)
              (ignore_names) (list): list of names to ignore
              (ignore_symb_dirs) (str): if 'yes', ignore symbolically linked dirs 
                                        (to avoid recursion such as in LLVM)
              (add_path) (str) - if 'yes', add full path to the final list of files

    Returns:
              (dict): Unified CK dictionary:

                return (int): return code =  0, if successful
                                          >  0, if error
                (error) (str): error text if return > 0

                list (dict): dictionary of all files:
                             {"file_with_full_path":{"size":.., "path":..}

                sizes (dict): sizes of all files (the same order as above "list")

                number (int): (internal) total number of files in a current directory (needed for recursion)

    """

    import sys
    
    number = 0
    if i.get('number', '') != '':
        number = int(i['number'])

    inames = i.get('ignore_names', [])

    fname = i.get('file_name', '')

    limit = -1
    if i.get('limit', '') != '':
        limit = int(i['limit'])

    a = {}

    iall = i.get('all', '')

    pe = ''
    if i.get('path_ext', '') != '':
        pe = i['path_ext']

    po = i.get('path', '')
    if sys.version_info[0] < 3:
        po = unicode(po)

    pattern = i.get('pattern', '')
    if pattern != '':
        import fnmatch

    xisd = i.get('ignore_symb_dirs', '')
    isd = False
    if xisd == 'yes':
        isd = True

    ap = i.get('add_path', '')

    try:
        dirList = os.listdir(po)
    except Exception as e:
        None
    else:
        for fn in dirList:
            p = os.path.join(po, fn)
            if iall == 'yes' or fn not in cfg['special_directories']:
                if len(inames) == 0 or fn not in inames:
                    if os.path.isdir(p):
                        if not isd or os.path.realpath(p) == p:
                            r = list_all_files({'path': p, 'all': iall, 'path_ext': os.path.join(pe, fn),
                                                'number': str(number), 'ignore_names': inames, 'pattern': pattern,
                                                'file_name': fname, 'ignore_symb_dirs': xisd, 'add_path': ap, 'limit': limit})
                            if r['return'] > 0:
                                return r
                            a.update(r['list'])
                    else:
                        add = True

                        if fname != '' and fname != fn:
                            add = False

                        if pattern != '' and not fnmatch.fnmatch(fn, pattern):
                            add = False

                        if add:
                            pg = os.path.join(pe, fn)
                            if os.path.isfile(p):
                                a[pg] = {'size': os.stat(p).st_size}

                                if ap == 'yes':
                                    a[pg]['path'] = po

                    number = len(a)
                    if limit != -1 and number >= limit:
                        break

    return {'return': 0, 'list': a, 'number': str(number)}

###########################################################################
def gen_uid():
    """
    Generate CM UID
    """

    import uuid

    return {'return':0,
            'uid':uuid.uuid4().hex[:16]}

###########################################################################
def is_cm_uid(obj):
    """
    Check if a string is a valid CM UID

    Args:    
              obj (str): CM alias or UID

    Returns:
              (bool): True if a string is a valid CK UID
    """

    import re

    if len(obj) != 16:
        return False

    pattern = r'[^\.a-f0-9]'
    if re.search(pattern, obj.lower()):
        return False

    return True

###########################################################################
def parse_cm_object(obj, max_length = 2):
    """
    Parse CM object

    Args:    
        obj (str): CM object

                      CM sub-object = UID | alias | alias,UID | UID,alias
                      repo CM sub-object | CM sub-object

                      Examples:

                      cm os
                      cm 281d5c3e3f69d8e7
                      cm os,281d5c3e3f69d8e7
                      cm 281d5c3e3f69d8e7,os

                      cm octoml@mlops,os
                      cm octoml@mlops,dbfa91645e429380:os,281d5c3e3f69d8e7
                      cm dbfa91645e429380:281d5c3e3f69d8e7

    Returns:
        return (int): return code == 0 if no error 
                                  >0 if error

        (error) (str): error string if return>0

        cm_object (list): first argument: CM alias | UID
                          (second element: 

    """

    str_err='CM object {} is not recognized'
    
    cm_object = []

    split_obj = obj.split(':')

    if len(split_obj) > max_length:
        return {'return':1, 'error':str_err.format(obj)}
    
    for obj in split_obj:
        sub_objects = obj.split(',')

        if len(sub_objects)==0 or len(sub_objects) > 2:
            return {'return':1, 'error':str_err.format(obj)}

        if len(sub_objects)==1:
            if is_cm_uid(sub_objects[0]):
                sub_object = ('',sub_objects[0])
            else:
                sub_object = (sub_objects[0],'')
        elif len(sub_objects)==2:
            if is_cm_uid(sub_objects[1]) or not is_cm_uid(sub_objects[0]):
                sub_object = (sub_objects[0], sub_objects[1])
            elif is_cm_uid(sub_objects[0]) or not is_cm_uid(sub_objects[1]):
                sub_object = (sub_objects[1], sub_objects[0])
            else:
                return {'return':1, 'error':str_err.format(sub_objects)}
        else:
            return {'return':1, 'error':str_err.format(sub_objects)}

        cm_object.insert(0, sub_object)
                
    return {'return':0, 'cm_object':cm_object}


###########################################################################
def match_objects(uid, alias, uid2, alias2):
    """
    Check if 2 CM objects match

    Args:    

          alias can't have wildcards (real CM object)
          alias2 can have wildcards (search)
          
          281d5c3e3f69d8e7,* == 281d5c3e3f69d8e7,*
          281d5c3e3f69d8e7,os == ,os
          ,os == 281d5c3e3f69d8e7,os
          ,* != 281d5c3e3f69d8e7,*

          os
          281d5c3e3f69d8e7
          os,281d5c3e3f69d8e7
          281d5c3e3f69d8e7,os


    Returns:
        return (int): return code == 0 if no error 
                                  >0 if error

        (error) (str): error string if return>0

        match (bool): True if 2 CM objects match (uid and/or alias)

    """

    match = False

    if uid is None: uid = ''
    if alias is None: alias = ''
    if uid2 is None: uid2 = ''
    if alias2 is None: alias2 = ''
    
    # We match first by UID no matter what the alias is (the last one can change)
    if uid!='' and uid2!='':
        if uid==uid2:
            match = True
    else:
        # As soon as one UID is not there, we try to match by alias with wildcards
        # Both aliases must be present otherwise ambiguity - we report is as no match
        object2_has_wildcards = False
        if '*' in alias2 or '?' in alias2:
            object2_has_wildcards = True

        if object2_has_wildcards:
            import fnmatch

            if fnmatch.fnmatch(alias, alias2):
                match = True
        else:
            if alias2=='' or alias.lower()==alias2.lower():
                match = True

    return {'return':0, 'match': match}

###########################################################################
def get_list_from_cli(i, key):
    """
    Get list from a CLI 

    Args:    

    Returns:
        return (int): return code == 0 if no error 
                                  >0 if error

        (error) (str): error string if return>0

        match (bool): True if 2 CM objects match (uid and/or alias)

    """

    tags = i.get(key, [])

    if type(tags)!=list:
        xtags = tags.split(',')

        tags = [t.strip() for t in xtags]

    return tags

###########################################################################
def init_module(CModule, cmind, module_name):
    """
    Initialize module

    Args:    

    Returns:
        return (int): return code == 0 if no error 
                                  >0 if error

        (error) (str): error string if return>0

    """
    

    module = CModule(cmind, module_name)

    module_path = module.path

    # Try to load meta description
    path_module_meta = os.path.join(os.path.dirname(module_path), cmind.cfg['file_cmeta'])

    r = is_file_json_or_yaml(file_name = path_module_meta)
    if r['return']>0: return r

    module.meta = {}

    if r['is_file']:
        # Load artifact class
        r=load_yaml_and_json(path_module_meta)
        if r['return']>0: return r

        module.meta = r['meta']

    return {'return':0, 'module':module}

##############################################################################
def merge_dicts(i):
    """Merge intelligently dict1 with dict2 key by key in contrast with dict1.update(dict2)
       Target audience: end users

       It can merge sub-dictionaries and lists instead of substituting them

    Args:    
              dict1 (dict): merge this dict with dict2 (will be directly modified!)
              dict2 (dict): dict to be merged
              append_lists (str): if 'yes', append lists instead of creating the new ones
              ignore_keys (list): ignore keys

    Returns:
              (dict): Unified CK dictionary:

                return (int): return code =  0, if successful
                                          >  0, if error
                (error) (str): error text if return > 0

                dict1 (dict): dict1 passed through the function

    """

    a = i['dict1']
    b = i['dict2']

    append_lists=i.get('append_lists','')

    ignore_keys = i.get('ignore_keys',[])

    for k in b:
        if k in ignore_keys:
            continue
        v = b[k]
        if type(v) is dict:
            if k not in a:
                a.update({k: b[k]})
            elif type(a[k]) == dict:
                merge_dicts({'dict1': a[k], 'dict2': b[k], 'append_lists':append_lists})
            else:
                a[k] = b[k]
        elif type(v) is list:
            if append_lists!='yes' or k not in a:
               a[k] = []
            for y in v:
                a[k].append(y)
        else:
            a[k] = b[k]

    return {'return': 0, 'dict1': a}

###########################################################################
def process_meta_for_inheritance(i):
    """Process meta for inheritance

    Args:
              artifact (obj): CM artifact
              meta (dict): original meta
              cmind (obj): initialized CM to search for base artifacts
              (base_recursion) (int): track recursion during inheritance

    Returns:
              (dict): Unified CK dictionary:

                return (int): return code =  0, if successful
                                          >  0, if error
                (error) (str): error text if return > 0

                dict (dict):        CK updated meta with inheritance from base entries
                (dict_orig) (dict): original CK meta if CK was updated with a base entry

    """

    automation = i['automation']
    current_meta = i.get('meta',{})
    cmind = i['cmind']
    
    base_entry = current_meta.get('_base_artifact','').strip()

    if base_entry!='':
        base_recursion = int(i.get('base_recursion','0'))

        if base_recursion > 10:
            return {'return':8, 'error':'inheritance recursion is too deep > 10 ({})'.format(i)}
        
        j=base_entry.find('::')
        if j>0:
            automation = base_entry[:j]
            artifact = base_entry[j+2:]
        else:
            artifact = base_entry

        r = cmind.access({'automation':automation,
                          'action':'search',
                          'artifact':artifact,
                          'ignore_inheritance':True,
                          'skip_con':True})
        if r['return']>0: return r

        lst = r['list']

        if len(lst)==0:
            return {'return':1, 'error':'base artifact {} not found in {}'.format(artifact, current_meta['alias']+','+current_meta['uid'])}

        if len(lst)>1:
            return {'return':1, 'error':'more than 1 base artifact {} found in {}'.format(artifact, current_meta['alias']+','+current_meta['uid'])}
        
        base_artifact = lst[0]

        # Load with meta and recursive inheritance
        r = base_artifact.load(base_recursion = base_recursion + 1)
        if r['return']>0: return r
            
        base_meta = base_artifact.meta

        r = merge_dicts({'dict1': base_meta, 
                         'dict2': current_meta})
        if r['return']>0: return r

        current_meta = base_meta

    return {'return':0, 'meta':current_meta}
