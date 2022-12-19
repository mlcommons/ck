import os

ERROR_UNKNOWN_FILE_EXTENSION = 1
ERROR_PATH_NOT_FOUND=2
ERROR_FILE_NOT_FOUND=16

###########################################################################
def load_json_or_yaml(file_name):

    if file_name.endswith('json'):
        return load_json(file_name)
    elif file_name.endswith('yaml'):
        return load_yaml(file_name)

    return {'return':ERROR_UNKNOWN_FILE_EXTENSION, 'error':'unknown file extension'}

###########################################################################
def save_json_or_yaml(file_name, data, sort_keys=False):
    if file_name.endswith('json'):
        return save_json(file_name, data, sort_keys)
    elif file_name.endswith('yaml'):
        return save_yaml(file_name, data, sort_keys)

    return {'return':ERROR_UNKNOWN_FILE_EXTENSION, 'error':'unknown file extension'}

###########################################################################
def load_json(file_name):

    import json
    
    with open(file_name) as jf:
        data = json.load(jf)

    return {'return':0,
            'data': data}

###########################################################################
def save_json(file_name, data={}, indent=2, sort_keys=True):

    import json
    
    with open(file_name, 'w') as jf:
        jf.write(json.dumps(data, indent=indent, sort_keys=sort_keys))

    return {'return':0}

###########################################################################
def load_yaml(file_name):

    import yaml
    
    with open(file_name) as jf:
        data = yaml.load(jf, Loader=yaml.FullLoader)

    return {'return':0,
            'data': data}

###########################################################################
def save_yaml(file_name, data={}, sort_keys=True):

    import yaml
    
    with open(file_name, 'w') as jf:
        data = yaml.dump(data, jf)

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
