#
# Collective Knowledge: CK-powered TensorFlow crowdbenchmarking (very early prototyping)
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

ck_url='http://cknowledge.org/repo/web.php?native_action=show&native_module_uoa=program.optimization&scenario=bca33b04b438d756'
ck_url1='http://cknowledge.org/repo/web.php?wcid=bca33b04b438d756:'

ffstat='ck-stat-flat-characteristics.json'
ffmin='ck-stat-flat-min.json'

form_name='wa_web_form'
onchange='document.'+form_name+'.submit();'

#hextra='<i><center>\n'
#hextra+='This is an on-going long-term project. Please check our vision [ '
#hextra+='<a href="http://doi.acm.org/10.1145/2909437.2909449">IWOCL\'16</a>, \n'
#hextra+='<a href="http://arxiv.org/abs/1506.06256">CPC\'15</a>, \n'
#hextra+='<a href="https://www.youtube.com/watch?v=Q94yWxXUMP0">YouTube</a>, \n'
#hextra+='<a href="http://ctuning.org/cm/wiki/index.php?title=CM:data:45741e3fbcf4024b:1db78910464c9d05">wiki</a> ] '
#hextra+=' and <a href="https://github.com/ctuning/ck-tensorflow">CK-TensorFlow GitHub repo</a> for more details!'
#hextra+='</center></i>\n'
#hextra+='<br>\n'

hextra='<i><center>\n'
hextra+=' [ <a href="http://cKnowledge.org/ai">Collaborative unification of AI</a> ], '
hextra+=' [ <a href="https://github.com/ctuning/ck-caffe2">CK-Caffe2</a> / <a href="https://github.com/dividiti/ck-caffe">CK-Caffe</a> ], '
hextra+=' [ <a href="https://github.com/ctuning/ck-tensorflow">CK-Tensorflow</a> ], '
hextra+=' [ <a href="http://cKnowledge.org/android-apps.html">Android app</a> ], '
hextra+=' [ <a href="https://en.wikipedia.org/wiki/Collective_Knowledge_(software)">CK intro</a>, \n'
hextra+='<a href="https://www.researchgate.net/publication/304010295_Collective_Knowledge_Towards_RD_Sustainability">vision</a> and \n'
hextra+='<a href="https://arxiv.org/abs/1506.06256">crowd-tuning</a>; \n'
hextra+='<a href="https://www.youtube.com/watch?v=Q94yWxXUMP0">YouTube lecture</a> ] \n'
hextra+='</center></i>\n'
hextra+='<br>\n'

