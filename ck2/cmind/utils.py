# Auxilary functions for CM

# Some functionality was reused from the CK framework for compatibility

import os

ERROR_UNKNOWN_FILE_EXTENSION = 1
ERROR_PATH_NOT_FOUND = 2
ERROR_FILE_NOT_FOUND = 16

###########################################################################
def load_yaml_and_json(file_name_without_ext, check_if_exists = False, encoding = 'utf8'):

    """
    Load YAML file if exists then JSON file if exists and merge with the first one

    Args:    
       (CM input dict):

       file_name_without_ext (str): file name without extension (to check yaml and then json)
       (check_if_exists) (bool): if True, fail if doesn't exist
       (encoding) (str): file encoding ('utf8' by default)

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

       * meta (dict): merged meta of found file(s)

    """

    meta = {}

    not_found = True
    
    for file_ext in [('.yaml', load_yaml), 
                     ('.json', load_json)]:
        file_name = file_name_without_ext + file_ext[0]

        r = file_ext[1](file_name, check_if_exists = True, encoding = encoding) # To avoid failing if doesn't exist
        if r['return'] != ERROR_FILE_NOT_FOUND:
            not_found = False
            if r['return'] > 0: return r

        meta.update(r.get('meta', {}))

    # If none is found
    if not_found:
        return {'return':ERROR_FILE_NOT_FOUND, 'error': 'YAML and JSON file {} not found'.format(file_name_without_ext)}

    return {'return':0, 'meta':meta}

###########################################################################
def is_file_json_or_yaml(file_name):

    """
    Is file JSON or YAML?

    Args:    
       (CM input dict):

       file_name (str): path to file without extension

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

       * is_file (bool): if True, there is a file with YAML and/or JSON extension

    """

    for file_ext in ['.yaml', '.json']:
        file_path = file_name + file_ext

        if os.path.isfile(file_path):
            return {'return':0, 'is_file':True, 'path':file_path}

    return {'return':0, 'is_file':False}

###########################################################################
def load_json_or_yaml(file_name, check_if_exists = False, encoding = 'utf8'):
    """
    Attempt to load file as JSON or YAML.

    Args:    
       (CM input dict):

       file_name (str): file name that has either JSON or YAML extension
       (check_if_exists) (bool): if True, fail if doesn't exist
       (encoding) (str): file encoding ('utf8' by default)

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

       * meta (dict): merged meta of found file(s)

    """

    if file_name.endswith('.json'):
        return load_json(file_name, check_if_exists = check_if_exists, encoding = encoding)
    elif file_name.endswith('.yaml'):
        return load_yaml(file_name, check_if_exists = check_if_exists, encoding = encoding)

    return {'return':ERROR_UNKNOWN_FILE_EXTENSION, 'error':'file extension must be .json or .yaml in {}'.format(file_name)}

###########################################################################
def save_json_or_yaml(file_name, meta, sort_keys=False, encoding = 'utf8'):
    """
    Save meta to either JSON or YAML file.

    Args:    
       (CM input dict):

       file_name (str): file name that has either JSON or YAML extension
       meta (dict): meta to save
       (sort_keys) (bool): if True, sort keys
       (encoding) (str): file encoding ('utf8' by default)

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

    """

    if file_name.endswith('.json'):
        return save_json(file_name, meta, sort_keys, encoding = encoding)
    elif file_name.endswith('.yaml'):
        return save_yaml(file_name, meta, sort_keys, encoding = encoding)

    return {'return':ERROR_UNKNOWN_FILE_EXTENSION, 'error':'unknown file extension'}

###########################################################################
def load_json(file_name, check_if_exists = False, encoding='utf8'):
    """
    Load JSON file.

    Args:    
       (CM input dict):

       file_name (str): file name
       (check_if_exists) (bool): if True, fail if doesn't exist
       (encoding) (str): file encoding ('utf8' by default)

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

       * meta (dict): meta from the file

    """

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
    """
    Save meta to JSON file.

    Args:    
       (CM input dict):

       file_name (str): file name 
       meta (dict): meta to save
       (indent) (int): 2 by default
       (sort_keys) (bool): if True, sort keys
       (encoding) (str): file encoding ('utf8' by default)

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

    """

    import json

    with open(file_name, 'w', encoding = encoding) as jf:
        jf.write(json.dumps(meta, indent=indent, sort_keys=sort_keys)+'\n')

    return {'return':0}

