#
# Collective Knowledge (CK)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin
#

import sys
import os

##############################################################################


def load_json_file(i):
    """Load json from file into dict
       Target audience: end users

    Args:    
              json_file (str): name of a json file 

    Returns:
              (dict): Unified CK dictionary:

                return (int): return code =  0, if successful
                                          >  0, if error
                (error) (str): error text if return > 0

                dict (dict or list): dict or list from the json file

    """

    import json

    fn = i['json_file']

    try:
        if sys.version_info[0] > 2:
            f = open(fn, 'r', encoding='utf8')
        else:
            f = open(fn, 'r')
    except Exception as e:
        return {'return': 16, 'error': 'problem opening json file='+fn+' ('+format(e)+')'}

    try:
        s = f.read()
    except Exception as e:
        f.close()
        return {'return': 1, 'error': 'problem reading json file='+fn+' ('+format(e)+')'}

    f.close()

    try:
        if sys.version_info[0] > 2:
            d = json.loads(s)
        else:
            d = json.loads(s, encoding='utf8')
    except Exception as e:
        return {'return': 1, 'error': 'problem parsing json from file='+fn+' ('+format(e)+')'}

    return {'return': 0, 'dict': d}

##############################################################################


def save_json_to_file(i):
    """Save dict to a json file
       Target audience: end users

    Args:    
              json_file (str): filename to save dictionary
              dict (dict): dict to save
              (sort_keys) (str): if 'yes', sort keys
              (safe) (str): if 'yes', ignore non-JSON values (only for Debugging - changes original dict!)

    Returns:
              (dict): Unified CK dictionary:

                return (int): return code =  0, if successful
                                          >  0, if error
                (error) (str): error text if return > 0

    """

    import json
    import ck.strings

    fn = i['json_file']

    if i.get('safe', '') == 'yes':
        d = i['dict']

        sd = {}

        # Check main unprintable keys
        for k in d:
            try:
                json.dumps(d[k])
            except Exception as e:
                pass
            else:
                sd[k] = d[k]

        i['dict'] = sd

    r = ck.strings.dump_json(i)
    if r['return'] > 0:
        return r
    s = r['string'].replace('\r', '')+'\n'

    return save_text_file({'text_file': fn, 'string': s})


##############################################################################
def load_yaml_file(i):
    """Load YAML file to dict
       Target audience: end users

    Args:    
              yaml_file (str): name of a YAML file

    Returns:
              (dict): Unified CK dictionary:

                return (int): return code =  0, if successful
                                          >  0, if error
                (error) (str): error text if return > 0

                dict (dict): dict from a YAML file

    """

    import yaml

    fn = i['yaml_file']

    try:
        if sys.version_info[0] > 2:
            f = open(fn, 'r', encoding='utf8')
        else:
            f = open(fn, 'r')
    except Exception as e:
        return {'return': 16, 'error': 'problem opening YAML file='+fn+' ('+format(e)+')'}

    try:
        s = f.read()
    except Exception as e:
        f.close()
        return {'return': 1, 'error': 'problem reading YAML file='+fn+' ('+format(e)+')'}

    f.close()

    try:
        d = yaml.load(s, Loader=yaml.FullLoader)
    except Exception as e:
        return {'return': 1, 'error': 'problem parsing YAML from file='+fn+' ('+format(e)+')'}

    return {'return': 0, 'dict': d}

##############################################################################


def save_yaml_to_file(i):
    """Save dict to a YAML file
       Target audience: end users

    Args:    
              yaml_file (str): name of a YAML file
              dict (dict): dict to save

    Returns:
              (dict): Unified CK dictionary:

                return (int): return code =  0, if successful
                                          >  0, if error
                (error) (str): error text if return > 0

    """

    import yaml

    fn = i['yaml_file']
    d = i['dict']

    try:
        # If using just dump and keys are in unicode,
        # pyyaml adds warning and makes produced yaml unparsable
        s = yaml.safe_dump(d)
    except Exception as e:
        return {'return': 1, 'error': 'problem converting dict to YAML ('+format(e)+')'}

    return save_text_file({'text_file': fn, 'string': s})


