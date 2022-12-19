#
# Collective Knowledge (CK)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin
#

import urllib
import json
import sys

try:
    from urllib.parse import urlencode
    from urllib.parse import quote_plus
except:
    from urllib import urlencode
    from urllib import quote_plus

try:
    import urllib.request as urllib2
except:
    import urllib2

##########################################################################


def request(i):
    """Web request to cKnowledge.org server
       Target audience: CK kernel and low-level developers

    Args:    
              get (dict): GET parameters
              post (dict): POST parameters

    Returns:
              (dict): Unified CK dictionary:

                return (int): return code =  0, if successful
                                          >  0, if error
                (error) (str): error text if return > 0

                string (str): returned string from the server
                dict (dict): JSON string converted to dict (if possible)

    """

    url = 'https://cKnowledge.org/api.php?'

    # Prepare dict to send to remote server
    ii = i.get('get', {})

    started = False
    for k in ii:
        v = ii[k]
        if started:
            url += '&'
        started = True
        url += k+'='+quote_plus(v)

    # Request
    request = urllib2.Request(url)

    # Connect
    try:
        f = urllib2.urlopen(request)
    except Exception as e:
        return {'return': 1, 'error': 'Access to cKnowledge.org failed ('+format(e)+')'}

    # Read
    try:
        s = f.read()
    except Exception as e:
        return {'return': 1, 'error': 'Failed to read stream from cKnowledge.org ('+format(e)+')'}

    # CLose
    try:
        f.close()
    except Exception as e:
        return {'return': 1, 'error': 'Failed to close stream from cKnowledge.org ('+format(e)+')'}

    # Check UTF
    try:
        s = s.decode('utf8')
    except Exception as e:
        pass

    # Check output
    d = {}

    # Try to convert output to dictionary
    try:
        d = json.loads(s)
    except Exception as e:
        pass

    return {'return': 0, 'string': s, 'dict': d}


##########################################################################
def access_ck_api(i):
    """Universal web request to the CK server (usually cKnowledge.io)
       Target audience: CK kernel and low-level developers

    Args:    
              url (str): URL API
              (dict) (dict): dict to send to above URL

    Returns:
              (dict): Unified CK dictionary:

                return (int): return code =  0, if successful
                                          >  0, if error
                (error) (str): error text if return > 0

                dict (dict): dictionary from the CK server

    """

    import ck.strings

    url = i['url']
    d = i.get('dict', {})

    # Import modules compatible with Python 2.x and 3.x
    import urllib

    try:
        import urllib.request as urllib2
    except:
        import urllib2

    try:
        from urllib.parse import urlencode
    except:
        from urllib import urlencode

    # Prepare post variables
    r = ck.strings.dump_json({'dict': d, 'skip_indent': 'yes'})
    if r['return'] > 0:
        return r

    s = r['string']
    if sys.version_info[0] > 2:
        s = s.encode('utf8')

    # Prepare request
    request = urllib2.Request(url, s, {'Content-Type': 'application/json'})

    # Connect
    try:
        f = urllib2.urlopen(request)
    except Exception as e:
        return {'return': 1, 'error': 'Access to the CK portal failed ('+format(e)+')'}

    # Read from Internet
    try:
        s = f.read()
        f.close()
    except Exception as e:
        return {'return': 1, 'error': 'Failed reading stream from the CK portal ('+format(e)+')'}

    # Check output
    try:
        s = s.decode('utf8')
    except Exception as e:
        pass

    # Try to convert output to dictionary
    r = ck.strings.convert_json_str_to_dict(
        {'str': s, 'skip_quote_replacement': 'yes'})
    if r['return'] > 0:
        return {'return': 1, 'error': 'can\'t parse output from the CK portal ('+r['error']+'):\n'+s[:256]+'\n\n...)'}

    d = r['dict']

    if 'return' in d:
        d['return'] = int(d['return'])
    else:
        return {'return': 99, 'error': 'repsonse doesn\'t follow the CK API standard'}

    return {'return': 0, 'dict': d}
