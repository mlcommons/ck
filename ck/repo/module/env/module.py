#
# Collective Knowledge (environment)
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
# set environment for tools and libraries 
# (multiple versions of the same tools/libraries can co-exist)

def env_set(i):
    """
    Input:  {
              (host_os)              - host OS (detect, if ommitted)
              (target_os)            - target OS (detect, if ommitted)
              (target_device_id)     - target device ID (detect, if omitted)
                     or
              (device_id)

              (repo_uoa)             - repo where to limit search

              (uoa)                  - environment UOA entry
               or
              (tags)                 - search UOA by tags (separated by comma)

              (or_tags)              - add entries which has groups of tags separated by ;
              (no_tags)              - exclude entris with these tags separated by comma
              (search_dict)          - require verbatim matches of some attributes

              (local)                - if 'yes', add host_os, target_os, target_device_id to search

              (key)                  - key from deps (to set env with path)
              (name)                 - user-friendly name of the dependency (if needs to be resolved)

              (deps)                 - already resolved deps

              (reuse_deps)           - if 'yes' reuse all deps if found in cache by tags
              (deps_cache)           - list with resolved deps
              (skip_cache)           - skip caching (sometimes needed to iterate over deps such as DNN libs
                                         during autotuning, crowd-benchmarking and crowd-tuning)

              (skip_auto_resolution)       - if 'yes', do not check if deps are already resolved
              (skip_default)               - if 'yes', skip detection of default installed software version
              (skip_installed)             - dict to specify on which platforms not to search already installed version
              (skip_pruning_by_other_deps) - if 'yes', do not prune available envs using other resolved deps

              (bat_file)             - if !='', use this filename to generate/append bat file ...
              (bat_new)              - if 'yes', start new bat file

              (env)                  - existing environment

              (print)                - if 'yes', print found environment

              (random)               - if 'yes' and there is a choice, select random
                                       (useful for quiet experiment crowdsourcing such as sw/hw crowdtuning)

              (quiet)                - if 'yes', automatically provide default answer to all questions when resolving dependencies ... 

              (force_env_init)       - if 'yes', add '1' when calling env script (useful for LLVM plugins for example to force reinit)

              (install_to_env)       - install dependencies to env instead of CK-TOOLS (to keep it clean)!

              (install_env)          - customize installation (useful for replay to rebuild proper package with external env)

              (version_from)         - check version starting from ... (list of numbers)
              (version_to)           - check version up to ... (list of numbers)

              (safe)                 - safe mode when searching packages first instead of detecting already installed soft
                                       (to have more deterministic build)

              (package_uoa)          - force installation package
                                       (also useful to rebuild deps during replay)

              (rebuild)              - if 'yes', attempt to set env to avoid downloading package again, just rebuild (if supported)
            }

    Output: {
              return           - return code =  0, if successful
                                             = 32, if environment was deleted (env_uoa - env which was not found)
                                             >  0, if error
              (error)          - error text if return > 0

              env_uoa          - found environment UOA
              env              - updated environment
              bat              - string for bat file
              lst              - all found entries
              dict             - meta of the selected env entry
              detected_version - detected version of a software
            }

    """

    import os
    import copy
    import json

    o=i.get('out','')
    ooo = o if o=='con' else ''     # shouldn't we consider other options?

    ran=i.get('random','')
    quiet=i.get('quiet','')

    name=i.get('name','')

    rebuild=i.get('rebuild','')

    skip_cache=i.get('skip_cache','')

    package_uoa=i.get('package_uoa','')

    install_env=i.get('install_env',{})

    # Clean output file
    sar=i.get('skip_auto_resolution','')
    cdeps=i.get('deps',{})

    deps_cache=i.get('deps_cache',[])
    reuse_deps=i.get('reuse_deps','')

    skip_default=i.get('skip_default','')
    skip_installed=i.get('skip_installed',{})

    iev=i.get('install_to_env','')
    safe=i.get('safe','')

    bf=i.get('bat_file','')
    if bf!='' and os.path.isfile(bf): os.remove(bf)

    vfrom=i.get('version_from',[])
    vto=i.get('version_to',[])

    # Check host/target OS/CPU
    hos=i.get('host_os','')
    tos=i.get('target_os','')
    tdid=i.get('target_device_id','')
    if tdid=='': tdid=i.get('device_id','')

    user_env = (hos!='' or tos!='' or tdid!='')

    # Get some info about OS
    ii={'action':'detect',
        'module_uoa':cfg['module_deps']['platform.os'],
        'host_os':hos,
        'target_os':tos,
        'device_id':tdid,
        'skip_info_collection':'yes'}
    r=ck.access(ii)
    if r['return']>0: return r

    hos=r['host_os_uid']
    hosx=r['host_os_uoa']
    hosd=r['host_os_dict']

    ck_os_name=hosd['ck_name']

    tos=r['os_uid']
    tosx=r['os_uoa']
    tosd=r['os_dict']

    # Check if base is different
    x1=hosd.get('base_uid','')
    x2=hosd.get('base_uoa','')
    if x1!='' and x2!='': 
       hos=x1
       hosx=x2
    x1=tosd.get('base_uid','')
    x2=tosd.get('base_uoa','')
    if x1!='' and x2!='': 
       tos=x1
       tosx=x2

    remote=tosd.get('remote','')

    tbits=tosd.get('bits','')

    hplat=hosd.get('ck_name','')

    tplat2=i.get('original_target_os_name2','')

    eset=hosd.get('env_set','')
    svarb=hosd.get('env_var_start','')
    svare=hosd.get('env_var_stop','')
    sdirs=hosd.get('dir_sep','')
    evs=hosd.get('env_var_separator','')
    eifs=hosd.get('env_quotes_if_space','')
    nout=hosd.get('no_output','')

    # Check environment UOA
    enruoa=i.get('repo_uoa','')
    tags=i.get('tags','')
    or_tags=i.get('or_tags','')
    no_tags=i.get('no_tags','')
    search_dict = i.get('search_dict')
    duoa=i.get('uoa','')

    lx=0
    dd={}
    setup={}

    if user_env or i.get('local','')=='yes':
       setup={'host_os_uoa':hos,
              'target_os_uoa':tos,
              'target_os_bits':tbits}

    if reuse_deps=='yes' and skip_cache!='yes':
       # Check in cache!
       dep_query = {'setup':setup, 'tags':tags.split(','), 'or_tags':or_tags.split(','), 'no_tags':no_tags.split(',')}
       for dc_q in deps_cache:
           dep_meta = dc_q.get('meta',{})
           r=ck.compare_dicts({'dict1':dep_meta, 'dict2':dep_query})     # if dep_meta contains dep_query...
           if r['return']>0: return r
           if r['equal']=='yes':
              duoa = dc_q.get('uoa','')
              reuse_deps='no' # to avoid updating cache
              break

    # Search
    ii={'action':'search',
        'module_uoa':work['self_module_uid'],
        'tags':tags,
        'repo_uoa':enruoa,
        'data_uoa':duoa,
        'add_info':'yes',
        'add_meta':'yes'
    } # Need to sort by version, if ambiguity

    if search_dict!=None and len(search_dict)>0:
       ii['search_dict']=search_dict

    iii=copy.deepcopy(ii) # may need to repeat after registration

    # Prepare possible warning
    x = '"{}"'.format(name) if name else 'required software '
    msg_env_not_found = 'no registered CK environment was found for {} dependency with tags="{}"'.format(x, tags)

    if no_tags!='':
       msg_env_not_found+=', no_tags="'+no_tags+'"'

    if len(setup)>0:
       ro=readable_os({'setup':setup})
       if ro['return']>0: return ro
       setup1=ro['setup1']

       msg_env_not_found+=' and setup='+json.dumps(setup1)

    if len(vfrom)>0 or len(vto)>0:
       msg_env_not_found+=' and version constraints ('+json.dumps(vfrom)+' <= v <= '+json.dumps(vto)+')'

    # Search for environment entries
    r=ck.access(ii)
    if r['return']>0: return r

    # Prune if needed
    r=prune_search_list({'lst':r['lst'], 
                         'or_tags':or_tags, 
                         'no_tags':no_tags, 
                         'version_from':vfrom, 
                         'version_to':vto,
                         'setup':setup,
    })
    if r['return']>0: return r
    sbov=r.get('skipped_because_of_version','')

    l=r['lst']
    lx=len(l)

    auoas=[]

    dname=''

    try_to_reinstall=False
    if lx==0 and duoa!='':
       # Check exact problem
       rx=ck.access({'action':'load',
                     'module_uoa':work['self_module_uid'],
                     'data_uoa':duoa})
       if rx['return']>0:
          if rx['return']!=16: return rx

          if package_uoa=='':
             rx['error']='strange - missing environment ('+duoa+') and package not specified (may happen during replay from another machine)'

             if o=='con' and quiet!='yes':
                ck.out('')
                ck.out('    WARNING: '+rx['error']+'!')
                ck.out('')
