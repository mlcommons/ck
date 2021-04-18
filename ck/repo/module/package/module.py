#
# Collective Knowledge (package)
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
fix_env_for_rebuild={"PACKAGE_GIT": "NO", 
                     "PACKAGE_WGET": "NO",
                     "PACKAGE_PATCH": "NO",
                     "PACKAGE_PATCH": "NO",
                     "PACKAGE_UNGZIP": "NO",
                     "PACKAGE_UNTAR": "NO",
                     "PACKAGE_UNBZIP": "NO",
                     "PACKAGE_SKIP_CLEAN_INSTALL": "YES",
                     "PACKAGE_SKIP_CLEAN_OBJ": "YES",
                     "PACKAGE_SKIP_CLEAN_SRC_DIR": "YES"}

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
# install package

def install(i):
    """
    Input:  {
              (target)            - if specified, use info from 'machine' module
                 or
              (host_os)           - host OS (detect, if omitted)
              (target_os)         - target OS (detect, if omitted)
              (target_device_id)  - target device ID (detect, if omitted)

              (data_uoa) or (uoa) - package UOA entry
                       or
              (tags)              - tags to search package if data_uoa=='' before searching in current path
              (or_tags)           - add entries which has groups of tags separated by ;
              (no_tags)           - exclude entris with these tags separated by comma

              (env_data_uoa)      - use this data UOA to record (new) env
              (env_repo_uoa)      - use this repo to record new env

              (install_path)      - full path with soft is installed
              (path)              - path with soft is installed (path from the package will be appended)

              (skip_process)      - if 'yes', skip archive processing
              (skip_setup)        - if 'yes', skip environment setup

              (deps)              - pre-set some deps, for example for compiler

              (reuse_deps)           - if 'yes' reuse all deps if found in cache by tags
              (deps_cache)           - list with resolved deps

              (deps.{KEY})        - set deps[KEY]["uoa']=value (user-friendly interface via CMD to set any given dependency)
              (preset_deps)       - dict with {"KEY":"UOA"} to preset dependencies

              (dep_add_tags.{KEY})   - extra tags added to specific subdictionary of deps{} for this particular resolution session

              (param)             - string converted into CK_PARAM and passed to processing script
              (params)            - dict, keys are converted into <KEY>=<VALUE> and passed to processing script

              (env_prefix)        - alternative env_prefix (overrides the one in soft entry)

              (env)               - add environment vars
              (env.{KEY})         - set env[KEY]=value (user-friendly interface via CMD)

              (Dkey)              - update params[key], i.e. ck install package:... -DENV1=val1 -DENV2=val2 (similar to CMAKE)

              (extra_version)     - add extra version, when registering software 
                                    (for example, -trunk-20160421)

              (extra_tags)        - add extra tags to separated customized packages (string separated by comma)

              (extra_path)        - add extra path to the automatically prepared one
                                    (for example, -trunk-20160421)

              (record_script)     - record tmp installation script with pre-set environment
                                    (to be able to call it to rebuild package without CK)

              (force_version)     - force version (useful for automatic installation of packages with multiple supported versions)

              (install_to_env)    - install this package and all dependencies to env instead of CK-TOOLS (to keep it clean)!

              (safe)              - safe mode when searching packages first instead of detecting already installed soft
                                    (to have more deterministic build)

              (add_hint)          - if 'yes', add hint that can skip package installation and detect soft instead

              (rebuild)           - if 'yes', attempt to set env to avoid downloading package again, just rebuild (if supported)
              (reinstall)         - if 'yes', also download package and then rebuild it ...

              (version_from)      - check version starting from ... (list of numbers)
              (version_to)        - check version up to ... (list of numbers)

              (ask)               - if 'yes', ask more questions, otherwise select default actions
              (ask_version)       - ask for the version of the package the user wants to install

              (debug)             - if 'yes', open shell before installing but with all resolved deps

              (quiet)             - if 'yes', install default package (answer 0 to selection questions)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              env_data_uoa - if installed fine
              env_data_uid - if installed fine
            }

    """
    import os
    import time
    import copy

    o=i.get('out','')

    oo=''
    if o=='con':
       oo=o

    ask=i.get('ask','')

    quiet=i.get('quiet','').strip().lower()

    xtags=i.get('tags','')
    xor_tags=i.get('or_tags','')
    xno_tags=i.get('no_tags','')

    reuse_deps=i.get('reuse_deps','')
    deps_cache=i.get('deps_cache',[])

    debug=i.get('debug','')

    # Check if package_channel is specifies and add tag
    pchannel=ck.cfg.get('package_channel','')
    if pchannel!='':
       if xtags!='': xtags+=','
       xtags+='channel-'+pchannel

    start_time = time.time()

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
                 'device_cfg':device_cfg,
                 'target_device_id':tdid,
                 'skip_info_collection':'yes'})
    if r['return']>0: return r

    hos=r['host_os_uid']
    hosx=r['host_os_uoa']
    hosd=r['host_os_dict']

    tos=r['os_uid']
    tosx=r['os_uoa']
    tosd=r['os_dict']

    host_add_path_string=r.get('host_add_path_string','')

    hosn=hosd.get('ck_name2','')
    osn=tosd.get('ck_name2','')

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

    tbits=tosd.get('bits','')

    ck_os_name=hosd['ck_name']
    tname2=tosd['ck_name2']
    macos = tosd.get('macos') == 'yes'

    vfrom=i.get('version_from',[])
    vto=i.get('version_to',[])

    if type(vfrom)!=list:
       rx=ck.access({'action':'split_version',
                     'module_uoa':cfg['module_deps']['soft'],
                     'version':vfrom})
       if rx['return']>0: return rx
       vfrom=rx['version_split']

    if type(vto)!=list:
       rx=ck.access({'action':'split_version',
                     'module_uoa':cfg['module_deps']['soft'],
                     'version':vto})
       if rx['return']>0: return rx
       vto=rx['version_split']

    rem=hosd.get('rem','')
    eset=hosd.get('env_set','')
    svarb=hosd.get('env_var_start','')
    svare=hosd.get('env_var_stop','')
    scall=hosd.get('env_call','')
    sdirs=hosd.get('dir_sep','')
    sext=hosd.get('script_ext','')
    evs=hosd.get('env_var_separator','')
    eifs=hosd.get('env_quotes_if_space','')
    eifsc=hosd.get('env_quotes_if_space_in_call','')
    wb=tosd.get('windows_base','')

    iev=i.get('install_to_env','')
    if iev=='':
       iev=ck.cfg.get('install_to_env','')

    safe=i.get('safe','')

    rebuild=i.get('rebuild','')
    reinstall=i.get('reinstall','')

    force_version = i.get('force_version', '')

    # Check package description
    duoa=i.get('uoa','')
    if duoa=='': duoa=i.get('data_uoa','')
    requested_muoa=i.get('module_uoa','')

    duid=''
    package_repo_uoa=''
    d={}
    required_variations = []

    if duoa=='' and requested_muoa=='':
       # Try to detect CID in current path
       rx=ck.detect_cid_in_current_path({})
       if rx['return']==0:
          duoa=rx.get('data_uoa','')
          package_repo_uoa=rx.get('repo_uoa','')

    if xtags:	# if tags are available, try searching both in tags and variations

          r=ck.access({'action':            'search_in_variations',
                       'data_uoa':			duoa,
                       'module_uoa':        'misc',
                       'query_module_uoa':  work['self_module_uid'],
                       'tags':              xtags,
                       'add_info':          'yes',
          })
          if r['return']>0: return r
          l=r['lst']
          if len(l)>0:
             # Check that support host/target OS
             ll=[]

             for q in l:
                 # Check if restricts dependency to a given host or target OS
                 rx=ck.access({'action':'check_target',
                               'module_uoa':cfg['module_deps']['soft'],
                               'dict':q.get('meta',{}),
                               'host_os_uoa':hosx,
                               'host_os_dict':hosd,
                               'target_os_uoa':tosx,
                               'target_os_dict':tosd})
                 if rx['return']==0:
                    specific_version = q.get('meta',{}).get('customize',{}).get('version','')
                    supported_versions = q.get('meta',{}).get('customize',{}).get('supported_versions')
                    if not specific_version and supported_versions and force_version=='':
                        for s_version in supported_versions:
                            q_clone = copy.deepcopy( q )
                            q_clone['meta']['customize']['version'] = s_version
                            ll.append( q_clone )
                    else:
                        ll.append(q)

             rx=ck.access({'action':'prune_search_list',
                              'module_uoa':cfg['module_deps']['env'],
                              'lst':ll,
                              'version_from':vfrom,
                              'version_to':vto,
                              'or_tags':xor_tags,
                              'no_tags':xno_tags})
             if rx['return']>0: return rx
             ll=rx['lst']

             # Select package 
             if len(ll)>0:
                # Sort by name and version
                l=sorted(ll, key=lambda k: (k.get('meta',{}).get('sort', 0),
                                            internal_get_val(k.get('meta',{}).get('customize',{}).get('version_split',[]), 0, 0),
                                            internal_get_val(k.get('meta',{}).get('customize',{}).get('version_split',[]), 1, 0),
                                            internal_get_val(k.get('meta',{}).get('customize',{}).get('version_split',[]), 2, 0),
                                            internal_get_val(k.get('meta',{}).get('customize',{}).get('version_split',[]), 3, 0),
                                            internal_get_val(k.get('meta',{}).get('customize',{}).get('version_split',[]), 4, 0),
                                            k.get('info',{}).get('data_name',''),
                                            k['data_uoa']),
                         reverse=True)

                selected_index=0
                if len(l)>1:
                    ver_options = []
                    ck.out('')
                    ck.out('More than one package or version found:')
                    ck.out('')

                    display_to_idx={}
                    for list_idx in range(len(l)):
                        package_entry = l[list_idx]
                        this_data_uid=package_entry['data_uid']

                        data_name_or_uoa = package_entry.get('info',{}).get('data_name', package_entry['data_uoa'])

                        dmeta=package_entry.get('meta',{})

                        declared_version = dmeta.get('customize',{}).get('version','')
                        version_if_defined = '  Version {} '.format(declared_version) if declared_version else ''

                        declared_comment = dmeta.get('comment','')
                        comment_in_braces = (declared_comment + ', ' if declared_comment else '') + this_data_uid

                        required_variations = package_entry.get('required_variations')
                        variations_to_display = ', Variations: {}'.format(','.join(required_variations)) if required_variations else ''

                        display_line = '{}{} ({}){}'.format(data_name_or_uoa, version_if_defined, comment_in_braces, variations_to_display)

                        display_to_idx[ display_line ] = list_idx
                        ver_options.append( display_line )

                    skip_display_line = 'Skip CK package installation and attempt to detect installed soft'
                    if i.get('add_hint','')=='yes':
                        ver_options.append( skip_display_line )

                    select_adict = ck.access({'action': 'select_string',
                                      'module_uoa': 'misc',
                                      'options': ver_options,
                                      'default': '0',
                                      'select_default': quiet,
                                      'no_skip_line': 'yes',
                                      'question': 'Please select the package to install',
                    })
                    if select_adict['return']>0: return select_adict

                    if select_adict['selected_value']==skip_display_line:
                        return {'return':16, 'error':'skipped package installation!'}

                    selected_index = select_adict['selected_index']

                    ck.out('')

                package_entry = l[selected_index]
                duid=package_entry.get('data_uid','')
                duoa=duid
                duoax=package_entry.get('data_uoa','')
                package_repo_uoa=package_entry.get('repo_uoa','')

                d=package_entry['meta']
                p=package_entry['path']
                required_variations = package_entry.get('required_variations',[])

                if o=='con':
                   ck.out('')
                   ck.out('  Package found: '+duoax+' ('+duid+')')
                   ck.out('')

          if duoa=='':
             x=''
             if xor_tags!='':
                x='and with or_tags="'+xor_tags+'" '
             if xno_tags!='':
                x='and with no_tags="'+xno_tags+'" '
             return {'return':16, 'error':'package with tags "'+xtags+'" '+x+'for your environment was not found!'}

    elif duoa:	# if tags were not available, try to load directly
       rx=ck.access({'action':'load',
                     'module_uoa':work['self_module_uid'],
                     'data_uoa':duoa})
       if rx['return']>0: return rx
       d=rx['dict']
       p=rx['path']

       duoa=rx['data_uoa']
       duid=rx['data_uid']
       package_repo_uoa=rx.get('repo_uoa','')


    # Check if restricts dependency to a given host or target OS
    rx=ck.access({'action':'check_target',
                  'module_uoa':cfg['module_deps']['soft'],
                  'dict':d,
                  'host_os_uoa':hosx,
                  'host_os_dict':hosd,
                  'target_os_uoa':tosx,
                  'target_os_dict':tosd})
    if rx['return']>0: return rx

    # Get main params
    tags=copy.deepcopy(d.get('tags',[]))

    extra_cli_tags = i.get('extra_tags','').strip()
    if extra_cli_tags!='':
        extra_cli_tags = extra_cli_tags.split(',')
        tags.extend(extra_cli_tags)
    else:
        extra_cli_tags = []
    vari_and_cli_tags = set(extra_cli_tags)		# to be topped up with variations, serialized and added to the install path

    udeps=d.get('deps',{})

    depsx=i.get('deps',{})
    if len(depsx)>0: 
        # RECENT UPDATE: check that is correct
        # Update only those keys that are in soft deps
        for k in udeps:
            if k in depsx:
                udeps[k]=depsx[k]