selector=[{'name':'Type', 'key':'tensorflow_type'},
          {'name':'DNN engine', 'key':'dnn_engine_name'},
          {'name':'Network', 'key':'dataset_uoa'},
          {'name':'Platform', 'key':'plat_name', 'new_line':'yes'},
          {'name':'CPU', 'key':'cpu_name'},
          {'name':'OS', 'key':'os_name', 'new_line':'yes'},
          {'name':'GPGPU', 'key':'gpgpu_name'}]

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
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import copy
    import os

    # Setting output
    o=i.get('out','')
    oo=''
    if o=='con': oo='con'

    quiet=i.get('quiet','')

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
       ii['data_uoa']='tensorflow'
       ii['exchange_repo']=er
       ii['exchange_subrepo']=esr
       ii['skip_welcome']='yes'
       ii['skip_log_wait']='yes'
       ii['crowdtuning_type']='tensorflow-crowd-benchmarking'
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
    if cpu_name=='': cpu_name='unknown-'+fcpu.get('cpu_abi','')
    cpu_uid=features.get('cpu_uid','')
    gpu_name=fgpu.get('name','')
    gpgpu_name=''
    sn=fos.get('serial_number','')

    # Ask for cmd
    tp=['cpu', 'cuda'] #, 'opencl']

    ck.out(line)
    ck.out('Select TensorFlow library type:')
    ck.out('')
    r=ck.access({'action':'select_list',
                 'module_uoa':cfg['module_deps']['choice'],
                 'choices':tp})
    if r['return']>0: return r
    xtp=r['choice'].strip()

    # Get extra platform features if "cuda" or "opencl"
    run_cmd='time_'+xtp

    tags='lib,tensorflow,tensorflow-'+xtp
    gpgpu_uid=''
    if xtp=='cuda' or xtp=='opencl':
        r=ck.access({'action':'detect',
                     'module_uoa':cfg['module_deps']['platform.gpgpu'],
                     'host_os':hos,
                     'target_os':tos,
                     'device_id':tdid,
                     'type':xtp,
                     'share':'yes',
                     'exchange_repo':er,
                     'exchange_subrepo':esr})
        if r['return']>0: return r
        gfeat=r.get('features',{})
        gpgpus=gfeat.get('gpgpu',[])

        if len(gpgpus)>0:
            gpgpu_name=gpgpus[0].get('gpgpu',{}).get('name','')
            gpgpu_uid=gpgpus[0].get('gpgpu_uoa','')

    # Get deps from TensorFlow program
    r=ck.access({'action':'load',
                 'module_uoa':cfg['module_deps']['program'],
                 'data_uoa':'tensorflow'})
    if r['return']>0: return r

    dd=r['dict']
    pp=r['path']

    # Get explicit choices (batch size, num batches)
    env=i.get('env',{})
    echoices=dd['run_vars']
    for k in echoices:
        if env.get(k,'')!='':
            echoices[k]=env[k]

    # Prepare CK pipeline for a given workload
    ii={'action':'pipeline',

        'module_uoa':cfg['module_deps']['program'],
        'data_uoa':'tensorflow',

        'prepare':'yes',

        'env':env,
        'choices':choices,
        'cmd_key':run_cmd,
        'no_state_check':'yes',
        'no_compiler_description':'yes',
        'skip_info_collection':'yes',
        'skip_calibration':'yes',
        'cpu_freq':'max',
        'gpu_freq':'max',
        'env_speed':'yes',
        'energy':'no',
        'skip_print_timers':'yes',
        'generate_rnd_tmp_dir':'no',

        'out':oo}

    rr=ck.access(ii)
    if rr['return']>0: return rr

    ds=choices.get('dataset_uoa','')

    fail=rr.get('fail','')
    if fail=='yes':
        return {'return':10, 'error':'pipeline failed ('+rr.get('fail_reason','')+')'}

    ready=rr.get('ready','')
    if ready!='yes':
        return {'return':11, 'error':'couldn\'t prepare universal CK program workflow'}

    deps=rr.get('dependencies',{})
    ydeps=deps

    # Check saved deps (if from bin package)
    xk=deps['lib-tensorflow']
    pfull=xk.get('cus',{}).get('full_path','')
    pbin=os.path.dirname(os.path.dirname(os.path.dirname(pfull)))
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
          dname=deps['lib-caffe']['dict']['data_name']

          ydeps['lib-tensorflow']['dict']=copy.deepcopy(rx['dict'])
          ydeps['lib-tensorflow']['dict']['data_name']=dname


    state=rr['state']
    tmp_dir=state['tmp_dir']

    # Clean pipeline
    if 'ready' in rr: del(rr['ready'])
    if 'fail' in rr: del(rr['fail'])
    if 'return' in rr: del(rr['return'])

    # Check if aggregted stats
    aggregated_stats={} # Pre-load statistics ...

    # Prepare high-level experiment meta
    meta={'cpu_name':cpu_name,
          'os_name':os_name,
          'plat_name':plat_name,
          'gpu_name':gpu_name,
          'tensorflow_type':xtp,
          'gpgpu_name':gpgpu_name,
          'cmd_key':run_cmd,
          'dataset_uoa':ds,
          'echoices':echoices}

    # Process deps
    xdeps={}
    xnn=''
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
    mdep=ydeps.get('lib-tensorflow',{})
    mdeps=mdep.get('dict',{}).get('deps',{})

    for k in mdeps:
        dvers[k]=mdeps[k].get('ver','')

    # Checking engine name
    d_engine=xdeps.get('lib-tensorflow',{})
    d_engine_name=d_engine.get('data_name','')
    d_engine_package_uoa=d_engine.get('package_uoa','')
    d_engine_ver=d_engine.get('ver','')

    meta['xversions']=dvers
    meta['xdeps']=xdeps
    meta['nn_type']=xnn
    meta['choices']=xchoices

    meta['dnn_engine_name']=d_engine_name
    meta['dnn_engine_package_uoa']=d_engine_package_uoa

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

    record_module_uoa=work['self_module_uid']

    # Find remote entry
    ii={'action':'search',
        'module_uoa':record_module_uoa,
        'repo_uoa':er,
        'remote_repo_uoa':esr,
        'search_dict':{'meta':meta}}
    rx=ck.access(ii)
    if rx['return']>0: return rx

    lst=rx['lst']

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
                      'remote_repo_uoa':esr,
                      'load_extra_json_files':[ffstat]})
        if rx['return']==0:
           aggregated_stats=rx.get('extra_json_files',{}).get(ffstat,{})
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

        'iterations':1,
        'repetitions':repetitions,

        'collect_all':'yes',
        'process_multi_keys':['##characteristics#*'],

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

    ls=rrr.get('last_iteration_output',{})
    state=ls.get('state',{})
    xchoices=copy.deepcopy(ls.get('choices',{}))
    lsaf=rrr.get('last_stat_analysis',{}).get('dict_flat',{})

    ddd={'meta':mmeta}

    ddd['choices']=xchoices

    features=ls.get('features',{})

    deps=ls.get('dependencies',{})

    fail=ls.get('fail','')
    fail_reason=ls.get('fail_reason','')

    ch=ls.get('characteristics',{})

    # Save pipeline
    ddd['state']={'fail':fail, 'fail_reason':fail_reason}
    ddd['characteristics']=ch

    ddd['user']=user

    if not found:
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


    # Push statistical characteristics
    x0=lsaf.get("##characteristics#run#time_fwbw_norm#min",None)

    if x0!=None and x0>0:
       if o=='con':
          ck.out('')
          ck.out('Pushing file with statistics to server ...')

       fstat=os.path.join(pp,tmp_dir,ffstat)

       r=ck.save_json_to_file({'json_file':fstat, 'dict':lsaf, 'sort_keys':'yes'})
       if r['return']>0: return r

       rx=ck.access({'action':'push',
                     'module_uoa':record_module_uoa,
                     'data_uoa':rduid,
                     'repo_uoa':er,
                     'remote_repo_uoa':esr,
                     'filename':fstat,
                     'overwrite':'yes'})
       if rx['return']>0: return rx

       os.remove(fstat)

       # Push statistical characteristics

       dmin={"##characteristics#run#time_fwbw_norm#min":x0}

       if o=='con':
          ck.out('')
          ck.out('Pushing file with min stats to server ...')

       fmin=os.path.join(pp,tmp_dir,ffmin)

       r=ck.save_json_to_file({'json_file':fmin, 'dict':dmin, 'sort_keys':'yes'})
       if r['return']>0: return r

       rx=ck.access({'action':'push',
                     'module_uoa':record_module_uoa,
                     'data_uoa':rduid,
                     'repo_uoa':er,
                     'remote_repo_uoa':esr,
                     'filename':fmin,
                     'overwrite':'yes'})
       if rx['return']>0: return rx

       os.remove(fmin)

       if o=='con':
           ck.out('')
           ck.out('Succesfully recorded results in remote repo (Entry UID='+rduid+')')
    else:
       if o=='con':
           ck.out('')
           ck.out('WARNING: did not record results to remote repo (Entry UID='+rduid+')')

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

    h='<hr>\n'
    h+='<center>\n'
    h+='\n\n<script language="JavaScript">function copyToClipboard (text) {window.prompt ("Copy to clipboard: Ctrl+C, Enter", text);}</script>\n\n' 

    h+='<h2>Aggregated results from TensorFlow crowd-benchmarking (time, accuracy, energy, cost, ...)</h2>\n'

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

            v=meta.get(kx,'')
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
        k=ckey+kk['key']
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

            if v!='' and meta.get(k,'')!=v:
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
    h+='   <td '+ha+'><b>All raw files</b></td>\n'
    h+='   <td '+ha+'><b>Type</b></td>\n'
    h+='   <td '+ha+'><b>DNN engine</b></td>\n'
    h+='   <td '+ha+'><b>Network</b></td>\n'
    h+='   <td '+ha+'><b>Batch size</b></td>\n'
    h+='   <td '+ha+'><b>Num batches</b></td>\n'
    h+='   <td '+ha+'><b>FWBW time (sec.)</b></td>\n'
    h+='   <td '+ha+'><b>FW time (sec.)</b></td>\n'
    h+='   <td '+ha+'><b>Chars</b></td>\n'
    h+='   <td '+ha+'><b>Platform</b></td>\n'
    h+='   <td '+ha+'><b>CPU</b></td>\n'
    h+='   <td '+ha+'><b>GPGPU</b></td>\n'
    h+='   <td '+ha+'><b>OS</b></td>\n'
    h+='   <td '+ha+'><b>Fail?</b></td>\n'
    h+='   <td '+ha+'><b>User</b></td>\n'
    h+='   <td '+ha+'><b>Replay</b></td>\n'
    h+='  <tr>\n'

    # Dictionary to hold target meta
    tm={}

    ix=0
    bgraph={'0':[]} # Just for graph demo
    if hi_uid!='':
        bgraph['1']=[]

    # Load min stat
    for q in plst:
        pmin=os.path.join(q['path'],ffmin)
        dx={'##characteristics#run#time_fwbw_norm#min':1e99}

        if os.path.isfile(pmin):
           rx=ck.load_json_file({'json_file':pmin})
           if rx['return']==0:
              dx=rx['dict']

              # Fix
              x=dx.get('##characteristics#run#time_fwbw_norm#min','')
              if x==None or x=='' or x>50000: 
                 dx['##characteristics#run#time_fwbw_norm#min']=1e99
                 if q.get('meta',{}).get('state',{}).get('fail_reason','')=='':
                    q['meta']['state']['fail']='yes'
                    q['meta']['state']['fail_reason']='strange timing'

        q['min_stat']=dx

    # Sort
    splst=sorted(plst, key=lambda x: x.get('min_stat',{}).get('##characteristics#run#time_fwbw_norm#min',0))

    for q in splst:
        ix+=1

        duid=q['data_uid']
        path=q['path']

        d=q['meta']

        meta=d.get('meta',{})

        params=d.get('choices',{}).get('params',{}).get('params',{})

        tp=meta.get('tensorflow_type','')
        nn=meta.get('nn_type','')

        plat_name=meta.get('plat_name','')
        cpu_name=meta.get('cpu_name','')
        os_name=meta.get('os_name','')
        gpgpu_name=meta.get('gpgpu_name','')

        plat_uid=meta.get('platform_uid','')
        cpu_uid=meta.get('cpu_uid','')
        os_uid=meta.get('os_uid','')
        gpu_uid=meta.get('gpu_uid','')
        gpgpu_uid=meta.get('gpgpu_uid','')

        ds=meta.get('dataset_uoa','')

        echoices=meta.get('echoices',{})

        bs=echoices.get('BATCH_SIZE','')
        nb=echoices.get('NUM_BATCHES','')

        xdeps=meta.get('xdeps',{})

        d_engine=xdeps.get('lib-tensorflow',{})
        d_engine_name=d_engine.get('data_name','')
        d_engine_package_uoa=d_engine.get('package_uoa','')
        d_engine_ver=d_engine.get('ver','')

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

        bg=' style="background-color:#'+bgc+';"'

        h+='  <tr'+bg+'>\n'

        x=work['self_module_uid']
        if cmuoa!='': x=cmuoa
        h+='   <td '+ha+'>'+str(ix)+')&nbsp;<a href="'+url0+'&wcid='+x+':'+duid+'">'+duid+'</a></td>\n'

        h+='   <td '+ha+'>'+tp+'</a></td>\n'

        h+='   <td '+ha+'>'+d_engine_name+'<br><i>('+d_engine_ver+')</i></a></td>\n'

        h+='   <td '+ha+'>'+ds+'</a></td>\n'

        # Characteristics
        # Check if has statistics
        dstat={}
        fstat=os.path.join(path,'ck-stat-flat-characteristics.json')
        if os.path.isfile(fstat):
            r=ck.load_json_file({'json_file':fstat, 'dict':dstat})
            if r['return']>0: return r
            dstat=r['dict']

        h+='   <td '+ha+'>'+str(bs)+'</td>\n'
        h+='   <td '+ha+'>'+str(nb)+'</td>\n'

        x=''

        # Check if has stats
        x0=dstat.get("##characteristics#run#time_fwbw_norm#min",None)
        x0e=dstat.get("##characteristics#run#time_fwbw_norm#exp",None)
        x1=dstat.get("##characteristics#run#time_fwbw_norm#center",None)
        xr=dstat.get("##characteristics#run#time_fwbw_norm#repeats",None)
        x2=dstat.get("##characteristics#run#time_fwbw_norm#halfrange",None)
        x=''
        if x0!=None:
            x='<b>'+('%.3f'%x0)+'&nbsp;</b>\n'

        if x0e!=None and x2!=None:
            x+='<br><br>('+('%.3f'%x0e)+'&nbsp;&PlusMinus;&nbsp;'+('%.3f'%x2)+')\n'

        if xr!=None:
            x+='<br><i>'+str(xr)+'&nbsp;repetitions</i>\n'

        h+='   <td '+ha+'>'+x+'</td>\n'

        x0=dstat.get("##characteristics#run#time_fw_norm#min",None)
        x0e=dstat.get("##characteristics#run#time_fw_norm#exp",None)
        x1=dstat.get("##characteristics#run#time_fw_norm#center",None)
        xr=dstat.get("##characteristics#run#time_fw_norm#repeats",None)
        x2=dstat.get("##characteristics#run#time_fw_norm#halfrange",None)
        x=''
        if x0!=None:
            x='<b>'+('%.3f'%x0)+'&nbsp;</b>\n'

        if x0e!=None and x2!=None:
            x+='<br><br>('+('%.3f'%x0e)+'&nbsp;&PlusMinus;&nbsp;'+('%.3f'%x2)+')\n'

        if xr!=None:
            x+='<br><i>'+str(xr)+'&nbsp;repetitions</i>\n'

        h+='   <td '+ha+'>'+x+'</td>\n'

