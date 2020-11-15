#
# Collective Knowledge (program)
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
# clean, compile and run program(s) - can be with wildcards
# (afterwards will call "process_in_dir" to clean, compile and run specific programs)

def process(i):
    """
    Input:  {
              sub_action   - clean, compile, run

              (repo_uoa)        - program repo UOA
              (module_uoa)      - program module UOA
              (data_uoa)        - program data UOA
              (program_tags)    - an alternative mechanism for finding a program by a unique combination of tags

              (host_os)        - host OS (detect, if omitted)
              (target_os)      - OS module to check (if omitted, analyze host)
              (device_id)      - device id if remote (such as adb)

              (process_in_tmp)       - (default 'yes') - if 'yes', clean, compile and run in the tmp directory
              (tmp_dir)              - (default 'tmp') - if !='', use this tmp directory to clean, compile and run
              (generate_rnd_tmp_dir) - if 'yes', generate random tmp directory

            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              Output of the last compile from function 'process_in_dir'

              tmp_dir      - directory where clean, compile, run
            }

    """

    import os
    import copy

    ic=copy.deepcopy(i)

    # Check if global writing is allowed
    r=ck.check_writing({})
    if r['return']>0: return r

    o=i.get('out','')

    ruoa=i.get('repo_uoa','')
    muoa=i.get('module_uoa','')
    duoa=i.get('data_uoa','')
    program_tags = i.get('program_tags','')

    lst=[]

    if duoa!='':
        # Potentially fill wildcards:
        r=ck.search({'action':'search',
                    'repo_uoa':ruoa,
                    'module_uoa':muoa,
                    'data_uoa':duoa,
                    'add_meta':'yes',
        })  # contains path and meta.json in 'meta'
        if r['return']>0: return r
        lst=r['lst']

    elif program_tags:
        r=ck.access({'action':           'search_in_variations',
                    'module_uoa':        'misc',
                    'query_module_uoa':  work['self_module_uid'],
                    'tags':              program_tags,
        })  # contains path and meta.json in 'meta'
        if r['return']>0: return r
        lst=r['lst']

    else:
        # First, try to detect CID in current directory
        r=ck.cid({})
        if r['return']==0:
            ruoa=r.get('repo_uoa','')
            muoa=r.get('module_uoa','')
            duoa=r.get('data_uoa','')

            rx=ck.access({'action':'load',
                        'module_uoa':muoa,
                        'data_uoa':duoa,
                        'repo_uoa':ruoa,
            })  # contains path and meta.json in 'dict'
            if rx['return']==0 and rx['dict'].get('program','')=='yes':
                rx['meta'] = rx.pop('dict')     # enforcing 'meta'/'dict' output format compatibility
                lst = [ rx ]

        if duoa=='':
            # Attempt to load configuration from the current directory
            try:
                p=os.getcwd()
            except OSError:
                os.chdir('..')
                p=os.getcwd()

            pc=os.path.join(p, ck.cfg['subdir_ck_ext'], ck.cfg['file_meta'])
            if os.path.isfile(pc):
                r=ck.load_json_file({'json_file':pc})
                if r['return']==0 and r['dict'].get('program','')=='yes':
                    d=r['dict']

                    ii=copy.deepcopy(ic)
                    ii['path']=p
                    ii['meta']=d
                    return process_in_dir(ii)

            return {'return':1, 'error':'data UOA is not defined'}

    if len(lst)==0:
       return {'return':1, 'error':'no program(s) found'}

    r={'return':0}
    for ll in lst:

        path=ll['path']
        ruid=ll['repo_uid']
        muid=ll['module_uid']
        duid=ll['data_uid']
        dalias=ll['data_uoa']
        meta_dict=ll['meta']

        if o=='con':
           ck.out('')
           ck.out('* '+dalias+' ('+duid+')')
           ck.out('')

        # Check if base_uoa suggests to use another program path
        buoa=meta_dict.get('base_uoa','')
        if buoa!='':
           rx=ck.access({'action':'find',
                         'module_uoa':muid,
                         'data_uoa':buoa})
           if rx['return']>0:
              return {'return':1, 'error':'problem finding base entry '+buoa+' ('+rx['error']+')'}

           path=rx['path']

        ii=copy.deepcopy(ic)
        ii['meta']=meta_dict
        ii['path']=path
        ii['repo_uoa']=ruid
        ii['module_uoa']=muid
        ii['data_uoa']=duid
        ii['data_alias']=dalias
        r=process_in_dir(ii)

        if r['return']>0 or r.get('misc',{}).get('fail_reason','')!='':
           print_warning({'data_uoa':dalias, 'repo_uoa':ruid})
        if r['return']>0: return r

    return r

##############################################################################
# compile, run and clean a given CK program (called from universal functions here)

def process_in_dir(i):
    """
    Input:  {
              Comes from 'compile', 'run' and 'clean' functions

              sub_action             - clean, compile, run

              (host_os)              - host OS (detect, if omitted)
              (target_os)            - OS module to check (if omitted, analyze host)
              (device_id)            - device id if remote (such as adb)

              (target)               - target machine added via 'ck add machine' with prepared target description
                                       (useful to create farms of machines for crowd-benchmarking and crowd-tuning using CK)

              (device_cfg)           - extra device cfg (if empty, will be filled in from 'machine' module description)

              (compute_platform_id)  - if !='', set env['CK_COMPUTE_PLATFORM_ID']
              (compute_device_id)    - if !='', set env['CK_COMPUTE_DEVICE_ID']

              path                   - path
              meta                   - program description

              (tmp_dir)              - if !='', use it instead of 'tmp' dir to compile and run code
              (generate_rnd_tmp_dir) - if 'yes', generate random tmp directory to compile and run program
                                       (useful during crowd-tuning)

              (run_batch_name)       - if !='', use this batch name instead of randomly generated one

              (compiler_vars)        - dict with set up compiler flags (-D var)
                                       they will update the ones defined as default in program description ...

              (no_vars)              - skip compiler vars (if you want to use default ones from the sources) ...

              (compiler_tags)        - extra compiler tags

              (remove_compiler_vars) - list of compiler vars to remove

              (extra_env_for_compilation) - set environment variables before compiling program

              (flags)                - compile flags
              (lflags)               - link flags

              (speed)                - if 'yes', compile for speed (use env CK_OPT_SPEED from compiler)
              (size)                 - if 'yes', compile for size (use env CK_OPT_SIZE from compiler)

              (compile_type)         - static or dynamic (dynamic by default;
                                         however takes compiler default_compile_type into account)
                  or
              (static or dynamic)

              (use_clang_opt)        - use Clang opt optimizer

              (repeat)               - repeat kernel via environment CT_REPEAT_MAIN if supported

              (sudo)                 - if 'yes', force using sudo
                                       (if not set up in OS, use ${CK_SUDO_INIT}, ${CK_SUDO_PRE}, ${CK_SUDO_POST})

              (affinity)             - set processor affinity for tihs program run (if supported by OS - see "affinity" in OS)
                                       examples: 0 ; 0,1 ; 0-3 ; 4-7  (the last two can be useful for ARM big.LITTLE arhictecture

              (clean)                - if 'yes', clean tmp directory before using
              (skip_clean_after)     - if 'yes', do not remove run batch
              (keep)                 - the same as skip_clean_after

              (repo_uoa)             - program repo UOA
              (module_uoa)           - program module UOA
              (data_uoa)             - program data UOA

              (params)               - dictionary with parameters passed via pre/post processing to third-party tools
                                       for example, to configure ARM Workload Automation
              (params.{KEY})         - set params[KEY]=value (user-friendly interface via CMD)

              (misc)                 - misc  dict
              (characteristics)      - characteristics/features/properties
              (env)                  - preset environment
              (env.{KEY})            - set env[KEY]=value (user-friendly interface via CMD)

              (deps.{KEY})           - set deps[KEY]["uoa']=value (user-friendly interface via CMD to set any given dependency)
              (preset_deps)          - dict with {"KEY":"UOA"} to preset dependencies

              (post_process_script_uoa) - run script from this UOA
              (post_process_subscript)  - subscript name
              (post_process_params)     - (string) add params to CMD

              (deps)                 - already resolved deps (useful for auto-tuning)
              (deps_cache)           - list of already resolved deps (useful to automate crowd-benchmarking and crowd-tuning)
              (reuse_deps)           - if 'yes', reuse deps by keys

              (dep_add_tags.{KEY})   - extra tags added to specific subdictionary of deps{} for this particular resolution session

              (cmd_key)              - CMD key
              (dataset_uoa)          - UOA of a dataset
              (dataset_file)         - dataset filename (if more than one inside one entry - suggest to have a UID in name)

              (extra_env)            - extra environment before running code as string
              (pre_run_cmd)          - pre CMD for binary
              (extra_run_cmd)        - extra CMD (can use $#key#$ for autotuning)
              (debug_run_cmd)        - substitute CMD with this one - usually useful for debugging to pre-set env for all deps
              (run_cmd_substitutes)  - dict with substs ($#key#$=value) in run CMD (useful for CMD autotuning)

              (console)              - if 'yes', output to console

              (skip_device_init)     - if 'yes', do not initialize device

              (skip_calibration)     - if 'yes', skip execution time calibration (make it around 4.0 sec)
              (calibration_time)     - calibration time in string, 4.0 sec. by default
              (calibration_max)      - max number of iterations for calibration, 10 by default

              (pull_only_timer_files) - if 'yes', pull only timer files, but not output files
                                        (useful for remove devices during statistical repetition)

              (energy)                - if 'yes', start energy monitoring (if supported) using script ck-set-power-sensors
                                       Also, set compiler var CK_MONITOR_ENERGY=1 and run-time var CK_MONITOR_ENERGY=1

                                       Note: files, monitored for energy, are defined in system environment.
                                             For example, odroid .profile as:
                                               export CK_ENERGY_FILES="/sys/bus/i2c/drivers/INA231/3-0040/sensor_W;/sys/bus/i2c/drivers/INA231/3-0041/sensor_W;/sys/bus/i2c/drivers/INA231/3-0044/sensor_W;/sys/bus/i2c/drivers/INA231/3-0045/sensor_W;"

              (run_output_files)              - extra list of output files (useful to add in pipeline to collect profiling from Android mobile, for example)

              (extra_post_process_cmd)        - append at the end of execution bat (for example, to call gprof ...)

              (statistical_repetition_number) - int number of current (outside) statistical repetition
                                                to avoid pushing data to remote device if !=0 ...
              (autotuning_iteration)          - int number of current autotuning iteration
                                                to avoid pushing some data to remote device if !=0 ...
              (skip_dataset_copy)             - if 'yes', dataset stays the same across iterations of pipeline, so do not copy to remote again

              (unparsed)                      - if executing ck run program ... -- (unparsed params), add them to compile or run ...

              (compile_timeout)               - (sec.) - kill compile job if too long
              (run_timeout)                   - (sec.) - kill run job if too long

              (add_rnd_extension_to_bin)      - if 'yes', add random extension to binary and record list
              (add_save_extension_to_bin)     - if 'yes', add '.save' to bin to save during cleaning ...

              (skip_print_timers)             - if 'yes', skip printing fine-grain timers after execution

              (skip_file_print)               - skip file printing (if 'print_files_after_run' list is in program meta)

              (skip_output_validation)        - skip validation of output (dangerous during auto-tuning -
                                                  some optimizations may break semantics or change accuracy)
              (output_validation_repo)        - output validation repo UOA (when recording new output)
              (program_output_uoa)            - use this UOA to check/record program output 
                                                (to have the same output entry for groups of similar programs)

              (overwrite_reference_output)    - if 'yes', overwrite reference output (useful if broken)

              (quiet)                         - if 'yes', automatically provide default answer to all questions when resolving dependencies ...
              (random)                        - if 'yes', select deps randomly (useful for quite crowd-tuning / DNN classification)

              (install_to_env)       - install dependencies to env instead of CK-TOOLS (to keep it clean)!

              (safe)                 - safe mode when searching packages first instead of detecting already installed soft
                                       (to have more deterministic build)

              (skip_exec)            - if 'yes', do not clean output files and skip exec to be able to continue

              (record_deps)          - if !='', record dependencies to this file
            }

    Output: {
              return          - return code =  0, if successful
                                            >  0, if error
              (error)         - error text if return > 0

              misc            - updated misc dict
              characteristics - updated characteristics
              env             - updated environment
              deps            - resolved deps, if any
            }

    """
    import os
    import time
    import sys
    import shutil
    import time
    import copy

    start_time=time.time()

    sys.stdout.flush()

    o=i.get('out','')
    oo=''
    if o=='con': oo='con'

    sa=i['sub_action']

    sdi=i.get('skip_device_init','')

    sca=i.get('skip_clean_after','')
    if sca=='':
       sca=i.get('keep','')

    grtd=i.get('generate_rnd_tmp_dir','')

    quiet=i.get('quiet','')
    ran=i.get('random','')

    rbn=i.get('run_batch_name','')

    iev=i.get('install_to_env','')
    safe=i.get('safe','')
    skip_exec=i.get('skip_exec','')
    record_deps=i.get('record_deps','')

    misc=i.get('misc',{})
    ccc=i.get('characteristics',{})
    env=i.get('env',{})
    xparams=i.get('params',{})

    uco=i.get('use_clang_opt','')=='yes'

    deps=i.get('deps',{})
    reuse_deps=i.get('reuse_deps','')
    deps_cache=i.get('deps_cache',[])

    # Check user-friendly env and params
    preset_deps=i.get('preset_deps', {})
    dep_add_tags = i.get('dep_add_tags', {})
    for q in i:
        if q.startswith('env.'):
           env[q[4:]]=i[q]
        elif q.startswith('params.'):
           xparams[q[7:]]=i[q]
        elif q.startswith('deps.'):
           preset_deps[q[5:]]=i[q].split(':')[-1]
        elif q.startswith('dep_add_tags.'):
           _ , dep_name    = q.split('.')
           dep_add_tags[dep_name] = i[q]


    are=i.get('add_rnd_extension_to_bin','')
    ase=i.get('add_save_extension_to_bin','')

    rof=i.get('run_output_files',[])
    eppc=i.get('extra_post_process_cmd','')

    unparsed=i.get('unparsed', [])
    sunparsed=''
    for q in unparsed:
        if sunparsed!='': sunparsed+=' '
        sunparsed+=q

    sfp=i.get('skip_file_print','')

    ee=i.get('extra_env','')
    ercmd=i.get('extra_run_cmd','')
    drcmd=i.get('debug_run_cmd','')

    prcmd=i.get('pre_run_cmd','')
    rcsub=i.get('run_cmd_substitutes','')

    cons=i.get('console','')

    flags=i.get('flags','')
    if uco:
       split_flags=flags.split(' ')

    lflags=i.get('lflags','')
    cv=i.get('compiler_vars',{})
    ncv=i.get('no_vars',{})
    ctags=i.get('compiler_tags','')
    rcv=i.get('remove_compiler_vars',[])
    eefc=i.get('extra_env_for_compilation',{})

    fspeed=i.get('speed','')
    fsize=i.get('size','')

    xrepeat=i.get('repeat','')
    if xrepeat=='': xrepeat='-1'
    repeat=int(xrepeat)

    me=i.get('energy','')

    xcto=i.get('compile_timeout','')
    xrto=i.get('run_timeout','')

    pp_uoa=i.get('post_process_script_uoa','')
    pp_name=i.get('post_process_subscript','')
    pp_params=i.get('post_process_params','')

    # Check if need to initialize device and directly update input i !
    r=ck.access({'action':'find',
                 'module_uoa':cfg['module_deps']['module'],
                 'data_uoa':cfg['module_deps']['machine']})
    if r['return']==0:
        ii={'action':'init',
            'module_uoa':cfg['module_deps']['machine'],
            'input':i}

        if sa=='run':
            ii['check']='yes'

        r=ck.access(ii)
        if r['return']>0: return r

    device_cfg=i.get('device_cfg',{})

    # Check host/target OS/CPU
    hos=i.get('host_os','')
    tos=i.get('target_os','')
    tdid=i.get('device_id','')

    # Get some info about platforms
    ii={'action':'detect',
        'module_uoa':cfg['module_deps']['platform.os'],
        'host_os':hos,
        'target_os':tos,
        'device_cfg':device_cfg,
        'device_id':tdid,
        'skip_device_init':sdi}

    if sa=='run':
       x='no'
       if i.get('skip_info_collection','')!='': x=i['skip_info_collection']
       ii['skip_info_collection']=x
       ii['out']=oo
    else:
       ii['skip_info_collection']='yes'

    r=ck.access(ii)
    if r['return']>0: return r

    hos=r['host_os_uid']
    hosx=r['host_os_uoa']
    hosd=r['host_os_dict']

    tos=r['os_uid']
    tosx=r['os_uoa']
    tosd=r['os_dict']

    tplat=tosd.get('ck_name','')
    tplat2=tosd.get('ck_name2','')

    host_add_path_string=r.get('host_add_path_string','')
    target_add_path_string=r.get('target_add_path_string','')

    if r['device_id']!='': tdid=r['device_id']
    xtdid=''
    if tdid!='': xtdid=' -s '+tdid

    remote=tosd.get('remote','')
    remote_ssh=tosd.get('remote_ssh','')

    tbits=tosd.get('bits','')

    # Update env for host from host/target OS desc if needed (for example for RPC)
    x=hosd.get('preset_host_env',{})

    if len(x)>0:
       env.update(x)
    x=tosd.get('preset_host_env',{})
    if len(x)>0:
       env.update(x)

    # Add path to CK target entry if used (to get machine specific files if needed)
    x=device_cfg.get('path_to_ck_target_entry','')
    if x!='':
       env['CK_TARGET_PATH']=x

    # update misc
    misc['host_os_uoa']=hosx
    misc['target_os_uoa']=tosx
    misc['target_os_bits']=tbits
    misc['device_id']=tdid

    # Check compile type
    ctype=i.get('compile_type','')
    if i.get('static','')=='yes': ctype='static'
    if i.get('dynamic','')=='yes': ctype='dynamic'
    # On default Android-32, use static by default
    # (old platforms has problems with dynamic)
    if ctype=='':
       if tosd.get('default_compile_type','')!='':
          ctype=tosd['default_compile_type']
       else:
          ctype='dynamic'

    # Get host platform type (linux or win)
    rx=ck.get_os_ck({})
    if rx['return']>0: return rx
    hplat=rx['platform']

    bbp=hosd.get('batch_bash_prefix','')
    bbpt=tosd.get('batch_bash_prefix','')
    rem=hosd.get('rem','')
    eset=hosd.get('env_set','')
    etset=tosd.get('env_set','')
    svarb=hosd.get('env_var_start','')
    svarb1=hosd.get('env_var_extra1','')
    svare=hosd.get('env_var_stop','')
    svare1=hosd.get('env_var_extra2','')
    scall=hosd.get('env_call','')
    sdirs=hosd.get('dir_sep','')
    sdirsx=tosd.get('remote_dir_sep','')
    if sdirsx=='': sdirsx=sdirs
    stdirs=tosd.get('dir_sep','')
    sext=hosd.get('script_ext','')
    sexe=hosd.get('set_executable','')
    se=tosd.get('file_extensions',{}).get('exe','')
    sbp=hosd.get('bin_prefix','')
    stbp=tosd.get('bin_prefix','')
    sqie=hosd.get('quit_if_error','')
    evs=hosd.get('env_var_separator','')
    envsep=hosd.get('env_separator','')
    envtsep=tosd.get('env_separator','')
    eifs=hosd.get('env_quotes_if_space','')
    eifsc=hosd.get('env_quotes_if_space_in_call','')
    eifsx=tosd.get('remote_env_quotes_if_space','')
    if eifsx=='': eifsx=eifsc
    wb=tosd.get('windows_base','')
    stro=tosd.get('redirect_stdout','')
    stre=tosd.get('redirect_stderr','')
    ubtr=hosd.get('use_bash_to_run','')
    no=tosd.get('no_output','')
    bex=hosd.get('batch_exit','')

    md5sum=hosd.get('md5sum','')

    # env for targets
    tsvarb=tosd.get('env_var_start','')
    tsvarb1=tosd.get('env_var_extra1','')
    tsvare=tosd.get('env_var_stop','')
    tsvare1=tosd.get('env_var_extra2','')

    ########################################################################
    p=i['path']
    meta=i['meta']

    ruoa=i.get('repo_uoa', '')
    muoa=i.get('module_uoa', '')
    duoa=i.get('data_uoa', '') # There will be data UID (not alias) from 'process' function from this module!
    dalias=i.get('data_alias','') 

    ########################################################################
    # Check if correct target OS
    r=ck.access({'action':'check_target',
                 'module_uoa':cfg['module_deps']['soft'],
                 'dict':meta,
                 'host_os_uoa':hos,
                 'host_os_dict':hosd,
                 'target_os_uoa':tos,
                 'target_os_dict':tosd})
    if r['return']>0: return r

    # Check if need specific device access type
    dat=meta.get('required_device_access_type',[])
    if len(dat)>0 and device_cfg.get('access_type','') not in dat:
       return {'return':1, 'error':'This program can not be used with the specified device target (need '+str(dat)+')'}

    target_exe=meta.get('target_file','')
    if target_exe=='' and meta.get('no_target_file','')!='yes':
       target_exe=cfg.get('target_file','')

    if are=='yes' and target_exe!='':
       rx=ck.gen_uid({})
       if rx['return']>0: return rx
       target_exe+='-'+rx['data_uid']

    if (meta.get('skip_bin_ext','')!='yes' or tplat=='win') and target_exe!='':
       target_exe+=se

    if ase=='yes' and target_exe!='':
       target_exe+='.save'

    if target_exe!='':
       misc['target_exe']=target_exe

    if meta.get('version','')!='':
       misc['program_version']=meta['version']

    # If muoa=='' assume program
    if muoa=='':
       muoa=work['self_module_uid']

    if duoa=='':
       x=meta.get('backup_data_uid','')
       if x!='':
          duoa=meta['backup_data_uid']

    # Reuse compile deps in run (useful for large benchmarks such as SPEC where compile and run is merged)
    rcd=meta.get('reuse_compile_deps_in_run','')

    # Check if compile in tmp dir
    cdir=p
    os.chdir(cdir)

    # Prepare params (if needed - for example, for ARM Workload Automation)
    params=meta.get('default_params',{})
    r=ck.merge_dicts({'dict1':params, 'dict2':xparams})
    if r['return']>0: return r

    ########################################################################
    # Check if need to add paths to CK entries as env
    qq=meta.get('ck_to_env',{})
    for q in qq:
        qc=qq[q]
        r=ck.access({'action':'find',
                     'cid':qc})
        if r['return']>0: return r
        env[q]=r['path']

    ########################################################################
    # Check affinity
    aff=i.get('affinity','')
    if aff!='':
       aff=tosd.get('set_affinity','').replace('$#ck_affinity#$',aff)

    ########################################################################
    # Check sudo

    sudo_init=tosd.get('sudo_init','')
    if sudo_init=='': sudo_init=svarb+svarb1+'CK_SUDO_INIT'+svare1+svare
    sudo_pre=tosd.get('sudo_pre','')
    if sudo_pre=='': sudo_pre=svarb+svarb1+'CK_SUDO_PRE'+svare1+svare
#    sudo_post=tosd.get('sudo_post','')
#    if sudo_post=='':
    sudo_post=svarb+svarb1+'CK_SUDO_POST'+svare1+svare

    isd=i.get('sudo','')
    if isd=='': isd=tosd.get('force_sudo','')

    srn=ck.get_from_dicts(i, 'statistical_repetition_number', '', None)
    if srn=='': srn=0
    else: srn=int(srn)

    ati=ck.get_from_dicts(i, 'autotuning_iteration', '', None)
    if ati=='': ati=0
    else: ati=int(ati)

    sdc=ck.get_from_dicts(i, 'skip_dataset_copy', '', None)

    ##################################################################################################################
    ################################### Clean ######################################
    if sa=='clean':
       # Get host platform type (linux or win)
       cmd=cfg.get('clean_cmds',{}).get(hplat)

       if o=='con':
          ck.out(cmd)
          ck.out('')

       if ubtr!='': cmd=ubtr.replace('$#cmd#$',cmd)
       rx=os.system(cmd)

       # Removing only 1 tmp directory. If there are multiple - may be used for crowdtuning - do not delete
       try:
           curdir=os.getcwd()
       except OSError:
           os.chdir('..')
           curdir=os.getcwd()

       q=os.path.join(curdir, 'tmp')
       if os.path.isdir(q):
          shutil.rmtree(q, ignore_errors=True)

#       for q in os.listdir(curdir):
#           if not os.path.isfile(q) and q.startswith('tmp'):
#              shutil.rmtree(q, ignore_errors=True)

       return {'return':0}

    # shall we process_in_tmp or not?
    #
    process_in_tmp = i.get('process_in_tmp', meta.get('process_in_tmp', 'yes') ).lower() == 'yes'

    td=''
    if process_in_tmp:
       tdx=i.get('tmp_dir','')
       td=tdx
       if td=='': td='tmp'

       if i.get('clean','')=='yes':
          if td!='' and os.path.isdir(td):
#             cxx1=os.getcwd()
#             os.chdir(os.path.join(p,td))

#             cmd=cfg.get('clean_cmds',{}).get(hplat)

#             if o=='con':
#                ck.out(cmd)
#                ck.out('')

#             if ubtr!='': cmd=ubtr.replace('$#cmd#$',cmd)
#             rx=os.system(cmd)

#             os.chdir(cxx1)

             shutil.rmtree(td, ignore_errors=True)

       if tdx=='' and grtd=='yes':
          # Generate tmp dir
          import tempfile
          fd, fn=tempfile.mkstemp(suffix='', prefix='tmp-ck-')
          os.close(fd)
          os.remove(fn)
          td=os.path.basename(fn)

       cdir=os.path.join(p, td)

    misc['tmp_dir']=td
    misc['path']=p

    if cdir!='' and not os.path.isdir(cdir):
       time.sleep(1)
       try:
          os.makedirs(cdir)
       except Exception as e:
          pass
       if not os.path.isdir(cdir):
          return {'return':1, 'error':'can\'t create tmp directory ('+cdir+')'}

    sb='' # Batch

    # If extra paths
    if host_add_path_string!='' and (remote!='yes' or sa!='run'):
       sb+=host_add_path_string+'\n\n'

    if sa=='run' and target_add_path_string!='':
       sb+=target_add_path_string+'\n\n'

    if o=='con':
       ck.out(sep)
       ck.out('Current directory: '+cdir)

    try:
        odir=os.getcwd()
    except OSError:
        os.chdir('..')
        odir=os.getcwd()

    os.chdir(cdir)

    try:
        rcdir=os.getcwd()
    except OSError:
        os.chdir('..')
        rcdir=os.getcwd()

    # If run and dynamic or reuse compile deps, check deps prepared by compiler
    fdeps=cfg.get('deps_file','')
    if meta.get('skip_tmp_deps','')!='yes' and len(deps)==0 and sa=='run' and (rcd=='yes' or ctype=='dynamic'):
       if os.path.isfile(fdeps):
          if o=='con':
             ck.out('')
             ck.out('Reloading depedencies from compilation '+fdeps+' ...')

          rx=ck.load_json_file({'json_file':fdeps})
          if rx['return']>0: return rx
          deps=rx['dict']

    # If compile type is dynamic, reuse deps even for run (to find specific DLLs)
    # (REMOTE PLATFORMS ARE NOT SUPPORTED AT THE MOMENT, USE STATIC COMPILATION)