#        udeps.update(depsx)

    preset_deps   = i.get('preset_deps', {})
    dep_add_tags  = i.get('dep_add_tags', {})
    for q in i:
        if q.startswith('deps.'):
           preset_deps[q[5:]]=i[q].split(':')[-1]
        elif q.startswith('dep_add_tags.'):
           _ , dep_name    = q.split('.')
           dep_add_tags[dep_name] = i[q]

    for q in preset_deps:
        if q in udeps:
           udeps[q]['uoa']=preset_deps[q]


    cus=d.get('customize',{})
    env=d.get('env',{})

    # This environment will be passed to process scripts (if any)
    pr_env=cus.get('install_env',{})

    # Update this env from CK kernel (for example, to decide what to use, git or https). FIXME: check the desired precedence between cus and ck.cfg
    pr_env.update(ck.cfg.get('install_env',{}))


    # Some main dictionary keys have been previously living there,
    # but now that we have variations it is more practical to move them to 'customize' subdictionary
    # which can be more flexibly edited based on variations.
    # If you need this functionality, please add these keys into the following tuple:

    for moving_key in ('package_name', 'package_extra_name'):
        if (moving_key not in cus) and (moving_key in d):
            cus[moving_key]=d[moving_key]

    supported_variations  = d.get('variations', {})

    # If more than 1 variation and no required variations, show them to a user
    if len(supported_variations)>1 and len(required_variations)==0:
        ck.out('More than one version variation found in this package:')
        ck.out('')

        sorted_supported_variations=sorted(supported_variations, key=lambda k: supported_variations[k].get('on_by_default','')!='yes')

        j=0
        key_variation={}
        for variation in sorted_supported_variations:
             ck.out(str(j)+') '+variation)
             key_variation[j]=variation
             j+=1

        ck.out('')

        if quiet!='yes':
           x=input('Please select a variation or press Enter for the default one (0): ')

           x=x.strip()
           if x=='': x='0'

           ix=int(x)
           if ix<0 or ix>=j:
               return {'return':1, 'error':'variation number is not recognized'}
        else:
           ck.out('Selected 0 (default)')
           ix=0

        required_variations=[key_variation[ix]]

    required_vari_pairs   = [ (variation_name, False) for variation_name in required_variations ]
    default_vari_pairs    = [ (variation_name, True) for variation_name in supported_variations if supported_variations[variation_name].get('on_by_default', '')=='yes' ]
    vari_pairs            = required_vari_pairs + default_vari_pairs    # NB: the order is important!

    # Update this env from all the supported variations.
    # Detect if an incompatible mix of variation tags was required
    # that would lead to undefined behaviour, and bail out if so.
    #

    if vari_pairs:
        extra_env_from_variations = {}
        extra_cus_from_variations = {}
        extra_tags_from_variations = []

        supported_variations = d.get('variations', {})
        for (curr_variation, optional_variation) in vari_pairs:
            extra_env = supported_variations[curr_variation].get('extra_env',{})
            colliding_vars = set(extra_env_from_variations.keys()) & set(extra_env.keys()) # non-empty intersection means undefined behaviour

            if colliding_vars and optional_variation:   # a non-critical collision of env means we simply skip the optional_variation
                continue

            for coll_var in colliding_vars:     # have to check actual values to detect a mismatch
                if extra_env_from_variations[coll_var] != extra_env[coll_var]:
                    return { 'return':1,
                             'error':'contradiction on variable ({}) detected when adding "{}" variation tag'.format(coll_var,curr_variation)}

            extra_cus = supported_variations[curr_variation].get('extra_customize',{})
            colliding_cuss = set(extra_cus_from_variations.keys()) & set(extra_cus.keys()) # non-empty intersection means undefined behaviour

            if colliding_cuss and optional_variation:   # a non-critical collision of cus means we simply skip the optional_variation
                continue

            for coll_cus in colliding_cuss:     # have to check actual values to detect a mismatch
                if extra_cus_from_variations[coll_cus] != extra_env[coll_cus]:
                    return { 'return':1,
                             'error':'contradiction on customize ({}) detected when adding "{}" variation tag'.format(coll_cus,curr_variation)}

            extra_var_tags = supported_variations[curr_variation].get('extra_tags',[])
            if extra_var_tags and type(extra_var_tags)!=list:
              extra_var_tags=extra_var_tags.split(',')

            extra_env_from_variations.update( extra_env )   # merge of one particular variation
            extra_cus_from_variations.update( extra_cus )
            extra_tags_from_variations.extend( [curr_variation] + extra_var_tags )
            vari_and_cli_tags.add(curr_variation)

        pr_env.update( extra_env_from_variations )  # merge of all variations
        cus.update( extra_cus_from_variations )
        tags.extend( extra_tags_from_variations )


    # Customize keys that start with a '*' are requesting environment substitution.
    for raw_cus_key  in [ k for k in cus.keys() if k[0]=='*' ]:
        raw_cus_value = cus.pop(raw_cus_key)

        rx = ck.access({'action':'substitute_from_dict',
            'module_uoa': 'misc',
            'input_string': raw_cus_value,
            'mapping': pr_env,
            'tolerant': 'no',
        })
        if rx['return']>0: return rx
        cus_key = raw_cus_key[1:]
        cus[cus_key] = rx['output_string']
        ck.out("customize substitution: [{}] '{}' -> '{}'".format(cus_key, raw_cus_value, cus[cus_key]))

    # Environment keys that start with a '*' are requesting environment substitution.
    for raw_env_key  in [ k for k in pr_env.keys() if k[0]=='*' ]:
        raw_env_value = pr_env.pop(raw_env_key)

        rx = ck.access({'action':'substitute_from_dict',
            'module_uoa': 'misc',
            'input_string': raw_env_value,
            'mapping': pr_env,
            'tolerant': 'no',
        })
        if rx['return']>0: return rx
        env_key = raw_env_key[1:]
        pr_env[env_key] = rx['output_string']
        ck.out("install_env substitution: [{}] '{}' -> '{}'".format(env_key, raw_env_value, pr_env[env_key]))



    # Conservatively setting cus['version'] to PACKAGE_VERSION only if it was previously unset.
    # FIXME: review the desired precedence between 'version' and PACKAGE_VERSION , taking into account that
    #        1) 'version' could have been set either directly in cus or selected via supported_versions and
    #        2) PACKAGE_VERSION could have been set either in cus['install_env'] or via variations..['extra_env']
    if not cus.get('version') and pr_env.get('PACKAGE_VERSION'):
        cus['version'] = pr_env.get('PACKAGE_VERSION')

    ver=cus.get('version', '')

    env_display_name=cus.get('package_name', '')

    extra_version=i.get('extra_version', cus.get('extra_version','') )

    extra_dir=cus.get('extra_dir','')


    # Check if need to ask version - this is useful when
    # a package downloads specific file depending on the version
    # and it is also reflected in the installed path 
    # (see GCC universal installation)
    if d.get('ask_version','')=='yes' and force_version=='':
       ck.out('')
       r=ck.inp({'text':'Enter version of the package you would like to install: '})
       if r['return']>0: return r
       ver=r['string'].strip()

    # Force version
    if force_version!='':
       ver = cus['version'] = force_version

    pr_env['PACKAGE_VERSION']=ver

    ver += extra_version      # extra_version is normally added for disambiguation on CK side, so we add it later to avoid spoiling PACKAGE_VERSION

    tags.append('host-os-'+hosx)
    tags.append('target-os-'+tosx)
    tags.append(tbits+'bits')

    enruoa=i.get('env_repo_uoa','')
    enduoa=i.get('env_data_uoa','')
    enduid=i.get('env_data_uid','')


    # Update this env from customize meta (for example to pass URL to download package)