#                ry=ck.inp({'text':'    Would you like to detect / reinstall again (Y/n)? '})
#                x=ry['string'].strip()
#
#                if x=='n' or x=='no':
#                   return rx
          else:
             # Otherwise can try to rebuild from provided package UOA
             ck.out('')
             ck.out('WARNING: environment doesn\'t exist but package provided - trying to redetect/reinstall ...')

          duoa=''
          iii['data_uoa']=duoa # since will be later new search
          l=[]
          lx=0

          try_to_reinstall=True

          # Repeat search if has without data uoa
          r=ck.access(iii)
          if r['return']>0: return r

          # Prune if needed
          r=prune_search_list({'lst':r['lst'], 
                               'or_tags':or_tags, 
                               'no_tags':no_tags, 
                               'version_from':vfrom, 
                               'version_to':vto,
                               'setup':setup,
                               'package_uoa':package_uoa})
          if r['return']>0: return r
          sbov=r.get('skipped_because_of_version','')

          l=r['lst']
          lx=len(l)

          auoas=[]

          dname=''

       if not try_to_reinstall:
          dds=rx['dict'].get('setup',{})

          # Changed setup
          if o=='con':
             ck.out('')
             ck.out('WARNING: requested host or target OS info is not matching info in env '+duoa+'!')

             ck.out('')
             rx=ck.access({'action':'convert_uid_to_alias', 'module_uoa':cfg['module_deps']['os'], 'uoa':dds.get('host_os_uoa','')})
             if rx['return']>0: return rx
             x=rx['string']
             ck.out(' Host OS UOA in env '+duoa+'    : '+x)
             rx=ck.access({'action':'convert_uid_to_alias', 'module_uoa':cfg['module_deps']['os'], 'uoa':setup.get('host_os_uoa','')})
             if rx['return']>0: return rx
             x=rx['string']
             ck.out(' Requested host OS UOA                  : '+x)

             ck.out('')
             rx=ck.access({'action':'convert_uid_to_alias', 'module_uoa':cfg['module_deps']['os'], 'uoa':dds.get('target_os_uoa','')})
             if rx['return']>0: return rx
             x=rx['string']
             ck.out(' Target OS UOA in env '+duoa+'  : '+x)
             rx=ck.access({'action':'convert_uid_to_alias', 'module_uoa':cfg['module_deps']['os'], 'uoa':setup.get('target_os_uoa','')})
             if rx['return']>0: return rx
             x=rx['string']
             ck.out(' Requested target OS UOA                : '+x)

             ck.out('')
             ck.out(' Target OS bits in env '+duoa+' : '+dds.get('target_os_bits',''))
             ck.out(' Requested target OS bits               : '+setup.get('target_os_bits',''))

             ck.out('')
             ck.out(' Target or_tags : '+dds.get('tags',''))
             ck.out(' Requested or_tags  : '+or_tags)

             ck.out('')
             ck.out(' Target no_tags : '+dds.get('no_tags',''))
             ck.out(' Requested no_tags  : '+no_tags)

             ck.out('')
             ck.out(' This is a possible bug - please report here:')
             ck.out('   * https://groups.google.com/forum/#!forum/collective-knowledge')
             ck.out('')

          return {'return':33, 'error':'current host or target OS ('+str(setup)+' is not matching the one in software env '+duoa}

    # If no entries and safe mode, search packages first
    showed_warning=False

    if lx==0 and duoa=='' and tags!='' and (safe=='yes' or package_uoa!=''):
       ck.out('==========================================================================================')
       ck.out('WARNING: '+msg_env_not_found)
       showed_warning=True

       if len(install_env)>0:
          if o=='con':
             ck.out('')
             ck.out('Reusing original and slightly pruned environment ...')
             ck.out('')

          for k in list(install_env.keys()):
              # TBD: quite ugly - maybe should record external env explicitly ...
              if k in ['LFLAGS', 'CXXFLAGS', 'CK_HOST_CPU_NUMBER_OF_PROCESSORS', 'LCORE_FLAGS']:
                 del(install_env[k])

       rx=internal_install_package({'out':ooo,
             'package_uoa':package_uoa,
             'tags':tags,
             'or_tags':or_tags, 
             'no_tags':no_tags,
             'quiet':quiet,
             'install_to_env':iev,
             'install_env':install_env,
             'safe':safe,
             'host_os':hos,
             'target_os':tos,
             'device_id':tdid,
             'add_hint':'yes',
             'reuse_deps':reuse_deps,
             'deps_cache':deps_cache,
             'version_from':vfrom,
             'version_to':vto,
             'deps':cdeps,
             'rebuild':rebuild,
             'sub_deps': i.get('current_deps',{}) if try_to_reinstall else {},
       })
       if rx['return']>0 and rx['return']!=16: return rx

       if rx['return']==0:
          duoa=rx['env_data_uoa']
          duid=rx['env_data_uid']

    # If no entries, try to detect default ones and repeat
    if lx==0 and duoa=='':
       history_deps=[]

       if o=='con' and tags!='' and not showed_warning:
          ck.out('')
          ck.out(' ********')
          ck.out(' WARNING: '+msg_env_not_found)
          ck.out('')

          showed_warning=True

       # First, try to detect already installed software, but not registered (default)