#    if (ctype=='dynamic' or sa=='compile' or rcd=='yes'):
       # Resolve deps (unless should be explicitly ignored, such as when installing local version with all dependencies set)

    if len(deps)==0:
       deps=meta.get('compile_deps',{})

    if len(deps)==0:
       deps=meta.get('deps',{})

    if remote=='yes' and sa=='run' and 'android' in tosd.get('tags',[]) and 'adb' not in deps:
       deps['adb']={
                    "force_target_as_host": "yes",
                    "local": "yes",
                    "name": "adb tool",
                    "sort": -10,
                    "tags": "tool,adb"
                   }

    if len(deps)>0:
       if o=='con':
          ck.out(sep)

       # Add extra compiler flags
       if ctags!='' and 'compiler' in deps:
          xctags=deps['compiler'].get('tags','')
          if xctags!='':
             xctags+=','
          xctags+=ctags
          deps['compiler']['tags']=xctags

       # Check user-friendly deps
       for q in preset_deps:
           if q in deps:
              deps[q]['uoa']=preset_deps[q]

       ii={'action':'resolve',
           'module_uoa':cfg['module_deps']['env'],
           'host_os':hos,
           'target_os':tos,
           'device_id':tdid,
           'deps':deps,
           'deps_cache':deps_cache,
           'reuse_deps':reuse_deps,
           'add_customize':'yes',
           'random':ran,
           'quiet':quiet,
           'install_to_env':iev,
           'dep_add_tags': dep_add_tags,
           'safe':safe}
       if o=='con': ii['out']='con'

       if meta.get('pass_env_to_resolve', '')=='yes':
           ii.update({ 'install_env': env })

       rx=ck.access(ii)
       if rx['return']>0: return rx

       if sa=='compile' or remote!='yes':
          sb+=no+rx['bat']

       deps=rx['deps'] # Update deps (add UOA)

    if sa=='compile':
       rx=ck.save_json_to_file({'json_file':fdeps, 'dict':deps})
       if rx['return']>0: return rx

    # If compiler, load env
    comp=deps.get('compiler',{})
    comp_uoa=comp.get('uoa','')
    dcomp={}

    if comp_uoa!='':
       rx=ck.access({'action':'load',
                     'module_uoa':cfg['module_deps']['env'],
                     'data_uoa':comp_uoa})
       if rx['return']>0: return rx
       dcomp=rx['dict']

    # Add energy monitor, if needed and if supported
    sspm1=tosd.get('script_start_power_monitor','')
    sspm2=tosd.get('script_stop_power_monitor','')

    if me=='yes' and sspm1!='':
       if o=='con':
          ck.out('')
          ck.out('Adding energy monitor')
          ck.out('')

       sb+='\n'
       sb+=scall+' '+sspm1+'\n'
       sb+='\n'

    ##################################################################################################################
    ################################### Compile ######################################
    if sa=='compile':
       # Clean target file
       if target_exe!='' and os.path.isfile(target_exe):
          os.remove(target_exe)

    if sa=='compile' or sa=='get_compiler_version':
       # Check if pre-process script
       x=meta.get('use_preprocess_compilation_scripts',{})
       if len(x)>0:
          xam=x.get('module_uoa','')
          if xam=='': xam=work['self_module_uid']
          xad=x.get('data_uoa','')
          r=ck.access({'action':'find',
                       'module_uoa':xam,
                       'data_uoa':xad})
          if r['return']>0: return r
          ppp1=r['path']

          # Check if has custom script
          cs=None
          csn=x.get('script_name','')
          if csn=='': csn='custom'

          rx=ck.load_module_from_path({'path':ppp1, 'module_code_name':csn, 'skip_init':'yes'})
          if rx['return']>0: return rx
          cs=rx['code']

          csf=x.get('script_func','')
          if csf=='': csf='setup'

          if csf not in dir(cs):
             return {'return':1, 'error':'function '+csf+' not found in script '+csn+' in path '+ppp1}

          # Call customized script
          ii={"host_os_uoa":hosx,
              "host_os_uid":hos,
              "host_os_dict":hosd,
              "target_os_uoa":tosx,
              "target_os_uid":tos,
              "target_os_dict":tosd,
              "target_device_id":tdid,
              "meta":meta,
              "env":env,
              "deps":deps,
              "self_cfg":cfg,
              "ck_kernel":ck
             }

          if o=='con': ii['interactive']='yes'
          if i.get('quiet','')=='yes': ii['interactive']=''

          script_func=getattr(cs, csf)
          rx=script_func(ii)
          if rx['return']>0: return rx

          # Update install env from customized script (if needed)
          new_env=rx.get('install_env',{})
          if len(new_env)>0:
             env.update(new_env)

       # Process compile vars
       compile_vars=meta.get('compile_vars',{})
       for q in compile_vars:
           if q not in env:
              x=compile_vars[q]
              try:
                 x=x.replace('$#src_path#$', src_path)
              except Exception as e: # need to detect if not string (not to crash)
                 pass
              env[q]=x

       # Update env from deps
#       for kkd in sorted(deps, key=lambda kk: deps[kk].get('sort',0)):
#           for kkd1 in deps[kkd].get('dict',{}).get('env',{}):
#               if kkd1 not in env:
#                  env[kkd1]=deps[kkd]['dict']['env'][kkd1]

       # Add compiler dep again, if there
       cb=deps.get('compiler',{}).get('bat','')
       if cb!='' and not sb.endswith(cb):
          sb+='\n'+no+cb.strip()+' 1\n' # We set 1 to tell environment that it should set again even if it was set before

#          for kkd1 in deps['compiler'].get('dict',{}).get('env',{}):
#              if kkd1 not in env:
#                 env[kkd1]=deps['compiler']['dict']['env'][kkd1]

       # Add other deps at the end if needed
       for q in deps:
           x=deps[q]
           if x.get('add_to_the_end_of_bat','')=='yes' and x.get('bat','')!='':
              y=x['bat']
              if not sb.endswith(y):
                 sb+='\n'+no+y.strip()+' 1\n' # We set 1 to tell environment that it should set again even if it was set before

       # Add env
       for k in sorted(env):
           v=str(env[k])
           v=v.replace('$<<',svarb).replace('>>$',svare)

           if eifs!='' and wb!='yes':
              if v.find(' ')>=0 and not v.startswith(eifs):
                 v=eifs+v+eifs

           sb+=no+eset+' '+k+'='+str(v)+'\n'

       sb+='\n'

       # Try to detect version
       csd=deps.get('compiler',{}).get('dict',{})
       csuoa=csd.get('soft_uoa','')
       fp=csd.get('customize',{}).get('full_path','')
       uloc=csd.get('customize',{}).get('use_locale_for_version','')

       cver=''
       if csuoa!='':
          r=ck.access({'action':'internal_detect',
                       'module_uoa':cfg['module_deps']['soft'],
                       'tool':fp,
                       'uoa':csuoa,
                       'env':cb,
                       'use_locale':uloc,
                       'con':o})
          if r['return']==0:
             cver=r['version_str']
             misc['compiler_detected_ver_list']=r['version_lst']
             misc['compiler_detected_ver_str']=cver
             misc['compiler_detected_ver_raw']=r['version_raw']

             if o=='con':
                ck.out(sep)
                ck.out('Detected compiler version: '+cver)
                ck.out('')

       if sa=='compile':
          # Check linking libs + include paths for all deps
          sll=''
          sin=''
          for k in sorted(deps, key=lambda kk: deps[kk].get('sort',0)):
              depsk=deps[k]
              kv=depsk.get('cus',{})

              # Process include
              pl3l=kv.get('path_include','')
              pl3ll=kv.get('path_includes',[])
              if pl3l not in pl3ll:
                 pl3ll.append(pl3l)

              for pl3 in pl3ll:
                  if pl3!='':
                     if pl3.endswith('\\'): pl3=pl3[:-1] # otherwise can be problems on Windows ...
                     if sin!='': sin+=' '
                     sin+=svarb+svarb1+'CK_FLAG_PREFIX_INCLUDE'+svare1+svare+eifsc+pl3+eifsc

              # Process lib (if not skipped)
              if depsk.get('skip_linking','')=='yes':
                 continue

              pl1=kv.get('path_lib','')
              if pl1=='': pl1=kv.get('path_static_lib','')
              pl1d=kv.get('path_dynamic_lib','')
              if pl1d=='': pl1d=pl1

              # Check if extra
              extra_libs=depsk.get('extra_libs',[])
              els=[]

              cus_extra_libs=kv.get('extra_static_libs',{})
              if len(cus_extra_libs)==0: cus_extra_libs=kv.get('extra_dynamic_libs',{})

              for el in extra_libs:
                  x=cus_extra_libs.get(el,'')
                  if x=='':
                     return {'return':1, 'error':'library '+el+'is not defined in dependencies'}
                  els.append(x)

              x=kv.get('static_lib','')
              if x=='' and ctype=='dynamic' and kv.get('dynamic_lib','')!='': x=kv['dynamic_lib']
              els.append(x)

              # Check if force to add library path (-L)
              path_added=False
              if tplat!='win' and depsk.get('force_add_static_lib_path','')=='yes':
                  sll+=' '+svarb+svarb1+'CK_FLAG_PREFIX_LIB_DIR'+svare1+svare+eifsc+pl1d+eifsc
                  path_added=True

              for pl2 in els:
                  if pl2!='':
                     if sll!='': sll+=' '
                     if ctype=='dynamic' and wb!='yes' and (remote=='yes' or pl1d!='') and csd.get('customize',{}).get('can_strip_dynamic_lib','')=='yes':
                        pl2x=os.path.splitext(pl2)[0]
                        if pl2x.startswith('lib'): pl2x=pl2x[3:]
                        if not path_added:
                           if pl1d.endswith('\\'): pl1d=pl1d[:-1] # otherwise can be problems on Windows ...
                           sll+=' '+svarb+svarb1+'CK_FLAG_PREFIX_LIB_DIR'+svare1+svare+eifsc+pl1d+eifsc
                           path_added=True
                        sll+=' -l'+pl2x
                     else:
                        sll+=eifsc
                        if pl1!='':
                           sll+=pl1+sdirs
                        sll+=pl2
                        sll+=eifsc

              evr=depsk.get('extra_ld_vars','')
              if evr!='':
                 evr=evr.replace('$<<',svarb).replace('>>$',svare)
                 sll+=' '+evr

          # Check if local includes
          linc=meta.get('include_dirs',[])
          if len(linc)>0:
             for q in linc:
                 # Check if source from another entry (species)
                 full_path=''

                 if q.startswith('$#ck_take_from_{'):
                    r9=substitute_some_ck_keys({'string':q})
                    if r9['return']>0: return r9
                    x=r9['string']
                 else:
                    if td!='': full_path='..'+sdirs
                    else: full_path=''
                    x=os.path.join(full_path,q)

                 if x.endswith('\\'): x=x[:-1] # otherwise can be problems on Windows ...

                 if sin!='': sin+=' '
                 sin+=svarb+svarb1+'CK_FLAG_PREFIX_INCLUDE'+svare1+svare+eifsc+x+eifsc

          # Check if includes as environment var (we search in env settings,
          #    not in real env, otherwise, can have problems, when concatenating -I with empty string)
          line=meta.get('compiler_add_include_as_env_from_deps',[])
          xline=[]

          for qq in line:
              if qq.find('$<<')<0 and qq.find('>>$')<0:
                 qq='$<<'+qq+'>>$'

              jq1=qq.find('$<<')
              while jq1>=0:
                 jq2=qq.find('>>$')
                 if jq2>0:
                    q=qq[jq1+3:jq2]

                    qx=''
                    for g1 in deps:
                        gg=deps[g1]
                        gge=gg.get('dict',{}).get('env',{})
                        xgge=gge.get(q,'')
                        if xgge!='':
                           qx=xgge
                           break

                    qq=qq[:jq1]+qx+qq[jq2+3:]
                    jq1=qq.find('$<<')

                 else:
                    return {'return':1, 'error':'inconsistency in "compiler_add_include_as_env_from_deps" key in program meta'}

              xline.append(qq)

          for xgge in xline:
              if xgge!='':
                 if xgge.endswith('\\'): xgge=xgge[:-1] # otherwise can be problems on Windows ...
                 if sin!='': sin+=' '
                 sin+=svarb+svarb1+'CK_FLAG_PREFIX_INCLUDE'+svare1+svare+eifsc+xgge+eifsc

          # Obtaining compile CMD (first from program entry, then default from this module)
          ccmds=meta.get('compile_cmds',{})
          ccmd=ccmds.get(hplat,{})
          if len(ccmd)==0:
             ccmd=ccmds.get('default',{})
          if len(ccmd)==0:
             ccmds=cfg.get('compile_cmds',{})
             ccmd=ccmds.get(hplat,{})
             if len(ccmd)==0:
                ccmd=ccmds.get('default',{})

          sccmd=ccmd.get('cmd','')
          if sccmd=='':
             return {'return':1, 'error':'compile CMD is not found'}

          sccmd=sccmd.replace('$#script_ext#$',sext)
          sccmd=sccmd.replace('$#dir_sep#$',stdirs)

          sccmd=sccmd.replace('$<<',svarb).replace('>>$',svare)

          # Source files
          sfs=meta.get('source_files',[])

          compiler_env=''
          if hplat=='win':
             compiler_env=meta.get('compiler_env_win','')
          if compiler_env=='':
             compiler_env=meta.get('compiler_env','')
          if compiler_env=='': 
             compiler_env='CK_CC'

          sfprefix='..'+sdirs

          scfb=''

          flags_def=''
          if fspeed=='yes':
               scfb+=' '+svarb+'CK_OPT_SPEED'+svare+' '
               flags_def+=' '+svarb+'CK_OPT_SPEED'+svare+' '
          elif fsize=='yes':
               flags_def+=' '+svarb+'CK_OPT_SIZE'+svare+' '

          scfb+=svarb+'CK_FLAGS_CREATE_OBJ'+svare
          scfb+=' '+svarb+'CK_COMPILER_FLAGS_OBLIGATORY'+svare
          if ctype=='dynamic':
             scfb+=' '+svarb+'CK_FLAGS_DYNAMIC_BIN'+svare
          elif ctype=='static':
             scfb+=' '+svarb+'CK_FLAGS_STATIC_BIN'+svare
          if meta.get('skip_local_include','')!='yes':
             scfb+=' '+svarb+svarb1+'CK_FLAG_PREFIX_INCLUDE'+svare1+svare+sfprefix

          scfa=''

          # Check build -D flags
          sbcv=''
          bcv={}

          if ncv!='yes':
             bcv=meta.get('build_compiler_vars',{})

             for q in rcv:
                 if q in bcv: del(bcv[q])

          bcv.update(cv)

          bcv['CK_HOST_OS_NAME_'+hosd.get('ck_name','').upper()]='1'
          bcv['CK_HOST_OS_NAME2_'+hosd.get('ck_name2','').upper()]='1'
          bcv['CK_TARGET_OS_NAME_'+tosd.get('ck_name','').upper()]='1'
          bcv['CK_TARGET_OS_NAME2_'+tosd.get('ck_name2','').upper()]='1'

          # Update env if energy meter
          if me=='yes':
             bcv['CK_MONITOR_ENERGY']='1'

          if o=='con' and len(bcv)>0:
             ck.out(sep)
             ck.out('Compiler vars:')

          if meta.get('skip_compiler_vars','')!='yes':
             for k in sorted(bcv):
                 kv=bcv[k]

                 if sbcv!='': sbcv+=' '
                 sbcv+=svarb+svarb1+'CK_FLAG_PREFIX_VAR'+svare1+svare+k
                 if kv!='': sbcv+='='+str(kv)

                 if o=='con':
                    ck.out('  '+k+'='+str(kv))

          # Check if compiler flags as environment variable
          cfev=''
          if hplat=='win':
             cfev=meta.get('compiler_flags_as_env_win','')
          if cfev=='':
             cfev=meta.get('compiler_flags_as_env','')
          if cfev!='':
             cfev=cfev.replace('$<<',svarb).replace('>>$',svare)
             sbcv+=' '+cfev

          # Check if has customization scripts
          scus=os.path.join(cdir,'..','customize'+sext)
          if os.path.isfile(scus):
             sb+='\n'+scall+' '+scus+'\n\n'

          # Prepare compilation
          sb+='\n'

          denv=dcomp.get('env',{})
          sobje=denv.get('CK_OBJ_EXT','')
          sofs=''
          xsofs=[]

          if ee!='':
             sb+='\n'+no+ee+'\n\n'

          if o=='con': ck.out(sep)

          # Compilation flags
          xcfb=scfb

          if sbcv!='': xcfb+=' '+sbcv
          if sin!='': xcfb+=' '+sin

          if uco:
             xcfb+=' -emit-llvm'
          else:
             xcfb+=' '+flags

          # Linking flags
          slfb=svarb+'CK_COMPILER_FLAGS_OBLIGATORY'+svare
          slfb+=' '+lflags
          if ctype=='dynamic':
             slfb+=' '+svarb+'CK_FLAGS_DYNAMIC_BIN'+svare
          elif ctype=='static':
             slfb+=' '+svarb+'CK_FLAGS_STATIC_BIN'+svare

          slfa=''
          if target_exe!='':
             slfa=' '+svarb+svarb1+'CK_FLAGS_OUTPUT'+svare1+svare+target_exe
          slfa+=' '+svarb+'CK_LD_FLAGS_MISC'+svare
          slfa+=' '+svarb+'CK_LD_FLAGS_EXTRA'+svare

          evrf=meta.get('extra_ld_vars_first','')
          if evrf!='':
             evrf=evrf.replace('$<<',svarb).replace('>>$',svare)
             slfa+=' '+evrf

          if sll!='': slfa+=' '+sll

          evr=''
          if hplat=='win':
             evr=meta.get('extra_ld_vars_win','')
          if evr=='':
             evr=meta.get('extra_ld_vars','')
          if evr!='':
             evr=evr.replace('$<<',svarb).replace('>>$',svare)
             slfa+=' '+evr

          # Check if includes as environment var
          llinkle=meta.get('linker_add_lib_as_env',[])
          if len(llinkle)>0:
             for q in llinkle:
                 if slfa!='': slfa+=' '
                 slfa+=svarb+svarb1+q+svare1+svare

          # Check if call compile CMD only once with all files
          if meta.get('use_compile_script','')=='yes':
             cc=sccmd

             # Add compiler and linker flags as environment
             sb+='\n'
             genv={'CK_PROG_COMPILER_FLAGS_BEFORE':xcfb,
                   'CK_PROG_LINKER_FLAGS_BEFORE':slfb,
                   'CK_PROG_LINKER_FLAGS_AFTER':slfa,
                   'CK_PROG_COMPILER_VARS':sbcv,
                   'CK_PROG_COMPILER_FLAGS':flags_def+' '+flags,
                   'CK_PROG_LINKER_LIBS':sll,
                   'CK_PROG_TARGET_EXE':target_exe}

             extcomp=meta.get('extra_env_for_compilation',{})
             if len(extcomp)>0:
                genv.update(extcomp)

             if len(eefc)>0:
                genv.update(eefc)

             for gg in genv:
                 gx=genv[gg]
                 if eifs!='': gx=gx.replace(eifs, '\\'+eifs)
                 sb+=no+eset+' '+gg+'='+eifs+gx+eifs+'\n'

             sb+='echo '+eifs+cc+eifs+'\n'
             sb+=no+cc+'\n'
             sb+=no+sqie+'\n'

             sb+='\n'
          else:
             for sf in sfs:
                 sf=sf.strip()

                 xcfa=scfa

                 # Check if source from another entry (species)
                 full_path=''
                 if sf.startswith('$<<'):
                    full_path=sf.replace('$<<',svarb).replace('>>$',svare)

                 elif sf.startswith('$#ck_take_from_{'):
                    b2=sf.find('}#$')
                    if b2=='':
                       return {'return':1, 'error':'can\'t parse source file '+sf+' ...'}
                    bb=sf[16:b2]

                    rb=ck.access({'action':'load',
                                  'module_uoa':muoa,
                                  'data_uoa':bb})
                    if rb['return']>0:
                       return {'return':1, 'error':'can\'t find sub-entry '+bb}

                    sf=sf[b2+3:]

                    full_path=os.path.join(rb['path'],sf)

                 else:
                    full_path=os.path.join(sfprefix,sf)

                 sf0,sf1=os.path.splitext(sf)

                 sf00=os.path.basename(sf)
                 sf00a,sf00b=os.path.splitext(sf00)

                 if uco:
                    sfobj=sf00a+'.bc'
                 else:
                    sfobj=sf00a+sobje
                 if sofs!='': sofs+=' '
                 sofs+=sfobj
                 xsofs.append(sfobj)

                 if 'CK_FLAGS_OUTPUT' in denv:
                    xcfa+=' '+svarb+svarb1+'CK_FLAGS_OUTPUT'+svare1+svare+sfobj

                 cc=sccmd
                 cc=cc.replace('$#source_file#$', full_path)

                 cc=cc.replace('$#compiler#$', svarb+compiler_env+svare)

                 cc=cc.replace('$#flags_before#$', xcfb)
                 cc=cc.replace('$#flags_after#$', xcfa)

                 if sunparsed!='': cc+=' '+sunparsed

                 sb+='echo '+eifs+cc+eifs+'\n'
                 sb+=no+cc+'\n'
                 sb+=no+sqie+'\n'

                 sb+='\n'

                 # Check if clang opt
                 if uco:
                    for clang_opt_flag in split_flags:
                        sb+='\necho "\nopt '+clang_opt_flag+' -o '+sfobj+' '+sfobj+'"\n'
                        sb+='opt '+clang_opt_flag+' -o '+sfobj+' '+sfobj+'\n'

          # Convert Clang BC to .o
          if uco:
             sb+='\necho "\nllc -filetype=obj '+sfobj+'"\n'
             sb+='llc -filetype=obj '+sfobj+'\n\n'

          # Obtaining link CMD (first from program entry, then default from this module)
          if sofs!='':
             linker_env=meta.get('linker_env','')
             if linker_env=='': linker_env=compiler_env

             lcmds=meta.get('link_cmds',{})
             lcmd=lcmds.get(hplat,{})
             if len(lcmd)==0:
                lcmd=lcmds.get('default',{})
             if len(lcmd)==0:
                lcmds=cfg.get('link_cmds',{})
                lcmd=lcmds.get(hplat,{})
                if len(lcmd)==0:
                   lcmd=lcmds.get('default',{})

             slcmd=lcmd.get('cmd','')
             if slcmd!='':
                slfb=svarb+'CK_COMPILER_FLAGS_OBLIGATORY'+svare
                slfb+=' '+lflags
                if ctype=='dynamic':
                   slfb+=' '+svarb+'CK_FLAGS_DYNAMIC_BIN'+svare
                elif ctype=='static':
                   slfb+=' '+svarb+'CK_FLAGS_STATIC_BIN'+svare

                slfa=''
                if target_exe!='':
                   slfa=' '+svarb+svarb1+'CK_FLAGS_OUTPUT'+svare1+svare+target_exe
                slfa+=' '+svarb+'CK_LD_FLAGS_MISC'+svare
                slfa+=' '+svarb+'CK_LD_FLAGS_EXTRA'+svare

                evrf=meta.get('extra_ld_vars_first','')
                if evrf!='':
                   evrf=evrf.replace('$<<',svarb).replace('>>$',svare)
                   slfa+=' '+evrf

                if sll!='': slfa+=' '+sll

                evr=''
                if hplat=='win':
                   evr=meta.get('extra_ld_vars_win','')
                if evr=='':
                   evr=meta.get('extra_ld_vars','')
                if evr!='':
                   evr=evr.replace('$<<',svarb).replace('>>$',svare)
                   slfa+=' '+evr

                # Check if includes as environment var
                llinkle=meta.get('linker_add_lib_as_env',[])
                if len(llinkle)>0:
                   for q in llinkle:
                       if slfa!='': slfa+=' '
                       slfa+=svarb+svarb1+q+svare1+svare

                cc=slcmd
                cc=cc.replace('$#linker#$', svarb+linker_env+svare)
                cc=cc.replace('$#obj_files#$', sofs)
                cc=cc.replace('$#flags_before#$', slfb)
                cc=cc.replace('$#flags_after#$', slfa)

                sb+='echo '+eifs+cc+eifs+'\n'
                sb+=no+cc+'\n'
                sb+=no+sqie+'\n'

          # Add objdump
          if target_exe!='':
             if meta.get('skip_objdump','')!='yes':
                sb+='\n'+no+svarb+'CK_OBJDUMP'+svare+' '+target_exe+' '+stro+' '+target_exe+'.dump'+'\n'

             # Add md5sum
             if meta.get('skip_md5sum','')!='yes':
                x='<'