#    pr_env.update(cus.get('install_env',{}))
#    I moved it up to record changed env!

    for kpe in pr_env:
        x=pr_env[kpe]
        if x==str(x):
           x=str(x).replace('$#sep#$',sdirs) 

           j=x.find('$#path_to_cid=')
           if j>=0:
              j1=x.find('#$',j+13)
              if j1>0:
                 xcid=x[j+14:j1]

                 # Try to resolve CID
                 rx=ck.access({'action':'find', 'cid':xcid})
                 if rx['return']>0: 
                    return {'return':rx['return'], 'error':'Can\'t find entry when processing install_env var "'+kpe+'" ('+rx['error']+')'}

                 rxp=rx['path']

                 x=x[:j]+rxp+x[j1+2:]
 
           pr_env[kpe]=x

    ##########################################################################################
    #
    # All of the following:
    #       (1) "original" directory of the current entry
    #       (2) directory of the entry pointed by 'use_scripts_from_another_entry'
    #       (3) directory of the entry pointed by 'use_preprocess_scripts_from_another_entry'
    # may have a customization python script 'custom.py' (named in module/package/.cm/meta.json)
    #
    # The interface methods that will be optionally called (if the script provides them) are:
    #       * pre_path()
    #       * post_deps()
    #       * setup()
    #       * post_setup()
    #
    # In case both the "original" and the "other" directory contain the customization script,
    # each of the methods listed above will be attempted:
    #       * first in the "other" (typically representing the base entry)
    #       * and then in the "original" (typically representing the derived entry)
    #
    # The top two entries listed above may also contain install.{sh|bat} scripts.
    #
    # The mechanism seems to be an attempt to perform multiple inheritance of the entries,
    # both 'use_scripts_from_another_entry' and 'use_preprocess_scripts_from_another_entry'
    # representing the parents.
    #
    ##########################################################################################
    customization_script=None
    original_customization_script=None # original - always in the current directory of a package!


    # Initial assumption is that the "original" directory of the entry contains the customization script:
    #
    (customization_script_path, shell_script_path) = (p, p)


    # Loading original_customization_script from the original entry, if possible:
    #
    rx=ck.load_module_from_path({'path':customization_script_path, 'module_code_name':cfg['custom_script_name'], 'skip_init':'yes'})
    if rx['return']==0: 
       original_customization_script=rx['code']


    # The second entry may contain both custom.py and install.{sh|bat} :
    #
    another_entry_with_scripts=d.get('use_scripts_from_another_entry', None)
    if another_entry_with_scripts:
       r=ck.access({'action':'find',
                    'module_uoa':   another_entry_with_scripts.get('module_uoa', work['self_module_uid']),
                    'data_uoa':     another_entry_with_scripts.get('data_uoa','')
                })
       if r['return']>0: return r
       (customization_script_path, shell_script_path) = (r['path'], r['path']) # may change later via use_preprocess_scripts_from_another_entry


    # The third entry may only contain custom.py :
    #
    another_entry_with_preprocess_scripts=d.get('use_preprocess_scripts_from_another_entry', None)
    if another_entry_with_preprocess_scripts:
       r=ck.access({'action':'find',
                    'module_uoa':   another_entry_with_preprocess_scripts.get('module_uoa', work['self_module_uid']),
                    'data_uoa':     another_entry_with_preprocess_scripts.get('data_uoa','')
                })
       if r['return']>0: return r
       customization_script_path=r['path']


    # What follows may be a bit confusing:
    #
    # If original_customization_script existed, we will only attempt to load customization_script from another_entry_with_preprocess_scripts.
    #
    # However if there was no original_customization_script, we may attempt to load:
    #   (1) original_customization_script again [ if defined last ] - will silently fail again
    #   (2) customization_script from use_scripts_from_another_entry [ if defined last ]
    #   (3) customization_script from use_preprocess_scripts_from_another_entry [ if defined last ]
    # In any case the loading is allowed to silently fail without notice.
    #
    if another_entry_with_preprocess_scripts or not original_customization_script:
       rx=ck.load_module_from_path({'path':customization_script_path, 'module_code_name':cfg['custom_script_name'], 'skip_init':'yes'})
       if rx['return']==0: 
          customization_script=rx['code']

    else:       # if there was no other script to load, we move the previously loaded code into customization_script
       (original_customization_script, customization_script) = (None, original_customization_script)


    # Check if need host CPU params
    features={}
    if d.get('need_cpu_info','')=='yes':
       r=ck.access({'action':'detect',
                    'module_uoa':cfg['module_deps']['platform.cpu'],
                    'host_os':hos,
                    'target_os':hos})
       if r['return']>0: return r

       cpu_ft=r.get('features',{}).get('cpu',{})
       features.update(r.get('features',{}))

       pr_env['CK_HOST_CPU_NUMBER_OF_PROCESSORS']=cpu_ft.get('num_proc','1')

       # We may want to pass more info (including target CPU) ...

    # Set up extra vars
    pr_env['CK_TARGET_CPU_BITS']=tosd.get('bits','')
    pr_env['CK_HOST_OS_ID']=hosn
    pr_env['CK_TARGET_OS_ID']=osn
    pr_env['CK_MD5SUM_CMD']=hosd.get('md5sum', 'md5sum')

    # Check if need host GPGPU params
    # We need a question here ('out':oo), since there can be multiple available drivers and we need to let user select the right one
    if d.get('need_gpgpu_info','')=='yes':
       r=ck.access({'action':'detect',
                    'module_uoa':cfg['module_deps']['platform.gpgpu'],
                    'type':d.get('need_gpgpu_type',''),
                    'host_os':hos,
                    'target_os':hos,
                    'out':oo})
       if r['return']>0: return r

       features.update(r.get('features',{}))

    # Update env from input
    envx=i.get('env',{})

    for q in i:
        if q.startswith('env.'):
           envx[q[4:]]=i[q]

    if len(envx)>0:
       pr_env.update(envx)

    # Search by exact terms
    setup={'host_os_uoa':hos,
           'target_os_uoa':tos,
           'target_os_bits':tbits}
    if ver!='':
       setup['version']=ver

    # Resolve deps
    if cus.get('ignore_deps','')=='yes':
       udeps={}

    sdeps=''
    if len(udeps)>0:
       env_resolve_action_dict={
           'action':'resolve',
           'module_uoa':cfg['module_deps']['env'],
           'host_os':hos,
           'target_os':tos,
           'target_device_id':tdid,
           'repo_uoa':enruoa,
           'install_to_env':iev,
           'install_env':pr_env,
           'reuse_deps':reuse_deps,
           'deps_cache':deps_cache,
           'dep_add_tags': dep_add_tags,
           'safe':safe,
           'quiet':quiet,
           'deps':udeps}
       if o=='con': env_resolve_action_dict['out']='con'

       rx=ck.access(env_resolve_action_dict)
       if rx['return']>0: return rx
       sdeps=rx['bat']
       udeps=rx['deps'] # Update deps (add UOA)

    for q in udeps:
        v=udeps[q]
        if v.get('uoa','')!='':
           setup['deps_'+q]=v['uoa']

    # Check installation path
    pre_path=i.get('path','')
    pi=i.get('install_path','')
    vari_and_cli_path = '-'.join([''] + sorted(list(vari_and_cli_tags)) ) if vari_and_cli_tags else ''
    extra_path=i.get('extra_path','')
    fp=i.get('full_path','')

    x=cus.get('input_path_example','')
    if x!='': pie=' (example: '+x+')'
    else: pie=''

    # If rebuild option, try to set vars to avoid download 
    if rebuild=='yes': pr_env.update(fix_env_for_rebuild)

    # Customize installation before installation path is finalized ******************************************************
    param_dict_for_pre_path={"host_os_uoa":hosx,
        "host_os_uid":hos,
        "host_os_dict":hosd,
        "target_os_uoa":tosx,
        "target_os_uid":tos,
        "target_os_dict":tosd,
        "target_device_id":tdid,
        "cfg":d,
        "tags":tags,
        "env":env,
        "install_env":pr_env,
        "deps":udeps,
        "customize":cus,
        "self_cfg":cfg,
        "features":features,
        "version":ver,
        "ck_kernel":ck
       }

    if o=='con': param_dict_for_pre_path['interactive']='yes'
    if quiet=='yes': param_dict_for_pre_path['interactive']=''

    rx = internal_run_if_present(customization_script, 'pre_path', param_dict_for_pre_path, pr_env)
    if rx['return']>0: return rx

    rx = internal_run_if_present(original_customization_script, 'pre_path', param_dict_for_pre_path, pr_env)
    if rx['return']>0: return rx

    dep_tags = []

    # Iterate through all resolved dependencies and check which tags we need to create from them,
    #   preserving the desired sort order:
    #
    for dep_name, dep_dict in sorted(udeps.items(), key=lambda pair: pair[1].get('sort',0)) :
        if dep_dict.get('uoa',''):
            if dep_name in ('compiler', 'host-compiler') :
                dep_tag_prefix  = 'compiled-by-'
            elif dep_dict.get('add_to_tags', dep_dict.get('add_to_path','') )=='yes':
                dep_tag_prefix = 'needs-'
            else:
                dep_tag_prefix = ''

            # Empty prefix means we don't want this dependency to appear in tags:
            #
            if dep_tag_prefix:
                dep_tag     = dep_tag_prefix + dep_dict.get('build_dir_name','unknown_' + dep_name)
                dep_tags.append( dep_tag )

                dep_version = dep_dict.get('ver')
                if dep_version:
                    dep_tags.append( dep_tag + '-' + dep_version )

    # Join stripped tags and compiler tags into a CSV string:
    stripped_tags   = [t.strip() for t in tags if t.strip()]
    tags_csv        = ','.join( dep_tags + stripped_tags )

    xprocess    = i.get('skip_process','')!='yes' or rebuild=='yes' or reinstall=='yes'

    xsetup      = i.get('skip_setup','')!='yes' and d.get('skip_setup','')!='yes'

    shell_script_name=d.get('process_script','')
    if pi=='':
       # Check if environment already exists to check installation path
       if enduoa=='':
          if o=='con':
             ck.out('')
             ck.out('Searching if CK environment for this package already exists using:')
             ck.out('  * Tags: '+tags_csv)
             if len(udeps)>0:
                for q in udeps:
                    v=udeps[q]
                    vuoa=v.get('uoa','')
                    if vuoa!='':
                       ck.out('  * Dependency: '+q+'='+v.get('uoa',''))

          r=ck.access({'action':'search',
                       'module_uoa':cfg['module_deps']['env'],
                       'tags':tags_csv,
                       'search_dict':{'setup':setup}})
          if r['return']>0: return r
          lst=r['lst']

          # If more than one entry, try to prune by package UID if exists
          if len(lst)>1 and duid!='':
             new_lst=[]
             for je in lst:
                 skip=False
                 rje=ck.access({'action':'load',
                                'module_uoa':cfg['module_deps']['env'],
                                'data_uoa':je['data_uid'],
                                'repo_uoa':je['repo_uid']})
                 if rje['return']==0:
