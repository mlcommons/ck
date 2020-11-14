#
# Collective Knowledge (program optimization)
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
line='****************************************************************'

welcome   = "Computer systems become very inefficient" \
            " due to too many design and optimization choices available - " \
            " optimizing compilers are simply not keeping pace with all this complexity and rapidly evolving hardware and software." \
            " It is possible to speed up code from 15% to more than 10x while considerably reducing energy usage and code size" \
            " for many popular algorithms (DNN, vision processing, BLAS) using multi-objective autotuning (compiler optimizations, " \
            " OpenCL/CUDA/OpenMP/MPI/algorithm parameters)." \
            " Unfortunately, it can be untolerably slow and there is a lack of realistic workloads.\n\n" \
            "Therefore, we have developed this CK-based experimental workflow for collaborative program autotuning and machine learning"  \
            " across diverse hardware and environments kindly provided by volunteers." \
            " Furthermore, users can share their own realistic workloads to participate in crowd-tuning.\n" 

welcome1  = "NOTE: this program will send some anonymized info about your hardware and OS features" \
            " to the public Collective Knowledge Server to select unexplored optimization points" \
            " or validate previously found optimizations!\n\n" \
            "You can find more info about optimization crowdsourcing including results here:\n" \
            " * http://cTuning.org/crowdsource-optimization\n\n" \
            "We would like to appologize in advance if this program will crash your system (very rare when using OpenCL/OpenGL)!\n" \
            "We would like to sincerely thank you for participating in this community effort" \
            " and help us optimize computer systems to accelerate knowledge discovery and boost innovation " \
            " in science and technology while making our planet greener!\n\n" \

wscenario='scenario'
wprune='pruning'

fstats='stats.json'
fsummary='summary.json'
fclassification='classification.json'
fgraph='tmp-reactions-graph.json'
fsolutions='tmp-solutions.json'

iuoa='index'

key_prune='__web_prune__'

opt_keys=['gcc','llvm','opencl','opengl','cuda','icc','pgi','openmp','mpi','bugs']

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
# test remote access

def test(i):
    """
    Input:  {
              (email)      - optional email
              (type)       - crowdtuning type (mobile,compiler/OpenCL)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              status       - string with status
            }

    """

    import os

    o=i.get('out','')

    status="CK server works fine!";

    email=i.get('email','')
    user=email

    tp=i.get('type','')

    ii={'action':'log', 'module_uoa':cfg['module_deps']['experiment'], 'file_name':cfg['log_file_test'], 'text':email}
    r=ck.access(ii)
    if r['return']>0: return r

    # Time
    r=ck.get_current_date_time({})
    if r['return']>0: return r

    idt=r['iso_datetime']

    # Load/create and lock
    # Hack
    bak1=ck.cfg["forbid_writing_to_local_repo"]
    ck.cfg["forbid_writing_to_local_repo"]="no"

    bak2=ck.cfg["allow_writing_only_to_allowed"]
    ck.cfg["allow_writing_only_to_allowed"]="no"

    ii={'action':'load',
        'common_func':'yes',
        'module_uoa': cfg['module_deps']['experiment.user'],
        'data_uoa':'all',
        'get_lock':'yes',
        'create_if_not_found':'yes',
        'lock_expire_time':20
       }
    r=ck.access(ii)
    if r['return']>0: return r

    d=r['dict']
    lock_uid=r['lock_uid']

    du=d.get('users',{})
    dt=d.get('timeline',[])

    if user!='' and user!='-' and user not in du:
       du[user]={}
       d['users']=du

       pack={}
       pack['user']=user
       pack['type']=tp
       pack['iso_datetime']=idt
       pack['new_user']='yes'
       dt.append(pack)

       d['timeline']=dt

    ii={'action':'update',
        'common_func':'yes',
        'module_uoa': cfg['module_deps']['experiment.user'],
        'data_uoa':'all',
        'ignore_update':'yes',
        'sort_keys':'yes',
        'dict':d,
        'substitute':'yes',
        'unlock_uid':lock_uid
       }
    r=ck.access(ii)
    if r['return']>0: return r

    ck.cfg["forbid_writing_to_local_repo"]=bak1
    ck.cfg["allow_writing_only_to_allowed"]=bak2

    if o=='con':
       ck.out(status)

    return {'return':0, 'status':status}

##############################################################################
# explore program optimizations