#                if hplat=='win':x=''
                sb+='\n'+no+md5sum+' '+x+' '+target_exe+'.dump '+stro+' '+target_exe+'.md5'+'\n'

             # Add git hash (if supported)
             xnull='/dev/null'
             if hplat=='win': xnull='null'
             sb+='\n'+no+'git rev-parse HEAD '+stro+' '+target_exe+'.git_hash'+' '+stre+xnull+'\n'

          # Stop energy monitor, if needed and if supported
          if me=='yes' and sspm2!='':
             if o=='con':
                ck.out('')
                ck.out('Adding energy monitor')
                ck.out('')

             sb+='\n'
             sb+=scall+' '+sspm2+'\n'
             sb+='\n'

          # Add exit /0 if needed (on Windows git and md5sum can mess up return code)
          if bex!='':
             sb+='\n\n'+bex.replace('$#return_code#$','0')

          # Record to tmp batch and run
          rx=ck.gen_tmp_file({'prefix':'tmp-', 'suffix':sext, 'remove_dir':'yes'})
          if rx['return']>0: return rx
          fn=rx['file_name']

          rx=ck.save_text_file({'text_file':fn, 'string':sb})
          if rx['return']>0: return rx

          y=''
          if sexe!='':
             y+=sexe+' '+sbp+fn+envsep
          y+=' '+scall+' '+sbp+fn

          if o=='con':
             ck.out('')
             ck.out('Executing prepared batch file '+fn+' ...')
             ck.out('')

          sys.stdout.flush()
          start_time1=time.time()

          if ubtr!='': y=ubtr.replace('$#cmd#$',y)

          ############################################## Compiling code here ##############################################
          rx=0
          ry=ck.system_with_timeout({'cmd':y, 'timeout':xcto})
          rry=ry['return']

          if rry>0:
             if rry!=8: return ry
          else:
             rx=ry['return_code']

          comp_time=time.time()-start_time1
          ccc['compilation_time']=comp_time

          if sca!='yes':
             if fn!='' and os.path.isfile(fn): os.remove(fn)

          git_hash=''
          # Try to read git hush file
          if os.path.isfile(target_exe+'.git_hash'):
             rz=ck.load_text_file({'text_file':target_exe+'.git_hash'})
             if rz['return']==0:
                git_hash=rz['string'].strip()
                ccc['program_git_hash']=git_hash

          ofs=0
          tbs=0
          md5=''
          if rry==8:
             misc['compilation_success']='no'
             misc['compilation_success_bool']=False
             misc['fail_reason']=ry['error']

             ccc['compilation_success']='no'
             ccc['compilation_success_bool']=False
             ccc['fail_reason']=ry['error']
          elif rx>0:
             misc['compilation_success']='no'
             misc['compilation_success_bool']=False
             misc['fail_reason']='return code '+str(rx)+' !=0 '

             ccc['compilation_success']='no'
             ccc['compilation_success_bool']=False
             ccc['fail_reason']='return code '+str(rx)+' !=0 '
          else:
             misc['compilation_success']='yes'
             misc['compilation_success_bool']=True
             ccc['compilation_success']='yes'
             ccc['compilation_success_bool']=True

             # Check some characteristics
             if os.path.isfile(target_exe):
                ccc['binary_size']=os.path.getsize(target_exe)
                ofs=ccc['binary_size']
                tbs=ofs

                # Try to read md5 file
                if os.path.isfile(target_exe+'.md5'):
                   rz=ck.load_text_file({'text_file':target_exe+'.md5'})
                   if rz['return']==0:
                      md5x=rz['string']
                      ix=md5x.find(' ')
                      if ix>0:
                         md5=md5x[:ix].strip()
                         ccc['md5_sum']=md5

             # Check obj file sizes
             if len(xsofs)>0:
                ofs=0
                ccc['obj_sizes']={}
                for q in xsofs:
                    if os.path.isfile(q):
                       ofs1=os.path.getsize(q)
                       ccc['obj_sizes'][q]=ofs1
                       ofs+=ofs1
                ccc['obj_size']=ofs

          ccc['compilation_time_with_module']=time.time()-start_time

          if o=='con':
             s=''
             if meta.get('no_compile','')=='yes':
                s='Warning: This program doesn\'t require compilation ...'
             else:
                s='Compilation time: '+('%.3f'%comp_time)+' sec.'

                if meta.get('no_target_file','')!='yes':
                   s+='; Object size: '+str(ofs)+'; Total binary size: '+str(tbs)+'; MD5: '+md5

             ck.out(sep)
             ck.out(s)
             if misc.get('compilation_success','')=='no':
                ck.out('')
                ck.out('Warning: compilation failed!')

    ##################################################################################################################
    ################################### Run ######################################
    elif sa=='run':
       start_time=time.time()

       # Remote dir
       if remote=='yes':
          rdir=tosd.get('remote_dir','')
          if rdir!='' and not rdir.endswith(stdirs): rdir+=stdirs
          if td!='': rdir+=td
          if rdir!='' and not rdir.endswith(stdirs): rdir+=stdirs

       src_path_local=p+sdirs
       if remote=='yes' and remote_ssh!='yes':
          src_path=rdir
       else:
          src_path=src_path_local

       sc=i.get('skip_calibration','')
       xcalibrate_time=i.get('calibration_time','')
       if xcalibrate_time=='': xcalibrate_time=cfg['calibration_time']
       calibrate_time=float(xcalibrate_time)


       # Figure out the "active" cmd key
       run_cmds=meta.get('run_cmds',{})
       if len(run_cmds)==0:
          return {'return':1, 'error':'no CMD for run'}

       kcmd=i.get('cmd_key','')
       krun_cmds=sorted(list(run_cmds.keys()))
       if kcmd=='':
          if len(krun_cmds)>1:
             zz={}
             iz=0
             for z in sorted(run_cmds, key=lambda rcmds:run_cmds[rcmds].get('sort',0)):
                 add=True

                 # Check if skip by deps tags
                 skp=run_cmds[z].get('skip_if_deps_tags',[])

                 for sk in skp:
                     if len(sk)>0:
                        for skx in deps:
                            sktags=deps[skx].get('dict',{}).get('tags',[])
                            found=True
                            for skt in sk:
                                if skt not in sktags:
                                   found=False
                                   break
                            if found:
                               add=False
                               break

                        if not add:
                           break

                 if add:
                    # Check if add only by deps tags
                    aif=run_cmds[z].get('add_only_if_deps_tags',[])

                    if len(aif)>0:
                       add=False
                       for sk in aif:
                           if len(sk)>0:
                              for skx in deps:
                                  sktags=deps[skx].get('dict',{}).get('tags',[])
                                  found=True
                                  for skt in sk:
                                      if skt not in sktags:
                                         found=False
                                         break
                                  if found:
                                     add=True
                                     break

                              if add:
                                 break

                 if add:
                    zz[str(iz)]=z
                    iz+=1

             if len(zz)>0:
                if len(zz)==1:
                   x='0'
                else:
                   ck.out('')
                   ck.out('More than one commmand line is found to run this program:')
                   ck.out('')

                   for iz in range(0, len(zz)):
                       zs=str(iz)
                       z=zz[zs]
                       zcmd=run_cmds[z].get('run_time',{}).get('run_cmd_main','')

                       if zcmd!='': z+=' ('+zcmd+')'
                       ck.out(zs+') '+z)

                   ck.out('')
                   rx=ck.inp({'text':'Select command line (or Enter to select 0): '})
                   x=rx['string'].strip()
                   if x=='': x='0'

                   if x not in zz:
                      return {'return':1, 'error':'command line number is not recognized'}

                kcmd=zz[x]
             else:
                return {'return':1, 'error':'no CMD for run for these software dependencies'}

          else:
             kcmd=krun_cmds[0]
       else:
          if kcmd not in krun_cmds:
             return {'return':1, 'error':'CMD key not found in program description'}

       # Command line key is set
       vcmd=run_cmds[kcmd]
       misc['cmd_key']=kcmd


       # Update environment with defaults (run_vars are runtime environment defaults)

       run_vars = meta.get('run_vars',{}).copy()        # first load ground-level-precedence defaults for all commands
       run_vars.update( vcmd.get('run_vars',{}) )       # then override with higher-precedence defaults for this specific command

       for q in run_vars:
           if q not in env:
              x=run_vars[q]
              try:
                 x=x.replace('$#src_path#$', src_path)
              except Exception as e: # need to detect if not string (not to crash)
                 pass
              env[q]=x

       # Update env if repeat
       if sc!='yes' and 'CT_REPEAT_MAIN' in run_vars:
          if repeat!=-1:
             if 'CT_REPEAT_MAIN' not in run_vars:
                return {'return':1, 'error':'this program is not supporting execution time calibration'}
             env['CT_REPEAT_MAIN']=str(repeat) # it is fixed by user
             sc='yes'
          else:
             repeat=int(run_vars.get('CT_REPEAT_MAIN','1'))
             env['CT_REPEAT_MAIN']='$#repeat#$' # find later

       # Update env if energy meter
       if me=='yes':
          env['CK_MONITOR_ENERGY']='1'
          env['XOPENME_FILES']=svarb+svarb1+'CK_ENERGY_FILES'+svare1+svare


       # Check run-time deps
       rx=update_run_time_deps({'host_os':hos,
                                'target_os':tos,
                                'target_id':tdid,
                                'deps':deps,
                                'deps_cache':deps_cache,
                                'reuse_deps':reuse_deps,
                                'meta':meta,
                                'cmd_key':kcmd,
                                'cmd_meta':vcmd,
                                'out':oo,
                                'install_to_env':iev,
                                'env_for_resolve':env,
                                'dep_add_tags':dep_add_tags,
                                'preset_deps':preset_deps,
                                'random':ran,
                                'safe':safe,
                                'quiet':quiet})
       if rx['return']>0: return rx

       # Record deps if needed
       if record_deps!='':
          r9=ck.save_json_to_file({'json_file':record_deps, 'dict':deps})
          if r9['return']>0: return r9

       aenv=rx.get('aggregated_env',{})

       if rx.get('resolve',{}).get('bat','')!='':
          if remote!='yes':
             sb+=no+rx['resolve']['bat']

       ##################################################
       c=''

       rt=vcmd.get('run_time',{})

       rif=rt.get('run_input_files',[])
       treat_input_file_path_as_absolute={}

       # Check if dynamic and remote to copy .so to devices (but for the 1st autotuning and statistical iteration!)
       #  unless explicitly forbidden (such as libOpenCL ...)
       if ctype=='dynamic' and remote=='yes':
          if srn==0 and ati==0:
             for q in deps:
                 qq=deps[q].get('cus',{})
                 qdl=qq.get('dynamic_lib','')

                 if qq.get('skip_copy_to_remote','')!='yes':
                     if qdl!='':
                         qpl=qq.get('path_lib','')
                         qq1=os.path.join(qpl,qdl)
                         if os.path.isfile(qq1) and not qq1.endswith('.a'):
                            rif.append(qq1)
                            treat_input_file_path_as_absolute[qq1]='yes' # if pushing to external, do not use current path

                     aef=qq.get('adb_extra_files',[])
                     for qq1 in aef:
                         rif.append(qq1)
                         treat_input_file_path_as_absolute[qq1]='yes' # if pushing to external, do not use current path

       # Check if run_time env is also defined
       rte=rt.get('run_set_env2',{})
       if len(rte)>0:
          env.update(rte)

       # Check GPGPU
       compute_platform_id=i.get('compute_platform_id','')
       compute_device_id=i.get('compute_device_id','')

       # Check if need to select GPGPU
       ngd=rt.get('need_compute_device','')
       if ngd!='':
           if o=='con':
              ck.out(sep)
              ck.out('Detecting GPGPU targets ...')
              ck.out('')

           ii={'action':'detect',
                        'module_uoa':cfg['module_deps']['platform.gpgpu'],
                        'host_os':hos,
                        'target_os':tos,
                        'device_id':tdid,
                        'compute_platform_id':compute_platform_id,
                        'compute_device_id':compute_device_id,
                        'type':ngd,
#                        'deps':xdeps,
                        'select':'yes',
                        'sudo':isd,
                        'out':oo,
                        'quiet':quiet}
           target=i.get('target','')
           if target!='': ii['target']=target
           r=ck.access(ii)
           if r['return']>0: return r

           compute_platform_id=r.get('choices',{}).get('compute_platform_id','')
           compute_device_id=r.get('choices',{}).get('compute_device_id','')

           if 'add_to_features' not in misc: misc['add_to_features']={}
           misc['add_to_features']['gpgpu']=r.get('features',{}).get('gpgpu',{})

           if 'add_to_choices' not in misc: misc['add_to_choices']={}
           misc['add_to_choices']['compute_platform_id']=compute_platform_id
           misc['add_to_choices']['compute_device_id']=compute_device_id

       # Finish GPGPU selection, if needed
       if compute_platform_id!='':
           env['CK_COMPUTE_PLATFORM_ID']=compute_platform_id
       if compute_device_id!='':
           env['CK_COMPUTE_DEVICE_ID']=compute_device_id

       # Check APK
       apk=meta.get('apk',{})
       if len(apk)>0:
           if o=='con':
               ck.out(sep)
               ck.out('Detecting/installing required APK ...')
               ck.out('')

           ix={'action':'install',
               'module_uoa':cfg['module_deps']['apk'],
               'host_os':hos,
               'target_os':tos,
               'device_id':tdid,
               'out':oo}

           ix.update(apk)

           r=ck.access(ix)
           if r['return']>0:
               if r['return']==16:
                   misc['run_success']='no'
                   misc['run_success_bool']=False
                   misc['fail_reason']=r['error']

                   return {'return':0, 'tmp_dir':rcdir, 'misc':misc, 'characteristics':ccc, 'deps':deps}

               return r

           if 'add_to_features' not in misc: misc['add_to_features']={}
           misc['add_to_features']['apk']=r.get('params',{})

       # Update env from deps
#       for kkd in sorted(deps, key=lambda kk: deps[kk].get('sort',0)):
#           for kkd1 in deps[kkd].get('dict',{}).get('env',{}):
#               if kkd1 not in env:
#                  env[kkd1]=deps[kkd]['dict']['env'][kkd1]

       # Check specialized env by OS from deps
       for k in deps:
           xenv=deps[k].get('cus',{}).get('env_by_os',{}).get(tplat2,{})
           if len(xenv)>0:
              for k1 in xenv:
                  if env.get(k1,'')=='':
                     env[k1]=xenv[k1]

       # Add compiler dep again, if there (otherwise some libs can set another compiler)
       x=deps.get('compiler',{}).get('bat','')
       if remote!='yes' and x!='' and not sb.endswith(x):
          sb+='\n'+no+x.strip()+' 1\n' # We set 1 to tell environment that it should set again even if it was set before

#          for kkd1 in deps['compiler'].get('dict',{}).get('env',{}):
#              if kkd1 not in env:
#                 env[kkd1]=deps['compiler']['dict']['env'][kkd1]

       # Check if need to remove some env before run (useful for remote devices)
       for k in meta.get('remove_env_before_run',[]):
           if k in env:
              del(env[k])

       # Command line preparation
       c=rt.get('run_cmd_main','')
       if remote=='yes' and rt.get('run_cmd_main_remote','')!='':
          c=rt['run_cmd_main_remote']
       if drcmd!='':
          c=drcmd

       if c=='':
          return {'return':1, 'error':'cmd is not defined'}
       if remote=='yes':
          c=c.replace('$<<','${').replace('>>$','}')
       else:
          c=c.replace('$<<',svarb+svarb1).replace('>>$',svare1+svare)

       c=c.replace('$#script_ext#$',sext)
       c=c.replace('$#dir_sep#$',stdirs)

       up_dir=''
       if remote!='yes': up_dir='../'

       c=c.replace('$#up_dir#$',up_dir)

       # Add extra before CMD if there ...
       c=prcmd+' '+c

       # Replace bin file
       te=target_exe
       if meta.get('skip_add_prefix_for_target_file','')!='yes':
          te=stbp+te

       # Check if affinity
       if aff!='':
          te=aff+' '+te

       c=c.replace('$#BIN_FILE#$', te)
       c=c.replace('$#os_dir_separator#$', stdirs)

       x=''
       if remote_ssh!='yes':
          x='..'+stdirs
       c=c.replace('$#previous_dir#$', x)

       c=c.replace('$#src_path#$', src_path)

       c=c.replace('$#env1#$',svarb)
       c=c.replace('$#env2#$',svare)

       # Update keys in run cmd (useful for CMD autotuning)
       for k in rcsub:
           xv=rcsub[k]
           c=c.replace('$#'+k+'#$',str(xv))

       # Check if takes datasets from CK
       dtags=vcmd.get('dataset_tags',[])

       # Check if need to add dataset file as JSON to run_vars
       adfe=vcmd.get('add_dataset_file_to_env','')

       edtags=i.get('extra_dataset_tags', [])
       if len(dtags)>0 and len(edtags)>0:
          dtags += edtags

       dmuoa=cfg['module_deps']['dataset']
       dduoa=i.get('dataset_uoa','')
       dfile=''
       dfile_keys=[]
       if dduoa!='' or len(dtags)>0:
          if dduoa=='':
             misc['dataset_tags']=dtags

             dtags_csv = ','.join(dtags)

             rx=ck.access({'action':'search',
                           'module_uoa':dmuoa,
                           'tags':dtags_csv,
                           'add_info':'yes'})
             if rx['return']>0: return rx

             lst=rx['lst']

             if len(lst)==0:
                return {'return':1, 'error':'no related datasets found (tags='+dtags_csv+')'}
             elif len(lst)==1:
                dduoa=lst[0].get('data_uid','')
             else:
                ck.out('')
                ck.out('More than one dataset entry is found for this program:')
                ck.out('')

#                zz={}
#                iz=0
#                for z1 in sorted(lst, key=lambda v: v['data_uoa']):
#                    z=z1['data_uid']
#                    zu=z1['data_uoa']
#
#                    zs=str(iz)
#                    zz[zs]=z
#
#                    ck.out(zs+') '+zu+' ('+z+')')
#
#                    iz+=1
#
#                ck.out('')
#                rx=ck.inp({'text':'Select dataset UOA (or Enter to select 0): '})
#                x=rx['string'].strip()
#                if x=='': x='0'
#
#                if x not in zz:
#                   return {'return':1, 'error':'dataset number is not recognized'}
#
#                dduoa=zz[x]

                r=ck.access({'action':'select_uoa',
                             'module_uoa':cfg['module_deps']['choice'],
                             'choices':lst})
                if r['return']>0: return r
                dduoa=r['choice']
                ck.out('')

          if dduoa=='':
             return {'return':1, 'error':'dataset is not specified'}

       misc['dataset_uoa']=dduoa

       # If remote, init
       if remote=='yes':
          rs=tosd['remote_shell'].replace('$#device#$',xtdid)
          rse=tosd.get('remote_shell_end','')+' '

          if sdi!='yes':
             ck.out(sep)
             r=ck.access({'action':'init_device',
                          'module_uoa':cfg['module_deps']['platform'],
                          'os_dict':tosd,
                          'device_id':tdid,
                          'out':oo})
             if r['return']>0: return r

          # Try to create directories
          x=rs+' '+tosd['make_dir']+rdir+' '+rse

          if o=='con':
             ck.out('')
             ck.out('Executing: '+x)

          r=os.system(x)

       # If remote and target exe
       if remote=='yes' and target_exe!='' and srn==0:
          if srn==0:
             # Copy exe to remote
             ry=copy_file_to_remote({'host_os_dict':hosd,
                                     'target_os_dict':tosd,
                                     'device_id':tdid,
                                     'file1':target_exe,
                                     'file2':rdir+target_exe,
                                     'out':oo})
             if ry['return']>0: return ry

             # Set chmod
             se=tosd.get('set_executable','')
             if se!='':
                y=rs+' '+se+' '+rdir+target_exe+' '+rse
                if o=='con':
                   ck.out(sep)
                   ck.out(y)
                   ck.out('')

                ry=os.system(y)
                if ry>0:
                   return {'return':1, 'error':'making binary executable failed on remote device'}

       # Loading dataset
       dset={}
       dp=''
       dfiles=[]
       ddalias=''
       dduid=''
       if dduoa!='':
          rx=ck.access({'action':'load',
                        'module_uoa':dmuoa,
                        'data_uoa':dduoa})
          if rx['return']>0: return rx
          ddalias=rx['data_alias']
          dduid=rx['data_uid']
          dd=rx['dict']
          dp=rx['path']
          xdp=dp+sdirs

          if remote=='yes':
             c=c.replace('$#dataset_path#$','')
          else:
             c=c.replace('$#dataset_path#$',xdp)

          sb+='\n'+no+etset+' CK_DATASET_PATH='+xdp+'\n'
          dset['path']=xdp

          dfiles=dd.get('dataset_files',[])
          if len(dfiles)>0:

             dfile=i.get('dataset_file','')
             if dfile!='':
                dfiles=[dfile]
                misc['dataset_file']=dfile
             elif len(dfiles)>0:
                if len(dfiles)==1:
                   dfile=dfiles[0]
                else:
                   # Check if has description:
                   desc_dfiles=[]
                   desc_dfiles1=dd.get('desc_dataset_files',{})
                   for q in dfiles:
                       x=desc_dfiles1.get(q,{}).get('name','')
                       if x=='': x=q
                       desc_dfiles.append(x)

                   ck.out('************ Selecting dataset file ...')
                   ck.out('')

                   r=ck.access({'action':'select_list',
                                'module_uoa':cfg['module_deps']['choice'],
                                'choices':dfiles,
                                'desc':desc_dfiles})
                   if r['return']>0: return r
                   dfile=r['choice']

             if dfile!='':
                env['CK_DATASET_FILENAME']=dfile
#                sb+='\n'+no+eset+' CK_DATASET_FILENAME='+dfile+'\n'
                dset['file']=dfile

                # Check if need to add to env
                if adfe=='yes':
                   jdfile=os.path.join(xdp,os.path.splitext(dfile)[0]+'.json')

                   # Attempt to load json data sets file
                   rk=ck.load_json_file({'json_file':jdfile})
                   if rk['return']>0: return rk
                   xxd=rk['dict']

                   # Smart update - if already there, do not update
                   dfile_keys=list(xxd.keys())
                   for k in xxd:
                       if env.get(k,'')=='':
                          env[k]=xxd[k]

             xdfiles=[] # put selected file first
             if dfile=='':
                xdfiles=dfiles
             else:
                xdfiles.append(dfile)
                for df in dfiles:
                    if df!=dfile:
                       xdfiles.append(df)

             for k in range(0, len(xdfiles)):
                 df=dfiles[k]
#                 if dfile!='' and k==0: 
#                    df=dfile

                 kk='$#dataset_filename'
                 if k>0: kk+='_'+str(k)
                 kk+='#$'

                 c=c.replace(kk, df)

                 if remote=='yes' and srn==0 and sdi!='yes' and sdc!='yes':
                    # Check if only selected to send
                    if vcmd.get('send_only_selected_file','')=='yes' and dfile!=df:
                       continue

                    # check if also extra files
                    dfx=[df]

                    dfx1=dd.get('extra_dataset_files',{}).get(df,[])
                    for dfy in dfx1:
                        if dfy not in dfx:
                           dfx.append(dfy)

                    for dfz in dfx:
                        df0, df1 = os.path.split(dfz)

                        # Push data files to device
                        y=tosd.get('remote_push_pre','').replace('$#device#$',xtdid)
                        if y!='':
                           y=y.replace('$#file1#$', os.path.join(dp,dfz))
                           y=y.replace('$#file1s#$', df1)
                           y=y.replace('$#file2#$', rdir+dfz)

                           if o=='con':
                              ck.out(sep)
                              ck.out(y)
                              ck.out('')

                           ry=os.system(y)
                           if ry>0:
                              return {'return':1, 'error':'copying to remote device failed'}

                        # Push data files to device, if first time
                        y=tosd['remote_push'].replace('$#device#$',xtdid)
                        y=y.replace('$#file1#$', os.path.join(dp,dfz))
                        y=y.replace('$#file1s#$', df1)
                        y=y.replace('$#file2#$', rdir+dfz)
                        if o=='con':
                           ck.out(sep)
                           ck.out(y)
                           ck.out('')

                        ry=os.system(y)
                        if ry>0:
                           return {'return':1, 'error':'copying to remote device failed'}

          rcm=dd.get('cm_properties',{}).get('run_time',{}).get('run_cmd_main',{})
          for k in rcm:
              kv=rcm[k]
              c=c.replace('$#'+k+'#$',kv)

          misc['dataset_uoa']=dduoa

       # Add env to batch
       sb+='\n'
       sbenv=''
       for k in sorted(env):
           v=str(env[k])
           v=v.replace('$<<',tsvarb).replace('>>$',tsvare)

           if eifsx!='' and wb!='yes':
              if v.find(' ')>=0 and not v.startswith(eifsx):
                 v=eifsx+v+eifsx

           sbenv+=no+etset+' '+k+'='+str(v)+'\n'
       sb+=sbenv+'\n'

       if tosd.get('extra_env','')!='':
          sb+=no+tosd['extra_env']+'\n'

       # Check if need to add env with current path
       if remote=='yes' and len(tosd.get('remote_env_set',[]))>0:
           for q in tosd['remote_env_set']:
               sb+=q+'\n'
           sb+='\n'

       if remote=='yes':
            cetr = rt.get('copy_env_to_remote', [])
            for etr_key in cetr:
                etr_value = aenv.get(etr_key, '')
                sb += '{} {}="{}"\n'.format(etset, etr_key, etr_value)

       # Check if pre-processing script via CK
       pvck=rt.get('pre_process_via_ck',{})
       if len(pvck)>0:

          pvckp=src_path_local

          pvckm=pvck.get('module_uoa','')
          if pvckm=='': pvckm=work['self_module_uid']
          pvckd=pvck.get('data_uoa','')

          if pvckd!='':
             rp=ck.access({'action':'find',
                           'module_uoa':pvckm,
                           'data_uoa':pvckd})
             if rp['return']>0: return rp
             pvckp=rp['path']

          pvckc=pvck.get('script_name','')
          if pvckc=='': pvckc='preprocess'

          if o=='con':
             ck.out('')
             ck.out('  (pre processing via CK ('+pvckp+', '+pvckc+')')
             ck.out('')

          # Check if has custom script
          try:
              cdd=os.getcwd()
          except OSError:
              os.chdir('..')
              cdd=os.getcwd()

          cs=None
          rxx=ck.load_module_from_path({'path':pvckp, 'module_code_name':pvckc, 'skip_init':'yes'})

          cs=rxx.get('code', None)
          if cs==None:
             rxx['return']=1
             rxx['error']='problem loading python code: '+rxx['error']

          if rxx['return']==0:
             os.chdir(cdd) # restore current dir from above operation

             # Call customized script
             ii={"host_os_uoa":hosx,
                 "host_os_uid":hos,
                 "host_os_dict":hosd,
                 "target_os_uoa":tosx,
                 "target_os_uid":tos,
                 "target_os_dict":tosd,
                 "target_device_id":tdid,
                 "ck_kernel":ck,
                 "misc":misc,
                 "meta":meta,
                 "deps":deps,
                 "env":env,     # env has to be updated via returned bat file, but it can be updated for the reproducibility
                 "run_time":rt,
                 "dataset_uoa":dduoa,
                 "dataset_file":dfile,
                 "dataset_path":dp,
                 "dataset_meta":dset,
                 "params":params,
                 "device_cfg":device_cfg,
                 "out":oo
                }

             rxx=cs.ck_preprocess(ii)

             if rxx['return']==0:
                nenv=rxx.get('new_env',{})
                for zk in nenv:
                    zv=str(nenv[zk])
                    env[zk]=zv
                    if zv.find(' ')>=0 and not zv.startswith(eifsx):
                       zv=eifsx+zv+eifsx
                    sb+=no+etset+' '+zk+'='+str(zv)+'\n'

                psb=rxx.get('bat','')
                if psb!='':
                    sb+='\n'+psb+'\n'

                # Add any additional commands to be added to the run script
                peppc=rxx.get('extra_post_process_cmd','')
                if peppc!='':
                    eppc+='\n'+peppc+'\n'

                # Add any additional input files required by preprocessing
                preprocessed_rif=rxx.get('run_input_files',[])
                rif += sorted(list(set(preprocessed_rif)-set(rif)))

                # Add any additional output files generated by preprocessing
                preprocessed_rof=rxx.get('run_output_files',[])
                rof += sorted(list(set(preprocessed_rof)-set(rof)))

          if rxx['return']>0:
             misc['run_success']='no'
             misc['run_success_bool']=False
             misc['fail_reason']='pre-processing script via CK failed ('+rxx['error']+')'

             if o=='con':
                ck.out('  (pre processing script via CK failed: '+rxx['error']+')')

             return {'return':0, 'tmp_dir':rcdir, 'misc':misc, 'characteristics':ccc, 'deps':deps}

       # If remote and target exe
       if remote=='yes' and (target_exe!='' or meta.get('force_copy_input_files_to_remote','')=='yes'):
          if sdi!='yes' and srn==0 or ati==0:
             # Copy explicit input files, if first time
             remapped_env_path = {}
             for df in rif:
                 # Update if has env
                 j1=df.find('$<<')
                 j2=df.find('>>$')
                 if -1<j1 and j1<j2:
                    df_envar_key    = df[j1+3:j2]
                    df_suffix       = df[j2+3:]
                    skip_if_missing = False

                    if df_envar_key=='':    # $<<>>$abcde.txt means it's in the program's tmp/ directory
                        df = df_suffix
                        treat_input_file_path_as_absolute[df]='yes'
                    else:
                        if df_envar_key[0]=='?':
                            skip_if_missing = True
                            df_envar_key = df_envar_key[1:]

                        df_envar_value=env.get(df_envar_key, aenv.get(df_envar_key, ''))

                        if df_envar_value!='':
                            df=df[:j1]+df_envar_value+df_suffix
                            treat_input_file_path_as_absolute[df]='yes'

                        elif skip_if_missing:
                            if o=='con':
                              ck.out('Skipping copying a file to remote, because '+df_envar_key+' conditional variable path mapped to an empty value')
                            continue
                        else:
                            return {'return':1, 'error':'environment variable "'+df_envar_key+'" was not found in environment from dependencies'}

                 else:
                    df_envar_key=None

                 df_basename = os.path.basename(df)

                 if df in treat_input_file_path_as_absolute:
                    df_host_path=df
                    df_target_path=rdir+df_basename
                 else:
                    df_host_path=os.path.join(p,df)
                    df_target_path=rdir+df

                 if df_envar_key: # if it was a substitution...
                    remapped_env_path[df_envar_key] = df_target_path if df_suffix=='' else rdir # ...remapping the original variable

                 ry=copy_file_to_remote({'host_os_dict':hosd,
                                         'target_os_dict':tosd,
                                         'device_id':tdid,
                                         'file1':df_host_path,
                                         'file1s':df_basename,
                                         'file2':df_target_path,
                                         'out':oo})
                 if ry['return']>0: return ry

             # delayed for later to only record each remapping once:
             for df_envar_key in remapped_env_path:
                sb += etset+' '+df_envar_key+'='+str(remapped_env_path[df_envar_key])+'\n'

       # Check if has unparsed
       if sunparsed!='':
          c+=' '+sunparsed

       # Check if redirect output
       rco1=rt.get('run_cmd_out1','')
       rco2=rt.get('run_cmd_out2','')

       if ee!='':
          sb+='\n'+no+ee+'\n\n'

       sb+='\necho    executing code ...\n'

       if (remote!='yes' or meta.get('run_via_third_party','')=='yes') and cons!='yes':
          if ercmd!='': c+=' '+ercmd
          if rco1!='': c+=' '+stro+' '+rco1
          if rco2!='': c+=' '+stre+' '+rco2
       sb+=no+c+'\n'

       # Stop energy monitor, if needed and if supported
       if me=='yes' and sspm2!='':
          if o=='con':
             ck.out('')
             ck.out('Adding energy monitor')
             ck.out('')

          sb+='\n'
          sb+=scall+' '+sspm2+'\n'
          sb+='\n'

       fn=''

       # Check pre-processing scripts
       lppc0=rt.get('pre_process_cmds',[])
       ppc0=rt.get('pre_process_cmd','')
       if ppc0!='': lppc0.append(ppc0)

       # Check if traditional pre-processing script
       srx=0 # script exit code
       if len(lppc0)>0:
          sbu=sbenv+'\n\n'

          if ee!='':
             sbu+='\n'+no+ee+'\n\n'

          for ppc in lppc0:
              while ppc.find('$<<')>=0:
                 j1=ppc.find('$<<')
                 j2=ppc.find('>>$')
                 if j2>0:
                    j3=ppc[j1+3:j2]
                    ppc=ppc[:j1]+env.get(j3,'')+ppc[j2+3:]

              ppc=ppc.replace('$<<',svarb).replace('>>$',svare)
              ppc=ppc.replace('$#dir_sep#$',stdirs)
              ppc=ppc.replace('$#src_path_local#$', src_path_local).replace('$#src_path#$', src_path)