#                    print (rje['dict'].get('customize',{}).get('used_package_uid',''))
#                    print (duid)

                    if rje['dict'].get('customize',{}).get('used_package_uid','')!=duid:
                       skip=True

                 if not skip:
                    new_lst.append(je)

             lst=new_lst

          if len(lst)==1:
             fe=lst[0]

             enruoa=fe['repo_uid']
             enduoa=fe['data_uoa']
             enduid=fe['data_uid']

             if iev=='yes':
                pi=fe['path']

             if o=='con':
                x=enduoa
                if enduid!=enduoa: x+=' ('+enduid+')'

                ck.out('')
                ck.out('CK environment found for this package: '+x)
          elif len(lst)>1:
             ck.out('')
             ck.out('AMBIGUITY: more than one environment entry found for this installation')

             ck.out('')
             for je in lst:
                 ck.out(' * '+je['data_uid'])
             ck.out('')

             return {'return':1, 'error':'more than one environment entry found for this installation, please specify using --env_data_uoa={correct environment entry UID}'}
          else:
             if o=='con':
                ck.out('')
                ck.out('CK environment not found for this package ...')

       # Load env if exists
       if enduoa!='':
          r=ck.access({'action':'load',
                       'module_uoa':cfg['module_deps']['env'],
                       'repo_uoa':enruoa,
                       'data_uoa':enduoa})
          if r['return']>0: return r
          de=r['dict']

          x=de.get('customize',{}).get('path_install','')
          if x!='': pi=x

          x=de.get('customize',{}).get('full_path','')
          if x!='': fp=x

#          if extra_dir!='':
#             j=pi.rfind(extra_dir)
#             if j>=0:
#                pi=pi[:j]
#
#             if pi!='':
#                j=len(pi)
#                if pi[j-1]==sdirs:
#                   pi=pi[:-1]


          if fp!='':
             if o=='con':

                if ask=='yes' and xprocess:
                   ck.out('')
                   ck.out('It appears that package is already installed or at least file from the package is already found in path: '+fp)

                   if shell_script_name:
                      ck.out('')
                      rx=ck.inp({'text':'Would you like to overwrite and process it again (y/N)? '})
                      x=rx['string'].strip().lower()
                      if x!='y' and x!='yes':
                         xprocess=False

                if ask=='yes' and xsetup:
                   ck.out('')
                   rx=ck.inp({'text':'Would you like to setup environment for this package again (Y/n)? '})
                   x=rx['string'].strip().lower()
                   if x=='n' or x=='no':
                      xsetup=False

                if ask!='yes' and xprocess:
                   ck.out('')
                   ck.out('  OVERWRITING AND PROCESSING AGAIN!')

             else:
                return {'return':1, 'error':'package is already installed in path '+pi}

       if enduoa=='' and iev=='yes':
          # Create dummy env and then set path there
          # TBD - if installation fails, we still have this dummy - need to check what to do ...
          #  can remove: ck rm env:* --tags=tmp
          xx=tags_csv
          if xx!='': xx+=','
          xx+='tmp'
          rx=ck.access({'action':'add',
                        'module_uoa':cfg['module_deps']['env'],
                        'repo_uoa':enruoa,
                        'tags':xx,
                        'dict':{'setup':setup}})
          if rx['return']>0: return rx

          enduoa=rx['data_uoa']
          enduid=rx['data_uid']
          pi=rx['path']

       if cus.get('skip_path','')!='yes' and pi=='':
          if o=='con':
             ck.out('')

          pix=''
          sp=d.get('suggested_path','')

          if pre_path=='':
             rz=prepare_install_path({})
             if rz['return']>0: return rz
             x=rz['path']
          else:
             x=pre_path

          if x!='' and sp!='':
             # Prepare installation path
             # First via package + version
             nm=sp

