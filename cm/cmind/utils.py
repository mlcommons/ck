# Auxilary functions for CM
#
# Some functionality was reused from the CK framework for compatibility
#
# Author(s): Grigori Fursin
# Contributor(s):
#
# Copyright: https://github.com/mlcommons/ck/blob/master/COPYRIGHT.txt
# License: https://github.com/mlcommons/ck/blob/master/LICENSE.md
# History: https://github.com/mlcommons/ck/blob/master/HISTORY.CM.md
# White paper: https://arxiv.org/abs/2406.16791
# Project contributors: https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md

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
def safe_load_json(path, file_name='', encoding='utf8'):
    """
    Load JSON file if exists, otherwise return empty dict

    Args:    
       (CM input dict):

       file_name (str): file name
       (encoding) (str): file encoding ('utf8' by default)

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

       * meta (dict): meta from the file

    """

    path_to_file = os.path.join(path, file_name) if file_name == '' or path != file_name else path

    meta = {}

    r = load_json(path_to_file, check_if_exists=True, encoding=encoding)
    if r['return'] == 0:
        meta = r['meta']

    return {'return':0, 'meta': meta}

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
        try:
            meta = json.load(jf)
        except Exception as e:
            return {'return':4, 'error': f'detected problem in {file_name}: {e}'}

    return {'return':0, 'meta': meta}

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

    with open(file_name, 'w', encoding = encoding, newline='\n') as jf:
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
        try:
            if int(yaml.__version__[0])>=5:
                meta = yaml.load(yf, Loader=yaml.FullLoader)
            else:
                # To support old versions
                meta = yaml.safe_load(yf)
        except Exception as e:
            return {'return':4, 'error': f'detected problem in {file_name}: {e}'}

    return {'return':0,
            'meta': meta}


