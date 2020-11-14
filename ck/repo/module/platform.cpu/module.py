#
# Collective Knowledge (platform - CPU)
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
# detect CPU

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
                cpu        - CPU features (properties), unified
                cpu_misc   - assorted CPU features (properties), platform dependent

                os         - OS features (properties), unified
                os_misc    - assorted OS features (properties), platform dependent
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

    einf=i.get('extra_info','')
    if einf=='': einf={}

    # Get OS info ##############################################################
    import copy
    ii=copy.deepcopy(i)
    ii['out']=oo
    if i.get('skip_print_os_info','')=='yes':ii['out']=''
    ii['action']='detect'
    ii['module_uoa']=cfg['module_deps']['platform.os']
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

    prop=rr['features']['os']

    # Some params
    ro=tosd.get('redirect_stdout','')
    remote=tosd.get('remote','')
    remote_ssh=tosd.get('remote_ssh','')
    win=tosd.get('windows_base','')
    mac=tosd.get('macos','')
    unix=win!='yes' and mac!='yes'

    dv=''
    if tdid!='': dv=' -s '+tdid

    # Init
    target={}
    target_freq={}
    target_freq_all={}
    target_freq_max={}
    target_num_proc=''
    info_cpu={}

    new_format=''
    unique_cpus=[]

    spd=tosd.get('skip_platform_detection','')

    if spd=='yes':
       # Nothing
       pass
    elif unix:
       # Get all params
       params={}
       if remote=='yes' and remote_ssh!='yes':
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

       # Read cpuinfo
       fnx='/proc/cpuinfo'

       if remote=='yes':

          # Read file
          rx=ck.gen_tmp_file({'prefix':'tmp-ck-'})
          if rx['return']>0: return rx
          fcpuinfo=rx['file_name']

          x=tosd.get('remote_shell','').replace('$#device#$',dv)+' cat '+fnx+' '+tosd.get('remote_shell_end','')+' '+ro+fcpuinfo

          if o=='con' and pdv=='yes':
             ck.out('')
             ck.out('Executing: '+x)

          rx=os.system(x)
          if rx!=0: 
             if os.path.isfile(fnx): os.remove(fcpuinfo)
             fcpuinfo='' # Do not process further

       else:
          fcpuinfo=fnx

       # Read and parse file
       pp=0 # current logical processor
       spp=str(pp)
       info_cpu[spp]={}
       target_freq[spp]=0
       target_freq_max[spp]=0
       first_skipped=False

       if fcpuinfo!='':
          rx=ck.load_text_file({'text_file':fcpuinfo, 'split_to_list':'yes'})
          if rx['return']>0: return rx
          ll=rx['lst']
          if remote=='yes' and os.path.isfile(fcpuinfo): os.remove(fcpuinfo)

          for q in ll:
              q=q.strip()
              if q!='':
                 x1=q.find(':')
                 if x1>0:
                    k=q[0:x1].strip()
                    v=q[x1+1:].strip()

                    if k=='processor':
                       if not first_skipped:
                          first_skipped=True
                       else:
                          pp+=1
                          spp=str(pp)
                          info_cpu[spp]={}

                    if k!='':
                       info_cpu[spp][k]=v

                       if k.find('MHz')>=0:
                          target_freq[spp]=float(v)
          target_num_proc=str(pp+1)

       # Legacy - outdated - should check name of each CPU (can be different in big-little, for example)
       target_cpu=info_cpu[spp].get('Hardware','')
       if target_cpu=='':
          target_cpu=info_cpu[spp].get('model name','')
       target_sub_cpu=info_cpu[spp].get('Processor','')
       if target_sub_cpu=='':
          target_sub_cpu=info_cpu[spp].get('model name','')
       target_cpu_features=info_cpu[spp].get('Features','')
       if target_cpu_features=='':
          target_cpu_features=info_cpu[spp].get('flags','')

       wa={'device_config':{'core_clusters':[], 'core_names':[]}}
       wa_id=0
       wa_unique={}
       xtcpu=''

       # Process each processor
       for px in range(0, pp+1):
           spx=str(px)

           tcpu=info_cpu[spx].get('Hardware','')
           if tcpu=='':
              tcpu=info_cpu[spx].get('model name','')

           if tcpu=='': # new format
              ic=info_cpu[spx]
              ic1=ic.get('CPU implementer','')
              ic2=ic.get('CPU architecture','')
              ic3=ic.get('CPU variant','')
              ic4=ic.get('CPU part','')
              ic5=ic.get('CPU revision','')

              tcpu=ic1+'-'+ic2+'-'+ic3+'-'+ic4+'-'+ic5

              info_cpu[spx]['cpu_abi']=params.get('ro.product.cpu.abi','') # not sure if correct for all processors
              info_cpu[spx]['new_format']='yes'

              new_format='yes'
           else:
              tsub_cpu=info_cpu[spp].get('Processor','')
              if tsub_cpu=='':
                 tsub_cpu=info_cpu[spp].get('model name','')
              info_cpu[spx]['ck_cpu_subname']=tsub_cpu

           x=params.get('ro.product.cpu.abi','') # not sure if correct for all processors
           if info_cpu[spx].get('cpu_abi','')=='' and x!='':
              info_cpu[spx]['cpu_abi']=x

           info_cpu[spx]['ck_cpu_name']=tcpu

           tcpu_features=info_cpu[spp].get('Features','')
           if tcpu_features=='':
              tcpu_features=info_cpu[spp].get('flags','')
           info_cpu[spx]['cpu_features']=tcpu_features

           # add unique
           found=False
           for uc in unique_cpus:
               if uc.get('ck_cpu_name','')==tcpu:
                  found=True
                  break

           if not found and tcpu!='' and tcpu!='----':
               unique_cpus.append(info_cpu[spx])

           if xtcpu=='' and tcpu!='' and tcpu!='----':
               xtcpu=tcpu

           # add unique in Workload Automation format
           if tcpu!='':
               if tcpu not in wa_unique:
                   wa_unique[tcpu]=wa_id
                   if tcpu!='----':
                       wa_id+=1

               wa_idx=wa_unique[tcpu]

               wa['device_config']['core_names'].append(tcpu)
               wa['device_config']['core_clusters'].append(wa_idx)

       # Clean up CPU names for workload automation
       wa_cn=wa['device_config']['core_names']
       for q in range(0, len(wa_cn)):
           tcpu=wa_cn[q]
           if tcpu=='----' and xtcpu!='':
               wa_cn[q]=xtcpu

       # Collect all frequencies
       for px in range(0, pp+1):
           fnx='/sys/devices/system/cpu/cpu'+str(px)+'/cpufreq/scaling_cur_freq'
           if remote=='yes':
              rx=ck.gen_tmp_file({'prefix':'tmp-ck-'})
              if rx['return']>0: return rx
              ffreq=rx['file_name']

              x=tosd.get('remote_shell','').replace('$#device#$',dv)+' cat '+fnx+' '+tosd.get('remote_shell_end','')+' '+ro+ffreq

              if o=='con' and pdv=='yes':
                 ck.out('')
                 ck.out('Executing: '+x)

              rx=os.system(x)
              if rx!=0:
                 if o=='con':
                    ck.out('')
                    ck.out('Non-zero return code :'+str(rx)+' - likely failed')
