#
# Collective Knowledge (CK web front-end)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: cTuning foundation
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel) 

# Local settings

import os

fdata_name='ck_top_data'
fmodule_name='ck_top_module'
frepo_name='ck_top_repo'

form_name='ck_top_form'
onchange='document.'+form_name+'.submit();'

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
    return {'return':0}


##############################################################################
# display webpage with interactive dashboard widget

def display(args):
    """
    Input:  {
              (host)        - Internal web server host
              (port)        - Internal web server port

              (wfe_host)    - External web server host
              (wfe_port)    - External web server port

              (extra_url)   - extra URL
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    # Filter and pass some arguments from command line to browser
    extra_url = { key:args[key] for key in args if key in ['scenario', 'global'] }
    extra_url = "&".join("{0}={1}".format(key, extra_url[key]) for key in extra_url)

    args['action'] = 'start'
    args['module_uoa'] = 'web'
    args['browser'] = 'yes'
    args['template'] = 'dashboard'
    args['cid'] = ''
    args['extra_url'] = extra_url

    return ck.access(args)
