#
# Collective Knowledge (checking and installing software)
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
env_install_path='CK_TOOLS'
env_search='CK_DIRS'

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
# detect is given software is already installed and register it in the CK or install it if package exists

def detect(i):
    """
    See "check" API
    """

    return check(i)

##############################################################################
# detect soft (internal function - gradually outdated)

def internal_detect(i):
    """
    Input:  {
              (host_os)           - host OS (detect, if omitted)
              (target_os)         - target OS (detect, if omitted)
              (target_device_id)  - target device ID (detect, if omitted)

              (data_uoa) or (uoa) - software UOA entry
               or
              (tags)              - search UOA by tags (separated by comma)

              (tool)              - force this tool name

              (env)               - if !='', use this env string before calling compiler (to set up env)

              (show)              - if 'yes', show output

              (force_version)     - if !='', use this version
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              version_str  - version as string
              version_lst  - version as list of strings
              version_raw  - raw list of strings (output of --version)
            }

    """

    import os

    o=i.get('out','')

    # Check host/target OS/CPU
    hos=i.get('host_os','')
    tos=i.get('target_os','')
    tdid=i.get('target_device_id','')

    r=ck.access({'action':'detect',
                 'module_uoa':cfg['module_deps']['platform.os'],
                 'host_os':hos,
                 'target_os':tos,
                 'target_device_id':tdid,
                 'skip_info_collection':'yes'})
    if r['return']>0: return r

    hos=r['host_os_uid']
    hosx=r['host_os_uoa']
    hosd=r['host_os_dict']

    tos=r['os_uid']
    tosx=r['os_uoa']
    tosd=r['os_dict']

    hplat=hosd['ck_name']
    tplat=tosd['ck_name']

    env=i.get('env','')

    ubtr=hosd.get('use_bash_to_run','')

    svarb=hosd.get('env_var_start','')
    svarb1=hosd.get('env_var_extra1','')
    svare=hosd.get('env_var_stop','')
    svare1=hosd.get('env_var_extra2','')
    sexe=hosd.get('set_executable','')
    sbp=hosd.get('bin_prefix','')
    envsep=hosd.get('env_separator','')
    scall=hosd.get('env_call','')
    sext=hosd.get('script_ext','')

    # Check soft UOA
    duoa=i.get('uoa','')
    if duoa=='': duoa=i.get('data_uoa','')
    if duoa=='':
       # Search
       tags=i.get('tags','')

       if tags!='':
          r=ck.access({'action':'search',
                       'module_uoa':work['self_module_uid'],
                       'tags':tags})
          if r['return']>0: return r
          l=r['lst']
          if len(l)>0:
             duid=l[0].get('data_uid')
             duoa=duid

    if duoa=='':
       return {'return':1, 'error':'software entry was not found'}

    # Load
    r=ck.access({'action':'load',
                 'module_uoa':work['self_module_uid'],
                 'data_uoa':duoa})
    if r['return']>0: return r
    d=r['dict']
    p=r['path']

    duoa=r['data_uoa']
    duid=r['data_uid']

    if o=='con':
       x=duoa
       if duid!=duoa: x+=' ('+duid+')'
       ck.out('Software description entry found: '+x)


    # Check if customize script is redirected into another entry:
    #
    another_entry_with_customize_script=d.get('use_customize_script_from_another_entry', None)
    if another_entry_with_customize_script:
       r=ck.access({'action':'find',
                    'module_uoa':   another_entry_with_customize_script.get('module_uoa', work['self_module_uid']),
                    'data_uoa':     another_entry_with_customize_script.get('data_uoa','')
                })
       if r['return']>0: return r
       customization_script_path = r['path']
    else:
       customization_script_path = p


    cs=None
    rx=ck.load_module_from_path({'path':customization_script_path, 'module_code_name':cfg['custom_script_name'], 'skip_init':'yes'})
    if rx['return']==0: 
       cs=rx['code']
    elif another_entry_with_customize_script or not rx['error'].startswith("can't find module code"):
       return rx

    # Checking name
    cus=d.get('customize',{})
    tool=i.get('tool','')
    if tool=='':
       if cus.get('soft_file_as_env','')!='':
          tool=svarb+cus['soft_file_as_env']+svare

       if cus.get('soft_file_not_tool','')!='yes':
          ry=prepare_target_name({'host_os_dict':hosd,
                                  'target_os_dict':tosd,
                                  'cus':cus})
          if ry['return']>0: return ry
          tool=ry['tool']

    # Preparing CMD
    soft_version_cmd=cus.get('soft_version_cmd',{}).get(hplat,'')

    if o=='con':
       ck.out('')
       ck.out('Prepared cmd: '+soft_version_cmd+' ...')

    # Check version (via customized script) ...
    ver=''
    lst=[]
    ii={'full_path':tool,
        'bat':env,
        'host_os_dict':hosd,
        'target_os_dict':tosd,
        'cmd':soft_version_cmd,
        'use_locale':cus.get('use_locale_for_version',''),
        'customize':cus,
        'custom_script_obj':cs,
        'data_uid': duid
    }
    if ck.cfg.get('minimize_soft_detect_output','')!='yes':
       ii['out']=o
    rx=get_version(ii)
    if rx['return']==0:
       ver=rx['version']
       lst=rx['version_lst']

    if ver=='':
       return {'return':16, 'error':'version was not detected'}

    # Split version
    rx=split_version({'version':ver})
    if rx['return']>0: return rx
    sver=rx['version_split']

    if i.get('show','')=='yes':
       ck.out('Output:')
       ck.out('')
       for q in lst:
           ck.out('  '+q)

    if o=='con':
       ck.out('')
       ck.out('Version detected: '+ver)

    return {'return':0, 'version_str':ver, 
                        'version_lst':sver, 
                        'version_raw':lst}

##############################################################################
# setup environment for a given software - 
# it is a low level routine which ask you the exact path to the tool and its version

