#
# Collective Knowledge: CK-powered CLBlast crowd-tuning
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

line='================================================================'

ck_url='http://cknowledge.org/repo/web.php?native_action=show&native_module_uoa=program.optimization&scenario=6c5af99f945739bd'
ck_url1='http://cknowledge.org/repo/web.php?wcid=experiment.bench.dnn:'

ffstat='ck-stat-flat-characteristics.json'
ffmin='ck-stat-flat-min.json'

form_name='wa_web_form'
onchange='document.'+form_name+'.submit();'

hextra='<i><center>\n'
hextra+=' [ <a href="https://en.wikipedia.org/wiki/Collective_Knowledge_(software)">CK intro</a>, \n'
hextra+='<a href="https://arxiv.org/abs/1506.06256">universal workload crowd-tuning</a>; \n'
hextra+='<a href="https://www.researchgate.net/publication/304010295_Collective_Knowledge_Towards_RD_Sustainability">vision</a> and \n'
hextra+='<a href="https://www.youtube.com/watch?v=Q94yWxXUMP0">YouTube lecture</a> ] \n'
hextra+='</center></i>\n'
hextra+='<br>\n'

selector=[{'name':'Routine (CK wrapper)', 'key':'program_uoa'},
          {'name':'GPGPU', 'key':'gpgpu_name'},
          {'name':'CPU', 'key':'cpu_name'},
          {'name':'Platform', 'key':'plat_name', 'new_line':'yes'},
          {'name':'OS', 'key':'os_name'}]

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
# crowdsource these experiments