###########################################################################
def load_yaml(file_name, check_if_exists = False, encoding = 'utf8'):
    """
    Load YAML file.

    Args:    
       (CM input dict):

       file_name (str): file name
       (check_if_exists) (bool): if True, fail if doesn't exist
       (encoding) (str): file encoding ('utf8' by default)

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

       * meta (dict): meta from the file

    """

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
def load_txt(file_name, encoding = 'utf8', remove_after_read = False, 
             check_if_exists = False, split = False,
             match_text = '', fail_if_no_match = ''):
    """
    Load text file.

    Args:    
       (CM input dict):

       file_name (str): file name 
       (encoding) (str): file encoding ('utf8' by default)
       (remove_after_read) (bool): if True, remove file after read (False by default)
       (check_if_exists) (bool): If True, check if file exists and return CM error instead of raising error (False by default)
       (split) (bool): If True, split string into list (False by default)
       (match_text) (str): Regular expression to match text (useful for version detection)

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

       * string (str): string from file

    """

    if check_if_exists and not os.path.isfile(file_name):
        return {'return':16, 'error':'{} was not found'.format(file_name)}
    
    with open(file_name, 'rt', encoding = encoding) as tf:
        s = tf.read()

    if remove_after_read:
        os.remove(file_name)

    rr = {'return':0,
          'string':s}

    if split:
        rr['list'] = s.split('\n')

    if match_text != '':
        import re
        match = re.search(match_text, s)

        if fail_if_no_match!='' and match is None:
            return {'return':1, 'error': fail_if_no_match}
        
        rr['match'] = match

    return rr

###########################################################################
def load_bin(file_name):
    """
    Load binary file.

    Args:    
       (CM input dict):

       file_name (str): file name 

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

       * bin (bytes): file content

    """

    with open(file_name, 'rb') as bf:
        b = bf.read()

    return {'return':0,
            'bin': b}

###########################################################################
def save_yaml(file_name, meta={}, sort_keys=True, encoding = 'utf8'):
    """
    Save meta to YAML file.

    Args:    
       (CM input dict):

       file_name (str): file name 
       meta (dict): meta to save
       (sort_keys) (bool): if True, sort keys
       (encoding) (str): file encoding ('utf8' by default)

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

    """

    import yaml

    with open(file_name, 'w', encoding = encoding) as yf:
        meta = yaml.dump(meta, yf)

    return {'return':0}

###########################################################################
def save_txt(file_name, string = '', encoding = 'utf8'):
    """
    Save string to text file.

    Args:    
       (CM input dict):

       file_name (str): file name 
       string (str): string to save
       (encoding) (str): file encoding ('utf8' by default)

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

    """

    with open(file_name, 'wt', encoding = encoding) as tf:
        tf.write(string)

    return {'return':0}