def setup(i):
    """
    Input:  {
              (host_os)           - host OS (detect, if omitted)
              (target_os)         - target OS (detect, if omitted)
              (target_device_id)  - target device ID (detect, if omitted)

              (data_uoa) or (uoa) - soft configuration UOA
               or
              (tags)              - search UOA by tags (separated by comma)

              (soft_name)         - use this user friendly name for environment entry
              (soft_add_name)     - add extra name to above name (such as anaconda)

              (customize)         - dict with custom parameters 
                                    (usually passed to customize script)

                                    skip_add_dirs
                                    skip_add_to_path
                                    skip_add_to_bin
                                    skip_add_to_ld_path
                                    add_include_path

                                    skip_path - skiping installation path (for local versions)

                                    version      - add this version
                                    skip_version - if 'yes', do not add version

              (skip_path)         - skiping installation path (for local versions)

              (env)               - update default env with this dict

              (ienv)              - supply extra install_env overrides via this mechanism

              (deps)              - list with dependencies (in special format, possibly resolved (from package))

              (install_path)      - path with soft is installed
              (full_path)         - full path to a tool or library (install_path will be calculated automatically)

              (bat_file)          - if !='', record environment to this bat file, 
                                    instead of creating env entry

              (quiet)             - if 'yes', minimize questions

              (env_data_uoa)      - use this data UOA to record (new) env
              (env_repo_uoa)      - use this repo to record new env
              (env_new)           - if 'yes', do not search for environment (was already done in package, for example)

              (package_uoa)       - if called from package, record package_uoa just in case

              (reset_env)         - if 'yes', do not use environment from existing entry, but use original one

              (extra_version)     - add extra version, when registering software 
                                    (for example, -trunk-20160421)

              (skip_device_info_collection) - if 'yes', do not collect device info
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              env_data_uoa - environment entry UOA
              env_data_uid - environment entry UID

              deps         - resolved dependencies (if any)
            }

    """

    import os
    import json

    o=i.get('out','')

    env_new=i.get('env_new','')

    ########################################################################
    # Check host/target OS/CPU
    hos=i.get('host_os','')
    tos=i.get('target_os','')
    tdid=i.get('target_device_id','')
    if tdid=='': tdid=i.get('device_id','')

    ii={'action':'detect',
        'module_uoa':cfg['module_deps']['platform.os'],
        'host_os':hos,
        'target_os':tos,
        'target_device_id':tdid,
        'skip_info_collection':'no'}

    if i.get('skip_device_info_collection','')=='yes':
        ii['skip_info_collection']='yes'

    r=ck.access(ii)
    if r['return']>0: return r

    features=r.get('features',{})

    hos=r['host_os_uid']
    hosx=r['host_os_uoa']
    hosd=r['host_os_dict']

    tos=r['os_uid']
    tosx=r['os_uoa']
    tosd=r['os_dict']

    tbits=tosd.get('bits','')

    hplat=hosd['ck_name']
    tplat=tosd['ck_name']

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

    # Check soft UOA
    duoa=i.get('uoa','')
    if duoa=='': duoa=i.get('data_uoa','')

    tags=i.get('tags','')

    if duoa=='':
       xcids=i.get('xcids',[])
       if len(xcids)>0:
          duoa=xcids[0].get('data_uoa','')

    duid=duoa

    if duoa=='' and tags!='':
       r=ck.access({'action':'search',
                    'module_uoa':work['self_module_uid'],
                    'tags':tags})
       if r['return']>0: return r
       l=r['lst']
       if len(l)>0:
          duid=l[0].get('data_uid')
          duoa=duid

    d={}
    p=''

    ########################################################################
    if duoa=='':
       # Try to detect CID in current path
       rx=ck.detect_cid_in_current_path({})
       if rx['return']==0:
          duoa=rx.get('data_uoa','')

    if duoa!='':
       # Load defined or found soft entry
       r=ck.access({'action':'load',
                    'module_uoa':work['self_module_uid'],
                    'data_uoa':duoa})
       if r['return']>0: return r

       d=r['dict']
       p=r['path']

       duoa=r['data_uoa']
       duid=r['data_uid']

    if duoa=='':
       try:
           p=os.getcwd()
       except OSError:
           os.chdir('..')
           p=os.getcwd()

       pc=os.path.join(p, ck.cfg['subdir_ck_ext'], ck.cfg['file_meta'])

       found=False
       if os.path.isfile(pc):
          r=ck.load_json_file({'json_file':pc})
          if r['return']==0:
             d=r['dict']
             found=True

       if not found:
          return {'return':1, 'error':'software UOA (data_uoa) is not defined'}

    if o=='con':
       if duoa!='' and duid!='':
          x=': '+duoa
          if duid!=duoa: x+=' ('+duid+')'
       else:
          x=' in local directory'
       ck.out('  Software entry found'+x)

    # Check deps, customize, install path
    ltags=d.get('tags',[])
    deps=d.get('deps',{})
    env=d.get('env',{})
    cus=d.get('customize',{})
    pi=''

    csp=d.get('can_skip_path','')

    extra_version=i.get('extra_version', cus.get('extra_version',''))

    # Add tags from the search!
    for q in tags.split(','):
        q1=q.strip()
        if q1!='' and q1 not in ltags: ltags.append(q1)

    # Finish tags
    tg='host-os-'+hosx
    if tg not in ltags: ltags.append(tg)

    tg='target-os-'+tosx
    if tg not in ltags: ltags.append(tg)

    tg=tbits+'bits'
    if tg not in ltags: ltags.append(tg)

    ########################################################################
    # Check if environment already set (preload to update)
    enduoa=i.get('env_data_uoa','')
    enruoa=i.get('env_repo_uoa','')
    update=False

    if enduoa!='':
       rx=ck.access({'action':'load',
                     'module_uoa':cfg['module_deps']['env'],
                     'data_uoa':enduoa,
                     'repo_uoa':enruoa})
       if rx['return']==0:
          update=True

          edx=rx['dict']

          cus.update(edx.get('customize',{}))
          deps=edx.get('deps',{})
          if i.get('reset_env','')!='yes' and 'tmp' not in edx.get('tags',[]):
             env=edx.get('env',{})
          pi=cus.get('path_install','')

    # Update from input
    udeps=i.get('deps',{})
    deps.update(udeps)

    uenv=i.get('env',{})
    env.update(uenv)

    ucus=i.get('customize',{})
    cus.update(ucus)

    envp=cus.get('env_prefix','')
    envps=envp+'_SET'


    if i.get('soft_name','')!='':   # (direct input overrides meta-data)
       dname = i['soft_name']

    else:
       dname = d.get('soft_name','') + cus.get('package_extra_name', '')

    dname += i.get('soft_add_name','')


    ienv=i.get('ienv',{}) # override install_env using command-line options
    for ienv_key in ienv:
      if 'install_env' not in cus: # manual vivification
        cus['install_env'] = {}
      cus['install_env'][ienv_key] = ienv[ienv_key]

    pi1=i.get('install_path','')
    if pi1!='': pi=pi1

    fp=i.get('full_path','')

    ########################################################################
    # Check meta
    setup={'host_os_uoa':hos,
           'target_os_uoa':tos,
           'target_os_bits':tbits}

    # Resolve deps (if not ignored, such as when installing local version with all dependencies set)
    if cus.get('ignore_deps','')=='yes':
       deps={}

    sdeps=''
    sdeps1=''
    if len(deps)>0:
       ii={'action':'resolve',
           'module_uoa':cfg['module_deps']['env'],
           'host_os':hos,
           'target_os':tos,
           'target_device_id':tdid,
           'repo_uoa':enruoa,
           'deps':deps}
       if o=='con': ii['out']='con'

       rx=ck.access(ii)
       if rx['return']>0: return rx
       sdeps=rx['bat']
       sdeps1=rx['cut_bat']
       deps=rx['deps'] # Update deps (add UOA)

    for q in deps:
        v=deps[q]
        vuoa=v.get('uoa','') # can be undefined if OS specific
        if vuoa!='': setup['deps_'+q]=vuoa


    # Check if customize script is redirected into another entry:
    #
    another_entry_with_customize_script=d.get('use_customize_script_from_another_entry', None)
    if another_entry_with_customize_script:
       r=ck.access({'action':'find',
                    'module_uoa':   another_entry_with_customize_script.get('module_uoa', work['self_module_uid']),
                    'data_uoa':     another_entry_with_customize_script.get('data_uoa','')
                })
       if r['return']>0: return r
       customization_script_path = r['path']
    else:
       customization_script_path = p


    cs=None
    rx=ck.load_module_from_path({'path':customization_script_path, 'module_code_name':cfg['custom_script_name'], 'data_uoa':duoa ,'cfg':d, 'skip_init':'yes'})
    if rx['return']==0: 
       cs=rx['code']
    elif another_entry_with_customize_script or not rx['error'].startswith("can't find module code"):
       return rx


    ########################################################################
    ########################################################################
    ########################################################################
    ########################################################################
    # Starting processing soft

    # Check via full path first
    if pi=='' and fp=='' and o=='con' and cus.get('skip_path','')!='yes' and i.get('skip_path','')!='yes' and not update:
       ck.out('')

       ry=prepare_target_name({'host_os_dict':hosd,
                               'target_os_dict':tosd,
                               'cus':cus})
       if ry['return']>0: return ry
       sname=ry['tool']

       y0='installed library, tool or script'
       if sname!='': 
          suname=d.get('soft_name','')

          if cus.get('skip_soft_file_is_asked','')=='yes':
             if suname!='': y0=suname
          else:  
             y0=sname
             if suname!='': y0=suname+' ('+sname+')'

       y1='full path to '+y0

       y2=''
       y3=cus.get('soft_path_example',{}).get(hplat,'')
       if y3!='': y2=' (example: '+y3+')'

       r=ck.inp({'text':'Enter '+y1+y2+': '})
       fp=r['string'].strip()

    # Check if file really exists and check version if a tool
    ver=cus.get('version','')
    vercus=ver
    if fp!='':
       if cus.get('skip_file_check','')!='yes' and not os.path.exists(fp):
          return {'return':1, 'error':'software not found in a specified path ('+fp+')'}

       skip_existing='no'
       if cus.get('force_cmd_version_detection','')=='yes':
          skip_existing='yes'
          ver=''

       if ver=='':
          soft_version_cmd=cus.get('soft_version_cmd',{}).get(hplat,'')

          if o=='con':
             ck.out('')
             ck.out('  Attempting to detect version automatically (if supported) ...')

          # Check version (via customized script) ...
          ii={'full_path':fp,
              'bat':sdeps,
              'host_os_dict':hosd,
              'target_os_dict':tosd,
              'cmd':soft_version_cmd,
              'customize':cus,
              'custom_script_obj':cs,
              'skip_existing':skip_existing,
              'skip_add_target_file':cus.get('soft_version_skip_add_target_file',''),
              'use_locale':cus.get('use_locale_for_version',''),
              'data_uid': duid,
              'deps': deps,
          }
          if ck.cfg.get('minimize_soft_detect_output','')!='yes':
             ii['out']=o
          rx=get_version(ii)
          if rx['return']==0:
             ver=rx['version']
             if o=='con':
                ck.out('')
                ck.out('  Detected version: '+ver)
          elif rx['return']!=16 and rx['return']!=22:
             return rx
          else:
             if o=='con':
                ck.out('')
                ck.out('  WARNING: didn\'t manage to automatically detect software version!')

    ########################################################################
    # Get various git info ...
    ss1=''
    ss2=''
    ss3=''
    ss4=''
    ss5=''

    ver_to_search=ver

    if cus.get('use_git_revision','')=='yes':
       import datetime

       psrc=cus.get('git_src_dir','')

       dfp=i.get('full_path_install','')

       if dfp!='':
          if psrc!='':
             dfp=os.path.join(dfp, psrc)

          try:
              pwd1=os.getcwd()
          except OSError:
              os.chdir('..')
              pwd1=os.getcwd()

          if os.path.isdir(dfp):
             os.chdir(dfp)

             r=ck.access({'action':'run_and_get_stdout',
                          'module_uoa':cfg['module_deps']['os'],
                          'cmd':['git','rev-parse','--short','HEAD']})
             if r['return']==0 and r['return_code']==0: 
                ss1=r['stdout'].strip()

             r=ck.access({'action':'run_and_get_stdout',
                          'module_uoa':cfg['module_deps']['os'],
                          'cmd':['git','log','-1','--format=%cd']})
             if r['return']==0 and r['return_code']==0: 
                ss2=r['stdout'].strip()
                if ss2!='':
                   ss2x=ss2
                   j=ss2x.find(' +')
                   if j<0:
                      j=ss2x.find(' -')
                   if j>0:
                      ss2x=ss2[:j]

                   x=datetime.datetime.strptime(ss2x, '%a %b %d %H:%M:%S %Y')

                   ss3=x.isoformat()

                   ss4=ss3[:10].replace('-','')

                   if ss1!='':
                      ss5=ss4+'-'+ss1

             if 'git_info' not in cus:
                cus['git_info']={}

             cus['git_info']['revision']=ss1
             cus['git_info']['datetime']=ss2
             cus['git_info']['iso_datetime']=ss3
             cus['git_info']['iso_datetime_cut']=ss4
             cus['git_info']['iso_datetime_cut_revision']=ss5

             if o=='con':
                ck.out('')
                if ss1!='':
                   ck.out('Detected GIT revision:                 '+ss1)
                if ss2!='':
                   ck.out('Detected GIT date time of last commit: '+ss2)

             os.chdir(pwd1)

             ver+='-'+ss1

    ########################################################################
    # Check if force version
    x=i.get('force_version','').strip()
    if x!='': ver=i['force_version'] 

    ########################################################################
    # Ask for version if was not detected or is not explicitly specified (for example, from a package)
    if ver==''  and cus.get('skip_version','')!='yes' and o=='con':
       ck.out('')
       r=ck.inp({'text':'Enter version of this software (for example, 3.21.6-2 or press Enter if default/unknown): '})
       ver=r['string'].strip().lower()
       ver_to_search=ver

    # Add extra, if needed (useful for changing trunks)
    if extra_version!='':
       ver+=extra_version
       ver_to_search+=extra_version

    # If customized version has changed, try to check env again ...
    if vercus!=ver:
       env_new='no'

    # Split version
    rx=split_version({'version':ver})
    if rx['return']>0: return rx
    sver=rx['version_split']

    # Add version to setup and separate into tags
    setup['version']=ver_to_search
    setup['version_split']=sver

    # Prepare tags from version
    if ver!='': 
       x=''
       for q in sver:
           if x!='':x+='.'
           x+=str(q)

           tg='v'+x

           if tg not in ltags:
              ltags.append(tg)

    unsplit_version_tag_prefix = cus.get('unsplit_version_to_tags_prefixed_with')
    if unsplit_version_tag_prefix != None:      # NB: empty string is treated differently from absence!
        ltags.append( unsplit_version_tag_prefix + ver_to_search )

    tags_csv = ','.join( [t.strip() for t in ltags if t] )

    ########################################################################
    # Search if environment is already registered for this version
    # (to delete or reuse it)
    finish=False
    if enduoa=='' and env_new!='yes':
       if o=='con':
          ck.out('')
          ck.out('Searching if environment already exists using:')
          ck.out('  * Tags: '+tags_csv)
          if len(deps)>0:
             for q in deps:
                 v=deps[q]
                 vuoa=v.get('uoa','')
                 if vuoa!='':
                    ck.out('  * Dependency: '+q+'='+v.get('uoa',''))

       r=ck.access({'action':'search',
                    'module_uoa':cfg['module_deps']['env'],
                    'repo_uoa':enruoa,
                    'tags':tags_csv,
                    'search_dict':{'setup':setup}})
       if r['return']>0: return r
       lst=r['lst']

       if len(lst)>0:
          fe=lst[0]

          enduoa=fe['data_uoa']
          enduid=fe['data_uid']

          if o=='con':
             x=enduoa
             if enduid!=enduoa: x+=' ('+enduid+')'

             ck.out('')
             ck.out('Environment already registered for this version: '+x)

             update=False
             if i.get('update','')=='yes':
                update=True

             if not update:
                if o=='con':
                   ck.out('')

                   if i.get('quiet','')=='yes':
                      dl='y'
                   else:
                      r=ck.inp({'text':'Would you like to delete this entry and re-register environment (Y/n): '})
                      dl=r['string'].strip().lower()

                   if dl=='' or dl=='y' or dl=='yes':
                      update=False

                      rx=ck.access({'action':'delete',
                                    'module_uoa':cfg['module_deps']['env'],
                                    'data_uoa':enduoa,
                                    'repo_uoa':enruoa})
                      if rx['return']>0: return rx

                   else:
                      ck.out('')
                      r=ck.inp({'text':'Would you like to update this entry (Y/n): '})
                      upd=r['string'].strip().lower()

                      if upd=='' or upd=='y' or upd=='yes':
                         update=True
                      else:
                         finish=True

             if update:
                rx=ck.access({'action':'load',
                              'module_uoa':cfg['module_deps']['env'],
                              'data_uoa':enduoa,
                              'repo_uoa':enruoa})
                if rx['return']>0: return rx

                edx=rx['dict']

                cus1=edx.get('customize',{})
                deps1=edx.get('deps',{})
                env1=edx.get('env',{})

                cus.update(cus1)
                deps.update(deps1)
                env.update(env1)

                pi=cus.get('path_install','')

       else:
          if o=='con':
             ck.out('')
             ck.out('    Environment with above tags is not yet registered in CK ...')

    ############################################################
    if not finish:
       # Prepare environment and batch
       sb=''

       if o=='out':
          ck.out('')
          ck.out('Preparing environment and batch file ...')

       sdirs=hosd.get('dir_sep','')

       wb=tosd.get('windows_base','')

       rem=hosd.get('rem','')
       eset=hosd.get('env_set','')
       svarb=hosd.get('env_var_start','')
       svare=hosd.get('env_var_stop','')

       evs=hosd.get('env_var_separator','')
       eifs=hosd.get('env_quotes_if_space','')

       ellp=hosd.get('env_ld_library_path','')
       if ellp=='': ellp='LD_LIBRARY_PATH'
       elp=hosd.get('env_library_path','')
       if elp=='': elp='LIBRARY_PATH'

       # Check installation path
       if fp=='' and cus.get('skip_path','')!='yes' and i.get('skip_path','')!='yes' and not update:
          if o=='con':
