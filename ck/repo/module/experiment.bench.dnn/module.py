#
# Collective Knowledge: CK-powered Caffe crowdbenchmarking (very early prototyping)
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

ck_url='http://cknowledge.org/repo/web.php?native_action=show&native_module_uoa=program.optimization&scenario=1eb2f50d4620903e'
ck_url1='http://cknowledge.org/repo/web.php?wcid=experiment.bench.dnn:'

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
#hextra+=' and <a href="https://github.com/dividiti/ck-caffe">CK-Caffe GitHub repo</a> for more details!'
#hextra+='</center></i>\n'
#hextra+='<br>\n'

hextra='<i><center>\n'
hextra+=' [ <a href="http://cKnowledge.org/ai">Community-driven AI R&D powered by CK</a> ], '
hextra+=' [ <a href="https://github.com/ctuning/ck-caffe2">CK-Caffe2</a> / <a href="https://github.com/dividiti/ck-caffe">CK-Caffe</a> ], '
hextra+=' [ <a href="https://github.com/ctuning/ck-tensorflow">CK-TensorFlow</a> ], '
hextra+=' [ <a href="https://en.wikipedia.org/wiki/Collective_Knowledge_(software)">Wikipedia</a>, \n'
hextra+='<a href="https://www.researchgate.net/publication/304010295_Collective_Knowledge_Towards_RD_Sustainability">paper 1</a>, \n'
hextra+='<a href="https://arxiv.org/abs/1506.06256">Paper 2</a>, \n'
hextra+='<a href="https://www.youtube.com/watch?v=Q94yWxXUMP0">YouTube CK intro</a> ], \n'
hextra+=' [ <a href="http://dividiti.blogspot.fr/2017/02/we-received-test-of-time-award-for-our.html">CGO\'17 test of time award for our interdisiplinary R&D</a> ]'
hextra+='</center></i>\n'
hextra+='<br>\n'

selector=[{'name':'Type', 'key':'dnn_type'},
          {'name':'DNN engine', 'key':'dnn_engine_name'},
          {'name':'Model', 'key':'nn_type'},
          {'name':'Platform', 'key':'plat_name', 'new_line':'yes'},
          {'name':'CPU', 'key':'cpu_name'},
          {'name':'OS', 'key':'os_name', 'new_line':'yes'},
          {'name':'GPGPU', 'key':'gpgpu_name'}]

replay_clean_vars=['no_compile','host_os','device_id']
replay_clean_env_vars=['CK_CAFFE_MODEL','CK_CAFFE_MODEL_FILE','CK_ENV_MODEL_CAFFE_WEIGHTS']
  
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
       ii['data_uoa']='caffe'
       ii['exchange_repo']=er
       ii['exchange_subrepo']=esr
       ii['skip_welcome']='yes'
       ii['skip_log_wait']='yes'
       ii['crowdtuning_type']='caffe-crowd-benchmarking'
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
    tp=['cpu', 'cuda', 'cuda_fp16', 'opencl']

    ck.out(line)
    ck.out('Select Caffe library type:')
    ck.out('')
    r=ck.access({'action':'select_list',
                 'module_uoa':cfg['module_deps']['choice'],
                 'choices':tp})
    if r['return']>0: return r
    xtp=r['choice']

    xtp16=''
    if xtp=='cuda_fp16':
       xtp='cuda'
       xtp16='yes'

    android=False
    if 'android' in tos: android=True

    # Get extra platform features if "cuda" or "opencl"
    if android:
       run_cmd='default'
       prog_uoa='caffe-time'
    else:
       run_cmd='time_cpu'
       prog_uoa='caffe'

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

        if android:
           if xtp!='opencl':
              return {'return':1, 'error':'can\'t crowdbenchmark this type of DNN engine on selected target platform'}

           run_cmd='default'
           prog_uoa='caffe-time-opencl'
        else:
           run_cmd='time_gpu'
           if xtp16=='yes': run_cmd='time_gpu_fp16'

    # Get deps from caffe program
    r=ck.access({'action':'load',
                 'module_uoa':cfg['module_deps']['program'],
                 'data_uoa':prog_uoa})
    if r['return']>0: return r

    pp=r['path']

#    lib_dep=r['dict']['run_deps']['lib-caffe']

#    deps={'lib-caffe':lib_dep}

    # Check environment for selected type