#                 can fail on MacOS, hence continue ...
#                 return {'return':1, 'error':'access to remote device failed'}
           else:
              ffreq=fnx

           # Read and parse file
           rx=ck.load_text_file({'text_file':ffreq, 'split_to_list':'yes'})
           if rx['return']==0: 
              ll=rx['lst']
              if remote=='yes' and os.path.isfile(ffreq): os.remove(ffreq)

              if len(ll)>0:
                 llx=ll[0].strip()
                 if llx!='':
                    fr=0
                    try:
                      fr=float(llx)/1000
                      target_freq[str(px)]=fr
                      info_cpu[str(px)]['cur_freq']=fr
                    except ValueError:
                      pass

           fnx='/sys/devices/system/cpu/cpu'+str(px)+'/cpufreq/cpuinfo_max_freq'
           if remote=='yes':
              rx=ck.gen_tmp_file({'prefix':'tmp-ck-'})
              if rx['return']>0: return rx
              ffreq=rx['file_name']

              x=tosd.get('remote_shell','').replace('$#device#$',dv)+' cat '+fnx+' '+tosd.get('remote_shell_end','')+' '+ro+ffreq

              if o=='con' and pdv=='yes':
                 ck.out('')
                 ck.out('Executing: '+x)

              rx=os.system(x)
              if rx!=0:
                 if o=='con':
                    ck.out('')
                    ck.out('Non-zero return code :'+str(rx)+' - likely failed')
