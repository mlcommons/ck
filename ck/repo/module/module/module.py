#
# Collective Knowledge
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
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

       ck.out('')

       if license=='':
          r=ck.inp({'text':'Add brief module license (or Enter to use "'+ck.cfg['default_license']+'"): '})
          license=r['string']
          if license=='': license=ck.cfg['default_license']

       if copyright=='':
          r=ck.inp({'text':'Add brief module copyright (or Enter to use "'+ck.cfg['default_copyright']+'"): '})
          copyright=r['string']
          if copyright=='': copyright=ck.cfg['default_copyright']

       ck.out('')

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
             ck.out('')

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

##############################################################################
# show info about modules

def show(i):
    """
    Input:  {
               (the same as list; can use wildcards)


            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')

    html=False
    if o=='html' or i.get('web','')=='yes':
       html=True

    h=''

    unique_repo=False
    if i.get('repo_uoa','')!='': unique_repo=True

    import copy
    ii=copy.deepcopy(i)

    ii['out']=''
    ii['action']='list'
    ii['add_meta']='yes'

    rx=ck.access(ii)
    if rx['return']>0: return rx

    ll=sorted(rx['lst'], key=lambda k: k['data_uoa'])

    if html:
       h+='<i><b>Note:</b> you can obtain JSON API of a given action of a given module in CMD via "ck &lt;action&gt; &lt;module&gt; --help"</i><br><br>\n'
       h+='<table cellpadding="5">\n'

       h+=' <tr>\n'
       h+='  <td><b>CK&nbsp;module&nbsp;(aka&nbsp;wrapper,&nbsp;plugin&nbsp;or&nbsp;container):</b></td>\n'
       h+='  <td width="200"><b>CK Repository:</b></td>\n'
       h+='  <td><b>Description and actions:</b></td>\n'
       h+=' </tr>\n'


    repo_url={}

    for l in ll:
        ln=l['data_uoa']
        lr=l['repo_uoa']

        lr_uid=l['repo_uid']
        url=''
        if lr=='default':
           url='' #'http://github.com/ctuning/ck'
        elif lr_uid in repo_url:
           url=repo_url[lr_uid]
        else:
           rx=ck.load_repo_info_from_cache({'repo_uoa':lr_uid})
           if rx['return']>0: return rx
           url=rx.get('dict',{}).get('url','')
           repo_url[lr_uid]=url


        if lr not in cfg['skip_repos']:
           lm=l['meta']
           ld=lm.get('desc','')

           actions=lm.get('actions',{})

           ###############################################################
           if html:
              h+=' <tr>\n'

              h+='  <td valign="top"><b>'+ln+'</b></td>\n'

              x1=''
              x2=''
              if url!='':
                 x1='<a href="'+url+'">'
                 x2='</a>'

              h+='  <td valign="top"><i>'+x1+lr+x2+'</i></td>\n'

              h+='  <td valign="top">'+ld+'\n'

              if len(actions)>0:
                 h+='<ul>\n'
                 for q in sorted(actions):
                     qq=actions[q]
                     qd=qq.get('desc','')
                     h+='<li><i>'+q+'</i>'
                     if qd!='':
                        h+=' - '+qd
                 h+='</ul>\n'

              h+='</td>\n'

              h+=' </tr>\n'

           ###############################################################
           elif o=='mediawiki':
              x=lr
              if url!='':
                 x='['+url+' '+lr+']'
              ck.out('* \'\'\''+ln+'\'\'\' ('+x+') - '+ld)
              if len(actions)>0:
                 for q in sorted(actions):
                     qq=actions[q]
                     qd=qq.get('desc','')
                     ck.out('** \'\''+q+'\'\' - '+qd)

           ###############################################################
           elif o=='con' or o=='txt':
              if unique_repo:
                 ck.out('')
                 s=ln+' - '+ld

              else:
                 ss=''
                 if len(ln)<35: ss=' '*(35-len(ln))

                 ss1=''
                 if len(lr)<30: ss1=' '*(30-len(lr))

                 s=ln+ss+'  ('+lr+')'
                 if ld!='': s+=ss1+'  '+ld

              ck.out(s)

              if len(actions)>0:
                 ck.out('')
                 for q in sorted(actions):
                     qq=actions[q]
                     qd=qq.get('desc','')
                     ck.out('  * '+q+' - '+qd)


    if html:
       h+='</table>\n'

    return {'return':0, 'html':h}