def crowdsource(i):
    """
    Input:  {
              (local)               - if 'yes', local crowd-benchmarking, instead of public
              (user)                - force different user ID/email for demos

              (choices)             - force different choices to program pipeline

              (repetitions)         - statistical repetitions (default=1), for now statistical analysis is not used (TBD)

              (no_compile)          - if 'yes', skip program compilation (for Android)

              (m)                   - dataset dimension M
              (n)                   - dataset dimension N
              (k)                   - dataset dimension K
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import copy
    import os
    import random

    # Setting output
    o=i.get('out','')
    oo=''
    if o=='con': oo='con'

    quiet=i.get('quiet','')

    duoa=i.get('data_uoa','')
    if duoa=='':
       duoa='clblast-tune-*'

    er=i.get('exchange_repo','')
    if er=='': er=ck.cfg['default_exchange_repo_uoa']
    esr=i.get('exchange_subrepo','')
    if esr=='': esr=ck.cfg['default_exchange_subrepo_uoa']

    if i.get('local','')=='yes': 
       er='local'
       esr=''

    la=i.get('local_autotuning','')

    repetitions=i.get('repetitions','')
    if repetitions=='': repetitions=3
    repetitions=int(repetitions)

    record='no'

    # Check if any input has . and convert to dict
    for k in list(i.keys()):
        if k.find('.')>0:
            v=i[k]

            kk='##'+k.replace('.','#')

            del(i[k])

            r=ck.set_by_flat_key({'dict':i, 'key':kk, 'value':v})
            if r['return']>0: return r

    choices=i.get('choices',{})
    env=i.get('env',{})

    if 'env' not in choices: choices['env']={}

    r=ck.merge_dicts({'dict1':choices['env'], 'dict2':copy.deepcopy(env)})
    env={}

    xchoices=copy.deepcopy(choices)

    # Get user 
    user=''

    mcfg={}
    ii={'action':'load',
        'module_uoa':'module',
        'data_uoa':cfg['module_deps']['program.optimization']}
    r=ck.access(ii)
    if r['return']==0:
       mcfg=r['dict']

       dcfg={}
       ii={'action':'load',
           'module_uoa':mcfg['module_deps']['cfg'],
           'data_uoa':mcfg['cfg_uoa']}
       r=ck.access(ii)
       if r['return']>0 and r['return']!=16: return r
       if r['return']!=16:
          dcfg=r['dict']

       user=dcfg.get('user_email','')

    # Initialize local environment for program optimization ***********************************************************
    pi=i.get('platform_info',{})
    if len(pi)==0:
       ii=copy.deepcopy(i)
       ii['action']='initialize'
       ii['module_uoa']=cfg['module_deps']['program.optimization']
       ii['exchange_repo']=er
       ii['exchange_subrepo']=esr
       ii['skip_welcome']='yes'
       ii['skip_log_wait']='yes'
       ii['crowdtuning_type']='clblast-crowd-tuning'
       r=ck.access(ii)
       if r['return']>0: return r

       pi=r['platform_info']
       user=r.get('user','')

    hos=pi['host_os_uoa']
    hosd=pi['host_os_dict']

    tos=pi['os_uoa']
    tosd=pi['os_dict']
    tbits=tosd.get('bits','')

    remote=tosd.get('remote','')

    tdid=pi['device_id']

    features=pi.get('features',{})

    fplat=features.get('platform',{})
    fos=features.get('os',{})
    fcpu=features.get('cpu',{})
    fgpu=features.get('gpu',{})

    plat_name=fplat.get('name','')
    plat_uid=features.get('platform_uid','')
    os_name=fos.get('name','')
    os_uid=features.get('os_uid','')

    cpu_name=fcpu.get('name','')
    if cpu_name=='': 
       #cpu_name='unknown-'+fcpu.get('cpu_abi','')
       # Likely CPU with multiple cores (such as big-little)
       cpu_unique=features.get('cpu_unique',[])
       for x in cpu_unique:
           if cpu_name!='':
              cpu_name+=' ; '

           y=x.get('ck_arch_real_name','')
           if y=='': y=x.get('ck_cpu_name','')

           cpu_name+=y

    cpu_uid=features.get('cpu_uid','')
    gpu_name=fgpu.get('name','')
    gpgpu_name=''
    sn=fos.get('serial_number','')

    gpgpu_uid=''

    r=ck.access({'action':'detect',
                 'module_uoa':cfg['module_deps']['platform.gpgpu'],
                 'host_os':hos,
                 'target_os':tos,
                 'device_id':tdid,
                 'type':'opencl',
                 'share':'yes',
                 'exchange_repo':er,
                 'exchange_subrepo':esr,
                 'select':'yes',
                 'out':'con'})
    if r['return']>0: return r
    gfeat=r.get('features',{})
    gpgpus=gfeat.get('gpgpu',[])

    cp_id=r['choices']['compute_platform_id']
    cd_id=r['choices']['compute_device_id']

    if len(gpgpus)>0:
        gpgpu_name=gpgpus[0].get('gpgpu',{}).get('name','')
        gpgpu_uid=gpgpus[0].get('gpgpu_uoa','')

    # Check if need square
    square=random.randint(0,1)
    dim=0
    if square==1: dim=random.randrange(64,513,64)

    # Check input (later add ML-based exploration)
    dm=i.get('m','').strip()
    if dm=='': 
       dm=512
#       if square==1: dm=dim
#       else: dm=random.randrange(64,1025,64)
    dm=int(dm)
    env['CK_CLBLAST_MSIZE']=dm

    dn=i.get('n','').strip()
    if dn=='': 
       dn=512
#       if square==1: dn=dim
#       else: dn=random.randrange(64,1025,64)
    dn=int(dn)
    env['CK_CLBLAST_NSIZE']=dn

    dk=i.get('n','').strip()
    if dk=='': 
       dk=512
#       if square==1: dk=dim
#       else: dk=random.randrange(64,1025,64)
    dk=int(dk)
    env['CK_CLBLAST_KSIZE']=dk

    clblast_iters=2 # In fact we rely on CK statistical repetitions with different run-time context ...
    if i.get('clblast_iterations','')!='':
       clblast_iters=i['clblast_iterations']
    env['CK_CLBLAST_ITERATIONS']=clblast_iters

    # Prepare CK pipeline for a given workload
    ii={'action':'pipeline',

        'module_uoa':cfg['module_deps']['program'],
        'data_uoa':duoa,

        'host_os':hos,
        'target_os':tos,
        'device_id':tdid,

        'skip_target':'yes',

        'prepare':'yes',

        'no_clean':i.get('no_compile',''),
        'no_compile':i.get('no_compile',''),

        'compute_platform_id':cp_id,
        'compute_device_id':cd_id,

        'env':env,
        'choices':choices,
#        'dependencies':deps,
#        'cmd_key':run_cmd,
        'no_state_check':'yes',
        'no_compiler_description':'yes',
        'skip_info_collection':'yes',
        'skip_calibration':'yes',
        'cpu_freq':'max',
        'gpu_freq':'max',
        'env_speed':'yes',
        'energy':'no',
        'skip_print_timers':'yes',
        'generate_rnd_tmp_dir':'yes',

        'out':oo}

    rr=ck.access(ii)
    if rr['return']>0: return rr

    fail=rr.get('fail','')
    if fail=='yes':
        return {'return':10, 'error':'pipeline failed ('+rr.get('fail_reason','')+')'}

    ready=rr.get('ready','')
    if ready!='yes':
        return {'return':11, 'error':'couldn\'t prepare universal CK program workflow'}

    state=rr['state']
    tmp_dir=state.get('tmp_dir','')
    if tmp_dir=='': tmp_dir='tmp' # usually when no_compile

    deps=rr['dependencies'] # resolved deps
    ydeps=deps

    if i.get('no_compile','')=='yes':
       pdeps=os.path.join(pp,tmp_dir,'tmp-deps.json')
       if os.path.isfile(pdeps):
          qdeps=copy.deepcopy(deps) # need to keep current selected model for run-time

          rz=ck.load_json_file({'json_file':pdeps})
          if rz['return']>0: return rz
          deps=rz['dict']

          deps.update(qdeps)

    # Check saved deps (if from bin package)
    xk=deps['lib-clblast']
    pbin=xk.get('cus',{}).get('path_bin','')
    if pbin!='':
       rx=ck.access({'action':'find_config_file',
                     'module_uoa':cfg['module_deps']['soft'],
                     'full_path':pbin,
                     'filename':'ck-install-saved.json'})
       if rx['return']>0: return rx
       if rx['found']=='yes':
          if o=='con':
             ck.out('')
             ck.out('Found saved config file for CK binary distribution - reusing deps ...')
             ck.out('')

          ydeps=copy.deepcopy(deps)
          dname=deps['lib-clblast']['dict']['data_name']

          ydeps['lib-clblast']['dict']=copy.deepcopy(rx['dict'])
          ydeps['lib-clblast']['dict']['data_name']=dname

    # Clean pipeline
    if 'ready' in rr: del(rr['ready'])
    if 'fail' in rr: del(rr['fail'])
    if 'return' in rr: del(rr['return'])

    duoa=rr.get('choices',{}).get('data_uoa','')

    # Prepare high-level experiment meta
    meta={'cpu_name':cpu_name,
          'os_name':os_name,
          'plat_name':plat_name,
          'gpu_name':gpu_name,
          'gpgpu_name':gpgpu_name,
          'program_uoa':duoa}

    # Process deps
    xdeps={}
    xblas=''

    for k in ydeps:
        dp=ydeps[k]

        dpd=dp.get('dict',{})

        ptags=dpd.get('tags',[])

        puoa=dpd.get('package_uoa','')
        if puoa=='':
           puoa=dp.get('cus',{}).get('used_package_uid','')

        dname=dpd.get('data_name','')

        xdeps[k]={'name':dp.get('name',''), 'data_name':dname, 'ver':dp.get('ver',''), 'package_uoa':puoa, 'package_tags':ptags}

    # versions of engine sub deps
    dvers={}
    mdep=ydeps.get('lib-clblast',{})
    mdeps=mdep.get('dict',{}).get('deps',{})

    for k in mdeps:
        dvers[k]=mdeps[k].get('ver','')

    # Checking engine name
    d_engine=xdeps.get('lib-clblast',{})
    d_engine_name=d_engine.get('data_name','')
    d_engine_package_uoa=d_engine.get('package_uoa','')
    d_engine_ver=d_engine.get('ver','')

    meta['xversions']=dvers
    meta['xdeps']=xdeps
    meta['choices']=xchoices

    meta['dataset_m']=dm
    meta['dataset_n']=dn
    meta['dataset_k']=dk

    meta['clblast_engine_name']=d_engine_name
    meta['clblast_engine_package_uoa']=d_engine_package_uoa

    mmeta=copy.deepcopy(meta)

    # Extra meta which is not used to search similar case ...
    mmeta['platform_uid']=plat_uid
    mmeta['os_uid']=os_uid
    mmeta['cpu_uid']=cpu_uid
    mmeta['gpgpu_uid']=gpgpu_uid
    mmeta['user']=user

    # Check if already exists (to aggregate stats)
    aggregated_stats={}
    rduid=''
    found=False

    if o=='con':
        ck.out('')
        ck.out('Checking if results already exists in a public repo (to aggregate statistics) ...')

    record_module_uoa=cfg['record_module_uoa']

    # Find remote entry
    ii={'action':'search',
        'module_uoa':record_module_uoa,
        'repo_uoa':er,
        'remote_repo_uoa':esr,
        'search_dict':{'meta':meta}}
    rx=ck.access(ii)
    if rx['return']>0: return rx

    lst=rx['lst']
    best_gflops=-1

    if len(lst)==1:
        rduid=lst[0]['data_uid']
        found=True

        if o=='con':
           ck.out('')
           ck.out('Results found. Pre-loading aggregated stats from '+rduid+' ...')

        # Load stats
        rx=ck.access({'action':'load',
                      'module_uoa':record_module_uoa,
                      'data_uoa':rduid,
                      'repo_uoa':er,
                      'remote_repo_uoa':esr})
        if rx['return']==0:
           drx=rx['dict']
           if drx.get('best_gflops','')!='':
              best_gflops=drx['best_gflops']
        else:
           ck.out('')
           ck.out('WARNING: couldn\'t load data ('+rx['error']+')')
    else:
       rx=ck.gen_uid({})
       if rx['return']>0: return rx
       rduid=rx['data_uid']

    # Run CK pipeline *****************************************************
    pipeline=copy.deepcopy(rr)
    if len(choices)>0:
        r=ck.merge_dicts({'dict1':pipeline['choices'], 'dict2':xchoices})
        if r['return']>0: return r

    ii={'action':'autotune',
        'module_uoa':cfg['module_deps']['pipeline'],

        'data_uoa':cfg['module_deps']['program'],

        'host_os':hos,
        'target_os':tos,
        'device_id':tdid,

        'iterations':1,
        'repetitions':repetitions,

        'collect_all':'yes',
        'process_multi_keys':['##characteristics#run#statistics*'],

        'tmp_dir':tmp_dir,

        'pipeline':pipeline,

        'stat_flat_dict':aggregated_stats,

        "features_keys_to_process":["##choices#*"],

        "record_params": {
          "search_point_by_features":"yes"
        },

        'out':oo}

    rrr=ck.access(ii)
    if rrr['return']>0: return rrr

    ##characteristics#run#statistics
    ls=rrr.get('last_iteration_output',{})
    state=ls.get('state',{})
    xchoices=copy.deepcopy(ls.get('choices',{}))
    lsaf=rrr.get('last_stat_analysis',{}).get('dict_flat',{})

    # Check if has good result
    al=rrr.get('all',[])
    best_params={}
    best_time=0
    for q in al:
        qq=q.get('characteristics_list',[])
        for q1 in qq:
            bc=q1.get('run',{}).get('statistics',{}).get('best_configuration',{})
            gf=bc.get('GFLOPS','')
            if gf=='': gf='0.0'
            gf=float(gf)
            if gf>best_gflops+0.5:
               best_gflops=gf
               best_params=bc.get('parameters',{})
               best_time=bc.get('time','')

    if len(best_params)==0:
       ck.out('')
       ck.out('WARNING: no better solutions was found by CLBlast ...')
    else:   
       ddd={'meta':mmeta}

       ddd['choices']=xchoices

       ddd['best_parameters']=best_params
       ddd['best_gflops']=best_gflops
       ddd['best_time']=best_time

       features=ls.get('features',{})

       deps=ls.get('dependencies',{})

       fail=ls.get('fail','')
       fail_reason=ls.get('fail_reason','')

       # Save pipeline
       ddd['state']={'fail':fail, 'fail_reason':fail_reason}

       ddd['user']=user

       if o=='con':
          ck.out('')
          ck.out('Saving results to the remote public repo ('+rduid+') ...')

       # Update meta
       rx=ck.access({'action':'add',
                     'module_uoa':record_module_uoa,
                     'data_uoa':rduid,
                     'repo_uoa':er,
                     'remote_repo_uoa':esr,
                     'dict':ddd,
                     'sort_keys':'yes'})
       if rx['return']>0: return rx

       # Check host URL prefix and default module/action
       url=ck_url+'&highlight_uid='+rduid+'#'+rduid
       ck.out('')
       r=ck.inp({'text':'Would you like to open a browser to see results "'+url+'" (y/N)? '})
       if r['return']>0: return r

       x=r['string'].strip().lower()
       if x=='y' or x=='yes':
          import webbrowser
          webbrowser.open(url)

    return {'return':0}

##############################################################################
# show results

def show(i):
    """
    Input:  {
               (crowd_module_uoa) - if rendered from experiment crowdsourcing
               (crowd_key)        - add extra name to Web keys to avoid overlapping with original crowdsourcing HTML
               (crowd_on_change)  - reuse onchange doc from original crowdsourcing HTML
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    st=''

    cmuoa=i.get('crowd_module_uoa','')
    ckey=i.get('crowd_key','')

    conc=i.get('crowd_on_change','')
    if conc=='':
        conc=onchange

    hi_uid=i.get('highlight_uid','')

    h=''
    h+='<center>\n'
    h+='\n\n<script language="JavaScript">function copyToClipboard (text) {window.prompt ("Copy to clipboard: Ctrl+C, Enter", text);}</script>\n\n' 

    h+=hextra

    # Check host URL prefix and default module/action
    rx=ck.access({'action':'form_url_prefix',
                  'module_uoa':'wfe',
                  'host':i.get('host',''), 
                  'port':i.get('port',''), 
                  'template':i.get('template','')})
    if rx['return']>0: return rx
    url0=rx['url']
    template=rx['template']

    url=url0
    action=i.get('action','')
    muoa=i.get('module_uoa','')

    st=''

    url+='action=index&module_uoa=wfe&native_action='+action+'&'+'native_module_uoa='+muoa
    url1=url

    # List entries
    ii={'action':'search',
        'module_uoa':work['self_module_uid'],
        'add_meta':'yes'}

    if cmuoa!='':
        ii['module_uoa']=cmuoa

    r=ck.access(ii)
    if r['return']>0: return r

    lst=r['lst']

    # Check unique entries
    choices={}
    wchoices={}

    for q in lst:
        d=q['meta']
        meta=d.get('meta',{})

        for kk in selector:
            kx=kk['key']
            k=ckey+kx

            if k not in choices: 
                choices[k]=[]
                wchoices[k]=[{'name':'','value':''}]

            kflat=kk.get('flat_key','')
            if kflat=='': kflat='##'+kx

            rx=ck.get_by_flat_key({'dict':meta, 'key':kflat})
            if rx['return']>0: return rx
            v=rx['value']
            if v==None: v=''

            if v!='':
                if v not in choices[k]: 
                    choices[k].append(v)
                    wchoices[k].append({'name':v, 'value':v})

    # Prepare query div ***************************************************************
    if cmuoa=='':
        # Start form + URL (even when viewing entry)
        r=ck.access({'action':'start_form',
                     'module_uoa':cfg['module_deps']['wfe'],
                     'url':url1,
                     'name':form_name})
        if r['return']>0: return r
        h+=r['html']

    for kk in selector:
        kx=kk['key']
        k=ckey+kx
        n=kk['name']

        nl=kk.get('new_line','')
        if nl=='yes':
            h+='<br>\n<div id="ck_entries_space8"></div>\n'

        v=''
        if i.get(k,'')!='':
            v=i[k]
            kk['value']=v

        # Show hardware
        ii={'action':'create_selector',
            'module_uoa':cfg['module_deps']['wfe'],
            'data':wchoices.get(k,[]),
            'name':k,
            'onchange':conc, 
            'skip_sort':'no',
            'selected_value':v}
        r=ck.access(ii)
        if r['return']>0: return r

        h+='<b>'+n+':</b> '+r['html'].strip()+'\n'

    # Check hidden
    if hi_uid!='':
        h+='<input type="hidden" name="highlight_uid" value="'+hi_uid+'">\n'

    h+='<br><br>'

    # Prune list
    plst=[]
    for q in lst:
        d=q['meta']
        meta=d.get('meta',{})

        # Check selector
        skip=False
        for kk in selector:
            k=kk['key']
            n=kk['name']
            v=kk.get('value','')

            kflat=kk.get('flat_key','')
            if kflat=='': kflat='##'+kx

            rx=ck.get_by_flat_key({'dict':meta, 'key':kflat})
            if rx['return']>0: return rx
            vxx=rx['value']
            if vxx==None: vxx=''

            if v!='' and vxx!=v:
                skip=True

        if not skip:
            plst.append(q)

    # Check if too many
    lplst=len(plst)
    if lplst==0:
        h+='<b>No results found!</b>'
        return {'return':0, 'html':h, 'style':st}
    elif lplst>50:
        h+='<b>Too many entries to show ('+str(lplst)+') - please, prune list further!</b>'
        return {'return':0, 'html':h, 'style':st}

    # Prepare table
    h+='<table border="1" cellpadding="7" cellspacing="0">\n'

    ha='align="center" valign="top"'
    hb='align="left" valign="top"'

    h+='  <tr style="background-color:#dddddd">\n'
    h+='   <td '+ha+'><b>#</b></td>\n'
    h+='   <td '+ha+'><b>GPGPU</b></td>\n'
    h+='   <td '+ha+'><b>CPU</b></td>\n'
    h+='   <td '+ha+'><b>Platform</b></td>\n'
    h+='   <td '+ha+'><b>OS</b></td>\n'
    h+='   <td '+ha+'><b>Routine (CK wrapper)</b></td>\n'
    h+='   <td '+ha+'><b>GFLOPs</b></td>\n'
    h+='   <td '+ha+'><b>Time (s)</b></td>\n'
    h+='   <td '+ha+'><b>Dataset (M N K)</b></td>\n'
    h+='   <td '+ha+'><b>Best parameters</b></td>\n'
    h+='   <td '+ha+'><b>Choices (env)</b></td>\n'
    h+='   <td '+ha+'><b>CLBlast engine</b></td>\n'
    h+='   <td '+ha+'><b>Power consumption (W)<br>min / max</td>\n'
    h+='   <td '+ha+'><b>Memory usage (MB)</td>\n'
    h+='   <td '+ha+'><b>Bug detected?</b></td>\n'
    h+='   <td '+ha+'><b>User</b></td>\n'
    h+='   <td '+ha+'><b>Replay</b></td>\n'
    h+='  <tr>\n'

    # Dictionary to hold target meta
    tm={}

    ix=0
    bgraph={'0':[]} # Just for graph demo
    if hi_uid!='':
        bgraph['1']=[]

    # Sort
    splst=sorted(plst, key=lambda x: x.get('meta',{}).get('best_gflops',0), reverse=True)

    for q in splst:
        ix+=1

        duid=q['data_uid']
        path=q['path']

        d=q['meta']

        # Check if has statistics
        dstat={}
        fstat=os.path.join(path,'ck-stat-flat-characteristics.json')
        if os.path.isfile(fstat):
            r=ck.load_json_file({'json_file':fstat, 'dict':dstat})
            if r['return']>0: return r
            dstat=r['dict']

        x=''

        # Check if has stats
        x0=dstat.get("##characteristics#run#time_fwbw_ms#min",None)

        meta=d.get('meta',{})

        choices=d.get('choices',{})
        env=choices.get('env',{})
        params=choices.get('params',{}).get('params',{})

        best_gflops=d.get('best_gflops',0)
        best_time=d.get('best_time',0)

        xdeps=meta.get('xdeps',{})

        d_engine=xdeps.get('lib-clblast',{})
        d_engine_name=d_engine.get('data_name','')
        d_engine_package_uoa=d_engine.get('package_uoa','')
        d_engine_ver=d_engine.get('ver','')

        plat_name=meta.get('plat_name','')
        cpu_name=meta.get('cpu_name','')
        os_name=meta.get('os_name','')
        gpgpu_name=meta.get('gpgpu_name','')

        program_uoa=meta.get('program_uoa','')

        plat_uid=meta.get('platform_uid','')
        cpu_uid=meta.get('cpu_uid','')
        os_uid=meta.get('os_uid','')
        gpu_uid=meta.get('gpu_uid','')
        gpgpu_uid=meta.get('gpgpu_uid','')

        user=meta.get('user','')

        te=d.get('characteristics',{}).get('run',{})

#        bgc='afffaf'
        bgc='dfffdf'
        fail=d.get('state',{}).get('fail','')
        fail_reason=d.get('state',{}).get('fail_reason','')
        if fail=='yes':
            if fail_reason=='': fail_reason='yes'
            bgc='ffafaf'
        elif hi_uid!='' and duid==hi_uid:
            bgc='9fff9f'

#            bgraph['0'].append([ix,None])
#            bgraph['1'].append([ix,x0])

        bgraph['0'].append([ix,best_gflops])
        if fail!='yes' and best_gflops!=0 and duid!=hi_uid:
            if hi_uid!='': bgraph['1'].append([ix,best_gflops])

        bg=' style="background-color:#'+bgc+';"'

        h+='  <tr'+bg+'>\n'

        # Number
        h+='   <td '+ha+'>'+str(ix)+'</a></td>\n'

        # Platform, etc ...
        x=gpgpu_name
        if gpgpu_uid!='':
            x='<a href="'+url0+'&wcid='+cfg['module_deps']['platform.gpgpu']+':'+gpgpu_uid+'">'+x+'</a>'
        h+='   <td '+ha+'>'+x+'</td>\n'

        x=cpu_name
        if cpu_uid!='':
            x='<a href="'+url0+'&wcid='+cfg['module_deps']['platform.cpu']+':'+cpu_uid+'">'+x+'</a>'
        h+='   <td '+ha+'>'+x+'</td>\n'

        x=plat_name
        if plat_uid!='':
            x='<a href="'+url0+'&wcid='+cfg['module_deps']['platform']+':'+plat_uid+'">'+x+'</a>'
        h+='   <td '+ha+'>'+x+'</td>\n'

        x=os_name
        if os_uid!='':
            x='<a href="'+url0+'&wcid='+cfg['module_deps']['platform']+':'+os_uid+'">'+x+'</a>'
        h+='   <td '+ha+'>'+x+'</td>\n'

        x1=program_uoa
        if x1.startswith('clblast-tune-'): x1=x1[13:]
        x='<a href="'+url0+'&wcid='+cfg['module_deps']['program']+':'+program_uoa+'">'+x1+'</a>'
        h+='   <td '+ha+'>'+x+'</td>\n'

        # All files
        uu1=work['self_module_uid']
        if cmuoa!='': uu1=cmuoa
        uu2=str(ix)+')&nbsp;<a href="'+url0+'&wcid='+uu1+':'+duid+'">'+duid+'</a>'
        uu3='[&nbsp;<a href="'+url0+'&wcid='+uu1+':'+duid+'">See&nbsp;raw&nbsp;files</a>&nbsp;]'

        # GFLOPs
        h+='   <td '+ha+'>'+('%.1f'%best_gflops)+'&nbsp;&PlusMinus;&nbsp;?</a></td>\n'

        # Time
        h+='   <td '+ha+'>'+('%.3f'%best_time)+'&nbsp;&PlusMinus;&nbsp;?</a></td>\n'

        # Dataset
        x=''
        dm=meta.get('dataset_m','')
        dn=meta.get('dataset_n','')
        dk=meta.get('dataset_k','')

        x=str(dm)+'&nbsp;x&nbsp;'+str(dn)+'&nbsp;x&nbsp;'+str(dk)
        h+='   <td '+ha+'>'+x+'</a></td>\n'

        # Best parameters
        x=''
        bp=d.get('best_parameters',{})
        for k in sorted(bp):
            v=bp[k]
            x+=str(k)+'='+str(v)+'\n'
        x=x.replace("\'","'").replace("'","\\'").replace('\"','"').replace('"',"\\'").replace('\n','\\n')

        x1=''
        if x!='':
            x1+='<input type="button" class="ck_small_button" onClick="alert(\''+x+'\');" value="View all">'

        h+='   <td '+ha+'>'+x1+'</td>\n'

        # Choices (for now env)
#        x='<table border="0" cellpadding="0" cellspacing="2">\n'
        x=''
        for k in sorted(env):
            v=env[k]
            x+=str(k)+'='+str(v)+'\n'
#            x+='<tr><td>'+str(k)+'=</td><td>'+str(v)+'</td></tr>\n'
#        x+='</table>\n'
#        x=x.replace("'","\'").replace('"',"\\'").replace('\n','\\n')
        x=x.replace("\'","'").replace("'","\\'").replace('\"','"').replace('"',"\\'").replace('\n','\\n')

        x1=''
        if x!='':
            x1+='<input type="button" class="ck_small_button" onClick="alert(\''+x+'\');" value="View all">'

        h+='   <td '+ha+'>'+x1+'</td>\n'

        # Engine
        x=''
        if d_engine_ver!='':
           x+='Version&nbsp;<b><a href="'+url0+'&wcid=package:'+d_engine_package_uoa+'">'+d_engine_ver+'</a></b>'

        # Versions
        ver=''
        dver=meta.get('xversions',{})
        for dx in sorted(dver):
            vx=dver[dx]
            if vx!=None and vx!='':
               ver+=dx+': '+str(dver[dx])+'\n'

        ver=ver.replace("\'","'").replace("'","\\'").replace('\"','"').replace('"',"\\'").replace('\n','\\n')
        if ver!='':
            ver='<input type="button" class="ck_small_button" onClick="alert(\''+ver+'\');" value="See versions of all deps">'

        h+='   <td '+ha+'>'+x+'<br><br>'+ver+'</td>\n'

        # Power consumption (TBD)
        x=''

        h+='   <td '+ha+'>'+x+'</td>\n'

        # Memory usage
        x=''

        mem=dstat.get("##characteristics#run#memory_mbytes#max",None)
        if mem!=None:
           x=str(int(mem))+' MB'

        h+='   <td '+ha+'>'+x+'</td>\n'


        # Crowdsourcing bug detection
        x=fail_reason
        if x=='': 
            x=''
        else:
            fail_reason=fail_reason.replace("\'","'").replace("'","\\'").replace('\"','"').replace('"',"\\'").replace('\n','\\n')
            x='Yes <input type="button" class="ck_small_button" onClick="alert(\''+fail_reason+'\');" value="Log">'

        h+='   <td '+ha+'>'+x+'</td>\n'


        h+='   <td '+ha+'><a href="'+url0+'&action=index&module_uoa=wfe&native_action=show&native_module_uoa=experiment.user">'+user+'</a></td>\n'

        h+='   <td '+ha+'><input type="button" class="ck_small_button" onClick="copyToClipboard(\'TBD - need support in CLBlast\');" value="Replay"><br><br>\n'
        h+='              '+uu3+'</td>\n'

        h+='  <tr>\n'

    h+='</table>\n'
    h+='</center>\n'

    if cmuoa=='':
        h+='</form>\n'

    if len(bgraph['0'])>0:
       ii={'action':'plot',
           'module_uoa':cfg['module_deps']['graph'],

           "table":bgraph,

           "h_lines":[1.0],

           "ymin":0,

           "ignore_point_if_none":"yes",

           "plot_type":"d3_2d_bars",

           "display_y_error_bar":"no",

           "title":"Powered by Collective Knowledge",

           "axis_x_desc":"Experiment",
           "axis_y_desc":"GFLOPs",

           "plot_grid":"yes",

           "d3_div":"ck_interactive",

           "image_width":"900",
           "image_height":"400",

           "wfe_url":url0}

       r=ck.access(ii)
       if r['return']==0:
          x=r.get('html','')
          if x!='':
             st+=r.get('style','')

             h+='<br>\n'
             h+='<center>\n'
             h+='<div id="ck_box_with_shadow" style="width:920px;">\n'
             h+=' <div id="ck_interactive" style="text-align:center">\n'
             h+=x+'\n'
             h+=' </div>\n'
             h+='</div>\n'
             h+='</center>\n'

    return {'return':0, 'html':h, 'style':st}

##############################################################################
# replay experiment (TBD)

def replay(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    return {'return':1, 'error':'TBD: need support in CLBlast'}

##############################################################################
# browse public results

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

    import webbrowser

    ck.out('Opening web page '+ck_url+' ...')

    webbrowser.open(ck_url)

    return {'return':0}