def explore(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    ck.out('')
    ck.out('Command line: ')
    ck.out('')

    import json
    cmd=json.dumps(i, indent=2)

    ck.out(cmd)

    return {'return':0}

##############################################################################
# crowdsource program optimization

def crowdsource(i):
    """
    Input:  {
              (host_os)                    - host OS (detect, if omitted)
              (target_os)                  - OS module to check (if omitted, analyze host)
              (device_id)                  - device id if remote (such as adb)

              (once)                       - if 'yes', run scenario once (useful for autotuning a given program)

              (iterations)                 - limit number of iterations, otherwise infinite (default=30)
                                             if -1, infinite (or until all choices are explored)

              (repetitions)                - statistical repetitions of a given experiment

              (local_autotuning)           - if 'yes', local autotuning instead of collaborative optimization

              (quiet)                      - do not ask questions, but select random ...
              (skip_welcome)               - if 'yes', do not print welcome header

              (skip_exchange)              - if 'yes', do not exchange platform info
                                            (development mode)

              (record_repo)                - repo where to search/record local experiments 
                                             ("local" by default, to avoid polluting other repos)

              (user)                       - user email/ID to record solutions (attribute found good solutions)

              (local)                      - if 'yes', use local repo for exchange (local autotuning/benchmarking)
              (exchange_repo)              - which repo to record/update info (remote-ck by default)
              (exchange_subrepo)           - if remote, remote repo UOA

              (force_platform_name)        - if !='', use this for platform name

              (scenario)                   - module UOA of crowdsourcing scenario
              (scenario_cfg)               - cfg of a scenario

              (seed)                       - autotuning seed

              (program_tags)               - force selection of programs by tags

              (program_uoa)                - force program UOA
              (cmd_key)                    - CMD key
              (dataset_uoa)                - dataset UOA
              (dataset_file)               - dataset filename (if more than one inside one entry - suggest to have a UID in name)
              (extra_dataset_tags)         - list of extra data set tags (useful to set "small" during mobile phone crowdtuning)

              (calibration_time)           - change calibration time (deafult 10 sec.)

              (objective)                  - extension to flat characteristics (min,exp,mean,center) to tune on Pareto
                                             (default: min - to see what we can squeeze from a given architecture)

              (keep_tmp)                   - if 'yes', do not remove run batch

              (ask_pipeline_choices)       - if 'yes', ask for each pipeline choice, otherwise random selection 

              (experiment_meta)            - meta when recording experiment
              (experiment_meta_extra)      - extra meta such as platform UIDs

              (record_uoa)                 - use this UOA to recrod experiments instead of randomly generated ones

              (compiler_description_uoa)   - force compiler description UOA (see module "compiler")

              (flag_tags)                  - extra flag tags (must have)
              (any_flag_tags)              - extra flag tags (any of these)

              (pause_if_fail)              - if pipeline fails, ask to press Enter
                                             (useful to analyze which flags fail during compiler flag autotuning)

              (omit_probability)           - probability to omit optimization (for example, compiler flags during exploration/crowdtuning)
              (parametric_flags)           - if 'yes', also tune parametric flags
              (cpu_flags)                  - if 'yes', also tune cpu-specific flags

              (compiler_env_uoa)           - fix compiler environment

              (new)                        - if 'yes', do not search for existing experiment, but start new

              (solutions)                  - list of solutions
              (solutions_info)             - info (repo_uoa, module_uoa, data_uoa)

              (gcc)                        - add tag 'gcc' to search optimization crowdsourcing scenarios
              (llvm)                       - add tag 'llvm' to search optimization crowdsourcing scenarios
              (opencl)                     - add tag 'opencl' to search optimization crowdsourcing scenarios
              (cuda)                       - add tag 'cuda' to search optimization crowdsourcing scenarios
              (openmp)                     - add tag 'openmp' to search optimization crowdsourcing scenarios
              (mpi)                        - add tag 'mpi' to search optimization crowdsourcing scenarios
              (tbb)                        - add tag 'tbb' to search optimization crowdsourcing scenarios
              (opengl)                     - add tag 'opengl' to search optimization crowdsourcing scenarios
              (bugs)                       - add tag 'bugs' to search optimization crowdsourcing scenarios
              (explore)                    - add tags 'explore' to search optimization crowdsourcing scenarios
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    tags='crowdsource,experiments,program optimization'
    if i.get('local_autotuning','')=='yes': 
       tags='program optimization,autotuning'

    extra_tags=i.get('extra_tags','')
    if extra_tags!='':
       tags+=','+extra_tags

    for q in cfg['opt_keys']:
        if i.get(q,'')=='yes':
           if tags!='': tags+=','
           tags+=q

    i['tags']=tags
    i['module_uoa']=cfg['module_deps']['experiment']

    return ck.access(i)

##############################################################################
# viewing entries as html

def show(i):
    """
    Input:  {
              scenario

              (widget)        - if 'yes', use as embedded widget
              (prepared_url0) - pre-defined URL0 if widget
              (prepared_url1) - pre-defined URL1 if widget
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              html         - generated HTML
            }

    """

    import os
    import copy

    widget=False
    if i.get('widget','')=='yes': widget=True

    sh=i.get('skip_html','')

    form_name='ck_cresults_form'
    onchange='document.'+form_name+'.submit();'

    h='<center>'
    st=''

    if not widget:
#       h+='<h2>Public experiments crowdsourced and shared using CK workflow framework</h2>\n'

       # Check host URL prefix and default module/action
       rx=ck.access({'action':'form_url_prefix',
                     'module_uoa':'wfe',
                     'host':i.get('host',''), 
                     'port':i.get('port',''), 
                     'template':i.get('template','')})
       if rx['return']>0: return rx
       url0=rx['url']

       url=url0
       action=i.get('action','')
       muoa=i.get('module_uoa','')

       url+='action=index&module_uoa=wfe&native_action='+action+'&'+'native_module_uoa='+muoa
       url1=url

       # Prepare query div ***************************************************************
       # Start form + URL (even when viewing entry)
       r=ck.access({'action':'start_form',
                    'module_uoa':cfg['module_deps']['wfe'],
                    'url':url1,
                    'name':form_name})
       if r['return']>0: return r
       h+=r['html']
    else:
       url0=i.get('prepared_url0','')
       url1=i.get('prepared_url1','')
       form_name=i.get('prepared_form_name','')
       onchange='document.'+form_name+'.submit();'

    # Listing available crowdsourcing scenarios ...
    scenario=i.get('scenario','')

    if scenario=='': 
       # Check if has local var
       scenario=ck.cfg.get('default_crowdtuning_scenario','')

    if scenario=='':
#       scenario=cfg['module_deps']['experiment.tune.compiler.flags.llvm.e']
       scenario=cfg['module_deps']['experiment.tune.compiler.flags.gcc.e']

    scenario_tags='crowdsource,experiments,program optimization'
    if i.get('prepared_scenario_tags','')!='':
       scenario_tags+=','+i['prepared_scenario_tags']

    ii={'action':'search',
        'module_uoa':cfg['module_deps']['module'],
        'add_meta':'yes',
        'add_info':'yes',
        'tags':scenario_tags}
    r=ck.access(ii)
    if r['return']>0: return r

    xls=r['lst']

    url5=ck.cfg.get('wiki_data_web','')

    results=[]

    if len(xls)==0:
       h+='<b>Can\'t find any local experiment crowdsourcing scenarios ...</b>'
    else:
       ls=sorted(xls, key=lambda v: (int(v.get('meta',{}).get('priority',0)), v['data_uoa']))

       ii={'action':'convert_ck_list_to_select_data',
           'module_uoa':cfg['module_deps']['wfe'],
           'lst':ls, 
           'add_empty':'yes',
           'sort':'no',
           'value_uoa':scenario,
           'ignore_remote':'yes'}
       r=ck.access(ii)
       if r['return']>0: return r
       dls=r['data']
       if r.get('value_uid','')!='': scenario=r['value_uid']

       if scenario=='': scenario=ls[0]['data_uid']

       ii={'action':'create_selector',
           'module_uoa':cfg['module_deps']['wfe'],
           'data':dls,
           'name':wscenario,
           'onchange':onchange, 
           'skip_sort':'yes',
#           'style':'width:400px;',
           'selected_value':scenario}
       r=ck.access(ii)
       if r['return']>0: return r
       h+='<b>Select CK-powered unified experimental workflow:</b> '+r['html']

       h+='</center>\n'

       if not widget:
#          h+='<hr>\n'

          rx=links({})
          if rx['return']>0: return rx
          h+=rx['html']

       h+='\n'

       # Check scenario
       if scenario!='':
          # Load scenario
          ii={'action':'load',
              'module_uoa':cfg['module_deps']['module'],
              'data_uoa':scenario}
          r=ck.access(ii)
          if r['return']>0: return r
          ds=r['dict']

          eh=ds.get('external_html',{})
          ehmuoa=eh.get('module_uoa','')
          if ehmuoa!='':
              ii=copy.deepcopy(i)
              ii.update(eh)
              ii['crowd_module_uoa']=scenario
              ii['crowd_on_change']=onchange

              r=ck.access(ii)
              if r['return']>0: return r
              h+=r['html']
              st+=r.get('style','')

              return {'return':0, 'html':h, 'style':st}

          # Get replay description + first key
          ik=ds.get('improvements_keys',[])
          ik0=''
          if len(ik)>0:
             ik0=ik[0]

          xxmuoa=ds.get('replay_desc',{}).get('module_uoa','')
          xxkey=ds.get('replay_desc',{}).get('desc_key','')

          pdesc={}
          if xxmuoa!='':
             r=ck.access({'action':'load',
                          'module_uoa':cfg['module_deps']['module'],
                          'data_uoa':xxmuoa})
             if r['return']>0: return r
             pdesc=r.get('desc',{})
             if xxkey!='': pdesc=pdesc.get(xxkey,{})

          pr=ds.get('prune_results',[])
          ipr=len(pr)
          if ipr>0:
             rl=[]

             # Try to find index
             ii={'action':'load',
                 'module_uoa':scenario,
                 'data_uoa':iuoa}
             rx=ck.access(ii)
             if rx['return']==0:
                p=rx['path']

                mprune={}

                px=os.path.join(p, fstats)
                if os.path.isfile(px):
                   rx=ck.load_json_file({'json_file':px})
                   if rx['return']>0: return rx
                   dd=rx['dict']

                   mm=dd.get('meta',{})

                   h+='<center>\n'
                   h+='<div id="ck_box_with_shadow1">\n'
                   h+='<center><b>Prune solutions by </b></small>\n'

#                   h+='<table border="0" cellpadding="5" cellspacing="0">\n'
                   for q in pr:
                       qd=q.get('desc','')
                       qi=q.get('id','')

                       l=mm.get(qi,{})

                       kk=key_prune+qi
                       vv=i.get(kk,'')

                       if vv!='':
                          mprune[qi]=vv

                       dt=[{'name':'', 'value':''}]
                       for k in sorted(l):
                           dt.append({'name':k, 'value':k}) 

                       ii={'action':'create_selector',
                           'module_uoa':cfg['module_deps']['wfe'],
                           'data':dt,
                           'name':kk,
                           'onchange':onchange, 
                           'skip_sort':'yes',
                           'selected_value':vv}
                       r=ck.access(ii)
                       if r['return']>0: return r

#                       h+=' <tr><td>'+qd+':</td><td>'+r['html']+'</td></tr>\n'
                       h+=qd+': '+r['html']+' \n'


#                   h+='</table>\n'
                   h+='</center></div>\n'
                   h+='<p>\n'
                   h+='</center>\n'

                # Prune
                ii={'action':'search',
                    'common_func':'yes',
                    'module_uoa': scenario,
                    'search_dict':{'meta':mprune},
                    'add_meta':'yes'
                   }
                r=ck.access(ii)
                if r['return']>0: return r
                rl=r['lst']

                if ipr==1:
                   rl=sorted(rl, key=lambda a: a.get('meta',{}).get('meta',{}).get(pr[0]['id'],''), reverse=pr[0].get('reverse',False))
                elif ipr==2:
                   rl=sorted(rl, key=lambda a: (a.get('meta',{}).get('meta',{}).get(pr[0]['id'],''), \
                                                a.get('meta',{}).get('meta',{}).get(pr[1]['id'],'')), reverse=pr[0].get('reverse',False))
                elif ipr>2:
                   rl=sorted(rl, key=lambda a: (a.get('meta',{}).get('meta',{}).get(pr[0]['id'],''), \
                                                a.get('meta',{}).get('meta',{}).get(pr[1]['id'],''), \
                                                a.get('meta',{}).get('meta',{}).get(pr[2]['id'],'')), reverse=pr[0].get('reverse',False))

             irl=len(rl)
             if irl==0:
                h+='<center><br><br><b>Public solutions are not yet shared/found!</b><br><br><br></center>'
             else:
#                   h+=str(len(rl))+' entries found!</b>'

                if irl>100: 
                   h+=str(irl)+' entries found - showing first 100!</b>'
                   irl=100

               # Check host URL prefix and default module/action
#                url0=ck.cfg.get('wfe_url_prefix','')

                h+='<center>\n'
                h+='<table class="ck_table" border="0">\n'

                h+=' <tr style="background-color:#cfcfff;">\n'
                h+='  <td><b>\n'
                h+='   #\n'
                h+='  </b></td>\n'

                h+='  <td><b>\n'
                h+='   <a href="'+url0+'wcid='+scenario+':">UID</a>\n'
                h+='  </b></td>\n'

                h+='  <td align="center"><b>\n'
                h+='   <a href="'+cfg['url_discuss']+'">Discuss</a>\n'
                h+='  </b></td>\n'

                h+='  <td><b>\n'
                h+='   Number of distinct solutions\n'
                h+='  </b></td>\n'
                h+='  <td><b>\n'
                h+='   Max improvement (first characteristic)\n'
                h+='  </b></td>\n'
                for k in pr:
                    qd=k.get('desc','')
                    qi=k.get('id','')

                    h+='  <td><b>\n'
                    h+='   '+qd+'\n'
                    h+='  </b></td>\n'
                h+=' </tr>\n'

                iq=0
                for q in range(0, irl):
                    qq=rl[q]

                    duid=qq['data_uid']

                    qqm=qq['meta']

                    dm=qqm.get('meta',{})

                    ns=qqm.get('solutions','')

                    if ns!='' and int(ns)>0:
                       iq+=1

                       results.append(qq)

                       h+='<tr>'
                       h+=' <td>'+str(iq)+'</td>'
                       if widget:
                          h+=' <td><button type="submit" name="view_solution_'+scenario+'_'+duid+'">Predict optimization</button></td>\n'
                       else:
                          h+=' <td><a href="'+url0+'wcid='+scenario+':'+duid+'">Click to see solutions ('+duid+')</a></td>\n'

                       h+=' <td align="center">'
                       if url5!='': h+='<a href="'+url5+scenario+'_'+duid+'">Wiki</a>'
                       h+='</td>\n'

                       h+=' <td align="center">'+str(ns)+'</td>'

                       dv=qqm.get('max_improvement_first_key',None)
                       y=''
                       if dv!=None:
                          try:
                             y=('%.2f' % dv)
                          except Exception as e: 
                             pass

                       h+=' <td align="center">'+y+'</td>'
                       for k in pr:
                           qd=k.get('desc','')
                           qi=k.get('id','')
                           qr=k.get('ref_uid','')
                           qm=k.get('ref_module_uoa','')

                           x=dm.get(qi,'')
                           if x!='' and qm!='' and qr!='':
                              xuid=dm.get(qr,'')
                              if xuid!='':
                                 x='<a href="'+url0+'wcid='+qm+':'+xuid+'">'+x+'</a>'

                           h+='  <td>'
                           h+='   '+x
                           h+='  </td>'

                       h+='</tr>'

                h+='</table>\n'

                if not widget:
                   h+='<br><a href="http://arxiv.org/abs/1506.06256"><img src="'+url0+'action=pull&common_action=yes&cid='+cfg['module_deps']['module']+':'+work['self_module_uid']+'&filename=images/image-workflow1.png"></a><br>\n'

                x=ck.cfg.get('extra_browser_text_ct','')
                if x!='':
                   h+=x+'\n'

                h+='</center>\n'

    if sh=='yes':
       h=''
       st=''

    return {'return':0, 'html':h, 'style':st, 'results':results}

##############################################################################
# add new solution

def add_solution(i):
    """
    Input:  {
              packed_solution         - new packed points
              scenario_module_uoa     - scenario UID
              meta                    - meta to search
              (meta_extra)            - extra meta to add

              exchange_repo           - where to record (local or remote)
              exchange_subrepo        - where to recrod (if remote, local repo in remote machine)

              (packed_solution)       - new packed solution (experimental points ready to be sent via Internet 
                                        if communicating with crowd-server)

              (solution_uid)          - new solution UID (if found)

              solutions               - list of solutions (pre-existing and new with re-classification)

              (workload)              - workload dict to classify distinct optimizations
                                        (useful for collaborative machine learning and run-time adaptation)

              (user)                  - user email/ID to attribute found solutions (optional for privacy)          

              (first_key)             - first key (to record max speedup)
            }

    Output: {
              return              - return code =  0, if successful
                                                >  0, if error
              (error)             - error text if return > 0

              (recorded)          - if 'yes', submitted solution was recorded

              if recorded=='yes':
              (recorded_info)     - dict with recorded entry {'repo_uoa', 'module_uoa', 'data_uoa'}
            }

    """

    import os
    import copy

    o=i.get('out','')
    oo=''
    if o=='con': oo='con'

    ps=i.get('packed_solution','')
    sols=i.get('solutions',[])
    suid=i.get('solution_uid','')

    ruoa=i.get('repo_uoa','')
    smuoa=i['scenario_module_uoa']
    meta=i['meta']
    emeta=i.get('meta_extra',{})

    er=i.get('exchange_repo','')
    esr=i.get('exchange_subrepo','')

    user=i.get('user','')

    choices=i.get('choices',{})
    ft=i.get('features',{})

    fk=i.get('first_key','')

    workload=i.get('workload',{})

    # Search if exists
    ii={
        'repo_uoa': ruoa,
        'scenario_module_uoa':smuoa,
        'meta':meta,
        'out':oo
       }
    r=get(ii)
    if r['return']>0: return r

    si=r['solutions_info']
    found=si['found']

    if found=='yes':
       duoa=si['data_uoa']
    else:
       metax=copy.deepcopy(meta)

#       metax.update(emeta) 
       if emeta.get('cpu_uid','')!='': metax['cpu_uid']=emeta['cpu_uid']
       if emeta.get('compiler_description_uoa','')!='': metax['compiler_description_uoa']=emeta['compiler_description_uoa']

       ii={'action':'add',
           'common_func':'yes',
           'repo_uoa': ruoa,
           'module_uoa': smuoa,
           'dict':{'meta':metax}
          }
       r=ck.access(ii)
       if r['return']>0: return r
       duoa=r['data_uid']

    if o=='con': 
       ck.out('  Loading and locking entry ('+duoa+') ...')

    # Loading existing info and locking
    ii={'action':'load',
        'common_func':'yes',
        'module_uoa':smuoa,
        'data_uoa':duoa,
        'repo_uoa': ruoa,
        'get_lock':'yes',
        'lock_expire_time':120}
    r=ck.access(ii)
    if r['return']>0: return r
    duid=r['data_uid']

    lock_uid=r['lock_uid']

    p=r['path']
    d=r['dict']

    # Unpack new solution (may be pruned later)
    if suid!='' and ps!='':
       p1=os.path.join(p, suid)
       if not os.path.isdir(p1):
          os.makedirs(p1)

       # Prepare tmp file
       rx=ck.convert_upload_string_to_file({'file_content_base64':ps,
                                            'filename':''})
       if rx['return']>0: return rx
       fn=rx['filename']

       # Unzip
       rx=ck.unzip_file({'archive_file':fn,
                         'path':p1,
                         'overwrite':'yes',
                         'delete_after_unzip':'yes'})
       if rx['return']>0: return rx

    # Load summary file
    osols=[]
    psum=os.path.join(p, fsummary)
    if os.path.isfile(psum):
       rx=ck.load_json_file({'json_file':psum})
       if rx['return']>0: return rx
       osols=rx['dict']

    # Load classification file
    classification={}
    pcl=os.path.join(p, fclassification)
    if os.path.isfile(pcl):
       rx=ck.load_json_file({'json_file':pcl})
       if rx['return']>0: return rx
       classification=rx['dict']

    # First go through new solutions and update min/max in classification
    bsuid='' # best solution for this workload found
    bvv=None
    bimp={}
    bchars={}

    wsuid='' # best solution for this workload found
    wvv=None
    wimp={}

    for sol in sols:
        xuid=sol['solution_uid']

        vv=sol.get('touched',None)
        if vv==None: vv=0
        vv=int(vv)
        vv+=1
        sol['touched']=vv

        vv=sol.get('iterations',None)
        if vv==None: vv=1
        sol['iterations']=vv

        cls=classification.get(xuid,{})

        # Use first point
        points=sol.get('points',[])
        if len(points)>0:
           point=points[0]

           imp=point.get('improvements',{})
           chars=point.get('characteristics',{})

           # If reaction exists, means that already not new - take it 
           rimp=point.get('improvements_reaction',{}) 
           if len(rimp)>0:
              imp=rimp

           # Get current best/worst by first key
           hi=cls.get('highest_improvements',{})
           hiw=cls.get('highest_improvements_workload',{})
           hd=cls.get('highest_degradations',{})
           hdw=cls.get('highest_degradations_workload',{})

           vi=hi.get(fk, None)
           vd=hd.get(fk, None)

           # Get new key
           vv=imp.get(fk, None)

           # Check if better
           if vv!=None and point.get('reaction_info',{}).get('fail','')!='yes':
              if vi==None or vv>vi:
                 hi=imp
                 hiw=workload

              if bvv==None or vv>bvv:
                 bsuid=xuid
                 bvv=vv
                 bimp=imp
                 bchars=chars

           # Check if worse
           if vv!=None and vv<0.96 and (vd==None or vv<vd):
              hd=imp
              hdw=workload

              if wvv==None or vv>wvv:
                 wsuid=xuid
                 wvv=vv
                 wimp=imp

           cls['highest_improvements']=hi
           cls['highest_improvements_workload']=hiw
           cls['highest_degradations']=hd
           cls['highest_degradations_workload']=hdw

           # If not in existing solution, add there, otherwise update touched/iterations
           found=False
           for osol in osols:
               ouid=osol['solution_uid']
               if ouid==xuid:
                  vv=osol.get('touched',None)
                  if vv==None: vv=0
                  vv=int(vv)
                  vv+=1
                  osol['touched']=vv

                  vv=osol.get('iterations',None)
                  if vv==None: vv=0
                  vv=int(vv)
                  vv+=1
                  osol['iterations']=vv

                  found=True
                  break

           if not found:
              osols.append(sol)

        classification[xuid]=cls

    # Add our point to the best ones
    checked=[]
    for q in sols:
        checked.append(q['solution_uid'])

    if o=='con':
       ck.out('')
       ck.out('  UID for  best result (current solution): '+bsuid)
       ck.out('  UID for worst result (current solution): '+wsuid)
       ck.out('')

    if bsuid!='' and bvv!=None:
       cls=classification[bsuid]
       w=cls.get('best',[])

       w1=[{'workload':workload, 'improvements':bimp, 'characteristics':bchars, 'checked':checked}] # will add the latest info & checked list
       for wx in w:
           ww=wx.get('workload',{})
           if ww.get('program_uoa','')!=workload.get('program_uoa','') or \
              ww.get('cmd_key','')!=workload.get('cmd_key',''):
              w1.append(wx)

       # Sort
       w2=sorted(w1, key=lambda v: (ck.safe_float(v.get('improvements',{}).get(fk,0.0),0.0)), reverse=True)

       cls['best']=w2
       classification[bsuid]=cls

    if wsuid!='' and wvv!=None:
       cls=classification[wsuid]
       w=cls.get('worst',[])

       w1=[{'workload':workload, 'improvements':wimp, 'checked':checked}]
       for wx in w:
           ww=wx.get('workload',{})
           if ww.get('program_uoa','')!=workload.get('program_uoa','') or \
              ww.get('cmd_key','')!=workload.get('cmd_key',''):
              w1.append(wx)

       w2=sorted(w1, key=lambda v: (ck.safe_float(v.get('improvements',{}).get(fk,0.0),0.0)))

       cls['worst']=w2
       classification[wsuid]=cls

    # Sort solutions via classification and highest improvements
    hcls=sorted(classification, key=lambda v: (ck.safe_float(classification[v].get('highest_improvements',{}).get(fk,0.0),0.0)), reverse=True)
    wcls=sorted(classification, key=lambda v: (ck.safe_float(classification[v].get('highest_degradations',{}).get(fk,0.0),0.0)))

    dv=ck.safe_float(classification[hcls[0]].get('highest_improvements',{}).get(fk,0),0.0)
    if dv>0.0:
       d['max_improvement_first_key']=dv

    dv=ck.safe_float(classification[wcls[0]].get('highest_degradations',{}).get(fk,0),0.0)
    if dv>0.0:
       d['max_degradation_first_key']=dv

    # prune solutions - go from left to right and check uniquness of workloads in best solutions
    #  (datasets can differ since they can result in different solutions) 
    unique_workloads=[]

    for k in hcls:
        cc=classification[k]
        best=cc.get('best',[])
        nbest=[] # reconstructed best with evicted non-unique workloads
        for b in best:
            w=b.get('workload',{})

            found=False
            for ww in unique_workloads:
                if ww.get('program_uoa','')==w.get('program_uoa','') and \
                   ww.get('cmd_key','')==w.get('cmd_key',''):
                   found=True
                   break

            if not found:
               unique_workloads.append(w)
               nbest.append(b)

        cc['best']=nbest

    # remove unused
    uids_to_delete=[]

    for q in classification:
        cc=classification[q].get('best',[])
        if len(cc)==0:
           uids_to_delete.append(q)

    for q in uids_to_delete:
        if q in classification:
           del(classification[q])

           p1=os.path.join(p, q)
           if os.path.isdir(p1):
              import shutil
              try:
                 shutil.rmtree(p1, ignore_errors=True)
              except Exception as e: 
                 if o=='con':
                    ck.out('')
                    ck.out('WARNING: can\'t fully erase tmp dir '+p1)
                    ck.out('')
                 pass

    # rebuild/resort solutions by highest
    sols=[]

    for k in hcls:
        if k not in uids_to_delete:
           for x in osols:
               xuid=x.get('solution_uid','')
               if xuid==k:
                  sols.append(x)
                  break

    # Check number of solutions
    ls=len(sols)
    d['solutions']=ls

    # Checking if new solution and record user if needed
    x=classification.get(suid,{})
    if len(x)>0:
       if x.get('user','')=='' and user!='':
          x['user']=user
          classification[suid]=x

    # Saving classification file
    rx=ck.save_json_to_file({'json_file':pcl, 'dict':classification, 'sort_keys':'yes'})
    if rx['return']>0: return rx

    # Saving summary file
    rx=ck.save_json_to_file({'json_file':psum, 'dict':sols, 'sort_keys':'yes'})
    if rx['return']>0: return rx

    # Updating and unlocking entry *****************************************************
    if o=='con': 
       ck.out('  Updating entry and unlocking ...')

    ii={'action':'update',
        'common_func':'yes',
        'repo_uoa': ruoa,
        'module_uoa': smuoa,
        'data_uoa':duid,
        'ignore_update':'yes',
        'sort_keys':'yes',
        'dict':d,
        'substitute':'yes',
        'unlock_uid':lock_uid
       }
    r=ck.access(ii)
    if r['return']>0: return r

    # *************************************************************** Adding some stats
    # Search if exists
    if o=='con': 
       ck.out('')
       ck.out('  Reloading index entry for statistics and locking ...')

    ii={'action':'load',
        'common_func':'yes',
        'repo_uoa': ruoa,
        'module_uoa': smuoa,
        'data_uoa':iuoa,
        'get_lock':'yes',
        'create_if_not_found':'yes',
        'lock_expire_time':120
       }
    r=ck.access(ii)

    p=r['path']
    d=r['dict']
    lock_uid=r['lock_uid']

    # Try to load keys.json
    dd={}
    px=os.path.join(p, fstats)
    if os.path.isfile(px):
       rx=ck.load_json_file({'json_file':px})
       if rx['return']>0: return rx
       dd=rx['dict']

    mm=dd.get('meta',None)
    if mm==None:
       mm={}

    for q in meta:
        qq=meta[q]

        v=mm.get(q, None)
        if v==None:
           v={}

        v1=v.get(qq, None)
        if v1==None:
           v1={}

        vv=v1.get('touched',None)
        if vv==None: 
           vv=0
        vv=int(vv)
        vv+=1

        v1['touched']=vv

        v[qq]=v1

        mm[q]=v

    dd['meta']=mm

    # Saving stats
    rx=ck.save_json_to_file({'json_file':px, 'dict':dd, 'sort_keys':'yes'})
    if rx['return']>0: return rx

    # Updating and unlocking entry *****************************************************
    if o=='con': 
       ck.out('  Updating entry and unlocking ...')

    ii={'action':'update',
        'common_func':'yes',
        'repo_uoa': ruoa,
        'module_uoa': smuoa,
        'data_uoa':iuoa,
        'ignore_update':'yes',
        'dict':d,
        'substitute':'yes',
        'unlock_uid':lock_uid
       }
    r=ck.access(ii)
    if r['return']>0: return r

    rr={'return':0}

    x=classification.get(suid,{})
    if len(x)>0:
       rr['recorded']='yes'
       rr['recorded_info']={'repo_uoa': ruoa, 'module_uoa': smuoa, 'data_uoa':duid}

       xstatus='*** Your explored solution (UID='+suid+') is BETTER than existing ones and was RECORDED! ***\n'

       s='Good solution!\n\n'
       s+='  User:         '+user+'\n\n'
       s+='  Solution UID: '+suid+'\n'
       s+='  Scenario UOA: '+smuoa+'\n'
       s+='  Data UOA:     '+duid+'\n'

       rr['recorded_info']['status']=xstatus
       rr['recorded_info']['log']=s

       # Record stats for non anonymous user
       if user!='' and user!='-':
          if o=='con':
             ck.out('')
             ck.out('Updating user statistics ...')

          # Time
          r=ck.get_current_date_time({})
          if r['return']>0: return r

          idt=r['iso_datetime']

          pack={'iso_datetime':idt,
                'solution_uid':suid,
                'scenario_uoa':smuoa,
                'data_uoa':duid}

          # Hack
          bak1=ck.cfg["forbid_writing_to_local_repo"]
          ck.cfg["forbid_writing_to_local_repo"]="no"

          bak2=ck.cfg["allow_writing_only_to_allowed"]
          ck.cfg["allow_writing_only_to_allowed"]="no"

          # Load/create and lock
          ii={'action':'load',
              'common_func':'yes',
              'module_uoa': cfg['module_deps']['experiment.user'],
              'data_uoa':'all',
              'get_lock':'yes',
              'create_if_not_found':'yes',
              'lock_expire_time':20
             }
          r=ck.access(ii)

          d=r['dict']
          lock_uid=r['lock_uid']

          du=d.get('users',{})
          dt=d.get('timeline',[])

          if user not in du:
             du[user]={}

          du[user]=pack
          d['users']=du

          pack['user']=user
          dt.append(pack)

          d['timeline']=dt

          ii={'action':'update',
              'common_func':'yes',
              'module_uoa': cfg['module_deps']['experiment.user'],
              'data_uoa':'all',
              'ignore_update':'yes',
              'sort_keys':'yes',
              'dict':d,
              'substitute':'yes',
              'unlock_uid':lock_uid
             }
          r=ck.access(ii)
          if r['return']>0: return r

          ck.cfg["forbid_writing_to_local_repo"]=bak1
          ck.cfg["allow_writing_only_to_allowed"]=bak2

    return rr

##############################################################################
# initialize experiment

def initialize(i):
    """
    Input:  {
              (host_os)                    - host OS (detect, if omitted)
              (target_os)                  - OS module to check (if omitted, analyze host)
              (device_id)                  - device id if remote (such as adb)

                  or

              (target)                     - if specified, use info from 'machine' module to set up target machine
              (device_cfg)                 - extra machine cfg (if empty, will be filled in from 'machine' description)

              (quiet)                      - do not ask questions, but select random ...
              (skip_welcome)               - if 'yes', do not print welcome header

              (skip_exchange)              - if 'yes', do not exchange platform info
                                            (development mode)

              (skip_gpu_info)              - if 'yes', do not collect GPU info
              (platform_init_uoa)          - if !='', use these platform.init scripts

              (change_user)                - if yes', change user

              (local)                      - if 'yes', use local repo for exchange (local autotuning/benchmarking)
              (exchange_repo)              - which repo to record/update info (remote-ck by default)
              (exchange_subrepo)           - if remote, remote repo UOA

              (force_platform_name)        - if !='', use this for platform name

              (skip_info_collection)       - if 'yes', skip info collection - useful when running scenarios remotly for mobile devices

              (crowdtuning_type)           - (by default = random-crowdtuning)

              (update_platform_init)       - update platform.init scripts (ask user)
            }

    Output: {
              return           - return code =  0, if successful
                                             >  0, if error
              (error)          - error text if return > 0

              platform_info    - output of ck detect platform
              user             - user email/ID
            }

    """

    import copy
    import os

    # Setting output
    o=i.get('out','')
    oo=''
    if o=='con': oo='con'

    user=''

    # Params
    hos=i.get('host_os','')
    tos=i.get('target_os', '')
    tdid=i.get('device_id', '')
    target=i.get('target','')
    device_cfg=i.get('device_cfg',{})

    exc='yes'
    se=i.get('skip_exchange','')
    if se=='yes': exc='no'

    cu=i.get('change_user','')

    er=i.get('exchange_repo','')
    esr=i.get('exchange_subrepo','')

    fpn=i.get('force_platform_name','')

    crowdtuning_type=i.get('crowdtuning_type','')
    if crowdtuning_type=='': crowdtuning_type='random-crowdtuning'

    quiet=i.get('quiet','')

    sw=i.get('skip_welcome','')

    sic=i.get('skip_info_collection','')

    sgi=i.get('skip_gpu_info','')
    pscripts=i.get('platform_scripts','')
    piuoa=i.get('platform_init_uoa','')

    #**************************************************************************************************************
    # Welcome info
    if o=='con' and (i.get('welcome','')=='yes' or (quiet!='yes' and sw!='yes')):
       ck.out(line)
       ck.out(welcome)
       ck.out(welcome1)

       if quiet!='yes':
          r=ck.inp({'text':'Press Enter to continue'})

    # Prepare log
    ii={'action':'log', 'module_uoa':cfg['module_deps']['experiment'], 'file_name':cfg['log_file_own'], 'text':''}
    r=ck.access(ii)
    if r['return']>0: return r
    p=r['path']

    if o=='con':
       ck.out(line)
       ck.out('Experimental results will be appended to a local log file: '+p)

       if quiet!='yes' and i.get('skip_log_wait','')!='yes':
          ck.out('')
          r=ck.inp({'text':'Press Enter to continue'})

    #**************************************************************************************************************
    # Check if there is program crowdtuning configuration
    dcfg={}
    ii={'action':'load',
        'module_uoa':cfg['module_deps']['cfg'],
        'data_uoa':cfg['cfg_uoa']}
    r=ck.access(ii)
    if r['return']>0 and r['return']!=16: return r
    if r['return']!=16:
       dcfg=r['dict']

    user=i.get('user','')
    if user=='':
        user=dcfg.get('user_email','')

    if (user=='' and o=='con' and quiet!='yes') or (cu!='' and cu!='-'):
       if cu=='':
          ck.out(line)
          r=ck.inp({'text':'Enter your email if you would like to identify your local or global contributions or press Enter to generate random UID: '})
          xuser=r['string'].strip()
       else:
          xuser=cu.strip()

       if xuser=='':
          # If user is not specified, generate user UID
          rx=ck.gen_uid({})
          if rx['return']>0: return rx
          xuser=rx['data_uid']

       if xuser!=user:
          user=xuser
          dcfg['user_email']=user

          ii={'action':'update',
              'module_uoa':cfg['module_deps']['cfg'],
              'data_uoa':cfg['cfg_uoa'],
              'dict':dcfg}
          r=ck.access(ii)
          if r['return']>0: return r

    if o=='con':
       ck.out(line)
       ck.out('Your user ID : '+user)

    #**************************************************************************************************************
    # Testing remote platform
    if se!='yes' and er!='local':
       ck.out(line)
       ck.out('Testing experiment crowdsourcing server ...')
       ck.out('')

       ii={'action':'test',
           'module_uoa':work['self_module_uid'],
           'out':'',
           'email':user,
           'type':crowdtuning_type,
           'repo_uoa':er}
       r=ck.access(ii)
       if r['return']>0: return r

       ck.out('  SUCCESS!')

    #**************************************************************************************************************
    # Detecting platforms and exchanging info with public Server
    if o=='con':
       x='Detecting your platform info'
       if er!='local':
          x+=' and query public CK server to check shared info'

       ck.out(line)
       ck.out(x+' ...')
       ck.out('')

    ii={'action':'detect',
        'module_uoa':cfg['module_deps']['platform'],
        'out':oo,
        'host_os':hos,
        'target':target,
        'device_cfg':device_cfg,
        'target_os':tos,
        'target_device_id':tdid,
        'exchange':exc,
        'exchange_repo':er,
        'exchange_subrepo':esr,
        'skip_info_collection':sic,
        'quiet':quiet,
        'skip_gpu_info':sgi,
        'platform_init_uoa':piuoa,
        'update_platform_init':i.get('update_platform_init',''),
        'force_platform_name':fpn}
    rpp=ck.access(ii)
    if rpp['return']>0: return rpp

    hos=rpp['host_os_uoa']
    hosd=rpp['host_os_dict']

    tos=rpp['os_uoa']
    tosd=rpp['os_dict']
    tbits=tosd.get('bits','')

    remote=tosd.get('remote','')

    tdid=rpp['device_id']

    if hos=='':
       return {'return':1, 'error':'"host_os" is not defined or detected'}

    if tos=='':
       return {'return':1, 'error':'"target_os" is not defined or detected'}

    return {'return':0, 'platform_info':rpp, 'user':user}

##############################################################################
# perform program optimization

def run(i):
    """
    Input:  {
              (host_os)                    - host OS (detect, if omitted)
              (target_os)                  - OS module to check (if omitted, analyze host)
              (device_id)                  - device id if remote (such as adb)

              (once)                       - if 'yes', run scenario once (useful for autotuning a given program)

              (iterations)                 - limit number of iterations, otherwise infinite (default=30)
                                             if -1, infinite (or until all choices are explored)

              (repetitions)                - statistical repetitions of a given experiment

              (compiler_description_uoa)   - force compiler description UOA (see module "compiler")
              (flag_tags)                  - extra flag tags (must have)
              (any_flag_tags)              - extra flag tags (any of these)

              (quiet)                      - do not ask questions, but select random ...
              (skip_welcome)               - if 'yes', do not print welcome header

              (skip_exchange)              - if 'yes', do not exchange platform info
                                            (development mode)

              (user)                       - user email/ID to record solutions (attribute found good solutions)

              (local)                      - if 'yes', use local repo for exchange (local autotuning/benchmarking)
              (exchange_repo)              - which repo to record/update info (remote-ck by default)
              (exchange_subrepo)           - if remote, remote repo UOA

              (record_repo)                - repo where to search/record local experiments
                                             ("local" by default, to avoid polluting other repos)

              (local_autotuning)           - if 'yes', do not crowdtune, i.e. find local experiment and do not exchnage results

              (force_platform_name)        - if !='', use this for platform name

              (scenario)                   - module UOA of crowdsourcing scenario
              (scenario_cfg)               - cfg of a scenario

              (seed)                       - autotuning seed

              (program_tags)               - force selection of programs by tags

              (program_uoa)                - force program UOA
              (cmd_key)                    - CMD key
              (cmd_keys)                   - Select only from this list of available CMD keys

              (dataset_uoa)                - dataset UOA
              (dataset_file)               - dataset filename (if more than one inside one entry - suggest to have a UID in name)

              (extra_dataset_tags)         - list of extra data set tags (useful to set "small" during mobile phone crowdtuning)

              (calibration_time)           - change calibration time (deafult 10 sec.)

              (objective)                  - extension to flat characteristics (min,exp,mean,center) to tune on Pareto
                                             (default: min - to see what we can squeeze from a given architecture)

              (keep_tmp)                   - if 'yes', do not remove run batch

              (ask_pipeline_choices)       - if 'yes', ask for each pipeline choice, otherwise random selection 

              (platform_info)              - detected platform info

              (experiment_meta)            - meta when recording experiment
              (experiment_meta_extra)      - extra meta such as platform UIDs

               (record_failed)                    - if 'yes', record even failed experiments
                                                    (for debugging, buildbots, detecting designed 
                                                     architecture failures, etc)
               (record_only_failed)               - if 'yes', record only failed experiments
                                                    (useful to crowdsource experiments when searching only 
                                                     for compiler/program/architecture bugs  
                                                     (for example fuzzing via random compiler flags))...

              (record_uoa)                 - use this UOA to recrod experiments instead of randomly generated ones

              (solution_conditions)        - list of conditions:
                                               ["first key", "extra key", "condition", value]

              (pause_if_fail)              - if pipeline fails, ask to press Enter
                                             (useful to analyze which flags fail during compiler flag autotuning)

              (omit_probability)           - probability to omit optimization (for example, compiler flags during exploration/crowdtuning)
              (parametric_flags)           - if 'yes', also tune parametric flags
              (cpu_flags)                  - if 'yes', also tune cpu-specific flags
              (base_flags)                 - if 'yes', also tune base flag

              (compiler_env_uoa)           - fix compiler environment

              (new)                        - if 'yes', do not search for existing experiment, but start new

              (solutions)                  - list of solutions
              (solutions_info)             - info (repo_uoa, module_uoa, data_uoa)

              (solution_module_uoa)        - if !='' use it to reuse shared optimization cases
              (solution_data_uoa)          - force specific solution entry
              (solution_repo_uoa)          - force repo where to search existing solutions
              (solution_remote_repo_uoa)   - force sub-repo (if above repo is remote)

              (prune)                      - prune solution (find minimal choices that give the same result)
              (reduce)                     - the same as above
              (reduce_bug)                 - reduce choices to localize bug (pipeline fail)
              (prune_md5)                  - if 'yes', check if MD5 doesn't change
              (prune_invert)               - prune all (turn off even swiched off)

              (replay)                     - if 'yes', replay

              (record_reactions)            - if 'yes', record optimization reaction
              (record_reactions_file)       - file to record reaction table for graph ...

              (record_solutions)            - if 'yes', record solutions
              (solutions_file)              - output solutions to a file

              (skip_pruning)                - if 'yes', do not prune best found result during crowdtuning

              (skip_collaborative)          - do not check collaborative solutions (useful for "clean" autotuning)

              (no_run)                      - if 'yes', do not run program - useful for generating experiments pack
                                              for crowtuning using Android mobile phones
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              (solutions)  - if 'solutions' present in input, possibly updated ones will present in output too (replay)
            }

    """

    import copy
    import os
    import time

    try:
       curdir=os.getcwd()
    except OSError:
       os.chdir('..')
       curdir=os.getcwd()

    # Setting output
    o=i.get('out','')
    oo=''
    if o=='con': oo='con'

    target=i.get('target','')

    hos=i.get('host_os','')
    tos=i.get('target_os','')
    tdid=i.get('target_device_id','')

    sic=i.get('skip_info_collection','')

    eruoa=i.get('record_repo','')
    if eruoa=='': eruoa='local'

    pifail=i.get('pause_if_fail','')

    pi=i.get('platform_info',{})

    scfg=i.get('scenario_cfg',{})

    la=i.get('local_autotuning','')

    user=i.get('user','')

    sp=i.get('skip_pruning','')

    sf=i.get('solutions_file','')
    if sf=='':
       sf=os.path.join(curdir, fsolutions)

    static=i.get('static','')

    xprune=i.get('prune','')
    reduce_bug=i.get('reduce_bug','')
    prune_md5=i.get('prune_md5','')
    prune_invert=i.get('prune_invert','')
    prune_invert_add_iters=i.get('prune_invert_add_iters','')
    prune_ignore_choices=i.get('prune_ignore_choices',[])
    result_conditions=i.get('result_conditions',[])

    record_failed=i.get('record_failed','')
    record_only_failed=i.get('record_only_failed','')

    replay=i.get('replay','')

    no_run=i.get('no_run','')

    recr=i.get('record_reactions','')
    recrf=i.get('record_reactions_file','')
    if recr=='yes' and recrf=='':
       recrf=os.path.join(curdir, fgraph)

    cd_uoa=i.get('compiler_description_uoa','')
    ftags=i.get('flag_tags','').strip()

    # Add boolean
    anyftags=i.get('any_flag_tags','').strip()

    if anyftags!='': anyftags+=','
    anyftags+='boolean'

    pflags=i.get('parametric_flags','')
    aflags=i.get('cpu_flags','')
    bflags=i.get('base_flags','')

    if pflags=='yes':
       if anyftags!='': anyftags+=','
       anyftags+='parametric'

    quiet=i.get('quiet','')

    # Check CPU specific tags
    if aflags=='yes':
       if anyftags!='': anyftags+=','
       anyftags+='cpu-specific'

       cpu_ft=pi.get('features',{}).get('cpu',{}).get('compile_tags','')
       if cpu_ft!='':
          if anyftags!='': anyftags+=','
          anyftags+=cpu_ft

    if bflags=='yes':
       if anyftags!='': anyftags+=','
       anyftags+='base'

    oprob=i.get('omit_probability','')

    program_tags=i.get('program_tags','').strip()

    program_uoa=i.get('program_uoa','')
    if program_uoa=='': program_uoa=i.get('data_uoa','')
    cmd_key=i.get('cmd_key','')
    cmd_keys=i.get('cmd_keys',[])
    dataset_uoa=i.get('dataset_uoa','')
    dataset_file=i.get('dataset_file','')
    edt=i.get('extra_dataset_tags',[])

    sdeps=i.get('dependencies',{})

    apc=i.get('ask_pipeline_choices','')

    smuoa=i.get('scenario_module_uoa','')

    rep=i.get('repetitions','')

    iterations=i.get('iterations','')
    if iterations=='': iterations=30
    iterations=int(iterations)

    # Turn no state check by default!
    nsc=i.get('no_state_check','')
    xsc=i.get('state_check','')
    if xsc=='yes': nsc='no'
    if nsc=='': nsc='yes'

    cat=i.get('calibration_time','')
    if cat=='': cat=10.0

    objective=i.get('objective','')
    if objective=='': objective=scfg.get('objective', '')
    if objective=='': objective='min'

    xobjective=''
    if objective!='':
       xobjective='#'+objective

    seed=i.get('seed','')

    sdesc=scfg.get('desc','')
    ssdesc=i.get('subscenario_desc','')

    ktmp=i.get('keep_tmp','')
    kexp=i.get('keep_experiments','')

    scon=scfg.get('solution_conditions',[])
    cscon=i.get('customize_solution_conditions',[])
    if len(cscon)>0: scon=cscon

    er=i.get('exchange_repo','')
    esr=i.get('exchange_subrepo','')

    repeat=i.get('repeat','')

    sols=i.get('solutions',[])
    sols_info=i.get('solutions_info',{})

    # Check if customize scenario
    if len(i.get('scenario_cfg_update',{}))>0:
       scfg.update(i['scenario_cfg_update'])

    # Check (multi-objective) characteristics to process
    ok=scfg.get('original_keys',[])
    fk=scfg.get('frontier_keys',[])
    ik=scfg.get('improvements_keys',[])
    rk=scfg.get('record_keys',[])
    pk=scfg.get('print_extra_keys',[])

    threshold=scfg.get('reference_threshold','')
    if threshold=='': threshold=0.03

    # Update objective (min,max,exp) - if exp, need to add confidence interval
    #                                  otherwise we are not using points with high variation!          
    for l in range(0, len(ok)):
         ok[l]=ok[l].replace('$#obj#$',objective)

    for l in range(0, len(fk)):
         fk[l]=fk[l].replace('$#obj#$',objective)

    for l in range(0, len(ik)):
         ik[l]=ik[l].replace('$#obj#$',objective)

    for l in range(0, len(rk)):
         rk[l]=rk[l].replace('$#obj#$',objective)

    for l in range(0, len(pk)):
         pk[l]=pk[l].replace('$#obj#$',objective)

    ik0=ik[0] # first key to sort

    # Prepare output (embed autotuning results)
    rrr={'return':0}

    #**************************************************************************************************************
    # Preparing pipeline with a temporary directory and random choices if not fixed (progs, datsets, etc)
    ii={'action':'pipeline',
        'module_uoa':cfg['module_deps']['program'],
        'host_os':hos,
        'target':target,
        'target_os':tos,
        'target_device_id':tdid,
        'dependencies':sdeps,
        'force_resolve_deps':'yes',
        'program_tags':program_tags,
        'program_uoa':program_uoa,
        'cmd_key':cmd_key,
        'cmd_keys':cmd_keys,
        'dataset_uoa':dataset_uoa,
        'dataset_file':dataset_file,
        'skip_local':'yes',
        'calibration_time':cat,
        'generate_rnd_tmp_dir':'yes', # to be able to run crowdtuning in parallel on the same machine ...
        'prepare':'yes',
        'skip_info_collection':sic,
        'quiet':quiet,
        'out':oo}
    if apc!='yes':
       ii['random']='yes'
    if cd_uoa!='':
       ii['compiler_description_uoa']=cd_uoa
    if len(edt)>0:
       ii[ 'extra_dataset_tags']=edt
    if nsc!='': 
       ii['no_state_check']=nsc
    if static!='': 
       ii['static']=static
    r=ck.access(ii)
    if r['return']>0: return r

    ready=r['ready']
    unexpected=False
    if ready!='yes':
       x='   WARNING: didn\'t manage to prepare program optimization workflow'

       ck.out('')
       ck.out(x+' ...')

       gg={'action':'log', 'module_uoa':cfg['module_deps']['experiment'],'file_name':cfg['log_file_own'], 'skip_header':'yes', 'text':x+'\n'}
       rx=ck.access(gg)
    else:
       ################################################################################
       # Continue
       del(r['return'])

       pipeline=r

       if no_run=='yes':
          pipeline['no_run']='yes'
          pipeline['add_rnd_extension_to_bin']='yes'
#          pipeline['add_save_extension_to_bin']='yes'
          pipeline['skip_device_info']='yes'
#          pipeline['no_clean']='yes'
          rep=1

       state=r['state']
       tmp_dir=state['tmp_dir']

       choices=r['choices']

       hos=choices.get('host_os','')
       tos=choices.get('target_os','')
       tdid=choices.get('device_id','')
       tcfg=choices.get('device_cfg','')

       ft=r['features']

       prog_uoa=choices['data_uoa']
       cmd_key=choices.get('cmd_key','')
       dataset_uoa=choices.get('dataset_uoa','')
       dataset_file=choices.get('dataset_file','')

       cdu=choices.get('compiler_description_uoa','')

       cver=ft.get('compiler_version',{}).get('str','')

       meta=i.get('experiment_meta',{})
       meta['objective']=objective

       emeta=i.get('experiment_meta_extra',{})
       emeta['compiler_description_uoa']=cdu

       mmeta=copy.deepcopy(meta) # to add extra when recording local experiments (helper)
       mmeta['scenario_module_uoa']=smuoa
       mmeta['scenario_desc']=sdesc
       mmeta['subscenario_desc']=ssdesc

       mmeta['program_uoa']=prog_uoa
       mmeta['cmd_key']=cmd_key
       mmeta['dataset_uoa']=dataset_uoa
       mmeta['dataset_file']=dataset_file

       workload={} # to classify distinct optimizations across different workloads
                   # later may be used for split-compilation and run-time adaptation
       workload['program_uoa']=prog_uoa
       workload['cmd_key']=cmd_key
       workload['dataset_uoa']=dataset_uoa
       workload['dataset_file']=dataset_file

       pchoices1={}
       pchoices_order1=[]

       euoa0=i.get('record_uoa','')
       puid0=''
       found=False
       results00={}
       ####################################################### IF LOCAL AUTOTUNING
       if la=='yes' and i.get('new','')!='yes':
          if o=='con':
             ck.out('')
             ck.out('Searching if similar experiment already exists in your local repo ...')

          ###########################################################################################33
          # Try to find in local experiments by meta
          jj={'action':'get',
              'module_uoa':cfg['module_deps']['experiment'],
              'repo_uoa':eruoa,
              'data_uoa':euoa0,
              'meta':mmeta,
              'flat_keys_list':ik,
              'load_json_files':['features_flat','flat','features']
             }
          rx=ck.access(jj)
          if rx['return']>0: return rx

          points=rx['points']
          if len(points)>0:
             # Search for reference/pemanent point 
             for q in points:
                 if q.get('features',{}).get('permanent','')=='yes':
                    found=True

                    euoa0=q['data_uid']
                    puid0=q['point_uid']

                    if o=='con':
                       ck.out('')
                       ck.out('  Found previous exploration ('+euoa0+'/'+puid0+') - restarting ...')

                    repeatx=q.get('features',{}).get('choices',{}).get('repeat','')

                    if str(repeat)!='' and str(repeatx)!=str(repeat):
                       return {'return':1, 'error':'requested kernel repeat number ('+str(repeat)+') is not the same as in reference point ('+str(repeatx)+')'}

                    repeat=repeatx

                    time.sleep(2)

                    break

       if euoa0=='':
          rx=ck.gen_uid({})
          if rx['return']>0: return rx
          euoa0=rx['data_uid'] # Where to keep experiment

       lx= ' * Program:                  '+prog_uoa+'\n' \
           ' * CMD:                      '+cmd_key+'\n' \
           ' * Dataset:                  '+dataset_uoa+'\n' \
           ' * Dataset file:             '+dataset_file+'\n'

       if ftags!='':
          lx+=' * Compiler flag tags (all): '+ftags+'\n'

       if anyftags!='':
          lx+=' * Compiler flag tags (any): '+anyftags+'\n'

       if repeat!='':
          lx+=' * Kernel repetitions:       '+str(repeat)+'\n'

       lx+=' * Default compiler version: '+cver+'\n' \
           ' * Compiler description:     '+cdu+'\n' \
           ' * Experiment UOA:           '+euoa0+'\n' \

       emeta['compiler_version']=cver
       emeta['compiler_description_uoa']=cdu
       emeta['kernel_repetitions']=repeat
       emeta['compiler_flag_tags']=ftags
       emeta['omit_probability']=str(oprob)

       if o=='con':
          ck.out(line)
          ck.out('Prepared experiment:')
          ck.out('')
          ck.out(lx)

       # Load program module to get desc keys
       pdesc={}

       xxmuoa=scfg.get('replay_desc',{}).get('module_uoa','')
       xxkey=scfg.get('replay_desc',{}).get('desc_key','')

       if xxmuoa!='':
          r=ck.access({'action':'load',
                       'module_uoa':cfg['module_deps']['module'],
                       'data_uoa':xxmuoa})
          if r['return']>0: return r
          pdesc=r.get('desc',{})
          if xxkey!='': pdesc=pdesc.get(xxkey,{})

       # Saving pipeline
       pipeline_copy=copy.deepcopy(pipeline)

       # ***************************************************************** Check if similar cases already found collaboratively
       last_sol_id=''

       if i.get('skip_collaborative','')!='yes':
          osols=copy.deepcopy(sols)

          if o=='con':
             ck.out('')
             ck.out('Searching if collaborative solutions already exist ...')

          xsmuoa=smuoa
          if i.get('solution_module_uoa','')!='':
             xsmuoa=i['solution_module_uoa']

          xsduoa=''
          xmeta=copy.deepcopy(meta)
          if i.get('solution_data_uoa','')!='':
             xsduoa=i['solution_data_uoa']
             xmeta={}

          xser=er
          if i.get('solution_repo_uoa','')!='':
             xser=i['solution_repo_uoa']

          xsesr=esr
          if i.get('solution_remote_repo_uoa','')!='':
             xsesr=i['solution_remote_repo_uoa']

          ii={'action':'get',
              'module_uoa':work['self_module_uid'],
              'repo_uoa':xser,
              'remote_repo_uoa':xsesr,
              'scenario_module_uoa':xsmuoa,
              'data_uoa':xsduoa,
              'meta':xmeta}
          rz=ck.access(ii)
          if rz['return']>0: return rz

          sols=rz['solutions']

          # Add user ones (remove solution UID to avoid mixing up with exising ones!)
          for q in osols:
              if 'solution_uid' in q: del(q['solution_uid'])
              if 'last_touch_uid' in q: del(q['last_touch_uid'])
              sols.append(q)

       isols=len(sols)

       if isols>0:
          ck.out('')
          ck.out('  Found '+str(isols)+' solution(s) - trying them first ...')

          time.sleep(2)

          iterations+=isols

       lx=' ===============================================================================\n' \
          ' * Scenario:                 '+sdesc+'\n' \
          ' * Sub scenario:             '+ssdesc+'\n' \
          ' * User:                     '+user+'\n' \
          ' * Existing solutions:       '+str(len(sols))+'\n' \
          ' * Number of iterations:     '+str(iterations)+'\n'+lx

       gg={'action':'log', 'module_uoa':cfg['module_deps']['experiment'],'file_name':cfg['log_file_own'], 'skip_header':'yes', 'text':lx}
       r=ck.access(gg)
       if r['return']>0: return r

       # ***************************************************************** FIRST EXPERIMENT !!!!!!!!!!!!!!
       if o=='con':
          ck.out(line)
          ck.out('Running first experiment with default optimization:')
          ck.out('')

       pipeline=copy.deepcopy(pipeline_copy)
       pup0=scfg.get('experiment_0_pipeline_update',{})
       if len(i.get('experiment_0_pipeline_update',{}))>0:
          pup0.update(i['experiment_0_pipeline_update'])

       if rep!='': pup0['repetitions']=rep
       if nsc!='': pup0['no_state_check']=nsc

       ii={'action':'autotune',
           'module_uoa':cfg['module_deps']['pipeline'],
           'data_uoa':cfg['module_deps']['program'],
           'host_os':hos,
           'target_os':tos,
           'target_device_id':tdid,

           "pipeline":pipeline,

           "iterations":1,

           "choices_order":[ [] ],

           "tmp_dir":tmp_dir,

           "skip_clean_after":"yes",

           "record":"yes",
           "record_uoa":euoa0,
           "record_repo":eruoa,
           "record_permanent":'yes',

           "tags":"crowdtuning,tmp",

           "meta":mmeta,

           'quiet':quiet,

           'out':oo
          }


       if i.get('save_to_file','')!='':
          ii['save_to_file']=i['save_to_file']

       if la!='yes':
          ii["skip_record_pipeline"]="yes"
          ii["skip_record_desc"]="yes"

       if len(rk)>0:
          ii['process_multi_keys']=rk

       if pifail!='':
          ii['pause_if_fail']=pifail

       if len(sols)>0:
          ii['solutions']=sols
          ii['ref_solution']='yes'

       r=ck.merge_dicts({'dict1':ii, 'dict2':pup0})
       if r['return']>0: return r
       ii=r['dict1']

       if 'pipeline_update' not in ii: ii['pipeline_update']={}
       ii['pipeline_update']['repeat']=repeat

       r=ck.access(ii)
       if r['return']>0: 
          gg={'action':'log', 'module_uoa':cfg['module_deps']['experiment'],'file_name':cfg['log_file_own'], 'skip_header':'yes', 'text':'   FAILURE: '+r['error']+'\n'}
          rx=ck.access(gg)
          return r

       rrr=copy.deepcopy(r)

       lio=r['last_iteration_output']
       fail=lio.get('fail','')
       target_exe_0=''
       target_path_0=''
       target_path_1=''
       if fail=='yes':
          unexpected=True
          x='   WARNING: pipeline execution failed ('+lio.get('fail_reason','')+')'

          ck.out('')
          ck.out(x+' ...')

          gg={'action':'log', 'module_uoa':cfg['module_deps']['experiment'],'file_name':cfg['log_file_own'], 'skip_header':'yes', 'text':x+'\n'}
          rx=ck.access(gg)
       else:
          # get flat dict from last stat analysis to calculate improvements of all characteristics
          fdfi=r.get('last_stat_analysis',{}).get('dict_flat',{})

          state=lio.get('state',{})
          repeat=state.get('repeat','')
          ftmp_dir=state.get('cur_dir','')

          target_exe_0=state.get('target_exe','')
          target_path_0=ftmp_dir

          ft=lio.get('features',{})

          emeta['kernel_repetitions']=repeat
          fp_cpu=ft.get('platform',{}).get('cpu',{})

          emeta['cpu_cur_freq']=fp_cpu.get('current_freq',{})
          emeta['cpu_num_proc']=fp_cpu.get('num_proc',1)

          ri=r['recorded_info']
          points1=ri.get('points',[])
          ruid=ri['recorded_uid']       # UID of the default one

          if len(points1)==0:
             unexpected=True

             x='   WARNING: explored points were not recorded (possibly internal error)'

             ck.out('')
             ck.out(x+' ...')

             gg={'action':'log', 'module_uoa':cfg['module_deps']['experiment'],'file_name':cfg['log_file_own'], 'skip_header':'yes', 'text':x+'\n'}
             rx=ck.access(gg)
          else:
             puid00=points1[0]

             # Check if need to run extra experiments
             # (for example when crowdsourcing program benchmarking or compiler bug detection,
             #  no need to run extra experiments)

             iii={'action':'get',
                  'module_uoa':cfg['module_deps']['experiment'],
                  'data_uoa':ruid,
                  'flat_keys_list':ik,
                  'load_json_files':['features_flat','flat','features']}

             # Load default point info
             r=ck.access(iii)
             if r['return']>0: 
                gg={'action':'log', 'module_uoa':cfg['module_deps']['experiment'],'file_name':cfg['log_file_own'], 'skip_header':'yes', 'text':'   FAILURE: '+r['error']+'\n'}
                rx=ck.access(gg)
                return r

             results1=r.get('points',{})

             # Detect reference optimization points
             if len(results1)>0:
                # Search for reference/pemanent point 
                for q in results1:
                    if q.get('features',{}).get('permanent','')=='yes':

                       choices1=q.get('features_flat',{})
                       choices_order1=q.get('features',{}).get('choices_order',[])

                       rx=prune_choices({'choices':choices1,
                                         'choices_order':choices_order1})
                       if rx['return']>0: return rx

                       pchoices1=rx['pruned_choices']             # only tuning keys
                       pchoices_order1=rx['pruned_choices_order'] # only keys (orders)

                       break

             # If local autotuning and appending to existing one,
             # check if still the same execution ...
             if la=='yes' and found:
                rx=compare_results({'point0':puid0,
                                    'point1':puid00,
                                    'results':results1,
                                    'keys':ok,
                                    'keys_desc':pdesc,
                                    'threshold':threshold})
                if rx['return']>0: return rx
                diff=rx['different']

                if diff=='yes':
                   if o=='con':
                      ck.out('')
                      ck.out('Results differ: '+rx['report']+' ...')
                      ck.out('Deleting point '+puid00+' ...')

                   rx=ck.access({'action':'delete_points',
                                 'module_uoa':cfg['module_deps']['experiment'],
                                 'points':[{'module_uid':cfg['module_deps']['experiment'], 
                                            'data_uid':euoa0,
                                            'point_uid':puid00}],
                                 'out':oo})
                   if rx['return']>0: return rx

                   unexpected=True

                   x='   WARNING: reference points differ in some characteristics - can\'t continue ...'

                   ck.out('')
                   ck.out(x+' ...')

                   gg={'action':'log', 'module_uoa':cfg['module_deps']['experiment'],'file_name':cfg['log_file_own'], 'skip_header':'yes', 'text':x+'\n'}
                   rx=ck.access(gg)

                   return {'return':0}
                else:
                   if o=='con':
                      ck.out('')
                      ck.out('Validating of previous points finished SUCCESSFULLY - substituting reference point '+puid0+' ...')

                   rx=ck.access({'action':'delete_points',
                                 'module_uoa':cfg['module_deps']['experiment'],
                                 'points':[{'module_uid':cfg['module_deps']['experiment'], 
                                            'data_uid':euoa0,
                                            'point_uid':puid0}],
                                 'out':oo})
                   if rx['return']>0: return rx

                   # Recreating list of original points
                   points1=[]
                   for q in results1:
                       qq=q['point_uid']
                       if qq!=puid0:
                          points1.append(qq)

                time.sleep(2)

             # Continue autotuning

             results2={}
             points2=[]
             points2p=[] #permanent

             if scfg.get('skip_autotuning','')!='yes':
                # *************************************************************** PREPARE AUTOTUNING
                # Prepare autotuning
                pipeline=copy.deepcopy(pipeline_copy)

                pup1=scfg.get('experiment_1_pipeline_update',{})
                pup1['frontier_keys']=fk

                if bflags=='yes':
                   zpu=pup1.get('pipeline_update',{})
                   zpu['best_base_flag']='no'
                   pup1['pipeline_update']=zpu

                if len(pup1.get('choices_selection',[]))>0:
                   xpup1=pup1['choices_selection'][0]

                   if ftags!='':
                      tg=xpup1.get('tags','')
                      if tg!='': tg+=','
                      tg+=ftags
                      xpup1['tags']=tg
                   if anyftags!='':
                      tg=xpup1.get('anytags','')
                      if tg!='': tg+=','
                      tg+=anyftags
                      xpup1['anytags']=tg
                   if oprob!='':
                      xpup1['omit_probability']=oprob

                   pup1['choices_selection'][0]=xpup1

                # Check customization
                if len(i.get('choices_order',[]))>0:
                   pup1['choices_order']=i['choices_order']
                if len(i.get('choices_selection',[]))>0:
                   pup1['choices_selection']=i['choices_selection']
                if len(i.get('frontier_keys',[]))>0:
                   pup1['frontier_keys']=i['frontier_keys']

                if len(i.get('experiment_1_pipeline_update',{}))>0:
                   pup1.update(i['experiment_1_pipeline_update'])

                if rep!='': pup1['repetitions']=rep
                if seed!='': pup1['seed']=seed

                ################################################################### Start main autotuning !!!!!!!!!!
                # Run autotuning
                if o=='con':
                   ck.out(line)
                   ck.out('Running multi-dimensional and multi-objective autotuning ...')
                   ck.out('')

                ii={'action':'autotune',

                    'module_uoa':cfg['module_deps']['pipeline'],
                    'data_uoa':cfg['module_deps']['program'],
                    'host_os':hos,
                    'target_os':tos,
                    'target_device_id':tdid,

                    "pipeline":pipeline,

                    "iterations":iterations,

                    "choices_order":[ [] ],

                    "tmp_dir":tmp_dir,

                    "tags":"crowdtuning,tmp",

                    "meta":mmeta,

                    'aggregate_failed_cases':'yes',

                    'flat_dict_for_improvements':fdfi,

# For Debugging
#                    'ask_enter_after_choices':'yes',
#                    'ask_enter_after_each_iteration':'yes',

                    'quiet':quiet,

                    "record":"yes",
                    "record_uoa":euoa0,
                    "record_repo":eruoa,

                    "record_failed":record_failed,
                    "record_only_failed":record_only_failed,

                    'out':oo
                   }

                if no_run=='yes':   # during crowdtuning for mobile phones need to save original exe
                   import tempfile
                   xfd, xfn=tempfile.mkstemp(suffix='', prefix='tmp-ck-')
                   os.close(xfd)
                   os.remove(xfn)
                   target_path_1=os.path.basename(xfn)

                   ii['tmp_dir']=target_path_1

                if i.get('save_to_file','')!='':
                   ii['save_to_file']=i['save_to_file']

                if la!='yes':
                   ii["skip_record_pipeline"]="yes"
                   ii["skip_record_desc"]="yes"

                ii['condition_objective']=xobjective 

                if len(sols)>0:
                   ii['solutions']=sols
                   if xprune=='yes':
                      ii['prune']=xprune
                      ii['reduce_bug']=reduce_bug
                      ii['prune_md5']=prune_md5
                      ii['prune_invert']=prune_invert
                      ii['prune_ignore_choices']=prune_ignore_choices
                      ii['prune_result_conditions']=result_conditions

                if xprune!='yes' and no_run!='yes':
                   ii['result_conditions']=scon
                   ii['prune_invert_add_iters']=prune_invert_add_iters

                if len(rk)>0:
                   ii['process_multi_keys']=rk

                if pifail!='':
                   ii['pause_if_fail']=pifail

                r=ck.merge_dicts({'dict1':ii, 'dict2':pup1})
                if r['return']>0: return r
                ii=r['dict1']

                if 'pipeline_update' not in ii: ii['pipeline_update']={}
                ii['pipeline_update']['repeat']=repeat

                r=ck.access(ii)
                if r['return']>0: 
                   gg={'action':'log', 'module_uoa':cfg['module_deps']['experiment'],'file_name':cfg['log_file_own'], 'skip_header':'yes', 'text':'   FAILURE: '+r['error']+'\n'}
                   rx=ck.access(gg)
                   return r

                rrr=copy.deepcopy(r)

                sols=r.get('solutions',[])

                failed_cases=r.get('failed_cases',[])
                if xprune!='yes' and len(failed_cases)>0:
                   sfc=''
                   for fc in failed_cases:
                       fcp=fc.get('pipeline_state',{})
                       fcpr=fcp.get('fail_reason','')
                       fcc=fc.get('characteristics',{})
                       sfc+='   * fail reason:    '+fcpr+'\n'
                       jcf=fcc.get('compile',{}).get('joined_compiler_flags','')
                       sfc+='     compiler flags: '+jcf+'\n'
                       repl='ck pipeline program:'+prog_uoa+' --cmd_key='+cmd_key+' --dataset_uoa='+dataset_uoa+' --dataset_file='+dataset_file+' --target_os='+tos
                       if tdid!='': repl+=' --device_id='+tdid
                       repl+=' --flags="'+jcf+'" '
                       sfc+='     relaxed replay: '+repl+'\n\n'

                   if sfc!='':
                      gg={'action':'log', 'module_uoa':cfg['module_deps']['experiment'],'file_name':cfg['log_file_own'], 'skip_header':'yes', 'text':'\n FAILED CASES:\n'+sfc+'\n'}
                      rx=ck.access(gg)

#               If no frontier, points will not be added, so will not use it
#                ri=r['recorded_info']
#                points2=ri['points']

                # Load updated point info
                r=ck.access(iii)
                if r['return']>0: return r
                results2=r.get('points',{})

                for k in results2:
                    kk=k.get('point_uid','')
                    if kk!='' and kk not in points2:
                       if k.get('features',{}).get('permanent','')=='yes':
                          points2p.append(kk)
                       else:
                          points2.append(kk)

             # Prepare some meta
             if xprune!='yes':
                # Prepare meta
                pif=pi.get('features',{})

                plat_uid=pif.get('platform_uid','')
                plat_cpu_uid=pif.get('cpu_uid','')
                plat_os_uid=pif.get('os_uid','')
                plat_gpu_uid=pif.get('gpu_uid','')

                # Find if need to add points
                points_to_add=[]

                # Good points 
                report=''
                keys=[]
                if len(points2)>0:
                   if len(ik)>0:
                      for x in ik:
                          keys.append(x)
                      for x in pk:
                          keys.append(x)

                      # Find size of keys
                      il=0
                      for k in keys:
                          k1=pdesc.get(k,{}).get('desc','')
                          if k1=='': k1=k

                          if len(k1)>il: il=len(k1)

                      # Find point in results
                      qi=0
                      for q in points2:
                          ppp={}

                          qq={}
                          for e in results2:
                              if e.get('point_uid','')==q:
                                 qq=e
                                 break

                          if len(qq)>0:
                             behavior2=qq.get('flat',{})
                             choices2=qq.get('features_flat',{})
                             ft=qq.get('features',{})

                             suid=ft.get('features',{}).get('solution_uid','')
                             if suid!='':
                                report+='            Skipping pre-existing solution '+suid+' ...'
                             else:
                                choices_order2=ft.get('choices_order',[])

                                rx=prune_choices({'choices':choices2,
                                                  'choices_order':choices_order2})
                                if rx['return']>0: return rx

                                ppp['pruned_choices']=rx['pruned_choices']
                                ppp['pruned_choices_order']=rx['pruned_choices_order']

                                qi+=1
                                report+='        '+str(qi)+':\n'

                                for k in keys:
                                    dv=behavior2.get(k,None)

                                    if dv!=None:
                                       y=''
                                       try:
                                          y=('%.3f' % dv)
                                       except Exception as e: 
                                          y=dv
                                          pass

                                       k1=pdesc.get(k,{}).get('desc','')
                                       if k1=='': k1=k

                                       ix=len(k1)

                                       report+='          * '+k1+(' ' * (il-ix))+' : '+y+'\n' 

                                ppp['characteristics']={}
                                for k in ok:
                                    dv=behavior2.get(k,None)
                                    ppp['characteristics'][k]=dv
                                    # temporally hardwire the following - later move the whole characteristics thing 
                                    # to proper and sperate program.benchmarking
                                    k='##characteristics#run#repeat#min'
                                    ppp['characteristics'][k]=behavior2.get(k,None)

                                ppp['improvements']={}
                                for k in ik:
                                    dv=behavior2.get(k,None)
                                    ppp['improvements'][k]=dv

                                ppp['misc']={}
                                for k in pk:
                                    dv=behavior2.get(k,None)
                                    ppp['misc'][k]=dv

                                points_to_add.append(ppp)

                # Prepare and possibly prune new solution
                if replay!='yes':
                   # remove user solutions (if there is a good solution, it will be added next here)
                   solsx=[]
                   for q in sols:
                       if q.get('solution_uid','')!='': solsx.append(q)
                   sols=solsx

                   suid=''
                   if len(points_to_add)>0:
                      # Generate new solution UID
                      r=ck.gen_uid({})
                      if r['return']>0: return r
                      suid=r['data_uid'] # solution UID

                      # Generate last touch UID
                      r=ck.gen_uid({})
                      if r['return']>0: return r
                      ltuid=r['data_uid'] # solution UID

                      # Sort points by first key
                      points_to_add=sorted(points_to_add, key=lambda v: (ck.safe_float(v.get(ik0,0.0),0.0)), reverse=True)

                      # Prepare new solution
                      sol={'solution_uid':suid,
                           'choices':choices,
                           'extra_meta':emeta,
                           'ref_choices':pchoices1,
                           'ref_choices_order':pchoices_order1,
                           'points':points_to_add,
                           'iterations':iterations,
                           'touched':1,
                           'last_touch_uid':ltuid,
                           'validated':1}
                      if user!='' and user!='-':
                         sol['user']=user

                      if no_run=='yes':
                         rrr['off_line']={'solutions':[sol],
                                          'module_uoa':work['self_module_uid'],
                                          'repo_uoa':er,
                                          'remote_repo_uoa':esr,
                                          'scenario_module_uoa':smuoa,
                                          'meta':meta,
                                          'meta_extra':emeta,
                                          'solutions':sols,
                                          'solution_uid':suid,
                                          'workload':workload,
                                          'iterations':iterations,
                                          'first_key':ik0}

                      else:
                         report='      New SOLUTION ('+suid+'):\n\n'+report

                      # trying to prune (unless skiping)
                      if sp!='yes' and no_run!='yes':
                         # Flash report
                         report=report+'\n    ****** Starting pruning new solution ... ******\n\n'

                         if o=='con' and report!='':
                            ck.out('')
                            ck.out(report)

                         gg={'action':'log', 'module_uoa':cfg['module_deps']['experiment'],'file_name':cfg['log_file_own'], 'skip_header':'yes', 'text':report}
                         r=ck.access(gg)

                         report=''

                         # preparing pruning
                         ii={'action':'prune',

                             'module_uoa':smuoa,

                             'host_os':hos,
                             'target_os':tos,
                             'target_device_id':tdid,

                             'solutions':[sol],

                             'dependencies':sdeps,

                             'repetitions':rep,
                             'repeat':repeat,

                             'quiet':'yes',

                             'out':oo
                            }

                         iix=copy.deepcopy(ii)

                         rx=ck.access(ii)
                         if rx['return']>0: return rx

                         gg={'action':'log', 'module_uoa':cfg['module_deps']['experiment'],'file_name':cfg['log_file_own'], 'skip_header':'yes', 'text':rx.get('report','')}
                         ry=ck.access(gg)

                         # removing pruning experiment entry if needed
                         if kexp!='yes':
                            ri=rx.get('recorded_info',{})
                            euoax=ri.get('last_recorded_uid','')

                            if euoax!='':
                               if o=='con':
                                  ck.out('')
                                  ck.out('Removing pruning experiment entry '+euoax+' ...')

                               ii={'action':'rm',
                                   'module_uoa':cfg['module_deps']['experiment'],
                                   'data_uoa':euoax,
                                   'force':'yes'}
                               ry=ck.access(ii)
                               # Skip return code

                         sol=rx['solutions'][0]
                         sol['pruned']='yes'

                         # rerun last solution after purning to get correct stats
                         if o=='con':
                            ck.out('')
                            ck.out('    ****** Running last pruned solution ******')

                         ii=copy.deepcopy(iix)
                         ii['action']='replay'
                         ii['ignore_comparison']='yes'
                         ii['solutions']=[sol]

                         rx=ck.access(ii)
                         if rx['return']>0: return rx

                         sol=rx['solutions'][0]

                         ri=rx.get('recorded_info',{})

                         lio=rx.get('last_iteration_output',{})
                         if lio.get('fail','')!='yes':
                            # Substitute points
                            # clean previous experiment entry
                            if kexp!='yes' and not unexpected:
                               if o=='con':
                                  ck.out('')
                                  ck.out('Removing experiment entry '+euoa0+' ...')

                               ii={'action':'rm',
                                   'module_uoa':cfg['module_deps']['experiment'],
                                   'data_uoa':euoa0,
                                   'force':'yes'}
                               ry=ck.access(ii)
                               # Skip return code

                            # new points to pack solution
                            euoa0=ri['recorded_uid']
                            points2=ri['points']
                            points2p=[]

                            # Rebuild solution
                            points=sol.get('points',[])
#                            qi=0
                            for p in range(0, len(points)):
                                pp=points[p]

#                                qi+=1
#                                report+='        '+str(qi)+':\n'

                                behavior2=pp.get('reaction_raw_flat',{})

#                                for k in keys:
#                                    dv=behavior2.get(k,None)
#
#                                    if dv!=None:
#                                       y=''
#                                       try:
#                                          y=('%.3f' % dv)
#                                       except Exception as e: 
#                                          y=dv
#                                          pass
#
#                                       k1=pdesc.get(k,{}).get('desc','')
#                                       if k1=='': k1=k
#
#                                       ix=len(k1)
#
#                                       report+='          * '+k1+(' ' * (il-ix))+' : '+y+'\n' 

                                x=pp.get('misc',{})
                                for k in x:
                                    dv=behavior2.get(k,None)
                                    x[k]=dv
                                pp['misc']=x

                                if 'reaction_raw_flat' in pp: del(pp['reaction_raw_flat'])

                                x=pp.get('improvements_reaction',{})
                                pp['improvements']=x

                                if 'improvements_reaction' in pp: del(pp['improvements_reaction'])

                                if 'reaction_info' in pp: del(pp['reaction_info'])

                                points[p]=pp

                            sol['points']=points

                      # Append new solution
                      points_to_add=sol.get('points',[])

                      if len(points_to_add)>0:
                         sol['solution_uid']=suid # renew (otherwise deleted by pipeline)
                         sols.append(sol)

                # Pack solution(s) if new ****************************************************************
                ps=''
                if len(points_to_add)>0:
                   # Sort here 
                   if la!='yes':
                      # Packing new points
                      if o=='con':
                         ck.out('')
                         ck.out('       Packing good points of solution(s) ...')

                      # Add original points and remove delete ones
                      ppoints=[]
                      for q in points2:
                          ppoints.append(q)
                      for q in points2p: # add reference too to be able to reproduce result or find discriminating features!
                          ppoints.append(q)

                      rx=ck.access({'action':'pack',
                                    'module_uoa':cfg['module_deps']['experiment'],
                                    'data_uoa':euoa0,
                                    'points':ppoints})
                      if rx['return']>0: return rx
                      ps=rx['file_content_base64']

                # Draw reactions, if needed
                if no_run=='yes':
                   rrr['original_target_exe']=target_exe_0
                   rrr['original_path_exe']=target_path_0
                   rrr['new_path_exe']=target_path_1
                   if 'off_line' in rrr:
                      rrr['off_line']['packed_solution']=ps

                else:
                   if recrf!='':
                      table_orig=[]
                      table_new=[]

                      si=0
                      for s in range(0, len(sols)):
                          sol=sols[s]
                          si+=1

                          points=sol.get('points',[])
                          for p in range(0, len(points)):
                              point=points[p]

                              # Check if reaction
                              imp=point.get('improvements',{})
                              ov=imp.get(ik0,0.0) # Here we put 0.0 even if None for a graph

                              rrf=point.get('reaction_raw_flat',{})
                              nv=rrf.get(ik0,0.0) # Here we put 0.0 even if None for a graph

                              table_orig.append([si, ov])
                              table_new.append([si, nv])

                          d={
                              "module_uoa":"graph",

                              "table":{"0": table_orig, "1":table_new},

                              "ignore_point_if_none":"yes",

                              "plot_type":"mpl_2d_bars",

                              "display_y_error_bar":"no",

                              "title":"Powered by Collective Knowledge",

                              "axis_x_desc":"Solution",
                              "axis_y_desc":"Improvement ("+ik0+")",

                              "plot_grid":"yes",

                              "mpl_image_size_x":"12",
                              "mpl_image_size_y":"6",
                              "mpl_image_dpi":"100"
                            }

                          rx=ck.save_json_to_file({'json_file':recrf, 'dict':d})
                          if rx['return']>0: return rx

                   # Report ****************************************************************
                   rrr['solutions']=sols

                   if len(sols)==0:
                      report='      New solutions were not found...\n\n'+report

                   # Finish report
                   if o=='con' and report!='':
                      ck.out('')
                      ck.out(report)

                   gg={'action':'log', 'module_uoa':cfg['module_deps']['experiment'],'file_name':cfg['log_file_own'], 'skip_header':'yes', 'text':report}
                   r=ck.access(gg)

                   # Add/update solution ********************************************************************
                   if replay!='yes' and len(sols)>0:
                      if o=='con':
                         ck.out('')
                         ck.out('       Adding/updating solution(s) in repository ...')

                      # Adding solution
                      ii={'action':'add_solution',
                          'module_uoa':work['self_module_uid'],
                          'repo_uoa':er,
                          'remote_repo_uoa':esr,
                          'scenario_module_uoa':smuoa,
                          'meta':meta,
                          'meta_extra':emeta,
                          'solutions':sols,
                          'solution_uid':suid,
                          'workload':workload,
                          'packed_solution':ps,
                          'iterations':iterations,
                          'first_key':ik0,
                          'user':user,
                          'out':oo}
                      rx=ck.access(ii)
                      if rx['return']>0: return rx

                      if rx.get('recorded','')=='yes':
                         ri=rx.get('recorded_info',{})
                         xlog=ri.get('log','')

                         rz=ck.access({'action':'log',
                                       'module_uoa':cfg['module_deps']['experiment'],
                                       'file_name':cfg['log_file_results'],
                                       'text':xlog})
                         if rz['return']>0: return rz

          rrr['scenario_desc']=sdesc
          rrr['subscenario_desc']=ssdesc

          ################################################################################
          # Clean temporal directory and entry
          if ktmp!='yes' and no_run!='yes':
             if o=='con':
                ck.out('')
                ck.out('Removing temporal directory '+ftmp_dir+' ...')
             import shutil
             os.chdir(curdir)
             try:
                shutil.rmtree(ftmp_dir, ignore_errors=True)
             except Exception as e: 
                if o=='con':
                   ck.out('')
                   ck.out('WARNING: can\'t fully erase tmp dir')
                   ck.out('')
                pass

          if kexp!='yes' and not unexpected:
             if o=='con':
                ck.out('')
                ck.out('Removing experiment entry '+euoa0+' ...')
#
             ii={'action':'rm',
                 'module_uoa':cfg['module_deps']['experiment'],
                 'data_uoa':euoa0,
                 'force':'yes'}
             r=ck.access(ii)
             # Skip return code
          else:
             if o=='con':
                ck.out('')
                ck.out('Note that you can:')
                ck.out('  * replay above experiments via "ck replay experiment:'+euoa0+' (--point={above solution UID})"')
                if xprune!='yes' and replay!='yes':
                   ck.out('  * plot non-interactive graph for above experiments via "ck plot graph:'+euoa0+'"')
                   ck.out('  * view these experiments in a browser via "ck browse experiment:'+euoa0+'"')

       if i.get('once','')=='yes':
          finish=True

    # Record solutions if needed
    if i.get('record_solutions','')=='yes':
       rx=ck.save_json_to_file({'json_file':sf,'dict':{"solutions":rrr['solutions']}})
       if rx['return']>0: return rx

    return rrr

##############################################################################
# compare results (if similar or not)

def compare_results(i):
    """
    Input:  {
              results     - dict with results from experiments
              point0      - original point
              point1      - new point to compare
              keys        - keys to compare
              (keys_desc) - keys description
              (threshold) - 0.03
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    report=''

    results=i['results']
    puid0=i['point0']
    puid1=i['point1']
    keys=i['keys']

    dkeys=i.get('keys_desc',{})
    diff='no'

    t=i.get('threshold','')
    if t=='': t=0.03
    t=float(t)

    ch0={}
    for q in results:
        if q['point_uid']==puid0:
           ch0=q.get('flat',{})
           break

    ch1={}
    for q in results:
        if q['point_uid']==puid1:
           ch1=q.get('flat',{})
           break

    fine=True
    for k in keys:
        k1=dkeys.get(k,{}).get('desc','')
        if k1=='': k1=k

        v0=ch0.get(k, None)
        v1=ch1.get(k, None)

        if (v0==None and v1!=None) or (v0!=None and v1==None):
           report='  Difference for "'+k1+'" - v0!=v1'
           fine=False
           break
        else:
           if type(v0)==float or type(v0)==int or type(v0)==ck.type_long:
              if not (type(v1)==float or type(v1)==int or type(v1)==ck.type_long):
                 report='  Difference for "'+k1+'" - types do not match'
                 fine=False
                 break
              else:
                 if v1==0:
                    report='  Difference for "'+k1+'" - v1=0'
                    fine=False
                    break

                 d=float(v0)/float(v1)
                 if d<(1-t) or d>(1+t):
                    report='  key "'+k1+'" variation out of normal ('+('%2.3f'%d)+')'
                    fine=False
                    break

           elif v0!=v1:
                report='  key "'+k1+'" - v0!=v1'
                fine=False
                break

    if not fine: 
       diff='yes'

    return {'return':0, 'different':diff, 'report':report}

##############################################################################
# prepare links

def links(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    h='<div style="background-color:#FFCF8F;padding:5px;margin:5px">\n'
    h+='<center>'
    h+='[ Participated '
    h+='  <a href="http://cknowledge.org/repo/web.php?action=index&module_uoa=wfe&native_action=show&native_module_uoa=experiment.user">users</a>, \n'
    h+='  <a href="http://cknowledge.org/repo/web.php?action=index&module_uoa=wfe&native_action=show&native_module_uoa=platform">platforms</a>, \n'
    h+='  <a href="http://cknowledge.org/repo/web.php?action=index&module_uoa=wfe&native_action=show&native_module_uoa=platform.os">OS</a>, \n'
    h+='  <a href="http://cknowledge.org/repo/web.php?action=index&module_uoa=wfe&native_action=show&native_module_uoa=platform.cpu">CPU</a>, \n'
    h+='  <a href="http://cknowledge.org/repo/web.php?action=index&module_uoa=wfe&native_action=show&native_module_uoa=platform.gpu">GPU</a>, \n'
    h+='  <a href="http://cknowledge.org/repo/web.php?action=index&module_uoa=wfe&native_action=show&native_module_uoa=platform.gpgpu">GPGPU</a>, \n'
    h+='  <a href="http://cknowledge.org/repo/web.php?action=index&module_uoa=wfe&native_action=show&native_module_uoa=platform.nn">NN</a>, \n'
    h+='  <a href="http://cknowledge.org/repo/web.php?action=index&module_uoa=wfe&native_action=show&native_module_uoa=platform.npu">NPU</a> ] \n'
    h+='[ <a href="https://github.com/ctuning/ck/wiki/Crowdsourcing-optimization">How to participate</a> ] \n'
    h+='[ Motivation (<a href="https://www.slideshare.net/GrigoriFursin/adapting-to-a-cambrian-aiswhw-explosion-with-open-codesign-competitions-and-collective-knowledge">PPT</a>) (<a href="https://portalparts.acm.org/3230000/3229762/fm/frontmatter.pdf">PDF</a>) ] \n'
    h+='[ Papers <a href="https://arxiv.org/abs/1801.08024">1</a> , <a href="https://arxiv.org/abs/1506.06256">2</a> , <a href="https://www.researchgate.net/publication/304010295_Collective_Knowledge_Towards_RD_Sustainability">3</a>] \n'
    h+='[ <a href="http://cKnowledge.org/android-apps.html"><b>Android app</b></a> ] \n'
    h+='[ <b><a href="http://cknowledge.org/repo/web.php?wcid=42b9a1221eb50259:collective_training_set">Collective training set</a></b> ] \n'
    h+='[ <b><a href="http://cKnowledge.org/ai">Unified AI</a></b> ] \n'

#    h+='[ <a href="https://github.com/ctuning/ck"><b>open research SDK</b></a> ], \n'
#    h+='[ <b>Android apps to crowdsource experiments:</b> <a href="http://cKnowledge.org/android-apps.html">small kernels</a>, <a href="https://play.google.com/store/apps/details?id=openscience.crowdsource.video.experiments">apps (DNN)</a>) ], \n'
#    h+='[ A few papers: <a href="http://arxiv.org/abs/1506.06256">CPC\'15</a>, \n'
#    h+='  <a href="https://www.researchgate.net/publication/304010295_Collective_Knowledge_Towards_RD_Sustainability">DATE\'16</a>, \n'
#    h+='  <a href="http://arxiv.org/abs/1406.4020">TRUST@PLDI\'14</a>, <a href="http://cknowledge.org/interactive-report">interactive</a>,\n'
#    h+='  <a href="https://www.youtube.com/watch?v=Q94yWxXUMP0">YouTube</a>\n'
#    h+='  ], \n'
#    h+='[ <a href="http://cTuning.org/ae">Our reproducible initiative for ACM conferences</a> ], \n'
#    h+='[ <a href="http://dividiti.blogspot.fr/2017/02/we-received-test-of-time-award-for-our.html">CGO\'17 test of time award for our interdisiplinary R&D</a> ], '
#    h+='[ <b><a href="http://cknowledge.org/ai/ck-api-demo">Open and unified CK API for AI</a></b> ] '

    h+='</center>\n'
    h+='</div>\n'

#    # Here we close main div and create a dummy one
#    h+='</div>\n'
#    h+='<div>\n'


    return {'return':0, 'html':h}

##############################################################################
# prune choices (leave only from iterations)

def prune_choices(i):
    """
    Input:  {
               choices       - dict of choices
               choices_order - choices order
            }

    Output: {
              return               - return code =  0, if successful
                                                 >  0, if error
              (error)              - error text if return > 0

              pruned_choices       - leave only tuning keys (values)
              pruned_choices_order - leave only tuning keys (order)
            }

    """

    pc={}
    pco=[]

    choices=i.get('choices',{})
    corder=i.get('choices_order',[])

    for q in sorted(corder):
        if q.startswith('##'):
           q1='##choices'+q[1:]
           v=choices.get(q1, None)

           if v!=None:
              pc[q]=v
              pco.append(q)

    return {'return':0, 'pruned_choices':pc, 'pruned_choices_order':pco}

##############################################################################
# get solutions

def get(i):
    """
    Input:  {
              (repo_uoa)          - repo_uoa
              scenario_module_uoa - scenario UID
              (meta)              - search by meta
              (smeta)             - search solution meta (program_uoa, cmd, etc)

              (data_uoa)          - narrow search
              (solution_uid)      - return only this solution
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              if i['only_choices']=='yes':
               choices_list       - list of choices, ready to add to autotuning

              else:
               found
               repo_uoa
               module_uoa
               data_uoa
               solutions          - list of solutions
            }

    """

    import os

    o=i.get('out','')

    ruoa=i.get('repo_uoa','')
    meta=i.get('meta',{})
    smeta=i.get('smeta',{})

    duoa=i.get('data_uoa','')

    smuoa=i['scenario_module_uoa']

    suid=i.get('solution_uid','')
    oc=i.get('only_choices','')

    choices=[]

    # Search if exists
    if o=='con': 
       ck.out('')
       ck.out('  Searching scenario solutions ...')

    ii={'action':'search',
        'common_func':'yes',
        'repo_uoa': ruoa,
        'module_uoa': smuoa,
        'data_uoa':duoa,
        'add_meta':'yes'
       }
    if len(meta)>0:
       ii['search_dict']={'meta':meta}

    r=ck.access(ii)
    if r['return']>0: return r
    rl=r['lst']

    et=r.get('elapsed_time','')
    if et!='' and o=='con':
       ck.out('      Elapsed time (s) :'+str(et))

    # Check solution (should be one)
    psols=[] # pruned solutions
    sols=[]

    fruoa=''
    fmuoa=''
    fduoa=''

    found='no'

    lsid=''

    if len(rl)>0:
       rlx=rl[0]

       fruoa=rlx['repo_uid']
       fmuoa=rlx['module_uid']
       fduoa=rlx['data_uid']

       found='yes'

       p=rlx['path']

       psum=os.path.join(p, fsummary)
       if os.path.isfile(psum):
          rx=ck.load_json_file({'json_file':psum})
          if rx['return']>0: return rx
          sols=rx['dict']

       # Check if exists by the same choices
       for q in sols:
           qmeta=q.get('choices',{})

           equal='yes'

           if len(smeta)>0:
              rx=ck.compare_dicts({'dict1':qmeta, 'dict2':smeta})
              if rx['return']>0: return rx
              equal=rx['equal']

           if equal=='yes': 
              if suid!='':
                 if q.get('solution_uid','')!=suid:
                    equal='no'

              if equal=='yes':
                 psols.append(q)

    return {'return':0, 'solutions':psols, 'solutions_info':{'found':found, 'repo_uoa':fruoa, 'module_uoa':fmuoa, 'data_uoa':fduoa}}

##############################################################################
# replay optimization solution

def replay(i):
    """
    Input:  {
               (solutions)          - pre-existing solutions (to avoid getting it from repos)
               (solutions_info)     - pre-existing solutions info (for scenario)

               (local)              - use local repositories. By default - crowdtuning repo (remote-ck)

               (repo_uoa)           - repo UOA with optimization
               (remote_repo_uoa)    - if repo above is remote, use this repo on remote machine

               (data_uoa)           - experiment data UOA (can have wildcards)

               (solution_uid)       - solution UID, if known (otherwise all - useful to classify a given program by reactions to optimizations)

               (prune)              - if 'yes', prune solution

               (record_solutions)   - if 'yes', record solutions
               (solutions_file)     - output solutions to a file

               (record_reactions)         - if 'yes', record optimization reaction
               (record_reactions_file)    - file to record reaction table for graph ...

               (ignore_comparison)        - if 'yes', do not compare results
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              solutions    - processed solutions (including reactions)
            }

    """

    import copy
    import os

    curdir=os.getcwd()

    o=i.get('out','')

    xprune=i.get('prune','')

    sols=ck.get_from_dicts(i, 'solutions', '', None)
    sols_info=ck.get_from_dicts(i, 'solutions_info', {}, None)

    ruoa=ck.get_from_dicts(i, 'repo_uoa', '', None)
    rruoa=ck.get_from_dicts(i, 'remote_repo_uoa', '', None)

    local=ck.get_from_dicts(i, 'local', '', None)

    if ruoa=='' and local!='yes':
       ruoa=ck.cfg['default_exchange_repo_uoa']

    muoa=ck.get_from_dicts(i, 'module_uoa', '', None)
    mruoa=ck.get_from_dicts(i, 'module_ref_uoa', '', None)
    if mruoa!='': muoa=mruoa

    # Check if it's generic program.optimization and scenario pre-exists
    x=sols_info.get('module_uoa','')
    if x!='':
       if muoa==work['self_module_uoa'] or muoa==work['self_module_uid']:
          muoa=x

    if muoa==work['self_module_uoa'] or muoa==work['self_module_uid']:
       return {'return':1, 'error':'scenario_module_uoa is not defined'}

    # Check specific replay/prune params from the scenario module
    rx=ck.access({'action':'load',
                  'module_uoa':cfg['module_deps']['module'],
                  'data_uoa':muoa})
    if rx['return']>0: return rx
    drx=rx['dict']

    duoa=ck.get_from_dicts(i, 'data_uoa', '', None)

    scenario=ck.get_from_dicts(i, 'scenario', '', None)
    if scenario=='-':
       scenario=''
    elif scenario=='':
       scenario=muoa

    suid=ck.get_from_dicts(i, 'solution_uid', '', None)

    if 'module_cfg' in i: del(i['module_cfg'])
    if 'module_work' in i: del(i['module_work'])
    if 'xcids' in i: del(i['xcids'])
    if 'cids' in i: del(i['cids'])
    if 'cid' in i: del(i['cid'])

    ic=copy.deepcopy(i)

    # Get solutions
    if len(sols)==0:
       ii={'action':'get',
           'repo_uoa':ruoa,
           'module_uoa':work['self_module_uid'],
           'scenario_module_uoa':muoa,
           'data_uoa':duoa}
       if rruoa!='': 
          ii['remote_repo_uoa']=rruoa
       if suid!='': 
          ii['solution_uid']=suid
       r=ck.access(ii)
       if r['return']>0: return r

       sols=r['solutions']

    # Check solutions
    osols=copy.deepcopy(sols) # original solutions
    isols=len(sols)
    if isols==0:
       return {'return':1, 'error':'solutions not found'}

    if o=='con':
       ck.out(str(isols)+' solution(s) found - checking ...')

    # Run autotuning
    ic['action']='autotune'
    ic['module_uoa']=cfg['module_deps']['program']

    ic['solutions']=sols
    ic['scenario']=scenario

    if ic.get('new','')=='':
       ic['new']='yes'

    if ic.get('iterations','')=='':
       if xprune=='yes':
          pp=sols[0].get('points',[])
          if len(pp)==0 or len(pp[0].get('pruned_choices',{}))==0:
             return {'return':1, 'error':'points in first solution are not found'}
          ic['iterations']=len(pp[0]['pruned_choices'])+1
          ic['prune_invert_add_iters']='yes'
       else:
          ic['iterations']=0 # Correct ones will be calculated further

    ignore=[]
    if ic.get('program_uoa','')!='':
       ic['data_uoa']=ic['program_uoa']
       del(ic['program_uoa'])

       ignore.append('program_tags')
       ignore.append('data_uoa')
       ignore.append('cmd_key')
       ignore.append('dataset_uoa')
       ignore.append('dataset_file')

       renew_workload_info=True

    if ic.get('cmd_key','')!='':
       ignore.append('dataset_uoa')
       ignore.append('dataset_file')

    if ic.get('dataset_uoa','')!='':
       ignore.append('dataset_file')

    # Pre-select various params from the first solution
    choices=sols[0].get('choices',{})

    for q in choices:
        if q in ignore:
           continue
        if ic.get(q,'')=='':
           ic[q]=choices[q]

    # If prune, check specific params (such as prune_md5)
    if xprune=='yes':
       ic.update(drx.get('prune_autotune_pipeline',{}))
    else:
       ic['replay']='yes'

    ic['skip_collaborative']='yes'

    rrr=ck.access(ic)
    if rrr['return']>0: return rrr

    # Check and classify solutions
    sols=rrr.get('solutions',[])

    # Print results
    if o=='con' and xprune!='yes' and i.get('ignore_comparison','')!='yes':
       ck.out('')
       ck.out('  Comparing original and new improvements:')

       keys=[]
       ll=0

       for q in sols:
           suid=q.get('solution_uid','')

           ck.out('')
           ck.out('    * Solution '+suid+':')

           points=q.get('points',[])

           ip=0
           for p in points:

               ip+=1

               ck.out('')
               ck.out('        Point: '+str(ip))

               oimp=p.get('improvements',{})
               imp=p.get('improvements_reaction',{})

               if len(keys)==0:
                  keys=sorted(list(oimp.keys()))
                  for k in keys:
                      if len(k)>ll: ll=len(k)

               ck.out('')
               for k in keys:
                   ov=oimp.get(k, None)
                   v=imp.get(k, None)

                   x=''
                   if ov!=None:
                      j=ll-len(k)

                      x+=('%2.2f' % ov)

                      x+=' vs '

                      if v!=None:
                         x+=('%2.2f' % v)
                      else:
                         x+='None'

                   ck.out('             '+k+(' '*j)+' : '+x) 

    return rrr

##############################################################################
# classify solutions

def classify(i):
    """
    Input:  {
              solutions         - list of solutions with reactions
              key               - key for classification analysis/sorting
              (force_best_suid) - if !='', return it as best UID (when new solution found)
              (skip_clean)      - if 'yes', do not remove reactions
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import copy

    sols=i['solutions']

    choices=i.get('choices',{})
    extra_meta=i.get('extra_meta',{})

    fbsuid=i.get('force_best_suid','')

    sclean=i.get('skip_clean','')

    cc={}

    key=i['key']

    best_suid=''
    worst_suid=''

    best_v=1.0
    worst_v=1.0

    wimp={}
    wdeg={}

    checked=[] # Checked solutions for this workload

    si=0
    for s in range(0, len(sols)):
        sol=sols[s]
        si+=1

        suid=sol.get('solution_uid','')
        checked.append(suid)

        points=sol.get('points',[])
        for p in range(0, len(points)):
            point=points[p]

            # Check if reaction
            imp=point.get('improvements',{})
            ov=imp.get(key,0.0) # Here we put 0.0 even if None for a graph

            best=point.get('improvements_best',{})
            worst=point.get('improvements_worst',{})

            if len(best)==0: 
               best=imp
               worst=imp





            oimp=copy.deepcopy(imp)

            ov=imp.get(key,0.0) # Here we put 0.0 even if None for a graph

            rrf=point.get('reaction_raw_flat',{})
            nv=rrf.get(key,0.0) # Here we put 0.0 even if None for a graph

            nimp={}
            for k in imp:
                nimp[k]=rrf.get(k, None)

            best=point.get('improvements_best',{})
            worst=point.get('improvements_worst',{})


            # Update solution only if new reaction is better by the main key
            if point.get('reaction_info',{}).get('fail','')!='yes' and nv>ov:
               imp=nimp

            # clean reactions from original
#            if sclean!='yes':
#               if 'reaction_info' in point:
#                  del(point['reaction_info'])
#               if 'improvements_reaction' in point:
#                  del(point['improvements_reaction'])
#               if 'reaction_raw_flat' in point:
#                  del(point['reaction_raw_flat'])

            # Check all keys for historical best/worst by first key
            best=point.get('improvements_best',{})
            worst=point.get('improvements_worst',{})

            for k in imp:
                v=nimp.get(k, None)
                if v==None:
                   v=imp.get(k, None)

                vbo=best.get(k, None)
                vwo=worst.get(k, None)
                
                if v!=None and (vbo==None or v>vbo): best[k]=v
                if v!=None and (vwo==None or v<vwo): worst[k]=v

            if len(best)==0: best=oimp # if new solution

            point['improvements_best']=best
            point['improvements_worst']=worst

            # If didn't fail, check best/worst by main key only for classification!
            if point.get('reaction_info',{}).get('fail','')!='yes':
               v=imp.get(key,None)

               if v!=None: 
                  if fbsuid=='' and v>best_v: 
                     best_v=v
                     best_suid=suid
                     wimp=imp

                  if v<worst_v and v<0.97: 
                     worst_v=v
                     worst_suid=suid
                     wdeg=imp

            if fbsuid!='' and fbsuid==suid:
               wimp=imp

        points[p]=point
        sols[s]=sol

    if fbsuid!='': best_suid=fbsuid

    cc['best_solution_uid']=best_suid
    cc['worst_solution_uid']=worst_suid
    cc['workload_improvements']=wimp
    cc['workload_degradations']=wdeg
    cc['checked']=checked

    return {'return':0, 'solutions':sols, 'classification':cc}

##############################################################################
# prune solutions

def prune(i):
    """
    See "replay" API
    """

    import os


    try:
        curdir=os.getcwd()
    except OSError:
        os.chdir('..')
        curdir=os.getcwd()

    o=i.get('out','')

    graph=i.get('graph','')
    if 'graph' in i: del(i['graph'])

    i['prune']='yes'

    if i.get('invert','')=='yes':
       del(i['invert'])
       i['prune_invert']='yes'

    r=replay(i)
    if r['return']>0: return r

    sol=r['solutions'][0]['points'][0]

    pruned_influence=sol.get('pruned_influence',{})
    pruned_chars=sol.get('pruned_chars',[])
    pruned_inversed_flags=sol.get('pruned_inversed_flags',{})

    pruned_choices_order=sol.get('pruned_choices_order',[])
    pruned_choices=sol.get('pruned_choices',{})

    if graph=='yes' and len(pruned_influence)>0 and len(pruned_chars)>0:
       gf=i.get('graph_file','')
       if gf=='':
          gf=os.path.join(curdir, fgraph)

       table={}
       jx=0
       for k in pruned_chars:
           jj=str(jx)
           table[jj]=[]
           jx+=1

       xlabels=[]

       j=0
       k0=pruned_chars[0]

       # remove null
       pin={}
       for q in pruned_influence:
           if (pruned_influence[q].get(k0,0.0))!=None:
              pin[q]=pruned_influence[q]

       for q in sorted(pin, key=lambda v: (ck.safe_float(pruned_influence[v].get(k0,0.0),0.0))):
           qq=pruned_influence[q]

           qv=pruned_choices.get(q,None)
           if qv=='' or qv==None:
              qv=pruned_inversed_flags.get(q,'')
              if qv=='': qv=q
              x='Adding '+qv
           else:
              x='Removing '+str(qv)

           xlabels.append(x)

           jx=0
           for k in pruned_chars:
               vv=[j]
               vv.append(qq.get(k,None))

               jj=str(jx)
               table[jj].append(vv)
               jx+=1

           j+=1

       d={
           "module_uoa":"graph",

           "table":table,
           "axis_x_labels":xlabels,

           "ignore_point_if_none":"yes",

           "plot_type":"mpl_2d_bars",

           "display_y_error_bar":"no",

           "title":"Powered by Collective Knowledge",

           "ymax":1.1,

           "axis_x_desc":"Solution",
           "axis_y_desc":"Improvement",

           "legend":pruned_chars,

           "plot_grid":"yes",

           "mpl_image_size_x":"12",
           "mpl_image_size_y":"6",
           "mpl_image_dpi":"100"
         }

       rx=ck.save_json_to_file({'json_file':gf, 'dict':d})
       if rx['return']>0: return rx

       if o=='con':
          ck.out('')
          ck.out('Note: graph with reactions to pruned optimizations was recorded. Plot it via "ck graph @'+fgraph+'"')

    return r


##############################################################################
# get workloads for a given solution

def get_workloads(i):
    """
    Input:  {
              (repo_uoa)          - repo_uoa
              scenario_module_uoa - scenario UID
              data_uoa            - narrow search
              solution_uid        - return only this solution
              (key)               - default 'best', can be 'worst'
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              workloads    - list of workloads
            }

    """

    import os

    o=i.get('out','')

    ruoa=i.get('repo_uoa','')
    duoa=i.get('data_uoa','')

    smuoa=i['scenario_module_uoa']

    suid=i.get('solution_uid','')

    key=i.get('key','')
    if key=='': key='best'

    # Load solution
    ii={'action':'load',
        'repo_uoa': ruoa,
        'module_uoa': smuoa,
        'data_uoa':duoa
       }
    r=ck.access(ii)
    if r['return']>0: return r

    p=r['path']

    # Load classification file
    classification={}
    pcl=os.path.join(p, fclassification)
    if os.path.isfile(pcl):
       rx=ck.load_json_file({'json_file':pcl})
       if rx['return']>0: return rx
       classification=rx['dict']

    # Get by key
    ww=classification.get(suid,{}).get(key,{})

    return {'return':0, 'workloads':ww}

##############################################################################
# record problems (for example, when impossible to detect CPU during mobile device crowdtuning)

def problem(i):
    """
    Input:  {
               (problem)      - problem info
               (problem_data) - aux problem data
               (email)        - user ID

            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    o=i.get('out','')

    email=i.get('email','')
    user=email

    problem=i.get('problem','')
    problem_data=i.get('problem_data','')

    err='\nProblem: '+problem+'\n\n'+problem_data+'\n\n'

    ii={'action':'log', 'module_uoa':cfg['module_deps']['experiment'], 'file_name':cfg['log_file_error'], 'text':err}
    r=ck.access(ii)
    if r['return']>0: return r

    return {'return':0}

##############################################################################
# show local results

def dashboard(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    i['action']='start'
    i['module_uoa']='web'
    i['cid']=''
    i['browser']='yes'
    i['extra_url']='action=index&module_uoa=wfe&native_action=show&native_module_uoa=program.optimization'

    return ck.access(i)

##############################################################################
# return json instead of html in show (needed for CK AI API)

def show_json(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    r=show(i)
    if r['return']>0: return r

    return {'return':0, 'results':r.get('results',[])}