#             if cus.get('no_ver_in_suggested_path','')!='yes' and cus.get('version','')!='':
#                nm+='-'+cus.get('version','')
             if cus.get('no_ver_in_suggested_path','')!='yes' and ver!='':
                nm+='-'+ver.strip('-')

             # Then if compiler
             bdn=udeps.get('compiler',{}).get('build_dir_name','')
             vr=udeps.get('compiler',{}).get('ver','')
             if bdn=='':
                bdn=udeps.get('support_compiler',{}).get('build_dir_name','')
                vr=udeps.get('support_compiler',{}).get('ver','')

             if cus.get('no_compiler_in_suggested_path','')!='yes' and bdn!='':
                nm+='-'+bdn
                if vr!='':
                   nm+='-'+vr

             # Then any deps with explicitly specified 'add_to_path'
             for u in sorted(udeps, key=lambda v: udeps[v].get('sort',0)):
                 uu=udeps[u]
                 if uu.get('add_to_path','')=='yes':
                    vr=uu.get('ver','')

                    softuoa=uu.get('dict',{}).get('soft_uoa','')
                    salias=uu.get('dict',{}).get('soft_alias','')
                    if salias=='': salias=softuoa

                    if salias!='':
                       nm+='-'+salias
                    if vr!='':
                       nm+='-'+vr

             # Then some extra path, if non-empty
             nm += cus.get('extra_suggested_path','')

             # Then another extra path, if non-empty
             nm += vari_and_cli_path + extra_path

             # Finally OS
             if cus.get('no_os_in_suggested_path','')!='yes':
                nm+='-'+tosx

             pix=os.path.join(x, nm)
             if cus.get('no_os_in_suggested_path','')!='yes':
                if not tosx.endswith(tbits): pix+='-'+tbits

             if o=='con' and (ask=='yes' or cus.get('force_ask_path','')=='yes'):
                ck.out('*** Suggested installation path: '+pix)
                r=ck.inp({'text':'  Press Enter to use suggested path or input new installation path '+pie+': '})
                pi=r['string'].strip()
                if pi=='': pi=pix
             else:
                pi=pix
                if d.get('no_install_path','')!='yes':
                   ck.out('*** Installation path used: '+pix)

             if o=='con':
                ck.out('')

          else:
             if o=='con':
                r=ck.inp({'text':'Enter installation path '+pie+': '})
                pi=r['string'].strip()

       if pi=='' and cus.get('skip_path','')!='yes':
          return {'return':1, 'error':'installation path is not specified'}


    suoa=d.get('soft_uoa','') or cus.get('soft_uoa', '')

    # Check dependencies
    deps={}
    soft_dict={}
    if suoa!='':
       rx=ck.access({'action':'load',
                     'module_uoa':cfg['module_deps']['soft'],
                     'data_uoa':suoa})
       if rx['return']>0: return rx
       soft_dict=rx['dict']
       deps=soft_dict.get('deps',{})

    # In case 'package_name' was missing from the package, use the default from soft entry
    if env_display_name=='':
       env_display_name=soft_dict.get('soft_name','')


    env_display_name+=cus.get('package_extra_name', '')

    # TODO: instead of this application-specific substitute, start using generic
    # "*package_extra_name" or "*package_name" substitute - then the following
    # paragraph could be removed:
    rx = ck.access({'action':'substitute_from_dict',
        'module_uoa': 'misc',
        'input_string': env_display_name,
        'mapping': pr_env,
    })
    if rx['return']>0: return rx
    env_display_name = rx['output_string']



    # Save package UOA to the cus
    cus['used_package_uoa']=duoa
    cus['used_package_uid']=duid

    # Update by package deps (more precise)
    for q in deps:
        v=deps[q]
        if q not in udeps:
           udeps[q]=v

    # Prepare environment based on deps
    if cus.get('ignore_deps','')=='yes':
       udeps={}

    sdeps=''
    if len(udeps)>0:
       env_resolve_action_dict={'action':'resolve',
           'module_uoa':cfg['module_deps']['env'],
           'host_os':hos,
           'target_os':tos,
           'target_device_id':tdid,
           'repo_uoa':enruoa,
           'install_to_env':iev,
           'reuse_deps':reuse_deps,
           'deps_cache':deps_cache,
           'dep_add_tags': dep_add_tags,
           'safe':safe,
           'deps':udeps}
       if rebuild=='yes': env_resolve_action_dict['rebuild']='yes'
       if o=='con': env_resolve_action_dict['out']='con'

       rx=ck.access(env_resolve_action_dict)
       if rx['return']>0: return rx
       sdeps=rx['bat']

    if o=='con' and pi!='':
       ck.out('')
       ck.out('Installing to '+pi)
       ck.out('')

    # Customize installation based on resolved dependencies *************************************************************
    param_dict_for_post_deps={"host_os_uoa":hosx,
        "host_os_uid":hos,
        "host_os_dict":hosd,
        "target_os_uoa":tosx,
        "target_os_uid":tos,
        "target_os_dict":tosd,
        "target_device_id":tdid,
        "cfg":d,
        "tags":tags,
        "env":env,
        "features":features,
        "customize":cus,
        "self_cfg":cfg,
        "version":ver,
        "ck_kernel":ck,
        "deps":udeps
       }

    if o=='con': param_dict_for_post_deps['interactive']='yes'
    if quiet=='yes': param_dict_for_post_deps['interactive']=''

    rx = internal_run_if_present(customization_script, 'post_deps', param_dict_for_post_deps, pr_env)
    if rx['return']>0: return rx

    rx = internal_run_if_present(original_customization_script, 'post_deps', param_dict_for_post_deps, pr_env)
    if rx['return']>0: return rx

    hd_r=ck.access({'action':       'get_home_dir',
                    'module_uoa':    'misc',
    })
    if hd_r['return']>0: return r
    home_dir=hd_r['home_dir']

    soft_cfg={}

    # Check if continue processing
    if (shell_script_name or (customization_script and 'setup' in dir(customization_script))) and xprocess:
       # start bat
       shell_wrapper_contents=hosd.get('batch_prefix','')+'\n'

       if host_add_path_string!='':
          shell_wrapper_contents+=host_add_path_string+'\n\n'

       # Check if extra params to pass as environment
       param=i.get('param',None)
       params=d.get('params',{})
       params.update(i.get('params',{}))

       # Parse -D ...
       for k in i:
           if k.startswith('D'):
              params[k[1:]]=i[k]

       if param!=None:
          shell_wrapper_contents+='\n'
          xs=''
          if param.find(' ')>=0 and eifs!='': xs=eifs
          shell_wrapper_contents+=eset+' CK_PARAM='+xs+param+xs+'\n'

       if len(params)>0:
          for q in params:
              v=params[q]
              if v!=None:
                 xs=''
                 if v.find(' ')>=0 and eifs!='': xs=eifs
                 shell_wrapper_contents+=eset+' '+q+'='+xs+v+xs+'\n'

       shell_wrapper_contents+='\n'

       # Check installation path
       if pi=='' and cus.get('skip_path','')!='yes':
          if o=='con':
             ck.out('')

             pix=''
             sp=d.get('suggested_path','')

             rz=prepare_install_path({})
             if rz['return']>0: return rz
             x=rz['path']

             if x!='' and sp!='':
                pix=os.path.join(x, sp+'-'+cus.get('version','')+'-'+tosx)
                if not tosx.endswith(tbits): pix+='-'+tbits
                ck.out('Suggested path: '+pix)
                r=ck.inp({'text':'  Press Enter to use suggested path or input new installation path '+pie+': '})
                pi=r['string'].strip()
                if pi=='': pi=pix
             else:
                r=ck.inp({'text':'Enter installation path '+pie+': '})
                pi=r['string'].strip()

          if pi=='':
             return {'return':1, 'error':'installation path is not specified'}


       def efp_substitute(efp):

          efp=efp.replace('$#home#$', home_dir)
          efp=efp.replace('$#sep#$', sdirs)
          efp=efp.replace('$#abi#$', tosd.get('abi',''))
          efp=efp.replace('$#processor#$', tosd.get('processor',''))
          for k in pr_env:
              v=str(pr_env[k])
              efp=efp.replace('$<<' +k+ '>>$',v)

            # NOTE: adapted from module/soft/module.py/prepare_target_name()
            #       After successful testing this function should be moved out
            #       into a common utility space and imported from there.
            #       Also, check whether the original function was supposed to be
            #           sourcing the data from hosd or tosd.
          file_extensions=tosd.get('file_extensions',{})
          for k in file_extensions:
              v=file_extensions[k]
              efp=efp.replace('$#file_ext_'+k+'#$',v)

          host_file_extensions=hosd.get('host_file_extensions',{})
          for k in host_file_extensions:
              v=host_file_extensions[k]
              efp=efp.replace('$#host_file_ext_'+k+'#$',v)

          return efp


       # Check if there is already library or tool exists
       efp=d.get('end_full_path_universal')
       if efp==None or len(efp)==0:
          efpd = d.get('end_full_path', {})
          efp = efpd['macos'] if (macos and 'macos' in efpd) else efpd.get(tname2,[])

       efp_or_list    = efp if type(efp)==list else [ efp ]                             # enforce list
       fp_candidates  = [ os.path.join( pi, efp_substitute(x) ) for x in efp_or_list ]  # apply substitution and create full paths
       fp_matches     = [ x for x in fp_candidates if os.path.exists(x) ]               # find all matches

       cont=True

       if len(fp_matches)>0:
          if o=='con':
                ck.out('')
                ck.out('It appears that package is already installed or at least file from the package already found in path: {}'.format(fp_matches))

                if (rebuild!='yes' and reinstall!='yes') or ask=='yes':
                   ck.out('')
                   rx=ck.inp({'text':'Would you like to overwrite/process it again (y/N)? '})
                   x=rx['string'].strip().lower()
                   if x!='y' and x!='yes':
                      cont=False
                else:
                   ck.out('')
                   ck.out('  OVERWRITING AND PROCESSING AGAIN!')


       # Check if need to use scripts from another entry
       if cont:
          # Customize main installation
          param_dict_for_setup={"host_os_uoa":hosx,
              "host_os_uid":hos,
              "host_os_dict":hosd,
              "target_os_uoa":tosx,
              "target_os_uid":tos,
              "target_os_dict":tosd,
              "target_device_id":tdid,
              "cfg":d,
              "tags":tags,
              "env":env,
              "new_env":pr_env,
              "deps":udeps,
              "features":features,
              "customize":cus,
              "self_cfg":cfg,
              "version":ver,
              "path":shell_script_path,
              "path_original_package":p,
              "script_path":customization_script_path,
              "out":oo,
              "install_path":pi
             }

          if o=='con': param_dict_for_setup['interactive']='yes'
          if quiet=='yes': param_dict_for_setup['interactive']=''

          param_dict_for_post_setup=copy.deepcopy(param_dict_for_setup)

          param_dict_for_post_setup['ck_kernel']=ck
          param_dict_for_setup['ck_kernel']=ck

          rx = internal_run_if_present(customization_script, 'setup', param_dict_for_setup, pr_env)
          if rx['return']>0: return rx
          else:
                soft_cfg=rx.get('soft_cfg',{})

          rx = internal_run_if_present(original_customization_script, 'setup', param_dict_for_setup, pr_env)
          if rx['return']>0: return rx

          # Prepare process script
          if shell_script_name:
             shell_script_name+=sext
             shell_script_full_path=os.path.join(shell_script_path,shell_script_name)

             if not os.path.isfile(shell_script_full_path):
                return {'return':1, 'error':'processing script '+shell_script_name+' is not found'}

             # Add deps if needed before running
             if sdeps!='':
                shell_wrapper_contents+=sdeps

             # Add compiler dep again, if there
             shell_wrapper_contents+='\n'
             for k in sorted(udeps, key=lambda v: udeps[v].get('sort',0)):
                 if 'compiler' in k or udeps[k].get('repeat_at_the_end','')=='yes':
                    x=udeps[k].get('bat','').strip()
                    if x!='' and not shell_wrapper_contents.endswith(x):
                       shell_wrapper_contents+=x+' 1\n'
             shell_wrapper_contents+='\n'

             # Add misc environment (prepared above)
             for q in pr_env:
                 qq=str(pr_env[q])

                 qq=qq.replace('$<<',svarb).replace('>>$',svare)

                 if qq.find(' ')>0:
                    qq=eifs+qq+eifs
                 shell_wrapper_contents+=eset+' '+q+'='+qq+'\n'

             # If install path has space, add quotes for some OS ...
             xs=''
             if pi.find(' ')>=0 and eifs!='': xs=eifs
             shell_wrapper_contents+=eset+' INSTALL_DIR='+xs+pi+xs+'\n'

             # If Windows, add MingW path
             if wb=='yes':
                rm=ck.access({'action':'convert_to_cygwin_path',
                              'module_uoa':cfg['module_deps']['os'],
                              'path':pi})
                if rm['return']>0: return rm
                ming_pi=rm['path']
                shell_wrapper_contents+=eset+' INSTALL_DIR_MINGW='+xs+ming_pi+xs+'\n'

             xs=''
             if p.find(' ')>=0 and eifs!='': xs=eifs
             shell_wrapper_contents+=eset+' PACKAGE_DIR='+xs+shell_script_path+xs+'\n'

             # If Windows, add MingW path
             if wb=='yes':
                rm=ck.access({'action':'convert_to_cygwin_path',
                              'module_uoa':cfg['module_deps']['os'],
                              'path':shell_script_path})
                if rm['return']>0: return rm
                ming_ppp=rm['path']
                shell_wrapper_contents+=eset+' PACKAGE_DIR_MINGW='+xs+ming_ppp+xs+'\n'

             xs=''
             if p.find(' ')>=0 and eifs!='': xs=eifs
             shell_wrapper_contents+=eset+' ORIGINAL_PACKAGE_DIR='+xs+p+xs+'\n'

             # If Windows, add MingW path
             if wb=='yes':
                rm=ck.access({'action':'convert_to_cygwin_path',
                              'module_uoa':cfg['module_deps']['os'],
                              'path':p})
                if rm['return']>0: return rm
                ming_p=rm['path']
                shell_wrapper_contents+=eset+' ORIGINAL_PACKAGE_DIR_MINGW='+xs+ming_p+xs+'\n'

             shell_wrapper_contents+='\n'

             if debug=='yes':
                import platform

                xs='Warning: you are in a new shell with a pre-set CK environment. Enter "exit" to return to the original one!'
                if platform.system().lower().startswith('win'):
                   shell_wrapper_contents+='echo '+xs+'\n'
                   shell_wrapper_contents+='cmd\n'
                else:
                   shell_wrapper_contents+='echo "'+xs+'"\n'
                   shell_wrapper_contents+='bash\n'

             xs=''
             if p.find(' ')>=0 and eifsc!='': xs=eifsc
             shell_wrapper_contents+=scall+' '+xs+shell_script_full_path+xs+'\n\n'

             if wb=='yes' and d.get('check_exit_status','')!='yes':
                shell_wrapper_contents+='exit /b 0\n'

             rs=i.get('record_script','')

             # Generate tmp file (or use record script)
             if rs:
                shell_wrapper_name=rs
                if shell_wrapper_name==os.path.basename(shell_wrapper_name):
                   shell_wrapper_name=os.path.join(os.getcwd(),shell_wrapper_name)
             else:
                rx=ck.gen_tmp_file({'prefix':'tmp-ck-', 'suffix':sext})
                if rx['return']>0: return rx
                shell_wrapper_name=rx['file_name']

             # Write to tmp file
             rx=ck.save_text_file({'text_file':shell_wrapper_name, 'string':shell_wrapper_contents})
             if rx['return']>0: return rx

             # Go to installation path
             if not os.path.isdir(pi):
                os.makedirs(pi)
             os.chdir(pi)

             # Check if need to set executable flags
             se=hosd.get('set_executable','')
             if se!='':
                x=se+' '+shell_wrapper_name
                rx=os.system(x)

             # Run script
             rx=os.system(shell_wrapper_name)

             # Remove script (if tmp)
             if rs=='' and os.path.isfile(shell_wrapper_name):
                os.remove(shell_wrapper_name)

             if rx>0: 
                print_warning({'package_data_uoa':duoa, 'package_repo_uoa':package_repo_uoa, 'package_meta':d})
                return {'return':1, 'error':'package installation failed'}

          # Check if has post-setup Python script
          param_dict_for_post_setup['new_env']=pr_env

          rx = internal_run_if_present(customization_script, 'post_setup', param_dict_for_post_setup, {})
          if rx['return']>0: return rx

          rx = internal_run_if_present(original_customization_script, 'post_setup', param_dict_for_post_setup, {})
          if rx['return']>0: return rx


    fp_matches  = [ x for x in fp_candidates if os.path.exists(x) ]               # find all matches again
    fp          = fp_matches[0] if len(fp_matches) else fp_candidates[0] if len(fp_candidates) else pi

    if 'env_prefix' in i:
      cus['env_prefix'] = i['env_prefix']

    # Preparing soft registration
    soft_registration_action_dict={'action':'setup',
        'module_uoa':cfg['module_deps']['soft'],
        'data_uoa':suoa,
        'soft_name':env_display_name,
        'host_os':hos,
        'target_os':tos,
        'target_device_id':tdid,
        'tags':tags_csv,
        'customize':cus,
        'features':features,
        'env_new':'yes',
        'env_repo_uoa':enruoa,
        'env_data_uoa':enduoa,
        'env':env,
        'extra_version':extra_version
       }

    nw='no'
    if enduoa=='': nw='yes'

    if cus.get('collect_device_info','')!='yes':
        soft_registration_action_dict['skip_device_info_collection']='yes'

    if d.get('remove_deps','')=='yes':
       soft_registration_action_dict['deps_copy']=udeps
    else:
       soft_registration_action_dict['deps']=udeps

    if d.get('no_install_path','')!='yes':
       if fp!='':
          soft_registration_action_dict['full_path']=fp
          soft_registration_action_dict['full_path_install']=pi
       elif pi!='':              # mainly for compatibility with previous CK soft manager
          soft_registration_action_dict['install_path']=pi

    if duid!='': soft_registration_action_dict['package_uoa']=duid

    if len(soft_cfg)>0:
       soft_registration_action_dict.update(soft_cfg)

    ck_install_file_contents=copy.deepcopy(soft_registration_action_dict)

    # Check if need to setup environment
    if xsetup:
       if suoa=='':
          return {'return':1, 'error':'Software environment UOA is not defined in this package (soft_uoa)'}

       if suoa!='':
          if o=='con':
             ck.out('')
             ck.out('Setting up environment for installed package ...')
             ck.out('  (full path = '+fp+')')
             ck.out('')

          if o=='con': soft_registration_action_dict['out']='con'

          rx=ck.access(soft_registration_action_dict)
          if rx['return']>0: return rx

          enduoa=rx['env_data_uoa']
          enduid=rx['env_data_uid']

    # Recording cus dict to install dir to be able to rebuild env later if needed 
    if pi!='':
       ck_install_file_path=os.path.join(pi, cfg['ck_install_file'])

       if o=='con':
          ck.out('')
          ck.out('Recording CK configuration to '+ck_install_file_path+' ...')

       ck_install_file_contents['env_data_uoa']=enduid

       rx=ck.save_json_to_file({'json_file':ck_install_file_path, 'dict':ck_install_file_contents, 'sort_keys':'yes'})
       if rx['return']>0: return rx

    if o=='con' and pi!='':
       ck.out('')
       ck.out('Installation path: '+pi)
       ck.out('')

    elapsed_time=time.time()-start_time
    if o=='con':
       ck.out('Installation time: '+str(elapsed_time)+' sec.')

    return {'return':0, 'elapsed_time':elapsed_time, 'env_data_uoa':enduoa, 'env_data_uid':enduid}

