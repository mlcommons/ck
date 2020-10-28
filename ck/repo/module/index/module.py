#
# Collective Knowledge (indexing through ElasticSearch)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin
#

cfg = {}  # Will be updated by CK (meta description of this module)
work = {}  # Will be updated by CK (temporal data)
ck = None  # Will be updated by CK (initialized CK kernel)

# Local settings

##############################################################################
# Initialize module


def init(i):
    """

    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    return {'return': 0}

##############################################################################
# turn indexing on


def on(i):
    """

    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o = i.get('out', '')

    i['status'] = 'yes'

    r = status(i)
    if r['return'] > 0:
        return r

    if o == 'con':
        ck.out('Indexing is on')

    return {'return': 0}

##############################################################################
# turn indexing off


def off(i):
    """

    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o = i.get('out', '')

    i['status'] = 'no'

    r = status(i)
    if r['return'] > 0:
        return r

    if o == 'con':
        ck.out('Indexing is off')

    return {'return': 0}

##############################################################################
# show indexing status


def show(i):
    """

    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o = i.get('out', '')

    i['status'] = ''

    r = status(i)
    if r['return'] > 0:
        return r

    s = r['status']
    if s == 'yes':
        sx = 'on'
    else:
        sx = 'off'

    if o == 'con':
        ck.out('Indexing status: '+sx)

    return {'return': 0}

##############################################################################
# check indexing status


def status(i):
    """

    Input:  {
               status - if 'yes', turn it on 
                        if 'no', turn it off 
                        if '', return status
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
              status
            }

    """

    # Get current configuration
    cfg = {}

    r = ck.access({'action': 'load',
                   'repo_uoa': ck.cfg['repo_name_default'],
                   'module_uoa': ck.cfg['subdir_kernel'],
                   'data_uoa': ck.cfg['subdir_kernel_default']})
    if r['return'] == 0:
        cfg.update(r['dict'])

    r = ck.access({'action': 'load',
                   'repo_uoa': ck.cfg['repo_name_local'],
                   'module_uoa': ck.cfg['subdir_kernel'],
                   'data_uoa': ck.cfg['subdir_kernel_default']})
    if r['return'] > 0:
        if r['return'] != 16:
            return r

        ck.out('')
        ck.out('We strongly suggest you to setup local repository first!')
        return {'return': 0}

    cfg.update(r['dict'])

    # Turn on indexing
    st = i.get('status', '')
    s = cfg.get('use_indexing', ck.cfg.get('use_indexing', ''))

    if st != '':
        cfg['use_indexing'] = st
        s = st

    r = ck.access({'action': 'update',
                   'repo_uoa': ck.cfg['repo_name_local'],
                   'module_uoa': ck.cfg['subdir_kernel'],
                   'data_uoa': ck.cfg['subdir_kernel_default'],
                   'dict': cfg,
                   'substitute': 'yes',
                   'ignore_update': 'yes',
                   'skip_indexing': 'yes'})
    if r['return'] > 0:
        return r

    return {'return': 0, 'status': s}

##############################################################################
# check indexing status


def test(i):
    """

    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o = i.get('out', '')

    r = ck.access_index_server({'request': 'TEST', 'dict': {}})
    if r['return'] > 0:
        return r
    dd = r['dict']

    status = dd.get('status', 0)
    if status != 200:
        return {'return': 1, 'error': 'returned status is not 200'}

    version = dd.get('version', {}).get('number', '')

    if o == 'con':
        ck.out('Indexing server is working (version = '+version+')')

    return r

##############################################################################
# clean whole index


def clean(i):
    """

    Input:  {
              (force)  - if 'yes', force cleaning
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o = i.get('out', '')

    to_delete = True
    if o == 'con' and i.get('force', '') != 'yes':
        r = ck.inp({'text': 'Are you sure to clean the whole index (y/N): '})
        c = r['string'].lower()
        if c != 'y' and c != 'yes':
            to_delete = False

    if to_delete:
        r = ck.access_index_server(
            {'request': 'DELETE', 'path': '/_all', 'dict': {}})
        if r['return'] > 0:
            return r
        dd = r['dict']

        status = dd.get('status', 0)
        err = dd.get('error', '')

        if err != '':
            r = {'return': 1, 'error': err}

    return r