#                 can fail on MacOS, hence continue ...
#                 return {'return':1, 'error':'access to remote device failed'}
           else:
              ffreq=fnx

           # Read and parse file
           rx=ck.load_text_file({'text_file':ffreq, 'split_to_list':'yes'})
           if rx['return']==0:
              ll=rx['lst']
              if remote=='yes' and os.path.isfile(ffreq): os.remove(ffreq)

              if len(ll)>0:
                 llx=ll[0].strip()
                 if llx!='':
                    try:
                      fr=float(llx)/1000
                      target_freq_max[str(px)]=fr
                      info_cpu[str(px)]['max_freq']=fr
                    except ValueError:
                      pass

           fnx='/sys/devices/system/cpu/cpu'+str(px)+'/cpufreq/scaling_available_frequencies'
           if remote=='yes':
              rx=ck.gen_tmp_file({'prefix':'tmp-ck-'})
              if rx['return']>0: return rx
              ffreq=rx['file_name']

              x=tosd.get('remote_shell','').replace('$#device#$',dv)+' cat '+fnx+' '+tosd.get('remote_shell_end','')+' '+ro+ffreq

              if o=='con' and pdv=='yes':
                 ck.out('')
                 ck.out('Executing: '+x)

              rx=os.system(x)
              if rx!=0:
                 if o=='con':
                    ck.out('')
                    ck.out('Non-zero return code :'+str(rx)+' - likely failed')
#                 can fail on MacOS, hence continue ...
#                 return {'return':1, 'error':'access to remote device failed'}
           else:
              ffreq=fnx

           # Read and parse file
           rx=ck.load_text_file({'text_file':ffreq, 'split_to_list':'yes'})
           if rx['return']==0:
              ll=rx['lst']
              if remote=='yes' and os.path.isfile(ffreq): os.remove(ffreq)

              if len(ll)>0:
                 llx=ll[0].strip()
                 if llx!='':
                    all=llx.split(' ')
                    for h in all:
                        ppx=str(px)
                        if ppx not in target_freq_all: target_freq_all[ppx]=[]
                        try:
                           h=int(h)
                           target_freq_all[ppx].append(h)
                           if 'all_freqs' not in info_cpu[ppx]:
                              info_cpu[ppx]['all_freqs']=[]
                           info_cpu[ppx]['all_freqs'].append(ppx)
                        except ValueError:
                           pass

# FGG - it is already initalized here!
#       # Initialized device if needed
#       if sdi!='yes':
#          remote_init=tosd.get('remote_init','')
#          if remote_init!='':
#             r=ck.access({'action':'init_device',
#                          'module_uoa':cfg['module_deps']['platform'],
#                          'os_dict':tosd,
#                          'device_id':tdid})
#             if r['return']>0: return r