##############################################################################
def load_text_file(i):
    """Load a text file to a string or list
       Target audience: end users

    Args:    
              text_file (str): name of a text file
              (keep_as_bin) (str): if 'yes', return only bin
              (encoding) (str): by default 'utf8', however sometimes we use utf16

              (split_to_list) (str): if 'yes', split to list

              (convert_to_dict) (str): if 'yes', split to list and convert to dict
              (str_split) (str): if !='', use as separator of keys/values when converting to dict
              (remove_quotes) (str): if 'yes', remove quotes from values when converting to dict

              (delete_after_read) (str): if 'yes', delete file after read (useful when reading tmp files)

    Returns:
              (dict): Unified CK dictionary:

                return (int): return code =  0, if successful
                                          >  0, if error
                (error) (str): error text if return > 0

                bin (byte): loaded text file as byte array

                (string) (str): loaded text as string with removed \r

                (lst) (list): if split_to_list=='yes', split text to list

                (dict) (dict): if convert_to_dict=='yes', return as dict

    """

    fn = i['text_file']

    en = i.get('encoding', '')
    if en == '' or en == None:
        en = 'utf8'

    try:
        f = open(fn, 'rb')
    except Exception as e:
        return {'return': 16, 'error': 'problem opening text file='+fn+' ('+format(e)+')'}

    try:
        b = f.read()
    except Exception as e:
        f.close()
        return {'return': 1, 'error': 'problem reading text file='+fn+' ('+format(e)+')'}

    f.close()

    r = {'return': 0, 'bin': b}

    if i.get('delete_after_read', '') == 'yes':
        import os
        os.remove(fn)

    if i.get('keep_as_bin', '') != 'yes':
        try:
            # decode into Python string (unicode in Python3)
            s = b.decode(en).replace('\r', '')
        except Exception as e:
            return {'return': 1, 'error': 'problem decoding content from file "'+fn+'" ('+format(e)+')'}

        r['string'] = s

        cl = i.get('split_to_list', '')
        cd = i.get('convert_to_dict', '')

        if cl == 'yes' or cd == 'yes':
            lst = s.split('\n')
            r['lst'] = lst

            if cd == 'yes':
                dd = {}

                ss = i.get('str_split', '')
                rq = i.get('remove_quotes', '')
                if ss == '':
                    ss = ':'

                for q in lst:
                    qq = q.strip()
                    ix = qq.find(ss)
                    if ix > 0:
                        k = qq[0:ix].strip()
                        v = ''
                        if ix+1 < len(qq):
                            v = qq[ix+1:].strip()
                        if v != '' and rq == 'yes':
                            if v.startswith('"'):
                                v = v[1:]
                            if v.endswith('"'):
                                v = v[:-1]
                        dd[k] = v

                r['dict'] = dd

    return r

##############################################################################


def save_text_file(i):
    """Save string to a text file with all \r removed
       Target audience: end users

    Args:    
              text_file (str): name of a text file
              string (str): string to write to a file (all \r will be removed)
              (append) (str): if 'yes', append to a file

    Returns:
              (dict): Unified CK dictionary:

                return (int): return code =  0, if successful
                                          >  0, if error
                (error) (str): error text if return > 0

    """

    fn = i['text_file']

    s = i['string']

    try:
        s = s.replace('\r', '')
    except Exception as e:
        pass

    try:
        s = s.replace(b'\r', b'')
    except Exception as e:
        pass

    m = 'w'
    if i.get('append', '') == 'yes':
        m = 'a'

    try:
        s = s.encode('utf8')
    except Exception as e:
        pass

    try:
        #      if sys.version_info[0]>2:
        #         f=open(fn, m+'b')
        #         f.write(s)
        #      else:
        f = open(fn, m+'b')
        f.write(s)
    except Exception as e:
        return {'return': 1, 'error': 'problem writing text file='+fn+' ('+format(e)+')'}

    f.close()

    return {'return': 0}