#       FGG changed on 2017-10-20 to be able to detect new versions of soft  !
       if not (skip_default=='yes' or skip_installed.get(tplat2,'')=='yes'): # or sbov=='yes'):
          if o=='con':
             ck.out('  Trying to automatically detect required software ...')

          ii={'action':'search',
              'module_uoa':cfg['module_deps']['soft'],
              'tags':tags,
              'add_meta':'yes'}
          rx=ck.access(ii)
          if rx['return']>0: return rx

          slst=rx['lst']

          # Sorting and checking which has detection module
          detected=''
          ssi=0
          found=False
          for q in sorted(slst, key=lambda v: v.get('meta',{}).get('sort',0)):
              met=q.get('meta',{})
              auoa=q['data_uoa']
              auid=q['data_uid']
              aname=met.get('soft_name','')

              # Check no tags:
              if no_tags!='':
                 split_no_tags=no_tags.split(',')
                 soft_tags=met.get('tags',[])
                 soft_skip=False
                 for st in soft_tags:
                     if st in split_no_tags:
                        soft_skip=True
                        break
                 if soft_skip:
                    continue

              auoas.append(q['data_uoa'])
              ds=met.get('auto_detect','')
              if ds=='yes':
                 if auid not in history_deps:
                    # Check target
                    rx=ck.access({'action':'check_target',
                                  'module_uoa':cfg['module_deps']['soft'],
                                  'dict':met.get('customize',{}),
                                  'host_os_uoa':hosx,
                                  'host_os_dict':hosd,
                                  'target_os_uoa':tosx,
                                  'target_os_dict':tosd})
                    if rx['return']>0:
                       continue

                    history_deps.append(auid)
                    ssi+=1

                    if o=='con':
                       ck.out('')
                       ck.out('  '+str(ssi)+') Checking if "'+aname+'" ('+auoa+' / '+auid+') is installed ...')

                    # Detect software
                    ii={'action':'check',
                        'module_uoa':cfg['module_deps']['soft'],
                        'data_uoa':auid,
                        'skip_help':'yes',
                        'host_os':hos,
                        'target_os':tos,
                        'target_device_id':tdid,
                        'version_from':vfrom, 
                        'version_to':vto,
#                        'deps':cdeps,
                        'out':ooo}
                    if len(setup)>0:
                       ii.update(setup)
                    ry=ck.access(ii)
                    if ry['return']>0:
                       if o=='con':
                          ck.out('  (warning during intermediate step: '+ry['error']+')')
                    else:
                       found=True

                       hdeps=ry.get('deps',{})
                       for hd in hdeps:
                           xhd=hdeps[hd]
                           xxhd=xhd.get('dict',{}).get('soft_uoa','')
                           if xxhd not in history_deps:
                              history_deps.append(xxhd)

          # repeat search if at least one above setup was performed
          if not found:
             if o=='con':
                ck.out('    No software auto-detection scripts found for this software in CK :( ...')

                if len(auoas)>0:
                   ck.out('')
                   ck.out('       Checked following related CK soft entries:')
                   for q in auoas:
                       ck.out('        * '+q)

          else:
             r=ck.access(iii)
             if r['return']>0: return r

             # Prune if needed
             r=prune_search_list({'lst':r['lst'], 
                                  'or_tags':or_tags, 
                                  'no_tags':no_tags,
                                  'version_from':vfrom, 
                                  'version_to':vto,
                                  'setup':setup,
                                  'package_uoa':package_uoa})
             if r['return']>0: return r

             l=r['lst']
             lx=len(l)

    # Re-check/prune existing environment using already resolved deps
    if lx>0:
       ilx=0
       if i.get('skip_pruning_by_other_deps','')!='yes' and lx>1 and sar!='yes':
          # Try auto-resolve or prune choices
          nls=[]
          for z in range(0, lx):
              j=l[z]
              zm=j.get('meta',{})
              cus=zm.get('customize','')
              zdeps=zm.get('deps',{})

              skip=False
              for q in zdeps:
                  jj=zdeps[q]
                  juoa=jj.get('uoa','')

                  for a in cdeps:
                      if a==q:
                         aa=cdeps[a]
                         if aa.get('skip_reuse','')!='yes':

                             auoa=aa.get('uoa','')

                             # Tricky part: basically if similar and already resolved current deps are not the same is underneath ones ...
                             if auoa!='' and auoa!=juoa:
                                 skip=True
                                 break

                  if skip: break
              if not skip: nls.append(j)

          l=nls
          lx=len(l)

       # Select sub-deps (sort by version)
       if lx>1:
          ls=sorted(l, key=lambda k: (k.get('meta',{}).get('customize',{}).get('sort', 0),
                                      k.get('info',{}).get('data_name',k['data_uoa']),
                                      internal_get_val(k.get('meta',{}).get('setup',{}).get('version_split',[]), 0, 0),
                                      internal_get_val(k.get('meta',{}).get('setup',{}).get('version_split',[]), 1, 0),
                                      internal_get_val(k.get('meta',{}).get('setup',{}).get('version_split',[]), 2, 0),
                                      internal_get_val(k.get('meta',{}).get('setup',{}).get('version_split',[]), 3, 0),
                                      internal_get_val(k.get('meta',{}).get('setup',{}).get('version_split',[]), 4, 0)),
                    reverse=True)

          l=ls

          if ran=='yes':
             from random import randint
             ilx=randint(0, lx-1)
          elif quiet=='yes':
             ilx=0
          else:
             if o=='con':
                xq='required software'
                if name!='': xq='"'+name+'"'

                xq+=' with tags="'+tags+'"'

                if len(setup)>0:
                   import json

                   ro=readable_os({'setup':setup})
                   if ro['return']>0: return ro
                   setup1=ro['setup1']

                   xq+=' and setup='+json.dumps(setup1)

                ck.out('')
                ck.out('More than one environment found for '+xq+':')
                ck.out('')

                dep_options = []

                for opt_dict in l:  # looping through all options for this environment
                    zi=opt_dict.get('info',{})
                    zm=opt_dict.get('meta',{})
                    zu=opt_dict.get('data_uid','')

                    zdn=zi.get('data_name','')
                    zdeps=zm.get('deps',{})
                    xtags=zm.get('tags','')
                    cus=zm.get('customize',{})
                    ver=cus.get('version','')

                    tags_csv = ','.join( [t for t in xtags if t] )

                    this_option = [ '{} - v{} ({} ({}))'.format(zdn, ver, tags_csv, zu) ]

                    if len(zdeps)>0:
                        for j in sorted(zdeps, key=lambda v: zdeps[v].get('sort',0)):
                            jj=zdeps[j]
                            juoa=jj.get('uoa','')
                            if juoa!='': # if empty, it most likely means that this unresolved dependency
                                        # is for a different target
                                jtags=jj.get('tags','')
                                jver=jj.get('ver','')

                                this_option.append( '{}- Depends on "{}" (env UOA={}, tags="{}", version={})'.format(' '*35, j, juoa, jtags, jver))

                    dep_options.append(this_option)

                select_adict = ck.access({'action': 'select_string',
                                            'module_uoa': 'misc',
                                            'options': dep_options,
                                            'default': '0',
                                            'question': 'Select one of the options for '+xq,
                })
                if select_adict['return']>0: return select_adict

                ilx = select_adict['selected_index']

       if ilx<len(l):
          duid=l[ilx]['data_uid']
          duoa=duid

          dname=l[ilx].get('info',{}).get('data_name','')

          dd=l[ilx].get('meta',{})

          if o=='con' and i.get('print','')=='yes':
             x=duoa
             if duid!=duoa: x+=' ('+duid+')'
             ck.out('CK environment found using tags "'+tags+'" : '+x)

    # No registered environments found and environment UOA is not explicitly defined
    if duoa=='':
       if tags!='':
          if not showed_warning:
             ck.out('==========================================================================================')
             ck.out('WARNING: '+msg_env_not_found)

          rx=internal_install_package({'out':ooo,
                                       'tags':tags,
                                       'or_tags':or_tags, 
                                       'no_tags':no_tags,
                                       'quiet':quiet,
                                       'install_to_env':iev,
                                       'install_env':install_env,
                                       'safe':safe,
                                       'host_os':hos,
                                       'target_os':tos,
                                       'device_id':tdid,
                                       'reuse_deps':reuse_deps,
                                       'deps_cache':deps_cache,
                                       'version_from':vfrom,
                                       'version_to':vto,
                                       'rebuild':rebuild,
                                       'deps':cdeps})
          if rx['return']>0: return rx

          duoa=rx['env_data_uoa']
          duid=rx['env_data_uid']

       if duoa=='':
          if o=='con':
             ck.out('    CK packages are not found for this software :( !')
             ck.out('')

             if len(auoas)>0:
                if len(auoas)==1:
                   rx=ck.access({'action':'print_help',
                                 'module_uoa':cfg['module_deps']['soft'],
                                 'data_uoa':auoas[0],
                                 'platform':hplat})

                   rx=ck.inp({'text':'       Would you like to manually register software, i.e. if it is in an unusual path (y/N): '})
                   x=rx['string'].strip().lower()
                   if x=='yes' or x=='yes':
                      ck.out('')
                      rx=ck.access({'action':'setup',
                                    'module_uoa':cfg['module_deps']['soft'],
                                    'data_uoa':auoas[0],
                                    'out':'con'})
                      if rx['return']>0: return rx
                      ck.out('')

                else:
                   # Show possible Wiki page
                   rx=ck.inp({'text':'       Would you like to open wiki pages about related software (with possible installation info) (y/N): '})
                   x=rx['string'].strip().lower()

                   if x=='yes' or x=='yes':
                      ck.out('')
                      for q in auoas:
                          rx=ck.access({'action':'wiki',
                                        'module_uoa':cfg['module_deps']['soft'],
                                        'data_uoa':q})
                          if rx['return']>0: return rx
                      ck.out('')

             ck.out('')
          return {'return':1, 'error':msg_env_not_found}

    # Load selected environment entry
    r=ck.access({'action':'load',
                 'module_uoa':work['self_module_uid'],
                 'data_uoa':duoa})
    if r['return']>0: 
       if r['return']==16:
          r['return']=32
          r['env_uoa']=duoa
       return r
    d=r['dict']
    p=r['path']

    dname=r.get('data_name','')
    if dname!='':
        d['data_name']=dname

    suoa=d.get('soft_uoa','')
    cs=None
    if suoa!='':
       r=ck.access({'action':'load',
                    'module_uoa':cfg['module_deps']['soft'],
                    'data_uoa':suoa})
       if r['return']>0: return r

       salias=r['data_alias']
       d['soft_alias']=salias

       # Check if has custom script
       rx=ck.load_module_from_path({'path':r['path'], 'module_code_name':cfg['custom_script_name'], 'skip_init':'yes'})
       if rx['return']==0: 
          cs=rx['code']

    # Check that all sub dependencies still exists (if full path)
    outdated=False
    to_delete=False
    err=''

    subdeps=d.get('deps',{})    # sub-dependencies of the selected environment
                                # (normally already resolved, but check if software has changed in the meantime)
    for subdep_name in subdeps:
        subdep=subdeps[subdep_name]
        subdep_cus=subdep.get('dict',{}).get('customize',{})
        sfc=subdep_cus.get('skip_file_check','')
        full_path=subdep_cus.get('full_path','')

        if sfc!='yes' and full_path!='' and not os.path.isfile(full_path):
           outdated=True
           err='one of sub-dependencies ('+subdep_name+') have changed (file '+full_path+' not found)'
           break

        subdep_uoa=subdep.get('uoa','')
        if subdep_uoa!='':
           rx=ck.access({'action':'find',
                         'module_uoa':work['self_module_uid'],
                         'data_uoa':subdep_uoa})
           if rx['return']>0:
              if rx['return']!=16: return rx
              outdated=True
              err='one of sub-dependencies ('+subdep_name+') have changed (CK environment '+subdep_uoa+' not found)'
              break

        if reuse_deps=='yes' and skip_cache!='yes':
           # Check in cache!
           subdep_query = {'setup':setup, 'tags':subdep.get('tags','').split(','), 
                                          'or_tags':subdep.get('or_tags','').split(','),
                                          'no_tags':subdep.get('no_tags','').split(',')}
           dc_found = False
           for dc_q in deps_cache:
               dep_meta = dc_q.get('meta',{})
               r=ck.compare_dicts({'dict1':dep_meta, 'dict2':subdep_query})      # if dep_meta contains subdep_query...
               if r['return']>0: return r
               if r['equal']=='yes':
                  dc_found = True
                  break

           if not dc_found:
              deps_cache.append({'meta':subdep_query, 'uoa':subdep_uoa, 'tags':tags.split(','),
                                                                        'or_tags':or_tags.split(','),
                                                                        'no_tags':no_tags.split(',')})

    # Check if has changed but try to continue
    if outdated and ' have changed ' in err and o=='con' and quiet!='yes':
       ck.out('')
       ck.out('    WARNING: '+err)

       ck.out('')
       rx=ck.inp({'text':'    Would you like to continue at your own risk (y/N): '})
       x=rx['string'].strip().lower()

       if x=='y' or x=='yes':
          outdated=False

    # Check if file exists for current dependency
    verx=''
    cus=d.get('customize',{})
    full_path=cus.get('full_path','')

    tc='it appears that your environment has changed - '
    if not outdated and full_path!='' and cus.get('skip_file_check','')!='yes' and not os.path.isfile(full_path):
       err=tc+'software file not found in a specified path ('+full_path+')'
       outdated=True

    ver_in_env=cus.get('version','') # detected version during installation
    if not outdated and ver_in_env!='':
       scmd=cus.get('soft_version_cmd',{}).get(ck_os_name,'')
       if cus.get('skip_version_recheck','')!='yes' and scmd!='' and 'parse_version' in dir(cs):
          # Check version (via customized script) ...
          ii={'action':'get_version',
              'module_uoa':cfg['module_deps']['soft'],
              'full_path':full_path,
              'bat':'',
              'host_os_dict':hosd,
              'target_os_dict':tosd,
              'cmd':scmd,
              'custom_script_obj':cs,
              'use_locale':cus.get('use_locale_for_version','')}
          rx=ck.access(ii)
          if rx['return']==0:
             verx=rx['version']
             if verx!='' and verx!=ver_in_env:
                err=tc+'version during installation ('+ver_in_env+') is not the same as current version ('+verx+')'
                outdated=True

    if outdated:
       if o=='con':
          ck.out('')
          ck.out('WARNING: '+err)

          ck.out('')
          rx=ck.inp({'text':'Would you like to remove outdated environment entry from CK (Y/n)? '})
          x=rx['string'].strip()

          if x=='n' or x=='no':
             return {'return':1, 'error':err}
          to_delete=True

       # Deleting outdated environment
       if to_delete:
          if o=='con':
             ck.out('')
             ck.out('Removing outdated environment entry '+duoa+' ...')

          rx=ck.access({'action':'delete',
                        'module_uoa':work['self_module_uid'],
                        'data_uoa':duoa})
          if rx['return']>0: return rx

          return {'return':1, 'error':'Outdated environment was removed - please, try again!'}

    # Update cache
    if reuse_deps=='yes' and skip_cache!='yes':
       deps_cache.append({'meta':dep_query, 'uoa':duoa, 'tags':tags.split(','),
                                                        'or_tags':or_tags.split(','),
                                                        'no_tags':no_tags.split(',')})

    # Prepare environment and bat
    env=i.get('env',{})
    xenv=d.get('env',{})
    env.update(xenv)

    env_call=hosd.get('env_call','')
    bin_prefix=hosd.get('bin_prefix','')

    # Process CMD first:
    sb=''

    es=d.get('env_script','') or ( cfg['default_bat_name'] + hosd.get('script_ext','') )

    ppu=''
    if i.get('force_env_init','')=='yes':
       ppu=' 1'

    if es!='':
       pp=os.path.join(p,es)
       if i.get('key','')!='':
          sb+=eset+' CK_ENV_SCRIPT_'+i['key'].upper()+'='+pp+'\n'
       sb+=env_call+' '+pp+ppu+'\n'

    # Check bat file
    if bf!='':
       bn=i.get('bat_new','')
       x='a'
       if bn=='yes': x='w'

       try:
          fbf=open(bf, x)
          fbf.write(sb)
       except Exception as e: 
          fbf.close()
          return {'return':1, 'error':'problem writing environment file ('+format(e)+')'}

       fbf.close()

    return {'return':0, 'env_uoa':duoa, 'env':env, 'bat':sb, 'lst':l, 'dict':d, 'detected_version':verx}

##############################################################################
# show all installed environment