#             if update:
#                ck.out('')
#                ck.out('Current path to installed tool: '+pi)
#                r=ck.inp({'text':'Input new path to installed tool or press Enter to keep old: '})
#                pix=r['string'].strip()
#                if pix!='': pi=pix
             if pi=='':
                ck.out('')

                ye=cus.get('input_path_example','')
                if ye!='': y=' (example: '+ye+')'
                else: y=''

                y1=cus.get('input_path_text','')
                if y1=='': y1='path to installed software (root directory possibly pointing to bin, lib, include, etc)'
 
                r=ck.inp({'text':'Enter '+y1+y+': '})
                pi=r['string'].strip().strip('"')

                ipr=cus.get('input_path_remove','')
                if ipr!='' and ipr>0:
                   for q in range(0,ipr):
                       try:
                          pi=os.path.split(pi)[0]
                       except:
                          pass

          if pi=='' and csp!='yes':
             return {'return':1, 'error':'installation path is not specified'}

       if fp!='':
          cus['full_path']=fp

       if pi!='':
          cus['path_install']=pi

       ### OLD start
       if cus.get('skip_add_dirs','')!='yes' and pi!='':
          if cus.get('add_include_path','')=='yes' and cus.get('path_include','')=='':
             pii=pi+sdirs+'include'
             cus['path_include']=pii

          if cus.get('skip_add_to_bin','')!='yes':
             pib=pi
             if cus.get('skip_add_bin_ext','')!='yes': pib+=sdirs+'bin'
             cus['path_bin']=pib

          if cus.get('skip_add_to_ld_path','')!='yes' and cus.get('path_lib','')=='':
             plib=pi+sdirs+'lib64'
             if not os.path.isdir(plib):
                plib=pi+sdirs+'lib32'
                if not os.path.isdir(plib):
                   plib=pi+sdirs+'lib' 
                   if not os.path.isdir(plib):
                      return {'return':1, 'error':'can\'t find lib path'}
             cus['path_lib']=plib
       else:
          cus['skip_path']='yes'
       ### OLD stop

       # If install path has space, add quotes for some OS ...
       xs=''
       if pi.find(' ')>=0 and eifs!='':
          xs=eifs


       # Check if customize script is redirected into another entry:
       #
       another_entry_with_customize_script=d.get('use_customize_script_from_another_entry', None)
       if another_entry_with_customize_script:
          r=ck.access({'action':'find',
                       'module_uoa':   another_entry_with_customize_script.get('module_uoa', work['self_module_uid']),
                       'data_uoa':     another_entry_with_customize_script.get('data_uoa','')
                   })
          if r['return']>0: return r
          customization_script_path = r['path']
       else:
          customization_script_path = p


       cs=None
       rx=ck.load_module_from_path({'path':customization_script_path, 'module_code_name':cfg['custom_script_name'], 'data_uoa':duoa ,'cfg':d, 'skip_init':'yes'})
       if rx['return']==0: 
          cs=rx['code']
       elif another_entry_with_customize_script or not rx['error'].startswith("can't find module code"):
          return rx


       sadd=''
       if cs!=None and 'setup' in dir(cs):
          # Prepare info
          rx=ck.gen_tmp_file({})
          if rx['return']>0: return rx
          fn=rx['file_name']

          # Call setup script
          ii={"host_os_uoa":hosx,
              "host_os_uid":hos,
              "host_os_dict":hosd,
              "target_os_uoa":tosx,
              "target_os_uid":tos,
              "target_os_dict":tosd,
              "target_device_id":tdid,
              "soft_uoa":duoa,
              "soft_name":dname,
              "tags":ltags,
              "cfg":d,
              "env":env,
              "deps":deps,
              "deps_copy":i.get('deps_copy',{}),
              "customize":cus,
              "self_cfg":cfg,
              "version":ver,
              "version_split":sver,
              "features":features,
              "ck_kernel":ck
             }

          if o=='con': ii['interactive']='yes'
          if i.get('quiet','')=='yes': ii['interactive']=''

          rx=cs.setup(ii)
          if rx['return']>0: return rx

          sadd=rx['bat']
          pi=cus.get('path_install','')

          if cus.get('soft_name','')!='':
              dname=cus['soft_name']

          if cus.get('soft_extra_name','')!='':
              dname+=cus['soft_extra_name']

       #########################################################
       # Finish batch
       sb+=hosd.get('batch_prefix','')+'\n'

       check_if_set=hosd.get('batch_check_if_set','')
       if check_if_set!='':
          sb+=check_if_set.replace('$#ck_var#$',envps)+'\n'

       x=duoa
       if duid!=duoa: x+=' ('+duid+') '
       if len(tags)>0:
          y=''
          for q in ltags:
              if y!='': y+=','
              y+=q
          x+=' ('+y+')'
       sb+=rem+' '+'Soft UOA           = '+x+'\n'

       sb+=rem+' '+'Host OS UOA        = '+hosx+' ('+hos+')\n'
       sb+=rem+' '+'Target OS UOA      = '+tosx+' ('+tos+')\n'
       sb+=rem+' '+'Target OS bits     = '+tbits+'\n'
       if ver!='':
          sb+=rem+' '+'Tool version       = '+ver+'\n'
          cus['version']=ver
       if len(sver)>0:
          sb+=rem+' '+'Tool split version = '+json.dumps(sver)+'\n'
          cus['version_split']=sver
       sb+='\n'

       if sdeps!='':
          sb+=rem+' Dependencies:\n'
          sb+=sdeps1+'\n'

       if cus.get('skip_path','')!='yes' and i.get('skip_path','')!='yes' and pi!='':
          sb+=eset+' '+envp+'='+xs+pi+xs+'\n'
          cus['path_install']=pi

       envp_b=envp+'_BIN'
       pib=cus.get('path_bin','')
       envp_l=envp+'_LIB'
       plib=cus.get('path_lib','')
       envp_i=envp+'_INCLUDE'
       piib=cus.get('path_include','')

       if cus.get('skip_add_dirs','')!='yes': # and pi!='':
          if pib!='' and cus.get('skip_add_to_bin','')!='yes': 
             sb+=eset+' '+envp_b+'='+xs+pib+xs+'\n'
             if hplat=='win':
                rcc=ck.access({'action':'convert_to_cygwin_path',
                               'module_uoa':cfg['module_deps']['os'],
                               'path':pib})
                if rcc['return']==0:
                   sb+=eset+' '+envp_b+'_CYGWIN='+xs+rcc['path']+xs+'\n'

          if plib!='': 
             sb+=eset+' '+envp_l+'='+xs+plib+xs+'\n'
             if hplat=='win':
                rcc=ck.access({'action':'convert_to_cygwin_path',
                               'module_uoa':cfg['module_deps']['os'],
                               'path':plib})
                if rcc['return']==0:
                   sb+=eset+' '+envp_l+'_CYGWIN='+xs+rcc['path']+xs+'\n'

          if piib!='': 
             sb+=eset+' '+envp_i+'='+xs+piib+xs+'\n'
             if hplat=='win':
                rcc=ck.access({'action':'convert_to_cygwin_path',
                               'module_uoa':cfg['module_deps']['os'],
                               'path':piib})
                if rcc['return']==0:
                   sb+=eset+' '+envp_i+'_CYGWIN='+xs+rcc['path']+xs+'\n'

       if sadd!='':
          sb+='\n'+sadd

       # Add all env
       for k in sorted(env):
           v=str(env[k])

           if eifs!='' and wb!='yes':
              if v.find(' ')>=0 and not v.startswith(eifs):
                 v=eifs+v+eifs

           sb+=eset+' '+k+'='+v+'\n'
       sb+='\n'

       # Add to existing vars
       if cus.get('add_to_path','')=='yes' or (cus.get('skip_add_to_path','')!='yes' and cus.get('skip_add_to_bin','')!='yes' and cus.get('skip_dirs','')!='yes' and pi!=''):
          sb+=eset+' PATH='+svarb+envp_b+svare+evs+svarb+'PATH'+svare+'\n'

       if pi!='' and cus.get('skip_add_to_ld_path','')!='yes' and cus.get('skip_dirs','')!='yes':
          sb+=eset+' '+elp+'='+svarb+envp_l+svare+evs+svarb+elp+svare+'\n'
          sb+=eset+' '+ellp+'='+svarb+envp_l+svare+evs+svarb+ellp+svare+'\n'

       # Say that environment is set (to avoid recursion)
       sb+=eset+' '+envps+'=1\n'

       # Finish environment batch file
       if wb=='yes':
          sb+='\n'
          sb+='exit /b 0\n'

       # Check if save to bat file *****************************************************************************************
       bf=i.get('bat_file', '')
       pnew=''

       if bf=='':
          bf=cfg['default_bat_name']+hosd.get('script_ext','')

          # Preparing to add or update entry
          xx='added'

          ltags=sorted(ltags)

          dd={'tags':ltags,
              'setup':setup,
              'env':env,
              'deps':deps,
              'soft_uoa':duid,
              'customize':cus,
              'env_script':bf}

          if duid!='':
             dd['soft_uoa']=duid

          pduoa=i.get('package_uoa','')
          if pduoa!='':
             dd['package_uoa']=pduoa

          # Probably should have come from pi, but there are too many sources of pi !
          #
          install_location = i.get('install_path', i.get('full_path_install', ''))
          dd['install_location'] = install_location

          ii={'action':'add',
              'module_uoa':cfg['module_deps']['env'],
              'dict':dd,
              'sort_keys':'yes',
              'substitute':'yes'}

          if enduoa!='': ii['data_uoa']=enduoa
          if enruoa!='': ii['repo_uoa']=enruoa

          if update:
             ii['action']='update'
             xx='updated'

          # Adding/updating
          if dname!='':
             ii['data_name']=dname

          rx=ck.access(ii)
          if rx['return']>0: return rx

          enduoa=rx['data_uoa']
          enduid=rx['data_uid']

          pnew=rx['path']

          if o=='con':
             ck.out('')
             ck.out('Environment entry '+xx+' ('+enduoa+')!')

       # Record batch file
       if pnew=='': pb=bf
       else:        pb=os.path.join(pnew, bf)

       # Write file
       rx=ck.save_text_file({'text_file':pb, 'string':sb})
       if rx['return']>0: return rx

    return {'return':0, 'env_data_uoa':enduoa, 'env_data_uid':enduid, 'deps':deps}