##################################################################################
# internal function: run a method of a given customization script with param_dict
#                    and top up the topup_from_install_env dictionary from install_env

def internal_run_if_present(script, method_name, param_dict, topup_from_install_env):
    if script and method_name in dir(script):
        method = getattr(script, method_name)
        rx = method( param_dict )
        if rx.get('return')==0:
            topup_from_install_env.update( rx.get('install_env',{}) )
    else:
        rx = { 'return' : 0 };
    return rx

##############################################################################
# setup package (only environment)

def setup(i):
    """
    See "install" API with skip_process=yes
    """

    i['skip_process']='yes'
    return install(i)

##############################################################################
# internal function: get value from list without error if out of bounds

def internal_get_val(lst, index, default_value):
    v=default_value
    if index<len(lst):
       v=lst[index]
    return v

##############################################################################
# rebuild dependencies using packages

def rebuild_deps(i):
    """
    Input:  {
              (target)            - if specified, use info from 'machine' module
                 or
              (host_os)           - host OS (detect, if omitted)
              (target_os)         - target OS (detect, if omitted)
              (target_device_id)  - target device ID (detect, if omitted)

              (data_uoa) or (uoa) - package UOA entry
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')

    oo=''
    if o=='con':
       oo=o

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
                 'device_cfg':device_cfg,
                 'target_device_id':tdid,
                 'skip_info_collection':'yes'})
    if r['return']>0: return r

    hos=r['host_os_uid']
    hosx=r['host_os_uoa']
    hosd=r['host_os_dict']

    tos=r['os_uid']
    tosx=r['os_uoa']
    tosd=r['os_dict']

    # Get list of deps
    duoa=i.get('data_uoa','')
    r=ck.access({'action':'load',
                 'module_uoa':work['self_module_uid'],
                 'data_uoa':duoa})
    if r['return']>0: return r

    d=r['dict']

    deps=d.get('deps',{})

    for k in sorted(deps, key=lambda v: deps[v].get('sort',0)):
        dd=deps[k]
        dn=dd.get('name','')

        if dn=='':
            dn=k
        else:
            dn+=' ('+k+')'

        tags=dd.get('tags','')

        if oo=='con':
            ck.out('*******************************************************')
            ck.out('Dependency: '+dn)
            ck.out('Tags:       '+tags)
            ck.out('')

        ntos=tos
        if dd.get('force_target_as_host','')=='yes':
             ntos=hos

        # Attempt to install package by tags
        r=ck.access({'action':'install',
            'module_uoa':work['self_module_uid'],
            'tags':tags,
            'host_os':hos,
            'target_os':ntos,
            'device_id':tdid,
            'out':oo})
        if r['return']>0: 
           ck.out('')
           ck.out('Package installation failed: '+r['error']+'!')

    return {'return':0}

##############################################################################
# show available packages

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
       ii['ck_title']='Shared CK packages'
       r=ck.access(ii)
       if r['return']>0: return r

       h=r['html_start']+'\n'
       h2=r['html_stop']+'\n'

    unique_repo=False
    if i.get('repo_uoa','')!='': unique_repo=True

    list_action_dict=copy.deepcopy(i)

    list_action_dict['out']=''
    list_action_dict['action']='list'
    list_action_dict['add_meta']='yes'
    list_action_dict['time_out']=-1

    rx=ck.access(list_action_dict)
    if rx['return']>0: return rx

    ll=sorted(rx['lst'], key=lambda k: k['data_uoa'])

    if html:
       h+='<h2>Please check our new <a href="http://ReuseResearch.com/c.php?c=package">beta browser</a> for CK components!</h2>\n'

       h+='<br>\n'

       h+='<p>CK package manager unifies installation of code, data and models across different platforms and operating systems\n'
       h+='using the most appropriate solutions including wget, make, cmake, scons, spack, vcpkg, conan, easybuild, etc.\n'

       h+='<p>'
       h+='You can install a CK package into CK virtual environment as follows:\n'
       h+='<pre>\n'
       h+=' ck pull repo:{Repo UOA - see below}\n'
       h+=' ck install package:{Package UOA - see below}\n'
       h+='</pre>\n'

       h+='using tags:\n'
       h+='<pre>\n'
       h+=' ck install package --tags={some tags from below}\n'
       h+='</pre>\n'

       h+='to an unusual path:\n'
       h+='<pre>\n'
       h+=' ck install package:{Package UOA - see below} --install_path={full installation path}\n'
       h+='</pre>\n'

       h+='to a CK virtual environment entry :\n'
       h+='<pre>\n'
       h+=' $ ck set kernel var.install_to_env=yes\n'
       h+=' ck install package:{Package UOA - see below}\n'
       h+='</pre>\n'

       h+='or for a different OS target (Android):\n'
       h+='<pre>\n'
       h+=' ck ls os:android* | sort\n'
       h+=' ck install package:{Package UOA - see below} --target_os={OS UOA from above}\n'
       h+='</pre>\n'

       h+='You can then see or use registered virtual CK environments for installed packages as follows:\n'
       h+='<pre>\n'
       h+=' ck show env\n'
       h+=' ck show env --tags={some tags from below}\n'
       h+='\n'
       h+=' ck virtual env:{UID from above}\n'
       h+=' ck virtual env --tags={some tags from below}\n'
       h+='</pre>\n'

       h+='<p>\n'
       h+='See <pre>ck install package --help</pre> for more installation options.\n'
       h+='See <a href="http://cKnowledge.org/shared-soft-detection-plugins.html">related CK soft detection plugins</a>,\n'
       h+=' <a href="https://github.com/ctuning/ck/wiki">CK documentation</a>,\n'
       h+=' <a href="https://github.com/ctuning/ck/wiki#contributing">"how to contribute" guide</a>,\n'
       h+=' <a href="https://portalparts.acm.org/3230000/3229762/fm/frontmatter.pdf">ACM ReQuEST-ASPLOS\'18 report</a>\n'
       h+=' and the latest <a href="http://cKnowledge.org/rpi-crowd-tuning">CK paper</a> for further details.\n'
       h+='See <a href="https://github.com/ctuning/ck-spack">ck-spack repository</a> connecting CK and spack package manager.\n'

       h+='<p>\n'
       h+='<table cellpadding="4" border="1" style="border-collapse: collapse; border: 1px solid black;">\n'

       h+=' <tr>\n'
       h+='  <td nowrap><b>#</b></td>\n'
       h+='  <td nowrap><b>Package UOA</b></td>\n'
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

        if lr not in cfg.get('skip_repos',[]) and private!='yes' and url!='' and lr!='ck-spack':
           num+=1

           lm=l['meta']
           ld=lm.get('desc','')

           name=lm.get('soft_name','')

           cus=lm.get('customize',{})

           ver=cus.get('version','')

           xhos=lm.get('only_for_host_os_tags',[])
           xtos=lm.get('only_for_target_os_tags',[])

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

              yh=url2+'/tree/master/package/'+ln
              x='['+url2+' '+lr+']'
              y='['+yh+' link]'

           ###############################################################
           if html:
              h+=' <tr>\n'

              x1=''
              x2=''
              z1=''
              z11=''
              if url!='':
                 x1='<a href="'+url+'">'
                 x2='</a>'
                 z1='<a href="'+yh+'">'
                 z11='<a href="'+yh+'/.cm/meta.json">'

              h+='  <td nowrap valign="top"><a name="'+ln+'">'+str(num)+'</b></td>\n'

              h+='  <td nowrap valign="top">'+z1+ln+x2+' <i>('+z11+'CK meta'+x2+')</i></td>\n'

              h+='  <td nowrap valign="top">'+template+'</td>\n'

              h+='  <td nowrap valign="top">'+x1+lr+x2+'</td>\n'

              h+='  <td valign="top"><small>'+ytags+'</small>\n'

              h+='  <td valign="top"><small>'+yhos+'</small>\n'
              h+='  <td valign="top"><small>'+ytos+'</small>\n'

              h1=''
              if ld!='':
                 h1+='<p>\n'+ld

              h+='  <td valign="top">'+h1+'\n'

              h+='</td>\n'

              h+=' </tr>\n'

           ###############################################################
           elif o=='mediawiki':
              s=''

              x=lr
              y=''
              if url!='':
                 x='['+url+' '+lr+']'
                 y='['+url+'/tree/master/package/'+ln+' link]'

              s='\n'
              s+='=== '+ln+' ('+ver+') ===\n'
              s+='\n'
              s+='Tags: <i>'+ytags+'</i>\n'
              s+='<br>Host OS tags: <i>'+yhos+'</i>\n'
              s+='<br>Target OS tags: <i>'+ytos+'</i>\n'
              if y!='':
                 s+='\n'
                 s+='Package entry with meta: <i>'+y+'</i>\n'
              s+='\n'
              s+='Which CK repo: '+x+'\n'
              if to_get!='':
                 s+='<br>How to get: <i>'+to_get+'</i>\n'
              if to_get!='':
                 s+='\n'
                 s+='How to install: <i>ck install package:'+ln+' (--target_os={CK OS UOA})</i>'

              s+='\n'

              if of=='':
                 ck.out(s)
              else:
                 with open(of, "a") as ff:
                      ff.write(s)
                 
                 size+=len(s)
                 if size>=100000:
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
    ck.out('  Total packages: '+str(num))
    ck.out('')

    if html:
       h+='</table>\n'
       h+=h2

       if of!='':
          r=ck.save_text_file({'text_file':of, 'string':h})
          if r['return']>0: return r

    return {'return':0, 'html':h}

##############################################################################
# prepare installation path

def prepare_install_path(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              path         - prepared path where to install packages
            }

    """

    import os

    # Moved Tools to $HOME by default if CK_TOOLS is not defined
    x=os.environ.get(cfg["env_install_path"],'')
    if x=='':
       # Get home user directory
       from os.path import expanduser
       home = expanduser("~")
       x=os.path.join(home, cfg["install_path"])
       if not os.path.isdir(x):
          os.makedirs(x)

    return {'return':0, 'path':x}