###########################################################################
def check_and_create_dir(path):
    """
    Create directories if path doesn't exist.
    (from the CK framework).

    Args:
       path (str): path

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

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
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

       * path (str): path where file is found
       * path_to_file (str): path to file

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
    """
    List all files recursively in a given directory.
    (from the CK framework).

    Args:    
       (CM input dict):

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
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

       * list (dict): dictionary of all files:
                      {"file_with_full_path":{"size":.., "path":..}

       * number (int): (internal) total number of files in a current directory (needed for recursion)

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
    Generate CM UID.

    Args:    
        None

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

       * uid (str): CM UID

    """

    import uuid

    return {'return':0,
            'uid':uuid.uuid4().hex[:16]}

###########################################################################
def is_cm_uid(obj):
    """
    Check if a string is a valid CM UID.

    Args:    
       obj (str): CM alias or UID

    Returns:
       (bool): True if valid CM UID 16 hex characters

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
    Parse CM object in string and return tuple of CM objects.

    Examples:
        CM sub-object = UID | alias | alias,UID | UID,alias

        repo CM sub-object | CM sub-object

        cm os

        cm 281d5c3e3f69d8e7

        cm os,281d5c3e3f69d8e7

        cm 281d5c3e3f69d8e7,os

        cm octoml@mlops,os

        cm octoml@mlops,dbfa91645e429380:os,281d5c3e3f69d8e7

        cm dbfa91645e429380:281d5c3e3f69d8e7


    Args:    
        obj (str): CM object
        (max_length) (int): 

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

       * cm_object (list): first element: CM alias | UID
                           (second element: CM repo | UID)

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
def match_objects(uid, alias, uid2, alias2, more_strict = False):
    """
    Check if 2 CM objects match. 
    Used to search CM artifacts in CM repositories.

    Examples:
            281d5c3e3f69d8e7,* == 281d5c3e3f69d8e7,*

            281d5c3e3f69d8e7,os == ,os

            ,os == 281d5c3e3f69d8e7,os

            ,* != 281d5c3e3f69d8e7,*

            os

            281d5c3e3f69d8e7

            os,281d5c3e3f69d8e7

            281d5c3e3f69d8e7,os

    Args:
       uid (str): artifact UID
       alias (str): atifact alias that can't have wildcards [real CM object]

       uid2 (str): atifact 2 UID
       alias2 (str) artifact 2 alias that can have wildcards [search]

      (more_strict) (bool): if True, then ,os != 281d5c3e3f69d8e7, [needed to check automation]


    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

       * match (bool): True if 2 CM objects match (uid and/or alias)

    """

    match = False

    if uid is None: uid = ''
    if alias is None: alias = ''
    if uid2 is None: uid2 = ''
    if alias2 is None: alias2 = ''

    uid = uid.lower()
    uid2 = uid2.lower()

    # We match first by UID no matter what the alias is (the last one can change)
    if uid!='' and uid2!='':
        if uid==uid2:
            match = True
    elif more_strict and uid=='' and uid2!='' and alias2=='':
        # Not match
        pass
    else:
        # As soon as one UID is not there, we try to match by alias with wildcards
        # Both aliases must be present otherwise ambiguity - we report is as no match
        object2_has_wildcards = True if ('*' in alias2 or '?' in alias2) else False

        alias = alias.lower()
        alias2 = alias2.lower()

        if object2_has_wildcards:
            import fnmatch

            if fnmatch.fnmatch(alias, alias2):
                match = True
        else:
            if alias2=='' or alias==alias2:
                match = True

    return {'return':0, 'match': match}

###########################################################################
def get_list_from_cli(i, key):
    """
    Get list from CM command line.

    Args:    
       i (dict): CM input dict
       key (str): key to get

    Returns:
       tags (list): list of tags for a given key

    """

    tags = i.get(key, [])

    if type(tags)!=list:
        xtags = tags.split(',')

        tags = [t.strip() for t in xtags]

    return tags

##############################################################################
def merge_dicts(i):
    """
    Merge intelligently dict1 with dict2 key by key in contrast with dict1.update(dict2)

    It can merge sub-dictionaries and lists instead of substituting them

    Args:    
       (CM input dict): 

       dict1 (dict): merge this dict with dict2 (will be directly modified!)
       dict2 (dict): dict to be merged
       (append_lists) (bool): if True, append lists instead of creating the new ones
       (append_unique) (bool): if True, append lists when value doesn't exists in the original one
       (ignore_keys) (list): ignore keys

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

       * dict1 (dict): dict1 passed through the function

    """

    a = i['dict1']
    b = i['dict2']

    append_lists = i.get('append_lists', False)
    append_unique = i.get('append_unique', False)

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
            if not append_lists or k not in a:
               a[k] = []
            for y in v:
                if append_unique:
                    if y not in a[k]:
                        a[k].append(y)
                else:
                    a[k].append(y)
        else:
            a[k] = b[k]

    return {'return': 0, 'dict1': a}

###########################################################################
def process_meta_for_inheritance(i):
    """
    Check CM meta description for inheritance and update it if needed ("_base":"automation::artifact").

    Args:
       (CM input dict): 

       automation (str): CM automation
       meta (dict): original meta
       cmind (obj): initialized CM to search for base artifacts
       (base_recursion) (int): track recursion during inheritance

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

       * meta (dict): final meta description wihhout _base

    """

    automation = i['automation']
    current_meta = i.get('meta',{})
    cmind = i['cmind']

    base_entry = current_meta.get('_base','').strip()

    if base_entry!='':
        del (current_meta['_base'])

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
                          'ignore_inheritance':True})
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
                         'dict2': current_meta,
                         'append_lists': True})
        if r['return']>0: return r

        current_meta = r['dict1']

    return {'return':0, 'meta':current_meta}