def show(i):
    """
    Input:  {
              (repo_uoa)          - repository UOA (with wildcards)
              (module_uoa)        - module UOA (with wildcards)
              (data_uoa)          - data UOA (with wildcards)

              (tags)              - prune by tags
              (target_os)         - prune by target OS
              (target_bits)       - prune by target bits
              (version)           - prune by version
              (name)              - prune by name with wildcards
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              lst          - list from search function
              view         - sorted view list
            }

    """

    o=i.get('out','')

    tags=i.get('tags','')

    extended_tags = [ tags ] if tags else []

    tos_uoa=i.get('target_os','')
    if tos_uoa!='':
        # Load OS
        ry=ck.access({'action':'load',
                     'module_uoa':cfg['module_deps']['os'],
                     'data_uoa':tos_uoa})
        if ry['return']>0: return ry

        tos_uoa = ry['dict'].get('base_uoa','') or ry['data_uoa']

        extended_tags.append( 'target-os-'+tos_uoa )

    tb = i.get('target_bits','')
    if tb!='': extended_tags.append( tb+'bits' )

    ver = i.get('version','')
    if ver!='': extended_tags.append( 'v'+ver )

    tags = ','.join(extended_tags)

    name=i.get('name','')
    wname=False
    if name.find('*')>=0 or name.find('?')>=0:
        import fnmatch
        wname=True
        name=name.lower()

    # creating a list of patterns from the "main xcid" and the list of auxiliary xcids:
    full_xcids_list = [{
        'repo_uoa': i.get('repo_uoa',''),
        'module_uoa': i.get('module_uoa',''),
        'data_uoa': i.get('data_uoa',''),
    }] + i.get('xcids',[])

    lst = []

    # iterating through the list of patterns:
    for xcid in full_xcids_list:
        rx=ck.access({'action':'search',
            'repo_uoa':xcid.get('repo_uoa',''),
            'module_uoa':xcid.get('module_uoa',''),
            'data_uoa':xcid.get('data_uoa',''),
            'tags':tags,
            'add_info':'yes',
            'add_meta':'yes'})
        if rx['return']>0: return rx
        lst += rx['lst']

    # prepare view
    unsorted_dicts=[]

    table_fields = [    # Rearranging the lines below will rearrange the fields in the output:
        # (internal)         (external)     (align)
        ('data_uid',        'Env UID:',     ':>'),
        ('target_os_uoa',   'Target OS:',   ':>'),
        ('tbits',           'Bits:',        ':>'),
        ('data_name',       'Name:',        ':<'),
        ('version',         'Version:',     ':<'),
        ('tags',            'Tags:',        ':<'),
    ]

    # width of each field (initialized with minimum required width)
    max_width = { internal: len(external) for (internal, external, _) in table_fields }


    target_os_name={} # Caching target OS names

    for q in lst:
        duoa=q['data_uoa']
        duid=q['data_uid']

        ruoa=q['repo_uoa']
        ruid=q['repo_uid']

        info=q['info']
        meta=q['meta']

        if len(meta)==0:
           continue

        cus=meta.get('customize',{})
        setup=meta.get('setup',{})
        tags=meta.get('tags',[])

        host_os_uoa=setup.get('host_os_uoa','')
        target_os_uoa=setup.get('target_os_uoa','')
        tbits=setup.get('target_os_bits','')
        version=cus.get('version','')
        sversion=setup.get('version_split',[])

        dname=info.get('data_name','')

        if (not name) \
        or ( ( fnmatch.fnmatch(dname.lower(), name)) if wname else (name == dname) ):
           # Check target OS
           if target_os_uoa in target_os_name:
              tduoa=target_os_name[target_os_uoa]
           elif target_os_uoa:
              # Load
              ry=ck.access({'action':'load',
                            'module_uoa':cfg['module_deps']['os'],
                            'data_uoa':target_os_uoa})
              if ry['return']>0: return ry
              tduoa=ry['data_uoa']
              target_os_name[target_os_uoa]=tduoa
           else:
              tduoa = 'Any'

           tags_csv = ','.join( [t for t in tags if t] )

           env_info = {
                'data_uid':         duid,
                'repo_uid':         ruid,
                'tags':             tags_csv,
                'host_os_uoa':      host_os_uoa,
                'target_os_uoa':    tduoa,
                'tbits':            tbits,
                'version':          version,
                'version_split':    sversion,
                'data_name':        dname,
           }

           # Find maximum width for each field:
           for (internal, _, _) in table_fields:
                field_width = len(str(env_info[internal]))
                if field_width>max_width[internal]:
                    max_width[internal]=field_width

           unsorted_dicts.append(env_info)

    # Sort by target_os_uoa, name and split version
    sorted_dicts=sorted(unsorted_dicts, key=lambda k: (k['target_os_uoa'],
                                   k['tbits'],
                                   k['data_name'],
                                   internal_get_val(k.get('version_split',[]), 0, 0),
                                   internal_get_val(k.get('version_split',[]), 1, 0),
                                   internal_get_val(k.get('version_split',[]), 2, 0),
                                   internal_get_val(k.get('version_split',[]), 3, 0),
                                   internal_get_val(k.get('version_split',[]), 4, 0)),
              reverse=True)

    # Print
    if o=='con' and len(sorted_dicts)>0:

          last_field_name       = table_fields[-1][0]   # the last field is not padded, it is treated separately

          # All fields of the header are aligned to the left
          header_format = ' '.join( [ '{{p[{}]{}{}}}'.format(internal, ':<', max_width[internal]) for (internal, _, _) in table_fields[:-1]] \
                                    + [ '{{p[{}]}}'.format(last_field_name) ] )

          # Fields of the body are aligned differently, depending on the third column of table_fields:
          body_format   = ' '.join( [ '{{p[{}]{}{}}}'.format(internal, body_align, max_width[internal]) for (internal, _, body_align) in table_fields[:-1]] \
                                    + [ '{{p[{}]}}'.format(last_field_name) ] )


          header_line   = header_format.format( p={ internal: external for (internal, external, _) in table_fields } )

          ck.out(header_line)
          ck.out('')

          for field_values in sorted_dicts:
              body_line = body_format.format( p=field_values )

              ck.out( body_line )

    return {'return':0, 'lst':lst, 'view':sorted_dicts}


###############################################################################
## A helper function to compute a given DNF on a given dictionary of attributes
##
## The assumed structure of the DNF is:
#
# [
#     {   # either one combination:
#         'left_hand': [ 'up', 'UP', 'raised', 'RAISED', '1' ],
#         'right_hand': [ 'down', 'DOWN', 'lowered', 'LOWERED', '0']
#     },
#     {   # or another:
#         'right_hand': [ 'up', 'UP', 'raised', 'RAISED', '1' ],
#         'left_hand': [ 'down', 'DOWN', 'lowered', 'LOWERED', '0']
#     }
# ]

def match_attrib_DNF( attribs, conjunctions ):

    def match_one_conjunction( conjunction ):
        def match_one_attrib( attrib_name, values ):
            value_list = values if isinstance(values, list) else [ values ]     # the general case is a list of matching values
            return attribs.get(attrib_name,'') in value_list

        for attrib_name, value_list in conjunction.items():                     # AND: a single False makes everything False
            if not match_one_attrib( attrib_name, value_list ):
                return False
        return True

    dnf = conjunctions if isinstance(conjunctions, list) else [ conjunctions ]  # the general case is a list of conjunctions

    for conjunction in dnf:                                                     # OR: a single True makes everything True
        if match_one_conjunction( conjunction ):
            return True
    return False


##############################################################################
# resolve all dependencies

