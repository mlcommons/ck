#
# Collective Knowledge (platform - Neural Processing Unit)
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
# Detect Neural Network Accelerator

def detect(i):
    """
    Input:  {
              (target)               - if specified, use info from 'machine' module

              (host_os)              - host OS (detect, if omitted)
              (os) or (target_os)    - OS module to check (if omitted, analyze host)

              (device_id)            - device id if remote (such as adb)
              (skip_device_init)     - if 'yes', do not initialize device
              (print_device_info)    - if 'yes', print extra device info

              (skip_info_collection) - if 'yes', do not collect info (particularly for remote)

              (skip_print_os_info)   - if 'yes', do not print OS info

              (exchange)             - if 'yes', exchange info with some repo (by default, remote-ck)
              (share)                - the same as 'exchange'
              (exchange_repo)        - which repo to record/update info (remote-ck by default)
              (exchange_subrepo)     - if remote, remote repo UOA
              (exchange_locally)     - if 'yes', exchange locally

              (extra_info)           - extra info about author, etc (see add from CK kernel)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              features = {
                npun         - NPU features (properties), unified
                npu_misc     - assorted NPU features (properties), platform dependent
              }
            }

    """

    import os

    o=i.get('out','')

    oo=''
    if o=='con': oo=o

    # Check if target
    if i.get('target','')!='':
       r=ck.access({'action':'init',
                    'module_uoa':cfg['module_deps']['machine'],
                    'input':i})
       if r['return']>0: return r

    # Various params
    hos=i.get('host_os','')
    tos=i.get('target_os','')
    if tos=='': tos=i.get('os','')
    tdid=i.get('device_id','')

    sic=i.get('skip_info_collection','')
    sdi=i.get('skip_device_init','')
    pdv=i.get('print_device_info','')

    ex=i.get('exchange','')
    if ex=='': ex=i.get('share','')

    einf=i.get('extra_info','')
    if einf=='': einf={}

    # Get OS info
    import copy
    ii=copy.deepcopy(i)
    ii['out']=oo
    if i.get('skip_print_os_info','')=='yes': ii['out']=''
    ii['action']='detect'
    ii['module_uoa']=cfg['module_deps']['platform.cpu']
    rr=ck.access(ii) # DO NOT USE rr further - will be reused as return !
    if rr['return']>0: return rr

    hos=rr['host_os_uid']
    hosx=rr['host_os_uoa']
    hosd=rr['host_os_dict']

    tos=rr['os_uid']
    tosx=rr['os_uoa']
    tosd=rr['os_dict']

    tbits=tosd.get('bits','')

    tdid=rr['device_id']

    # Some params
    ro=tosd.get('redirect_stdout','')
    remote=tosd.get('remote','')
    win=tosd.get('windows_base','')

    stdirs=tosd.get('dir_sep','')

    dv=''
    if tdid!='': dv=' -s '+tdid

    # Init
    prop={}
    prop_all={}
    props=[]

    target_npu_name=''
    target_npu_vendor=''

    # Get info about NPUs ######################################################
    if win=='yes':
       return {'return':1, 'error':'Windows is not yet supported'}

    r=ck.access({'action':'run_and_get_stdout',
                 'module_uoa':cfg['module_deps']['os'],
                 'cmd': ['lsusb', '-v']})
    if r['return']>0: return r

    s=r['stdout'].split('\n')

    manufacturer=''
    product=''

    for q in s:
        q1=q.strip()
        if q1!='':
           j=q1.find(' ')
           if j>0:
              q2=q1[:j]
              q3=q1[j+1:].strip()
              if q2=='iManufacturer':
                 # Check known
                 if q3.lower().find('movidius')>=0:
                    manufacturer=q3[2:].strip()
                    product=''
              elif q2=='iProduct' and manufacturer!='':
                 product=q3[2:].strip()

                 jj={'name':product,
                     'vendor':manufacturer}

                 props.append(jj)

                 product=''
                 manufacturer=''

    # Check if need to select device and platform
    rr={'return':0, 'features':{'npu':props}}

    if len(props)==0 and o=='con':
       ck.out('')
       ck.out('WARNING: no CK-compatible NPU devices found ...')

    fuoa=''
    fuid=''

    # Exchanging info #################################################################
    if ex=='yes':
       er=i.get('exchange_repo','')
       esr=i.get('exchange_subrepo','')
       el=i.get('exchange_locally','')
       if el!='yes' and er=='': 
          er=ck.cfg['default_exchange_repo_uoa']
          esr=ck.cfg['default_exchange_subrepo_uoa']

       for j in range(0, len(props)):
           prop=props[j]
           xn=prop.get('name','')

           if o=='con':
              ck.out('')
              ck.out('Exchanging information with '+er+' repository for a unique NPU '+xn+' ...')

           ii={'action':'exchange',
               'module_uoa':cfg['module_deps']['platform'],
               'sub_module_uoa':work['self_module_uid'],
               'repo_uoa':er,
               'data_name':xn,
               'extra_info':einf,
               'all':'no',
               'dict':{'features':prop}}
           if esr!='': ii['remote_repo_uoa']=esr
           r=ck.access(ii)
           if r['return']>0: return r

           fuoa=r.get('data_uoa','')
           fuid=r.get('data_uid','')

           props[j].update(r['dict'].get('features',{}))

           if o=='con' and r.get('found','')=='yes':
              ck.out('  NPU CK entry already exists ('+fuid+') - loading latest meta (features) ...')

    # Printing
    if o=='con' and len(props)>0:
       for prop in props:
          ck.out('')
          ck.out('NPU name:   '+prop.get('name',''))
          ck.out('NPU vendor: '+prop.get('vendor',''))

    # Finalize features
    if fuoa!='' or fuid!='':
       rr['features']['npu_uoa']=fuoa
       rr['features']['npu_uid']=fuid

    return rr