###########################################################################
def find_api(file_name, func):
    """
    Find automation action API in a Python module

    Args:
       file_name (str): Python module
       func (str): automation action name

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

       * api (str): API
    """

    # Load file
    r = load_txt(file_name)
    if r['return'] >0: return r

    string = r['string']

    api = ''

    # Search for def
    search = 'def '+func+'('
    j = string.find(search)
    if j<0:
        return {'return':16, 'error':'API not found'}

    line1 = string.rfind('\n', 0, j)

    line_comment1 = string.find('"""', j)
    if line_comment1 <0 :
        return {'return':1, 'error':'API not found'}

    line_comment2 = string.find('"""', line_comment1 + 2)
    if line_comment2 <0 :
        return {'return':1, 'error':'API not found'}

    api = string[line1+1:line_comment2+3]

    return {'return':0, 'api':api}


###########################################################################
def find_file_in_current_directory_or_above(file_names, path_to_start = None, reverse = False):
    """
    Find file(s) in the current directory or above.

    Args:
       file_names (list): files to find
       (path_to_start) (str): path to start; use current directory if None
       (reverse) (bool): if True search recursively in current directory and below.

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

       * found (bool): True if found

       * path_to_file (str): full path to found file
       * path (str): path where found file is

    """

    if path_to_start is None:
        path_to_start=os.getcwd()

    found = False

    current_path = path_to_start

    # Only makes sense if found
    found_in_current_path = True

    # Go backwards to find cmr.yaml or cmr.json (CM repo description)
    while True:
       for file_name in file_names:
           path_to_file = os.path.join(current_path, file_name)

           if os.path.isfile(path_to_file):
               found = True
               break

       if found:
           break

       if reverse:
          # Get first directory
          dirs = os.listdir(current_path)

          new_path = ''

          for d in dirs:
              if not d.startswith('.'):
                  test_dir = os.path.join(current_path, d)
                  if os.path.isdir(test_dir):
                      new_path = test_dir
                      break

          if new_path == '':
              break        

       else:
          new_path = os.path.dirname(current_path)

          if new_path == current_path:
              break

       found_in_current_path = False

       current_path = new_path

    r = {'return':0, 'found': found}

    if found:
        r['path_to_file'] = path_to_file
        r['path'] = os.path.dirname(path_to_file)

        r['found_in_current_path'] = found_in_current_path

    return r

###########################################################################
def assemble_cm_object(alias,uid):
    """
    Assemble CM object string from alias and uid strings

    Args:    
       alias (str): CM artifact alias
       uid (str): CM artifact UID

    Returns: 
       (str) CM object (alias,uid)
    """

    if alias == None: alias = ''
    if uid == None: uid = ''

    cm_obj = ''

    if uid != '':
       cm_obj = uid

    if alias != '':
       if cm_obj !='':
           cm_obj = alias + ',' + cm_obj
       else:
           cm_obj = alias

    return cm_obj

###########################################################################
def assemble_cm_object1(cm_dict):
    """
    Assemble CM object string from dictionary with 'alias' and 'uid' keys

    Args:    
       cm_dict (dict): dictionary with CM artifact keys ('alias', 'uid')

    Returns: 
       (str) CM object (alias,uid)

    """

    return assemble_cm_object(cm_dict['alias'],cm_dict['uid'])

###########################################################################
def assemble_cm_object2(cm_obj):
    """
    Assemble CM object string from tuple

    Args:    
       cm_obj (tuple): CM object tuple (alias, uid)

    Returns: 
       (str) CM object (alias,uid)

    """

    return assemble_cm_object(cm_obj[0], cm_obj[1])

###########################################################################
def dump_safe_json(i):
    """
    Dump safe JSON

    Args:    
       (CM input dict): input to dump to console

    Returns: 
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

       * meta (dict): only "safe" values left (that can be serialized)

    """

    import json

    meta = {}

    for k in i:
        v = i[k]

        try:
           s = json.dumps(v)
        except Exception as e:
           pass
        else:
           meta[k] = v

    print (json.dumps(meta, indent=2, sort_keys=True, ensure_ascii=False))

    return {'return':0, 'meta': meta}

