#
# Collective Knowledge (checking and installing software)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Leo Gordon, leo@dividiti.com
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel)


def init(i):
    """
    Not to be called directly. Sets the path to the vqe_plugin.
    """

    return {'return':0}


def list(i):
    """
    Input:  {
            }

    Output: {
                return              - return code =  0, if successful
                                                  >  0, if error
                (error)             - error text if return > 0
            }
    Test:
            ck list sut
            ck list sut --out=json
    """

    from pprint import pprint

    interactive     = i.get('out')=='con'
    repo_uoa        = i.get('repo_uoa', '*')

    search_adict    = { 'action':       'search',
                        'repo_uoa':     i.get('repo_uoa', '*'),
                        'module_uoa':   i['module_uoa'],
                        'data_uoa':     i.get('data_uoa', '*'),
                        'add_meta':     'yes',
    }
    r=ck.access( search_adict )
    if r['return']>0: return r

    list_of_suts = r['lst']

    for entry in list_of_suts:
        repo_uoa    = entry['repo_uoa']
        module_uoa  = entry['module_uoa']
        data_uoa    = entry['data_uoa']
        ck_addr     = "{}:{}:{}".format(repo_uoa, module_uoa, data_uoa)
        path        = entry['path']
        data        = entry['meta'].get('data', {})
        system_name = data.get('system_name', '(Unknown system_name)')

        if interactive:
            ck.out("{}\t\t{}\t\t{}".format(ck_addr, system_name, path))

    return { 'return': 0, 'lst': list_of_suts }


def show(i):
    """
    Input:  {
                (data_uoa)          - name of the SUT entry
            }

    Output: {
                return              - return code =  0, if successful
                                                  >  0, if error
                (error)             - error text if return > 0
            }
    Test:
            ck show sut:velociti
    """

    from pprint import pprint

    interactive     = i.get('out')=='con'
    data_uoa = i.get('data_uoa')
    if data_uoa:
        load_adict = {  'action':           'load',
                        'module_uoa':       i['module_uoa'],
                        'data_uoa':         data_uoa,
        }
        r=ck.access( load_adict )
        if r['return']>0: return r

        data = r['dict'].get('data',{})

        if interactive:
            pprint(data)

    return { 'return': 0 }