#             Pre-processing is performed on the local machine, so dataset path should be local, not remote!
              ppc=ppc.replace('$#dataset_path#$',dp+sdirs)

              r9=substitute_some_ck_keys({'string':ppc})
              if r9['return']>0: return r9
              ppc=r9['string']

              # Substitute dataset file if needed
              for k in range(0, len(dfiles)):
                  df=dfiles[k]
                  if dfile!='' and k==0: df=dfile
                  kk='$#dataset_filename'
                  if k>0: kk+='_'+str(k)
                  kk+='#$'
                  ppc=ppc.replace(kk, df)

              sbu+=ppc+'\n'

          if o=='con':
              ck.out('')
              ck.out('  (pre processing:"')
              ck.out('')
              ck.out(sbu)
              ck.out('  )')

          # Record to tmp batch and run
          rx=ck.gen_tmp_file({'prefix':'tmp-', 'suffix':sext, 'remove_dir':'yes'})
          if rx['return']>0: return rx
          fn=rx['file_name']

          rx=ck.save_text_file({'text_file':fn, 'string':sbu})
          if rx['return']>0: return rx

          y=''
          if sexe!='':
             y+=sexe+' '+sbp+fn+envsep

          yy=scall+' '+sbp+fn
          y+=' '+yy

          srx=os.system(y)

          if sca!='yes' and os.path.isfile(fn):
             os.remove(fn)

          # If error code > 0, set as the error code of the main program and quit
          if srx>0:
             misc['run_success']='no'
             misc['run_success_bool']=False
             misc['fail_reason']='pre-processing script failed'

             if o=='con':
                ck.out('  (pre processing script failed!)')

             return {'return':0, 'tmp_dir':rcdir, 'misc':misc, 'characteristics':ccc, 'deps':deps}

       # Check post-processing scripts
       lppc=rt.get('post_process_cmds',[])
       lppcvc=rt.get('post_process_via_ck','')
       ppc=rt.get('post_process_cmd','')
       if ppc!='': lppc.append(ppc)

       ck_check_output=None # detect customized output comparison plugin

       fgtf=rt.get('fine_grain_timer_file','')
       if env.get('XOPENME_TIME_FILE','')!='':
          fgtf=env['XOPENME_TIME_FILE']

       # Check if extra post_process
       if eppc!='':
          sb+=eppc+'\n'

       sb=sb.replace('$#BIN_FILE#$', te)

       te1=te
       if te.startswith('./'):
          te1=te[2:]
       sb=sb.replace('$#ONLY_BIN_FILE#$', te1)

       # Calibrate execution time (to make it longer and minimize system variation,
       #   if supported)
       csb=sb
       orepeat=repeat
       calibrate_success=False

       xcn_max=i.get('calibration_max','')
       if xcn_max=='': xcn_max=cfg['calibration_max']
       cn_max=int(xcn_max)

       rof += rt.get('run_output_files',[])

       cn=1
       while True:
          # Clean output files
          files_to_delete = rt.get('run_delete_files',[]) + rof
          if rco1!='': files_to_delete.append(rco1)
          if rco2!='': files_to_delete.append(rco2)

          if o=='con' and len(files_to_delete)>0:
             ck.out('  Cleaning files and directories:')

          if skip_exec!='yes':
             for df in files_to_delete:
                 if o=='con': ck.out('    '+df)

                 if remote=='yes' and meta.get('run_via_third_party','')!='yes':
                    # Clean data files on device
                    y=rs+' '+tosd['delete_file']+ ' '+rdir+df+' '+rse
                    if o=='con':
                       ck.out('')
                       ck.out(y)
                       ck.out('')

                    ry=os.system(y)

                    if tosd.get('delete_file_extra','')!='':
                       y=tosd['delete_file_extra']+df+' '+rse
                       if o=='con':
                          ck.out('')
                          ck.out(y)
                          ck.out('')

                       ry=os.system(y)

                 if os.path.isfile(df):
                    os.remove(df)
                 elif os.path.isdir(df):
                    shutil.rmtree(df,ignore_errors=True)

             # Delete global directories locally (needed for ARM WA)
             for df in meta.get('clean_dirs',[]):
                 if df!='':
                    if o=='con':
                       ck.out('')
                       ck.out('  Removing directory '+df+' ...')
                       ck.out('')

                    shutil.rmtree(df,ignore_errors=True)

          new_directories = rt.get('run_make_directories',[]);
          if len(new_directories)>0:
                if o=='con':
                    ck.out('  Creating new directories:')

                for new_dir in new_directories:
                    if remote=='yes':
                        x=rs+' '+tosd['make_dir']+rdir+new_dir+' '+rse

                        if o=='con':
                            ck.out('')
                            ck.out('Executing: '+x)

                        r=os.system(x)
                    else:
                        shutil.rmtree(new_dir,ignore_errors=True)
                        os.mkdir(new_dir)

          if o=='con': ck.out('')

          if sc!='yes' and 'CT_REPEAT_MAIN' in run_vars:
             if o=='con':
                ck.out(sep)
                ck.out('### Calibration '+str(cn)+' out of '+xcn_max+' ; Kernel repeat number = '+str(repeat))

          sb=csb
          if sc!='yes' and 'CT_REPEAT_MAIN' in run_vars and repeat!=-1:
             sb=sb.replace('$#repeat#$', str(repeat))
             env['CT_REPEAT_MAIN']=str(repeat)

          # Check sudo init
          if isd=='yes':
             if o=='con':
                ck.out(sep)
                ck.out('  (preparing sudo - may ask password ...)')
             if remote!='yes':
                os.system(sudo_init)

          if o=='con':  ck.out(sep)

          # Prepare tmp batch file with run instructions
          if rbn=='':
             rx=ck.gen_tmp_file({'prefix':'tmp-', 'suffix':sext, 'remove_dir':'yes'})
             if rx['return']>0: return rx
             fn=rx['file_name']
          else:
             fn=rbn

          xbbp=bbp
          if remote=='yes':
             xbbp=bbpt

          if xbbp!='':
             sb=bbp+'\n\n'+sb

          rx=ck.save_text_file({'text_file':fn, 'string':sb})
          if rx['return']>0: return rx

          # Prepare execution
          if remote=='yes' and meta.get('run_via_third_party','')!='yes':
             # Copy above batch file to remote device
             y=tosd.get('remote_push','').replace('$#device#$',xtdid)
             y=y.replace('$#file1#$', fn)
             y=y.replace('$#file2#$', rdir+fn)

             if o=='con':
                ck.out(sep)
                ck.out(y)
                ck.out('')

             ry=os.system(y)
             if ry>0:
                return {'return':1, 'error':'copying to remote device failed'}

             # Prepare command line for remote device
             y=''

             if isd=='yes':
                y+=sudo_init+' '+envtsep
                y+=sudo_pre+' '+envtsep

             y+=tosd.get('interpreter','')+' '+stbp+fn

#             x=sb.split('\n')
#             for q in x:
#                 if q!='':
#                    if y!='': y+=envtsep
#                    y+=' '+q

             if isd=='yes': y=y+' '+envtsep+' '+sudo_post

             eifsx1=eifsx
             if rs.endswith('"'):
                 eifsx1=''
             elif eifsx!='':
                 y=y.replace('"','\\"')

             yrdir=rdir
             if tosd.get('remote_dir_full','')!='':
                 yrdir=tosd['remote_dir_full']+stdirs+rdir

             y=rs+' '+eifsx1+tosd['change_dir']+' '+yrdir+envtsep+' '+y+eifsx1+' '+rse

             if cons!='yes':
                if ercmd!='': y+=' '+ercmd
                if rco1!='': y+=' '+stro+' '+rco1
                if rco2!='': y+=' '+stre+' '+rco2

#             if o=='con':
#                ck.out(y)

          else:
             y=''
             if sexe!='':
                y+=sexe+' '+sbp+fn+envsep

             if isd=='yes':
                yy=sudo_pre+' '+sbp+fn+' '+envtsep+' '+sudo_post
             else:
                yy=scall+' '+sbp+fn
             y+=' '+yy

          if remote!='yes' and ubtr!='': y=ubtr.replace('$#cmd#$',y)

          if o=='con':
             ck.out(sep)
             ck.out('Prepared script:')
             ck.out('')
             ck.out(sb)
             ck.out(sep)
             ck.out('  ('+y.strip()+')')

          if o=='con':
             ck.out('')
             ck.out('  (sleep 0.5 sec ...)')
             time.sleep(0.5)
             ck.out('')
             ck.out('  (run ...)')

          ############################################## Running code here ##############################################
          sys.stdout.flush()
          start_time1=time.time()

          rx=0
          rry=0
          if skip_exec!='yes':
             ry=ck.system_with_timeout({'cmd':y, 'timeout':xrto})
             rry=ry['return']
             if rry>0:
                if rry!=8: return ry
             else:
                rx=ry['return_code']
          elif o=='con':
             ck.out('')
             ck.out('      * skiped execution ... *')

          exec_time=time.time()-start_time1
          # Hack to fix occasional strange effect when time.time() is 0
          if exec_time<0: exec_time=-exec_time

          if sca!='yes':
             if fn!='' and os.path.isfile(fn): os.remove(fn)

          # Pull files from the device if remote
          if remote=='yes':

             xrof=rof
             if i.get('pull_only_timer_files','')=='yes':
                xrof=[fgtf]

             for df in xrof:
                 # Pull output files from device
                 df0, df1 = os.path.split(df)

                 # Push data files to device
                 y=tosd['remote_pull'].replace('$#device#$',xtdid)
                 y=y.replace('$#file1#$', rdir+df)
                 y=y.replace('$#file1s#$', df1)
                 y=y.replace('$#file2#$', df)
                 if o=='con':
                    ck.out('')
                    ck.out(y)
                    ck.out('')

                 ry=os.system(y)

                 y=tosd.get('remote_pull_post','').replace('$#device#$',xtdid)
                 if y!='':
                    y=y.replace('$#file1#$', rdir+df)
                    y=y.replace('$#file1s#$', df1)
                    y=y.replace('$#file2#$', df)

                    if o=='con':
                       ck.out(sep)
                       ck.out(y)
                       ck.out('')

                    ry=os.system(y)
                    if ry>0:
                       return {'return':1, 'error':'pulling from remote device failed'}

          # Check if print files
          pfar=vcmd.get('print_files_after_run',[])
          if len(pfar)==0:
             pfar=meta.get('print_files_after_run',[])

          if len(pfar)>0 and sfp!='yes' and o=='con':
             ck.out('')
             ck.out(' (printing output files) ')

             for q in pfar:
                 ck.out('')
                 ck.out('    * '+q)
                 ck.out('')

                 rz=ck.load_text_file({'text_file':q, 'split_to_list':'yes', 'encoding':sys.stdout.encoding})
                 if rz['return']==0:
                    lxx=rz['lst']
                    for q1 in lxx:
                        ck.out('      '+q1)

          # Check if post-processing script from CMD
          if pp_uoa!='' and skip_exec!='yes':
             if o=='con':
                ck.out('')
                ck.out('  (post processing from script '+pp_uoa+' / '+pp_name+' ... )"')
                ck.out('')

             iz={'action':'run',
                 'module_uoa':cfg['module_deps']['script'],
                 'data_uoa':pp_uoa,
                 'name':pp_name,
                 'params':pp_params}
             rz=ck.access(iz)
             if rz['return']>0: return rz
             # For now ignore output

          # Check if post-processing script
          srx=0 # script exit code

          # Newer variant (more consistent with pre_process_via_ck
          if type(lppcvc)==dict and skip_exec!='yes':
             pvck=lppcvc

             pvckp=src_path_local

             pvckm=pvck.get('module_uoa','')
             if pvckm=='': pvckm=work['self_module_uid']
             pvckd=pvck.get('data_uoa','')

             if pvckd!='':
                rp=ck.access({'action':'find',
                              'module_uoa':pvckm,
                              'data_uoa':pvckd})
                if rp['return']>0: return rp
                pvckp=rp['path']

             pvckc=pvck.get('script_name','')
             if pvckc=='': pvckc='postprocess'

             if o=='con':
                ck.out('')
                ck.out('  (post processing via CK ('+pvckp+', '+pvckc+')')
                ck.out('')

             # Check if has custom script
             try:
                 cdd=os.getcwd()
             except OSError:
                 os.chdir('..')
                 cdd=os.getcwd()

             cs=None
             rxx=ck.load_module_from_path({'path':pvckp, 'module_code_name':pvckc, 'skip_init':'yes'})

             cs=rxx.get('code', None)
             if cs==None:
                rxx['return']=1
                rxx['error']='problem loading python code: '+rxx['error']

                misc['run_success']='no'
                misc['run_success_bool']=False
                misc['fail_reason']=rxx['error']

                return {'return':0, 'tmp_dir':rcdir, 'misc':misc, 'characteristics':ccc, 'deps':deps}

             if rxx['return']==0:
                os.chdir(cdd) # restore current dir from above operation

                if cs!=None and 'ck_check_output' in dir(cs):
                   ck_check_output=cs.ck_check_output

                if cs!=None and 'ck_postprocess' in dir(cs):
                   as_cmd=False

                   # Call customized script
                   ii={"host_os_uoa":hosx,
                       "host_os_uid":hos,
                       "host_os_dict":hosd,
                       "target_os_uoa":tosx,
                       "target_os_uid":tos,
                       "target_os_dict":tosd,
                       "target_device_id":tdid,
                       "ck_kernel":ck,
                       "misc":misc,
                       "meta":meta,
                       "deps":deps,
                       "env":env,
                       "dataset_uoa":dduoa,
                       "dataset_file":dfile,
                       "dataset_path":dp,
                       "dataset_meta":dset,
                       "run_time":rt,
                       "params":params,
                       "device_cfg":device_cfg,
                       "out":oo
                      }

                   rxx=cs.ck_postprocess(ii)
                   srx=rxx['return']
                   if srx==0:
                      xchars=rxx.get('characteristics',{})
                      if len(xchars)>0:
                         et=xchars.get('execution_time','')
                         if et!='':
                            exec_time=float(et)
                         ccc.update(xchars)

                      if len(rxx.get('misc',{}))>0:
                         misc.update(rxx['misc'])

                   else:
                      if o=='con':
                         ck.out('  (post processing script failed: '+rxx['error']+'!)')

                      misc['run_success']='no'
                      misc['run_success_bool']=False
                      misc['fail_reason']=rxx['error']

#                                break
                      return {'return':0, 'tmp_dir':rcdir, 'misc':misc, 'characteristics':ccc, 'deps':deps}

          # Older variant
          if len(lppc)>0 and skip_exec!='yes':
             for ppc in lppc:
                 while ppc.find('$<<')>=0:
                    j1=ppc.find('$<<')
                    j2=ppc.find('>>$')
                    if j2>0:
                       j3=ppc[j1+3:j2]
                       ppc=ppc[:j1]+env.get(j3,'')+ppc[j2+3:]

                 ppc=ppc.replace('$<<',svarb).replace('>>$',svare)
                 ppc=ppc.replace('$#dir_sep#$',stdirs)
                 ppc=ppc.replace('$#src_path_local#$', src_path_local).replace('$#src_path#$', src_path)

#                Post-processing is performed on the local machine, so dataset path should be local, not remote!
#                 if remote=='yes':
#                    ppc=ppc.replace('$#dataset_path#$','')
#                 elif dp!='':
                 ppc=ppc.replace('$#dataset_path#$',dp+sdirs)

                 r9=substitute_some_ck_keys({'string':ppc})
                 if r9['return']>0: return r9
                 ppc=r9['string']

                 if o=='con':
                    ck.out('')
                    ck.out('  (post processing: "'+ppc+'"')
                    ck.out('')

                 # Check if via CK, otherwise run as system
                 if lppcvc=='yes':
                    ppcs=ppc.split()
                    if len(ppcs)>1:
                       if ppcs[0].startswith('python'):
                          ppcm=ppcs[1]
                          ppcm1=os.path.basename(ppcm)
                          ppcm2=os.path.dirname(ppcm)

                          if ppcm1.endswith('.py'):
                             ppcm1=ppcm1[:-3]

                          # Check if has custom script
                          try:
                              cdd=os.getcwd()
                          except OSError:
                              os.chdir('..')
                              cdd=os.getcwd()

                          cs=None
                          rxx=ck.load_module_from_path({'path':ppcm2, 'module_code_name':ppcm1, 'skip_init':'yes'})
                          if rxx['return']>0:
                             if o=='con':
                                ck.out('  (post processing script failed: '+rxx['error']+'!)')

                             misc['run_success']='no'
                             misc['run_success_bool']=False
                             misc['fail_reason']=rxx['error']

#                             break
                             return {'return':0, 'tmp_dir':rcdir, 'misc':misc, 'characteristics':ccc, 'deps':deps}

                          cs=rxx['code']

                          os.chdir(cdd) # restore current dir from above operation

                          if cs!=None and 'ck_check_output' in dir(cs):
                             ck_check_output=cs.ck_check_output

                          if cs!=None and 'ck_postprocess' in dir(cs):
                             as_cmd=False

                             # Call customized script
                             ii={"host_os_uoa":hosx,
                                 "host_os_uid":hos,
                                 "host_os_dict":hosd,
                                 "target_os_uoa":tosx,
                                 "target_os_uid":tos,
                                 "target_os_dict":tosd,
                                 "target_device_id":tdid,
                                 "ck_kernel":ck,
                                 "misc":misc,
                                 "meta":meta,
                                 "deps":deps,
                                 "env":env,
                                 "dataset_uoa":dduoa,
                                 "dataset_file":dfile,
                                 "dataset_path":dp,
                                 "dataset_meta":dset,
                                 "run_time":rt,
                                 "params":params,
                                 "device_cfg":device_cfg,
                                 "out":oo
                                }

                             rxx=cs.ck_postprocess(ii)
                             srx=rxx['return']
                             if srx==0:
                                xchars=rxx.get('characteristics',{})
                                if len(xchars)>0:
                                   et=xchars.get('execution_time','')
                                   if et!='':
                                      exec_time=float(et)
                                   ccc.update(xchars)

                                if len(rxx.get('misc',{}))>0:
                                   misc.update(rxx['misc'])

                             else:
                                if o=='con':
                                   ck.out('  (post processing script failed: '+rxx['error']+'!)')

                                misc['run_success']='no'
                                misc['run_success_bool']=False
                                misc['fail_reason']=rxx['error']

#                                break
                                return {'return':0, 'tmp_dir':rcdir, 'misc':misc, 'characteristics':ccc, 'deps':deps}

                 else:
                    srx=os.system(ppc)
                    # If error code > 0, set as the error code of the main program and quit
                    if srx>0:
                       if o=='con':
                          ck.out('  (post processing script failed!)')

                       misc['run_success']='no'
                       misc['run_success_bool']=False
                       misc['fail_reason']='post processing script failed'

#                       break
                       return {'return':0, 'tmp_dir':rcdir, 'misc':misc, 'characteristics':ccc, 'deps':deps}

          # If script failed, exit
          if srx>0:
#              break
              return {'return':0, 'tmp_dir':rcdir, 'misc':misc, 'characteristics':ccc, 'deps':deps}

          # Check if fine-grain time
          if fgtf!='' and skip_exec!='yes':
             if o=='con':
                ck.out('')
                ck.out('  (reading fine grain timers from '+fgtf+' ...)')
                ck.out('')

             rq=ck.load_json_file({'json_file':fgtf})
             if rq['return']>0:
                misc['run_success']='no'
                misc['run_success_bool']=False
                misc['fail_reason']=rq['error']

                ccc['return_code']=rx

                if o=='con':
                    ck.out('')
                    ck.out('Program execution likely failed (can\'t find fine grain timers)!')
                    ck.out('')

                return {'return':0, 'tmp_dir':rcdir, 'misc':misc, 'characteristics':ccc, 'deps':deps}

             drq=rq['dict']
             ccc.update(drq)
             et=drq.get('execution_time','')
             exec_time=0.0
             if et!='':
                exec_time=float(et)

             if o=='con' and i.get('skip_print_timers','')!='yes':
                import json
                ck.out(json.dumps(drq, indent=2, sort_keys=True))
                ck.out('')

          # If return code >0 and program does not ignore return code, quit
          if (rx>0 and vcmd.get('ignore_return_code','').lower()!='yes') or rry>0:
             break

          # Check calibration
          if sc=='yes' or repeat==-1 or 'CT_REPEAT_MAIN' not in run_vars:
             calibrate_success=True
             break

          orepeat=repeat
          if exec_time<0.5: repeat*=10
          elif 0.8<(calibrate_time/exec_time)<1.4:
             calibrate_success=True
             break
          else:
             repeat*=float(calibrate_time/exec_time)
             if repeat<1: repeat=1
          repeat=int(repeat)

          if repeat==orepeat:
             calibrate_success=True
             break

          if o=='con' and sc!='yes':
             ck.out('')
             ck.out('### Calibration: time='+str(exec_time)+'; CT_REPEAT_MAIN='+str(orepeat)+'; new CT_REPEAT_MAIN='+str(repeat))

          if cn>=cn_max:
             misc['run_success']='no'
             misc['run_success_bool']=False
             misc['fail_reason']='calibration failed'

             if o=='con':
                ck.out('')
                ck.out('Program execution likely failed ('+misc['fail_reason']+')!')
                ck.out('')

             return {'return':0, 'tmp_dir':rcdir, 'misc':misc, 'characteristics':ccc, 'deps':deps}

          cn+=1

       if sc!='yes' and repeat!=-1 and 'CT_REPEAT_MAIN' in run_vars:
          if calibrate_success==False:
             misc['run_success']='no'
             misc['run_success_bool']=False
             misc['fail_reason']='calibration problem'

             if o=='con':
                ck.out('')
                ck.out('Program execution likely failed ('+misc['fail_reason']+')!')
                ck.out('')

             return {'return':0, 'tmp_dir':rcdir, 'misc':misc, 'characteristics':ccc, 'deps':deps}

       xrepeat=repeat
       if xrepeat<1: xrepeat=1

       ccc['return_code']=rx
       ccc['execution_time']=exec_time/abs(repeat)
       ccc['total_execution_time']=exec_time
       ccc['repeat']=xrepeat
       misc['calibration_success']=calibrate_success

       if rry==8:
          misc['run_success']='no'
          misc['run_success_bool']=False
          misc['fail_reason']=ry['error']

          ccc['run_success']='no'
          ccc['run_success_bool']=False
          ccc['fail_reason']=ry['error']
       if rx>0 and vcmd.get('ignore_return_code','').lower()!='yes':
          misc['run_success']='no'
          misc['run_success_bool']=False
          misc['fail_reason']='return code '+str(rx)+' !=0 '

          ccc['run_success']='no'
          ccc['run_success_bool']=False
          ccc['fail_reason']='return code '+str(rx)+' !=0 '
       else:
          misc['run_success']='yes'
          misc['run_success_bool']=True
          ccc['run_success']='yes'
          ccc['run_success_bool']=True

       ccc['execution_time_with_module']=time.time()-start_time

       # Check output correctness, if needed *****************************************************
       rcof=rt.get('run_correctness_output_files',[])
       if len(rcof)==0:
          rcof=meta.get('run_correctness_output_files',[])

       rcvars=rt.get('run_correctness_vars',[])

       if ccc['run_success_bool'] and len(rcof)>0 and i.get('skip_output_validation','')!='yes':
          ck.out('')
          ck.out('  (checking output correctness ...)')

          # Prepare directory with output files
          po=kcmd+'-'+dduid

          if dfile!='':
             if rt.get('run_correctness_extra_keys_from_dataset_file_json','')=='yes':
                for q in sorted(dfile_keys):
                    po+='-'+str(env.get(q,''))
             else:
                po+='-'+dfile
          if rt.get('output_invariant_of_repeat','')!='yes':
             po+='-'+str(xrepeat)

          # Check if output depends on extra vars
          if len(rcvars)>0:
             for q in rcvars:
                 po+='-'+str(env.get(q,''))

          oruoa=i.get('output_validation_repo','')
          pox=''
          found=False

          # Check if output from another program
          program_output_uoa=duoa

          if i.get('program_output_uoa','')!='':
             program_output_uoa=i['program_output_uoa']

          if rt.get('program_output_uoa','')!='':
             program_output_uoa=rt['program_output_uoa']

          # Check UID of program_output_uoa
          rx=ck.access({'action':'find',
                        'module_uoa':work['self_module_uid'],
                        'data_uoa':program_output_uoa})
          if rx['return']>0: return rx
          program_output_uoa=rx['data_uid']

          if i.get('overwrite_reference_output','')!='yes':
             if o=='con':
                ck.out('     * Searching directory with reference output "'+po+'" ...')

             # Search related entries with outputs (can be multiple - in local and project repos!)
             rx=ck.access({'action':'search',
                           'module_uoa':cfg['module_deps']['program.output'],
                           'data_uoa':'program-uid-'+program_output_uoa})
             if rx['return']>0: return rx
             dslst=rx['lst']

             for q in dslst:
                 pox=os.path.join(q['path'],po)
                 if os.path.isdir(pox):
                    found=True
                    break

          vfail=False
          vo={}

          if found:
             if o=='con':
                ck.out('     * Reference output found - validating ...')
                ck.out('     * File: '+pox)

             for fz in rcof:
                 vr=''

                 p1=os.path.join(cdir,fz)

                 if not os.path.isfile(p1):
                    vr='file not found'
                    vfail=True
                 else:
                    p2=os.path.join(pox,fz)

                    # If reference file doesn't exist (for example, we later updated meta),
                    # copy it to the reference ..
                    if not os.path.isfile(p2):
                       shutil.copyfile(p1,p2)
                    else:
                       if ck_check_output!=None:
                          r=ck_check_output({'ck_kernel':ck,
                                             'file1':p1,
                                             'file2':p2,
                                             'meta':meta,
                                             'env':env})
                          if r['return']>0:
                             vr=r['error']
                             vfail=True
                          elif r['failed']:
                             vr=r['fail_reason']
                             vfail=True
                       else:
                          import filecmp
                          vx=filecmp.cmp(p1,p2)

                          if not vx:
                             vr='exact match failed'
                             vfail=True

                 if vr!='':
                    if o=='con':
                       ck.out('       - check failed on "'+fz+'" ('+vr+')')

                    vo[fz]={'fail_reason':vr}

             if not vfail and o=='con':
                ck.out('       Validated successfully!')

             # If at least one failed, fail pipeline
             if vfail:
                import json

                misc['run_success']='no'
                misc['run_success_bool']=False
                misc['fail_reason']='output is not matching with the reference one: '+json.dumps(vo,indent=2)

                ccc['run_success']=misc['run_success']
                ccc['run_success_bool']=misc['run_success_bool']
                ccc['fail_reason']=misc['fail_reason']

          else:
             if o=='con':
                ck.out('     * Recording reference output ...')

             # First create / update entry
             potags=meta.get('tags',[])
             if dalias!='': 
                potags.append(dalias)

             if oruoa=='': oruoa='local' # avoid recording to existing repositories rather than local
                                         # unless explictly specified (to avoid pulluting shared project repos)

             ii={'action':'update',
                 'module_uoa':cfg['module_deps']['program.output'],
                 'data_uoa':'program-uid-'+program_output_uoa,
                 'data_name':dalias,
                 'repo_uoa':oruoa,
                 'ignore_update':'yes',
                 'tags':potags}
             r=ck.access(ii)
             if r['return']>0: return r
             pd=r['path']

             if o=='con':
                ck.out('     * Directory with output: '+pd)

             # Create sub-directory to hold correct output
             pd1=os.path.join(pd,po)
             if not os.path.isdir(pd1):
                os.makedirs(pd1)

             for fz in rcof:
                 p1=os.path.join(cdir,fz)
                 p2=os.path.join(pd,po,fz)

                 if not os.path.isfile(p1):
                    return {'return':1, 'error':'reference output file '+fz+' not found!'}

                 shutil.copyfile(p1,p2)

          # Update stats with output check
          svfail='no'
          if vfail: svfail='yes'

          misc['output_check_failed']=svfail
          misc['output_check_failed_bool']=vfail

          ccc['output_check_failed']=svfail
          ccc['output_check_failed_bool']=vfail

          if len(vo)>0:
             misc['output_check_failures']=vo
             ccc['output_check_failures']=vo

       # Output final execution time
       if o=='con' and rt.get('skip_print_execution_time','')!='yes':
          ck.out('')
          x='Execution time: '+('%.3f'%exec_time)+' sec.'
          if repeat>1:
             x+='; Repetitions: '+str(abs(repeat))+'; Normalized execution time: '+('%.9f'%(exec_time/abs(repeat)))+' sec.'
          ck.out(x)


    # Check to clean random directory
    #if grtd=='yes' and sca!='yes':
    #   os.chdir(odir)
    #   try:
    #      shutil.rmtree(cdir, ignore_errors=True)
    #   except Exception as e:
    #      pass

    if misc.get('run_success','')=='no' and o=='con':
       ck.out('')
       ck.out('Program execution likely failed ('+misc.get('fail_reason','')+')!')
       ck.out('')

    return {'return':0, 'tmp_dir':rcdir, 'misc':misc, 'characteristics':ccc, 'deps':deps}

##############################################################################
# clean program work and tmp files