##############################################################################
# search tool in pre-defined paths

def search_tool(i):
    """
    Input:  {
              path_list             - path list
              file_name             - name of file to find (can be with patterns)
              (recursion_level_max) - if >0, limit dir recursion
              (can_be_dir)          - if 'yes', return matched directories as well
              (return_symlinks)     - if 'yes', symlinks are returned as-is. Otherwise, they're resolved
            }

    Output: {
              return       - return code =  0, if successful
                                            >  0, if error
              (error)      - error text if return > 0

              list         - list of file (see ck.list_all_files)
              elapsed_time - elapsed time

            }
    """

    o=i.get('out','')

    import time
    import os
    start_time = time.time()

    pl=i['path_list']
    fn=i['file_name']
    pt=''

    rlm=i.get('recursion_level_max',0)
    cbd=i.get('can_be_dir','')
    return_symlinks = i.get('return_symlinks','')

    if fn.find('?')>=0 or fn.find('*')>=0:
       pt=fn
       fn=''

    lst=[]

    for p in pl:
        if o=='con':
           ck.out('    * Searching in '+p+' ...')

        r=list_all_files({'path':p, 
                          'file_name':fn, 
                          'pattern':pt,
                          'can_be_dir':cbd,
                          'recursion_level_max':rlm})
        if r['return']>0: return r
        lst.extend( r['list'] )

#    if return_symlinks != 'yes':
#      # resolving symlinks
#      lst = [os.path.realpath(p) for p in lst]
#      #removing duplicates
#      recorded_paths = set()
#      record_path = recorded_paths.add
#      lst = [p for p in lst if not (p in recorded_paths or record_path(p))]

    elapsed_time = time.time() - start_time

    return {'return':0, 'list':lst, 'elapsed_time':elapsed_time}


##############################################################################
# A helper function for list_all_files()

def _internal_check_encoded_path_is_dir( path ):
    """
        Need this complex structure to support UTF-8 file names in Python 2.7
    """

    import os
    import sys

    try:
        if os.path.isdir( path ):
            return path
    except Exception as e:

        try:
            path = path.encode('utf-8')
            if os.path.isdir( path ):
                return path
        except Exception as e:

            try:
                path = path.encode(sys.stdin.encoding)
                if os.path.isdir(p):
                    return path
            except Exception as e:
                pass

    return None

##############################################################################
# List all files recursively in a given directory

def list_all_files(i):
    """
    Input:  {
              path                  - top level path
              (file_name)           - search for a specific file name
              (pattern)             - return only files with this pattern
              (path_ext)            - path extension (needed for recursion)
              (can_be_dir)          - if 'yes', return matched directories as well
              (recursion_level_max) - if >0, limit dir recursion
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              list         - list of found files
            }
    """

    import sys
    import os

    list_of_results=[]

    fname               = i.get('file_name', '')
    fname_with_sep_bool = fname.find(os.sep)>=0

    can_be_dir          = i.get('can_be_dir', '')
    can_be_dir_bool     = can_be_dir == 'yes'

    pattern=i.get('pattern','')
    if pattern!='':
        import fnmatch

    pe = i.get('path_ext', '')
    po = i.get('path', '')
    if sys.version_info[0]<3: po=unicode(po)

    rl=i.get('recursion_level',0)
    rlm=i.get('recursion_level_max',0)

    if rl>rlm:
        return {'return':0, 'list':[]}

    try:
        dirList=os.listdir(po)
    except Exception as e:
        pass
    else:
        for fn in dirList:
            p=''
            try:
                p=os.path.join(po, fn)
            except Exception as e:
                pass

            if p!='':
                candidate = None
                if fname!='':
                    if fname_with_sep_bool and os.path.isdir(p):
                        deep_candidate = os.path.join(po, fname)
                        if os.path.exists( deep_candidate ):
                            candidate = deep_candidate

                    elif fname==fn:
                        candidate = p

                elif pattern!='' and fnmatch.fnmatch(fn, pattern):
                    candidate = p

                if candidate and (candidate not in list_of_results):
                    if os.path.isfile( candidate ) or (can_be_dir_bool and os.path.isdir( candidate )):
                        list_of_results.append( candidate )

                if _internal_check_encoded_path_is_dir(p):
                    r=list_all_files({'path':p, 'path_ext':os.path.join(pe, fn),
                                   'pattern':pattern, 'file_name':fname, 'can_be_dir':can_be_dir,
                                   'recursion_level':rl+1, 'recursion_level_max':rlm})
                    if r['return']>0: return r
                    list_of_results.extend( r.get('list',[]) )

    return {'return':0, 'list':list_of_results}

##############################################################################
# detect is given software is already installed and register it in the CK or install it if package exists

