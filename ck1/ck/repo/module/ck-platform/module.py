#
# Collective Knowledge (cKnowledge.io platform)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
##
# Developer: Grigori Fursin, Grigori.Fursin@cTuning.org, http://fursin.net
#

cfg = {}  # Will be updated by CK (meta description of this module)
work = {}  # Will be updated by CK (temporal data)
ck = None  # Will be updated by CK (initialized CK kernel)

# Local settings

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

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
# setup platform

def setup(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    from ck_032630d041b4fd8a import setup as xsetup

    xsetup.setup(i)

    return {'return':0}

##############################################################################
# login to platform

def login(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    from ck_032630d041b4fd8a import setup as xsetup
    
    xsetup.login(i)

    return {'return':0}

##############################################################################
# publish CK component

def publish(i):
    """
    Input:  {
              ckid (CID) - ({repo UOA}:){module UOA}:{data UOA}
              (tags)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    from ck_032630d041b4fd8a import obj as xobj

    i['cid']=i['ckid']

    return xobj.publish(i)

##############################################################################
# list versions of a CK component

def versions(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    from ck_032630d041b4fd8a import obj as xobj

    i['cid']=i['ckid']

    return xobj.versions(i)

##############################################################################
# init graph

def init_graph(i):
    """
    Input:  {
              uid [str] - graph identifyer
              (version) [str] - graph version
              (desc_file) [str] - file with graph description
              (tags) [str] - tags separated by comma
              (name)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    from ck_032630d041b4fd8a import graph as xgraph

    return xgraph.init(i)

##############################################################################
# push result

def push_result(i):
    """
    Input:  {
               uid
               version
               filename
               json_string
               point
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    from ck_032630d041b4fd8a import graph as xgraph

    return xgraph.push(i)

##############################################################################
# access platform

def access(i):
    """
    Input:  {
               filename,
               json_string
               display
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    from ck_032630d041b4fd8a import comm as xcomm

    return xcomm.access(i)