def resolve(i):
    """
    Input:  {
              (host_os)              - host OS (detect, if ommitted)
              (target_os)            - target OS (detect, if ommitted)
              (target_device_id)     - target device ID (detect, if omitted)
                  or
              (device_id)

              (repo_uoa)             - repo where to limit search

              deps                   - dependencies dict

              (reuse_deps)           - if 'yes' reuse all deps if found in cache by tags
              (deps_cache)           - list with resolved deps

              (dep_add_tags)         - a dictionary that maps extra tags to be added to specific subdictionaries of deps{}
                                       for this particular resolution
              (dep_add_tags.{KEY})   - extra tags added to specific subdictionary of deps{} for this particular resolution session

              (env)                  - env

              (install_env)          - env during installation

              (add_customize)        - if 'yes', add to deps customize field from the environment 
                                       (useful for program compilation)

              (skip_dict)            - if 'yes', do not add to deps dict field from the environment 
                                       (useful for program compilation)

              (skip_auto_resolution) - if 'yes', do not check if deps are already resolved

              (random)               - if 'yes' and there is a choice, select random
                                       (useful for quiet experiment crowdsourcing such as sw/hw crowdtuning)

              (quiet)                - if 'yes', automatically provide default answer to all questions when resolving dependencies ... 

              (install_to_env)       - install dependencies to env instead of CK-TOOLS (to keep it clean)!

              (safe)                 - safe mode when searching packages first instead of detecting already installed soft
                                       (to have more deterministic build)

              (rebuild)              - if 'yes', attempt to set env to avoid downloading package again, just rebuild (if supported)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              bat          - string for bat file calling all bats ...
              cut_bat      - string for bat file calling all bats (does not include deps that are explicitly excluded) ...
              deps         - updated deps (with uoa)
              env          - updated env
            }
    Test:
            cat deps_only.json
            {
                  "deps": {
                    "weights": {
                      "force_target_as_host": "yes",
                      "local": "yes",
                      "name": "TensorFlow Lite model and weights",
                      "no_tags": "mobilenet-all",
                      "sort": 30,
                      "tags": "model,tflite,image-classification"
                    },
              ...
            }

            ck resolve env @deps_only.json "@@@{'dep_add_tags': {'weights':'resnet'}}" --out=json
            ck resolve env @deps_only.json --dep_add_tags.weights=mobilenet --out=json

    """

    import copy

    o=i.get('out','')

    if o=='con':
       ck.out('')
       ck.out('  -----------------------------------')
       ck.out('  Resolving software dependencies ...')

    combined_env_script_body=''
    alternative_combined_env_script_body=''

    install_env=i.get('install_env',{})

    rebuild=i.get('rebuild','')

    sar=i.get('skip_auto_resolution','')

    deps=i.get('deps',{})

    dep_add_tags = i.get('dep_add_tags', {})
    for combi_opt in i:
        if combi_opt.startswith('dep_add_tags.'):
           _ , dep_name    = combi_opt.split('.')
           dep_add_tags[dep_name] = i[combi_opt]

    for a_dep in dep_add_tags:
        if a_dep in deps:
            tags_to_be_added = dep_add_tags[a_dep]
            if tags_to_be_added:
                deps[a_dep]['tags'] += ',' + tags_to_be_added
        else:   # I'd rather raise() here, but we are in CK
            ck.out("\n!!! Warning: dependency '{}' has not been found in the original entry - please check your input !!!\n".format(a_dep))

    deps_cache=i.get('deps_cache',[])
    reuse_deps=i.get('reuse_deps','')

    ran=i.get('random','')
    quiet=i.get('quiet','')

    iev=i.get('install_to_env','')
    safe=i.get('safe','')

    # Check host/target OS/CPU
    hos=i.get('host_os','')
    tos=i.get('target_os','')
    tdid=i.get('target_device_id','')
    if tdid=='': tdid=i.get('device_id','')

    # Get some info about OS
    ii={'action':'detect',
        'module_uoa':cfg['module_deps']['platform.os'],
        'host_os':hos,
        'target_os':tos,
        'device_id':tdid,
        'skip_info_collection':'yes'}
    r=ck.access(ii)
    if r['return']>0: return r

    hos=r['host_os_uid']
    hosx=r['host_os_uoa']
    hosd=r['host_os_dict']

    tos=r['os_uid']
    tosx=r['os_uoa']
    tosd=r['os_dict']

    hplat=hosd.get('ck_name','')
    hplat2=hosd.get('ck_name2','')
    tplat=tosd.get('ck_name','')
    tplat2=tosd.get('ck_name2','')

    # Check if base is different
    x1=hosd.get('base_uid','')
    x2=hosd.get('base_uoa','')
    if x1!='' and x2!='': 
       hos=x1
       hosx=x2
    x1=tosd.get('base_uid','')
    x2=tosd.get('base_uoa','')
    if x1!='' and x2!='': 
       tos=x1
       tosx=x2

    remote=tosd.get('remote','')

    tbits=tosd.get('bits','')

    # Checking deps
    env=i.get('env',{})
    enruoa=i.get('repo_uoa','')

    ac=i.get('add_customize','')
    sd=i.get('skip_dict','')

    res=[]
    iv=0

    sdeps=sorted(deps, key=lambda v: deps[v].get('sort',0))

    xsb=''  # Append to the end
    xsb1='' # Append to the end

    for k in sdeps:
        q=deps[k]

        if q.get('skipped','')=='yes':
           continue

        if q.get('enabled','')!='yes':
            enable_DNF = q.get('enable_if_env')
            if enable_DNF:
                if match_attrib_DNF( install_env, enable_DNF ):
                    q['enabled']='yes'
                else:
                    q['skipped']='yes'
                    continue

        if q.get('skipped','')!='yes':
            disable_DNF = q.get('disable_if_env')
            if disable_DNF:
                if match_attrib_DNF( install_env, disable_DNF ):
                    q['skipped']='yes'
                    continue
                else:
                    q['enabled']='yes'

        ytos=tos
        ytdid=tdid
        ytosx=tosx
        ytosd=tosd

        tags=q.get('tags','')
        or_tags=q.get('or_tags','')
        no_tags=q.get('no_tags','')
        name=q.get('name','')
        local=q.get('local','')
        sd=q.get('skip_default','')
        sinst=q.get('skip_installed',{})

        vfrom=q.get('version_from',[])
        vto=q.get('version_to',[])

        ek=q.get('env_key','')

        uoa=q.get('uoa','')

        skip_cache=q.get('skip_cache','')

        # Check if restricts dependency to a given host or target OS
        rx=ck.access({'action':'check_target',
                      'module_uoa':cfg['module_deps']['soft'],
                      'dict':q,
                      'host_os_uoa':hosx,
                      'host_os_dict':hosd,
                      'target_os_uoa':ytosx,
                      'target_os_dict':ytosd})
        if rx['return']>0:
           continue

        if q.get('force_target_as_host','')=='yes':
            ytos=hos
            ytdid=''
            ytosx=hosx
            ytosd=hosd

        # Extra tags to be added conditionally:
        #
        xtags=[]

        # Adding extra tags based on environment DNF:
        #
        update_tags_if_env = q.get('update_tags_if_env')
        if update_tags_if_env:
            for candidate_tag, add_tag_DNF in update_tags_if_env.items():
                if match_attrib_DNF( install_env, add_tag_DNF ):
                    xtags.append( candidate_tag )

        # Adding extra tags depending on host/target platform:
        #
        tx=q.get('update_tags_by_host_platform',{}).get(hplat,'')
        if tx!='': xtags.append(tx)
        tx=q.get('update_tags_by_host_platform2',{}).get(hplat2,'')
        if tx!='': xtags.append(tx)
        tx=q.get('update_tags_by_target_platform',{}).get(tplat,'')
        if tx!='': xtags.append(tx)
        tx=q.get('update_tags_by_target_platform2',{}).get(tplat2,'')
        if tx!='': xtags.append(tx)
        tx=q.get('update_tags_by_target_os_uoa',{}).get(ytosx,'')       # Ugly, but quick
        if tx!='': xtags.append(tx)

        for tx in xtags:
            if tags!='': tags+=','
            tags+=tx.strip()

        # Check if has associated package (in case of rebuilding deps for replay)
        qdict=q.get('dict',{})
        package_uoa=q.get('package_uoa','')
        if package_uoa=='':
           package_uoa=qdict.get('package_uoa','')
        if package_uoa=='':
           package_uoa=qdict.get('customize',{}).get('used_package_uid','')

        xinstall_env=copy.deepcopy(qdict.get('customize',{}).get('install_env',{}))
#        xinstall_env.update(install_env)
#       install_env=copy.deepcopy(xinstall_env) # This is bug - install_env is a global env which is common for the first package!

        # Try to set environment
        iv+=1

        if o=='con':
           x='*** Dependency '+str(iv)+' = '+k
           if name!='': x+=' ('+name+')'
           x+=':'
           ck.out('')
           ck.out(x)

        ii={'host_os':hos,
            'original_target_os_name2':tplat2,
            'target_os':ytos,
            'target_device_id':ytdid,
            'tags':tags,
            'or_tags':or_tags,
            'no_tags':no_tags,
            'repo_uoa':enruoa,
            'env':env,
            'uoa':uoa,
            'deps':deps,
            'current_deps':qdict.get('deps',{}),
            'deps_cache':deps_cache,
            'reuse_deps':reuse_deps,
            'skip_cache':skip_cache,
            'skip_auto_resolution':sar,
            'skip_default':sd,
            'skip_installed':sinst,
            'local':local,
            'random':ran,
            'name':name,
            'key':ek,
            'skip_pruning_by_other_deps':q.get('skip_pruning_by_other_deps',''),
            'quiet':quiet,
            'force_env_init':q.get('force_env_init',''),
            'install_to_env':iev,
            'install_env':xinstall_env,
            'version_from':vfrom,
            'version_to':vto,
            'package_uoa':package_uoa,
            'safe':safe
           }

        if rebuild=='yes': ii['rebuild']='yes'
        if o=='con': ii['out']='con'

        rx=env_set(ii)
        if rx['return']>0: return rx

        lst=rx['lst']
        dd=rx['dict']

        package_uoa=dd.get('package_uoa','')
        if package_uoa=='':
           package_uoa=dd.get('customize',{}).get('used_package_uid','')
        if package_uoa!='':
           q['package_uoa']=package_uoa # to be able to rebuild env for replay on another machine

        dver=rx.get('detected_version','')
        if dver!='': q['detected_ver']=dver

        if 'choices' not in q or len('choices')==0: 
           q['choices'] = [zw['data_uid'] for zw in lst]

        cus=dd.get('customize',{})

        if ac=='yes': q['cus']=cus
        if sd!='yes' or q.get('add_dict','')=='yes': q['dict']=dd

        ver=cus.get('version','')
        if ver!='': q['ver']=ver

        uoa=rx['env_uoa']
        q['uoa']=uoa
        q['num_entries']=len(lst)

        if o=='con':
           ck.out('')
           x='    Resolved. CK environment UID = '+uoa
           if dver!='': 
              x+=' (detected version '+dver+')'
           elif ver!='':
              x+=' (version '+ver+')'
           ck.out(x)

        bdn=cus.get('build_dir_name','')
        if bdn!='': q['build_dir_name']=bdn # Needed to suggest directory name for building libs

        if uoa not in res: res.append(uoa)

        env=rx['env']

        individual_env_script_body = rx['bat']

        q['bat'] = individual_env_script_body
        combined_env_script_body += individual_env_script_body

        if q.get('skip_from_bat','')!='yes':
           alternative_combined_env_script_body += individual_env_script_body

        pass_tags_to = q.get('pass_matching_tags_to', {})
        if pass_tags_to:
            resolved_tags = dd['tags']
            for tag_prefix in pass_tags_to:
                matching_tags = ','.join( [ matching_tag for matching_tag in resolved_tags if matching_tag.startswith(tag_prefix) ] )
                if matching_tags:
                    matching_tags = ','+matching_tags

                receiving_deps = pass_tags_to[tag_prefix]
                if type(receiving_deps) != list:
                    receiving_deps = [ receiving_deps ]
                for receiving_dep in receiving_deps:
                    deps[receiving_dep]['tags'] += matching_tags

    if o=='con':
       ck.out('  -----------------------------------')

    return {'return':0, 'deps':deps, 'env': env, 'bat':combined_env_script_body, 'cut_bat':alternative_combined_env_script_body, 'res_deps':res}

##############################################################################
# refresh environment (re-setup soft)