def check(i):
    """
    Input:  {
              (target)            - if specified, use info from 'machine' module
                 or
              (host_os)           - host OS (detect, if omitted)
              (target_os)         - target OS (detect, if omitted)
              (target_device_id)  - target device ID (detect, if omitted)

              (data_uoa) or (uoa) - software UOA entry
               or
              (tags)              - search UOA by tags (separated by comma)

              (interactive)       - if 'yes', and has questions, ask user
              (quiet)             - if 'yes', do not ask questions but select default value

              (default_selection) - default value for the selection from the menu
              (first_match)       - in case of match ambiguity in menu selection, just take the first match

              (skip_help)         - if 'yes', skip print help if not detected (when called from env setup)

              (deps)              - already resolved deps (if called from env)

              (dep_add_tags.{KEY})   - extra tags added to specific subdictionary of deps{} for this particular resolution session

              (extra_version)     - add extra version, when registering software 
                                    (for example, -trunk-20160421)
                                    Be careful - if there is auto version detection,
                                    CK will say that version has changed and will try to remove entry!

              (extra_tags)         - add extra tags to separate created entry from others 
                                     (for example Python 2.7 vs Anaconda Python 2.7)

              (extra_name)         - add extra name to soft (such as anaconda)

              (force_env_data_uoa) - force which env UID to use when regstering detect software -
                                     useful when reinstalling broken env entry to avoid breaking
                                     all dependencies of other software ...

              (search_dirs)        - extra directories where to search soft (string separated by comma)
              (search_dir)         - search only in this directory (useful for Spack and EasyBuild)

              (search_depth)       - force directory recursive search depth when detecting installed software

              (soft_name)          - name to search explicitly

              (version_from)       - check version starting from ... (string or list of numbers)
              (version_to)         - check version up to ... (string list of numbers)

              (force_version)      - if !='', use this version

              (full_path)          - force full path (rather than searching in all directories)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              path_install - path to the detected software
              cus          - dict with filled in info for the software
            }

    """

    import os
    import json
    import copy

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

    # Check host/target OS/CPU
    hos=i.get('host_os','')
    tos=i.get('target_os','')
    tdid=i.get('target_device_id','')

    r=ck.access({'action':'detect',
                 'module_uoa':cfg['module_deps']['platform.os'],
                 'host_os':hos,
                 'target_os':tos,
                 'target_device_id':tdid,
                 'skip_info_collection':'yes'})
    if r['return']>0: return r

    hos=r['host_os_uid']
    hosx=r['host_os_uoa']
    hosd=r['host_os_dict']

    tos=r['os_uid']
    tosx=r['os_uoa']
    tosd=r['os_dict']

    tosd.update(device_cfg.get('update_target_os_dict',{}))

    tbits=tosd.get('bits','')

    hplat=hosd.get('ck_name','')
    tplat=tosd.get('ck_name','')

    # Check versions
    vfrom=i.get('version_from',[])
    vto=i.get('version_to',[])

    if type(vfrom)!=list:
       rx=split_version({'version':vfrom})
       if rx['return']>0: return rx
       vfrom=rx['version_split']

    if type(vto)!=list:
       rx=split_version({'version':vto})
       if rx['return']>0: return rx
       vto=rx['version_split']

    tags=i.get('tags','')

    # Check soft UOA
    duoa=i.get('uoa', '')
    if duoa=='': duoa=i.get('data_uoa','')
    requested_muoa=i.get('module_uoa','')


    if duoa=='' and requested_muoa=='':
       # Try to detect CID in current path
       rx=ck.detect_cid_in_current_path({})
       if rx['return']==0:
          duoa=rx.get('data_uoa','')

    if tags:  # if tags are available, try searching both in tags and variations
        r=ck.access({'action':          'search_in_variations',
                    'data_uoa':         duoa,
                    'module_uoa':       'misc',
                    'query_module_uoa': work['self_module_uid'],
                    'tags':             tags,
        })
        if r['return']>0: return r
        l=r['lst']
        if len(l)>1:    # FIXME: we could be smarter and assume several soft_candidates from the very start,
                        #           merging all the options found into one big selector.

            ck.out("Found {} soft candidate entries matching tags '{}' :".format(len(l), tags))
            for candidate in l:
                candidate_tags      = candidate['meta']['tags']
                required_variations = candidate['required_variations']
                ck.out("\tck detect soft:{:<42}    # --tags={}".format(candidate['data_uoa'], ','.join(candidate_tags+required_variations)) )
            return {'return':1, 'error': "Please use a command that uniquely defines a soft: entry"}
        elif len(l)==1:
            r=l[0]
            soft_entry_dict=r['meta']
            required_variations=r['required_variations']
        else:
            return {'return':1, 'error':'software entry was not found'}

    elif duoa:  # if tags were not available, try to load directly
        r=ck.access({'action':'load',
                    'module_uoa':work['self_module_uid'],
                    'data_uoa':duoa,
        })
        if r['return']>0: return r

        soft_entry_dict=r['dict']
        required_variations = []
    else:
        return {'return':1, 'error':'please define either --data_uoa or --tags or both to get going'}

    duoa=r['data_uoa']
    duid=r['data_uid']
    soft_entry_path=r['path']

    cus=soft_entry_dict.get('customize',{})

    ########################################################################
    # Check env from input
    envx=copy.deepcopy(i.get('env',{}))
    ienv=copy.deepcopy(i.get('install_env',i.get('ienv',{})))   # parse install_env overrides out of install_env{}, install_env.XXX and ienv.XXX CLI options
    for q in i:
        if q.startswith('env.'):
           envx[q[len('env.'):]]=i[q]
        elif q.startswith('ienv.'):
           ienv[q[len('ienv.'):]]=i[q]
        elif q.startswith('install_env.'):
           ienv[q[len('install_env.'):]]=i[q]

    supported_variations = soft_entry_dict.get('variations', {})
    missing_variations = set(required_variations) - set(supported_variations)
    if missing_variations:
        return {'return':1, 'error':'Variations {} are not supported by soft:{}'.format(missing_variations, duoa)}

    # Update this cus from all the supported variations.
    # Detect if an incompatible mix of variation tags was required
    # that would lead to undefined behaviour, and bail out if so.
    #
    if required_variations:
        extra_env_from_variations = {}
        extra_cus_from_variations = {}

        for req_variation in required_variations:
            extra_env = supported_variations[req_variation].get('extra_env',{})
            colliding_vars = set(extra_env_from_variations.keys()) & set(extra_env.keys()) # non-empty intersection means undefined behaviour
            for coll_var in colliding_vars:     # have to check actual values to detect a mismatch
                if extra_env_from_variations[coll_var] != extra_env[coll_var]:
                    return { 'return':1,
                             'error':'contradiction on variable ({}) detected when adding "{}" variation tag'.format(coll_var,req_variation)}

            extra_cus = supported_variations[req_variation].get('extra_customize',{})
            colliding_cuss = set(extra_cus_from_variations.keys()) & set(extra_cus.keys()) # non-empty intersection means undefined behaviour
            for coll_cus in colliding_cuss:     # have to check actual values to detect a mismatch
                if extra_cus_from_variations[coll_cus] != extra_env[coll_cus]:
                    return { 'return':1,
                             'error':'contradiction on customize ({}) detected when adding "{}" variation tag'.format(coll_cus,req_variation)}

            extra_env_from_variations.update( extra_env )   # merge of one particular variation
            extra_cus_from_variations.update( extra_cus )

        ienv.update( extra_env_from_variations )  # merge of all variations
        cus.update( extra_cus_from_variations )


    extra_version=i.get('extra_version', cus.get('extra_version',''))


    # Check if restricts dependency to a given host or target OS
    rx=check_target({'dict':cus,
                     'host_os_uoa':hosx,
                     'host_os_dict':hosd,
                     'target_os_uoa':tosx,
                     'target_os_dict':tosd})
    if rx['return']>0: return rx


    # Check if need to resolve dependencies
    deps=i.get('deps',{})

    dep_add_tags  = i.get('dep_add_tags', {})
    for q in i:
        if q.startswith('deps.'):
           preset_deps[q[5:]]=i[q].split(':')[-1]
        elif q.startswith('dep_add_tags.'):
           _ , dep_name    = q.split('.')
           dep_add_tags[dep_name] = i[q]

    sbat=''
    if len(deps)==0:
       deps=soft_entry_dict.get('deps',{})

       if len(deps)>0:
          ii={'action':'resolve',
              'module_uoa':cfg['module_deps']['env'],
              'host_os':hos,
              'target_os':tos,
              'target_device_id':tdid,
              'deps':deps,
#              'env':envx,
              'dep_add_tags': dep_add_tags,
              'env':copy.deepcopy(envx),
              'install_env':ienv,
              'out':oo}
          rx=ck.access(ii)
          if rx['return']>0: return rx

          sbat=rx['bat']

#    if o=='con':
#       x=duoa
#       if duid!=duoa: x+=' ('+duid+')'
#       ck.out('Software description entry found: '+x)

    rr={'return':0}


    # Check if customize script is redirected into another entry:
    #
    another_entry_with_customize_script=soft_entry_dict.get('use_customize_script_from_another_entry', None)
    if another_entry_with_customize_script:
       r=ck.access({'action':'find',
                    'module_uoa':   another_entry_with_customize_script.get('module_uoa', work['self_module_uid']),
                    'data_uoa':     another_entry_with_customize_script.get('data_uoa','')
                })
       if r['return']>0: return r
       customization_script_path = r['path']
    else:
       customization_script_path = soft_entry_path


    cs=None
    rx=ck.load_module_from_path({'path':customization_script_path, 'module_code_name':cfg['custom_script_name'], 'skip_init':'yes'})
    if rx['return']==0: 
       cs=rx['code']
    elif another_entry_with_customize_script or not rx['error'].startswith("can't find module code"):
       return rx


    soft_version_cmd=cus.get('soft_version_cmd',{}).get(hplat,'')

    # Decide where to search depending on the Operating System
    #
    # 1) list all the potential places:
    #
    dir_candidates = []

    extra_search_dirs_universal = cus.get('extra_search_dirs_universal', [])
    dir_candidates.extend( extra_search_dirs_universal )

    extra_search_dirs = cus.get('extra_search_dirs', {}).get(hplat, [])
    dir_candidates.extend( extra_search_dirs )

    if cus.get('detect_in_soft_dir_only', '')=='yes':
        dir_candidates.append(
            soft_entry_path
        )
    else:
        if hplat=='win':
            dir_candidates.extend([
                os.environ.get('ProgramW6432', ''),
                os.environ.get('ProgramFiles(x86)', ''),
                os.environ.get('ProgramFiles', ''),
                'C:\\Program Files',
                'D:\\Program Files',
                'C:\\Program Files (x86)',
                'D:\\Program Files (x86)',
            ])
        else:
            dir_candidates.extend([
                '/usr',
                '/opt',
            ])
            if hosd.get('macos'):           # MacOSX is currently treated as a flavour of Linux
                dir_candidates.extend([
                    '/usr/local/Cellar',    # The location of software installed by brew prior to softlinking
                ])

        dir_candidates.append(
            os.environ.get(env_install_path, '')                    # from CK_TOOLS env
        )

        dir_separator   = ';' if hplat=='win' else ':'
        dir_candidates.extend(
            os.environ.get(env_search, '').split( dir_separator )   # from CK_DIRS
        )

        dir_candidates.extend(
            i.get('search_dirs', '').split(',')                     # from input
        )

        from os.path import expanduser
        dir_candidates.append(
            expanduser("~")                                         # from user space
        )

        if cus.get('detect_in_soft_dir', '')=='yes':
            dir_candidates.append(
                soft_entry_path
            )

    #
    # 2) filter through the candidates to find suitable and unique ones:
    #
    sdirs=hosd.get('dir_sep','')
    dirs=[]
    for candidate in dir_candidates:
        if candidate:
            candidate=candidate.replace('$#sep#$', sdirs)
            if os.path.isdir(candidate) and candidate not in dirs:
                dirs.append(candidate)


    # Check if interactive
    iv='yes'
    quiet=i.get('quiet','')
    if quiet=='yes' or o!='con': iv=''

    # If there is a function to customize dirs, call it
    if 'dirs' in dir(cs):
       ii={"host_os_uoa":hosx,
           "host_os_uid":hos,
           "host_os_dict":hosd,
           "target_os_uoa":tosx,
           "target_os_uid":tos,
           "target_os_dict":tosd,
           "target_device_id":tdid,
           "soft_entry_path":soft_entry_path,   # This is also a valid path suitable for soft detection (but not by default)
           "cfg":soft_entry_dict,
           "install_env":ienv,
           "self_cfg":cfg,
           "ck_kernel":ck,
           "dirs":dirs,
           "interactive":iv
          }
       rx=cs.dirs(ii)
       if rx['return']>0: return rx
       if rx.get('dirs'): dirs=rx['dirs']   # If anything was returned at all, trust that value, even if it is empty.
                                            # NB: Otherwise it may be the case that the original list was modified as a side effect.

    # Check if substitute all search dirs via kernel!
    x=ck.cfg.get('soft_search_dirs','')
    if x!='':
       dirs=x.split(',')

    # Check if substitute by 1 dir
    if i.get('search_dir','')!='':
       dirs=[i['search_dir'].strip()]

    # Check which file to search for
    sname=i.get('soft_name','')
    if sname=='':
       ry=prepare_target_name({'host_os_dict':hosd,
                               'target_os_dict':tosd,
                               'cus':cus})
       if ry['return']>0: return ry
       sname=ry['tool']

    cbd=cus.get('soft_can_be_dir','')

    sen=cus.get('soft_extra_name','')

    osname=sname
    if sname=='':
       return {'return':1, 'error':'software description doesn\'t have a name of file to search ...'}

    # Check if search for extensions gcc-4.9, clang-3.8, etc
    if hplat=='linux' and cus.get('search_numeric_ext_on_linux','')=='yes':
       sname+='*'

    # Search tools
    suname=soft_entry_dict.get('soft_name','')
    x=sname
    if suname!='': x=suname+' ('+sname+')'

    ck.out('')
    ck.out('  Searching for '+x+' to automatically register in the CK - it may take some time, please wait ...')
    ck.out('')

    # Check directory recursion depth customization when searching for installed software
    xrlm=i.get('search_depth','')
    if xrlm=='':
       xrlm=ck.cfg.get('force_soft_search_depth','')
       if xrlm=='':
          xrlm=cus.get('limit_recursion_dir_search_all','')

    if xrlm!='':
       rlm=int(xrlm)
    else:
       rlm=cus.get('limit_recursion_dir_search',{}).get(hplat,0)

    skip_sort='no'

    fp=i.get('full_path','')
    if fp!='':
       lst=[fp]
    else:
       rx=search_tool({'path_list':dirs, 'file_name':sname, 'recursion_level_max':rlm, 'can_be_dir':cbd, 'out':'con'})
       if rx['return']>0: return rx

       lst=rx['list']
       et=rx['elapsed_time']

       # Limit to required ones
       if 'limit' in dir(cs):
          rx=cs.limit({'list':lst,
                       'host_os_dict':hosd,
                       'target_os_dict':tosd,
                       'soft_name':osname,
                       'ck_kernel':ck})
          if rx['return']>0: return rx
          lst=rx['list']
          if rx.get('skip_sort','')!='': skip_sort=rx['skip_sort']

    # Print results
