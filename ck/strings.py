#
# Collective Knowledge (CK)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin
#

import sys

##############################################################################
def dump_json(i):
    """
    Desc: dump json to string

    Target: end users

    Input:  {
              dict          - dictionary
              (skip_indent) - if 'yes', skip indent
              (sort_keys)   - if 'yes', sort keys
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error

              string       - json string (in utf8)
            }
    """

    import json

    d=i['dict']
    si=i.get('skip_indent','')

    sk=False
    if i.get('sort_keys','')=='yes': sk=True

    try:
       if sys.version_info[0]>2:
          if si=='yes': s=json.dumps(d, ensure_ascii=False, sort_keys=sk)
          else:         s=json.dumps(d, indent=2, ensure_ascii=False, sort_keys=sk)
       else:
          if si=='yes': s=json.dumps(d, ensure_ascii=False, encoding='utf8', sort_keys=sk)
          else:         s=json.dumps(d, indent=2, ensure_ascii=False, encoding='utf8', sort_keys=sk)
    except Exception as e:
       return {'return':1, 'error':'problem converting dict to json ('+format(e)+')'}

    return {'return':0, 'string':s}



##############################################################################
def copy_to_clipboard(i): # pragma: no cover 
    """
    Desc: Copy string to clipboard if supported by OS (requires Tk or pyperclip)

    Target: end users

    Input:  {
              string - string to copy

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }
    """

    s=i['string']

    failed=False
    ee=''

    # Try to load pyperclip (seems to work fine on Windows)
    try:
       import pyperclip
    except Exception as e:
       ee=format(e)
       failed=True
       pass

    if not failed:
       pyperclip.copy(s)
    else:
       failed=False

       # Try to load Tkinter
       try:
          from Tkinter import Tk
       except ImportError as e:
          ee=format(e)
          failed=True
          pass

       if failed:
          failed=False
          try:
             from tkinter import Tk
          except ImportError as e:
             ee=format(e)
             failed=True
             pass

       if failed:
          return {'return':1, 'error':'none of pyperclip/Tkinter/tkinter packages is installed'}

       # Copy to clipboard
       try:
          r = Tk()
          r.withdraw()
          r.clipboard_clear()
          r.clipboard_append(s)
          r.destroy()
       except Exception as e:
          return {'return':1, 'error':'problem copying string to clipboard ('+format(e)+')'}

    return {'return':0}


##############################################################################
def convert_json_str_to_dict(i):
    """
    Desc: Convert string of a special format to json

    Target: end users

    Input:  {
              str                      - string (use ' instead of ", i.e. {'a':'b'} 
                                         to avoid issues in CMD in Windows and Linux!)

              (skip_quote_replacement) - if 'yes', do not make above replacement
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              dict         - dict from json file
            }
    """

    import json

    s=i['str']

    if i.get('skip_quote_replacement','')!='yes':
       s=s.replace('"', '\\"')
       s=s.replace('\'', '"')

    try:
       d=json.loads(s, encoding='utf8')
    except Exception as e:
       return {'return':1, 'error':'problem converting text to json ('+format(e)+')'}

    return {'return':0, 'dict': d}