#       if new_format=='yes':
#          for px in range(0, pp+1):
#              spx=str(px)
#
#              tcpu=info_cpu[spx].get('ck_cpu_name','')
#
#              # add unique
#              found=False
#              for uc in unique_cpus:
#                  if uc.get('ck_cpu_name','')==tcpu:
#                     found=True
#                     break
#
#              if not found and tcpu!='' and tcpu!='----':
#                 unique_cpus.append(info_cpu[spx])

       target['name']=target_cpu
       target['sub_name']=target_sub_cpu
       target['cpu_features']=target_cpu_features
       target['cpu_abi']=params.get('ro.product.cpu.abi','')
       target['num_proc']=target_num_proc
       target['current_freq']=target_freq
       target['max_freq']=target_freq_max
       target['all_freqs']=target_freq_all
       target['workload_automation']=wa

    ########################################################################################
    elif win=='yes':
      r=ck.access({'action':'get_from_wmic',
                   'module_uoa':cfg['module_deps']['platform'],
                   'group':'cpu',
                   'remote_shell':tosd.get('remote_shell','').replace('$#device#$',dv),
                   'remote_shell_end':tosd.get('remote_shell_end','')})
      if r['return']>0: return r
      info_cpu=r['dict']

      target_cpu=info_cpu.get('Name','')

      target_freq=int(info_cpu.get('CurrentClockSpeed','0'))
      target_freq_max=int(info_cpu.get('MaxClockSpeed','0'))

      target_num_proc=int(info_cpu.get('NumberOfLogicalProcessors','0'))

      target['name']=target_cpu
      target['sub_name']=target_cpu
      target['num_proc']=target_num_proc
      target['current_freq']={"0":target_freq}
      target['max_freq']={"0":target_freq_max}

      # To partially support new format
      unique_cpu={'ck_cpu_name':target_cpu,
                  'ck_cpu_subname':target_cpu}
      unique_cpus.append(unique_cpu)

    ########################################################################################
    elif mac=='yes':
      r=ck.access({'action':'run_and_get_stdout',
                   'module_uoa':cfg['module_deps']['os'],
                   'cmd': ['sysctl', 'machdep.cpu', 'hw.cpufrequency']})
      if r['return']>0: return r

      info_cpu={}
      for line in r['stdout'].splitlines():
        if ':' in line:
          left, right = line.split(':', 1)
          left = left.strip().lower()
          right = right.strip()
          info_cpu[left]=right

      target_cpu = info_cpu.get('machdep.cpu.brand_string','')
      target_num_proc = info_cpu.get('machdep.cpu.thread_count','')
      if target_num_proc == '':
        target_num_proc = info_cpu.get('machdep.cpu.core_count','')

      target_freq = int(info_cpu.get('hw.cpufrequency','0')) / 1000000
      target_freq_max = target_freq

      target['name']=target_cpu
      target['sub_name']=target_cpu
      target['cpu_features']=info_cpu.get('machdep.cpu.features','').lower()
      target['cpu_abi']=''
      target['num_proc']=target_num_proc
      target['current_freq']={'0':target_freq}
      target['max_freq']={'0':target_freq_max}

      # To partially support new format
      unique_cpu={'ck_cpu_name':target_cpu,
                  'ck_cpu_subname':target_cpu}
      unique_cpus.append(unique_cpu)      

    ########################################################################################
    if o=='con' and pdv!='no':
       ck.out('')
       if new_format=='yes':
          lup=len(unique_cpus)
          ck.out('Number of logical processors: '+str(target.get('num_proc',0)))
          ck.out('Number of unique processors:  '+str(lup))

          iup=0
          for up in unique_cpus:
              ck.out('')
              ck.out('  Unique processor: '+str(iup))

              x1=up.get('ck_cpu_name','')
              x1x=up.get('ck_cpu_name_real','')
              if x1x!='': x1=x1x+' ('+x1+')'

              x2=up.get('cpu_abi','')
              x3=up.get('cpu_features','')

              ck.out('    CPU name:     '+x1)
              ck.out('    CPU ABI:      '+x2)
              ck.out('    CPU features: '+x3)

              iup+=1

       else:
          ck.out('Number of logical processors: '+str(target.get('num_proc',0)))
          ck.out('CPU name:                     '+target.get('name',''))
          if target.get('name','')!=target.get('sub_name',''):
             ck.out('CPU sub name:                 '+target.get('sub_name',''))
          ck.out('CPU ABI:                      '+target.get('cpu_abi',''))
          ck.out('CPU features:                 '+target.get('cpu_features',''))

       ck.out('')
       ck.out('CPU frequency:')
       x=target.get('current_freq',{})
       for k in sorted(x, key=ck.convert_str_key_to_int):
           v=x[k]
           ck.out('  CPU'+k+' = '+str(v)+' MHz')
       ck.out('CPU max frequency:')
       x=target.get('max_freq',{})
       for k in sorted(x, key=ck.convert_str_key_to_int):
           v=x[k]
           ck.out('  CPU'+k+' = '+str(v)+' MHz')

       x=target.get('all_freqs',{})
       if len(x)>0:
          ck.out('CPU all frequencies (Hz):')
          import json
          for k in sorted(x, key=ck.convert_str_key_to_int):
              v=x[k]
              ck.out('  CPU'+k+' = '+json.dumps(v))

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

       if new_format=='yes':
          for unique in unique_cpus:
              xn=unique.get('ck_cpu_name','')

              if o=='con':
                 ck.out('')
                 ck.out('Exchanging information with '+er+' repository for a unique processor '+xn+' ...')

              # Copy nearly all (remove cur freq)

              mm={'features':unique}

              ii={'action':'exchange',
                  'module_uoa':cfg['module_deps']['platform'],
                  'sub_module_uoa':work['self_module_uid'],
                  'repo_uoa':er,
                  'data_name':xn,
                  'extra_info':einf,
                  'all':'no',
                  'dict':mm}
              if esr!='': ii['remote_repo_uoa']=esr
              r=ck.access(ii)
              if r['return']>0: return r

              if r.get('found','')=='yes':
                 fuoa=r.get('data_uoa','')
                 fuid=r.get('data_uid','')

                 ddd=r['dict'].get('features',{})

                 if o=='con':
                    ck.out('  CPU CK entry already exists ('+fuid+') - loading latest meta (features) ...')
                    x1=ddd.get('ck_processor_real_name','')
                    x2=ddd.get('ck_arch_real_name','')

                    x=x1
                    if x=='': x=x2
                    else:
                       if x2!='':
                          x+=' ('+x2+')'

                    if x!='':
                       ck.out('    Real name: '+x)

                 ddd['data_uoa']=fuoa
                 ddd['data_uid']=fuid

                 unique.update(ddd)

                 # Update all processors with this name
                 for px in range(0, pp+1):
                     spx=str(px)

                     tcpu=info_cpu[spx].get('ck_cpu_name','')
                     if tcpu==xn:
                        info_cpu[spx].update(ddd)

       else:
           if o=='con':
              ck.out('')
              ck.out('Exchanging information with '+er+' repository (old format) ...')

           xn=target.get('name','')

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

              dx=dcfg.get('platform_cpu_name',{}).get(tos,{})
              x=tdid
              if x=='': x='default'
              xn=dx.get(x,'')

              if (xn=='' and o=='con'):
                 r=ck.inp({'text':'Enter your processor name: '})
                 xxn=r['string'].strip()

                 if xxn!=xn:
                    xn=xxn

                    if 'platform_cpu_name' not in dcfg: dcfg['platform_cpu_name']={}
                    if tos not in dcfg['platform_cpu_name']: dcfg['platform_cpu_name'][tos]={}
                    dcfg['platform_cpu_name'][tos][x]=xn

                    ii={'action':'update',
                        'module_uoa':cfg['module_deps']['cfg'],
                        'data_uoa':cfg['cfg_uoa'],
                        'dict':dcfg}
                    r=ck.access(ii)
                    if r['return']>0: return r

              if xn=='':
                 return {'return':1, 'error':'can\'t exchange information where main name is empty'}

              target['name']=xn

           # Copy nearly all (remove cur freq)
           import copy
           xtarget=copy.deepcopy(target)
           if 'current_freq' in xtarget: del(xtarget['current_freq'])

           ii={'action':'exchange',
               'module_uoa':cfg['module_deps']['platform'],
               'sub_module_uoa':work['self_module_uid'],
               'repo_uoa':er,
               'data_name':target.get('name',''),
               'extra_info':einf,
               'all':'no',
               'dict':{'features':xtarget}} # Later we should add more properties from prop_all,
                                            # but should be careful to remove any user-specific info
           if esr!='': ii['remote_repo_uoa']=esr
           r=ck.access(ii)
           if r['return']>0: return r

           fuoa=r.get('data_uoa','')
           fuid=r.get('data_uid','')

           eft=r['dict'].get('features',{})

           if o=='con' and r.get('found','')=='yes':
              ck.out('  CPU CK entry already exists ('+fuid+') - loading latest meta (features) ...')
              target=eft

    # Finalize features
    if 'features' not in rr: rr['features']={}

    rr['features']['cpu']=target

    rr['features']['cpu_misc']=info_cpu
    rr['features']['cpu_unique']=unique_cpus
    rr['features']['cpu_new_format']=new_format

    if fuoa!='' or fuid!='':
       rr['features']['cpu_uoa']=fuoa
       rr['features']['cpu_uid']=fuid

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
                        "ondemand"
                        int value

              (env)                  - current env to specialize freq (CK_CPU*)...
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

    env=i.get('env',{})

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

    envtsep=tosd.get('env_separator','')
    etset=tosd.get('env_set','')

    tdid=rr['device_id']

    dir_sep=tosd.get('dir_sep','')

    remote=tosd.get('remote','')

    # Prepare scripts
    cmd=''
    if v=='min':
       cmd=tosd.get('script_set_min_cpu_freq','')
    elif v=='max':
       cmd=tosd.get('script_set_max_cpu_freq','')
    elif v=='ondemand':
       cmd=tosd.get('script_set_ondemand_cpu_freq','')
    else:
       cmd=tosd.get('script_set_cpu_freq','').replace('$#freq#$',str(v))

    if cmd!='':
       # Check path to scripts from env
       path_to_scripts=''

       pi_uoa=os.environ.get('CK_PLATFORM_INIT_UOA','')
       if pi_uoa=='':
          dcfg={}
          ii={'action':'load',
              'module_uoa':cfg['module_deps']['cfg'],
              'data_uoa':cfg['lcfg_uoa']}
          r=ck.access(ii)
          if r['return']>0 and r['return']!=16: return r
          if r['return']!=16:
             pi_key=tosx
             if remote=='yes' and tdid!='': pi_key+='-'+tdid

             dcfg=r['dict']
             pi_uoa=dcfg.get('platform_init_uoa',{}).get(pi_key,'')

       if pi_uoa!='' and remote!='yes':
          rx=ck.access({'action':'find',
                        'module_uoa':cfg['module_deps']['platform.init'],
                        'data_uoa':pi_uoa})
          if rx['return']==0:
             path_to_scripts=rx['path']

       if path_to_scripts=='':
          path_to_scripts=tosd.get('path_to_scripts','')


       if path_to_scripts!='':
          cmd=path_to_scripts+dir_sep+cmd

       # Add env
       xcmd=''
       for k in sorted(env):
           if k.startswith('CK_CPU'):
              v=str(env[k])

              if xcmd!='': xcmd+=envtsep
              xcmd+=etset+' '+k+'='+v

       if xcmd!='': 
          cmd=xcmd+envtsep+cmd

       if o=='con':
          ck.out('')
          ck.out('CMD to set CPU frequency:')
          ck.out('  '+cmd)

       # Get all params
       if remote=='yes':
          dv=''
          if tdid!='': dv=' -s '+tdid

          x=tosd.get('remote_shell','').replace('$#device#$',dv)+' "'+cmd+'"'

          rx=os.system(x)
          if rx!=0:
             if o=='con':
                ck.out('')
                ck.out('Non-zero return code :'+str(rx)+' - likely failed')

       else:
             rx=os.system(cmd)
             if rx!=0:
                if o=='con':
                   ck.out('')
                   ck.out('  Warning: setting frequency possibly failed - return code '+str(rx))

    return {'return':0}

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


    h='<h2>Processors of platforms participating in crowd-tuning</h2>\n'

    h+='<i>Reuse/extend <a href="https://github.com/ctuning/ck-crowdtuning-platforms/tree/master/platform.cpu">CK JSON meta information</a> of these processors using "ck pull repo:ck-crowdtuning-platforms" ...</i><br><br>\n'

    h+='<table class="ck_table" border="0">\n'

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
    h+='   Name 1\n'
    h+='  </b></td>\n'
    h+='  <td><b>\n'
    h+='   Name 2\n'
    h+='  </b></td>\n'
    h+='  <td><b>\n'
    h+='   Cores\n'
    h+='  </b></td>\n'
    h+='  <td><b>\n'
    h+='   Max frequency (MHz)\n'
    h+='  </b></td>\n'
    h+='  <td><b>\n'
    h+='   ABI\n'
    h+='  </b></td>\n'
    h+='  <td><b>\n'
    h+='   Features\n'
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
    for q in sorted(lst, key = lambda x: (x.get('meta',{}).get('features',{}).get('sub_name','').upper(), \
                                          x.get('meta',{}).get('features',{}).get('name','').upper())):

        num+=1

        duoa=q['data_uoa']
        duid=q['data_uid']

        meta=q['meta']
        ft=meta.get('features',{})

        name=ft.get('name','')
        if name=='':
           name=ft.get('ck_arch_real_name','')

        sub_name=ft.get('sub_name','')

        cores=ft.get('num_proc','')
        abi=ft.get('cpu_abi','')
        features=ft.get('cpu_features','')
        frequency=ft.get('max_freq',{})

        freq=''
        for x in range(0,1024):
            xx=str(x)
            if type(frequency)!=list or xx not in frequency: break
            if freq!='': freq+=', '
            freq+=str(frequency[xx])

        h+=' <tr>\n'
        h+='  <td valign="top">\n'
        h+='   '+str(num)+'\n'
        h+='  </td>\n'
        h+='  <td valign="top">\n'
        h+='   '+sub_name+'\n'
        h+='  </td>\n'
        h+='  <td valign="top">\n'
        h+='   '+name+'\n'
        h+='  </td>\n'
        h+='  <td valign="top">\n'
        h+='   '+str(cores)+'\n'
        h+='  </td>\n'
        h+='  <td valign="top">\n'
        h+='   '+freq+'\n'
        h+='  </td>\n'
        h+='  <td valign="top">\n'
        h+='   '+abi+'\n'
        h+='  </td>\n'
        h+='  <td valign="top">\n'
        h+='   '+features+'\n'
        h+='  </td>\n'
        h+='  <td valign="top">\n'
        h+='   <a href="'+url0+'wcid='+work['self_module_uoa']+':'+duid+'">'+duid+'</a>\n'
        h+='  </td>\n'
        h+=' </tr>\n'


    h+='</table><br><br>\n'

    return {'return':0, 'html':h}

##############################################################################
# browse platform.cpus participated in experiment crowdsourcing (crowd-benchmarking and crowd-tuning)

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
    url='https://github.com/ctuning/ck-crowdtuning-platforms/tree/master/platform.cpu'

    import webbrowser
    webbrowser.open(url)

    import time
    time.sleep(3)

    url='http://cknowledge.org/repo/web.php?action=index&module_uoa=wfe&native_action=show&native_module_uoa=platform.cpu'

    import webbrowser
    webbrowser.open(url)

    return {'return':0}