#        if fail!='yes' and x0!=None and duid!=hi_uid:
#            bgraph['0'].append([ix,x0])
#            if hi_uid!='': bgraph['1'].append([ix,None])

        if fail=='yes': x0=0
        bgraph['0'].append([ix,x0])
        if fail!='yes' and x0!=None and duid!=hi_uid:
            if hi_uid!='': bgraph['1'].append([ix,None])

        # Check all characteristics
        x=''
        x5=''
        for k in sorted(te):
            v=te[k]

            kx="##characteristics#run#"+k

            kx1=dstat.get(kx+'#center',None)
            kx2=dstat.get(kx+'#halfrange',None)

            x6=''
            if type(v)==int:
                if kx1!=None and kx2!=None:
                    x6=str(kx1)+' +- '+str(kx2)
                else:
                    x6=str(v)
            elif type(v)==float:
                if kx1!=None and kx2!=None:
                    x6=('%.1f'%kx1)+' +- '+('%.1f'%kx2)
                else:
                    x6=('%.1f'%v)

            if x6!='':
                x5+=str(k)+'='+x6+'\n'

#        x5=x5.replace("'","\'").replace('"',"\\'").replace('\n','\\n')
        x5=x5.replace("\'","'").replace("'","\\'").replace('\"','"').replace('"',"\\'").replace('\n','\\n')
        if x5!='':
            x+='<input type="button" class="ck_small_button" onClick="alert(\''+x5+'\');" value="All">'

        h+='   <td '+ha+'>'+x+'</td>\n'

        # Platform, etc ...
        x=plat_name
        if plat_uid!='':
            x='<a href="'+url0+'&wcid='+cfg['module_deps']['platform']+':'+plat_uid+'">'+x+'</a>'
        h+='   <td '+ha+'>'+x+'</td>\n'

        x=cpu_name
        if cpu_uid!='':
            x='<a href="'+url0+'&wcid='+cfg['module_deps']['platform.cpu']+':'+cpu_uid+'">'+x+'</a>'
        h+='   <td '+ha+'>'+x+'</td>\n'

        x=gpgpu_name
        if gpgpu_uid!='':
            x='<a href="'+url0+'&wcid='+cfg['module_deps']['platform.gpgpu']+':'+gpgpu_uid+'">'+x+'</a>'
        h+='   <td '+ha+'>'+x+'</td>\n'

        x=os_name
        if os_uid!='':
            x='<a href="'+url0+'&wcid='+cfg['module_deps']['platform']+':'+os_uid+'">'+x+'</a>'
        h+='   <td '+ha+'>'+x+'</td>\n'

        x=fail_reason
        if x=='': 
            x='No'
        else:
            fail_reason=fail_reason.replace("\'","'").replace("'","\\'").replace('\"','"').replace('"',"\\'").replace('\n','\\n')
            x='Yes <input type="button" class="ck_small_button" onClick="alert(\''+fail_reason+'\');" value="Log">'

        h+='   <td '+ha+'>'+x+'</td>\n'

        # Params
