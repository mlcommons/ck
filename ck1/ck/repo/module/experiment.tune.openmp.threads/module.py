#
# Collective Knowledge: compiler flags crowdtuning (crowdsource autotuning via spare computers such as mobile devices)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin, Grigori.Fursin@cTuning.org, http://fursin.net
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel) 

# Local settings
import copy

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
# crowdsource these experiments

def crowdsource(i):
    """
    See in module "experiment.tune.compiler.flags"
    """

    i['module_uoa']='experiment.tune.custom.dimensions'
    i['skip_pruning']='yes'
    i['module_cfg']=copy.deepcopy(cfg)
    i['module_work']=copy.deepcopy(work)
    return ck.access(i)

##############################################################################
# view solutions in html

def html_viewer(i):
    """
    See in module "experiment.tune.compiler.flags"
    """

    i['module_uoa']='experiment.tune.custom.dimensions'
    i['module_cfg']=copy.deepcopy(cfg)
    i['module_work']=copy.deepcopy(work)
    return ck.access(i)

##############################################################################
# replay optimization

def replay(i):
    """
    See in module "program.optimization"
    """

    i['module_uoa']=cfg['module_deps']['program.optimization']
    i['module_ref_uoa']=work['self_module_uid']
    i['module_cfg']=copy.deepcopy(cfg)
    i['module_work']=copy.deepcopy(work)
    return ck.access(i)

##############################################################################
# prune compiler flags to find minimal set of choices

def prune(i):
    """
    See in module "program.optimization"
    """

    i['module_uoa']=cfg['module_deps']['program.optimization']
    i['module_ref_uoa']=work['self_module_uid']
    i['module_cfg']=copy.deepcopy(cfg)
    i['module_work']=copy.deepcopy(work)
    return ck.access(i)
