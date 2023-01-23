#
# Collective Knowledge (Caffe2 CK front-end)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: cTuning foundation, admin@cTuning.org, http://cTuning.org
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel) 

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
    return {'return':0}

##############################################################################
# crowd-benchmark caffe2

def crowdbench(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    i['action']='crowdsource'
    i['module_uoa']=cfg['module_deps']['experiment.bench.caffe2']

    return ck.access(i)

##############################################################################
# replay experiment

def replay(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    i['module_uoa']=cfg['module_deps']['experiment.bench.caffe2']
    return ck.access(i)

##############################################################################
# autotune Caffe2 workloads

def autotune(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    i['module_uoa']=cfg['module_deps']['program']
    i['data_uoa']='caffe2'
    i['explore']='yes'
    i['extra_tags']='dnn'
    i['skip_collaborative']='yes'
    i['skip_pruning']='yes'
    i['iterations']=-1
    i['new']='yes'
    i['cmd_keys']=['time_cpu','time_cuda']

    return ck.access(i)
