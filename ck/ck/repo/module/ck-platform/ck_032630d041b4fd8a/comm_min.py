#
# Minimal communication with the cK server
#
# Developer(s): Grigori Fursin, https://fursin.net
#

import json
import sys
import os

##############################################################################
# Send JSON request to the cK portal (without CK)

def send(i):
    """
    Input:  {
              action [str]     - remote API action name
              url [str]        - URL
              dict [dict]      - dict to send to remote server
            }

    Output: {
              return  [int]    - return code = 0 if success or >0 if error
              (error) [str]    - error string if return>0 
            }
    """

    # Import modules compatible with Python 2.x and 3.x
    import urllib

    try:    import urllib.request as urllib2
    except: import urllib2

    try:    from urllib.parse import urlencode
    except: from urllib import urlencode

    url=i.get('url')
    if url=='' or url==None:
       return {'return':1, 'error': 'cK API URL is not defined'}

    # Prepare dict to send to remote server
    ii={}
    ii['action']=i.get('action','')
    ii['dict']=i.get('dict',{})

    # Prepare post variables
    try:
       if sys.version_info[0]>2:
          s=json.dumps(ii, ensure_ascii=False).encode('utf8')
       else:
          s=json.dumps(ii, ensure_ascii=False, encoding='utf8')
    except Exception as e:
       return {'return':1, 'error':'problem converting dict to json ('+format(e)+')'}

    # Prepare request
    request = urllib2.Request(url, s, {'Content-Type': 'application/json'})

    # Connect
    try:
       f=urllib2.urlopen(request)
    except Exception as e:
       return {'return':1, 'error':'Access to the cK portal failed ('+format(e)+')'}

    # Read from Internet
    try:
       s=f.read()
       f.close()
    except Exception as e:
       return {'return':1, 'error':'Failed reading stream from the cK portal ('+format(e)+')'}

    # Check output
    try: s=s.decode('utf8')
    except Exception as e: pass

    # Try to convert output to dictionary
    try:
       d=json.loads(s, encoding='utf8')
    except Exception as e:
       return {'return':1, 'error':'problem converting text to json ('+format(e)+')'}

    if 'return' in d: d['return']=int(d['return']) # Fix for some strange behavior when 'return' is not integer - should check why ...
    else:
       d['return']=99
       d['error']='repsonse doesn\'t follow the cK standard'

    return d