def refresh(i):
    """
    Input:  {
              (repo_uoa)          - repository UOA (with wildcards), default = local (to avoid updating other repos)
              (module_uoa)        - module UOA (with wildcards)
              (data_uoa)          - data UOA (with wildcards)

              (tags)              - prune by tags
              (target_os)         - prune by target OS
              (target_bits)       - prune by target bits
              (version)           - prune by version
              (name)              - prune by name with wildcards

              (reset_env)         - if 'yes', do not use environment from existing entry, but use original one
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              lst          - list from search function
              view         - sorted view list
            }

    """

    o=i.get('out','')

    ruoa = i.get('repo_uoa','') or 'local'
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')

    tags=i.get('tags','')

    extended_tags = [ tags ] if tags else []

    tos_uoa=i.get('target_os','')
    if tos_uoa!='':
        # Load OS
        ry=ck.access({'action':'load',
                     'module_uoa':cfg['module_deps']['os'],
                     'data_uoa':tos_uoa})
        if ry['return']>0: return ry

        tos_uoa = ry['dict'].get('base_uoa','') or ry['data_uoa']

        extended_tags.append( 'target-os-'+tos_uoa )

    tb = i.get('target_bits','')
    if tb!='': extended_tags.append( tb+'bits' )

    ver = i.get('version','')
    if ver!='': extended_tags.append( 'v'+ver )

    tags = ','.join(extended_tags)


    # FIXME: seems like the following bit was copied from show(), but the actual pattern matching bit was not, so there is no pattern matching actually.
    name=i.get('name','')
    wname=False
    if name.find('*')>=0 or name.find('?')>=0:
       import fnmatch
       wname=True
       name=name.lower()

    ii={'action':'search',
        'module_uoa':muoa,
        'repo_uoa':ruoa,
        'data_uoa':duoa,
        'tags':tags,
        'add_info':'yes',
        'add_meta':'yes'}
    rx=ck.access(ii)
    if rx['return']>0: return rx

    lst=rx['lst']

    # prepare view
    view=[]

    target_os_name={} # Caching target OS names

    for q in lst:
        duoa=q['data_uoa']
        duid=q['data_uid']

        ruoa=q['repo_uoa']
        ruid=q['repo_uid']

        info=q['info']
        meta=q['meta']

        cus=meta.get('customize',{})
        deps=meta.get('deps',{})
        setup=meta.get('setup','')
        tags=meta.get('tags',[])

        if 'tmp' in tags:
           continue

        tags_csv = ','.join( [t for t in tags if t] )

        host_os_uoa=setup.get('host_os_uoa','')
        target_os_uoa=setup.get('target_os_uoa','')
        tbits=setup.get('target_os_bits','')
        version=setup.get('version','')

        dname=info.get('data_name','')

        ck.out('***********************************************************************')
        ck.out(dname+' (Env: '+duid+')')

        ck.out('')
        ck.out('  Tags="'+tags_csv+'"')

        soft_uoa=meta.get('soft_uoa','')
        if soft_uoa=='':
           # Trying to detect the soft entry by "abstracting out" some of the tags:
           subtags=[]
           for q in tags:
               if not q.startswith('host-os-') and not q.startswith('target-os-') and \
                  not q.endswith('bits') and not q.startswith('v') and \
                  q!='retargeted':
                  subtags.append(q)

           subtags_csv = ','.join( [t for t in subtags if t] )

           ck.out('  All tags="'+tags_csv+'"')
           ck.out('  Searching soft UOA by tags="'+subtags_csv+'" ...')

           rx=ck.access({'action':'search',
                         'module_uoa':cfg['module_deps']['soft'],
                         'tags':subtags_csv})
           if rx['return']>0: return rx

           lst=rx['lst']
           if len(lst)==0:
              ck.out('')
              ck.out('  No soft found')

              rx=ck.inp({'text':'  Please, enter soft UOA: '})
              soft_uoa=rx['string'].strip()
           elif len(lst)==1:
              soft_uoa=lst[0]['data_uid']
              ck.out('     Unique soft UOA found='+lst[0]['data_uoa'])
           else:
              ck.out('')
              ck.out('  Available soft for these tags:')
              num={}
              ix=0
              for q in lst:
                  num[str(ix)]=q['data_uid']
                  ck.out('     '+str(ix)+') '+q['data_uoa'])
                  ix+=1

              rx=ck.inp({'text':'  Select one of the options for soft UOA: '})
              x=rx['string'].strip()

              if x not in num:
                 return {'return':1, 'error':'option is not recognized'}

              soft_uoa=num[x]

           meta['soft_uoa']=soft_uoa

           # Update environment entry
           rx=ck.access({'action':'update',
                         'module_uoa':work['self_module_uid'],
                         'data_uoa':duoa,
                         'data_name':dname,
                         'dict':meta,
                         'sort_keys':'yes'})
           if rx['return']>0: return rx

        # Check if package available to take env
        penv={}
        package_uoa=meta.get('package_uoa','')
        if package_uoa!='':
           ck.out('')
           ck.out('  Related package: '+package_uoa)

           rx=ck.access({'action':'load',
                         'module_uoa':cfg['module_deps']['package'],
                         'data_uoa':package_uoa})
           if rx['return']>0: return rx
           pdd=rx['dict']
           penv=pdd.get('env',{})

        # Trying new setup
        ck.out('')
        ck.out('  Refreshing setup ...')

        ii={'action':'setup',
            'module_uoa':cfg['module_deps']['soft'],
            'host_os':host_os_uoa,
            'target_os':target_os_uoa,
            'data_uoa':soft_uoa,
            'customize':cus,
            'deps':deps,
            'tags':tags_csv,
            'package_uoa':package_uoa,
            'skip_device_info_collection':'yes',
            'soft_name':dname,
            'env':penv,
            'env_data_uoa':duid}
        if i.get('reset_env','')!='': ii['reset_env']=i['reset_env']
        rx=ck.access(ii)
        if rx['return']>0: 
           rrx=rx['return']
           if rrx!=32 and rrx!=33:
              return rx
           if o=='con':
              if rrx==32:
                 ck.out('')
                 ck.out('One of the dependencies is missing for this CK environment!')
              elif rrx==33:
                 ck.out('')
                 ck.out('This environment has either missing dependencies or strange mismatch between registered software environment and current setup!')

              ck.out('')
              ry=ck.inp({'text':'Would you like to delete it (Y/n)? '})
              x=ry['string'].strip().lower()
              if x!='n' and x!='no':
                 ry=ck.access({'action':'delete',
                               'module_uoa':work['self_module_uid'],
                               'data_uoa':duid})
                 if ry['return']>0: return ry
           else:
              return rx

    return {'return':0}

##############################################################################
# internal function to convert host_os and target_os from UID to UOA to be readable

def readable_os(i):
    """
    Input:  {
              setup 
                (host_os_uoa)    - UID or UOA
                (target_os_uoa)  - UID or UOA
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              setup1       - processed setup with host_os_uoa and target_os_uoa as UOA
            }
    """

    original_setup = i.get('setup',{})

    import copy
    enriched_setup = copy.deepcopy( original_setup )

    for setup_key in ('host_os_uoa', 'target_os_uoa'):
        setup_value = original_setup.get(setup_key)
        if setup_value:
            r=ck.access({'action':'load',
                        'module_uoa':cfg['module_deps']['os'],
                        'data_uoa':setup_value})
            if r['return']>0: return r
            enriched_setup[setup_key]=r['data_uoa']

    return {'return':0, 'setup1':enriched_setup}

##############################################################################
# internal function: get value from list without error if out of bounds

def internal_get_val(lst, index, default_value):
    v=default_value
    if index<len(lst):
       v=lst[index]
    return v


##############################################################################
# parse 'A;B,C;D,~E,F' into [ [(True, A)], [(True, B), (True, C)], [(True, D), (False, E), (True, F)] ]

def parse_disjunction(disjunction):
    def parse_conjunction(conjunction):
        def parse_literal(literal):

            return (False, literal[1:]) if literal.startswith('~') else (True, literal)

        literals = [parse_literal(literal) for literal in conjunction.split(',')]

        return literals

    conjunctions = [parse_conjunction(conj) for conj in disjunction.split(';')] if len(disjunction) else []

    return conjunctions

##############################################################################
# Prune search list by no_tags

def prune_search_list(i):
    """
    Input:  {
              lst                    - list of entries after 'search'
              (or_tags)              - add entries which has groups of tags separated by ;
              (no_tags)              - string of tags to exclude
              (version_from)         - check version starting from ... (list of numbers)
              (version_to)           - check version up to ... (list of numbers)
              (package_uoa)          - prune by specific package
              (setup)                - prune by given setup dictionary
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              lst          - pruned list

              (skipped_because_of_version) - if 'yes', skip because of version check
            }
    """

    lst=i.get('lst',[])

    no_tags_csv = i.get('no_tags','')

    no_tags_set = set( no_tags_csv.split(',') if no_tags_csv!='' else [] )

    otags = parse_disjunction( i.get('or_tags','') )

    vfrom=i.get('version_from',[])
    vto=i.get('version_to',[])

    query_setup_dict=i.get('setup', {})

    pruned_lst=[]

    skipped_because_of_version=''

    query_package_uoa=i.get('package_uoa','')

    for entry in lst:
        meta=entry.get('meta',{})

        # Filter by package UOA
        if query_package_uoa:
            entry_package_uoa = meta.get('package_uoa','') or meta.get('customize',{}).get('used_package_uid','')
            if entry_package_uoa and entry_package_uoa!=query_package_uoa:
                continue

        entry_tags_set = set( meta.get('tags',[]) )

        # Filter out temporary entries (unfinished installation)
        if 'tmp' in entry_tags_set:
            continue

        # Filter out matches agains 'no_tags'
        if no_tags_set & entry_tags_set:
            continue

        # Filter by matching against 'or_tags' (full DNF support)
        if len(otags)>0:
            otags_ok = False
            for conjunction in otags:
                otags_ok = True
                for (bsign, t) in conjunction:
                    if (t in entry_tags_set) != bsign:    # Pythonic XOR
                        otags_ok = False        # if at least one member of conjunction is False, the whole conjunction is False
                        break
                if otags_ok:                    # if the current conjunction is True, the whole disjunction is True
                    break
            if not otags_ok:
                continue

        v=meta.get('setup',{}).get('version_split',[])

        # first check from env, but if not set, check from package
        if len(v)==0:
            v=meta.get('customize',{}).get('version_split',[])

        if len(v)==0:
            ver=meta.get('customize',{}).get('version','')

            if ver!='' and ver[0].isdigit():
                rx=ck.access({'action':'split_version',
                            'module_uoa':cfg['module_deps']['soft'],
                            'version':ver})
                if rx['return']>0: return rx
                v=rx['version_split']

                # NB: a side-effect: the result of version splitting is stored here:
                #
                entry['meta']['customize']['version_split'] = v

        if len(v)>0:
            if len(vfrom)>0:
                r=ck.access({'action':'compare_versions',
                            'module_uoa':cfg['module_deps']['soft'],
                            'version1':vfrom,
                            'version2':v})
                if r['return']>0: return r

                if r['result']=='>':
                    skipped_because_of_version='yes'
                    continue

            if len(vto)>0:
                r=ck.access({'action':'compare_versions',
                            'module_uoa':cfg['module_deps']['soft'],
                            'version1':v,
                            'version2':vto})
                if r['return']>0: return r

                if r['result']=='>':
                    skipped_because_of_version='yes'
                    continue

        entry_setup_dict = meta.get('setup')    # if entry_setup_dict is empty it matches anything
        if entry_setup_dict and len(query_setup_dict)>0:
            rx=ck.compare_dicts({'dict1':entry_setup_dict, 'dict2':query_setup_dict})       # check whether entry_setup_dict contains query_setup_dict
            if rx['return']>0: return rx
            if rx['equal']!='yes':
                continue

        # If we haven't hit "continue" anywhere above, the list element is ok to be included:
        pruned_lst.append(entry)

    return {'return':0, 'lst':pruned_lst, 'skipped_because_of_version':skipped_because_of_version}

##############################################################################
# remote env entry and installed package

