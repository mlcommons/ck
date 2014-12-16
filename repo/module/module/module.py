#
# Collective Knowledge
#
# See CK LICENSE.txt for licensing details
# See CK Copyright.txt for copyright details
#
# Developer: Grigori Fursin
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel) 

# Local settings
import os

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
# Add module

def add(i):
    """
    Input:  {
              (repo_uoa)          - repo UOA
              module_uoa          - normally should be 'module' already
              data_uoa            - UOA of the module to be created

              (desc)              - module description
              (license)           - module license
              (copyright)         - module copyright
              (developer)         - module developer
              (developer_email)   - module developer
              (developer_webpage) - module developer
              (actions)           - dict with actions {"func1":{}, "func2":{} ...}
              (dict)              - other meta description to add to entry
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              Output of the 'add' kernel function
            }

    """

    # Check if global writing is allowed
    r=ck.check_writing({'module_uoa':work['self_module_uoa']})
    if r['return']>0: return r

    o=i.get('out','')

    # Find path to module 'module' to get dummies
    r=ck.access({'action':'load',
                 'module_uoa':work['self_module_uoa'],
                 'data_uoa':work['self_module_uoa'],
                 'common_func':'yes'})
    if r['return']>0: return r
    p=r['path']

    pm=os.path.join(p,cfg['dummy_module'])
    pma=os.path.join(p,cfg['dummy_module_action'])

    # Load module dummy
    r=ck.load_text_file({'text_file':pm})
    if r['return']>0: return r
    spm=r['string']

    # Load module action dummy
    r=ck.load_text_file({'text_file':pma})
    if r['return']>0: return r
    spma=r['string']

    # Prepare meta description
    desc=i.get('desc','')
    license=i.get('license','')
    copyright=i.get('copyright','')
    developer=i.get('developer','')
    developer_email=i.get('developer_email','')
    developer_webpage=i.get('developer_webpage','')
    actions=i.get('actions',{})

    # If console mode, ask some questions
    if o=='con':
       if desc=='':
          r=ck.inp({'text':'Add brief module description: '})
          desc=r['string']

       if license=='':
          r=ck.inp({'text':'Add brief module license (or Enter to use "'+ck.cfg['default_license']+'"): '})
          license=r['string']
          if license=='': license=ck.cfg['default_license']

       if copyright=='':
          r=ck.inp({'text':'Add brief module copyright (or Enter to use "'+ck.cfg['default_copyright']+'"): '})
          copyright=r['string']
          if copyright=='': copyright=ck.cfg['default_copyright']

       if developer=='':
          r=ck.inp({'text':'Add module\'s developer (or Enter to use "'+ck.cfg['default_developer']+'"): '})
          developer=r['string']
          if developer=='': developer=ck.cfg['default_developer']

       if developer_email=='':
          r=ck.inp({'text':'Add module\'s developer email (or Enter to use "'+ck.cfg['default_developer_email']+'"): '})
          developer_email=r['string']
          if developer_email=='': developer_email=ck.cfg['default_developer_email']

       if developer_webpage=='':
          r=ck.inp({'text':'Add module\'s developer webpage (or Enter to use "'+ck.cfg['default_developer_webpage']+'"): '})
          developer_webpage=r['string']
          if developer_webpage=='': developer_webpage=ck.cfg['default_developer_webpage']

       if len(actions)==0:
          act='*'
          while act!='':
             if act!='*': ck.out('')

             r=ck.inp({'text':'Add action function (or Enter to stop): '})
             act=r['string']
             if act!='': 
                actions[act]={}

                r1=ck.inp({'text':'Support web (y/N): '})
                x=r1['string'].lower()
                if x=='yes' or x=='y': 
                   fweb='yes'
                   actions[act]['for_web']=fweb

                r1=ck.inp({'text':'Add action description: '})
                adesc=r1['string']
                if adesc!='': 
                   actions[act]['desc']=adesc

    ck.out('')

    # Prepare meta description
    dd={}
    if desc!='': 
       dd['desc']=desc
    spm=spm.replace('$#desc#$', desc)

    if license!='': 
       dd['license']=license
    spm=spm.replace('$#license#$', license)

    if copyright!='': 
       dd['copyright']=copyright
    spm=spm.replace('$#copyright#$', copyright)

    dev=''
    if developer!='': 
       dev=developer
       dd['developer']=developer

    if developer_email!='': 
       if dev!='': dev+=', '
       dev+=developer_email
       dd['developer_email']=developer_email

    if developer_webpage!='': 
       if dev!='': dev+=', '
       dev+=developer_webpage
       dd['developer_webpage']=developer_webpage

    if dev!='':
       spm=spm.replace('$#developer#$', dev)

    dd['actions']=actions

    # Substitute actions
    for act in actions:
        adesc=actions[act].get('desc','TBD: action description')
        spm+='\n'+spma.replace('$#action#$', act).replace('$#desc#$',adesc)

    dx=i.get('dict',{})

    r=ck.merge_dicts({'dict1':dx, 'dict2':dd})
    if r['return']>0: return r

    # Add entry (it will ask further questions about alias and user-friendly name)
    i['common_func']='yes'
    i['dict']=dx
    i['sort_keys']='yes'
    r=ck.access(i)
    if r['return']>0: return r

    # Add module code
    p=r['path']
    pf=os.path.join(p, ck.cfg['module_full_code_name'])
   
    if o=='con':
       ck.out('')
       ck.out('Creating module code '+pf+' ...')

    # Write module code
    rx=ck.save_text_file({'text_file':pf, 'string':spm})
    if rx['return']>0: return rx

    return r