###########################################################################
def load_txt(file_name, encoding = 'utf8', remove_after_read = False, 
             check_if_exists = False, split = False,
             match_text = '', fail_if_no_match = '', debug = False):
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

        if debug:
            print (match)

        if fail_if_no_match!='' and match is None:
            return {'return':1, 'error': fail_if_no_match, 'string':s}

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

    with open(file_name, 'w', encoding = encoding, newline='\n') as yf:
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

    with open(file_name, 'wt', encoding = encoding, newline='\n') as tf:
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
            if iall == 'yes':
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
def parse_cm_object(obj, max_length = 2, decompose = False):
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

    rr = {'return':0, 'cm_object':cm_object}

    if decompose:
        rr['decomposed_object'] = decompose_cm_obj(cm_object)

    return rr

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

    if a != b:
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
def find_file_in_current_directory_or_above(file_names, path_to_start = None, 
        reverse = False, path_to_stop = None):
    """
    Find file(s) in the current directory or above.

    Args:
       file_names (list): files to find
       (path_to_start) (str): path to start; use current directory if None
       (reverse) (bool): if True search recursively in current directory and below.
       (path_to_stop) (str): path to stop search (usually path to found repo)

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

          if path_to_stop != None and new_path == path_to_stop:
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
def process_input(i, update_input = True):
    """
    Process automation, artifact and artifacts from i['control']

    Args:    
       control['_unparsed_automation']
       control['_unparsed_artifact']
       control['_unparsed_artifacts']

    Returns: 
       TBD

    """

    control = i['control']

    for k in ['_parsed_automation', '_parsed_artifact']:
        if k in control:
            x = decompose_cm_obj(control[k])
            control[k[7:]] = x
            del(control[k])

    if '_parsed_artifacts' in control:
        control['_artifacts'] = []
        for artifact in control['_parsed_artifacts']:
            x = decompose_cm_obj(artifact)
            control['_artifacts'].append(x)
        del(control['_parsed_artifacts'])

    if update_input:
        for k in ['_automation', '_artifact']:
            if k in control:
                i[k[1:]] = control[k]['artifact']

        artifacts = control.get('_artifacts', [])

        if len(artifacts)>0:
            i['artifacts'] = []
            for a in artifacts:
                i['artifacts'].append(a['artifact'])

    return {'return':0}

###########################################################################
def decompose_cm_obj(cm_obj):
    """
    Decompose CM object into dictionary

    Args:    
      cm_obj (CM object)

    Returns: 
       (dict)
         artifact (str)
         name (str)
         name_alias (str)
         name_uid (str)
         repo (str)
         repo_alias (str)
         repo_uid (str)

    """
    cm_artifact = ''
    cm_artifact_name = ''
    cm_artifact_name_alias = ''
    cm_artifact_name_uid = ''
    cm_artifact_repo = ''
    cm_artifact_repo_alias = ''
    cm_artifact_repo_uid = ''

    if len(cm_obj)>0:
        cm_obj_artifact = cm_obj.pop(0)

        cm_artifact_alias = cm_obj_artifact[0]
        cm_artifact_uid = cm_obj_artifact[1]

        cm_artifact_name = assemble_cm_object(cm_artifact_alias, cm_artifact_uid)

        cm_artifact = cm_artifact_name

    if len(cm_obj)>0:
        cm_obj_repo = cm_obj.pop(0)

        cm_artifact_repo_alias = cm_obj_repo[0]
        cm_artifact_repo_uid = cm_obj_repo[1]

        cm_artifact_repo = assemble_cm_object(cm_artifact_repo_alias, cm_artifact_repo_uid)

        cm_artifact = cm_artifact_repo + ':' + cm_artifact

    return {'artifact':cm_artifact, 
            'name': cm_artifact_name,
            'name_alias': cm_artifact_alias,
            'name_uid': cm_artifact_uid, 
            'repo': cm_artifact_repo,
            'repo_alias': cm_artifact_repo_alias,
            'repo_uid': cm_artifact_repo_uid}

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
       (CM input dict): 
         - (timezone) (str): timezone in pytz format: "Europe/Paris"

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

    tz = None

    tz_str = i.get('timezone', '').strip()
    if tz_str != '':
        import pytz
        tz = pytz.timezone(tz_str)

    now1 = datetime.datetime.now(tz)
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

#    Outdated in Python 3.12+
#    import imp

    import importlib

    path = i['path']
    name = i['name']

    full_path = os.path.join(path, name + '.py')

    if not os.path.isfile(full_path):
        return {'return': 1, 'error': 'can\'t find Python module file {}'.format(full_path)}
    
#    # Find module
#    try:
#        found_module = imp.find_module(name, [path])
#    except ImportError as e:  # pragma: no cover
#        return {'return': 1, 'error': 'can\'t find module code (path={}, name={}, error={})'.format(path,name,format(e))}
#
#    full_name = found_module[0]
#    full_path = found_module[1]
#
#    # Generate uid for the run-time extension of the loaded module
#    # otherwise modules with the same extension (key.py for example)
#    # will be reloaded ...
#
#    r = gen_uid()
#    if r['return'] > 0: return r
#
#    code_uid = 'rt-'+r['uid']
#
#    try:
#        code = imp.load_module(code_uid, full_name, full_path, found_module[2])
#    except ImportError as e:
#        return {'return': 2, 'error': 'can\'t find module code (path={}, name={}, error={})'.format(path,name,format(e))}
#
#    found_module[0].close()



    found_spec = importlib.util.spec_from_file_location(name, full_path)
    if found_spec == None:
        return {'return': 1, 'error': 'can\'t find Python module file {}'.format(full_path)}

    try:
        loaded_code = importlib.util.module_from_spec(found_spec)
        found_spec.loader.exec_module(loaded_code)
    except Exception as e:  # pragma: no cover
        return {'return': 1, 'error': 'can\'t load Python module code (path={}, name={}, err={})'.format(path, name, format(e))}


#    return {'return':0, 'code': code, 'path': full_path, 'code_uid':code_uid}
    return {'return':0, 'code': loaded_code, 'path': full_path, 'code_uid':''}

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

###########################################################################
def filter_tags(tags):
    """
    Filter tags (remove starting with -)

    Args:    
       tags (list): list of tags

    Returns: 
       (list) list of filtered tags
    """

    filtered_tags = [t for t in tags if not t.startswith('-')]

    return filtered_tags

##############################################################################
def copy_to_clipboard(i):
    """
    Copy string to a clipboard

    Args:    

       string (str): string to copy to a clipboard
       (add_quotes) (bool): add quotes to the string in a clipboard
       (skip_fail) (bool): if True, do not fail

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0
    """

    s = i.get('string','')

    if i.get('add_quotes',False): s='"'+s+'"'

    failed = False
    warning = ''

    # Try to load pyperclip (seems to work fine on Windows)
    try:
        import pyperclip
    except Exception as e:
        warning = format(e)
        failed = True
        pass

    if not failed:
        pyperclip.copy(s)
    else:
        failed = False

        # Try to load Tkinter
        try:
            from Tkinter import Tk
        except ImportError as e:
            warning = format(e)
            failed = True
            pass

        if failed:
            failed = False
            try:
                from tkinter import Tk
            except ImportError as e:
                warning = format(e)
                failed = True
                pass

        if not failed:
            # Copy to clipboard
            try:
                r = Tk()
                r.withdraw()
                r.clipboard_clear()
                r.clipboard_append(s)
                r.update()
                r.destroy()
            except Exception as e:
                failed = True
                warning = format(e)

    rr = {'return':0}
    
    if failed:
        if not i.get('skip_fail',False):
            return {'return':1, 'error':warning}

        rr['warning']=warning 
    
    return rr

###########################################################################
def update_yaml(file_name, meta = {}, encoding = 'utf8'):
    """
    Update yaml file directly (unsafe - only first keys)

    Args:    
       (CM input dict):

         file_name (str): YAML file name 
         meta (dict): keys to update
         (encoding) (str): file encoding ('utf8' by default)

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

    """

    r = load_txt(file_name, encoding=encoding, split=True)
    if r['return']>0: return r

    yaml = r['list']

    for k in meta:
        # only simple string is supported
        v = str(meta[k])

        for j in range(0, len(yaml)):
            s = yaml[j]

            if s.startswith(k+':'):
                yaml[j]=k+': '+v

    r = save_txt(file_name, string = '\n'.join(yaml), encoding=encoding)
    if r['return']>0: return r

    return {'return':0}

###########################################################################
def call_internal_module(module_self, path_to_current_module, module_name, module_func, i):
    """
    Call CM function from internal submodule

    Args:    
        path_to_current_module (obj): must be __file__
        module_name (str): module name
        module_func (str): module function
        i (dict): CM input. Note that i['self_module'] = self from calling module will be added to the input

    Returns:
       (CM return dict):

       * return (int): return code == 0 if no error and >0 if error
       * (error) (str): error string if return>0

    """

    import sys
    import importlib

    sys.path.insert(0, os.path.dirname(os.path.abspath(path_to_current_module)))

    tmp_module=importlib.import_module(module_name)

    del(sys.path[0])

    if module_self!=None:
        i['self_module'] = module_self
    
    return getattr(tmp_module, module_func)(i)

###########################################################################
def tags_matched(tags, and_tags, no_tags):
    """
    Check if AND tags and NO tags match tags

    Args:    
        tags (list of str): full list of tags
        and_tags (list of str): list of AND tags
        no_tags (list of str): list of NO tags

    Returns:
        True if tags matched

    """

    matched = True
    
    if len(and_tags)>0:
        if not all(t in tags for t in and_tags):
            matched = False

    if matched and len(no_tags)>0:
        for t in no_tags:
            if t in tags:
                matched = False
                break

    return matched

##############################################################################
def rm_read_only(f, p, e):
    """
    Internal aux function to remove files and dirs even if read only
    particularly on Windows
    """

    import os
    import stat
    import errno

    ex = e[1]

    os.chmod(p, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
    f(p)

    return

##############################################################################
def debug_here(module_path, host='localhost', port=5678, text='', env={}, env_debug_uid=''):
    import os

    if env_debug_uid!='':
        if len(env)==0:
            env = os.environ
        x = env.get('CM_TMP_DEBUG_UID', '').strip()
        if x.lower() != env_debug_uid.lower():
            class dummy:
               def breakpoint(self):
                   return

            return dummy()

    workplace = os.path.dirname(module_path)

    print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print ('Adding remote debug breakpoint ...')
    if text != '':
        print (text)

    print ('')
    import debugpy
    debugpy.listen(port)

    print ('')
    print ('Waiting for debugger to attach ...')
    print ('')
    print ('Further actions for Visual Studio Code:')
    print ('  Open Python file in VS to set breakpoint: {}'.format(module_path))
    print ('  File -> Add Folder to Workplace: {}'.format(workplace))
    print ('  Run -> Add configuration -> Python Debugger -> Remote attach -> {} -> {}'.format(host, port))
    print ('     Сhange "remoteRoot" to ${workspaceFolder}')
    print ('  Set breakpoint ...')
    print ('  Run -> Start Debugging (or press F5) ...')
    print ('')

    debugpy.wait_for_client()

    # Go up outside this function to continue debugging (F11 in VS)
    return debugpy

##############################################################################
def compare_versions(version1, version2):
    """
    Compare versions

    Args:    

       version1 (str): version 1
       version2 (str): version 2

    Returns:
       comparison (int):  1 - version 1 > version 2
                          0 - version 1 == version 2
                         -1 - version 1 < version 2
    """

    l_version1 = version1.split('.')
    l_version2 = version2.split('.')

    # 3.9.6 vs 3.9
    # 3.9 vs 3.9.6

    i_version1 = [int(v) if v.isdigit() else v for v in l_version1]
    i_version2 = [int(v) if v.isdigit() else v for v in l_version2]

    comparison = 0

    for index in range(max(len(i_version1), len(i_version2))):
        v1 = i_version1[index] if index < len(i_version1) else 0
        v2 = i_version2[index] if index < len(i_version2) else 0

        if v1 > v2:
            comparison = 1
            break
        elif v1 < v2:
            comparison = -1
            break

    return comparison

##############################################################################
def check_if_true_yes_on(env, key):
    """
    Universal check if str(env.get(key, '')).lower() in ['true', 'yes', 'on']:

    Args:    

       env (dict): dictionary
       key (str): key

    Returns:
       True if str(env.get(key, '')).lower() in ['true', 'yes', 'on']:
    """

    return str(env.get(key, '')).lower() in ['true', 'yes', 'on']

##############################################################################
def check_if_none_false_no_off(env, key):
    """
    Universal check if str(env.get(key, '')).lower() in ['false', 'no', 'off']:

    Args:    

       env (dict): dictionary
       key (str): key

    Returns:
       True if str(env.get(key, '')).lower() in ['false', 'no', 'off']:
    """

    return str(env.get(key, '')).lower() in ['none', 'false', 'no', 'off']

##############################################################################
def convert_dictionary(d, key, sub = True):
    """
    Grigori added to gradually clean up very complex "cm docker scrpit" implementation

    Convert dictionary into flat dictionary with key prefix

    Example input:
      d = {'cfg':True, 'no-cache':True}
      key = 'docker'
      sub = True
    Example output:
      d = {'docker_cfg': True, 'docker_no_cache': True}

    Args:    

       d (dict): dictionary
       key (str): key

    Returns:
       True if str(env.get(key, '')).lower() in ['false', 'no', 'off']:
    """

    dd = {}

    for k in d:
        kk = k.replace('-', '_') if sub else k

        dd[key + '_' + kk] = d[k]

    return dd

##############################################################################
def test_input(i):
    """
    Test if input has keys and report them as error
    """

    r = {'return':0}

    if len(i)>0:
        unknown_keys = list(i.keys())
        unknown_keys_str = ', '.join(unknown_keys)

        x = '' if len(unknown_keys) == 1 else 's'

        r =  {'return': 1, 
              'error': f'unknown input key{x}: {unknown_keys_str}',
              'unknown_keys': unknown_keys,
              'unknown_keys_str': unknown_keys_str}

    return r

##############################################################################
def path2(path):
    """
    Add quotes if spaces in path
    """
    new_path = f'"{path}"' if not path.startswith('"') and ' ' in path else path

    return new_path

##############################################################################
def update_dict_with_flat_key(key, value, d):
    """
    Update dictionary via flat key (x.y.z)
    """

    if '.' in key:
       keys = key.split('.')

       new_d = d

       first = True

       for key in keys[:-1]:
           if first:
               first = False

           if key not in new_d:
              new_d[key] = {}

           new_d = new_d[key]

       new_d[keys[-1]] = value
    else:
       d[key] = value

    return {'return':0}

##############################################################################
def get_value_from_dict_with_flat_key(key, d):
    """
    Get value from dict via flat key (x.y.z)
    """

    if '.' in key:
       keys = key.split('.')
       new_d = d
       for key in keys[:-1]:
           if key in new_d:
              new_d = new_d[key]
       value = new_d.get(keys[-1])
    else:
       value = d.get(key)

    return value

##############################################################################
def load_module(cmind, task_path, sub_module_name):
    """
    Universal python module loaders
    """

    import importlib

    sub_module_obj = None

    sub_module_path = os.path.join(task_path, sub_module_name)
    if os.path.isfile(sub_module_path):
        sub_module_spec = importlib.util.spec_from_file_location(sub_module_name, sub_module_path)
        if sub_module_spec == None:
            return cmind.prepare_error(1, f"Can\'t load Python module file spec {sub_module_path}")

        try:
           sub_module_obj = importlib.util.module_from_spec(sub_module_spec)
           sub_module_spec.loader.exec_module(sub_module_obj)
        except Exception as e:  # pragma: no cover
           return cmind.prepare_error(1, f"Can\'t load Python module code {sub_module_path}:\n\n{e}")

    return {'return':0, 'sub_module_obj': sub_module_obj, 'sub_module_path': sub_module_path}

##############################################################################
def flatten_dict(d, fd = {}, prefix = ''):
    """
    Flatten dict ({"x":{"y":"z"}} -> x.y=z)
    """


    for k in d:
        v = d[k]

        if type(v) == list and len(v) == 1 and type(v[0]) == dict:
            v = v[0]

        if type(v) == dict:
           new_prefix = prefix + k + '.'
           flatten_dict(v, fd, new_prefix)
        else:
           fd[prefix + k] = str(v)

    return

##############################################################################
def safe_int(i, d):
    """
    Get safe int (useful for sorting function)

    Args:    
             i (any): variable with any type
             d (int): default value

    Returns: 
             (int): returns i if it can be converted to int, or d otherwise
    """

    r = d
    try:
        r = int(i)
    except Exception as e:
        pass

    return r

##############################################################################
def safe_float(i, d):
    """
    Get safe float (useful for sorting function)

    Args:    
             i (any): variable with any type
             d (float): default value

    Returns: 
             (float): returns i if it can be converted to float or d otherwise

    """

    r = d
    try:
        r = float(i)
    except Exception as e:
        pass

    return r

##############################################################################
def get_set(meta, key, state, keys):
    """
    Get value from dict and update in another dict 

    Args:
      meta (dict): original dict
      key (str): key to get value from original dict
      state (dict): target dict
      keys (list): list of keys to set value in target dict

    Returns:
      (Python object): value from original dict or None

    """

    v = meta.get(key, None)
    if v != None:
        cur = state
        vv = None
        for k in keys:
            if k == keys[-1]:
                vv = cur.get(k, None)
                if vv == None:
                    cur[k] = v
            else:
                if k not in cur:
                    cur[k] = {}
                cur = cur[k]

    return v

##############################################################################
def digits(s, first = True):
    """
    Get first digits and convert to int

    Args:    
      s (str): string ("1.3+xyz")
      first (bool): if True, choose only first digits, otherwise all

    Returns: 
      (int): returns int from first digits or 0

    """

    v = 0

    digits = ''
    for char in s:
        if char.isdigit():
            digits+=char
        elif first:
            break

    try:
       v = int(digits)
    except Exception as e:
       pass

    return v

##############################################################################
def substitute_template(template, variables):
    """
    Substitutes variables in a template string with values from a dictionary.

    Args:
        template (str): The template string with placeholders (e.g., "something-{var1}-something-{var2}").
        vars (dict): A dictionary containing variable-value pairs (e.g., {'var1': 'a', 'var2': 'b'}).

    Returns:
        str: The template string with placeholders replaced by the corresponding values.
    """
    try:
        return template.format(**variables)
    except KeyError as e:
        return f"Error: Missing value for {e.args[0]} in the vars dictionary."

##############################################################################
def get_memory_use(console = False):

    """
    Get memory usage

    Args:
        console (bool): if True, print to console

    Returns:
       memory_use (int)
       memory_use_gb (float)
       available_memory (int)
       available_memory_gb (float)
       total_memory (int)
       total_memory_gb (float)

    """

    import os
    import psutil

    pid = os.getpid()

    python_process = psutil.Process(pid)

    memory_use = python_process.memory_info()[0] # in bytes
    memory_use_gb = memory_use / (1024 ** 3) 

    memory_info = psutil.virtual_memory()

    available_memory = memory_info.available  # in bytes
    total_memory = memory_info.total  # in bytes

    available_memory_gb = available_memory / (1024 ** 3)
    total_memory_gb = total_memory / (1024 ** 3)

    if console:
        print(f"Total Memory: {total_memory_gb:.2f} GB")
        print(f"Available Memory: {available_memory_gb:.2f} GB")
        print(f"Used Python Memory: {memory_use_gb:.2f} GB")

    return {'return':0, 'memory_use': memory_use,
                        'memory_use_gb': memory_use_gb,
                        'available_memory': available_memory,
                        'available_memory_gb': available_memory_gb,
                        'total_memory': total_memory,
                        'total_memory_gb': total_memory_gb}

##############################################################################
def get_disk_use(path = '/', console = False):
    """
    Get disk space

    Args:
        console (bool): if True, print to console

    Returns:
       total (int)
       total_gb (float)
       used (int)
       used_gb (float)
       free (int)
       free_gb (float)

    """

    import shutil

    total, used, free = shutil.disk_usage(path)

    total_gb = total / 1e9
    used_gb = used / 1e9
    free_gb = free / 1e9

    if console:
        print(f"Total disk space: {total_gb:.2f} GB")
        print(f"Used disk space: {used_gb:.2f} GB")
        print(f"Free disk space: {free_gb:.2f} GB")

    return {'return':0, 
            'total': total,
            'total_gb': total_gb,
            'used': used,
            'used_gb': used_gb,
            'free': free,
            'free_gb': free_gb}
