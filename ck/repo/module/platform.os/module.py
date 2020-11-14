#
# Collective Knowledge (platform - OS)
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
# detect OS

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

              (extra_info)           - extra info about author, etc (see add from CK kernel)

              (return_multi_devices) - if 'yes' and multiple devices detected, return error=32 and devices

              (platform_init_uoa)    - if !='', use these platform.init scripts

              (quiet)                - if 'yes', do not ask questions (TBD: need to check that fully works)
            }

    Output: {
              return                - return code =  0, if successful
                                                  >  0, if error
              (error)               - error text if return > 0

              host_os_uoa            - host OS UOA
              host_os_uid            - host OS UID
              host_os_dict           - host OS meta

              os_uoa                 - target OS UOA
              os_uid                 - target OS UID
              os_dict                - target OS meta

              features = {
                os                   - OS features (properties), unified
                os_misc              - assorted OS features (properties), platform dependent
              }

              (devices)              - return devices if device_id==''
              (device_id)            - if device_id=='' and only 1 device, select it

              (host_add_path)          - list of paths to add before executing host tools ...
              (host_add_path_string)   - adding paths to PATH environment in a host OS format

              (target_add_path)        - list of paths to add before executing target tools ...
              (target_add_path_string) - adding paths to PATH environment in a target OS format

              (update_platform_init)   - update platform.init scripts (ask user)
            }

    """

    import os

    quiet=i.get('quiet','')

    o=i.get('out','')
    oo=''
    if o=='con': oo=o
    else: quiet='yes'

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

    tosd=i.get('target_os_dict',{})

    sic=i.get('skip_info_collection','')
    sdi=i.get('skip_device_init','')
    pdv=i.get('print_device_info','')

    piuoa=i.get('platform_init_uoa','')

    ex=i.get('exchange','')
    if ex=='': ex=i.get('share','')

    einf=i.get('extra_info','')
    if einf=='': einf={}

    # Detect and find most close host OS or load already existing one
    r=ck.access({'action':'find_close',
                 'module_uoa':cfg['module_deps']['os'],
                 'os_uoa':hos})
    if r['return']>0: return r

    hos=r['os_uid']
    hosx=r['os_uoa']
    hosd=r['os_dict']

    hadd_path=r.get('add_path',[])
    hadd_path_string=''
    tadd_path=[]
    tadd_path_string=''

    # Check/detect target OS
    r=ck.access({'action':'find_close',
                 'module_uoa':cfg['module_deps']['os'],
                 'os_uoa':tos,
                 'os_dict':tosd})
    if r['return']>0: return r

    tos=r['os_uid']
    tosx=r['os_uoa']
    tosd=r['os_dict']
    tosd.update(device_cfg.get('update_target_os_dict',{}))

    tp=tosd.get('ck_name','')
    tbits=tosd.get('bits','')

    remote=tosd.get('remote','')
    remote_ssh=tosd.get('remote_ssh','')
    win=tosd.get('windows_base','')
    mac=tosd.get('macos','')

    # Init params
    prop={}
    prop_all={}
    devices=[]

    prop_os_name=''
    prop_os_name_long=''
    prop_os_name_short=''
    prop_os_abi=''

    prop_serial_no=''

    ro=hosd.get('redirect_stdout','')

    if tosd.get('skip_platform_detection','')=='yes':
       sic='yes'

    # Check devices, if remote
    if sic!='yes' and remote=='yes' and tdid=='':
       # Get devices
       rx=ck.gen_tmp_file({'prefix':'tmp-ck-'})
       if rx['return']>0: return rx
       fn=rx['file_name']

       x=tosd.get('adb_devices','')
       if x!='':
          # Check that adb is installed (but should actually later use path)
          ii={'action':'resolve',
              'module_uoa':cfg['module_deps']['env'],
              'host_os':hos,
              'target_os':tos,
              'device_id':tdid,
              'deps':{
                'adb':{
                       "force_target_as_host": "yes",
                       "local": "yes", 
                       "name": "adb tool", 
                       "sort": -10, 
                       "tags": "tool,adb"
                      }
              },
              'add_customize':'yes',
              'quiet':quiet,
              'out':oo}
          rx=ck.access(ii)
          if rx['return']>0: return rx

          # Continue obtaining params
          x=x.replace('$#redirect_stdout#$', ro)
          x=x.replace('$#output_file#$', fn)

          if o=='con' and pdv=='yes':
             ck.out('')
             ck.out('Receiving list of devices:')
             ck.out('  '+x)

          rx=os.system(x)
          if rx!=0:
             return {'return':1, 'error':'access to remote device failed (return code='+str(rx)+')'}

          # Read and parse file
          rx=ck.load_text_file({'text_file':fn, 
                                'split_to_list':'yes',
                                'delete_after_read':'yes'})
          if rx['return']>0: return rx
          ll=rx['lst']

          devices=[]
          for q in range(1, len(ll)):
              s1=ll[q].strip()
              if s1!='':
                 q2=s1.find('\t')
                 if q2>0:
                    s2=s1[0:q2]
                    devices.append(s2)

          if len(devices)==0:
             return {'return':16, 'error':'no attached remoted devices found'}

          if o=='con':
             ck.out('')
             ck.out('Available remote devices:')
             for q in devices:
                 ck.out('  '+q)
             ck.out('')

          if tdid=='':
             if len(devices)==1:
                tdid=devices[0]
             else:
                if o=='con' and i.get('return_multi_devices','')!='yes':
                   ck.out('')
                   for j in range(0, len(devices)):
                       zs=str(j)
                       ck.out(zs+') '+devices[j])

                   ck.out('')
                   rx=ck.inp({'text':'Select one of the options for device or press Enter to select 0: '})
                   s=rx['string']
                   x=0
                   if s!='':
                      x=int(s.strip())

                   if x<0 or x>=len(devices):
                      return {'return':1, 'error':'option is not recognized'}

                   tdid=devices[x]
                else:
                   return {'return':32, 'error':'more than one remote device - specify via --device_id', 'devices':devices}

    # Collect additional info unless skipped
    if sic!='yes':
       if remote=='yes' and remote_ssh!='yes':
          # Initialized device if needed
          if sdi!='yes':
             remote_init=tosd.get('remote_init','')
             if remote_init!='':
                r=ck.access({'action':'init_device',
                             'module_uoa':cfg['module_deps']['platform'],
                             'os_dict':tosd,
                             'device_id':tdid})
                if r['return']>0: return r

          # Prepare ADB target device ID
          dv=''
          if tdid!='': dv=' -s '+tdid

          rx=ck.gen_tmp_file({'prefix':'tmp-ck-'})
          if rx['return']>0: return rx
          fn=rx['file_name']

          # Check serial number if needed
          x=tosd.get('adb_serial_no','')
          if x!='':
             x=x.replace('$#redirect_stdout#$', ro)
             x=x.replace('$#output_file#$', fn)
             x=x.replace('$#device#$',dv)

             if o=='con' and pdv=='yes':
                ck.out('')
                ck.out('Obtaining serial number:')
                ck.out('  '+x)

             rx=os.system(x)
             if rx!=0:
                if o=='con':
                   ck.out('')
                   ck.out('Non-zero return code :'+str(rx)+' - likely failed')
                return {'return':1, 'error':'access to remote device failed'}

             # Read and parse file
             rx=ck.load_text_file({'text_file':fn, 'split_to_list':'no', 'delete_after_read':'yes'})
             if rx['return']>0: return rx
             prop_serial_no=rx['string'].strip()

          # Get all params
          params={}

          x=tosd.get('adb_all_params','')
          if x!='':
             x=x.replace('$#redirect_stdout#$', ro)
             x=x.replace('$#output_file#$', fn)
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

             prop_os_name='Android '+params.get('ro.build.version.release','')

          # Get proc version
          # Reuse fn as tmp name

          x=tosd['remote_shell']+' cat /proc/version '+tosd.get('remote_shell_end','')+' '+ro+' '+fn
          x=x.replace('$#device#$',dv)

          if o=='con' and pdv=='yes':
             ck.out('')
             ck.out('Receiving /proc/version:')
             ck.out('  '+x)

          rx=os.system(x)
          if rx==0:
             # Read and parse file
             rx=ck.load_text_file({'text_file':fn, 'split_to_list':'yes', 'delete_after_read':'yes'})
             if rx['return']>0: return rx
             ll=rx['lst']

             if len(ll)>0:
                prop_os_name_long=ll[0]
                prop_os_name_short=prop_os_name_long

                ix=prop_os_name_long.find(' (')
                if ix>=0:
                   ix1=prop_os_name_long.find('-')
                   if ix1>=0 and ix1<ix: ix=ix1
                   prop_os_name_short=prop_os_name_long[:ix]

       if remote!='yes' or remote_ssh=='yes':

          prop_os_name_long=''
          prop_os_name_short=''

          if remote_ssh!='yes':
             import platform
             prop_os_name_long=platform.platform()
             prop_os_name_short=platform.system()+' '+platform.release()

          if win=='yes':
             if remote_ssh=='yes':
                 cmd=tosd['remote_shell']+'ver'+tosd.get('remote_shell_end','')

                 r=ck.access({'action':'run_and_get_stdout',
                              'module_uoa':cfg['module_deps']['os'],
                              'cmd': cmd, 'shell':'yes'})
                 if r['return']==0:
                     s=r['stdout']

                     j1=s.find('[Version ')
                     if j1>0:
                        j2=s.find(']',j1)
                        s0=s[j1+9:j2]
                        s1=s0.split('.')

                        prop_os_name_short='Windows '+s1[0]
                        prop_os_name_long='Windows-'+s0

                 prop_os_name=prop_os_name_short

                 if prop_os_name=='':
                     return {'return':1, 'error':'can\'t obtain OS version on remote node - likely disconnected or secret key not matching'}

             else:
                # If detected Windows 8, it may be Windows 10 ...
                if prop_os_name_short.find(' 8'):

                   r=ck.gen_tmp_file({})
                   if r['return']>0: return r
                   fn=r['file_name']

                   cmd='ver > '+fn
                   rx=os.system(cmd)
                   if rx==0:
                      r=ck.load_text_file({'text_file':fn, 
                                           'delete_after_read':'yes'})
                      if r['return']==0:
                         s=r['string']
                         j1=s.find('[Version ')
                         if j1>0:
                            j2=s.find(']',j1)
                            s0=s[j1+9:j2]
                            s1=s0.split('.')
                            if len(s1)>0 and s1[0]=='10':
                               prop_os_name_short='Windows 10'
                               prop_os_name_long='Windows-'+s0

                prop_os_name=prop_os_name_short

          elif mac=='yes':
            cmd=['sw_vers']

            if tosd.get('remote_shell','')!='':
               cmd=tosd['remote_shell']+'sw_vers'+tosd.get('remote_shell_end','')

            r=ck.access({'action':'run_and_get_stdout',
                         'module_uoa':cfg['module_deps']['os'],
                         'cmd': cmd})
            if r['return']==0:
              sw_vers={}
              for line in r['stdout'].splitlines():
                if ':' in line:
                  left, right = line.split(':', 1)
                  left = left.strip()
                  right = right.strip()
                  sw_vers[left]=right

              prop_os_name=sw_vers.get('ProductName', '') + ' ' + sw_vers.get('ProductVersion', '')

          else:
             # If Linux, remove extensions after - in a shorter version
             if prop_os_name_long=='':
                 prop_os_name_long=''

                 cmd=tosd['remote_shell']+'uname -s'+tosd.get('remote_shell_end','')

                 r=ck.access({'action':'run_and_get_stdout',
                              'module_uoa':cfg['module_deps']['os'],
                              'cmd': cmd, 'shell':'yes'})
                 if r['return']==0:
                     prop_os_name_long+=r['stdout'].strip()

                 cmd=tosd['remote_shell']+'uname -r'+tosd.get('remote_shell_end','')

                 r=ck.access({'action':'run_and_get_stdout',
                              'module_uoa':cfg['module_deps']['os'],
                              'cmd': cmd, 'shell':'yes'})
                 if r['return']==0:
                     prop_os_name_long+=' '+r['stdout'].strip()

                 prop_os_name_short=prop_os_name_long

             cmd=tosd.get('remote_shell','')+'uname -m'+tosd.get('remote_shell_end','')

             r=ck.access({'action':'run_and_get_stdout',
                          'module_uoa':cfg['module_deps']['os'],
                          'cmd': cmd, 'shell':'no'})
             if r['return']==0:
                 prop_os_abi=r['stdout'].strip()

             x=prop_os_name_short.find('-')
             if x>=0:
                prop_os_name_short=prop_os_name_short[:x]

             if prop_os_name=='':
                #Try to detect via /etc/*-release

                r=ck.gen_tmp_file({})
                if r['return']>0: return r
                fn=r['file_name']

                cmd='cat /etc/*-release'

                if tosd.get('remote_shell','')!='':
                   cmd=tosd['remote_shell']+cmd+tosd.get('remote_shell_end','')

                cmd+=' > '+fn

                rx=os.system(cmd)
                if rx==0:
                   r=ck.load_text_file({'text_file':fn, 
                                        'convert_to_dict':'yes',
                                        'str_split':'=',
                                        'remove_quotes':'yes',
                                        'delete_after_read':'yes'})
                   if r['return']==0:
                      ver=r['dict']
                      prop_os_name=ver.get('DISTRIB_DESCRIPTION', ver.get('PRETTY_NAME',''))

             if prop_os_name=='' and prop_os_name_short!='':
                prop_os_name=prop_os_name_short

    prop['ck_os_uoa']=tosx
    prop['ck_os_base_uoa']=tosd.get('base_uoa','')
    prop['name']=prop_os_name
    prop['name_long']=prop_os_name_long
    prop['name_short']=prop_os_name_short
    prop['abi']=prop_os_abi
    prop['serial_number']=prop_serial_no
    prop['bits']=tbits

    # Check if platform.init is defined for this target (to add target-specific scripts to PATH)
    dcfg={}
    ii={'action':'load',
        'module_uoa':cfg['module_deps']['cfg'],
        'data_uoa':cfg['lcfg_uoa']}
    r=ck.access(ii)
    if r['return']>0 and r['return']!=16: return r
    if r['return']!=16:
       dcfg=r['dict']

    pi_key=tosx
    if remote=='yes' and tdid!='': pi_key='remote-'+tdid
    elif remote_ssh=='yes' and tosd.get('remote_id','')!='': pi_key='remote-'+tosd['remote_id']

    first_time=False
    pi_uoa=dcfg.get('platform_init_uoa',{}).get(pi_key,'')

    if i.get('update_platform_init','')=='yes' or (pi_uoa=='' and sic!='yes'):
       first_time=True
       # Check if there are related platform.init
       tags='os-'+tp
       if remote=='yes' and remote_ssh!='yes':
          if tp=='linux': tags='os-android'
          else: tags+=',remote'

       rx=ck.access({'action':'search',
                     'add_meta':'yes',
                     'module_uoa':cfg['module_deps']['platform.init'],
                     'tags':tags})
       lrx=[]
       if rx['return']==0: 
          lrx=rx['lst']
       if len(lrx)==1:
          pi_uoa=lrx[0]['data_uid']
       elif len(lrx)>1:
            if piuoa!='':
                pi_uoa=piuoa
            elif o=='con':
                # Select platform.init
                ck.out('')
                ck.out('Some support tools and scripts may be available for your target platform in CK:')
                ck.out('')

                plat_options = [ 'Skip selection and do not ask this question again for your target OS']
                data_uids = [ '-' ]
                for z1 in sorted(lrx, key=lambda v: (v.get('meta',{}).get('sort',0),v['data_uoa'])):
                    duid=z1['data_uid']
                    duoa=z1['data_uoa']

                    data_uids.append( duid )
                    plat_options.append( '{} ({})'.format(duoa, duid) )

                select_adict = ck.access({'action': 'select_string',
                                        'module_uoa': 'misc',
                                        'options': plat_options,
                                        'default': '0',
                })
                if select_adict['return']>0: return select_adict

                selected_index = select_adict['selected_index']
                pi_uoa = data_uids[selected_index]

       # Record if new
       if pi_uoa!='':
          if 'platform_init_uoa' not in dcfg:
             dcfg['platform_init_uoa']={}

          dcfg['platform_init_uoa'][pi_key]=pi_uoa

          ii={'action':'update',
              'module_uoa':cfg['module_deps']['cfg'],
              'data_uoa':cfg['lcfg_uoa'],
              'dict':dcfg}
          r=ck.access(ii)
          if r['return']>0: return r

    if pi_uoa!='' and pi_uoa!='-':
       rx=ck.access({'action':'find',
                     'module_uoa':cfg['module_deps']['platform.init'],
                     'data_uoa':pi_uoa})
       if rx['return']>0: return rx
       px=rx['path']

       if remote=='yes':
          if first_time:
             dv=''
             if tdid!='': dv=' -s '+tdid
             xsp=tosd.get('dir_sep','')

             # Create directory if needed
             z=tosd.get('path_to_scripts','')
             if z=='':
                z=tosd.get('remote_dir','')

             if z!='':
                y=tosd.get('remote_shell','')+' '+tosd.get('make_dir','')+' '+z+tosd.get('remote_shell_end','')
                y=y.replace('$#device#$',dv)

                if o=='con':
                   ck.out('')
                   ck.out('* Creating directory with scripts on remote device:')
                   ck.out('  '+y)

                rx=os.system(y)
                # Ignore output (can be already created)

             # Copying files and setting chmod 755
             x=os.listdir(px)
             for q in x:
                 xx=os.path.join(px,q)
                 if os.path.isfile(xx):
                    xr=z+xsp+q

                    if len(xx)>1 and xx[1:2]==':':
                       xx='/'+xx[0:1]+'/'+xx[2:]
                    xx=xx.replace('\\','/')

                    # Push file to remote device
                    y=tosd.get('remote_push','')
                    y=y.replace('$#device#$',dv)
                    y=y.replace('$#file1#$', xx)
                    y=y.replace('$#file2#$', xr)
                    y=y.replace('$#file1s#$', xr)

                    ck.out('')
                    ck.out('* Copying file to remote device:')
                    ck.out('  '+y)

                    rx=os.system(y)
                    # Ignore output (can be already exist)

                    # Set executable
                    y=tosd.get('remote_shell','')+' '+tosd.get('set_executable','')+' '+xr+tosd.get('remote_shell_end','')
                    y=y.replace('$#device#$',dv)

                    ck.out('')
                    ck.out('* Setting executable for this file:')
                    ck.out('  '+y)

                    rx=os.system(y)

       else:
          tadd_path.append(px)

    if o=='con' and i.get('skip_print_os','')!='yes' and i.get('skip_print_os_info','')!='yes':
       ck.out('')
       ck.out('OS CK UOA:            '+tosx+' ('+tos+')')
       ck.out('')
       ck.out('OS name:              '+prop.get('name',''))
       ck.out('Short OS name:        '+prop.get('name_short',''))
       ck.out('Long OS name:         '+prop.get('name_long',''))
       ck.out('OS bits:              '+prop.get('bits',''))

       if prop_os_abi!='':
          ck.out('OS ABI:               '+prop.get('abi',''))

       if prop_serial_no!='':
          ck.out('')
          ck.out('Device serial number: '+prop_serial_no)

       if pi_uoa!='' and pi_uoa!='':
          ck.out('')
          ck.out('Platform init UOA:    '+pi_uoa)

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

          dx=dcfg.get('platform_os_name',{}).get(tos,{})
          x=tdid
          if x=='': x='default'
          xn=dx.get(x,'')

          if (xn=='' and o=='con'):
             r=ck.inp({'text':'Enter your OS name (for example, Windows 10 or Android 5.0): '})
             xxn=r['string'].strip()

             if xxn!=xn:
                xn=xxn

                if 'platform_os_name' not in dcfg: dcfg['platform_os_name']={}
                if tos not in dcfg['platform_os_name']: dcfg['platform_os_name'][tos]={}
                dcfg['platform_os_name'][tos][x]=xn

                ii={'action':'update',
                    'module_uoa':cfg['module_deps']['cfg'],
                    'data_uoa':cfg['cfg_uoa'],
                    'dict':dcfg}
                r=ck.access(ii)
                if r['return']>0: return r

          if xn=='':
             return {'return':1, 'error':'can\'t exchange information where main name is empty'}
          prop['name']=xn

       ii={'action':'exchange',
           'module_uoa':cfg['module_deps']['platform'],
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
          ck.out('  OS CK entry already exists ('+fuid+') - loading latest meta (features) ...')

    rr={'return':0, 'os_uoa':tosx, 'os_uid':tos, 'os_dict':tosd, 
                    'host_os_uoa':hosx, 'host_os_uid':hos, 'host_os_dict':hosd,
                    'features':{'os':prop, 'os_misc':prop_all}, 
                    'devices':devices, 'device_id':tdid}

    if fuoa!='' or fuid!='':
       rr['features']['os_uoa']=fuoa
       rr['features']['os_uid']=fuid

    if len(hadd_path)>0:
       rr['host_add_path']=hadd_path

       eset=hosd.get('env_set','')
       svarb=hosd.get('env_var_start','')
       svare=hosd.get('env_var_stop','')
       sdirs=hosd.get('dir_sep','')
       evs=hosd.get('env_var_separator','')
       eifs=hosd.get('env_quotes_if_space','')
       nout=hosd.get('no_output','')

       # Add to PATH and prepare as string
       x=''
       for q in hadd_path:
           if x!='':x+=evs
           if q.find(' ')>=0 and not q.startswith(eifs):
              q=eifs+q+eifs
           x+=q
       sb=nout+eset+' PATH='+x+evs+svarb+'PATH'+svare+'\n'

       rr['host_add_path_string']=sb

    if len(tadd_path)>0:
       rr['target_add_path']=tadd_path

       eset=tosd.get('env_set','')
       svarb=tosd.get('env_var_start','')
       svare=tosd.get('env_var_stop','')
       sdirs=tosd.get('dir_sep','')
       evs=tosd.get('env_var_separator','')
       eifs=tosd.get('env_quotes_if_space','')
       nout=tosd.get('no_output','')

       # Add to PATH and prepare as string
       x=''
       for q in tadd_path:
           if x!='':x+=evs
           if q.find(' ')>=0 and not q.startswith(eifs):
              q=eifs+q+eifs
           x+=q
       sb=nout+eset+' PATH='+x+evs+svarb+'PATH'+svare+'\n'

       rr['target_add_path_string']=sb

    return rr

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

    h='<h2>Operating Systems of platforms participating in crowd-tuning</h2>\n'

    h+='<i>Reuse/extend <a href="https://github.com/ctuning/ck-crowdtuning-platforms/tree/master/platform.os">CK JSON meta information</a> of these operating systems using "ck pull repo:ck-crowdtuning-platforms" ...</i><br><br>\n'

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
    h+='   Name\n'
    h+='  </b></td>\n'
    h+='  <td><b>\n'
    h+='   Bits\n'
    h+='  </b></td>\n'
    h+='  <td><b>\n'
    h+='   Name Long\n'
    h+='  </b></td>\n'
    h+='  <td><b>\n'
    h+='   Name Short\n'
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
    for q in sorted(lst, key = lambda x: (x.get('meta',{}).get('features',{}).get('name','').upper(), \
                                          x.get('meta',{}).get('features',{}).get('name_short','').upper(), \
                                          x.get('meta',{}).get('features',{}).get('name_long','').upper())):

        num+=1

        duoa=q['data_uoa']
        duid=q['data_uid']

        meta=q['meta']
        ft=meta.get('features',{})
        
        name=ft.get('name','')
        bits=ft.get('bits','')
        name_long=ft.get('name_long','')
        name_short=ft.get('name_short','')


        h+=' <tr>\n'
        h+='  <td valign="top">\n'
        h+='   '+str(num)+'\n'
        h+='  </td>\n'
        h+='  <td valign="top">\n'
        h+='   '+name+'\n'
        h+='  </td>\n'
        h+='  <td valign="top">\n'
        h+='   '+bits+'\n'
        h+='  </td>\n'
        h+='  <td valign="top">\n'
        h+='   '+name_short+'\n'
        h+='  </td>\n'
        h+='  <td valign="top">\n'
        h+='   '+name_long+'\n'
        h+='  </td>\n'
        h+='  <td valign="top">\n'
        h+='   <a href="'+url0+'wcid='+work['self_module_uoa']+':'+duid+'">'+duid+'</a>\n'
        h+='  </td>\n'
        h+=' </tr>\n'


    h+='</table><br><br>\n'

    return {'return':0, 'html':h}

##############################################################################
# browse platform.os participated in experiment crowdsourcing (crowd-benchmarking and crowd-tuning)

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
    url='https://github.com/ctuning/ck-crowdtuning-platforms/tree/master/platform.os'

    import webbrowser
    webbrowser.open(url)

    import time
    time.sleep(3)

    url='http://cknowledge.org/repo/web.php?action=index&module_uoa=wfe&native_action=show&native_module_uoa=platform.os'

    import webbrowser
    webbrowser.open(url)

    return {'return':0}