#        x='<table border="0" cellpadding="0" cellspacing="2">\n'
        x=''
        for k in sorted(params):
            v=params[k]
            x+=str(k)+'='+str(v)+'\n'
#            x+='<tr><td>'+str(k)+'=</td><td>'+str(v)+'</td></tr>\n'
#        x+='</table>\n'
#        x=x.replace("'","\'").replace('"',"\\'").replace('\n','\\n')
        x=x.replace("\'","'").replace("'","\\'").replace('\"','"').replace('"',"\\'").replace('\n','\\n')

        x1=''
        if x!='':
            x1='<input type="button" class="ck_small_button" onClick="alert(\''+x+'\');" value="See">'

#        h+='   <td '+ha+'>'+x1+'</td>\n'

        h+='   <td '+ha+'><a href="'+url0+'&action=index&module_uoa=wfe&native_action=show&native_module_uoa=experiment.user">'+user+'</a></td>\n'

        h+='   <td '+ha+'><input type="button" class="ck_small_button" onClick="copyToClipboard(\'TBD\');" value="Replay"></td>\n'

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
           "axis_y_desc":"Neural network total time (sec.)",

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

    # TBD - take params from remote/local experiment and pre-set ...
    # Run locally, i.e. do not share stats unless requested ...

    i['action']='crowdsource'
    i['module_uoa']=cfg['module_deps']['experiment.bench.tensorflow']

    return ck.access(i)
