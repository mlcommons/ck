#
# Collective Knowledge (platform detection)
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
sep='***************************************************************************************'

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
# collect info about platforms

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

              (exchange)             - if 'yes', exchange info with some repo (by default, remote-ck)
              (share)                - the same as 'exchange'
              (exchange_repo)        - which repo to record/update info (remote-ck by default)
              (exchange_subrepo)     - if remote, remote repo UOA
              (exchange_locally)     - if 'yes', exchange locally

              (force_platform_name)  - if !='', use this for platform name

              (extra_info)           - extra info about author, etc (see add from CK kernel)

              (quiet)                - do not ask questions whenever possible
              (skip_gpu_info)        - if 'yes', do not collect GPU info
              (platform_init_uoa)    - if !='', use these platform.init scripts
              (update_platform_init) - update platform.init scripts (ask user)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              host_os_uoa                 - host OS UOA
              host_os_uid                 - host OS UID
              host_os_dict                - host OS meta

              os_uoa                      - target OS UOA
              os_uid                      - target OS UID
              os_dict                     - target OS meta

              (devices)                   - return devices if device_id==''
              (device_id)                 - if device_id=='' and only 1 device, select it

              features = {
                cpu            - CPU features (properties), unified
                cpu_misc       - assorted CPU features (properties), platform dependent

                os             - OS features (properties), unified
                os_misc        - assorted OS features (properties), platform dependent

                platform       - platform features (properties), unified
                platform_misc  - assorted platform features (properties), platform dependent

                gpu            - GPU features (properties), unified
                gpu_misc       - assorted GPU features (properties), platform dependent
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

    device_cfg=i.get('device_cfg',{})

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

    quiet=i.get('quiet','')
    sgi=i.get('skip_gpu_info','')
    piuoa=i.get('platform_init_uoa','')

    einf=i.get('extra_info','')
    if einf=='': einf={}

    # If exchange, check that repo from this env is cached and recache if needed
    el=i.get('exchange_locally','')
    if el!='yes' and ex=='yes':
       er=i.get('exchange_repo','')

       if er!='':
          rx=ck.load_repo_info_from_cache({'repo_uoa':er})
          if rx['return']>0: 
             if o=='con':
                ck.out('')
                ck.out('It appears that CK remote repo ('+er+') is not in CK cache - recaching ...')

             rx=ck.access({'action':'recache',
                           'module_uoa':cfg['module_deps']['repo']})
             if rx['return']>0: return rx

    # Get OS info ###############################################################
    if oo=='con': 
       ck.out(sep)
       ck.out('Detecting OS and CPU features ...')

    import copy
    ii=copy.deepcopy(i)
    ii['out']=oo
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

    tosd.update(device_cfg.get('update_target_os_dict',{}))

    tbits=tosd.get('bits','')

    tdid=rr['device_id']

    # Some params
    ro=tosd.get('redirect_stdout','')
    win=tosd.get('windows_base','')

    dv=''
    if tdid!='': dv=' -s '+tdid

    spd=tosd.get('skip_platform_detection','')
    if spd=='yes':
       sgi='yes'

    # Init
    prop={}
    prop_all={}

    xos=rr['os_uoa']
    device_id=rr['device_id']

    os_uoa=rr['os_uoa']
    os_uid=rr['os_uid']
    os_dict=rr['os_dict']

    remote=os_dict.get('remote','')
    remote_ssh=os_dict.get('remote_ssh','')
    os_win=os_dict.get('windows_base','')
    os_mac=os_dict.get('macos','')

    ro=os_dict.get('redirect_stdout','')

    # Get GPU info ####################################################
    if sgi!='yes':
       if oo=='con': 
          ck.out(sep)
          ck.out('Detecting GPU features ...')

       import copy
       ii=copy.deepcopy(i)
       ii['out']=oo
       ii['skip_print_os_info']='yes'
       ii['action']='detect'
       ii['module_uoa']=cfg['module_deps']['platform.gpu']
       rx=ck.access(ii) # DO NOT USE rr further - will be reused as return !
       if rx['return']>0: return rx

       # Merge with other features
       ry=ck.merge_dicts({'dict1':rr, 'dict2':rx})
       if ry['return']>0: return ry
       rr=ry['dict1']

    # Get info about system ######################################################
    if oo=='con': 
       ck.out(sep)
       ck.out('Detecting system features ...')

    if remote=='yes' and remote_ssh!='yes':
       params={}

       rx=ck.gen_tmp_file({'prefix':'tmp-ck-'})
       if rx['return']>0: return rx
       fn=rx['file_name']

       x=tosd.get('adb_all_params','')
       x=x.replace('$#redirect_stdout#$', ro)
       x=x.replace('$#output_file#$', fn)

       dv=''
       if tdid!='': dv=' -s '+tdid
       x=x.replace('$#device#$',dv)

       if o=='con' and pdv=='yes':
          ck.out('')
          ck.out('Receiving all parameters:')
          ck.out('  '+x)

       rx=os.system(x)
       if rx!=0:
          if o=='con':
             ck.out('')
             ck.out('Non-zero return code :'+str(rx)+' - likely failed')
          return {'return':1, 'error':'access to remote device failed'}

       # Read and parse file
       rx=ck.load_text_file({'text_file':fn, 'split_to_list':'yes', 'delete_after_read':'yes'})
       if rx['return']>0: return rx
       ll=rx['lst']

       for s in ll:
           s1=s.strip()

           q2=s1.find(']: [')
           k=''
           if q2>=0:
              k=s1[1:q2].strip()
              v=s1[q2+4:].strip()
              v=v[:-1].strip()

              params[k]=v

       prop_all['adb_params']=params

#       for q in params:
#           v=params[q]
#           print q+'='+v

       model=params.get('ro.product.model','')
       manu=params.get('ro.product.manufacturer','')
       if model!='' and manu!='':
          if model.lower().startswith(manu.lower()):
             model=model[len(manu)+1:]

       if manu=='' and model!='': manu=model

       manu=manu.upper()
       model=model.upper()

       prop['name']=manu
       if model!='': prop['name']+=' '+model
       prop['model']=model
       prop['vendor']=manu
    elif spd!='yes':
       x1=''
       x2=''

       target_system_model=''
       target_name=''

       if os_win=='yes':
          r=get_from_wmic({'group':'csproduct',
                           'remote_shell':tosd.get('remote_shell','').replace('$#device#$',dv),
                           'remote_shell_end':tosd.get('remote_shell_end','')})
          if r['return']>0: return r
          info1=r['dict']

          x1=info1.get('Vendor','')
          x2=info1.get('Version','')

          target_name=x1+' '+x2

          r=get_from_wmic({'cmd':'computersystem get model',
                           'remote_shell':tosd.get('remote_shell','').replace('$#device#$',dv),
                           'remote_shell_end':tosd.get('remote_shell_end','')})
          if r['return']>0: return r
          target_system_model=r['value']

          prop_all['cs_product']=info1
       elif os_mac=='yes':
          ################################################### Obtaining info on MacOS (including remote)
          cmd=['system_profiler', 'SPHardwareDataType']

          if remote_ssh=='yes':
             cmd=tosd.get('remote_shell','').replace('$#device#$',dv)+' system_profiler SPHardwareDataType '+tosd.get('remote_shell_end','')

          r=ck.access({'action':'run_and_get_stdout',
                       'module_uoa':cfg['module_deps']['os'],
                       'cmd': cmd})
          if r['return']>0: return r

          x1='Apple Inc.'

          for line in r['stdout'].splitlines():
            if ':' in line:
              left, right = line.split(':', 1)
              left = left.strip().lower()
              if left == 'model name':
                target_name = right.strip()
              if left == 'model identifier':
                target_system_model = right.strip()
              if target_name!='' and target_system_model!='':
                break

       else:
          ################################################### Obtaining info on Linux (including remote)
          cmd=['cat', '/sys/devices/virtual/dmi/id/sys_vendor']

          if remote_ssh=='yes':
             cmd=tosd.get('remote_shell','').replace('$#device#$',dv)+' cat /sys/devices/virtual/dmi/id/sys_vendor '+tosd.get('remote_shell_end','')

          r=ck.access({'action':'run_and_get_stdout',
                       'module_uoa':cfg['module_deps']['os'],
                       'cmd': cmd})
          if r['return']>0: return r
          if r['stdout'].strip()!='': x1=r['stdout'].strip()

          cmd=['cat', '/sys/devices/virtual/dmi/id/product_version']

          if remote_ssh=='yes':
             cmd=tosd.get('remote_shell','').replace('$#device#$',dv)+' cat /sys/devices/virtual/dmi/id/product_version '+tosd.get('remote_shell_end','')

          r=ck.access({'action':'run_and_get_stdout',
                       'module_uoa':cfg['module_deps']['os'],
                       'cmd': cmd})
          if r['return']>0: return r
          if r['stdout'].strip()!='': x2=r['stdout'].strip()

          if x1!='' and x2!='':
             target_name=x1+' '+x2

          cmd=['cat', '/sys/devices/virtual/dmi/id/product_name']

          if remote_ssh=='yes':
             cmd=tosd.get('remote_shell','').replace('$#device#$',dv)+' cat /sys/devices/virtual/dmi/id/product_name '+tosd.get('remote_shell_end','')

          r=ck.access({'action':'run_and_get_stdout',
                       'module_uoa':cfg['module_deps']['os'],
                       'cmd': cmd})
          if r['return']>0: return r
          if r['stdout'].strip()!='': target_system_model=r['stdout'].strip()

          #############################################################################################################
          # If empty, try platform specific probes (for now here and later maybe in separate platform-specific scripts)
          if target_name=='' and target_system_model=='':
             # Check RPi
             fail=False
             try:
                import RPi.GPIO as GPIO
             except Exception as e:
                fail=True

             if not fail:
                try:
                   rpi=GPIO.RPI_INFO
                   x1=rpi.get('MANUFACTURER','')
                   target_name='Raspberry Pi'
                   target_system_model='Raspberry '+rpi.get('TYPE','')
                except Exception as e: 
                   pass

          if target_name=='' and target_system_model=='':
             # Check via /proc/device-tree/model
             rx=ck.load_text_file({'text_file':'/proc/device-tree/model'})
             if rx['return']==0:
                target_system_model=rx['string'].strip()
                zz1=target_system_model.split(' ')
                if len(zz1)>0:
                   x1=zz1[0]

       prop['vendor']=x1
       if target_name=='' and x1!='': target_name=x1
       prop['name']=target_name
       if target_system_model!='': prop['name']+=' ('+target_system_model+')'
       prop['model']=target_system_model

       fpn=i.get('force_platform_name','')
       if fpn!='':
          prop['name']=fpn

    if o=='con':
       ck.out('')
       ck.out('Platform name:   '+prop.get('name',''))
       ck.out('Platform vendor: '+prop.get('vendor',''))
       ck.out('Platform model:  '+prop.get('model',''))

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

       if o=='con':
          ck.out('')
          ck.out('Exchanging information with '+er+' repository ...')

       xn=prop.get('name','')
       if xn=='':
          # Check if exists in configuration

          dcfg={}
          ii={'action':'load',
              'module_uoa':cfg['module_deps']['cfg'],
              'data_uoa':cfg['cfg_uoa']}
          r=ck.access(ii)
          if r['return']>0 and r['return']!=16: return r
          if r['return']!=16:
             dcfg=r['dict']

          dx=dcfg.get('platform_name',{}).get(tos,{})
          x=tdid
          if x=='': x='default'
          xn=dx.get(x,'')

          if (xn=='' and o=='con'):
             r=ck.inp({'text':'Enter your platform name (for example Samsung Chromebook 2, Huawei Ascend Mate 7, IBM SyNAPSE): '})
             xxn=r['string'].strip()

             if xxn!=xn:
                xn=xxn

                if 'platform_name' not in dcfg: dcfg['platform_name']={}
                if tos not in dcfg['platform_name']: dcfg['platform_name'][tos]={}
                dcfg['platform_name'][tos][x]=xn

                ii={'action':'update',
                    'module_uoa':cfg['module_deps']['cfg'],
                    'data_uoa':cfg['cfg_uoa'],
                    'dict':dcfg}
                r=ck.access(ii)
                if r['return']>0: return r

          if xn=='':
             return {'return':1, 'error':'can\'t exchange information where main name is empty'}

          ixn=xn.find(' ')
          if ixn>0: 
             xx=xn[:ixn].strip()
             prop['vendor']=xx
             prop['model']=xn[ixn+1:].strip()

          prop['name']=xn

       ii={'action':'exchange',
           'module_uoa':work['self_module_uid'],
           'sub_module_uoa':work['self_module_uid'],
           'repo_uoa':er,
           'data_name':prop.get('name',''),
           'extra_info':einf,
           'all':'yes',
           'dict':{'features':prop}} # Later we should add more properties from prop_all,
                                     # but should be careful to remove any user-specific info
       if esr!='': ii['remote_repo_uoa']=esr
       r=ck.access(ii)
       if r['return']>0: return r

       fuoa=r.get('data_uoa','')
       fuid=r.get('data_uid','')

       prop=r['dict'].get('features',{})

       if o=='con' and r.get('found','')=='yes':
          ck.out('  Platform CK entry already exists ('+fuid+') - loading latest meta (features) ...')

    if 'features' not in rr: rr['features']={}

    rr['features']['platform']=prop
    rr['features']['platform_misc']=prop_all

    if fuoa!='' or fuid!='':
       rr['features']['platform_uoa']=fuoa
       rr['features']['platform_uid']=fuid

    return rr

##############################################################################
# Get info from WMIC on Windows

def get_from_wmic(i):
    """
    Input:  {
              cmd     - cmd for wmic
              (group) - get the whole group

              (remote_shell)     - remote shell prefix if needed
              (remote_shell_end) - remote shell suffix if needed
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              value        - obtained value
              (dict)       - if group
            }

    """

    import os

    value=''
    dd={}

    rs=i.get('remote_shell','')
    rse=i.get('remote_shell_end','')

    xcmd=i.get('cmd','')
    xgroup=i.get('group','')
    if xgroup!='': xcmd=xgroup

    # We need to use file since it is encoded with UTF-16 so will need to load it with this encoding
    rx=ck.gen_tmp_file({'prefix':'tmp-ck-'})
    if rx['return']>0: return rx
    fn=rx['file_name']

    cmd=rs+' wmic '+xcmd+' '+rse+' > '+fn

    r=os.system(cmd)
    if r!=0:
       return {'return':1, 'error':'command returned non-zero value: '+cmd}

    # Read and parse file
    enc='utf16'
    if rs!='': enc=''

    rx=ck.load_text_file({'text_file':fn, 'encoding':enc, 'split_to_list':'yes'})
    if rx['return']>0: return rx
    ll=rx['lst']

    if os.path.isfile(fn): os.remove(fn)

    if xgroup=='':
       if len(ll)>1:
          value=ll[1].strip()
    else:
       if len(ll)>1:
          kk=ll[0]
          value=ll[1]

          xkeys=kk.split(' ')
          keys=[]
          for q in xkeys:
              if q!='': keys.append(q)

          for q in range(0, len(keys)):
              k=keys[q]

              if q==0: qx=0
              else: 
                 y=' '
                 if q==len(keys)-1: y=''
                 qx=kk.find(' '+k+y)

              if q==len(keys)-1:
                 qe=len(value)
              else:
                 qe=kk.find(' '+keys[q+1]+' ')

              v=value[qx:qe].strip()
              dd[k]=v

    return {'return':0, 'value':value, 'dict':dd}

##############################################################################
# Init remote device

def init_device(i):
    """
    Input:  {
              os_dict      - OS dict to get info about how to init device
              device_id    - ID of the device if more than one
              (key)        - key from OS to use, by default remote_init
                             useful for deinitialization, i.e. use key=remote_deinit
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    o=i.get('out','')

    key=i.get('key','')
    if key=='': key='remote_init'

    osd=i['os_dict']
    tdid=i['device_id'].strip()

    ri=osd.get(key,'')
    if ri!='':
       dv=''
       if tdid!='': dv=' -s '+tdid
       ri=ri.replace('$#device#$',dv)

       if o=='con':
          ck.out('Initializing remote device:')
          ck.out('')
          ck.out('  '+ri)

       rx=os.system(ri)
       if rx!=0:
          if o=='con':
             ck.out('')
             ck.out('Non-zero return code :'+str(rx)+' - likely failed')
          return {'return':1, 'error':'remote device initialization failed'}

       device_init='yes'

    return {'return':0}

##############################################################################
# exchange properties

def exchange(i):
    """
    Input:  {
              sub_module_uoa - module to search/exchange
              data_name      - data name to search

              (search_dict)  - search entry by this meta

              (repo_uoa)     - where to record

              (dict)         - dictionary to check/record

              (all)          - if 'yes', check all dict['features'] and add to separate file 

              (extra_info)   - extra info about author, etc (see add from CK kernel)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              dict         - if exists, load updated dict (can be collaboratively extended to add more properties 
                                        (or unique/representative species -> software, hardware, gpu, programs, data sets!)
              (found)      - if 'yes', entry was found
            }

    """

    import os

    ruoa=i.get('repo_uoa','')
    smuoa=i['sub_module_uoa']

    dname=i.get('data_name','')

    dd=i.get('dict',{})
    ddf=dd.get('features',{})

    sd=i.get('search_dict',{})

    al=i.get('all','')

    if dname=='' and len(sd)==0:
       return {'return':1, 'error':'name and search meta are empty in platform information exchange'}

    # Search if already exists (and not only in upload)
    ii={'action':'search',
        'module_uoa':smuoa,
# FGG: I commented next line since we can move 
#      well-known entries to other repositories
#      such as ck-crowdtuning instead of upload
#       'repo_uoa':ruoa,
        'ignore_case':'yes'}
    if dname!='':
       ii['search_by_name']=dname
    if len(sd)>0:
       ii['search_dict']=sd

    rx=ck.access(ii)
    if rx['return']>0: return rx
    lst=rx['lst']

    if len(lst)==0:
       ei=i.get('extra_info',{})

       # Add info
       rx=ck.access({'action':'add',
                     'module_uoa':smuoa,
                     'repo_uoa':ruoa,
                     'data_name':dname,
                     'dict':dd,
                     'extra_info':ei,
                     'sort_keys':'yes'})

    else:
       # Load
       ll=lst[0]
       duoa=ll.get('data_uid','')
       xruoa=ll.get('repo_uoa','')
       rx=ck.access({'action':'load',
                     'module_uoa':smuoa,
                     'repo_uoa':xruoa,
                     'data_uoa':duoa})

       rx['found']='yes'

    if rx['return']>0: return rx

    if al=='yes':
       # We also record all info only if forced to do so
       #  by CK local kernel configuration. It is needed to aggregate
       #  such info on experiment crowdsourcing servers
       #  and then share this info via GitHub,
       #  but not locally, otherwise it will be a mess...

       rap=ck.cfg.get('record_all_platform_info','')
#          if rap=='yes':
#
#             # Not parallel usage safe (on the other hand, will not loose too much at the moment) ...
#
#             # Check if extra parameters are saved
#             p=rx['path']
#             p1=os.path.join(p, 'all.json')
#
#             d={'all':[]}
#             toadd=True
#
#             touched=0
#
#             if os.path.isfile(p1):
#                ry=ck.load_json_file({'json_file':p1})
#                if ry['return']>0: return ry
#                d=ry['dict']
#
#                touched=d.get('touched',0)
#                touched+=1
#
#                if 'all' not in d: d['all']=[]
#                dall=d.get('all',[])
#
#                for q in dall:
#                    rz=ck.compare_dicts({'dict1':q, 'dict2':ddf})
#                    if rz['return']>0: return rz
#                    if rz['equal']=='yes':
#                       toadd=False
#                       break
#
#             d['touched']=touched
#
#             if toadd:
#                d['all'].append(ddf)
#
#             rz=ck.save_json_to_file({'json_file':p1, 'dict':d})
#             if rz['return']>0: return rz

    return rx

##############################################################################
# deinitialize device (put to powersave mode)

def deinit(i):
    """
    Input:  {
              (target)               - target machine if needed (to correctly handle remote execution)

              (host_os)              - host OS (detect, if omitted)
              (os) or (target_os)    - OS module to check (if omitted, analyze host)
              (device_id)            - device id if remote (such as adb)
              (key)                  - {'remote_init' or 'remote_deinit'}
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')

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

    # Get OS info
    import copy
    ii=copy.deepcopy(i)
    ii['out']=o
    ii['action']='detect'
    ii['skip_device_init']='yes'     # consider that device was already initialized
    ii['skip_info_collection']='yes'
    ii['module_uoa']=cfg['module_deps']['platform.os']
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

    key=i.get('key','')
    if key=='': key='remote_deinit'

    ii={'os_dict':tosd,
        'device_id':tdid,
        'key':key,
        'out':o}
    return init_device(ii)

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


    h='<h2>Platforms participating in crowd-tuning</h2>\n'

    h+='<i>Reuse/extend <a href="https://github.com/ctuning/ck-crowdtuning-platforms/tree/master/platform">CK JSON meta information</a> of these platforms using "ck pull repo:ck-crowdtuning-platforms" ...</i><br><br>\n'

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
    h+='   Model\n'
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
                                          x.get('meta',{}).get('features',{}).get('model','').upper())):

        num+=1

        duoa=q['data_uoa']
        duid=q['data_uid']

        meta=q['meta']
        ft=meta.get('features',{})

        name=ft.get('name','')
        vendor=ft.get('vendor','')
        model=ft.get('model','')

        h+=' <tr>\n'
        h+='  <td valign="top">\n'
        h+='   '+str(num)+'\n'
        h+='  </td>\n'
        h+='  <td valign="top">\n'
        h+='   '+vendor+'\n'
        h+='  </td>\n'
        h+='  <td valign="top">\n'
        h+='   '+model+'\n'
        h+='  </td>\n'
        h+='  <td valign="top">\n'
        h+='   <a href="'+url0+'wcid='+work['self_module_uoa']+':'+duid+'">'+duid+'</a>\n'
        h+='  </td>\n'
        h+=' </tr>\n'


    h+='</table><br><br>\n'

    return {'return':0, 'html':h}

##############################################################################
# browse platforms participated in experiment crowdsourcing (crowd-benchmarking and crowd-tuning)

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
    url='https://github.com/ctuning/ck-crowdtuning-platforms/tree/master/platform'

    import webbrowser
    webbrowser.open(url)

    import time
    time.sleep(3)

    url='http://cknowledge.org/repo/web.php?action=index&module_uoa=wfe&native_action=show&native_module_uoa=platform'

    import webbrowser
    webbrowser.open(url)

    return {'return':0}
