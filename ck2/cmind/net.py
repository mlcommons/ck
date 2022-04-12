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
    """
    Web request to cKnowledge.org server to get release notes about components

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