#    if o=='con':
       ck.out('')
       ck.out('  Search completed in '+('%.1f' % et)+' secs. Found '+str(len(lst))+' target files (may be pruned) ...')

    # Select, if found
    il=0
    if len(lst)>0:
       # Trying to detect version
       if o=='con':
          ck.out('')
          ck.out('  Detecting and sorting versions (ignore some work output) ...')

       vlst=[]

#       FGG: decided to remove after discussing with LLNL because often picks up strange path instead of correct one ...

#       # Sometimes can be the same paths (due to soft links) - remove:
#       lst1=[]
#       lst2=[]
#       for q in reversed(lst):
#           q2=os.path.realpath(q)
#           if q2 not in lst2:
#              lst1.append(q)
#              lst2.append(q2)
#       lst=reversed(lst1) # return to original order if need to avoid sorting

       # Process each path
       if o=='con':
          ck.out('')

       for q in lst:
           kk={'path':q}

           pr=''
           if o=='con':
              pr='    * '+q

           # Try to detect version
           ver=''
           sver=[]
           ii={'full_path':q,
               'bat':sbat,
               'host_os_dict':hosd,
               'target_os_dict':tosd,
               'cmd':soft_version_cmd,
               'use_locale':cus.get('use_locale_for_version',''),
               'customize':cus,
               'custom_script_obj':cs,
               'data_uid': duid,
               'deps': deps
           }
           if ck.cfg.get('minimize_soft_detect_output','')!='yes':
              ii['out']=o
           rx=get_version(ii)
           if rx['return']>0:
              if o=='con':
                 pr+='\n        WARNING: '+rx['error']
           else:
              ver=rx['version']

              # Split version
              rx=split_version({'version':ver})
              if rx['return']>0: return rx
              sver=rx['version_split']

              kk['version']=ver
              kk['version_detected']=ver
              kk['version_split']=sver

              if o=='con':
                 pr+='   (Version '+ver+')'

           skip=False
           if len(vfrom)>0:
              r=compare_versions({'version1':vfrom, 'version2':sver})
              if r['return']>0: return r
              if r['result']=='>':  skip=True

           if not skip and len(vto)>0:
              r=compare_versions({'version1':sver, 'version2':vto})
              if r['return']>0: return r
              if r['result']=='>':  skip=True

           if skip: pr+=' - skipped because of version constraints!'

           if o=='con':
              ck.out(pr)

           if not skip and (cus.get('add_only_with_version','')!='yes' or ver!=''):
              vlst.append(kk)

       if o=='con':
          ck.out('')

       # Sort by version
       if skip_sort!='yes':
          vlst=sorted(vlst, key=lambda k: (internal_get_val(k.get('version_split',[]), 0, 0),
                                           internal_get_val(k.get('version_split',[]), 1, 0),
                                           internal_get_val(k.get('version_split',[]), 2, 0),
                                           internal_get_val(k.get('version_split',[]), 3, 0),
                                           internal_get_val(k.get('version_split',[]), 4, 0),
                                           k.get('path','')),
                     reverse=True)

       lst = [ q['path'] for q in vlst ]

       if len(lst)>1:
          if o=='con':
             ck.out('')

          default_selection = i.get('default_selection', '0')

          if iv=='yes':
                ck.out('  Registering software installations found on your machine in the CK:')
                ck.out('')
                ck.out('    (HINT: enter -1 to force CK package installation)')
                ck.out('')

                ver_options = []

                for kk in vlst:
                    q=kk['path']
                    ver=kk.get('version','')

                    ver_options.append( 'Version {} - {}'.format(ver, q) if ver else q )

                select_adict = ck.access({'action': 'select_string',
                                    'module_uoa': 'misc',
                                    'options': ver_options,
                                    'default': default_selection,
                                    'question': 'Please select the number of any above installation',
                                    'first_match': i.get('first_match', ''),
                })
                if select_adict['return']>0: return select_adict

                il = select_adict.get('selected_index', -1)

                if il<0:
                    return {'return':1, 'error':'selection number is not recognized'}

    # If not found, quit
    if len(lst)==0:
       if i.get('skip_help','')!='yes':
          r=print_help({'data_uoa':duid, 'platform':hplat})
          # Ignore output

       return {'return':16, 'error':'software was not automatically found on your system! Please, install it and re-try again!'}

    # Check if CK install dict already exists
    pf=lst[il]

    env_data_uoa=i.get('force_env_data_uoa','')

    puoa=''

    dname=''
    xtags=''

    rx=find_config_file({'full_path':pf, 'data_uid': duid})
    if rx['return']>0: return rx
    found=rx['found']

    if found=='yes':
       dx=rx['dict']

       cus=dx.get('customize',{})

       extra_version=dx.get('extra_version','')

       if dx.get('env_data_uoa','')!='' and env_data_uoa=='':
          env_data_uoa=dx['env_data_uoa']

       dname=soft_entry_dict.get('soft_name','')
       if cus.get('package_extra_name','')!='':
          dname+=cus['package_extra_name']

       puoa=dx.get('package_uoa','')

       xtags=dx.get('tags','')

       # FGG: should I add deps here or not - the thing is that the env 
       # most likely changed so probably not ...

       # New update -> I can now restore UIDs with deps, so maybe it's ok ...

       if o=='con':
          ck.out('')
          ck.out('  Found pre-recorded CK installation info ...')

    # Merge all relevant tags:
    extra_tags=i.get('extra_tags','').strip()

    extra_tags_set  = set( extra_tags.split(',') ) if extra_tags else set()
    main_tags_set   = set( xtags.split(',') )
    vari_tags_set   = set( required_variations )

    xtags = ','.join( list( main_tags_set | vari_tags_set | extra_tags_set ) )

    en=i.get('extra_name','')
    if en!='':
       en=' '+en

    # Attempt to register in CK
    if o=='con':
       ck.out('')
       ck.out('  Registering in the CK ('+pf+') ...')
       ck.out('')

    ii={'data_uoa':duid,
        'customize':cus,
        'full_path':pf,
        'quiet':quiet,
        'host_os':hos,
        'target_os':tos,
        'target_device_id':tdid,
        'deps':deps,
        'env':envx,
        'ienv':ienv,
        'env_data_uoa':env_data_uoa,
        'soft_name':dname,
        'soft_add_name':en,
        'package_uoa':puoa,
        'extra_version':extra_version,
        'tags':xtags,
        'out':oo}

    if cus.get('collect_device_info','')!='yes':
        ii['skip_device_info_collection']='yes'

    if i.get('force_version','')!='':
        ii['force_version']=i['force_version']

    rz=setup(ii)
    if rz['return']>0: return rz

    xeduoa=rz['env_data_uoa']
    xeduid=rz['env_data_uid']

    if o=='con':
       ck.out('  Successfully registered with UID: '+xeduid)

    return rz

##############################################################################
# get version of a given software (internal)

def get_version(i):
    """
    Input:  {
              full_path
              bat
              cmd

              custom_script_obj
              host_os_dict

              (show)                 - if 'yes', show output file

              (skip_existing)        - if 'yes', force detecting version again
              (skip_add_target_file) - if 'yes', do not add target file at the beginning 
                                       of CMD to detect version

              (use_locale)           - if 'yes', use locale to decode output
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              version      - string version
              version_lst  - raw output (as list)
            }

    """

    import os

    o=i.get('out','')

    fp=i.get('full_path','')
    sb=i.get('bat','')
    soft_version_cmd=i.get('cmd')
    data_uid    = i.get('data_uid')

    cs=i.get('custom_script_obj', None)
    cus=i.get('customize',{})   # should we be more strict [] here?

    hosd=i.get('host_os_dict',{})
    tosd=i.get('target_os_dict',{})

    bprefix=hosd.get('batch_prefix','')
    ubtr=hosd.get('use_bash_to_run','')
    svarb=hosd.get('env_var_start','')
    svarb1=hosd.get('env_var_extra1','')
    svare=hosd.get('env_var_stop','')
    svare1=hosd.get('env_var_extra2','')
    sexe=hosd.get('set_executable','')
    sbp=hosd.get('bin_prefix','')
    envsep=hosd.get('env_separator','')
    scall=hosd.get('env_call','')
    sext=hosd.get('script_ext','')
    eifsc=hosd.get('env_quotes_if_space_in_call','')
    nout=hosd.get('no_output','')
    deps=i.get('deps',{})

    sb=bprefix+sb

    ver=''
    lst=[]
    cmd=''

    # Attempt to check via CK config file
    if i.get('skip_existing','')!='yes':
       rx=find_config_file({'full_path':fp, 'data_uid': data_uid})
       if rx['return']>0: return rx
       found=rx['found']
       if found=='yes':
          ver=rx['dict'].get('customize',{}).get('version','')

    if ver=='':
       # Preparing CMD
       if 'version_cmd' in dir(cs):
          rx=cs.version_cmd({'full_path':fp,
                             'host_os_dict':hosd,
                             'target_os_dict':tosd,
                             'cmd':soft_version_cmd,
                             'ck_kernel':ck,
                             'customize':cus,
                             'out':o,
                             'deps':deps})
          if rx['return']>0: return rx
          cmd=rx.get('cmd','')
          ver=rx.get('version','')

       elif soft_version_cmd:
          if eifsc!='' and fp.find(' ')>=0 and not fp.startswith(eifsc):
             fp=eifsc+fp+eifsc

          if o!='con':
             cmd+=nout

          if i.get('skip_add_target_file','')=='yes':
             cmd+=' '+soft_version_cmd
          else:
             cmd+=fp+' '+soft_version_cmd

    if ver=='' and cmd:

       # Generate tmp file
       rx=ck.gen_tmp_file({})
       if rx['return']>0: return rx
       ftmp=rx['file_name']
 
       cmd=cmd.replace('$#filename#$', ftmp)

       if o=='con':
          cmdz=cmd.replace('\n','\n         ')
          ck.out('')
          ck.out('       ==============================')
          ck.out('       Prepared CMD to detect version:')
          ck.out('         '+cmdz.strip())

       # Finalizing batch file
       sb+='\n'+cmd+'\n'

       # Record to tmp batch and run
       rx=ck.gen_tmp_file({'prefix':'tmp-', 'suffix':sext, 'remove_dir':'no'})
       if rx['return']>0: return rx
       fnb=rx['file_name']

       rx=ck.save_text_file({'text_file':fnb, 'string':sb})
       if rx['return']>0: return rx

       # Executing script
       y=''
       if sexe!='':
          y+=sexe+' '+fnb+envsep
       y+=' '+scall+' '+fnb

       if ubtr!='': y=ubtr.replace('$#cmd#$',y)

       if o=='con':
          ck.out('')
          ck.out('       Executing "'+y+'" ...')

       ry=os.system(nout+y)
       # ignore return code (checking output file instead)

       os.remove(fnb)

       if os.path.isfile(ftmp): 
          import sys
          import locale

          en=sys.stdout.encoding
          if i.get('use_locale','')=='yes':
             en=locale.getdefaultlocale()[1]

          success=True
          for xen in [en, sys.stdout.encoding, locale.getdefaultlocale()[1]]:

             try:
                rx=ck.load_text_file({'text_file':ftmp, 'split_to_list':'yes', 'encoding':en})
             except UnicodeDecodeError:
                success=False

             if success:
                break

          if success:
             if rx['return']>0: return rx
             lst=rx['lst']

          if os.path.isfile(ftmp):
             os.remove(ftmp)

       if len(lst)==0:
          return {'return':16, 'error':'version output file is empty'}

       if i.get('show','')=='yes':
          ck.out('       Output:')
          ck.out('')
          for q in lst:
              ck.out('         '+q)

       if 'parse_version' in dir(cs):
         # Calling customized script to parse version
         ii={'output':lst,
             'host_os_dict':hosd,
             'full_path':fp,
             'ck_kernel':ck}
         rx=cs.parse_version(ii)
         if rx['return']>0 and rx['return']!=16: return rx

         ver=rx.get('version','')

       else:
          ck.out('parse_version() method is not defined => attempting to parse it trivially')
          ver = lst[0].strip()

    if ver=='':
       return {'return':16, 'error':'version was not detected'}

    if o=='con':
       ck.out('')
       ck.out('        Version detected: '+ver)
       ck.out('')

    return {'return':0, 'version':ver, 'version_lst':lst} 