def clean(i):
    """
    Input:  {
              (data_uoa) - entries to be cleaned (wildcards can be used)
              (repo_uoa)
              (tags)
              (force)    - if 'yes', force delete
              (f)        - if 'yes', force delete
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import copy
    import os
    import shutil

    o=i.get('out','')
    ooo = o if o=='con' else ''     # shouldn't we consider other options?

    force=i.get('force','')
    if force=='': force=i.get('f','')

    # If repo is not defined, use "local" to avoid removing env entries in other repos
    ruoa=i.get('repo_uoa','')
    if ruoa=='': ruoa='local'
    i['repo_uoa']=ruoa

    ii=copy.deepcopy(i)
    ii['action']='show'
    ii['out']=''

    r=ck.access(ii)
    if r['return']>0: return r

    lst=r['lst']

    # Check default path
    r=ck.access({'action':'prepare_install_path',
                 'module_uoa':cfg['module_deps']['package']})
    if r['return']>0: return r

    install_path=r['path']

    for q in lst:
        ruid=q['repo_uid']
        duid=q['data_uid']
        duoa=q['data_uoa']

        d=q['meta']
        info_data_name  = q.get('info',{}).get('data_name','UNKNOWN')
        tags_csv        = ','.join(d.get('tags',[]))

        cus=d.get('customize',{})
        full_path=cus.get('full_path','')
        absolute_package_install_path=''

        if full_path.startswith(install_path):
            if install_path.endswith(os.path.sep) or install_path.endswith('/'):    # is the first not enough?
                j=0
            else:
                j=1
            relative_path=full_path[len(install_path)+j:]

            package_install_dir_name=relative_path.split(os.path.sep)[0]

            if package_install_dir_name!='':
                absolute_package_install_path = os.path.join(install_path, package_install_dir_name)


        if absolute_package_install_path and os.path.isdir(absolute_package_install_path):
            display_location = ' package in dir "'+absolute_package_install_path+'" and'
        else:
            display_location = ''

        if force=='yes':
            delete_bool = True
        elif o=='con':
            r=ck.inp({'text':'Are you sure to delete'+display_location+' CK entry env:"'+duoa+'" - a '+info_data_name+' with tags: '+tags_csv+' (y/N): '})
            if r['return']>0: return r
            delete_bool = r['string'].strip().lower() == 'y'
        else:
            delete_bool = False

        if delete_bool:
            # Delete entry
            r=ck.access({'action':'rm',
                        'module_uoa':work['self_module_uid'],
                        'data_uoa':duid,
                        'repo_uoa':ruid,
                        'force': 'yes' if delete_bool else '',  # convert it to 'yes' string (whether originally 'yes' or 'y')
                        'out':ooo})
            if r['return']>0: return r

            # Delete package
            if absolute_package_install_path and os.path.isdir(absolute_package_install_path):
                shutil.rmtree(absolute_package_install_path)

    return {'return':0}

##############################################################################
# internal function to install package

def internal_install_package(i):
    """
    Input:  {
              (host_os)              - host OS (detect, if ommitted)
              (target_os)            - target OS (detect, if ommitted)
              (target_device_id)     - target device ID (detect, if omitted)
                     or
              (device_id)

              (package_uoa)          - fix package (useful for replay ...)
              (tags)                 - search UOA by tags (separated by comma)
              (or_tags)              - add entries which has groups of tags separated by ;
              (no_tags)              - exclude entris with these tags separated by comma

              (deps)                 - already resolved deps
              (sub_deps)             - deps for the package to be installed (for replay mainly)

              (reuse_deps)           - if 'yes' reuse all deps if found in cache by tags
              (deps_cache)           - list with resolved deps

              (quiet)                - if 'yes', automatically provide default answer to all questions when resolving dependencies ... 

              (install_to_env)       - install dependencies to env instead of CK-TOOLS (to keep it clean)!

              (install_env)          - customize installation (useful for replay to rebuild proper package with external env)

              (safe)                 - safe mode when searching packages first instead of detecting already installed soft
                                       (to have more deterministic build)

              (version_from)         - check version starting from ... (list of numbers)
              (version_to)           - check version up to ... (list of numbers)

              (add_hint)             - if 'yes', can skip package installation

              (rebuild)              - if 'yes', attempt to set env to avoid downloading package again, just rebuild (if supported)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              env_data_uoa - installed package data UOA (can be "" if not found)
              env_data_uid - installed package data UID (can be "" if not found)
            }

    """

    import os

    o=i.get('out','')
    ooo = o if o=='con' else ''     # shouldn't we consider other options?

    hos=i.get('host_os','')
    tos=i.get('target_os','')
    tdid=i.get('device_id','')
    package_uoa=i.get('package_uoa','')

    rebuild=i.get('rebuild','')

    deps_cache=i.get('deps_cache',[])
    reuse_deps=i.get('reuse_deps','')

    tags=i.get('tags','')
    or_tags=i.get('or_tags','')
    no_tags=i.get('no_tags','')
    quiet=i.get('quiet','')
    iev=i.get('install_to_env','')
    install_env=i.get('install_env',{})
    safe=i.get('safe','')
    ah=i.get('add_hint','')

    vfrom=i.get('version_from',[])
    vto=i.get('version_to',[])

    cdeps=i.get('deps',{})

    # Next, try to install via package for a given software
    if o=='con':
       ck.out('')
       ck.out('  Searching and installing CK software packages ...')
       if package_uoa!='':
          # Try to detect alias
          rx=ck.access({'action':'load',
                        'module_uoa':cfg['module_deps']['package'],
                        'data_uoa':package_uoa})
          if rx['return']>0: return rx
          package_uid=rx['data_uid']
          package_alias=rx['data_alias']

          ck.out('    * package UOA: '+package_alias+' ('+package_uid+')')
       ck.out('    * tags:        '+tags)
       ck.out('    * or tags:     '+or_tags)
       ck.out('    * no tags:     '+no_tags)
       ck.out('')

#          if quiet=='yes':
#             ck.out('  Searching and installing package with these tags automatically ...')
#             a='y'
#          else:
#             rx=ck.inp({'text':'  Would you like to search and install package with these tags automatically (Y/n)? '})
#             a=rx['string'].strip().lower()
#
#          if a!='n' and a!='no':
    try:
         save_cur_dir=os.getcwd()
    except OSError:
        os.chdir('..')
        save_cur_dir=os.getcwd()

    install_adict={'action':'install',
        'module_uoa':cfg['module_deps']['package'],
        'data_uoa':package_uoa,
        'out':ooo,
        'tags':tags,
        'or_tags':or_tags,
        'no_tags':no_tags,
        'install_to_env':iev,
        'env':install_env,
        'safe':safe,
        'host_os':hos,
        'target_os':tos,
        'device_id':tdid,
        'reuse_deps':reuse_deps,
        'deps_cache':deps_cache,
        'version_from':vfrom,
        'version_to':vto,
        'add_hint':ah}

    if rebuild=='yes': install_adict['rebuild']='yes'

    # Check if there is a compiler in resolved deps to reuse it
    sub_deps=i.get('sub_deps',{})
    if cdeps.get('compiler',{}).get('uoa','')!='': sub_deps['compiler']=cdeps['compiler']
    if cdeps.get('compiler-mcl',{}).get('uoa','')!='': sub_deps['compiler-mcl']=cdeps['compiler-mcl']
    if len(sub_deps)>0: install_adict['deps']=sub_deps

    duoa=''
    duid=''

    rx=ck.access(install_adict)
    if rx['return']==0:
       duoa=rx['env_data_uoa']
       duid=rx['env_data_uid']

       os.chdir(save_cur_dir)
    elif rx['return']!=16:  # 16 is a "magic number" meaning "user chose not to install" or "package not found"
       return rx

    return {'return':0, 'env_data_uoa':duoa, 'env_data_uid':duid}

##############################################################################
# DEPRECATED - use "ck virtual env" instead!
# set env for command line (pre-set various flags)

def xset(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    # Generate tmp file
    i['local']='yes'
    i['bat_file']='tmp-ck-env.bat'
    i['bat_new']='yes'
    i['print']='yes'

    return env_set(i)


##############################################################################
# pre-load environment for the shell

def virtual(i):
    """
    Input:  {
              data_uoa or uoa   - environment UOA to pre-load (see "ck show env")
              (tags)            - a combination of comma-separated tags to narrow down the search
              (or_tags)         - a combination of semicolon-separated and comma-separated tags to narrow down the search
              (tag_groups)      - independent groups of or_tags, separated by a space, refer to separate env entries
                                  that can be combined together: '--tag_groups=alpha,beta gamma,~delta epsilon;lambda,mu'
              (search_dict)     - require verbatim matches of some attributes
              (verbose)         - set to 'yes' to see the script that will be used to build the environment
              (shell_cmd)       - command line to run in the "environment-enriched" shell (make sure it is suitably quoted)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }
    Test:
        ck virtual env --tags=model,onnx,resnet --shell_cmd='echo $ML_MODEL_DATA_LAYOUT'

    """

    import copy

    duoa        = i.get('data_uoa', i.get('uoa','') )
    tag_groups  = i.get('tag_groups')
    list_of_updates = []

    if not duoa:
        list_of_uoa     = []
    elif ',' in duoa:      # TODO: becomes deprecated (but still works) in 1.10, becomes an error in 1.11
        # ck.out('')
        # ck.out('DEPRECATED: You seem to be using CSV format within a CID. Please list multiple CIDs on your command line instead.')
        # ck.out('')
        list_of_uoa = duoa.split(',')
    else:
        list_of_uoa = [ duoa ]

    for xcid in i.get('xcids',[]):
        if xcid['module_uoa'] == 'env':
            list_of_uoa.append( xcid['data_uoa'] )
        else:
            return {'return':1, 'error':"all CID entries have to be of 'env' type"}

    for uoa in list_of_uoa:
        if uoa:
            if '*' not in uoa:  # be a wildcard or be present!
                r = ck.access( {'action': 'load', 'module_uoa': 'env', 'data_uoa': uoa} )
                if r['return']>0: return r
            list_of_updates.append( {'uoa': uoa} )

    if tag_groups and len(tag_groups)>0:    # tag_groups are always added on top
        list_of_updates += [ {'or_tags': or_tags} for or_tags in tag_groups.split()]

    if not len(list_of_uoa) and ( i.get('tags') or i.get('or_tags') ):  # but make sure tags were seen at least once
        list_of_updates.append( {} )

    if not len(list_of_updates):    # if nothing else matched, let the user choose one env from the list
        list_of_updates.append( { 'uoa' : '*'} )

    prewrapper_lines  = []

    for dict_update in list_of_updates:
        env_set_alist = copy.deepcopy( i )
        env_set_alist.update( dict_update )

        r=env_set( env_set_alist )
        if r['return']>0: return r

        prewrapper_lines.append( r['bat'].strip() )

    return envsecute({ 'prewrapper_lines': prewrapper_lines, 'shell_cmd': i.get('shell_cmd'), 'verbose': i.get('verbose') })


################################################################################
# execute a shell command pre-wrapped with a given environment-modifying script

def envsecute(i):
    """
    Input:  {
                (prewrapper_lines)  - lines of the environment-setting pre-wrapper
                (shell_cmd)         - command line to run in the pre-wrapped shell (make sure it is suitably quoted)
                (verbose)           - set to 'yes' to see the pre_wrapper
            }

    Output: {
                return              - return code =  0, if successful
                                                  >  0, if error
                (error)             - error text if return > 0
            }
    Test:
            ck envsecute env @@@"{'prewrapper_lines': ['export ALPHA=alpha','echo 12345']}" --shell_cmd='echo $ALPHA $BETA'

    """

    # Run shell
    import platform
    import os
    import subprocess

    shell_cmd           = i.get('shell_cmd', None)
    prewrapper_lines    = i.get('prewrapper_lines', [])

    if i.get('verbose', '')=='yes':
        ck.out("*** Preloading the following environment:\n")
        ck.out("\n".join(prewrapper_lines))
        ck.out('')

    if not shell_cmd:
        ck.out('')
        ck.out('*** Warning: you are in a new shell with a pre-set CK environment. Enter "exit" to return to the original one!')

    if platform.system().lower().startswith('win'): # pragma: no cover

        if shell_cmd:
            prewrapper_lines.append( shell_cmd )
            termination_flag = '/C'     # terminate the CMD shell when the environment script & shell_cmd are over
        else:
            termination_flag = '/K'     # remain in the CMD shell

        shell_script_contents = ' & '.join( prewrapper_lines )

        p = subprocess.Popen(['cmd', termination_flag, shell_script_contents], shell = True, env=os.environ)
        p.wait()
        return_code  = p.returncode
    else:
        rx=ck.gen_tmp_file({'prefix': 'ck_envsecute_', 'suffix': '.sh'})
        if rx['return']>0: return rx
        prewrapper_filename=rx['file_name']

        shell_script_contents = '\n\n'.join( prewrapper_lines ) + '\n'

        rx=ck.save_text_file({'text_file':prewrapper_filename, 'string':shell_script_contents })
        if rx['return']>0: return rx

        full_cmd_list    = ['/bin/bash','--rcfile', prewrapper_filename, '-i'] + ( ['-c', shell_cmd] if shell_cmd else [] )

        return_code = subprocess.call(full_cmd_list, shell = False)

    return {'return':return_code, 'error':'Unknown error from the nested shell'}


##############################################################################
# return the install_location

def locate(i):
    """
    Input:  {
              (data_uoa or uoa) - environment entry/entries
              (tags)            - prune by tags
              (target_os)       - prune by target OS

            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    duoa        = i.get('data_uoa', i.get('uoa', '*') )
    tags_csv    = i.get('tags')

    tos_uoa     = i.get('target_os','')
    if tos_uoa!='':
        # Load OS
        ry=ck.access({'action':'load',
                     'module_uoa':cfg['module_deps']['os'],
                     'data_uoa':tos_uoa})
        if ry['return']>0: return ry

        tos_uoa = ry['dict'].get('base_uoa','') or ry['data_uoa']

        target_os_tag = 'target-os-'+tos_uoa
        i['tags'] = (tags_csv + ',' if tags_csv else '') + target_os_tag

    if duoa.find('*')!=-1 or duoa.find('?')!=-1 or tags_csv:
        searched_adict = ck.access( dict(i, action='search', out='') )
        if searched_adict['return']>0: return rx

        list_of_uoa = [ entry['data_uoa'] for entry in searched_adict['lst'] ]
    else:
        list_of_uoa = [ duoa ]

    install_locations = {}

    for uoa in list_of_uoa:

        loaded_adict = ck.access({'action':'load',
            'module_uoa':   'env',
            'data_uoa':     uoa,
        })
        if loaded_adict['return']>0: return loaded_adict

        install_location = loaded_adict.get('dict', {}).get('install_location', '')
        install_locations[uoa] = install_location

        if i.get('out')=='con':
            if len(list_of_uoa)>1:
                ck.out("env:{} -> {}".format(uoa, install_location))
            else:
                ck.out(install_location)

    return {'return': 0, 'install_locations': install_locations}


##############################################################################
# show the shell script for setting up this env

def cat(i):
    """
    Input:  {
              data_uoa or uoa   - environment UOA to pre-load (see "ck virtual env")
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    duoa        = i.get('data_uoa', i.get('uoa', '*') )
    tags_csv    = i.get('tags')

    if duoa.find(',')!=-1:      # TODO: becomes deprecated (but still works) in 1.10, becomes an error in 1.11
        # ck.out('')
        # ck.out('DEPRECATED: You seem to be using CSV format within a CID. Please list multiple CIDs on your command line instead.')
        # ck.out('')
        list_of_uoa = duoa.split(',')
    elif duoa.find('*')!=-1 or duoa.find('?')!=-1 or tags_csv:
        searched_adict = ck.access( dict(i, action='search') )
        if searched_adict['return']>0: return rx

        list_of_uoa = [ entry['data_uoa'] for entry in searched_adict['lst'] ]
    else:
        list_of_uoa = [ duoa ]

    for xcid in i.get('xcids',[]):
        if xcid['module_uoa'] == 'env':
            list_of_uoa.append( xcid['data_uoa'] )
        else:
            return {'return':1, 'error':"all CID entries have to be of 'env' type"}

    # Get some info about OS
    r=ck.access({'action':'detect',
        'module_uoa':cfg['module_deps']['platform.os'],
        'skip_info_collection':'yes',
    })
    if r['return']>0: return r
    hosd=r['host_os_dict']
    rem_marker  = hosd['rem']

    for uoa in list_of_uoa:

        loaded_adict = ck.access({'action':'load',
            'module_uoa':   'env',
            'data_uoa':     uoa,
        })
        if loaded_adict['return']>0: return loaded_adict

        entry_directory_path    = loaded_adict['path']
        env_script_name         = loaded_adict['dict'].get('env_script') or ( cfg['default_bat_name'] + hosd.get('script_ext','') )

        setup_script_path   = os.path.join( entry_directory_path, env_script_name)
        data_name           = loaded_adict['data_name']
        version             = loaded_adict['dict'].get('customize',{}).get('version', 'UNKNOWN_VERSION')
        tags_csv            = ','.join( loaded_adict['dict'].get('tags',[]) )

        header_lines = [
                    rem_marker,
                    '{} {}[ {} ver. {}, {} ]{}'.format(rem_marker, '-' * 20, data_name, version, setup_script_path, '-' * 20),
                    '{} Tags: {}'.format(rem_marker, tags_csv),
                    rem_marker,
        ]

        with open(setup_script_path, 'r') as setup_script_file:
            line_number = 0
            for input_line in setup_script_file:
                input_line = input_line.rstrip()
                ck.out( input_line )
                if not line_number:     # insert the auto-generated header right after the first line
                    for header_line in header_lines:
                        ck.out( header_line )
                line_number += 1

        ck.out( "\n\n" )

    return {'return':0}

##############################################################################
# remove tmp entries (when installation to env entry failed)

def rmtmp(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    i['action']='rm'
    i['data_uoa']='*'

    tags=i.get('tags','')
    if tags!='': tags+=','
    tags+='tmp'

    i['tags']=tags

    return ck.access(i)

##############################################################################
# get all versions from deps (recursively)

def get_all_versions_in_deps(i):
    """
    Input:  {
              deps        - deps dict
              (key)       - current key
              (only_root) - if 'yes', check only root keys

              (versions)  - current versions
              (tag_versions) - current versions by tags
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              versions     - all versions for all deps
              tag_versions     - all versions for all deps by tags
            }

    """

    deps=i['deps']
    key=i.get('key','')

    versions=i.get('versions',{})
    tversions=i.get('tversions',[])

    only_root=(i.get('only_root','')=='yes')

    for k in deps:
        xkey=key
        if xkey!='': xkey+='#'
        xkey+=k

        d=deps[k]

        dd=d.get('dict',{})

        tags=dd.get('tags',[])
        stags=','.join(tags)

        ver=d.get('ver','')

        versions[xkey]=ver

        if stags not in tversions:
           tversions.append(stags)

        deps2=dd.get('deps',{})
        if not only_root and len(deps2)>0:
           r=get_all_versions_in_deps({'deps':deps2, 'key':xkey, 'versions':versions, 'tag_versions':tversions})
           if r['return']>0: return r

    return {'return':0, 'versions':versions, 'tag_versions':tversions}

##############################################################################
# extracting summary of all deps

def deps_summary(i):
    """
    Input:  {
              deps - resolved deps
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              deps_summary - summary of deps
            }

    """

    deps=i['deps']
    ds=i.get('deps_summary',{})

    for x in deps:
        d=deps[x]
        dd=d.get('dict',{})

        ds[x]={}

        cx=dd.get('customize',{})

        ds[x]['tags']=d.get('tags',[])
        ds[x]['name']=d.get('name','')

        ds[x]['package_tags']=','.join(dd.get('tags',[]))
        ds[x]['data_name']=dd.get('data_name','')

        puoa=dd.get('package_uoa','')
        if puoa=='':
           puoa=d.get('cus',{}).get('used_package_uid','')
        ds[x]['package_uoa']=puoa

        ds[x]['version']=cx.get('version','')
        ds[x]['git_revision']=cx.get('git_info',{}).get('revision','')
        ds[x]['git_iso_datetime_cut_revision']=cx.get('git_info',{}).get('iso_datetime_cut_revision','')

        sdeps=dd.get('deps',{})
        if len(sdeps)>0:
           # Recursion
           r=deps_summary({'deps':sdeps})
           if r['return']>0: return r
           ds[x]['deps']=r['deps_summary']

    return {'return':0, 'deps_summary':ds}

##############################################################################
# delete env entries

def rm(i):
    """
    Input:  {
              (repo_uoa) - local by default
              (f)        - force removing
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    # Check that repo_uoa is local by default to avoid deleting permanent env in other entries

    ruoa=i.get('repo_uoa','')
    if ruoa=='': ruoa='local'
    i['repo_uoa']=ruoa

    i['common_func']='yes'

    return ck.access(i)

##############################################################################
# delete env entry

def delete(i):
    """
    Input:  { See rm function }
    Output: { See rm function }
    """

    return rm(i)

##############################################################################
# delete env entry

def remove(i):
    """
    Input:  { See rm function }
    Output: { See rm function }
    """

    return rm(i)