###########################################################################
def convert_tags_to_list(i):
    """
    Convert string tags to list

    Args:    
       (CM input dict): 

       (tags) (str) - string of tags separated by comma

    Returns: 
       tags_list (list): list of tags

    """

    tags = i.get('tags')
    if tags == None: tags=''

    tags = tags.strip()

    tags_list = []

    if tags!='': 
       tags_list_tmp = tags.split(',')

       for tag in tags_list_tmp:
           tag = tag.strip()

           if tag not in tags_list:
               tags_list.append(tag)

    return tags_list

##############################################################################
def get_current_date_time(i):
    """
    Get current date and time.

    Args:    
       (CM input dict): empty dict

    Returns: 
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

       * array (dict); dict with date and time

           - date_year (str)
           - date_month (str)
           - date_day (str)
           - time_hour (str)
           - time_minute (str)
           - time_second (str)

       * iso_datetime (str): date and time in ISO format
    """

    import datetime

    a = {}

    now1 = datetime.datetime.now()
    now = now1.timetuple()

    a['date_year'] = now[0]
    a['date_month'] = now[1]
    a['date_day'] = now[2]
    a['time_hour'] = now[3]
    a['time_minute'] = now[4]
    a['time_second'] = now[5]

    return {'return': 0, 'array': a, 'iso_datetime': now1.isoformat()}

##############################################################################
def gen_tmp_file(i):
    """
    Generate temporary files

    Args:    
       (CM input dict):

              (suffix) (str): temp file suffix
              (prefix) (str): temp file prefix
              (remove_dir) (bool): if True, remove dir

    Returns: 
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

       * file_name (str): temp file name 
    """

    xs = i.get('suffix', '')
    xp = i.get('prefix', '')
    s = i.get('string', '')

    import tempfile

    fd, fn = tempfile.mkstemp(suffix=xs, prefix=xp)
    os.close(fd)
    os.remove(fn)

    if i.get('remove_dir', False):
        fn = os.path.basename(fn)

    return {'return': 0, 'file_name': fn}

##############################################################################
def load_python_module(i):
    """
    Load python module

    Args:
       (CM input dict):

              path (str): path to a python module
              name (str): Python module name (without .py)

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

       * 

    """

    import imp

    path = i['path']
    name = i['name']

    # Find module
    try:
        found_module = imp.find_module(name, [path])
    except ImportError as e:  # pragma: no cover
        return {'return': 1, 'error': 'can\'t find module code (path={}, name={}, error={})'.format(path,name,format(e))}

    full_name = found_module[0]
    full_path = found_module[1]

    # Generate uid for the run-time extension of the loaded module
    # otherwise modules with the same extension (key.py for example)
    # will be reloaded ...

    r = gen_uid()
    if r['return'] > 0: return r

    code_uid = 'rt-'+r['uid']

    try:
        code = imp.load_module(code_uid, full_name, full_path, found_module[2])
    except ImportError as e:
        return {'return': 2, 'error': 'can\'t find module code (path={}, name={}, error={})'.format(path,name,format(e))}

    found_module[0].close()

    return {'return':0, 'code': code, 'path': full_path, 'code_uid':code_uid}

##############################################################################
def update_dict_if_empty(d, key, value):
    """
    Update dictionary if "key" is empty

    Args:
       d (dict): dict to check
       key (str); key in dict
       value: if d[key] is empty, set to this value

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

    """

    if d.get(key)==None or d.get(key)=='':
        d[key] = value

    return {'return':0}

##############################################################################
def sub_input(i, keys, reverse = False):
    """
    Create sub-input from the input using list of keys

    Args:
       i (dict): input
       keys (list); keys to check and add if reverse is False
                    keys not to add if reverse if True
       reverse (bool): either add or skip keys

    Returns:
       (dict): sub-input

    """

    ii={}

    if reverse:
        for k in i:
            if k not in keys:
                ii[k]=i[k]
    else:
        for k in keys:
            if k in i:
                ii[k]=i[k]

    return ii

##############################################################################
def convert_env_to_dict(s):
    """
    Create sub-input from the input using list of keys

    Args:
       s (str): string with env

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

       (dict): dictionary

    """

    env = s.split('\n')

    d = {}

    for e in env:
        e = e.strip()

        if e!='':
            process = e.split('=')

            if len(process)>0:
                k = process[0].strip()
                v = ''

                if len(process)>1:
                    v = process[1].strip()

                d[k]=v

    return {'return':0, 'dict':d}