#    r=ck.access({'action':'resolve',
#                 'module_uoa':cfg['module_deps']['env'],
#                 'deps':deps,
#                 'host_os':hos,
#                 'target_os':tos,
#                 'device_id':tdid,
#                 'out':o})
#    if r['return']>0: return r
#    deps=r['deps']

    # Prepare CK pipeline for a given workload
    ii={'action':'pipeline',

        'module_uoa':cfg['module_deps']['program'],
        'data_uoa':prog_uoa,

        'host_os':hos,
        'target_os':tos,
        'device_id':tdid,

        'skip_target':'yes',

        'prepare':'yes',

        'env':env,
        'choices':choices,
#        'dependencies':deps,
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

    # Clean pipeline
    if 'ready' in rr: del(rr['ready'])
    if 'fail' in rr: del(rr['fail'])
    if 'return' in rr: del(rr['return'])

    # Prepare high-level experiment meta
    meta={'cpu_name':cpu_name,
          'os_name':os_name,
          'plat_name':plat_name,
          'gpu_name':gpu_name,
          'dnn_type':xtp,
          'gpgpu_name':gpgpu_name,
          'cmd_key':run_cmd}

    # Process deps
    xdeps={}
    xnn=''
    xblas=''
    for k in deps:
        dp=deps[k]

        ptags=dp.get('tags',[])

        puoa=dp.get('package_uoa','')
        if puoa=='':
           puoa=dp.get('cus',{}).get('used_package_uoa','')

        dname=dp.get('dict',{}).get('data_name','')

        if k=='caffemodel':
            xnn=dname

            j1=xnn.rfind('(')
            if j1>0:
                xnn=xnn[j1+1:-1]

        xdeps[k]={'name':dp.get('name',''), 'data_name':dname, 'ver':dp.get('ver',''), 'package_uoa':puoa, 'package_tags':ptags}

    # versions of engine sub deps
    dvers={}
    mdep=deps['lib-caffe']
    mdeps=mdep.get('dict',{}).get('deps',{})

    for k in mdeps:
        dvers[k]=mdeps[k].get('ver','')

    meta['xversions']=dvers
    meta['xdeps']=xdeps
    meta['nn_type']=xnn
    meta['choices']=xchoices

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

    # Find remote entry
    ii={'action':'search',
        'module_uoa':work['self_module_uid'],
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
                      'module_uoa':work['self_module_uid'],
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

        'host_os':hos,
        'target_os':tos,
        'device_id':tdid,

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

    real_proto=xchoices.get('env',{}).get('CK_CAFFE_MODEL','') # to push to server

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

    # Add files
    ddd['file_stat']=ffstat

    if real_proto!='':
       ddd['file_model_topology']=os.path.basename(real_proto)

    if not found:
       if o=='con':
          ck.out('')
          ck.out('Saving results to the remote public repo ('+rduid+') ...')

       # Update meta
       rx=ck.access({'action':'add',
                     'module_uoa':work['self_module_uid'],
                     'data_uoa':rduid,
                     'repo_uoa':er,
                     'remote_repo_uoa':esr,
                     'dict':ddd,
                     'sort_keys':'yes'})
       if rx['return']>0: return rx

       # Push real proto
       if real_proto!='':
          if o=='con':
             ck.out('')
             ck.out('Pushing prototxt to the remote public repo ...')

          rx=ck.access({'action':'push',
                        'module_uoa':work['self_module_uid'],
                        'data_uoa':rduid,
                        'repo_uoa':er,
                        'remote_repo_uoa':esr,
                        'filename':real_proto,
                        'overwrite':'yes'})
          if rx['return']>0: return rx

    # Push statistical characteristics
    if o=='con':
       ck.out('')
       ck.out('Pushing file with statistics to server ...')

    fstat=os.path.join(pp,tmp_dir,ffstat)

    r=ck.save_json_to_file({'json_file':fstat, 'dict':lsaf, 'sort_keys':'yes'})
    if r['return']>0: return r

    rx=ck.access({'action':'push',
                  'module_uoa':work['self_module_uid'],
                  'data_uoa':rduid,
                  'repo_uoa':er,
                  'remote_repo_uoa':esr,
                  'filename':fstat,
                  'overwrite':'yes'})
    if rx['return']>0: return rx

    os.remove(fstat)

    # Info
    if o=='con':
        ck.out('')
        ck.out('Succesfully recorded results in remote repo (Entry UID='+rduid+')')
   
        # Check host URL prefix and default module/action
        url=ck_url+'&highlight_uid='+rduid
        ck.out('')
        ck.out('You can see your results at the following URL:')
        ck.out('')
        ck.out(url)

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
#    h='<hr>\n'
    h+='<center>\n'
    h+='\n\n<script language="JavaScript">function copyToClipboard (text) {window.prompt ("Copy to clipboard: Ctrl+C, Enter", text);}</script>\n\n' 

#    h+='<h2>Aggregated results from Caffe crowd-benchmarking (time, accuracy, energy, cost, ...)</h2>\n'

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
            if kflat=='': kflat='##'+k

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
    elif lplst>300:
        h+='<b>Too many entries to show ('+str(lplst)+') - please, prune list further!</b>'
        return {'return':0, 'html':h, 'style':st}

    # Prepare table
    h+='<table border="1" cellpadding="7" cellspacing="0">\n'

    ha='align="center" valign="top"'
    hb='align="left" valign="top"'

    h+='  <tr style="background-color:#dddddd">\n'
    h+='   <td '+ha+'><b>#</b></td>\n'
    h+='   <td '+ha+'><b>Platform</b></td>\n'
    h+='   <td '+ha+'><b>OS</b></td>\n'
    h+='   <td '+ha+'><b>CPU</b></td>\n'
    h+='   <td '+ha+'><b>GPGPU</b></td>\n'
    h+='   <td '+ha+'><b>Type</b></td>\n'
    h+='   <td '+ha+'><b>DNN engine</b></td>\n'
    h+='   <td '+ha+'><b>Model</b></td>\n'
    h+='   <td '+ha+'><b>Choices (env)</b></td>\n'
    h+='   <td '+ha+'><b>FWBW<br>min time</b><br><br>(exp&nbsp;time)<br>stat.&nbsp;repetitions</td>\n'
    h+='   <td '+ha+'><b>FW</b></td>\n'
    h+='   <td '+ha+'><b>BW</b></td>\n'
    h+='   <td '+ha+'><b>Per layer</b></td>\n'
    h+='   <td '+ha+'><b>HW costs</td>\n'
    h+='   <td '+ha+'><b>All usage costs (preparation, training, inference, errors, etc)</td>\n'
    h+='   <td '+ha+'><b>Model size</b></td>\n'
    h+='   <td '+ha+'><b><a href="https://github.com/dividiti/ck-caffe/blob/master/script/explore-accuracy/explore_accuracy.20160808.ipynb">Model accuracy on ImageNet</a></td>\n'
    h+='   <td '+ha+'><b>Model topology and parameters</td>\n'
    h+='   <td '+ha+'><b>Power consumption (W)<br>min&nbsp;/&nbsp;max</td>\n'
    h+='   <td '+ha+'><b>Acoustic noise (dB)<br>min&nbsp;/&nbsp;max</td>\n'
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

    # Load min stat
    for q in plst:
        pmin=os.path.join(q['path'],ffmin)
        dx={'##characteristics#run#time_fwbw_ms#min':1e99}

        if os.path.isfile(pmin):
           rx=ck.load_json_file({'json_file':pmin})
           if rx['return']==0:
              dx=rx['dict']

              # Fix
              x=dx.get('##characteristics#run#time_fwbw_ms#min','')
              if x==None or x=='' or x>50000: 
                 dx['##characteristics#run#time_fwbw_ms#min']=1e99
                 if q.get('meta',{}).get('state',{}).get('fail_reason','')=='':
                    q['meta']['state']['fail']='yes'
                    q['meta']['state']['fail_reason']='strange timing'

        q['min_stat']=dx

    # Sort
    splst=sorted(plst, key=lambda x: x.get('min_stat',{}).get('##characteristics#run#time_fwbw_ms#min',0))

#    splst=sorted(plst, key=lambda x: x.get('meta',{}).get('characteristics',{}).get('run',{}).get('time_fwbw_ms',0))

    for q in splst:
        ix+=1

        duid=q['data_uid']
        path=q['path']

        d=q['meta']

        # Characteristics
        # Check if has statistics
        dstat={}
        fstat=os.path.join(path,'ck-stat-flat-characteristics.json')
        if os.path.isfile(fstat):
            r=ck.load_json_file({'json_file':fstat, 'dict':dstat})
            if r['return']>0: return r
            dstat=r['dict']

        x0=dstat.get("##characteristics#run#time_fwbw_ms#min",None)

        meta=d.get('meta',{})

        choices=d.get('choices',{})
        env=choices.get('env',{})
        params=choices.get('params',{}).get('params',{})

        xdeps=meta.get('xdeps',{})

        d_model=xdeps.get('caffemodel',{})
        d_model_name=d_model.get('data_name','')
        d_model_package_uoa=d_model.get('package_uoa','')
        d_model_ver=d_model.get('ver','')

        d_engine=xdeps.get('lib-caffe',{})
        d_engine_name=d_engine.get('data_name','')
        d_engine_package_uoa=d_engine.get('package_uoa','')
        d_engine_ver=d_engine.get('ver','')

        tp=meta.get('dnn_type','')
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

        # Number
        h+='   <td '+ha+'><a name="'+duid+'">'+str(ix)+'</a></td>\n'

        # Platform, etc ...
        x=plat_name
        if plat_uid!='':
            x='<a href="'+url0+'&wcid='+cfg['module_deps']['platform']+':'+plat_uid+'">'+x+'</a>'
        h+='   <td '+ha+'>'+x+'</td>\n'

        x=os_name
        if os_uid!='':
            x='<a href="'+url0+'&wcid='+cfg['module_deps']['platform']+':'+os_uid+'">'+x+'</a>'
        h+='   <td '+ha+'>'+x+'</td>\n'

        x=cpu_name
        if cpu_uid!='':
            x='<a href="'+url0+'&wcid='+cfg['module_deps']['platform.cpu']+':'+cpu_uid+'">'+x+'</a>'
        h+='   <td '+ha+'>'+x+'</td>\n'

        x=gpgpu_name
        if gpgpu_uid!='':
            x='<a href="'+url0+'&wcid='+cfg['module_deps']['platform.gpgpu']+':'+gpgpu_uid+'">'+x+'</a>'
        h+='   <td '+ha+'>'+x+'</td>\n'

        # All files
        uu1=work['self_module_uid']
        if cmuoa!='': uu1=cmuoa
        uu2=str(ix)+')&nbsp;<a href="'+url0+'&wcid='+uu1+':'+duid+'">'+duid+'</a>'
        uu3='[&nbsp;<a href="'+url0+'&wcid='+uu1+':'+duid+'">See&nbsp;raw&nbsp;files</a>&nbsp;]<br><br>('+duid+')'
        uu4=uu1+':'+duid

        # Type
        h+='   <td '+ha+'>'+tp+'</a></td>\n'

        # Engine
        x=d_engine_name

        if d_engine_package_uoa!='':
           x='<a href="'+url0+'&wcid=package:'+d_engine_package_uoa+'">'+x+'</a>'

        if x!='' and d_engine_ver!='':
           x+='\n<br><br>Version&nbsp;<b>'+d_engine_ver+'</b>'

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

        # Model

        x=nn

        msize=''
        mtop=''
        mtop5=''

        if d_model_package_uoa!='':
           x='<a href="'+url0+'&wcid=package:'+d_model_package_uoa+'">'+x+'</a>'

           # Load features
           rx=ck.access({'action':'load',
                         'module_uoa':'package',
                         'data_uoa':d_model_package_uoa})
           if rx['return']==0: 
              mft=rx['dict'].get('features',{})

              msize=str(mft.get('model_size_mb',''))+'&nbsp;MB'
              mtop=str(mft.get('accuracy',''))
              mtop5=str(mft.get('accuracy_top5',''))

#        if x!='' and d_model_ver!='':
#           x+='\n<br><br>Version&nbsp;<b>'+d_model_ver+'</b>'

        h+='   <td '+ha+'>'+x+'</td>\n'

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
            if env.get('CK_CAFFE_BATCH_SIZE','')!='':
               x1+='Batch&nbsp;size='+env['CK_CAFFE_BATCH_SIZE']+'<br><br>\n'
            x1+='<input type="button" class="ck_small_button" onClick="alert(\''+x+'\');" value="View all">'

        h+='   <td '+ha+'>'+x1+'</td>\n'


        x=''

        # Check if has stats
        x0=dstat.get("##characteristics#run#time_fwbw_ms#min",None)
        x0e=dstat.get("##characteristics#run#time_fwbw_ms#exp",None)
        x1=dstat.get("##characteristics#run#time_fwbw_ms#center",None)
        xr=dstat.get("##characteristics#run#time_fwbw_ms#repeats",None)
        x2=dstat.get("##characteristics#run#time_fwbw_ms#halfrange",None)
        x=''
        if x0!=None:
            x='<b>'+('%.0f'%x0)+'&nbsp;ms.</b>\n'
#            x+='('+('%.0f'%x1)+'&nbsp;&PlusMinus;&nbsp;'+('%.0f'%x2)+'&nbsp;ms.)'

        if x0e!=None and x2!=None:
            x+='<br><br>('+('%.0f'%x0e)+'&nbsp;&PlusMinus;&nbsp;'+('%.0f'%x2)+'&nbsp;ms.)\n'

        if xr!=None:
            x+='<br><i>'+str(xr)+' repetitions</i>\n'

        h+='   <td '+ha+' style="background-color:#afffaf">'+x+'</td>\n'

        if fail=='yes': x0=0
        bgraph['0'].append([ix,x0])
        if fail!='yes' and x0!=None and duid!=hi_uid:
            if hi_uid!='': bgraph['1'].append([ix,None])

        x1=dstat.get("##characteristics#run#time_fw_ms#center",None)
        x2=dstat.get("##characteristics#run#time_fw_ms#halfrange",None)
        if x1!=None and x2!=None:
            x=('%.0f'%x1)+'&nbsp;&PlusMinus;&nbsp;'+('%.0f'%x2)+'&nbsp;ms.'

        h+='   <td '+ha+'>'+x+'</td>\n'

        x1=dstat.get("##characteristics#run#time_bw_ms#center",None)
        x2=dstat.get("##characteristics#run#time_bw_ms#halfrange",None)
        if x1!=None and x2!=None:
            x=('%.0f'%x1)+'&nbsp;&PlusMinus;&nbsp;'+('%.0f'%x2)+'&nbsp;ms.'

        h+='   <td '+ha+'>'+x+'</td>\n'

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

        # Also layers
        y5=''
        for j in range(0,1000):
            k1='##characteristics#run#per_layer_info@'+str(j)+'#direction#min'
            k2='##characteristics#run#per_layer_info@'+str(j)+'#label#min'
            k3='##characteristics#run#per_layer_info@'+str(j)+'#time_ms#min'
            k4='##characteristics#run#per_layer_info@'+str(j)+'#time_ms#max'
            k5='##characteristics#run#per_layer_info@'+str(j)+'#time_ms#exp_allx'

            v1=dstat.get(k1,'')
            v2=dstat.get(k2,'')
            v3=dstat.get(k3,'')
            v4=dstat.get(k4,'')
            v5=dstat.get(k5,[])

            if v1!='' and v2!='' and v3!='' and v4!='':
               v6=0
               if len(v5)>0:
                  v6=v5[0]

               xv3=''
               xv4=''
               xv5=''

               if v3!='': xv3=('%.1f'%v3)
               if v4!='': xv4=('%.1f'%v4)
               if v6!='': xv6=('%.1f'%v6)

               if y5=='': y5='Layers:\nName (direction): min time (ms.) ; expected time (ms.) ; max time (ms.)\n'

               y5+='\n'+v2+' ('+v1+'): '+xv3+';'+xv6+';'+xv4
            else:
               break

        y5=y5.replace("\'","'").replace("'","\\'").replace('\"','"').replace('"',"\\'").replace('\n','\\n')
        if y5!='':
            x+='<a href="'+ck_url1+duid+'">Stats per layer</a><br><br>\n'
            x+='<input type="button" class="ck_small_button" onClick="alert(\''+y5+'\');" value="All layers as pop-up">'

#        x5=x5.replace("'","\'").replace('"',"\\'").replace('\n','\\n')
        x5=x5.replace("\'","'").replace("'","\\'").replace('\"','"').replace('"',"\\'").replace('\n','\\n')
        if x5!='':
            x+='<br><br><input type="button" class="ck_small_button" onClick="alert(\''+x5+'\');" value="CK vars">'

        h+='   <td '+ha+'>'+x+'</td>\n'

        # Get info about platform
        hd={}
        if plat_uid!='':
           rh=ck.access({'action':'load',
                        'module_uoa':cfg['module_deps']['platform'],
                        'data_uoa':plat_uid})
           if rh['return']==0:
              hd=rh['dict']

        # Cost (take from platform meta)
        hc='-'
        if len(hd)>0:
           costs=hd.get('features',{}).get('cost',[])
           hc=''
           for c in costs:
               if hc!='': hc+='<br>\n'
               hc+='<b>'+str(c.get('price',''))+' '+c.get('currency','')+ '</b> - '+c.get('desc','')+' ('+c.get('date','')+')'

        h+='   <td '+ha+'>'+hc+'</a></td>\n'

        # TBD: all other costs
        h+='   <td '+ha+'></a></td>\n'

        # Model size
        h+='   <td '+ha+'>'+msize+'</td>\n'

        # Accuracy
        x=''

        if mtop!='' and mtop5!='':
           x=mtop+'&nbsp;/&nbsp;'+mtop5

#        if nn=='bvlc, alexnet':
#            x='0.568279&nbsp;/&nbsp;0.799501'
#        elif nn=='bvlc, googlenet':
#            x='0.689299&nbsp;/&nbsp;0.891441'
#        elif nn=='deepscale, squeezenet, 1.1':
#            x='0.583880&nbsp;/&nbsp;0.810123'
#        elif nn=='deepscale, squeezenet, 1.0':
#            x='0.576801&nbsp;/&nbsp;0.803903'

        h+='   <td '+ha+'>'+x+'</td>\n'

        # Model topology
        x=''

        fmt=d.get('file_model_topology','')
        if fmt!='':
           pfmt=os.path.join(path,fmt)
           if os.path.isfile(pfmt):
               x='<a href="'+url0+'&action=pull&common_action=yes&cid='+work['self_module_uid']+':'+duid+'&filename='+fmt+'">deploy.prototxt</a>\n'

        h+='   <td '+ha+'>'+x+'</td>\n'

        # Power consumption (TBD - real measurements)
        x='-'
        if len(hd)>0:
           power=hd.get('features',{}).get('power_consumption',{})
           if len(power)>0:
              pmin=power.get('min','')
              pmax=power.get('max','')

              x=str(pmin)+' / '+str(pmax)
        h+='   <td '+ha+'>'+x+'</a></td>\n'

        # Acoustic noise (TBD - real measurements)
        x='-'
        if len(hd)>0:
           power=hd.get('features',{}).get('acoustic_noise',{})
           if len(power)>0:
              pmin=power.get('min','')
              pmax=power.get('max','')

              x=str(pmin)+' / '+str(pmax)
        h+='   <td '+ha+'>'+x+'</a></td>\n'

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

        h+='   <td '+ha+'><input type="button" class="ck_small_button" onClick="copyToClipboard(\'ck replay '+uu4+' '+ck.cfg.get('add_extra_to_replay','')+'\');" value="Replay"><br><br>\n'
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

           "x_ticks_period":10,

           "axis_x_desc":"Experiment",
           "axis_y_desc":"Neural network total time (ms.)",

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

##############################################################################
# show info for all layers

def html_viewer(i):
    """
    Input:  {
              data_uoa - CK entry UOA to view
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    duoa=i.get('data_uoa','')

    # Load entry
    r=ck.access({'action':'load',
                 'module_uoa':work['self_module_uid'],
                 'data_uoa':duoa})
    if r['return']>0: return r
    p=r['path']
    d=r['dict']

    dchars=d.get('characteristics',{})
    dchoices=d.get('choices',{})
    dmeta=d.get('meta',{})

    # Load stats
    dstat={}
    fstat=os.path.join(p,'ck-stat-flat-characteristics.json')
    if os.path.isfile(fstat):
        r=ck.load_json_file({'json_file':fstat, 'dict':dstat})
        if r['return']>0: return r
        dstat=r['dict']

    # Prepare table
    h=''
#    h+='<hr>\n'
    h+='<br>\n'
    h+='<center>\n'
    h+='<h2>DNN engine and model evaluation statistics per layer (crowd-tuning)</h2><br>\n'
    h+='</center>\n'

    xdeps=dmeta.get('xdeps',{})
    lcaffe=xdeps.get('lib-caffe',{})
    lmodel=xdeps.get('caffemodel',{})

    # Prepare extra info
    h+='<p>\n'
    h+='<table border="1" cellpadding="8" cellspacing="0">\n'

    h+=' <tr>\n'
    h+='  <td><b>DNN engine name:</b></td>\n'
    h+='  <td>'+lcaffe.get('data_name','')+'</td>\n'
    h+=' </tr>\n'

    h+=' <tr>\n'
    h+='  <td><b>DNN engine version:</b></td>\n'
    h+='  <td>'+lcaffe.get('ver','')+'</td>\n'
    h+=' </tr>\n'

    h+=' <tr>\n'
    h+='  <td><b>DNN engine type:</b></td>\n'
    h+='  <td>'+dmeta.get('dnn_type','')+'</td>\n'
    h+=' </tr>\n'

    x=''

    dx=dmeta.get('xversions',{})
    for k in sorted(dx):
        v=dx[k]
        if v!='':
           if x!='': x+='<br>\n'
           x+=k+'='+str(v)+'\n'

    h+=' <tr>\n'
    h+='  <td><b>DNN engine dependencies:</b></td>\n'
    h+='  <td>'+x+'</td>\n'
    h+=' </tr>\n'

    h+=' <tr>\n'
    h+='  <td><b>DNN model name:</b></td>\n'
    h+='  <td>'+lmodel.get('data_name','')+'</td>\n'
    h+=' </tr>\n'

    h+=' <tr>\n'
    h+='  <td><b>DNN model version:</b></td>\n'
    h+='  <td>'+lmodel.get('ver','')+'</td>\n'
    h+=' </tr>\n'

    h+=' <tr>\n'
    h+='  <td><b>Batch size:</b></td>\n'
    h+='  <td>'+dchars.get('run',{}).get('REAL_ENV_CK_CAFFE_BATCH_SIZE','')+'</td>\n'
    h+=' </tr>\n'

# TBD: Need to show min,exp,max!
#    h+=' <tr>\n'
#    h+='  <td><b>FWBW time (ms.):</b></td>\n'
#    h+='  <td>'+str(dchars.get('run',{}).get('time_bw_ms',''))+'</td>\n'
#    h+=' </tr>\n'

#    h+=' <tr>\n'
#    h+='  <td><b>FW time (ms.):</b></td>\n'
#    h+='  <td>'+str(dchars.get('run',{}).get('time_fw_ms',''))+'</td>\n'
#    h+=' </tr>\n'

#    h+=' <tr>\n'
#    h+='  <td><b>BW time (ms.):</b></td>\n'
#    h+='  <td>'+str(dchars.get('run',{}).get('time_bw_ms',''))+'</td>\n'
#    h+=' </tr>\n'

    h+=' <tr>\n'
    h+='  <td><b>Platform:</b></td>\n'
    h+='  <td>'+dmeta.get('plat_name','')+'</td>\n'
    h+=' </tr>\n'

    h+=' <tr>\n'
    h+='  <td><b>OS:</b></td>\n'
    h+='  <td>'+dmeta.get('os_name','')+'</td>\n'
    h+=' </tr>\n'

    h+=' <tr>\n'
    h+='  <td><b>CPU:</b></td>\n'
    h+='  <td>'+dmeta.get('cpu_name','')+'</td>\n'
    h+=' </tr>\n'

    h+=' <tr>\n'
    h+='  <td><b>GPU:</b></td>\n'
    h+='  <td>'+dmeta.get('gpu_name','')+'</td>\n'
    h+=' </tr>\n'


    h+=' </tr>\n'
    h+='</table>\n'

    h+='<center>\n'
    h+='<p>\n'
    h+='<table border="0" cellpadding="10" cellspacing="0">\n'

    h+=' <tr>\n'
    h+='  <td><b>Name</b></td>\n'
    h+='  <td><b>Direction</b></td>\n'
    h+='  <td align="right"><b>Min time (ms.):</b></td>\n'
    h+='  <td align="right"><b>Expected time (ms.):</b></td>\n'
    h+='  <td align="right"><b>Max time (ms.):</b></td>\n'
    h+='  <td align="right"><b>Repetitions:</b></td>\n'
    h+=' </tr>\n'

    # Detecting number of layers
    jj={}

    for j in range(0,1000):
        k3='##characteristics#run#per_layer_info@'+str(j)+'#time_ms#min'
        v3=dstat.get(k3,'')

        if v3=='': break

        jj[j]=v3

    # Sorting by min time
    if i.get('all_params',{}).get('skip_sort','')!='yes':
       jj=sorted(jj, key=lambda x: jj[x], reverse=True)

    # Also layers
    for j in jj:
        k1='##characteristics#run#per_layer_info@'+str(j)+'#direction#min'
        k2='##characteristics#run#per_layer_info@'+str(j)+'#label#min'
        k3='##characteristics#run#per_layer_info@'+str(j)+'#time_ms#min'
        k4='##characteristics#run#per_layer_info@'+str(j)+'#time_ms#max'
        k5='##characteristics#run#per_layer_info@'+str(j)+'#time_ms#exp_allx'
        k7='##characteristics#run#per_layer_info@'+str(j)+'#time_ms#repeats'

        v1=dstat.get(k1,'')
        v2=dstat.get(k2,'')
        v3=dstat.get(k3,'')
        v4=dstat.get(k4,'')
        v5=dstat.get(k5,[])
        v7=dstat.get(k7,'')

        if v1!='' and v2!='' and v3!='' and v4!='':
           v6=0
           if len(v5)>0:
              v6=v5[0]

           xv3=''
           xv4=''
           xv6=''

           if v3!='':
              if v3<0.1: xv3='0'
              else: xv3='<b>'+('%.1f'%v3)+'</b>'

           if v4!='':
              if v4<0.1: xv4='0'
              else: xv4='<b>'+('%.1f'%v4)+'</b>'

           if v6!='':
              if v6<0.1: xv6='0'
              else: xv6='<b>'+('%.1f'%v6)+'</b>'

           h+=' <tr>\n'
           h+='  <td>'+v2+'</td>\n'
           h+='  <td>'+v1+'</td>\n'
           h+='  <td align="right">'+xv3+'</td>\n'
           h+='  <td align="right">'+xv6+'</td>\n'
           h+='  <td align="right">'+xv4+'</td>\n'
           h+='  <td align="right">'+str(v7)+'</td>\n'
           h+=' </tr>\n'

    h+='</table>\n'

    h+='</center>\n'

    return {'return':0, 'html':h, 'show_top':'yes'}

##############################################################################
# replay experiment (TBD)

def replay(i):
    """
    Input:  {
              (data_uoa)
              (remote)

              (host_os)
              (target_os)
              (device_id)
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

    duoa=i.get('data_uoa','')
    remote=i.get('remote','')

    er=''
    esr=''

    if remote=='yes':
       er=i.get('exchange_repo','')
       if er=='': er=ck.cfg['default_exchange_repo_uoa']
       esr=i.get('exchange_subrepo','')
       if esr=='': esr=ck.cfg['default_exchange_subrepo_uoa']

    # Try to load info
    if o=='con':
       ck.out('Loading experiment entry ...')
       ck.out('')

    r=ck.access({'action':'load',
                 'module_uoa':work['self_module_uid'],
                 'data_uoa':duoa,
                 'repo_uoa':er,
                 'remote_repo_uoa':esr})
    if r['return']>0: return r

    d=r['dict']

    hos=i.get('host_os','')
    tos=i.get('target_os','')
    tdid=i.get('device_id','')

    # Check two main deps (engine and model)
    meta=d.get('meta',{})
    xdeps=meta.get('xdeps',{})

#    TBD: rebuild env by tags!
#
#    dnn=xdeps.get('lib-caffe',{})
#    model=xdeps.get('caffemodel',{})
#
#    pdnn=dnn.get('package_uoa','')
#    pmodel=model.get('package_uoa','')
#
#    preset_env={}
#    penv=[pdnn,pmodel]
#
#    for j in range(0, len(penv)):
#        px=''
#        py=penv[j]
#
#        if py!='':
#           # Search by package
#           r=ck.access({'action':'search',
#                        'module_uoa':cfg['module_deps']['env'],
#                        'search_dict':{'package_uoa':py}})
#           if r['return']>0: return r
#
#           l=r['lst']
#
#        if j==0: preset_env['lib-caffe']=px
#        elif j==1: preset_env['caffemodel']=px

    # Run pipeline
    choices=d.get('choices',{})
    
    # Clean various vars
    for k in replay_clean_vars:
        if k in choices:
           del(choices[k])

    if i.get('target_os','')!='' and not i['target_os'].startswith('android'):
       del(i['target_os'])

    env=choices.get('env',{})
    for k in replay_clean_env_vars:
        if k in env:
           del(env[k])
    choices['env']=env

    if hos!='': choices['host_os']=hos
    if tos!='': choices['target_os']=tos
    if tdid!='': choices['device_id']=tdid

    pipeline_data_uoa=choices['module_uoa']

    # Prepare pipeline
    ii={'action':'pipeline',
        'module_uoa':cfg['module_deps']['program'],
        'prepare':'yes',
        'choices':choices,
        'out':o}
    rr=ck.access(ii)
    if rr['return']>0: return rr

    fail=rr.get('fail','')
    if fail=='yes':
        return {'return':10, 'error':'pipeline failed ('+rr.get('fail_reason','')+')'}

    ready=rr.get('ready','')
    if ready!='yes':
        return {'return':11, 'error':'couldn\'t prepare universal CK program workflow'}

    # Run pipeline
    ii={'action':'run',
        'module_uoa':cfg['module_deps']['pipeline'],
        'data_uoa':pipeline_data_uoa,
        'pipeline':rr,
        'out':o}
    rr=ck.access(ii)
    if rr['return']>0: return rr

    fail=rr.get('fail','')
    if fail=='yes':
        return {'return':10, 'error':'pipeline failed ('+rr.get('fail_reason','')+')'}

    if o=='con':
       ck.out('')
       ck.out('Your results:')
       ck.out('')

       dstat=rr.get('last_stat_analysis',{}).get('dict_flat',{})

       x0=dstat.get("##characteristics#run#time_fwbw_ms#min",None)
       x0e=dstat.get("##characteristics#run#time_fwbw_ms#exp",None)

       if x0!=None:
            ck.out('* FWBW min: '+('%.0f'%x0)+' ms.')
       if x0e!=None:
            ck.out('* FWBW exp: '+('%.0f'%x0e)+' ms.')

       x1=dstat.get("##characteristics#run#time_fw_ms#min",None)
       x1e=dstat.get("##characteristics#run#time_fw_ms#exp",None)

       if x1!=None:
            ck.out('* FW   min: '+('%.0f'%x1)+' ms.')
       if x1e!=None:
            ck.out('* FW   exp: '+('%.0f'%x1e)+' ms.')

       x2=dstat.get("##characteristics#run#time_bw_ms#min",None)
       x2e=dstat.get("##characteristics#run#time_bw_ms#exp",None)

       if x2!=None:
            ck.out('* BW   min: '+('%.0f'%x2)+' ms.')
       if x2e!=None:
            ck.out('* BW   exp: '+('%.0f'%x2e)+' ms.')

    return {'return':0}