##############################################################################
# internal function: get value from list without error if out of bounds

def internal_get_val(lst, index, default_value):
    v=default_value
    if index<len(lst):
       v=lst[index]
    return v

##############################################################################
# print help for this software entry

def print_help(i):
    """
    Input:  {
              data_uoa - data UOA to get help
              platform - platform name 
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    duoa=i['data_uoa']
    hplat=i['platform']

    ti=''
    # If only one related software entry found, try to read text notes from it 
    rx=ck.access({'action':'find',
                  'module_uoa':work['self_module_uid'],
                  'data_uoa':duoa})
    if rx['return']>0: return rx
    pppx=rx['path']

    ppx=os.path.join(pppx,'install.txt')
    if os.path.isfile(ppx):
       rx=ck.load_text_file({'text_file':ppx})
       if rx['return']==0:
          ti+=rx['string']

    ppx=os.path.join(pppx,'install.'+hplat+'.txt')
    if os.path.isfile(ppx):
       rx=ck.load_text_file({'text_file':ppx})
       if rx['return']==0:
          if ti!='': ti+='\n'
          ti+=rx['string']

    if ti!='':
       read=True

       ck.out('****** Installation notes: ******')

       ck.out(ti)

       ck.out('*********************************')

    else:
       # Show possible Wiki page
       rx=ck.inp({'text':'       Would you like to open wiki pages about installation and other info (if exists) (Y/n): '})
       x=rx['string'].strip().lower()

       if x!='n' and x!='no':
          ck.out('')
          rx=ck.access({'action':'wiki',
                        'module_uoa':work['self_module_uid'],
                        'data_uoa':duoa})
          if rx['return']>0: return rx
          ck.out('')

    return {'return':0}

##############################################################################
# check that host and target OS is supported

def check_target(i):
    """
    Input:  {
              dict           - dictionary with info about supported host and target OS

              host_os_uoa    - host OS UOA  (already resolved)
              host_os_dict   - host OS dict (already resolved)

              target_os_uoa  - target OS UOA  (already resolved)
              target_os_dict - target OS UOA  (already resolved)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    cus=i['dict']

    hosx=i['host_os_uoa']
    hosd=i['host_os_dict']

    tosx=i['target_os_uoa']
    tosd=i['target_os_dict']

    # Check if restricts dependency to a given host or target OS
    only_hos=cus.get('only_for_host_os',[])
    if len(only_hos)>0:
       if hosx not in only_hos:
          return {'return':1, 'error':'host OS is not supported by this software'}

    only_hos1=cus.get('only_for_host_os_tags',[])
    if len(only_hos1)>0:
       x=hosd.get('tags',[])
       found=False
       for xx in only_hos1:
           if xx in x:
              found=True
              break
       if not found:
          return {'return':1, 'error':'host OS family is not supported by this software'}

    only_tos=cus.get('only_for_target_os',[])
    if len(only_tos)>0:
       if tosx not in only_tos:
          return {'return':1, 'error':'target OS is not supported by this software'}

    only_tos1=cus.get('only_for_target_os_tags',[])
    if len(only_tos1)>0:
       x=tosd.get('tags',[])
       found=False
       for xx in only_tos1:
           if xx in x:
              found=True
              break
       if not found:
          return {'return':1, 'error':'target OS family is not supported by this software'}

    return {'return':0}

##############################################################################
# split version

def split_version(i):
    """
    Input:  {
              version - string version
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              version_split - split version
            }

    """

    import re

    ver=i['version']

    # Split version
    sver=[]
    if ver!='':
       if ver!='':
          sver1=re.split('\.|\-|\_', ver)
          for q in sver1:
              x=q
              try:
                 x=int(q)
              except:
                 #pass - causes problems when mixing strings and ints ...
                 x=0
              sver.append(x)

    return {'return':0, 'version_split':sver}

##############################################################################
# show available software descriptions

def show(i):
    """
    Input:  {
               (the same as list; can use wildcards)
               (out_file) - output to file (for mediawiki)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os
    import copy

    o=i.get('out','')

    of=i.get('out_file','')
    if of!='':
       xof=os.path.splitext(of)

    html=False
    if o=='html' or i.get('web','')=='yes':
       html=True

    h=''
    h2=''
    if i.get('new','')=='yes':
       ii=copy.deepcopy(i)
       ii['action']='preload_html_for_lists'
       ii['module_uoa']=cfg['module_deps']['misc']
       ii['ck_title']='Shared CK software detection plugins'
       r=ck.access(ii)
       if r['return']>0: return r

       h=r['html_start']+'\n'
       h2=r['html_stop']+'\n'

    unique_repo=False
    if i.get('repo_uoa','')!='': unique_repo=True

    ii=copy.deepcopy(i)

    ii['out']=''
    ii['action']='list'
    ii['add_meta']='yes'
    ii['time_out']=-1

    rx=ck.access(ii)
    if rx['return']>0: return rx

    ll=sorted(rx['lst'], key=lambda k: k['data_uoa'])

    if html:
       h+='<h2>Please check our new <a href="http://ReuseResearch.com/c.php?c=soft">beta browser</a> for CK components!</h2>\n'

       h+='<br>\n'
       h+='You can detect installed software and register it in the CK as follows:\n'
       h+='<pre>\n'
       h+=' ck pull repo:{Repo UOA - see below}\n'
       h+=' ck detect soft:{Soft UOA - see below}\n'
       h+='</pre>\n'

       h+='using tags:\n'
       h+='<pre>\n'
       h+=' ck detect soft --tags={some tags from below}\n'
       h+='</pre>\n'

       h+='in an unusual path:\n'
       h+='<pre>\n'
       h+=' ck detect soft:{Soft UOA - see below} --search_dirs={path to this software}\n'
       h+='</pre>\n'

       h+='or for a different OS target (Android):\n'
       h+='<pre>\n'
       h+=' ck ls os:android* | sort\n'
       h+=' ck detect soft:{Soft UOA - see below} --target_os={OS UOA from above}\n'
       h+='</pre>\n'

       h+='You can see or use registered virtual CK environments as follows:\n'
       h+='<pre>\n'
       h+=' ck show env\n'
       h+=' ck show env --tags={some tags from below}\n'
       h+='\n'
       h+=' ck virtual env:{UID from above}\n'
       h+=' ck virtual env --tags={some tags from below}\n'
       h+='</pre>\n'

       h+='<p>\n'
       h+='See <pre>ck detect soft --help</pre> for more detection options.\n'
       h+='See <a href="http://cKnowledge.org/shared-packages.html">related CK packages</a>,\n'
       h+=' <a href="https://github.com/ctuning/ck/wiki">CK documentation</a>,\n'
       h+=' <a href="https://github.com/ctuning/ck/wiki#contributing">"how to contribute" guide</a>,\n'
       h+=' <a href="https://portalparts.acm.org/3230000/3229762/fm/frontmatter.pdf">ACM ReQuEST-ASPLOS\'18 report</a>\n'
       h+=' and the latest <a href="http://cKnowledge.org/rpi-crowd-tuning">CK paper</a> for further details.\n'

       h+='<p>\n'
       h+='<table cellpadding="4" border="1" style="border-collapse: collapse; border: 1px solid black">\n'

       h+=' <tr>\n'
       h+='  <td nowrap><b>#</b></td>\n'
       h+='  <td nowrap><b>Soft UOA</b></td>\n'
       h+='  <td nowrap><b>Template?</b></td>\n'
       h+='  <td nowrap><b>Repo UOA</b></td>\n'
       h+='  <td><b>Tags</b></td>\n'
       h+='  <td><b>Host OS</b></td>\n'
       h+='  <td><b>Target OS</b></td>\n'
       h+='  <td><b>Notes</b></td>\n'
       h+=' </tr>\n'

    repo_url={}
    repo_private={}

    size=0
    isize=1

    private=''
    num=0
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
           repo_private[lr_uid]=rx.get('dict',{}).get('private','')
           repo_url[lr_uid]=url

        private=repo_private.get(lr_uid,'')

        if lr not in cfg.get('skip_repos',[]) and private!='yes' and url!='':
           num+=1

           lm=l['meta']
           ld=lm.get('desc','')

           soft_name=lm.get('soft_name','')

           cus=lm.get('customize',{})

           ad=lm.get('auto_detect','')
           if ad!='yes': ad='no'

           ep=cus.get('env_prefix','')

           xhos=cus.get('only_for_host_os_tags',[])
           xtos=cus.get('only_for_target_os_tags',[])

           tmpl=lm.get('template','')
           template=lm.get('template_type','')
           if tmpl=='yes' and template=='':
              template='yes'

           tags=lm.get('tags',[])
           ytags=','.join(tags)

           yhos=''
           ytos=''

           for q in xhos:
               if yhos!='': yhos+=','
               yhos+=q

           for q in xtos:
               if ytos!='': ytos+=','
               ytos+=q

           if yhos=='':
              yhos='any'
           else:
              yhos=yhos.replace('linux','linux,macos')

           if ytos=='':
              ytos='any'
           else:
              ytos=ytos.replace('linux','linux,macos')

           if lr=='default':
              to_get=''
           elif url.find('github.com/ctuning/')>0:
              to_get='ck pull repo:'+lr
           else:
              to_get='ck pull repo --url='+url

           x=lr
           y=''
           yh=''
           if url!='':
              url2=url

              if url2.endswith('.git'):
                 url2=url2[:-4]

              yh=url2+'/tree/master/soft/'+ln
              x='['+url2+' '+lr+']'
              y='['+yh+' link]'

           ###############################################################
           if html:
              h+=' <tr>\n'

              x1=''
              x2=''
              z1=''
              if url!='':
                 x1='<a href="'+url+'">'
                 x2='</a>'
                 z1='<a href="'+yh+'">'
                 z11='<a href="'+yh+'/.cm/meta.json">'

              h+='  <td nowrap valign="top"><a name="'+ln+'">'+str(num)+'</b></td>\n'

              h+='  <td nowrap valign="top">'+z1+ln+x2+'</b> <i>('+z11+'CK meta'+x2+')</i></td>\n'

              h+='  <td nowrap valign="top">'+template+'</td>\n'

              h+='  <td nowrap valign="top">'+x1+lr+x2+'</td>\n'

              h+='  <td valign="top"><small>'+ytags+'</small>\n'
              h+='  <td valign="top"><small>'+yhos+'</small>\n'
              h+='  <td valign="top"><small>'+ytos+'</small>\n'

              h1='Auto-detect? '+ad+'<br>\n'
              h1+='Environment variable: '+ep+'<br>\n'

              if ld!='':
                 h1+='<p>\n'+ld

              h+='  <td valign="top">'+h1+'\n'

              h+='</td>\n'

              h+=' </tr>\n'

           ###############################################################
           elif o=='mediawiki':
              s=''

              s+='\n'
              s+='=== '+ln+' ('+soft_name+') ===\n'
              s+='\n'
              s+='Auto-detect?: '+ad+'\n'
              s+='<br>Environment variable: <b>'+ep+'</b>\n'
              s+='\n'
              s+='Tags: <i>'+ytags+'</i>\n'
              s+='<br>Host OS tags: <i>'+yhos+'</i>\n'
              s+='<br>Target OS tags: <i>'+ytos+'</i>\n'
              if y!='':
                 s+='\n'
                 s+='Software entry with meta: <i>'+y+'</i>\n'
              s+='\n'
              s+='Which CK repo: '+x+'\n'
              if to_get!='':
                 s+='<br>How to get: <i>'+to_get+'</i>\n'
              if to_get!='':
                 s+='\n'
                 s+='How to detect: <b>ck detect soft:'+ln+' (--target_os={CK OS UOA})</b>\n'

              s+='\n'

              if of=='':
                 ck.out(s)
              else:
                 with open(of, "a") as ff:
                      ff.write(s)
                 
                 size+=len(s)
                 if size>=80000:
                    isize+=1
                    of=xof[0]+str(isize)+xof[1]
                    size=0 

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

    ck.out('')
    ck.out('  Total soft detection plugins: '+str(num))
    ck.out('')

    if html:
       h+='</table>\n'
       h+=h2

       if of!='':
          r=ck.save_text_file({'text_file':of, 'string':h})
          if r['return']>0: return r

    return {'return':0, 'html':h}

##############################################################################
# get version of a given software (internal)

def find_config_file(i):
    """
    Input:  {
              full_path  - where to start search
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              found    - 'yes' if found
              dict     - loaded dict with the configuration ...
              filename - filename
              path     - path
            }

    """

    import os

    pf=i['full_path']
    filter_data_uid = i.get('data_uid', '')

    pf1=os.path.dirname(pf)

    found='no'
    d={}

    fn=''
    pf2=''
    while pf1!=pf and pf1!='':
       fn=cfg['ck_install_file']
       pf2=os.path.join(pf1,fn)
       if os.path.isfile(pf2):
          rx=ck.load_json_file({'json_file':pf2})
          if rx['return']==0:
             found='yes'
             d=rx['dict']
             break
       else:
          fn=cfg['ck_install_file_saved']
          pf2=os.path.join(pf1,fn)
          if os.path.isfile(pf2):
             rx=ck.load_json_file({'json_file':pf2})
             if rx['return']==0:
                found='yes'
                d=rx['dict']
                break

       pf=pf1
       pf1=os.path.dirname(pf)

    config_data_uid = d.get('data_uoa', '')
    if filter_data_uid and (config_data_uid != filter_data_uid):
        found = 'no'
        d = {}

    return {'return':0, 'found':found, 'dict':d, 'filename':fn, 'path':pf2}

##############################################################################
# compare two versions (in list)

def compare_versions(i):
    """
    Input:  {
              version1 - version 1 to compare against version2 (list such as [1,62])
              version2 - (list such as [1,63])
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              result       "<" - version 1 < version 2
                           "=" - version 1 == version 2
                           ">" - version 1 > version 2
            }

    """

    def compare_versions_core(v1_orig, v2_orig):

        len_diff = len(v2_orig)-len(v1_orig)    # determine the (signed) length of zero-padding

        # now pad the shorter to match the longer:
        (v1, v2) = (v1_orig + [0]*len_diff, v2_orig) if len_diff>0 else (v1_orig, v2_orig + [0]*-len_diff)

        for j in range(0,len(v1)):
            (t1, t2) = (type(v1[j]), type(v2[j]))
            if t1 == t2:        # perform natural comparison within the same type
                if v1[j]<v2[j]:
                    return '<'
                elif v1[j]>v2[j]:
                    return '>'
            elif t1 == int:     # but any integer is higher than any letter combination
                return '>'
            elif t2 == int:
                return '<'

        return '='

    result = compare_versions_core(i['version1'], i['version2'])

    if i.get('out','')=='con':
       ck.out(result)

    return {'return':0, 'result':result}

##############################################################################
# compare two versions (in list)

def prepare_target_name(i):
    """
    Input:  {
              host_os_dict   - host OS dict
              target_os_dict - target OS dict
              cus            - custom meta
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              tool         - tool name
            }

    """

    cus=i['cus']

    hosd=i['host_os_dict']
    tosd=i['target_os_dict']

    hplat=hosd['ck_name']
    tplat=tosd['ck_name']

    tool=''

    sdirs=hosd.get('dir_sep','')

    plat=tplat
    osd=tosd
    if cus.get('soft_file_from_host_os','')=='yes':
       plat=hplat
       osd=hosd

    tool=cus.get('soft_file_universal','')
    if tool=='':
       tool=cus.get('soft_file',{}).get(plat,'')

    file_extensions=hosd.get('file_extensions',{})

    # Check file extensions from OS (for example, to specialize .dylib vs .so for MacOS)
    for k in file_extensions:
        v=file_extensions[k]

        tool=tool.replace('$#file_ext_'+k+'#$',v)

    tool=tool.replace('$#sep#$', sdirs)

    return {'return':0, 'tool':tool}

##############################################################################
# add software detection plugin with template

def add(i):
    """
    Input:  {
              (template) - if !='', use this program as template!
              (tags)     - if !='', use these tags
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')

    # Redirect to a universal template ...

    muoa=i['module_uoa']

    i['original_module_uoa']=muoa
    i['module_uoa']=cfg['module_deps']['misc']
    i['action']='prepare_entry_template'
    if 'cid' in i: del(i['cid'])

    r=ck.access(i)
    if r['return']>0: return r

    # Update newly created entry with special keys
    duid=r['data_uid']
    duoa=r['data_uoa']
    ruid=r['repo_uid']

    dd=r['dict']

    if 'template' in dd: del(dd['template'])
    if 'template_type' in dd: del(dd['template_type'])

    xtags=i.get('tags','')
    if xtags=='':
       ck.out('')
       r=ck.inp({'text':'Enter tags for your new soft detection plugin separated by comma (for example lib,tflite): '})
       xtags=r['string'].strip()

    tags=[]
    if xtags!='':
       for q in xtags.split(','):
           q=q.strip()
           if q not in tags:
              tags.append(q)
    else:
       for k in dd.get('tags',[]):
           if k!='template': 
              tags.append(k)
    dd['tags']=tags

    ii={'action':'update',
        'module_uoa':muoa,
        'data_uoa':duid,
        'repo_uoa':ruid,
        'dict':dd,
        'substitute':'yes',
        'sort_keys':'yes',
        'ignore_update':'yes'
       }

    if o=='con':
       ck.out('')
       ck.out('Further details about how to update meta.json and customize.py of your new software detection plugin:')
       ck.out('')
       ck.out(' * https://github.com/ctuning/ck/wiki/Adding-new-workflows')

    return ck.access(ii)

##############################################################################
# search for soft version in some files

def search_version(i):
    """
    Input:  {
              path - path to file (where to start search)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              (version) - version string if detected
            }

    """

    import os

    o=i.get('out','')

    ver=''

    p0=i['path']

    f=os.path.basename(p0)
    p=os.path.dirname(p0)

    # Searching for spack info
    while True:
       p1=os.path.join(p, '.spack/spec.yaml')
       if os.path.isfile(p1):
          # Read file and search for version
          r=ck.load_text_file({'text_file':p1})
          if r['return']==0:
             s=r['string']

             # Find first version
             j=s.find('version: ')
             if j>=0:
                j1=s.find('\n',j)
                if j1>=0:
                   ver=s[j+9:j1].strip()

          break

       pp=os.path.dirname(p)
       if pp==p:
          break

       p=pp

    # If not found, search for .settings
    if ver=='' and f!='' and f!='/' and f!='\\':
       f1=os.path.splitext(f)[0]+'.settings'
       p=os.path.dirname(p0)
       p1=os.path.join(p,f1)

       if os.path.isfile(p1):
          # Read file and search for version
          r=ck.load_text_file({'text_file':p1})
          if r['return']==0:
             s=r['string']

             # Find first version
             j=s.lower().find(' version:')
             if j>=0:
                j1=s.find('\n',j)
                if j1>=0:
                   ver=s[j+9:j1].strip()

    return {'return':0, 'version':ver}