##############################################################################
# prepare distribution

def distribute(i):
    """
    Input:  {
              (data_uoa) - package UOA

              (ext)      - output package ext (ck-distro-{ext}).zip  If not specified, UID is generated.
                or
              (filename) - full name of output package

              (path_key) - (path_bin, path_lib, path_include)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os
    import shutil

    # Init
    o=i.get('out','')

    oo=''
    if o=='con':
       oo=o

    cur_dir=os.getcwd()

    duoa=i.get('data_uoa','')
    tags=i.get('tags','')

    pk=i.get('path_key','')
    if pk=='': pk='path_bin'

    # Extension
    fn=i.get('filename','')
    if fn=='':
       ext=i.get('ext','')
       if ext=='':
          rx=ck.gen_uid({})
          if rx['return']>0: return rx
          ext=rx['data_uid']

       fn='ck-distro-'+ext+'.zip'

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
                 'device_cfg':device_cfg,
                 'target_device_id':tdid,
                 'skip_info_collection':'yes'})
    if r['return']>0: return r

    hos=r['host_os_uid']
    hosx=r['host_os_uoa']
    hosd=r['host_os_dict']

    tos=r['os_uid']
    tosx=r['os_uoa']
    tosd=r['os_dict']

    host_add_path_string=r.get('host_add_path_string','')

    hosn=hosd.get('ck_name2','')
    osn=tosd.get('ck_name2','')

    # Load package meta
    r=ck.access({'action':'load',
                 'module_uoa':work['self_module_uid'],
                 'data_uoa':duoa})
    if r['return']>0: return r
    d=r['dict']
    p0=r['path']

    # Get tags
    tags=d['tags']
    xtags=','.join(tags)

    # Resolve env
    if o=='con':
       ck.out('Searching environment for this package ...')

    r=ck.access({'action':'set',
                 'module_uoa':cfg['module_deps']['env'],
                 'tags':xtags,
                 'host_os':hos,
                 'target_os':tos,
                 'device_id':tdid,
                 'out':oo})
    if r['return']>0: return r

    de=r['dict']

    deps=de.get('deps',{})

    # Path
    cus=de.get('customize',{})
    pp=cus.get(pk,'')
    pp1=pp

    found=False
    while not found:
        pp1=os.path.dirname(pp)

        if pp1==pp:
           break

        ppx=os.path.join(pp1, cfg['ck_install_file'])
        if os.path.isfile(ppx):
           found=True
           break

        pp=pp1

    # Read ck-install.json
    if not found:
       return {'return':1, 'error':pp1+' not found in installation paths ...'}

    r=ck.load_json_file({'json_file':ppx})
    if r['return']>0: return r
    dx=r['dict']

    # Rename deps (to avoid mix ups with local env)
#    dx['saved_deps']=dx.pop('deps')

    # Save to tmp file
    rx=ck.gen_tmp_file({'prefix':'tmp-ck-', 'suffix':'.json'})
    if rx['return']>0: return rx
    ftmp=rx['file_name']

    r=ck.save_json_to_file({'json_file':ftmp, 'dict':dx, 'sort_keys':'yes'})
    if r['return']>0: return r

    # Check extra commands (for a given target platform)
    ec=d.get('distribute_extra_commands',{}).get(osn,[])

    for q in ec:
        if o=='con':
           ck.out('')
           ck.out('Executing extra command')
           ck.out('')

        q['out']=oo
        q['host_os']=hos
        q['target_os']=tos
        q['device_id']=tdid

        r=ck.access(q)
        if r['return']>0: return r

    # Check extra files (for a given target platform)
    ef=d.get('distribute_extra_file',{}).get(osn,[])

    r=get_paths_from_deps({'deps':deps})
    if r['return']>0: return r
    paths=r['paths']

    for q in ef:
        fx=q['file']

        if o=='con':
           ck.out('')
           ck.out('  * Searching extra file '+fx+' ...')

        where=q.get('where_key','')
        if where=='': where='path_bin'

        pzz=''

        muoa=q.get('module_uoa','')
        duoa=q.get('data_uoa','')
        if muoa!='' and duoa!='':
           r=ck.access({'action':'load',
                        'module_uoa':muoa,
                        'data_uoa':duoa})
           if r['return']>0: return r
           py=r['path']

           pi=q.get('extra_dir','')
           if pi!='': py=os.path.join(py,pi)

           pzz=os.path.join(py,fx)

        else:
           for py in paths:
               pz=os.path.join(py,fx)
               if os.path.isfile(pz):
                  pzz=pz
                  break

        if pzz=='':
           return {'return':1, 'error':'file not found'}

        if o=='con':
           ck.out('       Found ('+pzz+') - copying ...')

        pz1=cus.get(pk,'')

        if q.get('new_file','')!='': fx=q['new_file']

        pz2=os.path.join(pz1, fx)

        if os.path.isfile(pz2): os.remove(pz2)

        shutil.copyfile(pzz, pz2)

    # Check extra dirs (dist) in package
    px=os.path.join(p0,'dist')
    if os.path.isdir(px):
       if o=='con':
          ck.out('')
          ck.out('Copying extra dist directory ...')

       pxx=os.listdir(px)

       for q in pxx:
           q1=os.path.join(px,q)
           q2=os.path.join(pp,q)

           if o=='con':
              ck.out('  * '+q)

           if os.path.isdir(q2) or os.path.isfile(q2): 
              shutil.rmtree(q2)

           shutil.copytree(q1,q2)

    # Prepare zip
    import zipfile

    zip_method=zipfile.ZIP_DEFLATED

    r=ck.list_all_files({'path':pp})
    if r['return']>0: return r

    flx=r['list']

    # Write archive
    if o=='con':
       ck.out('')
       ck.out('Recording generated package to '+fn+' ...')

    pfn=os.path.join(cur_dir,fn)

    try:
       f=open(pfn, 'wb')
       z=zipfile.ZipFile(f, 'w', zip_method)

       for fn in flx:
           p1=os.path.join(pp, fn)
           z.write(p1, 'install'+os.sep+fn, zip_method)

       # ck-install.json
       z.write(ftmp, cfg['ck_install_file_saved'], zip_method)

       z.close()
       f.close()

    except Exception as e:
       return {'return':1, 'error':'failed to prepare archive ('+format(e)+')'}

    if os.path.isfile(ftmp):
       os.remove(ftmp)

    return {'return':0}

##############################################################################
# get all paths from deps

def get_paths_from_deps(i):
    """
    Input:  {
              (deps)  - deps
              (paths) - current list of paths
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    deps=i.get('deps',{})
    paths=i.get('paths',[])

    for k in sorted(deps, key=lambda v: deps[v].get('sort',0)):
        dp=deps[k]

        uoa=dp.get('uoa','')
        if uoa!='':
           r=ck.access({'action':'load',
                        'module_uoa':cfg['module_deps']['env'],
                        'data_uoa':uoa})
           if r['return']>0: return r
           dp1=r['dict']

           dpx=dp1.get('customize',{})

           x=dpx.get('path_bin','')
           if x!='' and x not in paths: paths.append(x)

           if x=='':
              # Trick for some dll on Windows
              x=dpx.get('path_lib','')
              if x!='':
                 x=os.path.dirname(x)
                 x=os.path.join(x,'bin')
                 if os.path.isdir(x) and x not in paths: paths.append(x)

           x=dpx.get('path_lib','')
           if x!='' and x not in paths: paths.append(x)
       
           x=dpx.get('path_include','')
           if x!='' and x not in paths: paths.append(x)

           ndpd=dp1.get('deps',{})
           if len(ndpd)>0:
              r=get_paths_from_deps({'deps':ndpd, 'paths':paths})
              if r['return']>0: return r
              paths=r['paths']

    return {'return':0, 'paths':paths}

##############################################################################
# reinstall package if already installed

def reinstall(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    i['reinstall']='yes'
    return install(i)

##############################################################################
# add package with template

def add(i):
    """
    Input:  {
              soft       - specify related soft UOA

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

    # Check related soft first
    suoa=i.get('soft','')
    if suoa=='':
       return {'return':1, 'error':'related software detection plugin is not specified. Specify the existing one using --soft={name from http://cKnowledge.org/shared-soft-detection-plugins.html} or create a new one using "ck add soft {repo}:soft:{name}"'}

    # Load soft to get UID and tags
    r=ck.access({'action':'load',
                 'module_uoa':cfg['module_deps']['soft'],
                 'data_uoa':suoa})
    if r['return']>0: return r

    suid=r['data_uid']
    sd=r['dict']
    stags=sd.get('tags',[])

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

    # Process tags
    xtags=i.get('tags','')
    if xtags=='':
       ck.out('')
       r=ck.inp({'text':'Enter extra version tags for your package plugin separated by comma (for example v6.0,v6): '})
       xtags=r['string'].strip()

    tags=stags
    if xtags!='':
       for q in xtags.split(','):
           q=q.strip()
           if q not in tags:
              tags.append(q)

    dd['soft_uoa']=suid
    dd['tags']=tags

    x=sd.get('customize',{}).get('soft_file_universal','')
    if x!='':
       dd['end_full_path_universal']=x
    else:
       x=sd.get('customize',{}).get('soft_file',{})
       if x!='':
          dd['end_full_path']=x

    # Update new entry
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
       ck.out('Further details about how to update meta.json and other files of your new package installation plugin:')
       ck.out('')
       ck.out(' * https://github.com/ctuning/ck/wiki/Adding-new-workflows')

    return ck.access(ii)

##############################################################################
# internal: print community warning when package fails

def print_warning(i):
    """
    Input:  {
              package_data_uoa
              package_repo_uoa
              package_meta
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    # Check if this warning is disabled in CK kernel
    if ck.cfg.get('skip_message_when_package_fails')!='yes':
       pduoa=i['package_data_uoa']
       pruoa=i['package_repo_uoa']
       pmeta=i['package_meta']

       package_ie=pmeta.get('customize',{}).get('install_env',{})
       purl=package_ie.get('PACKAGE_URL','')
       pc=package_ie.get('PACKAGE_GIT_CHECKOUT','')

       ck.out('')
       ck.out('   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

       ck.out('   CK detected a PROBLEM in the third-party CK package:')

#       ck.out('CK packages are developed, shared and improved by the community')
#       ck.out('to help users automate installation and customization')
#       ck.out('of code and data across diverse and evolving platforms:')
#       ck.out('* http://cKnowledge.org/shared-packages.html')
#
#       ck.out('')
#       ck.out('Therefore, they may sometimes fail with newer code versions,')
#       ck.out('under new settings or in previously unseen environments.')
#
#       ck.out('')
#       ck.out('In such case, please help the community by fixing the problem')
#       ck.out('and/or reporting it via CK mailing list and related repository:')
#       ck.out('(please provide all details about how to reproduce it):')
#
#       ck.out('')
#       ck.out('* https://groups.google.com/forum/#!forum/collective-knowledge')
#
#       ck.out('')
#       ck.out('You can turn off this message as follows:')
#       ck.out('$ ck set kernel --var.skip_message_when_package_fails=yes')

       # sometimes pruoa can still be UID -> check
       r=ck.access({'action':'load', 'module_uoa':work['self_module_uid'], 'data_uoa':pduoa})
       if r['return']==0:
          pduoa=r['data_uoa']

       url2=''

       crurl=''
       if pduoa!='' or pruoa!='':
          ck.out('')
          ck.out('   CK package:           '+pduoa)

          if purl!='':
             ck.out('   Native package URL:   '+purl)
             if pc!='':
                ck.out('   Git checkout:         '+pc)

          if pruoa!='':
             ck.out('   CK repo:              '+pruoa)

             # Attempt to read info about this repo
             r=ck.access({'action':'load',
                          'module_uoa':cfg['module_deps']['repo'],
                          'data_uoa':pruoa})
             if r['return']==0:
                d=r['dict']
                url=d.get('url','')
                if url!='':
                   url1=url+'/tree/master/package/'+pduoa
                   url2=url+'/issues'
                   ck.out('   CK repo URL:          '+url)
                   ck.out('   CK package URL:       '+url1)

                   ck.out('   Issues URL:           '+url2)

                   crurl=ck.cfg.get('wiki_data_web','')
                   if crurl!='':
                      crurl+='package/'+pduoa
#                      ck.out('')
 #                     ck.out('   CK stable package URL: '+crurl)

       x1='the community'
       x2='https://groups.google.com/forum/#!forum/collective-knowledge'
       x3='https://github.com/ctuning/ck/issues'
#       if url2!='':
#          x1='the authors'
#          x2=url2

       if crurl!='':
          ck.out('')
          ck.out('   Please, check that there is no discussion about this issue at '+crurl)
          ck.out('')

       ck.out('   Please, submit the *full* log to:')
       ck.out('     * '+x2)
       ck.out('     * '+x3)

       ck.out('   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
       ck.out('')

    return {'return':0}