##############################################################################
# set frequency

def set_freq(i):
    """
    Input:  {
              (host_os)              - host OS (detect, if omitted)
              (os) or (target_os)    - OS module to check (if omitted, analyze host)

              (device_id)            - device id if remote (such as adb)

              (value) = "max" (default)
                        "min"
                        int value
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    o=i.get('out','')
    oo=''
    if o=='con': oo=o

    v=i.get('value','')
    if v=='': v='max'

    # Various params
    hos=i.get('host_os','')
    tos=i.get('target_os','')
    if tos=='': tos=i.get('os','')
    tdid=i.get('device_id','')

    # Get OS info
    import copy
    ii=copy.deepcopy(i)
    ii['out']=''
    ii['action']='detect'
    ii['module_uoa']=cfg['module_deps']['platform.os']
    ii['skip_info_collection']='yes'
    ii['skip_device_init']='yes'
    rr=ck.access(ii)
    if rr['return']>0: return rr

    hos=rr['host_os_uid']
    hosx=rr['host_os_uoa']
    hosd=rr['host_os_dict']

    tos=rr['os_uid']
    tosx=rr['os_uoa']
    tosd=rr['os_dict']

    tbits=tosd.get('bits','')

    tdid=rr['device_id']

    dir_sep=tosd.get('dir_sep','')

    remote=tosd.get('remote','')

    return {'return':1, 'error':'under construction ...'}

##############################################################################
# viewing entries as html

def show(i):
    """
    Input:  {
              data_uoa
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              html         - generated HTML
            }

    """


    h='<h2>Neural Network Accelerators participating in crowd-tuning</h2>\n'

    h+='<i>Reuse/extend <a href="https://github.com/ctuning/ck-crowdtuning-platforms/tree/master/platform.npu">CK JSON meta information</a> of these Neural Processing Units using "ck pull repo:ck-crowdtuning-platforms" ...</i><br><br>\n'

    h+='<table class="ck_table" border="0" cellpadding="6" cellspacing="0">\n'

    # Check host URL prefix and default module/action
    rx=ck.access({'action':'form_url_prefix',
                  'module_uoa':'wfe',
                  'host':i.get('host',''), 
                  'port':i.get('port',''), 
                  'template':i.get('template','')})
    if rx['return']>0: return rx
    url0=rx['url']

    h+=' <tr style="background-color:#cfcfff;">\n'
    h+='  <td><b>\n'
    h+='   #\n'
    h+='  </b></td>\n'
    h+='  <td><b>\n'
    h+='   Vendor\n'
    h+='  </b></td>\n'
    h+='  <td><b>\n'
    h+='   Name\n'
    h+='  </b></td>\n'
    h+='  <td><b>\n'
    h+='   Notes\n'
    h+='  </b></td>\n'
    h+='  <td><b>\n'
    h+='   <a href="'+url0+'wcid='+work['self_module_uoa']+':">CK UID</a>\n'
    h+='  </b></td>\n'
    h+=' </tr>\n'

    ruoa=i.get('repo_uoa','')
    muoa=work['self_module_uoa']
    duoa=i.get('data_uoa','')

    r=ck.access({'action':'search',
                 'module_uoa':muoa,
                 'data_uoa':duoa,
                 'repo_uoa':ruoa,
                 'add_info':'yes',
                 'add_meta':'yes'})
    if r['return']>0: 
       return {'return':0, 'html':'Error: '+r['error']}

    lst=r['lst']

    num=0
    for q in sorted(lst, key = lambda x: (x.get('meta',{}).get('features',{}).get('vendor','').upper(), \
                                          x.get('meta',{}).get('features',{}).get('name','').upper())):

        num+=1

        duoa=q['data_uoa']
        duid=q['data_uid']

        meta=q['meta']
        ft=meta.get('features',{})

        ecid=meta.get('extra_cid','')
        notes=meta.get('notes','')

        if ecid!='':
           if notes!='':
              notes+='\n<br><br>\n'
           notes+='<a href="'+url0+'wcid='+ecid+'">Extra description</a>\n'

        vendor=ft.get('vendor','')
        name=ft.get('name','')

        h+=' <tr>\n'
        h+='  <td valign="top">\n'
        h+='   '+str(num)+'\n'
        h+='  </td>\n'
        h+='  <td valign="top">\n'
        h+='   '+vendor+'\n'
        h+='  </td>\n'
        h+='  <td valign="top">\n'
        h+='   '+name+'\n'
        h+='  </td>\n'
        h+='  <td valign="top">\n'
        h+='   '+notes+'\n'
        h+='  </td>\n'
        h+='  <td valign="top">\n'
        h+='   <a href="'+url0+'wcid='+work['self_module_uoa']+':'+duid+'">'+duid+'</a>\n'
        h+='  </td>\n'
        h+=' </tr>\n'

    h+='</table><br><br>\n'

    return {'return':0, 'html':h}

##############################################################################
# browse platform.npu participated in experiment crowdsourcing (crowd-benchmarking and crowd-tuning)

def browse(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    # TBD: should calculate url
    url='https://github.com/ctuning/ck-crowdtuning-platforms/tree/master/platform.npu'

    import webbrowser
    webbrowser.open(url)

    import time
    time.sleep(3)

    url='http://cknowledge.org/repo/web.php?action=index&module_uoa=wfe&native_action=show&native_module_uoa=platform.npu'

    import webbrowser
    webbrowser.open(url)

    return {'return':0}
