#
# Collective Knowledge: autotune any custom dimensions provided by user
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

line='****************************************************************'

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
    global cfg, work

    import copy

    mcfg=i.get('module_cfg',{})
    if len(mcfg)>0: 
       cfg=mcfg

    mwork=i.get('module_work',{})
    if len(mwork)>0: work=mwork

    # Setting output
    o=i.get('out','')
    oo=''
    if o=='con': oo='con'

    quiet=i.get('quiet','')

    er=i.get('exchange_repo','')
    if er=='': er=ck.cfg['default_exchange_repo_uoa']
    esr=i.get('exchange_subrepo','')
    if esr=='': esr=ck.cfg['default_exchange_subrepo_uoa']

    if i.get('local','')=='yes': 
       er='local'
       esr=''
    else:
       return {'return':1, 'error':'can\'t crowdsource these experiments'}

    la=i.get('local_autotuning','')

    # Get user 
    user=''

    mcfg={}
    ii={'action':'load',
        'module_uoa':'module',
        'data_uoa':cfg['module_deps']['program.optimization']}
    r=ck.access(ii)
    if r['return']==0:
       mcfg=r['dict']

       dcfg={}
       ii={'action':'load',
           'module_uoa':mcfg['module_deps']['cfg'],
           'data_uoa':mcfg['cfg_uoa']}
       r=ck.access(ii)
       if r['return']>0 and r['return']!=16: return r
       if r['return']!=16:
          dcfg=r['dict']

       user=dcfg.get('user_email','')

    ceuoa=i.get('compiler_env_uoa', '')

    if ceuoa!='':
       rx=ck.access({'action':'load',
                     'module_uoa':cfg['module_deps']['env'],
                     'data_uoa':ceuoa})
       if rx['return']>0: return rx
       ceuoa=rx['data_uid']

    # Initialize local environment for program optimization ***********************************************************
    pi=i.get('platform_info',{})
    if len(pi)==0:
       ii=copy.deepcopy(i)
       ii['action']='initialize'
       ii['module_uoa']=cfg['module_deps']['program.optimization']
       ii['exchange_repo']=er
       ii['exchange_subrepo']=esr
       r=ck.access(ii)
       if r['return']>0: return r

       pi=r['platform_info']
       user=r.get('user','')

    hos=pi['host_os_uoa']
    hosd=pi['host_os_dict']

    tos=pi['os_uoa']
    tosd=pi['os_dict']
    tbits=tosd.get('bits','')

    remote=tosd.get('remote','')

    tdid=pi['device_id']

    program_tags=i.get('program_tags','')
    if program_tags=='' and i.get('local_autotuning','')!='yes' and i.get('data_uoa','')=='':
       program_tags=cfg['program_tags']

    # Check that has minimal dependencies for this scenario ***********************************************************
    sdeps=i.get('dependencies',{}) # useful to preset inside crowd-tuning
    if len(sdeps)==0:
       sdeps=copy.deepcopy(cfg.get('deps',{}))
    if len(sdeps)>0:
       if o=='con':
          ck.out(line)
          ck.out('Resolving software dependencies required for this scenario ...')
          ck.out('')

       if ceuoa!='':
          x=sdeps.get('compiler',{})
          if len(x)>0:
             if 'cus' in x: del(x['cus'])
             if 'deps' in x: del(x['deps'])
             x['uoa']=ceuoa
             sdeps['compiler']=x

       ii={'action':'resolve',
           'module_uoa':cfg['module_deps']['env'],
           'host_os':hos,
           'target_os':tos,
           'device_id':tdid,
           'deps':sdeps,
           'add_customize':'yes'}
       if quiet=='yes': 
          ii['random']='yes'
       else:
          ii['out']=oo
       rx=ck.access(ii)
       if rx['return']>0: return rx

       sdeps=rx['deps'] # Update deps (add UOA)

    cpu_name=pi.get('features',{}).get('cpu',{}).get('name','')
    compiler_soft_uoa=sdeps.get('compiler',{}).get('dict',{}).get('soft_uoa','')
    compiler_env=sdeps.get('compiler',{}).get('bat','')

    plat_extra={}
    pft=pi.get('features',{})
    for q in pft:
        if q.endswith('_uid'):
           plat_extra[q]=pft[q]
        elif type(pft[q])==dict and pft[q].get('name','')!='':
           plat_extra[q+'_name']=pft[q]['name']

    # Detect real compiler version ***********************************************************
    compiler_version=''
    compiler=''
    if compiler_soft_uoa!="":
       if o=='con':
          ck.out(line)
          ck.out('Detecting compiler version ...')

       ii={'action':'internal_detect',
           'module_uoa':cfg['module_deps']['soft'],
           'data_uoa':compiler_soft_uoa,
           'host_os':hos,
           'target_os':tos,
           'target_device_id':tdid,
           'env':compiler_env}
       r=ck.access(ii)
       if r['return']>0: return r

       compiler_version=r['version_str']

       compiler=cfg.get('compiler_name','')+' '+compiler_version

    if o=='con':
       ck.out('')
       if compiler!='':
          ck.out('* Compiler: '+compiler)
       ck.out('* CPU:      '+cpu_name)
    
    # Start preparing input to run program.optimization
    ii=copy.deepcopy(i)

    em={'cpu_name':cpu_name}
    if compiler!='': em['compiler']=compiler

    ii['action']='run'
    ii['module_uoa']=cfg['module_deps']['program.optimization']

    ii['host_os']=hos
    ii['target_os']=tos
    ii['target_device_id']=tdid
    ii['dependencies']=sdeps

    ii['scenario_cfg']=cfg

    ii['platform_info']=pi

    ii['program_tags']=program_tags

    ii['scenario_module_uoa']=work['self_module_uid']

    ii['experiment_meta']=em

    ii['experiment_meta_extra']=plat_extra

    ii['exchange_repo']=er
    ii['exchange_subrepo']=esr

    ii['user']=user

    # Select sub-scenario ********************************************************************
    from random import randint
    ss=1 # num of scenarios

    sx=randint(1,ss)

    rr={'return':0}

    if sx==1 or la=='yes':
       # **************************************************************** explore random program/dataset
       sdesc='custom dimensions autotuner'
       if o=='con':
          ck.out('')
          ck.out('  ****** Sub-scenario: '+sdesc+' ******')

       ii['subscenario_desc']=sdesc

       rr=ck.access(ii)
       if rr['return']>0: return rr

    rr['platform_info']=pi

    return rr

##############################################################################
# view solutions in html

def html_viewer(i):
    """
    See in module "experiment.tune.compiler.flags"
    """

    i['module_uoa']='experiment.tune.compiler.flags'
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

    return {'return':1, 'error':'pruning is not yet supported in this scenario'}