def clean(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    i['sub_action']='clean'
    return process(i)

##############################################################################
# compile program

def compile(i):
    """
    See "process_in_dir" API
    """

    i['sub_action']='compile'
    return process(i)

##############################################################################
# run program

def run(i):
    """
    See "process_in_dir" API
    """

    i['sub_action']='run'
    run_output_dict = process(i)

    if i.get('treat_return_code_as_exit_code', '')=='yes' and run_output_dict.get('return')==0:
        run_output_dict['return']   = run_output_dict['characteristics']['return_code']
        run_output_dict['error']    = run_output_dict['characteristics'].get('fail_reason')

    return run_output_dict

##############################################################################
# prepare and run program pipeline (clean, compile, run, etc)

def pipeline(i):
    """
    Input:  {
              (repo_uoa)             - program repo UOA
              (module_uoa)           - program module UOA
              (data_uoa)             - program data UOA
                 or
              (program_uoa)          - useful if univeral pipeline is used, i.e. ck run pipeline:program program_uoa=...
                 or taken from .cm/meta.json from current directory

              (random)               - if 'yes', random selection of program, cmd, dataset uoa and dataset file
                                       (to support collaborative program optimization)

              (skip_local)           - if 'yes', skip detection of program in a local path

              (program_tags)         - select programs by these tags

              (program_dir)          - force program directory

              (target)               - target machine added via 'ck add machine' with prepared target description
                                       (useful to create farms of machines for crowd-benchmarking and crowd-tuning using CK)

              (host_os)              - host OS (detect, if omitted)
              (target_os)            - OS module to check (if omitted, analyze host)
              (device_id)            - device id if remote (such as adb)

              (local_platform)       - if 'yes', use host_os/target_os from the current platform
                                       (useful when replaying experiments from another machine and even OS)

              (prepare)              - if 'yes', only prepare setup, but do not clean/compile/run program
              (save_to_file)         - if !='', save updated input/output (state) to this file
              (skip_interaction)     - if 'yes' and out=='con', skip interaction to choose parameters

              (skip_device_init)     - if 'yes', skip device init
              (skip_info_collection) - if 'yes', skip info collection

              (skip_device_info)     - if 'yes', skip any device info -
                                       useful to prepare experiment crowdsourcing packs for remote devices

                 Pipeline sections' settings:

              (compute_platform_id)  - if !='', set env['CK_COMPUTE_PLATFORM_ID']
              (compute_device_id)    - if !='', set env['CK_COMPUTE_DEVICE_ID']

              (no_platform_features)    - if 'yes', do not collect full platform features
              (no_dataset_features)     - if 'yes', do not search and extract data set features
              (no_clean)                - if 'yes', do not clean directory before compile/run
              (no_compile)              - if 'yes', do not compile program (useful when running the same program
                                           under different system state conditions: CPU/GPU freq, cache/bus contentions, etc)
              (compile_only_once)       - if 'yes', compile only at first iteration
              (no_compiler_description) - if 'yes', do not search for most close compiler description with flags ...
              (no_run)                  - if 'yes', do not run program
                                             useful when using autotuning to find bugs in compiler,
                                             or find differently generated code sequencies, etc ...
              (no_state_check)          - do not check system/CPU state (frequency) over iterations ...


              (generate_rnd_tmp_dir) - if 'yes', compile and run program in randomly generated temporal dir
                      or
              (tmp_dir)              - if !='', use this tmp_dir

              (skip_clean_after)     - if 'yes', do not remove run batch
              (keep)                 - the same as skip_clean_after

              (console)              - if 'yes', output from program goes to console rather than file
                                          (usually for testing/demos)

              (cmd_key)              - CMD key
              (cmd_keys)             - Select only from this list of available CMD keys

              (dataset_uoa)          - UOA of a dataset
              (dataset_file)         - dataset filename (if more than one inside one entry - suggest to have a UID in name)
              (extra_dataset_tags)   - list of extra data set tags (useful to set "small" during mobile phone crowdtuning)

              (compiler_env_uoa)     - env of a compiler

              (compile_type)         - static or dynamic (dynamic by default;
                                         however takes compiler default_compile_type into account)
                  or
              (static or dynamic)

              (compiler_description_uoa)    - compiler description UOA (module compiler),
                                              if not set, there will be an attempt to detect the most close
                                              by version

              (compiler_vars)        - dict with set up compiler flags (-Dvar=value) ->
                                       they will update the ones defined as default in program description ...

              (no_vars)              - skip compiler vars (if you want to use default ones from the sources) ...

              (remove_compiler_vars) - list of compiler vars to remove

              (extra_env_for_compilation) - set environment variables before compiling program

              (flags)                - compile flags
              (lflags)               - link flags

              (compiler_flags)       - dict from compiler description (during autotuning),
                                       if set, description should exist in input:choices_desc#compiler_flags# ...

              (best_base_flag)       - if 'yes', try to select best flag if available ...
              (speed)                - the same as above
              (skip_best_base_flag)  - if 'yes', do not use best base flag (useful for exploration of other levels -O2,-O1,etc)
              (env_speed)            - use environment flag for best optimization (CK_OPT_SPEED)

              (shared_solution_cid)  - CID-UID1-UID2 of the shared optimization solution at cKnowledge.org/repo
                                       You can find it by clicking on a "Copy CID to clipboard" button of a given solution.
                                       See example at http://cknowledge.org/repo/web.php?wcid=8289e0cf24346aa7:79bca2b76876b5c6
                                       27bc42ee449e880e:79bca2b76876b5c6-8289e0cf24346aa7-f49649288ab0accd

              (Ocid-uid1-uid2)         Substituting compiler -Ox levels with shared solutions in above format
                                       (-O27bc42ee449e880e:79bca2b76876b5c6-8289e0cf24346aa7-f49649288ab0accd)

              (select_best_base_flag_for_first_iteration) - if 'yes' and autotuning_iteration=0


              (env)                  - preset environment
              (env.{KEY})            - set env[KEY]=value (user-friendly interface via CMD)

              (deps.{KEY})           - set deps[KEY]["uoa']=value (user-friendly interface via CMD to set any given dependency)
              (preset_deps)          - dict with {"KEY":"UOA"} to preset dependencies

              (params)               - dictionary with parameters passed via pre/post processing to third-party tools
                                       for example, to configure ARM Workload Automation
              (params.{KEY})         - set params[KEY]=value (user-friendly interface via CMD)

              (extra_env)            - extra environment as string
              (extra_run_cmd)        - extra CMD (can use $#key#$ for autotuning)
              (debug_run_cmd)        - substitute CMD with this one - usually useful for debugging to pre-set env for all deps
              (run_cmd_substitutes)  - dict with substs ($#key#$=value) in run CMD (useful for CMD autotuning)

              (sudo)                 - if 'yes', force using sudo
                                       (otherwise, can use ${CK_SUDO_INIT}, ${CK_SUDO_PRE}, ${CK_SUDO_POST})

              (affinity)             - set processor affinity for tihs program run (if supported by OS - see "affinity" in OS)
                                       examples: 0 ; 0,1 ; 0-3 ; 4-7  (the last two can be useful for ARM big.LITTLE arhictecture

              (repeat)               - repeat kernel via environment CT_REPEAT_MAIN if supported
              (do_not_reuse_repeat)  - if 'yes', do not reuse repeat across iterations - needed for dataset exploration, for example
              (skip_calibration)     - if 'yes', skip execution time calibration (otherwise, make it around 4.0 sec)
              (calibration_time)     - calibration time in string, 4.0 sec. by default
              (calibration_max)      - max number of iterations for calibration, 10 by default

              (statistical_repetition_number) - current statistical repetition of experiment
                                                (for example, may be used to skip compilation, if >0)
              (autotuning_iteration)          - (int) current autotuning iteration (automatically updated during pipeline tuning)
              (the_same_dataset)              - if 'yes', the dataset stays the same across iterations
                                                   so skip copying dataset to remote from 2nd iteration

              (repeat_compilation)     - if 'yes', force compilation, even if "statistical_repetition_number">0

              (cpu_freq)               - set CPU frequency, if supported (using SUDO, if also supported)
                                           using script ck-set-cpu-online-and-frequency
                                         if "max" - try to set to maximum using script ck-set-cpu-performance
                                         if "min" - try to set to minimum using scrupt ck-set-cpu-powersave

              (gpu_freq)               - set GPU frequency, if supported (using SUDO, if also supported)
                                           using script ck-set-gpu-online-and-frequency
                                         if "max" - try to set to maximum using script ck-set-gpu-performance
                                         if "min" - try to set to minimum using scrupt ck-set-gpu-powersave

              (energy)                  - if 'yes', start energy monitoring (if supported) using script ck-set-power-sensors

              (gprof)                   - if 'yes', use gprof to collect profile info
              (perf)                    - if 'yes', use perf to collect hardware counters
              (vtune)                   - if 'yes', use Intel vtune to collect hardware counters
              (sim)                     - if 'yes', use architecture simulator (found by tags "arch","sim")
              (valgrind)                - if 'yes', add valgrind

              (dvdt_prof)               - if 'yes', run program under dividiti's OpenCL profiler
              (mali_hwc)                - if 'yes', attempt to extract MALI GPU hardware counters

              (milepost)                - if 'yes', attempt to extract static program features using Milepost GCC and cTuning CC
              (milepost_out_file)       - if !='', record extracted MILEPOST features to this JSON file

              (compile_timeout)         - (sec.) - kill compile job if too long
              (run_timeout)             - (sec.) - kill run job if too long

              (post_process_script_uoa) - run script from this UOA
              (post_process_subscript)  - subscript name
              (post_process_params)     - (string) add params to CMD

              (dependencies)         - compilation dependencies
              (deps_cache)           - cache with resolved dependencies for reuse (if needed)
              (reuse_deps)           - if 'yes' reuse dependencies
              (force_resolve_deps)   - if 'yes', force resolve deps (useful for crowd-tuning)

              (choices)              - exposed choices (if any)
              (choices_order)        - vector of flattened choices (useful if optimizations need order
                                        such as LLVM or using our GCC plugin iterface to reorder passes,
                                        since 'choices' dict does not have order)

              (features)             - exposed features (if any)

              (characteristics)      - measured characteristics/features/properties (if any)

              (state)                - kept across pipeline iterations (for example, during autotuning/exploration)

                                       (tmp_dir)    - if temporal directory is used, return it
                                                      (useful if randomly generated, to be reused for run or further iterations)
                                       (repeat)     - kernel repeat ...
                                       (features.platform.cpu) - CPU features/properties obtained during iterations
                                                                 to check that state didn't change ...

              (skip_output_validation)        - skip validation of output (dangerous during auto-tuning -
                                                  some optimizations may break semantics or change accuracy)
              (output_validation_repo)        - output validation repo UOA (when recording new output)
              (program_output_uoa)            - use this UOA to check/record program output 
                                                (to have the same output entry for groups of similar programs)

              (overwrite_reference_output)    - if 'yes', overwrite reference output (useful if broken)

              (quiet)                - if 'yes', automatically provide default answer to all questions when resolving dependencies ...

              (last_md5)             - if !='', check if MD5 and fail if didn't change!
              (last_md5_fail_text)   - to recognize that pipeline failure is not really a failure,
                                       but MD5 is the same (useful when pruning compiler flags found
                                       during collaborative autotuning, particularly via mobile devices
                                       (less time to prune results))

              (skip_print_timers)          - if 'yes', skip printing fine-grain timers after execution

              (add_rnd_extension_to_bin)   - if 'yes', add random extension to binary and record list
              (add_save_extension_to_bin)  - if 'yes', add '.save' to bin to save during cleaning ...

              (install_to_env)       - install dependencies to env instead of CK-TOOLS (to keep it clean)!

              (safe)                 - safe mode when searching packages first instead of detecting already installed soft
                                       (to have more deterministic build)

              (skip_exec)            - if 'yes', do not clean output files and skip exec to be able to continue
                                       post-processing during debuging
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              !!! The same as input, but with updated information !!!

              ready        - if 'yes', pipeline is ready (all obligatory choices are set)
                             if 'no', clean/compile/run program is postponed

              state        - should be preserved across autotuning, active (online) learning, exploration, validation iterations
            }

    """

    import os
    import json
    import sys
    import time
    import copy

    o=i.get('out','')
    oo=''
    if o=='con': oo='con'

    pr=i.get('prepare','')
    si=i.get('skip_interaction','')

    if 'state' not in i: i['state']={}
    state=i['state']

    try:
        x=os.getcwd()
    except OSError:
        os.chdir('..')
        x=os.getcwd()

    state['cur_dir']=x

    if 'choices' not in i: i['choices']={}
    choices=i['choices']

    if 'choices_desc' not in i: i['choices_desc']={}
    choices_desc=i['choices_desc']
    choices_order=i.get('choices_order',[])

    if 'features' not in i: i['features']={}
    features=i['features']

    if 'characteristics' not in i: i['characteristics']={}
    chars=i['characteristics']

    if 'dependencies' not in i: i['dependencies']={}
    cdeps=i['dependencies']

    deps_cache=i.get('deps_cache',[])
    reuse_deps=i.get('reuse_deps','')
    ctags = ctags=i.get('compiler_tags','')
    dep_add_tags = i.get('dep_add_tags', {})
    for q in i:
        if q.startswith('dep_add_tags.'):
            _ , dep_name    = q.split('.')
            dep_add_tags[dep_name] = i[q]

    ai=ck.get_from_dicts(i, 'autotuning_iteration', '', None)
    sbbf=ck.get_from_dicts(i, 'select_best_base_flag_for_first_iteration','', None)

    if sbbf=='yes' and ai!='' and ai==0:
       i['best_base_flag']='yes'

    i['ready']='no'
    i['fail']='no'

    ###############################################################################################################
    # PIPELINE SECTION: VARS INIT

    if o=='con':
       ck.out('Initializing universal program pipeline ...')
       ck.out('')

    muoa=work['self_module_uid']

    meta=ck.get_from_dicts(i, 'program_meta', {}, choices) # program meta if needed
    desc=ck.get_from_dicts(i, 'program_desc', {}, choices) # program desc if needed

    quiet=ck.get_from_dicts(i, 'quiet', '', None)

    srn=ck.get_from_dicts(i, 'statistical_repetition_number', '', None)
    if srn=='': srn=0
    else: srn=int(srn)

    ati=ck.get_from_dicts(i, 'autotuning_iteration', '', None)
    if ati=='': ati=0
    else: ati=int(ati)

    last_md5=ck.get_from_dicts(i, 'last_md5', '', None)
    last_md5_fail_text=ck.get_from_dicts(i, 'last_md5_fail_text', '', None)

    random=ck.get_from_dicts(i, 'random', '', None)
    if random=='yes':
       from random import randint
    frd=ck.get_from_dicts(i, 'force_resolve_deps', '', None)

    ruoa=ck.get_from_dicts(i, 'repo_uoa', '', None)
    duoa=ck.get_from_dicts(i, 'data_uoa', '', choices)
    puoa=ck.get_from_dicts(i, 'program_uoa', '', None)
    if puoa!='':
       duoa=puoa
       choices['data_uoa']=duoa
    ptags=ck.get_from_dicts(i, 'program_tags', '', choices)
    kcmd=ck.get_from_dicts(i, 'cmd_key', '', choices)
    kcmds=ck.get_from_dicts(i, 'cmd_keys', [], None)
    dduoa=ck.get_from_dicts(i, 'dataset_uoa', '', choices)
    ddfile=ck.get_from_dicts(i, 'dataset_file', '', choices)
    edtags=ck.get_from_dicts(i, 'extra_dataset_tags', [], choices)
    druoa=ck.get_from_dicts(i, 'dataset_repo_uoa', '', None)

    ceuoa=ck.get_from_dicts(i, 'compiler_env_uoa', '', choices)

    scpuf=ck.get_from_dicts(i, 'cpu_freq', 'max', choices)
    sgpuf=ck.get_from_dicts(i, 'gpu_freq', 'max', choices)
    sme=ck.get_from_dicts(i, 'energy', '', choices)

    gprof=ck.get_from_dicts(i, 'gprof', '', choices)
    sim=ck.get_from_dicts(i, 'sim', '', choices)
    perf=ck.get_from_dicts(i, 'perf', '', choices)
    vtune=ck.get_from_dicts(i, 'vtune', '', choices)
    valgrind=ck.get_from_dicts(i, 'valgrind', '', choices)
    milepost=ck.get_from_dicts(i, 'milepost', '', choices)
    milepost_out_file=ck.get_from_dicts(i, 'milepost_out_file', '', None)

    params=ck.get_from_dicts(i, 'params',{},choices)

    # Check user-friendly env
    for q in list(i.keys()):
        if q.startswith('params.'):
           params[q[7:]]=i[q]
           if 'params' not in choices: choices['params']={}
           choices['parmas'][q[7:]]=i[q]
           del(i[q])

    espeed=ck.get_from_dicts(i, 'env_speed', '', choices)

    iev=ck.get_from_dicts(i, 'install_to_env', '', None)
    safe=ck.get_from_dicts(i, 'safe', '', choices)
    skip_exec=ck.get_from_dicts(i, 'skip_exec', '', None)

    prcmd=''

    pdir=ck.get_from_dicts(i, 'program_dir', '', None) # Do not save, otherwise can't reproduce by other people
    if pdir!='': os.chdir(pdir)

    sdi=i.get('skip_device_init', '')
    sic=i.get('skip_info_collection', '')

    sdf=i.get('skip_device_info', '')

    are=i.get('add_rnd_extension_to_bin', '')
    ase=i.get('add_save_extension_to_bin','')

    grtd=ck.get_from_dicts(i, 'generate_rnd_tmp_dir','', None)
    tdir=ck.get_from_dicts(i, 'tmp_dir','', None)

    sptimers=ck.get_from_dicts(i, 'skip_print_timers','', choices)

    sca=ck.get_from_dicts(i, 'skip_clean_after', '', choices) # I add it here to be able to debug across all iterations
    if sca=='':
       sca=ck.get_from_dicts(i, 'keep', '', choices)

    pp_uoa=ck.get_from_dicts(i, 'post_process_script_uoa','', choices)
    pp_name=ck.get_from_dicts(i, 'post_process_subscript','', choices)
    pp_params=ck.get_from_dicts(i, 'post_process_params', '', choices)

    flags=ck.get_from_dicts(i, 'flags', '', choices)
    lflags=ck.get_from_dicts(i, 'lflags', '', choices)

    sbbfx=ck.get_from_dicts(i, 'skip_best_base_flag', '', choices)

    no_compile=ck.get_from_dicts(i, 'no_compile', '', choices)
    compile_only_once=ck.get_from_dicts(i, 'compile_only_once', '', choices)
    no_run=ck.get_from_dicts(i, 'no_run', '', choices)
    no_state_check=ck.get_from_dicts(i, 'no_state_check', '', choices)

#    env=ck.get_from_dicts(i,'env',{},choices)
#   New handling of env vs choices to merge the properly!
    env=i.get('choices',{}).get('env',{})

    env.update(i.get('env',{}))
    if 'env' in i: del(i['env'])

    # Check user-friendly env and deps
    preset_deps=ck.get_from_dicts(i, 'preset_deps', {}, choices)
    for q in list(i.keys()):
        if q.startswith('env.'):
           env[q[4:]]=i[q]
#           if 'env' not in choices: choices['env']={}
#           choices['env'][q[4:]]=i[q]
           del(i[q])
        elif q.startswith('deps.'):
           preset_deps[q[5:]]=i[q]
           del(i[q])

    choices['env']=env

    eenv=ck.get_from_dicts(i, 'extra_env','',choices)
    ercmd=ck.get_from_dicts(i, 'extra_run_cmd','',choices)
    drcmd=ck.get_from_dicts(i, 'debug_run_cmd','',choices)
    rcsub=ck.get_from_dicts(i, 'run_cmd_substitutes',{},choices)

    if i.get('do_not_reuse_repeat','')=='yes' and srn==0:
       repeat=''
    else:
       repeat=ck.get_from_dicts(i,'repeat','',choices)
       if repeat=='': repeat=state.get('repeat','')

    rsc=ck.get_from_dicts(i, 'skip_calibration','', choices)
    rct=ck.get_from_dicts(i, 'calibration_time','',choices)
    rcm=ck.get_from_dicts(i, 'calibration_max','',choices)

    aff=ck.get_from_dicts(i, 'affinity', '', choices)

    cons=ck.get_from_dicts(i, 'console','',choices)

    tsd=ck.get_from_dicts(i, 'the_same_dataset', '', choices)

    odp=ck.get_from_dicts(i, 'dvdt_prof','',choices)
    mali_hwc=ck.get_from_dicts(i, 'mali_hwc','',choices)

    xcto=ck.get_from_dicts(i, 'compile_timeout','',choices)
    xrto=ck.get_from_dicts(i, 'run_timeout','',choices)

    cdu=ck.get_from_dicts(i, 'compiler_description_uoa','',choices)

    vout_skip=ck.get_from_dicts(i, 'skip_output_validation','',choices)
    vout_repo=ck.get_from_dicts(i, 'output_validation_repo','',choices)
    vout_over=ck.get_from_dicts(i, 'overwrite_reference_output','',choices)
    program_output_uoa=ck.get_from_dicts(i, 'program_output_uoa','',choices)

    compute_platform_id=ck.get_from_dicts(i, 'compute_platform_id','',choices)
    compute_device_id=ck.get_from_dicts(i, 'compute_device_id','',choices)

    ###############################################################################################################
    # PIPELINE SECTION: PROGRAM AND DIRECTORY SELECTION
    #                   (either as CID or CK descrpition from current directory or return that should be selected)

    # First, if duoa is not defined, try to get from current directory
    if len(meta)==0:
       if duoa=='' and i.get('skip_local','')!='yes':
          # First, try to detect CID in current directory
          r=ck.cid({})
          if r['return']==0:
             xruoa=r.get('repo_uoa','')
             xmuoa=r.get('module_uoa','')
             xduoa=r.get('data_uoa','')

             rx=ck.access({'action':'load',
                           'module_uoa':xmuoa,
                           'data_uoa':xduoa,
                           'repo_uoa':xruoa})
             if rx['return']>0: return rx
             xmeta=rx['dict']
             xdesc=rx.get('disc',{})

             if xmeta.get('program','')=='yes':
                duoa=xduoa
                muoa=xmuoa
                ruoa=xruoa
                meta=xmeta
                desc=xdesc

          if duoa=='':
             # Attempt to load configuration from the current directory
             pc=os.path.join(state['cur_dir'], ck.cfg['subdir_ck_ext'], ck.cfg['file_meta'])
             if os.path.isfile(pc):
                r=ck.load_json_file({'json_file':pc})
                if r['return']==0:
                   xmeta=r['dict']
                   if xmeta.get('program','')=='yes':
                      meta=xmeta

             px=os.path.join(state['cur_dir'], ck.cfg['subdir_ck_ext'], ck.cfg['file_desc'])
             if os.path.isfile(px):
                r=ck.load_json_file({'json_file':px})
                if r['return']==0:
                   xdesc=r['dict']

    # Second, if duoa is not detected or defined, prepare selection
    duid=''
    if len(meta)==0:
       if duoa=='': duoa='*'

       r=ck.search({'repo_uoa':ruoa, 'module_uoa':muoa, 'data_uoa':duoa, 'add_info':'yes', 'tags':ptags})
       if r['return']>0: return r

       lst=r['lst']
       if len(lst)==0:
          duoa=''
       elif len(lst)==1:
          duid=lst[0]['data_uid']
          duoa=lst[0]['data_uoa']
       else:
          if random=='yes':
             rb=randint(0,len(lst)-1)

             duid=lst[rb]['data_uid']
             duoa=lst[rb]['data_uoa']
          elif quiet=='yes':
             duid=lst[0]['data_uid']
             duoa=lst[0]['data_uoa']
          else:
             # SELECTOR *************************************
             choices_desc['##program_uoa']={'type':'uoa',
                                            'has_choice':'yes',
                                            'choices':lst,
                                            'tags':['setup'],
                                            'sort':1000}

             if o=='con' and si!='yes':
                ck.out('************ Selecting program/benchmark/kernel ...')
                ck.out('')
                r=ck.select_uoa({'choices':lst})
                if r['return']>0: return r
                duoa=r['choice']
                ck.out('')
             else:
                return finalize_pipeline(i)

    if len(meta)==0 and duoa=='':
       return {'return':1, 'error':'no programs found for this pipeline'}

    if pdir=='' and duoa!='':
       rx=ck.access({'action':'load',
                     'module_uoa':muoa,
                     'data_uoa':duoa,
                     'repo_uoa':ruoa})
       if rx['return']>0: return rx
       if len(meta)==0:
          meta=rx['dict']
       if len(desc)==0:
          desc=rx.get('desc',{})

       pdir=rx['path']
       duid=rx['data_uid']
       duoa=rx['data_uoa']

       # Check if base_uoa suggests to use another program path
       buoa=meta.get('base_uoa','')
       if buoa!='':
          rx=ck.access({'action':'find',
                        'module_uoa':muoa,
                        'data_uoa':buoa})
          if rx['return']>0:
             return {'return':1, 'error':'problem finding base entry '+buoa+' ('+rx['error']+')'}

          pdir=rx['path']

    if pdir=='': pdir=state['cur_dir']

    if duid=='':
        # Write program meta and desc only if no program UID, otherwise can restore from program entry
       i['program_meta']=meta
       i['program_desc']=desc

    if duid=='' and meta.get('backup_data_uid','')!='': duid=meta['backup_data_uid']

    if duoa!='': choices['data_uoa']=duoa
    if muoa!='': choices['module_uoa']=muoa
    # we are not recording repo_uoa for reproducibility (can be different across users) ...

    if o=='con':
       ck.out('  Selected program:          '+duoa+' ('+duid+')')

    ###############################################################################################################
    # PIPELINE SECTION: Host and target platform selection
    # Check via --target first (however, for compatibility, check that module exists first)
    local_platform=i.get('local_platform','')

    r=ck.access({'action':'find',
                 'module_uoa':cfg['module_deps']['module'],
                 'data_uoa':cfg['module_deps']['machine']})
    if r['return']==0 and i.get('skip_target','')!='yes' and local_platform!='yes':
       if o=='con':
          ck.out(sep)
          ck.out('Obtaining platform parameters and checking other obligatory choices for the pipeline ...')
          ck.out('')

#       Original code which was not allowing to reply on a different machine (host/target was overwrited by recorded pipeline)
#       target=i.get('target','')
#       if target=='':
#          target=choices.get('target','')
#          i['target']=target
#       device_cfg=i.get('device_cfg',{})
#       if len(device_cfg)==0: i['device_cfg']=choices.get('device_cfg',{})
#       tos=i.get('target_os','')
#       if tos=='': i['target_os']=choices.get('target_os','')
#       tdid=i.get('device_id','')
#       if tdid=='': i['device_id']=choices.get('device_id','')

       target=i.get('target','')

       if target=='':
          target=choices.get('target','')
          i['target']=target

       r=ck.search({'module_uoa':cfg['module_deps']['machine'], 'data_uoa':target, 'add_meta':'yes'})
       if r['return']>0: return r

       dlst=sorted(r['lst'], key=lambda v: v.get('meta',{}).get('access_type','')!='host')

       # Prune search by only required devices
       rdat=meta.get('required_device_access_type',[])

       lst=[]

       if len(rdat)==0:
          lst=dlst
       else:
          for q in dlst:
              if q.get('meta',{}).get('access_type','') in rdat:
                 lst.append(q)

       if len(lst)==0:
          if len(rdat)>0:
             return {'return':1, 'error':'no target devices found for this pipeline (use "ck add machine")'}
          # otherwide device is not strictly necessary for this program
       elif len(lst)==1:
          i['target']=lst[0]['data_uoa']
       else:
#          FGG remarked it since when many target machines are registered but not connected, often fail ...
#          if random=='yes':
#             rb=randint(0,len(lst)-1)
#
#             i['target']=lst[rb]['data_uoa']
          if quiet=='yes':
             i['target']=lst[0]['data_uoa']
          else:
             # SELECTOR *************************************
             choices_desc['##device_uoa']={'type':'uoa',
                                           'has_choice':'yes',
                                           'choices':lst,
                                           'sort':1}

             if o=='con' and si!='yes':
                ck.out('************ Selecting target device ...')
                ck.out('')

                zz={}
                iz=0
                for z1 in lst:
                    z=z1['data_uid']
                    zu=z1['data_uoa']

                    zs=str(iz)
                    zz[zs]=z

                    ck.out(zs+') '+zu+' ('+z+')')

                    iz+=1

                ck.out('')
                rx=ck.inp({'text':'Select UOA (or press Enter for 0): '})
                x=rx['string'].strip()
                if x=='': x='0'

                if x not in zz:
                   return {'return':1, 'error':'choice is not recognized ('+str(x)+')'}

                target=zz[x]
                i['target']=target

                ck.out('')
             else:
                return finalize_pipeline(i)

       ii={'action':'init',
           'module_uoa':cfg['module_deps']['machine'],
           'input':i}

       if no_run!='yes':
           ii['check']='yes'

       r=ck.access(ii)
       if r['return']>0: return r

       # Update choices if external change in target
       if target!='' and choices.get('target','')!=target: 
          choices['target']=target

          device_cfg=i.get('device_cfg',{})
          if len(device_cfg)!=0: choices['device_cfg']=device_cfg

       hos=i.get('host_os','')
       if hos!='' and choices.get('host_os','')!=hos:
          choices['host_os']=hos

       tos=i.get('target_os','')
       if tos!='' and choices.get('target_os','')!=tos:
          choices['target_os']=tos

       tdid=i.get('device_id','')
       if tdid!='' and choices.get('target_id','')!=tdid:
          choices['target_id']=tdid

    target=ck.get_from_dicts(i, 'target', '', choices)
    device_cfg=ck.get_from_dicts(i, 'device_cfg', {}, choices)

    hos=ck.get_from_dicts(i, 'host_os', '', choices)
    tos=ck.get_from_dicts(i, 'target_os', '', choices)
    tbits=ck.get_from_dicts(i, 'target_os_bits', '', choices)
    tdid=ck.get_from_dicts(i, 'device_id', '', choices)

    # Useful when replaying experiments, to retarget them to a local platform
    if local_platform=='yes':
       target=''
       hos=''
       tos=''
       tdid=''

    # Get some info about platforms
    ox=oo

    if sdf=='yes':
       sdi='yes'
       sic='yes'

    if sdi=='yes' and sic=='yes': ox=''

    ii={'action':'detect',
        'module_uoa':cfg['module_deps']['platform.os'],
        'host_os':hos,
        'target_os':tos,
        'device_id':tdid,
        'device_cfg':device_cfg,
        'skip_device_init':sdi,
        'skip_info_collection':sic,
        'out':ox}
    if si=='yes': ii['return_multi_devices']='yes'
    r=ck.access(ii)
    if r['return']>0:
       if r['return']==32:
          choices_desc['##device_id']={'type':'text',
                                       'has_choice':'yes',
                                       'choices':r['devices'],
                                       'tags':['setup'],
                                       'sort':1000}
          return finalize_pipeline(i)
       return r

    sdi='yes'
    i['skip_device_init']=sdi

    hos=r['host_os_uoa']
    hosd=r['host_os_dict']

    choices['host_os']=hos

    tos=r['os_uoa']
    tosd=r['os_dict']
    tbits=tosd.get('bits','')

    tplat=tosd.get('ck_name','')
    tplat2=tosd.get('ck_name2','')

    hosz=hosd.get('base_uoa','')
    if hosz=='': hosz=hos
    tosz=tosd.get('base_uoa','')
    if tosz=='': tosz=tos

    remote=tosd.get('remote','')

    tdid=r['device_id']
    if tdid!='': choices['device_id']=tdid

    choices['target_os']=tos
    choices['target_os_bits']=tbits

    choices['device_id']=r['device_id']

    if hos=='':
       return {'return':1, 'error':'host_os is not defined'}

    if tos=='':
       return {'return':1, 'error':'target_os is not defined'}

    # Get various OS vars
    rx=ck.get_os_ck({})
    if rx['return']>0: return rx
    hplat=rx['platform']

    bbp=hosd.get('batch_bash_prefix','')
    rem=hosd.get('rem','')
    eset=hosd.get('env_set','')
    etset=tosd.get('env_set','')
    svarb=hosd.get('env_var_start','')
    svarb1=hosd.get('env_var_extra1','')
    svare=hosd.get('env_var_stop','')
    svare1=hosd.get('env_var_extra2','')
    scall=hosd.get('env_call','')
    sdirs=hosd.get('dir_sep','')
    sdirsx=tosd.get('remote_dir_sep','')
    if sdirsx=='': sdirsx=sdirs
    stdirs=tosd.get('dir_sep','')
    sext=hosd.get('script_ext','')
    sexe=hosd.get('set_executable','')
    se=tosd.get('file_extensions',{}).get('exe','')
    sbp=hosd.get('bin_prefix','')
    stbp=tosd.get('bin_prefix','')
    sqie=hosd.get('quit_if_error','')
    evs=hosd.get('env_var_separator','')
    envsep=hosd.get('env_separator','')
    envtsep=tosd.get('env_separator','')
    eifs=hosd.get('env_quotes_if_space','')
    eifsc=hosd.get('env_quotes_if_space_in_call','')
    eifsx=tosd.get('remote_env_quotes_if_space','')
    if eifsx=='': eifsx=eifsc
    wb=tosd.get('windows_base','')
    stro=tosd.get('redirect_stdout','')
    stre=tosd.get('redirect_stderr','')
    ubtr=hosd.get('use_bash_to_run','')
    no=tosd.get('no_output','')

    rof=[] # run output files ...
    eppc='' # extra post process CMD

    # check sudo
    sudo_init=tosd.get('sudo_init','')
    if sudo_init=='': sudo_init=svarb+svarb1+'CK_SUDO_INIT'+svare1+svare
    sudo_pre=tosd.get('sudo_pre','')
    if sudo_pre=='': sudo_pre=svarb+svarb1+'CK_SUDO_PRE'+svare1+svare
#    sudo_post=tosd.get('sudo_post','')
#    if sudo_post=='':
    sudo_post=svarb+svarb1+'CK_SUDO_POST'+svare1+svare

    isd=ck.get_from_dicts(i, 'sudo', '', choices)
    if isd=='': isd=tosd.get('force_sudo','')

    # Check compile type
    ctype=ck.get_from_dicts(i, 'compile_type', '', choices)
    if i.get('static','')=='yes': ctype='static'
    if i.get('dynamic','')=='yes': ctype='dynamic'

    # On default Android-32, use static by default
    # (old platforms has problems with dynamic)
    if ctype=='':
       if tosd.get('default_compile_type','')!='':
          ctype=tosd['default_compile_type']
       else:
          ctype='dynamic'
    choices['compile_type']=ctype

    if o=='con':
       ck.out(sep)
       if target!='':
          ck.out('  Selected target platform:  '+target)
       ck.out('  Selected host platform:    '+hos)
       ck.out('  Selected target platform:  '+tos)
       if tdid!='':
          ck.out('  Selected target device ID: '+tdid)
          ck.out('')

    ###############################################################################################################
    # PIPELINE SECTION: Load deps

    if no_compile!='yes':
       if len(cdeps)==0 or ceuoa!='' or frd=='yes':
          if len(cdeps)==0:
             cdeps=meta.get('compile_deps',{})
          elif frd=='yes':
             xcdeps=cdeps
             cdeps=meta.get('compile_deps',{})
             cdeps.update(xcdeps)

    for q in preset_deps:
        if q in cdeps:
           cdeps[q]['uoa']=preset_deps[q]

    ###############################################################################################################
    # PIPELINE SECTION: Command line selection

    run_cmds=meta.get('run_cmds',{})
    if len(run_cmds)==0:
       return {'return':1, 'error':'no CMD for run'}

    krun_cmds=sorted(list(run_cmds.keys()))
    if len(kcmds)>0:
       krun_cmds=kcmds

    zrt={}
    if kcmd=='':
       if len(krun_cmds)>1:
          if random=='yes':
             rb=randint(0,len(krun_cmds)-1)
             kcmd=krun_cmds[rb]
          elif quiet=='yes':
             kcmd=krun_cmds[0]
          else:
             xchoices=[]
             dchoices=[]
             for z in sorted(run_cmds, key=lambda rcmds:run_cmds[rcmds].get('sort',0)):
                 xchoices.append(z)

                 zrt=run_cmds[z].get('run_time',{})
                 zcmd=zrt.get('run_cmd_main','')
                 dchoices.append(zcmd)

             # SELECTOR *************************************
             choices_desc['##cmd_key']={'type':'text',
                                        'has_choice':'yes',
                                        'choices':xchoices,
                                        'tags':['setup'],
                                        'sort':1100}

             if o=='con' and si!='yes':
                ck.out('************ Selecting command line ...')
                ck.out('')
                r=ck.access({'action':'select_list',
                             'module_uoa':cfg['module_deps']['choice'],
                             'choices':xchoices,
                             'desc':dchoices})
                if r['return']>0: return r
                kcmd=r['choice']
                ck.out('')
             else:
                return finalize_pipeline(i)

       else:
          kcmd=krun_cmds[0]
    else:
       if kcmd not in krun_cmds:
          return {'return':1, 'error':'CMD key "'+kcmd+'" not found in program description'}

    choices['cmd_key']=kcmd

    if o=='con':
       ck.out('  Selected command line:     '+kcmd)

    vcmd=run_cmds[kcmd]

    run_vars = meta.get('run_vars',{}).copy()       # first load ground-level-precedence defaults for all commands
    run_vars.update( vcmd.get('run_vars',{}) )      # then override with higher-precedence defaults for this specific command
    run_vars.update( env )                          # NB: mixing them in only to use as env_to_resolve in this function

    ###############################################################################################################
    # PIPELINE SECTION: expose and resolve run-time deps if needed

    rx=update_run_time_deps({'host_os':hos,
                             'target_os':tos,
                             'target_id':tdid,
                             'deps':cdeps,
                             'deps_cache':deps_cache,
                             'reuse_deps':reuse_deps,
                             'meta':meta,
                             'cmd_key':kcmd,
                             'cmd_meta':vcmd,
                             'out':oo,
                             'install_to_env':iev,
                             'env_for_resolve':run_vars,    # the whole stack (program-wide, command-wide and execution-specific)
                             'dep_add_tags':dep_add_tags,
                             'preset_deps':preset_deps,
                             'safe':safe,
                             'quiet':quiet})
    if rx['return']>0: return rx

    i['dependencies']=cdeps

    ###############################################################################################################
    # PIPELINE SECTION: dataset selection

    dtags=vcmd.get('dataset_tags',[])

    if len(dtags)>0 and len(edtags)>0:
       dtags += edtags

    dmuoa=cfg['module_deps']['dataset']
    dduid=''

    dtags_csv=','.join(dtags)

    if no_run!='yes' and (dduoa!='' or len(dtags)>0):
       if dduoa=='':
          rx=ck.access({'action':'search',
                        'dataset_repo_uoa':druoa,
                        'module_uoa':dmuoa,
                        'tags':dtags_csv,
                        'add_info':'yes'})
          if rx['return']>0: return rx

          lst=rx['lst']

          dataset_choices=[z['data_uid'] for z in lst]

          if len(lst)==0:
             duoa=''
          elif len(lst)==1:
             dduid=lst[0]['data_uid']
             dduoa=lst[0]['data_uoa']
          else:
             if random=='yes':
                rb=randint(0,len(lst)-1)

                dduid=lst[rb]['data_uid']
                dduoa=lst[rb]['data_uoa']
             elif quiet=='yes':
                dduid=lst[0]['data_uid']
                dduoa=lst[0]['data_uoa']
             else:
                # SELECTOR *************************************
                choices_desc['##dataset_uoa']={'type':'uoa',
                                               'has_choice':'yes',
                                               'choices':dataset_choices,
                                               'tags':['setup', 'dataset'],
                                               'sort':1200}

                if o=='con' and si!='yes':
                   ck.out('************ Selecting data set ...')
                   ck.out('')
                   r=ck.access({'action':'select_uoa',
                                'module_uoa':cfg['module_deps']['choice'],
                                'choices':lst})
                   if r['return']>0: return r
                   dduoa=r['choice']
                   ck.out('')
                else:
                   return finalize_pipeline(i)

       if dduoa=='':
          return {'return':1, 'error':'no datasets found for this pipeline'}

    ddmeta={}
    if dduoa!='':
       rx=ck.access({'action':'load',
                     'dataset_repo_uoa':druoa,
                     'module_uoa':dmuoa,
                     'data_uoa':dduoa})
       if rx['return']>0: return rx
       ddmeta=rx['dict']
       dduid=rx['data_uid']
       dduoa=rx['data_uoa']

    if dduoa!='':
       choices['dataset_uoa']=dduoa

       if o=='con':
          ck.out('  Selected data set:         '+dduoa+' ('+dduid+')')

    ###############################################################################################################
    # PIPELINE SECTION: dataset file selection (if more than one in one entry)
    ddfiles=ddmeta.get('dataset_files',[])

    if len(ddfiles)>0:
       choices_desc['##dataset_file']={'type':'text',
                                       'has_choice':'yes',
                                       'choices':ddfiles,
                                       'tags':['setup'],
                                       'sort':1100}

    if ddfile=='':
       if len(ddfiles)==1:
          ddfile=ddfiles[0]
       elif len(ddfiles)>0:
          if random=='yes':
             rb=randint(0,len(ddfiles)-1)
             ddfile=ddfiles[rb]
          elif quiet=='yes':
             ddfile=ddfiles[0]
          else:
             if o=='con' and si!='yes':
                # Check if has description:
                desc_ddfiles=[]
                desc_ddfiles1=ddmeta.get('desc_dataset_files',{})
                for q in ddfiles:
                    x=desc_ddfiles1.get(q,{}).get('name','')
                    if x=='': x=q
                    desc_ddfiles.append(x)

                ck.out('************ Selecting dataset file ...')
                ck.out('')

                r=ck.access({'action':'select_list',
                             'module_uoa':cfg['module_deps']['choice'],
                             'choices':ddfiles,
                             'desc':desc_ddfiles})
                if r['return']>0: return r
                ddfile=r['choice']
                ck.out('')
             else:
                return finalize_pipeline(i)

    choices['dataset_file']=ddfile

    if ddfile!='' and o=='con':
       ck.out('  Selected dataset file:     '+ddfile)

    ###############################################################################################################
    # PIPELINE SECTION: Architecture simulator
    if sim=='yes':
       if o=='con':
          ck.out(sep)
          ck.out('Adding architecture simulator ...')

       if 'arch-sim' not in cdeps:
          cdeps['arch-sim']={'local':'yes', 'tags':'arch,sim'}

    ###############################################################################################################
    # PIPELINE SECTION: Valgrind
    if valgrind=='yes':
       if o=='con':
          ck.out(sep)
          ck.out('Adding valgrind ...')

       if 'tool-valgrind' not in cdeps:
          cdeps['tool-valgrind']={'local':'yes', 'tags':'tool,valgrind'}

    ###############################################################################################################
    # PIPELINE SECTION: resolve compile dependencies
    if ceuoa!='':
       rx=ck.access({'action':'load',
                     'module_uoa':cfg['module_deps']['env'],
                     'data_uoa':ceuoa})
       if rx['return']>0: return rx
       ceuoa=rx['data_uid']

    if no_compile!='yes':
       if len(cdeps)==0 or ceuoa!='' or frd=='yes':
          if len(cdeps)>0:
             if o=='con':
                ck.out(sep)

             if ceuoa!='':
                # clean compiler version, otherwise wrong detection of flags
                if 'compiler_version' in features: del(features['compiler_version'])
                x=cdeps.get('compiler',{})
                if len(x)>0:
                   if 'cus' in x: del(x['cus'])
                   if 'deps' in x: del(x['deps'])
                   x['uoa']=ceuoa
                   cdeps['compiler']=x

             ii={'action':'resolve',
                 'module_uoa':cfg['module_deps']['env'],
                 'host_os':hos,
                 'target_os':tos,
                 'device_id':tdid,
                 'deps':cdeps,
                 'deps_cache':deps_cache,
                 'reuse_deps':reuse_deps,
                 'add_customize':'yes',
                 'quiet':quiet,
                 'install_to_env':iev,
                 'dep_add_tags': dep_add_tags,
                 'safe':safe,
                 'out':oo}

             rx=ck.access(ii)
             if rx['return']>0: return rx

             cdeps=rx['deps'] # Update deps (add UOA)
             i['dependencies']=cdeps

             # Check if multiple compiler choices
             cmpl=cdeps.get('compiler',{}).get('choices',[])
             if len(cmpl)>0 and len(choices_desc.get('##compiler_env_uoa',{}))==0:
                choices_desc['##compiler_env_uoa']={'type':'uoa',
                                                    'has_choice':'yes',
                                                    'choices':cmpl,
                                                    'sort':2000}

       else:
          if o=='con':
             ck.out('  Selected dependencies:     ')
             for dp in cdeps:
                 dpx=cdeps[dp]
                 tags=dpx.get('dict',{}).get('tags',[])
                 x=json.dumps(tags, sort_keys=True)
                 y=dpx.get('uoa','')
                 ck.out('      '+dp+' env = '+y+'; tags = '+x)


    ###############################################################################################################
    # PIPELINE SECTION: Detect compiler version

    if no_compile!='yes' and i.get('no_detect_compiler_version','')!='yes' and len(features.get('compiler_version',{}))==0:
       if no_compile!='yes':
          ii={'sub_action':'get_compiler_version',
              'target':target,
              'target_os':tos,
              'device_id':tdid,
              'host_os':hos,
              'path':pdir,
              'meta':meta,
              'deps':cdeps,
              'deps_cache':deps_cache,
              'reuse_deps':reuse_deps,
              'dep_add_tags': dep_add_tags,
              'generate_rnd_tmp_dir':grtd,
              'tmp_dir':tdir,
              'skip_clean_after':sca,
              'compile_type':ctype,
              'compiler_tags':ctags,
              'flags':flags,
              'lflags':lflags,
              'console':cons,
              'env':env,
              'extra_env':eenv,
              'out':oo}
          r=process_in_dir(ii)

          if r['return']>0: return r

          misc=r['misc']
          if tdir=='': tdir=misc.get('tmp_dir','')
          if tdir!='': state['tmp_dir']=tdir

          features['compiler_version']={'list':misc.get('compiler_detected_ver_list',[]),
                                        'str':misc.get('compiler_detected_ver_str',''),
                                        'raw':misc.get('compiler_detected_ver_raw','')}

    ###############################################################################################################
    # PIPELINE SECTION: get compiler description for flag options
    cflags_desc=choices_desc.get('##compiler_flags',{})

    if no_compile!='yes' and cdu=='' and i.get('no_compiler_description','')!='yes':
       cdt=cdeps.get('compiler',{}).get('dict',{}).get('tags',[])

       # Substitute with real compiler version
       creal=features.get('compiler_version',{}).get('list',[])

       al=[]
       icreal={}
       j=0
       for qi in creal:
           try:
              jj=int(qi)
              icreal[str(j)]=jj
              j+=1
           except Exception:
              break

       if len(icreal)>0:
          al.append(icreal)
          cdt1=[]
          for q in cdt:
              if not q.startswith('v'): cdt1.append(q)

          # Find most close
          ii={'action':'search',
              'module_uoa':cfg['module_deps']['compiler'],
              'add_meta':'yes',
              'tags':'auto'}
          rx=ck.access(ii)
          if rx['return']>0: return rx

          rl=rx['lst']

          xrmax=0 # max tag matches
          xruid=''
          xruoa=''

          for q in rl:
              qdt=q.get('meta',{}).get('tags',[])
              rx=0
              for qi in cdt1:
                  if qi in qdt:
                     rx+=1
              if rx>1:
                 vv=''
                 for qi in qdt:
                     if qi.startswith('v') and len(qi)>len(vv):
                        vv=qi
                 vx=vv[1:].split('.')

                 j=0
                 icreal1={'uid':q['data_uid'], 'uoa':q['data_uoa']}
                 for qi in vx:
                     try:
                        jj=int(qi)
                        icreal1[str(j)]=jj
                        j+=1
                     except Exception:
                        break

                 al.append(icreal1)

          # Sorting
          al1=sorted(al, key=lambda v: (int(v.get('0',0)), int(v.get('1',0)), int(v.get('2',0))))
          jj=0
          for qi in al1:
              if qi.get('uid','')!='':
                 xruid=qi['uid']
                 xruoa=qi['uoa']
              else:
                 # Check if exact match with next one
                 if jj+1<len(al1):
                    qii=al1[jj+1]

                    if qi.get('0',None)==qii.get('0',None) and \
                       qi.get('1',None)==qii.get('1',None) and \
                       (qi.get('2',None)==None or qii.get('2', None)==None or qi.get('2',None)==qii.get('2',None)):
                       xruid=qii['uid']
                       xruoa=qii['uoa']

                 break
              jj+=1

          if xruid=='':
             return {'return':1, 'error':'can\'t find most close compiler description by tags ('+ \
                      json.dumps(cdt1)+') with version '+json.dumps(creal)}

          cdu=xruoa

          if o=='con':
             ck.out('Most close found compiler description: '+xruoa+' ('+xruid+')')
             time.sleep(1)

    if cdu!='':
       choices['compiler_description_uoa']=cdu

       rx=ck.access({'action':'load',
                     'module_uoa':cfg['module_deps']['compiler'],
                     'data_uoa':cdu})
       if rx['return']>0: return rx
       xruid=rx['data_uid']
       rxd=rx['dict']
       rxdd=rx.get('desc',{})

       if o=='con':
          ck.out('')
          ck.out('Loading compiler description: '+cdu+' ('+xruid+') ...')

       if len(cflags_desc)==0:
          cflags_desc=rxdd.get('all_compiler_flags_desc',{})

          for q in cflags_desc:
              qq=cflags_desc[q]
              q1=q
              if q.startswith('##'):q1=q[2:]
              elif q.startswith('#'):q1=q[1:]
              choices_desc['##compiler_flags#'+q1]=qq

    ###############################################################################################################
    # PIPELINE SECTION: get compiler vars choices (-Dvar=value) - often for datasets such as in polyhedral benchmarks
    bcvd=desc.get('build_compiler_vars_desc',{})
    for q in bcvd:
        qq=bcvd[q]
        q1=q
        if q.startswith('##'):q1=q[2:]
        elif q.startswith('#'):q1=q[1:]
        choices_desc['##compiler_vars#'+q1]=qq

    cv=ck.get_from_dicts(i,'compiler_vars',{},choices)
    ncv=ck.get_from_dicts(i,'no_vars',{},choices)
    rcv=ck.get_from_dicts(i,'remove_compiler_vars',[],choices)
    eefc=ck.get_from_dicts(i,'extra_env_for_compilation',{},choices)

    ###############################################################################################################
    # PIPELINE SECTION: compute device if needed

    # Check if need to select GPGPU
    ngd=vcmd.get('run_time',{}).get('need_compute_device','')
    if no_run!='yes' and ngd!='':
        if compute_platform_id=='' and compute_device_id=='':
           if o=='con':
              ck.out('************ Detecting GPGPU targets ...')
              ck.out('')

           xdeps=copy.deepcopy(cdeps)
           ii={'action':'detect',
                        'module_uoa':cfg['module_deps']['platform.gpgpu'],
                        'host_os':hos,
                        'target_os':tos,
                        'device_id':tdid,
                        'type':ngd,
                        'deps':xdeps,
                        'select':'yes',
                        'sudo':isd,
                        'out':oo,
                        'quiet':quiet}
           if target!='': ii['target']=target
           r=ck.access(ii)
           if r['return']>0: return r

           gpgpu_num=r.get('choices',{}).get('compute_number',0)
           gpgpu_ft=r.get('features',{}).get('gpgpu',[])
           if gpgpu_num<len(gpgpu_ft):
              features['gpgpu']=gpgpu_ft[gpgpu_num]

           compute_platform_id=r.get('choices',{}).get('compute_platform_id','')
           compute_device_id=r.get('choices',{}).get('compute_device_id','')

           choices['compute_platform_id']=compute_platform_id
           choices['compute_device_id']=compute_device_id

    ###############################################################################################################
    # PIPELINE SECTION: get run vars (preset environment)
    rv=desc.get('run_vars_desc',{})
    for q in rv:
        qq=rv[q]
        q1=q
        if q.startswith('##'):q1=q[2:]
        elif q.startswith('#'):q1=q[1:]
        choices_desc['##env#'+q1]=qq

#    env=ck.get_from_dicts(i,'env',{},choices)

    ###############################################################################################################
    # PIPELINE SECTION: Check remote solution
    for k in i:
        if k.startswith('O'):
           i['shared_solution_cid']=k[1:]
           del(i[k])
           break
    scid=ck.get_from_dicts(i, 'shared_solution_cid', '', choices)

    if scid!='':
       if o=='con':
          ck.out(sep)
          ck.out('Attempting to load shared solution ('+scid+') ...')
          ck.out('')

       xsuid1=''
       xsuid2=''
       j=scid.find('-')
       if j>0:
          xscid=scid[j+1:].split('-')
          xsuid1=xscid[0]
          if len(xscid)>1:
             xsuid2=xscid[1]

          scid=scid[:j]

       rx=ck.parse_cid({'cid':scid})
       if rx['return']>0: return rx

       xsruoa=rx.get('repo_uoa','')
       xsmuoa=rx.get('module_uoa','')
       xsduoa=rx.get('data_uoa','')

       if xsruoa=='': xsruoa=ck.cfg['default_exchange_repo_uoa']

       ii={'action':'get',
           'module_uoa':xsmuoa,
           'repo_uoa':xsruoa,
           'scenario_module_uoa':xsuid1,
           'solution_uid':xsuid2,
           'data_uoa':xsduoa}
       rz=ck.access(ii)
       if rz['return']>0: return rz

       sols=rz['solutions']

       if len(sols)==0:
          return {'return':1, 'error':'no shared solutions found'}

       if len(sols)>1:
          return {'return':1, 'error':'ambiguity - more than 1 shared solution found'}

       xsp=sols[0].get('points',[])

       if len(xsp)==0:
          return {'return':1, 'error':'no optimization points found in a shared solution'}

       if len(xsp)>1:
          return {'return':1, 'error':'ambiguity - more than 1 optimization point found in a shared solution'}

       xpruned_choices=xsp[0].get('pruned_choices',{})
       xpruned_choices_order=xsp[0].get('pruned_choices_order',[])

       # Rebuild choices!
       for k in xpruned_choices_order:
           if k in xpruned_choices:
              if k not in choices_order:
                 choices_order.append(k)
              v=xpruned_choices[k]

              rx=ck.set_by_flat_key({'dict':choices, 'key':k, 'value':v})
              if rx['return']>0: return rx

       ck.out('')
       ck.out('Successfully pre-loaded solution choices and orders to program pipeline!')

    ###############################################################################################################
    # Pipeline ready for compile/run
    i['ready']='yes'
    if pr=='yes':
       return finalize_pipeline(i)

    ###############################################################################################################
    # Restore compiler flag selection with order for optimization reordering (!)
    # Simplified - needs to be improved for more complex cases (dict of dict)
    compiler_flags=ck.get_from_dicts(i, 'compiler_flags', {}, choices)

    # Check if use best base flag
    bbf=''

    if sbbfx!='yes':
       bbf=ck.get_from_dicts(i, 'best_base_flag', '', None)
       if bbf=='':
          bbf=ck.get_from_dicts(i, 'speed', '', None)
       if bbf=='yes':
          qx=choices_desc.get('##compiler_flags#base_opt',{}).get('choice',[])
          if len(qx)>0:
             compiler_flags['base_opt']=qx[0]
             if '##compiler_flags#base_opt' not in choices_order:
                choices_order.insert(0,'##compiler_flags#base_opt')

    for q in compiler_flags:
        if '##compiler_flags#'+q not in choices_order:
           choices_order.append('##compiler_flags#'+q)

    iflags=0 # number of selected compiler flags (only from choices - can minimize too)
    if len(compiler_flags)>0:
       # Check if compiler flags are not in order (to set some order for reproducibility)
       # At the same time clean up choices_order with non-used flags
       compiler_flags_used={}
       for q in choices_order:
           if q.startswith('##compiler_flags#'):
              qk=q[17:]
              if qk in compiler_flags:
                 qq=compiler_flags[qk]
                 if qq!=None and qq!='':
                    compiler_flags_used[qk]=qq
                    if flags!='': flags+=' '
                    flags+=str(qq)
                    iflags+=1
       compiler_flags=compiler_flags_used

    # to be able to properly record info
    choices['compiler_flags']=compiler_flags
    features['number_of_selected_compiler_flags']=iflags

    ###############################################################################################################
    # PIPELINE SECTION: use gprof for profiling
    gprof_tmp=''
    if gprof=='yes':
       if o=='con':
          ck.out(sep)
          ck.out('Adding gprof compilation flag ...')
          ck.out('')

       flags=svarb+svarb1+'CK_COMPILER_FLAG_GPROF'+svare1+svare+' '+flags
       lflags=svarb+svarb1+'CK_COMPILER_FLAG_GPROF'+svare1+svare+' '+lflags

       if cfg['gprof_file'] not in rof: rof.append(cfg['gprof_file'])

       rx=ck.gen_tmp_file({'prefix':'tmp-', 'remove_dir':'yes'})
       if rx['return']>0: return rx
       gprof_tmp=rx['file_name']

       eppc+='\n'+svarb+svarb1+'CK_PROFILER'+svare1+svare+' $#BIN_FILE#$ > '+gprof_tmp

    ###############################################################################################################
    # PIPELINE SECTION: set CPU frequency
    if scpuf!='' and sic!='yes':
       if o=='con':
          ck.out(sep)
          ck.out('Setting CPU frequency to '+str(scpuf)+' (if supported) ...')
          ck.out('')

       env['CK_CPU_FREQUENCY']=scpuf

       ii={'action':'set_freq',
           'module_uoa':cfg['module_deps']['platform.cpu'],
           'value':scpuf,
           'host_os':hos,
           'target':target,
           'target_os':tos,
           'device_id':tdid,
           'skip_print_os':'yes',
           'skip_device_init':sdi,
           'skip_info_collection':sic,
           'env':env,
           'out':oo}
       r=ck.access(ii)
       if r['return']>0: return r

    ###############################################################################################################
    # PIPELINE SECTION: set GPU frequency
    if sgpuf!='' and sic!='yes':
       if o=='con':
          ck.out(sep)
          ck.out('Setting GPU frequency to '+str(sgpuf)+' (if supported) ...')
          ck.out('')

       env['CK_GPU_FREQUENCY']=sgpuf

       ii={'action':'set_freq',
           'module_uoa':cfg['module_deps']['platform.gpu'],
           'value':sgpuf,
           'host_os':hos,
           'target':target,
           'target_os':tos,
           'device_id':tdid,
           'skip_print_os':'yes',
           'skip_device_init':sdi,
           'skip_info_collection':sic,
           'env':env,
           'out':oo}
       r=ck.access(ii)
       if r['return']>0: return r

    ###############################################################################################################
    # PIPELINE SECTION: get target platform features
    npf=i.get('no_platform_features','')
    if i.get('platform_features','')!='yes' and npf!='yes' and sic!='yes':
       if o=='con':
          ck.out(sep)
          ck.out('Detecting all target platform features ...')
          ck.out('')

       # Get some info about platforms
       ii={'action':'detect',
           'module_uoa':cfg['module_deps']['platform'],
           'target':target,
           'host_os':hos,
           'target_os':tos,
           'device_id':tdid,
           'skip_print_os':'yes',
           'skip_device_init':sdi,
           'skip_info_collection':sic,
           'out':oo}
       r=ck.access(ii)
       if r['return']>0: return r

       features['platform']=r.get('features',{})
       i['platform_features']='yes'
       i['skip_info_collection']='yes'

    ###############################################################################################################
    # PIPELINE SECTION: get dataset features
    npf=i.get('no_dataset_features','')
    if npf!='yes' and dduid!='':
       if o=='con':
          ck.out(sep)
          ck.out('Checking dataset features for '+dduoa+' ('+dduid+') ...')
          ck.out('')

       dsf=features.get('dataset',{})
       dsf1={}

       # Get some info about platforms (the same id as program UID)
       ii={'action':'load',
           'repo_uoa':druoa,
           'module_uoa':cfg['module_deps']['dataset.features'],
           'data_uoa':dduid}
       r=ck.access(ii)
       if r['return']>0:
          if r['return']==16:
             # Try to extract
             if o=='con':
                ck.out(sep)
                ck.out('Trying to extract dataset features ...')
                ck.out('')

             ii['tags']=dtags_csv
             ii['action']='extract'
             ii['out']=oo
             r=ck.access(ii)
             if r['return']==0:
                dsf1=r['dict'].get('features',{})

          # Ignore errors
       else:
          dsf1=r['dict'].get('features',{})

       if len(dsf1)>0 and o=='con':
          ck.out('Features found:')
          ck.out('  '+json.dumps(dsf1))

       dsf.update(dsf1)
       features['dataset']=dsf

    ###############################################################################################################
    # PIPELINE SECTION: Check that system state didn't change (frequency)
    if no_state_check!='yes':
       if o=='con': ck.out(sep)

       ii={'action':'detect',
           'module_uoa':cfg['module_deps']['platform.cpu'],
           'target':target,
           'host_os':hos,
           'target_os':tos,
           'device_id':tdid,
           'skip_print_os_info':'yes',
           'skip_device_init':sdi,
           'skip_info_collection':sic,
           'out':oo} # skip here since it's second time ...
       r=ck.access(ii)
       if r['return']==0:
          xft=r.get('features',{})
          xft1=xft.get('cpu',{})
          xft2=xft.get('cpu_misc',{})
          features['platform.cpu']=xft

          freq1=xft1.get('current_freq',{})
          chars['current_freq']=freq1

          sft=state.get('features.platform.cpu',{})
          if len(sft)==0 or (srn==0 and ati==0):
             state['features.platform.cpu']=xft1
          else:
             freq2=sft.get('current_freq',{})

             if o=='con':
                ck.out('')
                ck.out('Checking CPU frequency:')
                ck.out('')
                ck.out('  Now:    '+json.dumps(freq1, sort_keys=True))
                ck.out('         vs')
                ck.out('  Before: '+json.dumps(freq2, sort_keys=True))
                ck.out('')

             equal=True
             for icpu in freq2:
                 if icpu not in freq1:
                    equal=False
                    break
                 ff1=float(freq1[icpu])
                 ff2=float(freq2[icpu])
                 if ff2!=0:
                    diff=ff1/ff2
                 else:
                    equal=False
                    break
                 if diff<0.98 or diff>1.02:
                    equal=False
                    break

             if not equal:
                if o=='con':
                   ck.out('CPU frequency changed over iterations:')
                   ck.out('')
                i['fail_reason']='frequency changed during experiments'
                i['fail']='yes'
             else:
                ck.out('CPU frequency did not change ...')
                ck.out('')

    ###############################################################################################################
    # PIPELINE SECTION: Extract cTuning/MILEPOST static program features
    cs='yes'
    extracted_milepost_features=False
    if i.get('fail','')!='yes' and milepost=='yes' and \
       (compile_only_once!='yes' or ai==0) and \
       (srn==0 or (srn>0 and i.get('repeat_compilation','')=='yes')):
       if o=='con':
          ck.out(sep)
          ck.out('Extract MILEPOST/cTuning static program features ...')
          ck.out('')

       # Check that milepost repo exists
       rmil=ck.access({'action':'load',
                       'module_uoa':cfg['module_deps']['repo'],
                       'data_uoa':cfg['repo_deps']['reproduce-milepost-project']})
       if rmil['return']>0:
          if rmil['return']!=16: return rmil

          # Suggest to install MILEPOST repo
          if o=='con':
             rx=ck.inp({'text':'You need CK repo "reproduce-milepost-project" to extract static features. Install (Y/n)? '})
             x=rx['string'].strip().lower()
             ck.out('')

             if x!='n':
                ck.out(sep)
                rmil=ck.access({'action':'pull',
                                'module_uoa':cfg['module_deps']['repo'],
                                'data_uoa':'reproduce-milepost-project',
                                'out':'con'})
                if rmil['return']>0: return rmil
                ck.out(sep)

       # Set milepost tag to compiler deps
       mcdeps=copy.deepcopy(cdeps)
       mcdeps['compiler']={
        "local": "yes",
        "sort": 1,
        "tags": "compiler,lang-c,ctuning-cc"}

       mflags=flags
       if mflags!='': mflags+=' '
       mflags='-O3 --ct-extract-features'

       cl=i.get('clean','')
       if cl=='' and i.get('no_clean','')!='yes' and skip_exec!='yes' and srn==0: cl='yes'

       if meta.get('no_compile','')!='yes' and no_compile!='yes':
          if o=='con' and cl=='yes':
             ck.out('Cleaning working directory ...')
             ck.out('')

          ii={'sub_action':'compile',
              'target':target,
              'target_os':tos,
              'device_id':tdid,
              'host_os':hos,
              'path':pdir,
              'meta':meta,
              'deps':mcdeps,
              'deps_cache':deps_cache,
              'reuse_deps':reuse_deps,
              'generate_rnd_tmp_dir':grtd,
              'tmp_dir':tdir,
              'clean':cl,
              'skip_clean_after':sca,
              'compile_type':ctype,
              'flags':mflags,
              'lflags':lflags,
              'statistical_repetition':srn,
              'autotuning_iteration':ati,
              'console':cons,
              'env':env,
              'extra_env':eenv,
              'compiler_vars':cv,
              'no_vars':ncv,
              'remove_compiler_vars':rcv,
              'extra_env_for_compilation':eefc,
              'compile_timeout':xcto,
              'speed':espeed,
              'add_rnd_extension_to_bin':are,
              'add_save_extension_to_bin':ase,
              'out':oo}

          r=process_in_dir(ii)
          if r['return']>0: return r

          misc=r['misc']
          tdir=misc.get('tmp_dir','')

          cs=misc.get('compilation_success','')
          if cs=='no':
             x='MILEPOST feature extraction failed'
             if misc.get('fail_reason','')!='': x+=' - '+misc['fail_reason']
             i['fail_reason']=x
             i['fail']='yes'

          # Process features
          if o=='con' and cl=='yes':
             ck.out('')
             ck.out('Converting MILEPOST/cTuning features to JSON ...')
             ck.out('')

          feat={}

          x1=os.path.join(pdir, tdir)
          x=os.listdir(x1)
          for y in x:
              if os.path.isfile(y) and y.startswith('ici_features_function.') and y.endswith('.fre.ft'):
                 fun=y[22:-7]
                 feat1={}

                 rz=ck.load_text_file({'text_file':y})
                 if rz['return']==0:
                    x2=rz['string'].strip().split(',')
                    for z in x2:
                        z1=z.split('=')
                        if len(z1)>1:
                           zk=z1[0].strip()[2:]
                           zv=z1[1].strip()
                           feat1[zk]=float(zv)

                 feat[fun]=feat1

          features['program_static_milepost_features']=feat

          extracted_milepost_features=True

    ###############################################################################################################
    # PIPELINE SECTION: Compile program
    cs='yes'
    if i.get('fail','')!='yes' and no_compile!='yes' and \
       (compile_only_once!='yes' or ai==0) and \
       (srn==0 or (srn>0 and i.get('repeat_compilation','')=='yes')):
       if o=='con':
          ck.out(sep)
          ck.out('Compile program ...')
          ck.out('')

       cl=i.get('clean','')
       if cl=='' and i.get('no_clean','')!='yes' and skip_exec!='yes' and srn==0: cl='yes'

       if meta.get('no_compile','')!='yes' and no_compile!='yes':
          if o=='con' and cl=='yes':
             ck.out('Cleaning working directory ...')
             ck.out('')

          ii={'sub_action':'compile',
              'target':target,
              'target_os':tos,
              'device_id':tdid,
              'host_os':hos,
              'path':pdir,
              'meta':meta,
              'deps':cdeps,
              'generate_rnd_tmp_dir':grtd,
              'tmp_dir':tdir,
              'clean':cl,
              'skip_clean_after':sca,
              'compile_type':ctype,
              'flags':flags,
              'lflags':lflags,
              'statistical_repetition':srn,
              'autotuning_iteration':ati,
              'console':cons,
              'env':env,
              'speed':espeed,
              'params':params,
              'extra_env':eenv,
              'compiler_vars':cv,
              'no_vars':ncv,
              'remove_compiler_vars':rcv,
              'extra_env_for_compilation':eefc,
              'compile_timeout':xcto,
              'compute_platform_id':compute_platform_id,
              'compute_device_id':compute_device_id,
              'add_rnd_extension_to_bin':are,
              'add_save_extension_to_bin':ase,
              'out':oo}
          r=process_in_dir(ii)
          if r['return']>0: return r

          misc=r['misc']

          if 'add_to_state' in misc:
              state.update(misc['add_to_state'])
              del(misc['add_to_state'])
          if 'add_to_features' in misc:
              features.update(misc['add_to_features'])
              del(misc['add_to_features'])
          if 'add_to_choices' in misc:
              choices.update(misc['add_to_choices'])
              del(misc['add_to_choices'])

          tdir=misc.get('tmp_dir','')
          if tdir!='': state['tmp_dir']=tdir

          cch=r['characteristics']
          cch['joined_compiler_flags']=flags # Add joint compilation flags as string from previous sections
          chars['compile']=cch

          xct=cch.get('compilation_time',-1)
          xos=cch.get('obj_size',-1)

          cs=misc.get('compilation_success','')
          if cs=='no':
             x='compilation failed'
             if misc.get('fail_reason','')!='': x+=' - '+misc['fail_reason']
             i['fail_reason']=x
             i['fail']='yes'

          if last_md5!='':
             md5=cch.get('md5_sum','')
             if md5!='' and md5==last_md5:
                i['fail_reason']=last_md5_fail_text
                i['fail']='yes'

          texe=misc.get('target_exe','')
          state['target_exe']=texe

    ###############################################################################################################
    # PIPELINE SECTION: check if record MILEPOST features (after clean)
    if extracted_milepost_features and milepost_out_file!='':
       r=ck.save_json_to_file({'json_file':milepost_out_file, 'dict':feat})
       if r['return']>0: return r

    ###############################################################################################################
    # PIPELINE SECTION: Check if dataset is the same
    sdc='no'
    if tsd=='yes' and (ati!=0 or srn!=0):
       sdc='yes'

    ###############################################################################################################
    # PIPELINE SECTION: perf
    perf_tmp=''
    if perf=='yes':
       if o=='con':
          ck.out(sep)
          ck.out('Preparing perf ...')

       rx=ck.gen_tmp_file({'prefix':'tmp-', 'remove_dir':'yes'})
       if rx['return']>0: return rx
       perf_tmp=rx['file_name']

       prcmd+='perf stat -x, -o '+perf_tmp

       if perf_tmp not in rof: rof.append(perf_tmp)

    ###############################################################################################################
    # PIPELINE SECTION: Intel vTune
    vtune_tmp=''
    vtune_tmp1=''
    if vtune=='yes':
       if o=='con':
          ck.out(sep)
          ck.out('Preparing vtune ...')

       if 'vtune_profiler' not in cdeps:
          cdeps['vtune_profiler']={'local':'yes', 'tags':'perf,intel,vtune'}

       if hplat=='win':
          eenv='\nrd /S /Q r000\n'+eenv
       else:
          eenv='\nrm -rf r000\n'+eenv

       prcmd+='amplxe-runss -r r000 -event-based-counts --'

       rx=ck.gen_tmp_file({'prefix':'tmp-', 'remove_dir':'yes'})
       if rx['return']>0: return rx
       vtune_tmp=rx['file_name']
       vtune_tmp1=vtune_tmp+'.csv'

       if vtune_tmp1 not in rof: rof.append(vtune_tmp1)

       eppc+='\namplxe-cl -report hw-events -r r000 -report-output='+vtune_tmp+' -format csv -csv-delimiter=comma -filter module=$#ONLY_BIN_FILE#$'

    ###############################################################################################################
    # PIPELINE SECTION: Preload dividiti's OpenCL profiler.
    if odp=='yes':
       if hplat=='win':
          return {'return':1, 'error':'dividiti\'s OpenCL profiler is currently not supported under Windows'}

       if 'dvdt_prof' not in cdeps:
          cdeps['dvdt_prof']={'local':'yes', 'tags':'tool,opencl,dvdt,prof,dvdt-prof2'}

       eenv='export LD_PRELOAD="${CK_ENV_TOOL_DVDT_PROF_DYNAMIC_NAME_FULL}"; '+eenv

       fodp='tmp-dvdt-prof-output.json'
       if os.path.isfile(fodp): os.remove(fodp)

    ###############################################################################################################
    # PIPELINE SECTION: Set MALI HWC counter collector
    if mali_hwc=='yes':
       # Call process output vector
       r=ck.access({'action':'run', 
                    'module_uoa':cfg['module_deps']['script'], 
                    'data_uoa': cfg['data_deps']['mali_hwc'], #'mali-hwc', 
                    'code':'process', 
                    'func':'config'})
       if r['return']>0: 
          return {'return':r['return'], 'error':'Problem with MALI HWC script ('+r['error']+')'}

    ###############################################################################################################
    # PIPELINE SECTION: Valgrind
    if valgrind=='yes':
       if o=='con':
          ck.out(sep)
          ck.out('Adding valgrind ...')

       x=cdeps['tool-valgrind'].get('cus',{}).get('cmd_prefix',{}).get(tplat,'')
       if x=='':
          return {'return':1, 'error':'command line for architecture simulator is not defined'}

       prcmd+=x

    ###############################################################################################################
    # PIPELINE SECTION: Architecture simulator
    if sim=='yes':
       if o=='con':
          ck.out(sep)
          ck.out('Adding architecture simulator ...')

       x=cdeps['arch-sim'].get('cus',{}).get('cmd_prefix',{}).get(tplat,'')
       if x=='':
          return {'return':1, 'error':'command line for architecture simulator is not defined'}

       prcmd+=x

    ###############################################################################################################
    # PIPELINE SECTION: Run program
    xdeps={}
    if i.get('fail','')!='yes' and cs!='no' and no_run!='yes':
       if o=='con':
          ck.out(sep)
          ck.out('Running program ...')

       # Remove some keys from env
       if meta.get('skip_remove_run_env_keys','')!='yes':
          for k in list(env.keys()):
              if k.startswith('CK_AR_') or k.startswith('CK_CC_') or \
                 k.startswith('CK_CXX_') or k.startswith('CK_CMAKE_') or \
                 k.startswith('CK_COMPILER_') or k.startswith('CK_LINKER_'):
                 del(env[k])

       # Check run cmd keys subst
       for k in choices:
           if k.startswith('run_cmd_key_'):
              rcsub[k]=choices[k]

       ii={'sub_action':'run',
           'target':target,
           'target_os':tos,
           'device_id':tdid,
           'host_os':hos,
           'path':pdir,
           'console':cons,
           'meta':meta,
           'deps':cdeps,
           'deps_cache':deps_cache,
           'reuse_deps':reuse_deps,
           'cmd_key':kcmd,
           'dataset_uoa':dduoa,
           'dataset_file':ddfile,
           'generate_rnd_tmp_dir':grtd,
           'tmp_dir':tdir,
           'skip_clean_after':sca,
           'compile_type':ctype,
           'speed':espeed,
           'sudo':isd,
           'energy':sme,
           'affinity':aff,
           'flags':flags,
           'lflags':lflags,
           'repeat':repeat,
           'pre_run_cmd':prcmd,
           'run_output_files':rof,
           'skip_calibration':rsc,
           'calibration_time':rct,
           'calibration_max':rcm,
           'params':params,
           'post_process_script_uoa':pp_uoa,
           'post_process_subscript':pp_name,
           'post_process_params':pp_params,
           'statistical_repetition':srn,
           'autotuning_iteration':ati,
           'compute_platform_id':compute_platform_id,
           'compute_device_id':compute_device_id,
           'skip_output_validation':vout_skip,
           'output_validation_repo':vout_repo,
           'program_output_uoa':program_output_uoa,
           'overwrite_reference_output':vout_over,
           'skip_dataset_copy':sdc,
           'skip_exec':skip_exec,
           'env':env,
           'extra_env':eenv,
           'extra_run_cmd':ercmd,
           'debug_run_cmd':drcmd,
           'extra_post_process_cmd':eppc,
           'run_cmd_substitutes':rcsub,
           'compiler_vars':cv,
           'no_vars':ncv,
           'skip_print_timers':sptimers,
           'remove_compiler_vars':rcv,
           'extra_env_for_compilation':eefc,
           'run_timeout':xrto,
           'out':oo}
       r=process_in_dir(ii)
       if r['return']>0: return r

       misc=r['misc']

       if 'add_to_state' in misc:
           state.update(misc['add_to_state'])
           del(misc['add_to_state'])
       if 'add_to_features' in misc:
           features.update(misc['add_to_features'])
           del(misc['add_to_features'])
       if 'add_to_choices' in misc:
           choices.update(misc['add_to_choices'])
           del(misc['add_to_choices'])

       tdir=misc.get('tmp_dir','')
       if tdir!='': state['tmp_dir']=tdir

       rch=r['characteristics']
       chars['run']=rch

       xdeps=r.get('deps',{})
       if len(xdeps)>0:
          if 'dependencies' not in i:
             i['dependencies']={}
          i['dependencies'].update(xdeps)

       csuc=misc.get('calibration_success',True)
       rs=misc.get('run_success','')
       rsf=misc.get('fail_reason','')

       repeat=rch.get('repeat','')
       if repeat!='':
          state['repeat']=repeat
          choices['repeat']=repeat

       if rs=='no' or not csuc:
          x='execution failed'
          if rsf!='': x+=' - '+rsf
          i['fail_reason']=x
          i['fail']='yes'

    ###############################################################################################################
    # PIPELINE SECTION: set CPU frequency to ondemand to "calm" system (if supported)
    if scpuf!='' and sic!='yes':
        if o=='con':
           ck.out(sep)
           ck.out('Attempting to set CPU frequency to ondemand to "calm" system (if supported) ...')
           ck.out('')

        ii={'action':'set_freq',
            'module_uoa':cfg['module_deps']['platform.cpu'],
            'value':'ondemand',
            'target':target,
            'host_os':hos,
            'target_os':tos,
            'device_id':tdid,
            'skip_print_os':'yes',
            'skip_device_init':sdi,
            'skip_info_collection':sic,
            'out':oo}
        r=ck.access(ii)
        if r['return']>0: return r

    ###############################################################################################################
    # PIPELINE SECTION: set GPU frequency to ondemand to "calm" system (if supported)
    if sgpuf!='' and sic!='yes':
        if o=='con':
           ck.out(sep)
           ck.out('Attempting to set GPU frequency to ondemand to "calm" system (if supported) ...')
           ck.out('')

        ii={'action':'set_freq',
            'module_uoa':cfg['module_deps']['platform.gpu'],
            'value':'ondemand',
            'target':target,
            'host_os':hos,
            'target_os':tos,
            'device_id':tdid,
            'skip_print_os':'yes',
            'skip_device_init':sdi,
            'skip_info_collection':sic,
            'out':oo}
        r=ck.access(ii)
        if r['return']>0: return r

    ###############################################################################################################
    # PIPELINE SECTION: finish vtune
    if vtune=='yes':
       if o=='con':
          ck.out(sep)
          ck.out('Processing Intel vTune output ...')
          ck.out('')

       if os.path.isfile(vtune_tmp1):
          import csv

          clk='Hardware Event Count:CPU_CLK_UNHALTED.THREAD:Self'
          inst='Hardware Event Count:INST_RETIRED.ANY:Self'

          f=open(vtune_tmp1, 'rb')
          c=csv.reader(f, delimiter=',')

          hc=[]
          val={}

          first=True
          for q in c:
              if first:
                 first=False
                 if len(q)>1:
                    for k in range(2,len(q)):
                        hc.append(q[k])
              else:
                 func=q[0]
                 module=q[1]

                 if len(q)>1:
                    for k in range(2,len(q)):
                        val[hc[k-2]]=q[k]

                 break

          f.close()

          if sca!='yes':
             os.remove(vtune_tmp1)

          if len(val)>0:
             if clk in val and inst in val:
                cpi=0
                try:
                   cpi=float(val[clk])/float(val[inst])
                except ValueError:
                   pass
                if cpi!=0:
                   chars['run']['global_cpi']=cpi
                   chars['run']['global_clock']=float(val[clk])
                   chars['run']['global_instructions_retired']=float(val[inst])

    ###############################################################################################################
    # PIPELINE SECTION: finish perf
    if perf=='yes':
       if o=='con':
          ck.out(sep)
          ck.out('Processing perf output ...')
          ck.out('')

       if os.path.isfile(perf_tmp):
          ii={'text_file':perf_tmp,
              'split_to_list':'yes',
              'encoding':sys.stdin.encoding}
#          if sca!='yes':
#             ii['delete_after_read']='yes'

          rx=ck.load_text_file(ii)
          if rx['return']>0: return rx
          glst=rx['lst']

          clk='cycles'
          inst='instructions'
          val={}
          found=False
          for lx in glst:
             l=lx.strip()
             if found:
                x=l.find(',')
                if x>0:
                   v=l[0:x]

                   try:
                      v=float(v)
                   except ValueError:
                      pass

                   y=l.rfind(',')
                   if y>x:
                      key=l[y+1:]
                      val[key]=v
             elif l.find(',task-clock')>0:
                found=True

          if sca!='yes':
             os.remove(perf_tmp)

          if len(val)>0:
             if clk in val and inst in val:
                cpi=0
                try:
                   cpi=val[clk]/val[inst]
                except ValueError:
                   pass
                if cpi!=0:
                   chars['run']['global_cpi']=cpi
                   chars['run']['global_clock']=val[clk]
                   chars['run']['global_instructions_retired']=val[inst]
                   chars['run']['perf']=val

    ###############################################################################################################
    # PIPELINE SECTION: finish gprof
    if gprof=='yes':
       if o=='con':
          ck.out(sep)
          ck.out('Processing gprof output ...')
          ck.out('')

       if os.path.isfile(cfg['gprof_file']):
          ii={'text_file':gprof_tmp,
              'split_to_list':'yes',
              'encoding':sys.stdin.encoding}
          if sca!='yes':
             ii['delete_after_read']='yes'

          rx=ck.load_text_file(ii)
          if rx['return']>0: return rx
          glst=rx['lst']

          process=False
          cgprof={}
          for g in glst:
              if g.startswith(' time'):
                 process=True
                 continue

              if process:
                 if g=='':
                    break

                 gg1=g.strip().split(' ')
                 gg=[]
                 for g1 in gg1:
                     g1x=g1.strip()
                     if g1x!='': gg.append(g1x)

                 igg=len(gg)

                 if igg>0:
                    x1=gg[igg-1]
                    cgprof[x1]=gg
                    ck.out(' * '+str(x1)+' : '+str(gg[0])+' % ')

          chars['run']['gprof']=cgprof
          chars['run']['gprof_list']=glst
       else:
          ck.out('WARNING: gprof output was not found ...')
          ck.out('')

    ###############################################################################################################
    # PIPELINE SECTION: Post-process MALI HWC counters
    if mali_hwc=='yes':
       # Call process output vector
       r=ck.access({'action':'run', 
                    'module_uoa':cfg['module_deps']['script'], 
                    'data_uoa': cfg['data_deps']['mali_hwc'], #'mali-hwc', 
                    'code':'process', 
                    'func':'read'})
       if r['return']>0: 
          return {'return':r['return'], 'error':'Problem with MALI HWC script ('+r['error']+')'}

    ###############################################################################################################
    # PIPELINE SECTION: Post-process output from dividiti's OpenCL profiler.
    if odp=='yes':
        # Check that not processed yet by postprocessing program scripts
        # TBD: this code should be converted to CK canonical form ...
        if not os.path.isfile(fodp):
           dvdt_prof=xdeps.get('dvdt_prof',{})
           with open('tmp-dvdt-prof-deps.json', 'w') as f:
               json.dump(dvdt_prof, f, indent=2)
           # Load output.
           stdout_file = vcmd.get('run_time',{}).get('run_cmd_out1','')
           if not os.path.isfile(stdout_file):
               ck.out('\n  Warning: unable to invoke dvdt_prof, program output file not found\n')
           else:
               r=ck.load_text_file({
                   'text_file':stdout_file,
                   'split_to_list':'no'
               })
               if r['return']>0: return r

               # Locate profiler parser.
               dvdt_prof_dir=dvdt_prof['dict']['env']['CK_ENV_TOOL_DVDT_PROF']
               dvdt_prof_src_python=os.path.join(dvdt_prof_dir,'src','python')
               sys.path.append(dvdt_prof_src_python)
               from prof_parser import prof_parse

               # Parse profiler output.
               chars['run']['dvdt_prof']=prof_parse(r['string'])
               with open('tmp-dvdt-prof.json', 'w') as f:
                   json.dump(chars['run']['dvdt_prof'], f, indent=2)

               with open('tmp-dvdt-prof-'+str(srn)+'.json', 'w') as f:
                   json.dump(chars['run']['dvdt_prof'], f, indent=2)

    ###############################################################################################################
    # Deinit remote device, if needed
    ndi=i.get('no_deinit_remote_device','')
    if remote=='yes' and ndi!='yes':
       r=ck.access({'action':'init_device',
                    'module_uoa':cfg['module_deps']['platform'],
                    'os_dict':tosd,
                    'device_id':tdid,
                    'key':'remote_deinit'})
       if r['return']>0: return r

    ###############################################################################################################
    # PIPELINE SECTION: finalize PIPELINE
    if i.get('fail','')=='yes':
       print_warning({'data_uoa':duoa, 'repo_uoa':ruoa})

    i['out']=o
    return finalize_pipeline(i)

##############################################################################
# finalize pipeline
def finalize_pipeline(i):
    """
    Input:  {
              Input from pipeline that will be passed as output
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    o=i.get('out','')

    state=i.get('state',{})
    pr=i.get('prepare','')

    fail=i.get('fail','')
    fail_reason=i.get('fail_reason','')

    stfx=i.get('save_to_file','')
    stf=stfx
    cd=state.get('cur_dir','')
    if not os.path.isabs(stf):
       stf=os.path.join(cd, stf)

    # Cleaning input/output
    for q in cfg['clean_vars_in_output']:
        if q in i:
           del(i[q])

    if stfx!='':
       if o=='con':
          ck.out(sep)
          ck.out('Writing state to file '+stf+' ...')

       rx=ck.save_json_to_file({'json_file':stf,
                                'dict':i,
                                'sort_keys':'yes'})
       if rx['return']>0: return rx

    if o=='con':
       ck.out(sep)
       if i.get('ready','')=='yes':
          if pr=='yes':
             ck.out('Pipeline is ready!')
          else:
             if fail=='yes':
                x=''
                if fail_reason!='': x=' ('+fail_reason+')'
                ck.out('Pipeline failed'+x+'!')
             else:
                ck.out('Pipeline executed successfully!')
       else:
          ck.out('Pipeline is NOT YET READY - multiple choices exists!')

    i['return']=0

    return i

##############################################################################
# substitute some CK reserved keys
#   $#ck_take_from{CID or UID}#$ (if module_uoa omitted, use current one)
#   $#ck_host_os_sep#$

def substitute_some_ck_keys(i):
    """
    Input:  {
              string       - string to process
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              string       -
              path         - if substitute ck_take_from_{
            }

    """

    import os

    s=i['string']
    p=''

    b1=s.find('$#ck_take_from_{')
    if b1>=0:
       b2=s.find('}#$', b1)
       if b2<0:
          return {'return':1, 'error':'wrong format of the $#ck_take_from{}#$ ('+s+')'}
       bb=s[b1+16:b2]

       rx=ck.parse_cid({'cid':bb})
       if rx['return']==0:
          ruoa=rx.get('repo_uoa','')
          muoa=rx.get('module_uoa','')
          duoa=rx.get('data_uoa','')
       else:
          ruoa=''
          muoa=work['self_module_uid']
          duoa=bb

       rb=ck.access({'action':'load',
                     'module_uoa':muoa,
                     'data_uoa':duoa,
                     'repo_uoa':ruoa})
       if rb['return']>0: return rb

       p=rb['path']

       s=s[:b1]+p+os.path.sep+s[b2+3:]

    s=s.replace('$#ck_host_os_sep#$', os.path.sep)

    return {'return':0, 'string':s, 'path':p}

##############################################################################
# copy program

def cp(i):
    """
    Input:  {
               CID1
               CID2
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    i['common_func']='yes'
    r=ck.access(i)
    if r['return']>0: return r

    ruid=r['repo_uid']
    muid=r['module_uid']
    duid=r['data_uid']
    duoa=r['data_uoa']

    d=r['dict']

    d['backup_data_uid']=duid
    d['data_name']=duoa

    ii={'action':'update',
        'module_uoa':muid,
        'repo_uoa':ruid,
        'data_uoa':duid,
        'dict':d,
        'ignore_update':'yes',
        'sort_keys':'yes'}

    return ck.access(ii)

##############################################################################
# Common action: copy (or move) data entry

def copy(i):
    """
    See "cp" API

    """

    return cp(i)

##############################################################################
# crowdtune program (redirecting to crowdsource program.optimization from ck-crowdtuning)

def crowdtune(i):
    """
    See 'crowdsource program.optimization'

    """

    o=i.get('out','')

    m=cfg['module_program_optimization']

    # Check if module exists
    r=ck.access({'action':'find', 'module_uoa':'module', 'data_uoa':m})
    if r['return']>0:
       if o=='con':
          ck.out('Module "program.optimization" doesn\'t exist!')
          ck.out('')
          ck.out('Please, try to install shared repository "ck-crowdtuning"')
          ck.out('  $ ck pull repo:ck-crowdtuning')
          ck.out('')

       return r

    # Redirecting to crowdsource program.optimization
    i['action']='crowdsource'
    i['module_uoa']=m

    return ck.access(i)

##############################################################################
# clean all tmp directories

def clean_tmp(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os
    import shutil

    duoa=i.get('data_uoa','')
    ruoa=i.get('repo_uoa','')

    ii={'action':'search',
        'module_uoa':work['self_module_uid'],
        'data_uoa':duoa,
        'repo_uoa':ruoa}
    r=ck.access(ii)
    if r['return']>0: return r

    lst=r['lst']
    for q in lst:
        p=q['path']
        ck.out('Cleaning tmp* dirs in '+p+' ...')

        px=os.listdir(p)
        for xx in px:
            pp=os.path.join(p,xx)
            if os.path.isdir(pp) and xx.startswith('tmp'):
               ck.out('  * '+xx)
               shutil.rmtree(pp, ignore_errors=True)

    return {'return':0}

##############################################################################
# autotune program (redirecting to crowdsource program.optimization from ck-crowdtuning while using local repo)

def autotune(i):
    """
    Input:  {
               See 'crowdsource program.optimization'

               (iterations) - change iterations

               Force:

               local                = yes
               only_one_run         = yes
               keep_tmp             = yes
               skip_exchange        = yes
               change_user          = -
               skip_welcome         = yes
               program_tags         = ' '
               ask_pipeline_choices = yes

            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')

    m=cfg['module_program_optimization']

    # Check if module exists
    r=ck.access({'action':'find', 'module_uoa':'module', 'data_uoa':m})
    if r['return']>0:
       if o=='con':
          ck.out('WARNING: this function uses module "program.optimization" but can\'t find it')
          ck.out('')
          ck.out('Please, try to install shared repository "ck-crowdtuning"')
          ck.out('  $ ck pull repo:ck-crowdtuning')
          ck.out('')

       return r

    # Redirecting to crowdsource program.optimization
    i['action']='crowdsource'
    i['module_uoa']=m
    i['local']='yes'
    i['once']='yes'
    i['keep_experiments']='yes'
    i['skip_welcome']='yes'
    i['program_tags']=' '
    i['ask_pipeline_choices']='yes'
    i['local_autotuning']='yes'

    se=i.get('skip_exchange','')
    if se=='': se='yes'
    i['skip_exchange']=se

    cu=i.get('change_user','')
    if cu=='': cu='-'
    i['change_user']=cu

    return ck.access(i)

##############################################################################
# crowdtune programs via list

def xcrowdtune(i):
    """
    Input:  {
              workloads    - list of dicts to update input
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import copy

    l=i.get('workloads',[])

    i['action']='crowdtune'
    i['once']='yes'
    ii=copy.deepcopy(i)

    for q in l:
        iii=copy.deepcopy(ii)
        iii.update(q)
        r=ck.access(iii)
        if r['return']>0: return r

    return {'return':0}

##############################################################################
# benchmark program (run autotune with 1 iteration and full environment setup)

def benchmark(i):
    """
    Input:  {
              See "ck run pipeline --help" for all input keys

              Extra:
               (repetititons) - number of statistical repetitions of a pipeline
               (console) - print to console rather than to files
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')
    duoa=i.get('data_uoa','')

    i['action']='run'
    i['module_uoa']=cfg['module_deps']['pipeline']
    i['data_uoa']=work['self_module_uid']
    i['cid']=''

    up=i.get('pipeline_update',{})
    if duoa=='':
       # Try to get from current CID (as module!)
       r=ck.cid({})
       if r['return']==0:
          duoa=r.get('data_uoa','')

    if duoa=='':
       return {'return':1, 'error':'program is not defined'}

    up['program_uoa']=duoa

    if i.get('skip_freq','')=='yes':
       i['cpu_freq']=''
       up['cpu_freq']=''
       i['gpu_freq']=''
       up['gpu_freq']=''
    else:
       cf=i.get('cpu_freq','')
       if cf=='': cf='max'
       up['cpu_freq']=cf

       gf=i.get('gpu_freq','')
       if gf=='': gf='max'
       up['gpu_freq']=gf

    if i.get('debug_run_cmd','')!='':
       up['debug_run_cmd']=i['debug_run_cmd']

    up['console']=i.get('console','')

    nsc=i.get('no_state_check','')
    if nsc=='': nsc='yes'
    up['no_state_check']=nsc

    # Get all extra input to pipeline
    ik=ck.cfg.get('internal_keys',[])
    if len(ik)==0: # older CK kernel doesn't have it ...
       ik=cfg['internal_keys']

    for k in i:
        if k not in ik:
           up[k]=i[k]

    if len(up)>0:
       i['pipeline_update']=up

    # If pruning flags from command line, need to prepare in universal CK format (choices and order)
    iters=i.get('iterations','')

    if i.get('prune','')=='yes' and i.get('flags','')!='':
       pruned_choices_order=[]
       pruned_choices={}

       x=i['flags'].strip().split(' ')
       for q in range(0,len(x)):
           v=x[q].strip()
           k='##compiler_flags#from_cmd_'+str(q+1)
           pruned_choices_order.append(k)
           pruned_choices[k]=v

       i['solutions']=[{'points':[{
           'pruned_choices_order':pruned_choices_order,
           'pruned_choices':pruned_choices}]
          }]

       iters=-1

    i['iterations']=iters

    r=ck.access(i)
    if r['return']>0: return r

    if o=='con':
       ck.out(sep)
       ck.out('Some statistics:')

       lio=r.get('last_iteration_output',{})

       fail=lio.get('fail','')
       fail_reason=lio.get('fail_reason','')

       ck.out('')
       ck.out('* Failed: '+fail)
       if fail=='yes':
          ck.out('* Reason: '+fail_reason)

       flat=r.get('last_stat_analysis',{})
       if 'dict_flat' in flat: flat=flat.get('dict_flat',{}) # Stange incompatibility (not sure where it comes from)

       bs=flat.get('##characteristics#compile#binary_size#min',0)
       os=flat.get('##characteristics#compile#obj_size#min',0)

       ck.out('')
       ck.out('* Binary size: '+str(bs))
       ck.out('* Object size: '+str(os))

       repeat=flat.get('##characteristics#run#repeat#max',0)
       ck.out('')
       ck.out('* Kernel repeat: '+str(repeat))

       tmin=flat.get('##characteristics#run#total_execution_time#min',0)
       tmax=flat.get('##characteristics#run#total_execution_time#max',0)

       ntmin=flat.get('##characteristics#run#execution_time#min',0)
       ntmax=flat.get('##characteristics#run#execution_time#max',0)

       ck.out('')
       ck.out('* Normalized time in sec. (min .. max): '+str(ntmin)+' .. '+str(ntmax))

       ck.out('')
       ck.out('* Total time in us (min .. max): '+str(tmin)+' .. '+str(tmax))

       # Check if aggregated OpenCL kernel time
       found=False
       for k in sorted(flat):
           if k.startswith('##characteristics#run#execution_time_opencl_us') and k.endswith('#min'):
              tmin=flat[k]
              k1=k[:-3]+'max'
              tmax=flat.get(k1,tmin)

              kernel=k[47:-4]

              if not found:
                 found=True

                 ck.out('')
                 ck.out('* OpenCL aggregated kernel times in us. (min .. max):')
                 ck.out('')

              ck.out('  '+kernel+' : '+str(tmin)+' .. '+str(tmax))

       # Check if sequence of OpenCL kernel time and rebuild sequence
       kernels={}
       for k in flat:
           if k.startswith('##characteristics#run#execution_time_list_opencl') and k.endswith('#min'):
              j=k.find('#',49)
              if j>0:
                 num=k[49:j]

                 if num not in kernels:
                    kernels[num]={'lws':{},'gws':{}}

                 j=k.find('#',49)
                 if j>0:
                    x=k[j+1:-4]

                    v=flat[k]

                    if x=='kernel_time':
                       kernels[num]['kernel_time_min']=v

                       k1=k[:-3]+'max'
                       kernels[num]['kernel_time_max']=flat.get(k1,v)

                    elif x.startswith('lws@') or x.startswith('gws@'):
                       x1=x[4:]
                       kernels[num][x[:3]][x1]=v
                    else:
                       kernels[num][x]=v

       if len(kernels)>0:
          ck.out('')
          ck.out('* OpenCL kernel sequence with times in us. (min .. max), local work size, global work size:')
          ck.out('')

          for q in sorted(kernels, key=lambda v: kernels[v]['sequence']):
              qq=kernels[q]

              kernel=qq['kernel_name']
              sec=qq['sequence']

              tmin=qq['kernel_time_min']*1e-3
              tmax=qq['kernel_time_max']*1e-3

              lws=qq['lws']
              gws=qq['gws']

              xlws=''
              for j in sorted(lws):
                  if xlws!='': xlws+=','
                  xlws+=str(lws[j])

              xgws=''
              for j in sorted(gws):
                  if xgws!='': xgws+=','
                  xgws+=str(gws[j])

              x=''
              if xlws!='': x+='LWS='+xlws
              if xgws!='': 
                 if x!='': x+=' '
                 x+='GWS='+xgws
              if x!='': x=' ('+x+')'

              ck.out('  '+str(sec)+') '+kernel+' : '+str(tmin)+' .. '+str(tmax)+x)

       ck.out('')

    return r

##############################################################################
# Update run-time deps

def update_run_time_deps(i):
    """
    Input:  {
              (host_os)
              (target_os)
              (target_id)

              (deps)       - possibly resolved deps
              (deps_cache) - deps cache (to reuse deps if needed)
              (reuse_deps) - if 'yes', always attempt to reuse deps from above cache

              (meta)       - program meta
              (cmd_key)    - command line key
              (cmd_meta)   - meta for a given command line key

              (out)        - where to output
              (quiet)      - quiet mode
              (random)     - if 'yes', select deps randomly (useful for quite crowd-tuning / DNN classification)

              (install_to_env)       - install dependencies to env instead of CK-TOOLS (to keep it clean)!

              (safe)                 - safe mode when searching packages first instead of detecting already installed soft
                                       (to have more deterministic build)

              (preset_deps)          - to preset deps
            }

    Output: {
              return           - return code =  0, if successful
                                             >  0, if error
              (error)          - error text if return > 0

              (resolve)        - output from 'resolve env' for run-time deps if used

              (aggregated_env) - aggregated environment from all deps
            }
    """

    deps=i.get('deps',{})
    meta=i.get('meta',{})

    kcmd=i.get('cmd_key','')
    vcmd=i.get('cmd_meta',{})

    hos=i.get('host_os','')
    tos=i.get('target_os','')
    tdid=i.get('target_id','')

    quiet=i.get('quiet','')
    ran=i.get('random','')

    iev=i.get('install_to_env','')
    safe=i.get('safe','')

    deps_cache=i.get('deps_cache','')
    reuse_deps=i.get('reuse_deps','')

    dep_add_tags=i.get('dep_add_tags', {})

    o=i.get('out','')
    oo=''
    if o=='con': oo=o

    # Finding already prepared run-time deps in global deps
    rdeps={}

    for kd in deps:
        if deps[kd].get('for_run_time','')=='yes':
           rdeps[kd]=deps[kd]

    # If run time deps was not already set up, prepare them now
    rr={'return':0}

    if len(rdeps)==0:
       rdeps.update(meta.get('run_deps',{}))
       rdeps.update(vcmd.get('run_deps',{}))

       # Prune if needed
       for kd in list(rdeps.keys()):
           kdd=rdeps[kd].get('only_for_cmd',[])
           if len(kdd)>0 and kcmd not in kdd:
              del(rdeps[kd])

       ### Update dependencies if needed
       update_deps=vcmd.get('update_deps',{})
       if len(update_deps)>0:
          if o=='con':
             ck.out('')
             ck.out('  Updating deps based on selected command line key ...')

          for kd in update_deps:
              if kd in rdeps:
                 new_tags=update_deps[kd].get('tags','')
                 if new_tags!='':
                    old_tags=rdeps[kd].get('tags','')
                    if old_tags!='': old_tags+=','
                    rdeps[kd]['tags']=old_tags+new_tags
                 new_tags=update_deps[kd].get('no_tags','')
                 if new_tags!='':
                    old_tags=rdeps[kd].get('no_tags','')
                    if old_tags!='': old_tags+=','
                    rdeps[kd]['no_tags']=old_tags+new_tags

       # Check user-friendly deps
       pd=i.get('preset_deps',{})
       for q in pd:
           if q in rdeps:
              rdeps[q]['uoa']=pd[q]

       ii={'action':'resolve',
           'module_uoa':cfg['module_deps']['env'],
           'host_os':hos,
           'target_os':tos,
           'device_id':tdid,
           'deps':rdeps,
           'deps_cache':deps_cache,
           'reuse_deps':reuse_deps,
           'add_customize':'yes',
           'quiet':quiet,
           'random':ran,
           'install_to_env':iev,
           'dep_add_tags': dep_add_tags,
           'safe':safe,
           'out':oo}

       ## FIXME: this behaviour is to become default after sufficient testing (2018/09/10)
       #
       if meta.get('pass_env_to_resolve', '')=='yes':
            ii.update({ 'install_env': i.get('env_for_resolve',{}) })

       rx=ck.access(ii)
       if rx['return']>0: return rx

       rr['resolve']=rx

       # Add run deps back to global deps and mark for run_time (to reuse further in pipeline)
       for kd in rdeps:
           deps[kd]=rdeps[kd]
           deps[kd]['for_run_time']='yes'

    # Assemble environment from all deps
    xenv={}
    for kd in sorted(deps, key=lambda kk: deps[kk].get('sort',0)):
        xenv.update(deps[kd].get('dict',{}).get('env',{}))

    rr['aggregated_env']=xenv

    return rr

##############################################################################
# Copy file to remote

def copy_file_to_remote(i):
    """
    Input:  {
              host_os_dict
              target_os_dict
              device_id
              file1
              (file1s)
              file2
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }
    """

    import os

    o=i.get('out','')

    hosd=i['host_os_dict']
    host_hash_cmd = hosd.get('md5sum', 'md5sum')

    tosd=i['target_os_dict']

    tdid=i.get('device_id','')

    xtdid=''
    if tdid!='': xtdid=' -s '+tdid

    file1=i['file1']
    file1s=i.get('file1s','')
    if file1s=='': file1s=file1
    file2=i['file2']

    if file1=='':
       return {'return':1, 'error':'file to be sent to remote device is not specified'}

    if not os.path.exists(file1):
       return {'return':1, 'error':'file to be sent to remote device ('+file1+') is not found'}

    # Check params of remote file
    rs=tosd['remote_shell'].replace('$#device#$',xtdid)
    rse=tosd.get('remote_shell_end','')+' '

    x = rs + ' md5sum ' + file2 + rse

    shell='no'
    if x.startswith('ck'): shell='yes'

    ry=ck.run_and_get_stdout({'cmd':x, 'shell': shell})
    if ry['return']>0: return ry
    so=ry['stdout'].lower()

    skip=False
    if 'no such file or directory' not in so:
        remote_hash = so.split(' ')[0]

        rz=ck.run_and_get_stdout({'cmd': host_hash_cmd+' '+file1 , 'shell': 'no'})
        if rz['return']>0: return rz
        local_hash = rz['stdout'].lower().split(' ')[0]

        if remote_hash==local_hash:
            if o=='con':
                ck.out(sep)
                ck.out('Skipped copying file '+file1+' to remote (the same hash)')
            skip=True

    if not skip:
       y=tosd.get('remote_push_pre','').replace('$#device#$',xtdid)
       if y!='':
          y=y.replace('$#file1#$', file1).replace('$#file1s#$', file1s).replace('$#file2#$', file2)

          if o=='con':
             ck.out(sep)
             ck.out(y)
             ck.out('')

          ry=os.system(y)
          if ry>0:
             return {'return':1, 'error':'copying to remote device failed'}

       y=tosd['remote_push'].replace('$#device#$',xtdid)
       y=y.replace('$#file1#$', file1).replace('$#file1s#$', file1s).replace('$#file2#$', file2)

       if o=='con':
          ck.out(sep)
          ck.out(y)
          ck.out('')

       ry=os.system(y)
       if ry>0:
          return {'return':1, 'error':'copying to remote device failed'}

    return {'return':0}

##############################################################################
# prepare HTML/TEX table with results

def prepare_table_with_results(i):
    """
    Input:  {
               table_header
               entries
               
               (force_round)

               (out_html_file)
               (out_tex_file)

               (skip_stats) - if 'yes', do not show stats (useful to show reduced flags)

               (tex_wide) - if 'yes' create wide table

               (url_prefix) - add URL to index
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import ck.kernel as ck
    import os

    html_file=i.get('out_html_file','')
    tex_file=i.get('out_tex_file','')

    force_round=i.get('force_round',None)

    table_header=i['table_header']
    table=[]
    table_custom=[]

    entries=i['entries']

    cwd=os.getcwd()

    fh=os.path.join(cwd, html_file)
    ft=os.path.join(cwd, tex_file)

    url_prefix=i.get('url_prefix','')

    # Processing data (filling in table)
    for e in entries:
        duid=e['data_uid']
        duoa=e['data_uoa']
        puid=e['point']
        puidi=e.get('point_improvement','')
        no_imp=e.get('no_improvement','')
        note=e['note']
        ef=e['extra_field']
        custom=e.get('custom',{})

        ck.out('Processing '+duoa+' ('+puid+') ...')

        # Point 1
        r=ck.access({'action':'get',
                     'module_uoa':cfg['module_deps']['experiment'],
                     'data_uoa':duid,
                     'prune_points':[puid],
                     'load_json_files':['flat']})
        if r['return']>0: return r

        points=r.get('points',[])
        if len(points)==0:
           return {'return':1, 'error':'can\'t find data'}
        if len(points)>1:
           return {'return':1, 'error':'ambiguity - more than one point found'}

        p0=points[0]

        pf=p0.get('flat',{})
        if len(pf)==0:
           return {'return':1, 'error':'can\'t find stats in entry'}

        # Execution time
        et_min=pf.get('##characteristics#run#execution_time_kernel_0#min',None)
        et_exp=pf.get('##characteristics#run#execution_time_kernel_0#exp',None)
        et_mean=pf.get('##characteristics#run#execution_time_kernel_0#mean',None)
        et_range=pf.get('##characteristics#run#execution_time_kernel_0#range',None)
        et_range_percent=pf.get('##characteristics#run#execution_time_kernel_0#range_percent',None)

        # Total binary size (not object file size)
        bs=pf.get('##characteristics#compile#binary_size#min',None)

        # Flags
        flags=pf.get('##characteristics#compile#joined_compiler_flags#min','')

        # Point Improvement
        imp_et=0
        imp_bs=0

        # Get URL
        url=''
        if url_prefix!='':
           px=puid
           if puidi!='': px=puidi
           url1=url_prefix+'wcid=experiment:'+duid+'&subpoint='+px
           url2=url_prefix+'wcid=experiment:'+duid+'\&subpoint='+px

           custom['field_0_html']='<a href="'+url1+'">'+note+'</a>'
           custom['field_0_tex']='\href{'+url2+'}{'+note+'}'

        if puidi!='':
           r=ck.access({'action':'get',
                        'module_uoa':cfg['module_deps']['experiment'],
                        'data_uoa':duid,
                        'prune_points':[puidi],
                        'load_json_files':['flat']})
           if r['return']>0: return r

           ipoints=r.get('points',[])
           if len(ipoints)==0:
              return {'return':1, 'error':'can\'t find data'}
           if len(ipoints)>1:
              return {'return':1, 'error':'ambiguity - more than one point found'}

           ip0=ipoints[0]

           ipf=ip0.get('flat',{})
           if len(ipf)==0:
              return {'return':1, 'error':'can\'t find stats in entry'}

           # Execution time
           iet_min=ipf.get('##characteristics#run#execution_time_kernel_0#min',None)
           iet_exp=ipf.get('##characteristics#run#execution_time_kernel_0#exp',None)
           iet_mean=ipf.get('##characteristics#run#execution_time_kernel_0#mean',None)
           iet_range=ipf.get('##characteristics#run#execution_time_kernel_0#range',None)
           iet_range_percent=ipf.get('##characteristics#run#execution_time_kernel_0#range_percent',None)

           # Total binary size (not object file size)
           ibs=ipf.get('##characteristics#compile#binary_size#min',None)

           # Flags
           flags=ipf.get('##characteristics#compile#joined_compiler_flags#min','')

           # Make proper +- string
           r=ck.access({'action':'process_plus_minus',
                        'module_uoa':cfg['module_deps']['math.variation'],
                        'var_mean':et_mean,
                        'var_range':et_range,
                        'force_round':force_round})
           if r['return']>0: return r

           iet_mean=r['var_mean']
           iet_range=r['var_range']

           iet_h=r['html']
           iet_t=r['tex']

           # Calcluating improvements (should check relative error later)
           imp_et=float(et_min)/float(iet_min)
           imp_bs=float(bs)/float(ibs)

           simp_et='~ %.2f' % imp_et
           simp_bs='~ %.2f' % imp_bs

           custom['field_2_html']=simp_et+' <i>('+iet_h+')</i>'
           custom['field_2_tex']=simp_et+' ('+iet_t+')'

           custom['field_3_html']=simp_bs+' <i>('+str(bs)+')</i>'
           custom['field_3_tex']=simp_bs+' ('+str(bs)+')'
        else:
           # Make proper +- string
           r=ck.access({'action':'process_plus_minus',
                        'module_uoa':cfg['module_deps']['math.variation'],
                        'var_mean':et_mean,
                        'var_range':et_range,
                        'force_round':force_round})
           if r['return']>0: return r

           et_mean=r['var_mean']
           et_range=r['var_range']

           et_h=r['html']
           et_t=r['tex']

           if no_imp=='yes':
              et_h='no <i>('+et_h+')</i>'
              et_t='no ('+et_t+')'

              custom['field_3_html']='no <i>('+str(bs)+')</i>'
              custom['field_3_tex']='no ('+str(bs)+')'

           custom['field_2_html']=et_h
           custom['field_2_tex']=et_t

        # Check if need to bold them
        if e.get('bold_flags','')=='yes':
           flags1=flags.split(' ')
           hflags=''
           tflags=''

           for fl in flags1:
               tfl=fl
               if not fl.startswith('-fno-'):
                  fl='<b>'+fl+'</b>'
                  tfl='\\textbf{'+tfl+'}'

               if hflags!='': hflags+=' '
               hflags+=fl

               if tflags!='': tflags+=' '
               tflags+=tfl

           j='1'
           if i.get('skip_stats','')!='yes':
              j='4'

           custom['field_'+j+'_html']=hflags
           custom['field_'+j+'_tex']=tflags

        tb=[note]
        if i.get('skip_stats','')!='yes':
           if puidi!='':
              tb+=[ef, imp_et, imp_bs]
           else:
              tb+=[ef, et_mean, bs]
        tb.append(flags)

        table.append(tb)
        table_custom.append(custom)

    # Preparing table
    r=ck.access({'action':'prepare',
                 'module_uoa':cfg['module_deps']['table'],
                 'table':table,
                 'table_custom':table_custom,
                 'table_header':table_header,
                 'table_style':'border="1" cellpadding="5" cellspacing="0"',
                 'header_style':'style="background-color:#cfcfcf;"',
                 'element_style':'valign="top"',
                 'header_element_style':'valign="top"',
                 'tex_wide':i.get('tex_wide',''),
                 'record_html':fh,
                 'record_tex':ft})
    return r

##############################################################################
# find program output entry

def find_output(i):
    """
    Input:  {
              data_uoa
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')

    duoa=i.get('data_uoa','')
    if duoa=='':
       return {'return':1, 'error':'please, specify program UOA'}

    # Find program UID
    r=ck.access({'action':'load',
                 'module_uoa':work['self_module_uid'],
                 'data_uoa':duoa})
    if r['return']>0: return r
    duid=r['data_uid']

    puoa='program-uid-'+duid

    # Search output
    r=ck.access({'action':'search',
                 'module_uoa':cfg['module_deps']['program.output'],
                 'data_uoa':puoa})
    if r['return']>0: return r

    if o=='con':
       for q in r['lst']:
           ck.out(q['path'])

    return r

##############################################################################
# add program with templates
# suggested here: https://github.com/ctuning/ck-autotuning/issues/28

def add(i):
    """
    Input:  {
              (template) - if !='', use this program as template!
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')

    # Redirect to universal template ...

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

    dname=i.get('data_name','')
    if dname=='': dname=duoa

    if 'template' in dd: del(dd['template'])

    tags=[]
    for k in dd.get('tags',[]):
        if k!='template': tags.append(k)
    dd['tags']=tags

    dd['backup_data_uid']=duid
    dd['data_name']=dname

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
       ck.out('Further details about adding new CK programs and workflows:')
       ck.out('')
       ck.out(' * https://github.com/ctuning/ck/wiki/Adding-new-workflows')

    return ck.access(ii)

##############################################################################
# show available programs

def show(i):
    """
    Input:  {
               (the same as list; can use wildcards)
               (out_file) - output to file
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
       ii['ck_title']='Shared CK programs'
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
       h+='<h2>Please check our new <a href="http://ReuseResearch.com/c.php?c=program">beta browser</a> for CK components!</h2>\n'

       h+='<br>\n'
       h+='<b>List of portable and customizable program workflows:</b><br>\n'

       h+='<p>\n'
       h+='You can obtain repository with a given program (workflow) as follows:\n'
       h+='<pre>\n'
       h+=' ck pull repo:{Repo UOA - see below}\n'
       h+='</pre>\n'

       h+='You can then compile this program if necessary (CK will automatically detect\n'
       h+='  <a href="http://cKnowledge.org/shared-soft-detection-plugins.html">software dependencies</a>\n'
       h+='  or install missing <a href="http://cKnowledge.org/shared-packages.html">packages</a>) as follows:\n'
       h+='<pre>\n'
       h+=' ck compile program:{Program UOA - see below}\n'
       h+='</pre>\n'

       h+='You can run this program as follows:\n'
       h+='<pre>\n'
       h+=' ck run program:{Program UOA - see below}\n'
       h+='</pre>\n'

       h+='You can execute program pipeline which chains together various plugins to set up and monitor frequency, prepare data sets, compile program and run it several times, etc:\n'
       h+='<pre>\n'
       h+=' ck pipeline program:{Program UOA - see below} ...\n'
       h+='</pre>\n'

       h+='You can check extra options to customize above pipeline as follows:\n'
       h+='<pre>\n'
       h+=' ck pipeline program:{Program UOA - see below} --help\n'
       h+='</pre>\n'

       h+='You can customize pipeline execution via variables:\n'
       h+='<pre>\n'
       h+=' ck pipeline program:{Program UOA - see below} --env.VAR1=PARAM1 ...\n'
       h+='</pre>\n'

       h+='You can also benchmark a given program which includes executing this program several times, performing statistical analysis, unifying I/O, etc:\n'
       h+='<pre>\n'
       h+=' ck benchmark program:{Program UOA - see below}\n'
       h+='</pre>\n'

       h+='<p>\n'
       h+='See <a href="https://github.com/ctuning/ck/wiki">CK documentation</a>,\n'
       h+=' <a href="https://github.com/ctuning/ck/wiki#contributing">"how to contribute" guide</a>,\n'
       h+=' and the latest <a href="http://cKnowledge.org/rpi-crowd-tuning">CK paper</a> for further details.\n'

       h+='<p>\n'
       h+='<table cellpadding="4" border="1" style="border-collapse: collapse; border: 1px solid black;">\n'

       h+=' <tr>\n'
       h+='  <td nowrap><b>#</b></td>\n'
       h+='  <td nowrap><b>Program UOA</b></td>\n'
       h+='  <td nowrap><b>Template?</b></td>\n'
       h+='  <td nowrap><b>Repo UOA</b></td>\n'
       h+='  <td nowrap><b>Available command lines</b></td>\n'
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

              yh=url+'/tree/master/program/'+ln
              x='['+url+' '+lr+']'
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

              cmds=''
              run_cmds=lm.get('run_cmds',[])
              for rc in run_cmds:
                  cmds+='&#8226;&nbsp;'+rc+'<br>'

              h+='  <td nowrap valign="top"><a name="'+ln+'">'+str(num)+'</b></td>\n'

              h+='  <td nowrap valign="top">'+z1+ln+x2+'</b> <i>('+z11+'CK meta'+x2+')</i></td>\n'

              h+='  <td nowrap valign="top">'+template+'</td>\n'

              h+='  <td nowrap valign="top">'+x1+lr+x2+'</td>\n'

              h+='  <td nowrap valign="top">'+cmds+'</td>\n'

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
    ck.out('  Total programs: '+str(num))
    ck.out('')

    if html:
       h+='</table>\n'
       h+=h2

       if of!='':
          r=ck.save_text_file({'text_file':of, 'string':h})
          if r['return']>0: return r

    return {'return':0, 'html':h}

##############################################################################
# internal: print community warning when program fails

def print_warning(i):
    """
    Input:  {
              data_uoa
              repo_uoa
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    # Check if this warning is disabled in CK kernel
    pduoa=i['data_uoa']
    if pduoa!='' and ck.cfg.get('skip_message_when_program_fails')!='yes':
       pruoa=i['repo_uoa']

       ck.out('')
       ck.out('   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

       ck.out('   CK detected a PROBLEM in the third-party CK program pipeline:')

#       ck.out('The community develops, shares and improves CK program workflows')
#       ck.out('to be portable and customizable across many evolving platforms:')
#       ck.out('* http://cKnowledge.org/shared-programs.html')

#       ck.out('')
#       ck.out('Therefore, they may sometimes fail with newer code versions,')
#       ck.out('under new settings or in previously unseen environments.')

#       ck.out('')
#       ck.out('In such case, please help the community by fixing the problem')
#       ck.out('and/or reporting it via CK mailing list and related repository:')
#       ck.out('(please provide all details about how to reproduce it):')

#       ck.out('')
#       ck.out('* https://groups.google.com/forum/#!forum/collective-knowledge')

#       ck.out('')
#       ck.out('You can turn off this message as follows:')
#       ck.out('$ ck set kernel --var.skip_message_when_program_fails=yes')

       # sometimes pruoa can still be UID -> check
       r=ck.access({'action':'load', 'module_uoa':work['self_module_uid'], 'data_uoa':pduoa})
       if r['return']==0:
          pduoa=r['data_uoa']

       url2=''

       crurl=''
       if pduoa!='' or pruoa!='':
          ck.out('')
          ck.out('   Failed(?) CK program: '+pduoa)

          if pruoa!='':
             # Attempt to read info about this repo
             r=ck.access({'action':'load',
                          'module_uoa':cfg['module_deps']['repo'],
                          'data_uoa':pruoa})
             if r['return']==0:
                d=r['dict']
                pruoa=r['data_uoa']

                ck.out('   CK repo:              '+pruoa)

                url=d.get('url','')
                if url!='':
                   url1=url+'/tree/master/program/'+pduoa
                   url2=url+'/issues'

                   ck.out('')
                   ck.out('   CK repo URL:          '+url)
                   ck.out('   CK program URL:       '+url1)

                   ck.out('   Issues URL:           '+url2)

                   crurl=ck.cfg.get('wiki_data_web','')
                   if crurl!='':
                      crurl+='program/'+pduoa
#                      ck.out('')
#                      ck.out('   CK stable package URL: '+crurl)

       ck.out('   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

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
