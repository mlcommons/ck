#
# Collective Knowledge: crowdbenchmarking using ARM's workload automation and CK
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
compiler_choices='#choices#compiler_flags#'

line='================================================================'

fsummary='summary.json'
fclassification='classification.json'
fgraph='tmp-reactions-graph.json'
ffstat='ck-stat-flat-characteristics.json'

form_name='wa_web_form'
onchange='document.'+form_name+'.submit();'

hextra=''
#hextra+='<i><center>\n'
#hextra+=' [ <a href="http://cKnowledge.org/ai">Community-driven AI R&D powered by CK</a> ], '
#hextra+=' [ <i><a href="http://dividiti.blogspot.fr/2017/02/we-received-test-of-time-award-for-our.html">CGO\'17 test of time award for our interdisiplinary R&D</a></i> ], '
#hextra+=' [ <b><a href="http://cKnowledge.org/android-apps.html">Android app to crowd-optimize DNN engines and models</a></b> ], '
#hextra+=' [ <a href="https://github.com/ctuning/ck-caffe2">CK-Caffe2 GitHub</a> / <a href="https://github.com/dividiti/ck-caffe">CK-Caffe GitHub</a> ], '
#hextra+=' [ <a href="https://github.com/ctuning/ck-tensorflow">CK-TensorFlow GitHub</a> ], '
#hextra+=' [ <a href="https://en.wikipedia.org/wiki/Collective_Knowledge_(software)">Wikipedia</a>, \n'
#hextra+='<a href="https://www.researchgate.net/publication/304010295_Collective_Knowledge_Towards_RD_Sustainability">paper 1</a>, \n'
#hextra+='<a href="https://arxiv.org/abs/1506.06256">Paper 2</a>, \n'
#hextra+='<a href="https://www.youtube.com/watch?v=Q94yWxXUMP0">YouTube CK intro</a> ] \n'
#hextra+='</center></i>\n'
#hextra+='<br>\n'

selector=[{'name':'Scenario', 'key':'crowd_uid', 'module_uoa':'65477d547a49dd2c', 'module_key':'##dict#title'},
          {'name':'DNN engine', 'key':'engine'},
          {'name':'Model', 'key':'model'},
          {'name':'Platform', 'key':'plat_name','new_line':'no'},
          {'name':'OS', 'key':'os_name'},
          {'name':'CPU', 'key':'cpu_name', 'new_line':'no'},
          {'name':'CPU ABI', 'key':'cpu_abi'},
          {'name':'GPU', 'key':'gpu_name'}]

abis=[{'abi':'arm64-v8a',
       'os_uoa':'android21-arm64'},
      {'abi':'armeabi-v7a',
       'os_uoa':'android21-arm-v7a'}]

libxopenme='librtlxopenme.so'

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
# show results

def show(i):
    """
    Input:  {
               (crowd_module_uoa) - if rendered from experiment crowdsourcing
               (crowd_key)        - add extra name to Web keys to avoid overlapping with original crowdsourcing HTML
               (crowd_on_change)  - reuse onchange doc from original crowdsourcing HTML

               (highlight_behavior_uid) - highlight specific result (behavior)!
               (highlight_by_user)      - highlight all results from a given user

               (all)     - if 'yes', view all results

               (minimal) - if 'yes', use in interactive papers
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os
    import copy
    import time

    st=''

    minimal=i.get('minimal','')=='yes'

    cmuoa=i.get('crowd_module_uoa','')
    ckey=i.get('crowd_key','')

    debug=(i.get('debug','')=='yes')
#    debug=True

    conc=i.get('crowd_on_change','')
    if conc=='':
        conc=onchange

    hi_uid=i.get('highlight_behavior_uid','')
    hi_user=i.get('highlight_by_user','')

#    h='<hr>\n'
    h='<center>\n'
    h+='\n\n<script language="JavaScript">function copyToClipboard (text) {window.prompt ("Copy to clipboard: Ctrl+C, Enter", text);}</script>\n\n' 

    h+=hextra

#    h+='<hr>\n'
    h+='<br>\n'

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
    dt=time.time()
    ii={'action':'search',
        'module_uoa':work['self_module_uid'],
        'add_meta':'yes'}

    if cmuoa!='':
        ii['module_uoa']=cmuoa

    r=ck.access(ii)
    if r['return']>0: return r

    if debug: h+='\n<p>Debug time (CK query): '+str(time.time()-dt)+' sec.<p>\n'

    lst=r['lst']

    # Find unique variables
    dt=time.time()

    choices={}
    mchoices={} # cache of UID -> alias choices
    wchoices={}

    cache_meta={}

    for q in lst:
        d=q['meta']
        meta=d.get('meta',{})

        # Process some derivatives
        scenario=meta.get('crowd_uid','')

        kscenario=cfg['module_deps']['experiment.scenario.mobile']+':'+scenario
        if kscenario not in cache_meta:
            r=ck.access({'action':'load',
                         'module_uoa':cfg['module_deps']['experiment.scenario.mobile'],
                         'data_uoa':scenario})
            if r['return']>0: return r
            xd=r['dict']

            # Find model size
            for q in xd.get('files',[]):
                if q.get('model_weights','')=='yes':
                    xd['model_weights_size']=int(q.get('file_size',0)/1E6)
                    break

            cache_meta[kscenario]=xd
        else:
            xd=cache_meta[kscenario]

        if meta.get('engine','')=='': meta['engine']=xd.get('engine','')
        if meta.get('model','')=='': meta['model']=xd.get('model','')

        meta['engine_meta']=xd.get('engine_meta',{})

        # Process selector meta
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

                    muoa=kk.get('module_uoa','')
                    vv=v
                    if muoa!='':
                        if k not in mchoices:
                            mchoices[k]={}

                        vv=mchoices[k].get(v,'')
                        if vv=='':
                            r=ck.access({'action':'load',
                                         'module_uoa':muoa,
                                         'data_uoa':v})
                            if r['return']==0:
                                mk=kk.get('module_key','')
                                if mk=='': mk='##data_name'

                                rx=ck.get_by_flat_key({'dict':r, 'key':mk})
                                if rx['return']>0: return rx
                                vv=rx['value']

                        if vv=='' or vv==None: vv=v

                        mchoices[k][v]=vv

                    wchoices[k].append({'name':vv, 'value':v})

    if debug: h+='\n<p>Debug time (CK find unique vars): '+str(time.time()-dt)+' sec.<p>\n'

    # Prepare query div ***************************************************************
    dt=time.time()
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
            'selected_value':v,
            'style':'margin:5px;'}
        r=ck.access(ii)
        if r['return']>0: return r

        h+='<span style="white-space: nowrap"><b>'+n.replace(' ','&nbsp;')+':</b>&nbsp;'+r['html'].strip()+'</span>\n'

    if debug: h+='\n<p>Debug time (prepare selector): '+str(time.time()-dt)+' sec.<p>\n'

    # Check hidden
    if hi_uid!='':
        h+='<input type="hidden" name="highlight_behavior_uid" value="'+hi_uid+'">\n'

    if hi_user!='':
        h+='<input type="hidden" name="highlight_by_user" value="'+hi_user+'">\n'

    h+='<br><br>'

    # Prune list ******************************************************************
    dt=time.time()

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
                break # FGG added later - should be correct

        if not skip:
            # Process raw results
            arr=d.get('all_raw_results',[])

            for g in arr:
                nn=copy.deepcopy(q)

                ih=g.get('image_height',0)
                iw=g.get('image_width',0)

                it=0
                if ih!=0 and iw!=0:
                    it=ih*iw

                key=str(ih)+' x '+str(iw)

                prd=g.get('prediction','')
                if prd!='':
                    j1=prd.find('\n')
                    if j1>0:
                        j2=prd.find('\n',j1+1)
                        if j2>0:
                            prd=prd[j1:j2]

                # Check timing - currently temporal ugly hack
                t=g.get('time',[])

                tmin=0
                tmax=0

                if len(t)>0:
                    tmin=min(t)/1E3
                    tmax=max(t)/1E3

                nn['extra']={'key':key, 'raw_results':g, 'time_min':tmin, 'time_max':tmax, 'prediction':prd}

                # Check xOpenME timing
                xopenme=g.get('xopenme',{})
                xxopenme={}

                if type(xopenme)==dict:
                   for xk in xopenme:
                       t=xopenme[xk]

                       tmin=0
                       tmax=0

                       if len(t)>0:
                           tmin=min(t)
                           tmax=max(t)

                       xxopenme['xopenme_'+xk+'_min']=tmin
                       xxopenme['xopenme_'+xk+'_max']=tmax

                nn['extra'].update(xxopenme)

                plst.append(nn)

    if debug: h+='\n<p>Debug time (prune entries by user selection): '+str(time.time()-dt)+' sec.<p>\n'

    # Add extra selectors
    h+='<center>\n'

    wchoices9a=[{'name':'throughput', 'value':'throughput'}, {'name':'latency', 'value':'latency'}]
    key9a='sort_by'

    k=ckey+key9a

    v9a=''
    if i.get(k,'')!='':
        v9a=i[k]
    else:
       v9a=wchoices9a[0]['value']

    # Prepare selector
    ii={'action':'create_selector',
        'module_uoa':cfg['module_deps']['wfe'],
        'data':wchoices9a,
        'name':k,
        'onchange':conc, 
        'skip_sort':'yes',
        'selected_value':v9a}
    r=ck.access(ii)
    if r['return']>0: return r

    h+='<b>Sort by:</b> '+r['html'].strip()+'\n'

    wchoices9b=[{'name':'throughput vs top 1 accuracy', 'value':'throughput_top1'},
                {'name':'throughput vs top 5 accuracy', 'value':'throughput_top5'}, 
                {'name':'latency vs top 1 accuracy', 'value':'latency_top1'},
                {'name':'latency vs top 5 accuracy', 'value':'latency_top5'}, 
                {'name':'recognition time vs device cost vs model size', 'value':'time_cost'}]
    key9b='which_graph'

    k=ckey+key9b

    v9b=''
    if i.get(k,'')!='':
        v9b=i[k]
    else:
       v9b=wchoices9b[0]['value']

    # Prepare selector
    ii={'action':'create_selector',
        'module_uoa':cfg['module_deps']['wfe'],
        'data':wchoices9b,
        'name':k,
        'onchange':conc,
        'skip_sort':'yes',
        'selected_value':v9b}
    r=ck.access(ii)
    if r['return']>0: return r

    h+='&nbsp;&nbsp;<b>Plot:</b> '+r['html'].strip()+'\n'

    h+='</center>\n'
    h+='<p>\n'

    # Sort first before prunning
    dt=time.time()

    if v9a=='throughput':
       splst=sorted(plst, key=lambda x: x.get('extra',{}).get('xopenme_execution_time_kernel_2_min',0))
    else:
       splst=sorted(plst, key=lambda x: x.get('extra',{}).get('time_min',0))

    if debug: h+='\n<p>Debug time (sorting table): '+str(time.time()-dt)+' sec.<p>\n'

    # Demo graph
    bgraph={'0':[]} # Just for graph demo
    if hi_uid!='' or hi_user!='': bgraph['1']=[]

    # execution time vs cost
    bgraph2={'0':[]}
    igraph2={'0':[]}

    # execution time vs cost
    bgraph3={'0':[]}
    igraph3={'0':[]}
    f_bgraph3={}
    f_igraph3={}

    # Check if too many
    lplst=len(plst)
    min_view=False

    view_all=i.get('all','')
    if view_all!='': h+='<input type="hidden" name="view_all" value="'+view_all+'">\n'

    # Advertisement
    h+='<center>\n'
#    hhh+=' <a href="http://dividiti.com"><img src="http://cKnowledge.org/_resources/ai-cloud.png" height="240" style="padding:3px;"></a>\n'
#    hhh+=' <iframe width="426" height="240" src="https://www.youtube.com/embed/f4CfMrGPJPY" frameborder="0" style="padding:3px;"></iframe><br>\n'
    h+=' These are raw benchmarking/optimization results shared by volunteers from their Android devices\n'
    h+=' to test our collaborative approach to unify and crowdsource learning, benchmarking, optimization and co-design of efficient SW/HW stack for emerging workloads\n'
    h+=' across diverse devices, models and data sets. See <a href="http://cKnowledge.org/request.html">ACM ReQuEST tournaments</a> for more details!\n'
    h+='</center>\n'
    h+='<br>\n'

    if lplst==0:
        h+='<b>No results found!</b>'
        return {'return':0, 'html':h, 'style':st}
    elif lplst>100 and view_all!='yes':
        h+='<b>Too many <a href="https://arxiv.org/abs/1506.06256">species</a> ('+str(lplst)+') - see 150 top performing species or prune list further!</b><br><br>'

#        min_view=True

        # Removing entries but leave user selection
        splst1=[]
        iq=0
        for q in splst:
            rres=q['extra'].get('raw_results',{})
            buid=rres.get('behavior_uid','')
            user=rres.get('user','')

            if iq<150 or (hi_uid!='' and buid==hi_uid) or (hi_user!='' and hi_user==user):
               splst1.append(q)

            iq+=1

        splst=splst1

#        del splst[150:]

#        return {'return':0, 'html':h, 'style':st}

    # Long term TBD: here we should move table prepation either to numpy or django or both ...
    # This is just for a quick proof-of-concept (FGG)

    # Prepare table
#    bgc='afffaf'
    bgc='dfffdf'
    bg=' style="background-color:#'+bgc+';"'
    bg1=' style="background-color:#bfffbf;"'
    bg2=' style="background-color:#afffaf;"'
    bg9=' style="background-color:#afffaf;color:#7f0000;"'

    h+='<table border="1" cellpadding="7" cellspacing="0">\n'

    ha='align="center" valign="top"'
    hb='align="left" valign="top"'

    h+='  <tr style="background-color:#dddddd">\n'

    h+='   <td '+ha+'><b>#</b></td>\n'
    h+='   <td '+ha+'><b>Platform</b></td>\n'
    h+='   <td '+ha+'><b>Crowd scenario</b></td>\n'
    if not min_view:
       h+='   <td '+ha+'><b>Versions</b></td>\n'
    h+='   <td '+ha+'><b>Model weight size</b></td>\n'
    x=''
    if v9a=='latency':
       x=' style="color:#7f0000"'
    h+='   <td '+ha+x+'><b>Total time (min/max sec.)<p>*&nbsp;LATENCY&nbsp;*</b></td>\n'
    if not min_view:
       h+='   <td '+ha+'><b>Init network time (min/max sec.)</b></td>\n'
       h+='   <td '+ha+'><b>Image preparation (min/max sec.)</b></td>\n'
       x=''
       if v9a=='throughput':
          x=' style="color:#7f0000"'
       h+='   <td '+ha+x+'><b>Classification time (min/max sec.)<p>*&nbsp;THROUGHPUT&nbsp;*</b></td>\n'
       h+='   <td '+ha+'><b>Prediction probability</b></td>\n'
    h+='   <td '+ha+'><b>Power consumption (W)<br>min / max</td>\n'
    h+='   <td '+ha+'><b>Memory usage (MB)</td>\n'
    h+='   <td '+ha+'><b><a href="https://github.com/dividiti/ck-caffe/blob/master/script/explore-accuracy/explore_accuracy.20160808.ipynb">Model accuracy on ImageNet</a></td>\n'
    h+='   <td '+ha+'><b>Model topology and parameters</td>\n'
    h+='   <td '+ha+'><b>HW costs</td>\n'
    h+='   <td '+ha+'><b>All usage costs (preparation, training, inference, errors, etc)</td>\n'
    if not min_view:
       h+='   <td '+ha+'><b>Mispredictions and unexpected behavior</b></td>\n'
       h+='   <td '+ha+'><b>Image features</b></td>\n'
    h+='   <td '+ha+'><b>CPU</b></td>\n'
    if not min_view:
       h+='   <td '+ha+'><b>CPU ABI</b></td>\n'
    h+='   <td '+ha+'><b>GPU</b></td>\n'
    h+='   <td '+ha+'><b>OS</b></td>\n'
    h+='   <td '+ha+'><b>Data UID / Behavior UID</b></td>\n'
    if not min_view:
       h+='   <td '+ha+'><b>User</b></td>\n'
    h+='  <tr>\n'

    # Dictionary to hold target meta
    tm={}

    ix=0

    # Trick - want to put graph first
    hhh=h
    h=''

    dt=time.time()
    for q in splst:
        ix+=1

        duid=q['data_uid']
        path=q['path']

        d=q['meta']

        meta=d.get('meta',{})

        extra=q['extra']
        img=extra.get('img',{})
        rres=extra.get('raw_results',{})

        mp=rres.get('mispredictions',[])

        key=extra.get('key','')

        buid=rres.get('behavior_uid','')
        pred=extra.get('prediction','').replace(' ','&nbsp;')
        user=rres.get('user','')

        tmin=extra.get('time_min',0)
        tmax=extra.get('time_max',0)

        scenario=meta.get('crowd_uid','')

        plat_name=meta.get('plat_name','')
        cpu_name=meta.get('cpu_name','')
        cpu_abi=meta.get('cpu_abi','')
        os_name=meta.get('os_name','')
        gpu_name=meta.get('gpu_name','')
        gpgpu_name=meta.get('gpgpu_name','')

        plat_uid=meta.get('platform_uid','')
        cpu_uid=meta.get('cpu_uid','')
        os_uid=meta.get('os_uid','')
        gpu_uid=meta.get('gpu_uid','')
        gpgpu_uid=meta.get('gpgpu_uid','')

        te=d.get('characteristics',{}).get('run',{})

        bgx=bg
        bgx1=bg1
        bgx2=bg2
        bgx9=bg9

        if (hi_uid!='' and buid==hi_uid) or (hi_user!='' and hi_user==user):
           bgx=' style="background-color:#ffcf7f"'
           bgx1=' style="background-color:#ffbf5f"'
           bgx2=' style="background-color:#ffaf2f"'
           bgx9=' style="background-color:#ffaf2f;color:#7f0000;"'

        # Starting raw
        h+='  <tr'+bgx+'>\n'

        h+='   <td '+ha+'><a name="'+buid+'" id="'+buid+'">'+str(ix)+'</a></td>\n'

        x=plat_name
        if plat_uid!='':
            x='<a href="'+url0+'&wcid='+cfg['module_deps']['platform']+':'+plat_uid+'">'+x+'</a>'
        h+='   <td '+ha+'>'+x+'</td>\n'

        # Output scenario
        xx=mchoices.get(ckey+'crowd_uid',{}).get(scenario,'')

        kscenario=cfg['module_deps']['experiment.scenario.mobile']+':'+scenario
        xd=cache_meta[kscenario]

        xx=xd.get('title','')
        model_weights_size=int(xd.get('model_weights_size',0))+1

        fbsize=xd.get('features',{}).get('fixed_batch_size','')

        h+='   <td '+ha+'><a href="'+url0+'&wcid='+kscenario+'">'+xx+'</a></td>\n'

        # Versions
        if not min_view:
           ver=''
           dver=meta.get('engine_meta',{}).get(cpu_abi,{})
           ver+='main: '+str(dver.get('program_version',''))+'\n'
           dps=dver.get('deps_versions',{})
           for dx in dps:
               ver+=dx+': '+str(dps[dx].get('version',''))+'\n'

           ver=ver.replace("\'","'").replace("'","\\'").replace('\"','"').replace('"',"\\'").replace('\n','\\n')
           if ver!='':
               ver='<input type="button" class="ck_small_button" onClick="alert(\''+ver+'\');" value="View">'
           h+='   <td '+ha+'>'+ver+'</td>\n'

        # Model weight size
        h+='   <td '+ha+'>'+str(model_weights_size)+' MB</td>\n'

        # Check relative time
        xx='<b>'+('%.3f'%tmin)+'</b>&nbsp;/&nbsp;'+('%.3f'%tmax)

        if tmin==0: xx+='<br><b><center>bug?</center></b>\n'
#        TBD: need to check how time is normalized ...
#        elif fbsize!='':
#           xx+='<br><br><i>batch size='+str(fbsize)+'</i>'

        if (hi_uid!='' and buid==hi_uid) or (hi_user!='' and hi_user==user):
            bgraph['0'].append([ix,None])
            bgraph['1'].append([ix,tmin])
        else:
            bgraph['0'].append([ix,tmin])
            if hi_uid!='' or hi_user!='': 
               bgraph['1'].append([ix,None])

        x=bgx9 if v9a=='latency' else bgx1

        h+='   <td '+ha+' '+x+'>'+xx+'</a></td>\n'

        # Finer grain timing
        ttmin=tmin
        ttdelta=tmax-tmin

        if not min_view:
           for ixo in range(0,3):
              tmin=extra.get('xopenme_execution_time_kernel_'+str(ixo)+'_min',0)
              tmax=extra.get('xopenme_execution_time_kernel_'+str(ixo)+'_max',0)

              if tmin<0: tmin=0 # detected bug

              xx='<b>'+('%.3f'%tmin)+'</b>&nbsp;/&nbsp;'+('%.3f'%tmax)
              if tmin==0 and ixo!=1: 
                 xx+='<br><b><center>possible bug detected - check further</center></b>\n'

              x=bgx9 if (v9a=='throughput' and ixo==2) else bgx1

              if v9b.startswith('throughput') and ixo==2:
                 ttmin=tmin
                 ttdelta=tmax-tmin

              h+='   <td '+ha+' '+x+'>'+xx+'</a></td>\n'

           # Accuracy
           x=pred
           j=x.find('-')
           if j>0:
               x=x[:j-1].strip()
           h+='   <td '+ha+' '+bgx2+'>'+x+'</a></td>\n'

        # Get info about platform
        hd={}
        if plat_uid!='':
           rh=ck.access({'action':'load',
                        'module_uoa':cfg['module_deps']['platform'],
                        'data_uoa':plat_uid})
           if rh['return']==0:
              hd=rh['dict']

        # Energy TBD
        x='-'
        if len(hd)>0:
           power=hd.get('features',{}).get('power_consumption',{})
           if len(power)>0:
              pmin=power.get('min','')
              pmax=power.get('max','')

              x=str(pmin)+' / '+str(pmax)
        h+='   <td '+ha+'>'+x+'</a></td>\n'

        # Memory usage TBD
        h+='   <td '+ha+'>-</a></td>\n'

        # Accuracy (take from model info)
        acc=xd.get('features',{}).get('accuracy','')
        acc5=xd.get('features',{}).get('accuracy_top5','')

        x=str(acc)
        if acc5!='':
           x+=' / '+str(acc5)

        if x=='': x='-'

        h+='   <td '+ha+'>'+x+'</a></td>\n'

        # Will be used to optimize model topology and parameters
        x='default'

        xfiles=xd.get('files',[])
        for xf in xfiles:
            if xf.get('filename','')=='deploy.prototxt':
               xx1=xf.get('from_data_uoa','')
               if xx1=='':
                  xx1=scenario
               xx2=xf.get('path','')

               x='<a href="'+url0+'&action=pull&common_action=yes&cid='+cfg['module_deps']['experiment.scenario.mobile']+':'+xx1+'&filename='+xx2+'/deploy.prototxt'+'">deploy.prototxt</a>\n'

               break

        h+='   <td '+ha+'>'+x+'</a></td>\n'

        # Cost (take from platform meta)
        hc='-'
        last_cost=0
        if len(hd)>0:
           costs=hd.get('features',{}).get('cost',[])
           hc=''
           if len(costs)>0:
              last_cost=int(costs[0].get('price','0'))
              for c in costs:
                  if hc!='': hc+='<br>\n'
                  hc+='<b>'+str(c.get('price',''))+' '+c.get('currency','')+ '</b> - '+c.get('desc','')+' ('+c.get('date','')+')'

        h+='   <td '+ha+'>'+hc+'</a></td>\n'

        # TBD: all other costs
        h+='   <td '+ha+'></a></td>\n'

        # Mispredictions and unexpected behavior
        if not min_view:
           x=''
           for q in mp:
               ca=q.get('correct_answer','')
               mi=q.get('mispredicted_image','')
               mr=q.get('misprediction_results','')

               if mr!='':
                   j1=mr.find('\n')
                   if j1>0:
                       j2=mr.find('\n',j1+1)
                       if j2>0:
                           mr=mr[j1:j2]

               xx=ca
               if mi!='':
                   y=work['self_module_uid']
                   if cmuoa!='': y=cmuoa
                   url=url0+'action=pull&common_action=yes&cid='+y+':'+duid+'&filename='+mi

                   if ca=='': ca='<i>unknown</i>'
                   xx='<a href="'+url+'">'+ca+'</a>'

               if x!='':
                   x+='<hr>\n'

               x+='<strike>'+mr+'</strike><br>'+xx+'<br>\n'

           if tmin==0: x+='<br><b><center>Bug detected</center></b>\n'

           h+='   <td '+ha+'>'+x+'</td>\n'

           # All images
           h+='   <td '+ha+'>'+key.replace(' ','&nbsp;')+'</a></td>\n'

        # Extra info about platform
        x=cpu_name
        if cpu_uid!='':
            x='<a href="'+url0+'&wcid='+cfg['module_deps']['platform.cpu']+':'+cpu_uid+'">'+x+'</a>'
        h+='   <td '+ha+'>'+x+'</td>\n'

        # CPU ABI
        if not min_view:
           h+='   <td '+ha+'>'+cpu_abi+'</td>\n'

        x=gpu_name
        if gpu_uid!='':
            x='<a href="'+url0+'&wcid='+cfg['module_deps']['platform.gpu']+':'+gpu_uid+'">'+x+'</a>'
        h+='   <td '+ha+'>'+x+'</td>\n'

        x=os_name
        if os_uid!='':
            x='<a href="'+url0+'&wcid='+cfg['module_deps']['platform']+':'+os_uid+'">'+x+'</a>'
        h+='   <td '+ha+'>'+x+'</td>\n'

        # Data
        x=work['self_module_uid']
        if cmuoa!='': x=cmuoa
        raw_data_url=url0+'wcid='+x+':'+duid
        h+='   <td '+ha+'><a href="'+raw_data_url+'">'+duid+' '+buid+'</a></td>\n'

        # User
        if not min_view:
           h+='   <td '+ha+'><a href="'+url0+'&action=index&module_uoa=wfe&native_action=show&native_module_uoa=experiment.user">'+user+'</a></td>\n'

           h+='  <tr>\n'

        tdelta=tmax-tmin # show best specie!
#        if tdelta>0.1: tdelta=0.1 # to avoid messy graph - just show that there is an issue with variation ...

        if tmin>0: # to skip bugs
           # check accuracy
           xcol='#0000bf'
           size5=2
           if acc5!='' and acc5>0:
              top5=(float(acc5)-0.8)*1000+50
              size5=(float(acc5)-0.75)*40+2
              col=hex(int(top5))[2:]
              xcol='#'+col+col+'ff'

           # mem usage
##           xx=(int(model_weights_size/20))*5.35+127
#           x=hex(int((xx)))[2:]
#           if len(x)<2: x='0'+x
#           mcol='#0000'+x

           divide=80
           if i.get(ckey+'engine')=='TFLite CPU':
              divide=3
           sizem=int(1+(model_weights_size/divide))+3

           bgraph2['0'].append([model_weights_size,tmin,tmin+tdelta])
           igraph2['0'].append({'size':3,'color':xcol})

           features={}

           X=0
           Y=0
           YD=0
           YS=0
           to_add=False

           if v9b=='time_cost':
              if last_cost>0:
                 to_add=True

                 if debug:
                    sizem=int(1+(model_weights_size/80))*6

                 X=last_cost
                 Y=tmin
                 YD=tdelta
                 YS=sizem
           else:
              if acc>0 and ttmin>0:
                 to_add=True

                 if debug:
                    sizem=int(1+(model_weights_size/80))*6

                 X=ttmin
                 if v9b.endswith('top1'):
                    Y=acc
                 else:
                    Y=acc5
                 YD=ttdelta
                 YS=sizem

                 if Y=='': 
                    Y=0
                    YD=0

           if to_add:
              # FGG: must improve to make a constant threshold afterwards (after knowing Ymin and Ymax)
              if (type(Y)==float or type(Y)==int) and Y>0 and YD>0 and YD>float(Y)*0.05: YD=float(Y)*0.05

              bgraph3['0'].append([X,Y,Y+YD])
#              igraph3['0'].append({'size':YS, 'color':xcol, 'features':meta, 'url':'', 'url_ext':raw_data_url})
              igraph3['0'].append({'size':YS, 'color':xcol, 'features':meta, 'anchor':buid})

              # For frontier
#              rx=ck.gen_uid({})
#              if rx['return']>0: return rx
#              puid=rx['data_uid']

#              f_bgraph3[puid]={"X":X, "Y":Y}
#              f_igraph3[puid]={'size':YS, 'tdelta':YD, 'features':meta, 'url':'', 'url_ext':raw_data_url}


    h+='</table>\n'
    h+='</center>\n'

    if debug: h+='\n<p>Debug time (preparing html of a table): '+str(time.time()-dt)+' sec.<p>\n'

    if cmuoa=='':
        h+='</form>\n'

    # 1st graph
    if len(bgraph['0'])>0:
       dt=time.time()
       ii={'action':'plot',
           'module_uoa':cfg['module_deps']['graph'],

           "table":bgraph,

           "ymin":0,

           "ignore_point_if_none":"yes",

           "plot_type":"d3_2d_bars",

           "display_y_error_bar":"no",

           "title":"Powered by Collective Knowledge",

           "x_ticks_period":50,

           "axis_x_desc":"Experiment",
           "axis_y_desc":"DNN image classification time (s)",

           "plot_grid":"yes",

           "d3_div":"ck_interactive",

           "image_width":"900",
           "image_height":"400",

           "wfe_url":url0}

#       r=ck.access(ii)
#       if r['return']==0:
#          x=r.get('html','')
#          if x!='':
#             st+=r.get('style','')
#
#             h+='<br>\n'
#             h+='<center>\n'
#             h+='<div id="ck_box_with_shadow" style="width:920px;">\n'
#             h+=' <div id="ck_interactive" style="text-align:center">\n'
#             h+=x+'\n'
#             h+=' </div>\n'
#             h+='</div>\n'
#             h+='</center>\n'

    # 2nd graph
    if len(bgraph2['0'])>0:
       ii={'action':'plot',
           'module_uoa':cfg['module_deps']['graph'],

           "table":bgraph2,
           "table_info":igraph2,

           "xmin":-10,
           "ymin":0,

           "ignore_point_if_none":"yes",

           "plot_type":"d3_2d_scatter",

           "display_y_error_bar2":"no",

           "title":"Powered by Collective Knowledge",

           "x_ticks_period":50,

#           "axis_x_desc":"Weigths size (MB)",
#           "axis_y_desc":"DNN image classification time (s)",

           "plot_grid":"yes",

           "d3_div":"ck_interactive2",

           "image_width":"900",
           "image_height":"400",

           "wfe_url":url0}

#       r=ck.access(ii)
#       if r['return']==0:
#          x=r.get('html','')
#          if x!='':
#             st+=r.get('style','')
#
#             h+='<br>\n'
#             h+='<center>\n'
#             h+='<div id="ck_box_with_shadow" style="width:920px;">\n'
#             h+='\n'
#             h+=' <div id="ck_interactive2" style="text-align:center">\n'
#             h+=x+'\n'
#             h+=' </div>\n'
#             h+='</div>\n'
#             h+='</center>\n'

    # 3nd graph
    graph_html=''
    graph_style=''

    if len(bgraph3['0'])>0:
       # Fontier
       r=ck.access({'action':'filter',
                    'module_uoa':cfg['module_deps']['math.frontier'],
                    'points':f_bgraph3})
       if r['return']>0: return r

       points=r['points']

       bgraph3['1']=[]
       igraph3['1']=[]

       if v9b=='time_cost':
          xdesc='Device price, $'
          ydesc='image classification time, sec.'
       elif v9b=='throughput_top1' or v9b=='':
          xdesc='throughput (image classification), sec.'
          ydesc='Top1 accuracy'
       elif v9b=='throughput_top5':
          xdesc='throughput (image classification), sec.'
          ydesc='Top5 accuracy'
       elif v9b=='latency_top1':
          xdesc='latency (image classification), sec.'
          ydesc='Top1 accuracy'
       elif v9b=='latency_top5':
          xdesc='latency (image classification), sec.'
          ydesc='Top5 accuracy'

       for q in points:
           q1=f_bgraph3[q]
           q2=f_igraph3[q]

           bgraph3['1'].append([q1['X'],q1['Y'],q1['Y']+q2['tdelta']])
           del(q2['tdelta'])
           igraph3['1'].append(q2)

       ii={'action':'plot',
           'module_uoa':cfg['module_deps']['graph'],

           "table":bgraph3,
           "table_info":igraph3,

           "ignore_point_if_none":"yes",

           "plot_type":"d3_2d_scatter",
           "display_y_error_bar2":"yes",

           "title":"Powered by Collective Knowledge",

           "x_ticks_period":50,

           "axis_x_desc":xdesc,
           "axis_y_desc":ydesc,

            "xmin":-0.01,
            "ymin":0,
#           "ymax":25,

           "point_style":{"1":{"color":"#dc3912", "connect_lines":"no"}},

           "plot_grid":"no",

           "d3_div":"ck_interactive3",

           "image_width":"900",
           "image_height":"400",

           "wfe_url":url0}

       # Temporal hack
       if debug: 
          ii['out_to_file']='/tmp/dnn-co-design.pdf'
          ii['customize_dots']='yes'
          ii['plot_type']='mpl_2d_scatter'

       r=ck.access(ii)
       if r['return']==0:
          graph_html=r.get('html','')
          if graph_html!='':
             graph_style=r.get('style','')
             st+=graph_style

             hhh+='<center>\n'
             hhh+='<div id="ck_box_with_shadow" style="width:920px;">\n'
             hhh+=' <div id="ck_interactive3" style="text-align:center">\n'
#             hhh+='Device cost (X axis, &euro;) vs image classification time (Y axis, s.) vs model size (dot size) vs model TOP5 ImageNet accuracy (darker colors for lower accuracy).\n'
             hhh+='Dot size ~ model size ; dot color ~ model TOP5 ImageNet accuracy (darker colors for lower accuracy).\n'
#             hhh+='<b><span style="color:#9f0000">Red dots - surviving species for a given realistic AI scenario</span></b>.<br>\n'
             hhh+=graph_html+'\n'
             hhh+=' </div>\n'
             hhh+='</div>\n'
             hhh+='</center>\n'
             hhh+='<br>\n'

       # Extra vision slide
       hhh+='<p>\n<center><a href="https://www.slideshare.net/GrigoriFursin/adapting-to-a-cambrian-aiswhw-explosion-with-open-codesign-competitions-and-collective-knowledge"><img src="http://cknowledge.org/_resources/b4b07ad3a7839327-cropped.png" width="600"></a></center><p>\n'

       if debug: hhh+='\n<p>Debug time (preparing graph): '+str(time.time()-dt)+' sec.<p>\n'

    # Adding table
    hhh+=h

    rr={'return':0, 'style':st}

    if minimal:
       rr['graph_html']=graph_html
       rr['style']=graph_style
       rr['table']=bgraph3
       rr['table_info']=igraph3
    else:
       rr['html']=hhh

    return rr

##############################################################################
# process raw results from mobile devices

def process(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import copy

#    Debug
#    ck.save_json_to_file({'json_file':'/tmp/xyz1.json','dict':i})

    crowd_uid=i.get('crowd_uid','')
    email=i.get('email','')
    raw_results=i.get('raw_results',{})

    cfb=i.get('cpu_freqs_before',{})
    cfa=i.get('cpu_freqs_after',{})

    features=i.get('platform_features',{})

    fplat=features.get('platform',{})
    fos=features.get('os',{})
    fcpu=features.get('cpu',{})
    fgpu=features.get('gpu',{})

    plat_name=fplat.get('name','')
    plat_uid=features.get('platform_uid','')
    os_name=fos.get('name','')
    os_uid=features.get('os_uid','')
    gpu_uid=features.get('gpu_uid','')
    cpu_name=fcpu.get('name','')
    cpu_abi=fcpu.get('cpu_abi','')
    if cpu_name=='' and cpu_abi!='': 
        cpu_name='unknown-'+fcpu.get('cpu_abi','')
    cpu_uid=features.get('cpu_uid','')
    gpu_name=fgpu.get('name','')
    gpgpu_name=''
    gpgpu_uid=''
    sn=fos.get('serial_number','')

    # Prepare high-level experiment meta
    meta={'cpu_name':cpu_name,
          'cpu_abi':cpu_abi,
          'os_name':os_name,
          'plat_name':plat_name,
          'gpu_name':gpu_name,
          'gpgpu_name':gpgpu_name,
          'crowd_uid':crowd_uid}

    # Load scenario and update meta
    r=ck.access({'action':'load',
                 'module_uoa':cfg['module_deps']['experiment.scenario.mobile'],
                 'data_uoa':crowd_uid})
    if r['return']>0: return r
    xd=r['dict']

    meta['engine']=xd.get('engine','')
    meta['model']=xd.get('model','')

    mmeta=copy.deepcopy(meta)

    # Extra meta which is not used to search similar case ...
    mmeta['platform_uid']=plat_uid
    mmeta['os_uid']=os_uid
    mmeta['cpu_uid']=cpu_uid
    mmeta['gpu_uid']=gpu_uid
    mmeta['gpgpu_uid']=gpgpu_uid

    # Generate behavior UID
    rx=ck.gen_uid({})
    if rx['return']>0: return rx
    buid=rx['data_uid']

    raw_results['user']=email
    raw_results['behavior_uid']=buid

    # Check if already exists
    duid=''
    ddd={}

    ii={'action':'search',
        'module_uoa':work['self_module_uid'],
        'repo_uoa':ck.cfg.get('record_local_repo_uoa',''),
        'search_dict':{'meta':meta},
        'add_meta':'yes'}
    rx=ck.access(ii)
    if rx['return']>0: return rx

    lst=rx['lst']

    if len(lst)==1:
        duid=lst[0]['data_uid']
        ddd=lst[0]['meta']
    else:
        rx=ck.gen_uid({})
        if rx['return']>0: return rx
        duid=rx['data_uid']

    # We keep time1,2,3 just for compatibility with the first beta version
    t=raw_results.get('time',[])
    tx=raw_results.get('time1',None)
    if tx!=None: t.append(tx)
    tx=raw_results.get('time2',None)
    if tx!=None: t.append(tx)
    tx=raw_results.get('time3',None)
    if tx!=None: t.append(tx)
    raw_results['time']=t

    # Check XOpenME
    xopenme={}

    yopenme=raw_results.get('xopenme',[])
    for xx in yopenme:
        for k in xx:
            v=xx[k]
            if k not in xopenme:
               xopenme[k]=[]
            if v!=None:
               xopenme[k].append(v)

    raw_results['xopenme']=xopenme

    # Record freq (not checking if changed at this stage)
    raw_results['cpu_freqs_before']=[cfb]
    raw_results['cpu_freqs_after']=[cfa]

    # Process freq before and freq after (for now no any intelligence)
    fb=raw_results

    # Process results
    results=ddd.get('all_raw_results',[])

    # Check if already exists with this image topology
    found=False
    for q in results:
        if (q.get('image_height',None)==raw_results.get('image_height',None) and \
           q.get('image_width',None)==raw_results.get('image_width',None)) or \
           (q.get('image_height',None)==raw_results.get('image_width',None) and \
           q.get('image_width',None)==raw_results.get('image_height',None)):
            t=q.get('time',[])

            for tx in raw_results.get('time',[]):
                t.append(tx)
            q['time']=t

            tkk1=raw_results.get('xopenme',{})
            tkk2=q.get('xopenme',{})

            for tk in tkk1:
                if tk not in tkk2: tkk2[tk]=[]
                for tx in tkk1[tk]:
                    if tx!=None: 
                       tkk2[tk].append(tx)

            q['xopenme']=tkk2

            fb=q.get('cpu_freqs_before',[])
            fb.append(cfb)
            q['cpu_freqs_before']=fb

            fa=q.get('cpu_freqs_after',[])
            fa.append(cfa)
            q['cpu_freqs_before']=fa

            buid=q.get('behavior_uid','')

            found=True

            break

    if not found:
        results.append(raw_results)

    ddd['all_raw_results']=results

    xmeta=ddd.get('meta',{})
    xmeta.update(mmeta)
    ddd['meta']=xmeta

    # Update meta
    rx=ck.access({'action':'update',
                  'module_uoa':work['self_module_uid'],
                  'data_uoa':duid,
                  'repo_uoa':ck.cfg.get('record_local_repo_uoa',''),
                  'dict':ddd,
                  'substitute':'yes',
                  'sort_keys':'yes'})
    if rx['return']>0: return rx

    # Prepare url with results
    rx=ck.access({'action':'form_url_prefix',
                  'module_uoa':'wfe'})
    if rx['return']>0: return rx

    url=rx['url']+'&action=index&module_uoa=wfe&native_action=show&native_module_uoa=program.optimization&scenario='+work['self_module_uid']+'&highlight_behavior_uid='+buid

    return {'return':0, 'status':'Results successfully added to Collective Knowledge (UID='+duid+')!', 'data_uid':duid, 'behavior_uid':buid, 'result_url':url}

##############################################################################
# record unexpected behavior

def process_unexpected_behavior(i):
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

    duid=i.get('data_uid','')
    buid=i.get('behavior_uid','')
    cuid=i.get('crowd_uid','')
    rres=i.get('raw_results','')
    ca=i.get('correct_answer','')
    file_base64=i.get('file_base64','')

    # Find data
    r=ck.access({'action':'load',
                 'module_uoa':work['self_module_uid'],
                 'data_uoa':duid})
    if r['return']>0: return r
    d=r['dict']
    p=r['path']

    # Find behavior
    found=False
    arr=d.get('all_raw_results',[])
    for q in arr:
        if q.get('behavior_uid','')==buid:
            found=True
            break

    if not found:
        return {'return':1, 'error':'can\'t find behavior '+buid+' in entry '+duid}

    # Generate UID for the file with unexpected behavior
    rx=ck.gen_uid({})
    if rx['return']>0: return rx

    ff='misprediction-image-'+rx['data_uid']+'.jpg'

    pf=os.path.join(p,ff)

    mp=q.get('mispredictions',[])

    qq={}
    qq['misprediction_results']=rres
    qq['mispredicted_image']=ff
    qq['correct_answer']=ca

    mp.append(qq)

    q['mispredictions']=mp

    # Record file
    rx=ck.convert_upload_string_to_file({'file_content_base64':file_base64,
                                         'filename':pf})
    if rx['return']>0: return rx

    # Update entry (should add lock in the future for parallel processing)
    r=ck.access({'action':'update',
                 'module_uoa':work['self_module_uid'],
                 'data_uoa':duid,
                 'dict':d,
                 'sort_keys':'yes',
                 'substitute':'yes',
                 'ignore_update':'yes'})
    if r['return']>0: return r

    return {'return':0}

##############################################################################
# generate scenario to crowdsource benchmarking/optimization of DNN engines/models on Android devices

def generate(i):
    """
    Input:  {
              (prune_target_os) - prune generated scenarios by this target OS (ABI)
              (prune_engine)    - prune generated scenarios by this engine
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os
    import copy
    import shutil
    import itertools

    o=i.get('out','')

    p_tos=i.get('prune_target_os','')
    p_engine=i.get('prune_engine','')

    # Get platform params
    ck.out('Detecting host platform info ...')
    ck.out('')

    i['action']='detect'
    i['module_uoa']=cfg['module_deps']['platform']
    i['out']=''
    rpp=ck.access(i)
    if rpp['return']>0: return rpp

    hos=rpp['host_os_uoa']
    hosd=rpp['host_os_dict']

    # Search all scenarios
    r=ck.access({'action':'search',
                 'module_uoa':cfg['module_deps']['experiment.scenario.mobile'],
                 'add_meta':'yes'})
    if r['return']>0: return r

    lst=r['lst']
    if len(lst)==0:
       return {'return':1, 'error':'no pre-recorded crowd-scenarios found ...'}

    uids={}
    found=False

    engine_meta={}

    engine_state='' # If engine changes, clean up found uids ...

    # Go through required engines (CPU,OpenCL) and ABIs, and compile classification with related libs ...
    for prog,b in list(itertools.product(cfg['prog_uoa'],abis)):

        abi=b['abi']
        os_uoa=b['os_uoa']
        if i.get('target_os','')!='': os_uoa=i['target_os']

        engine=prog['engine']
        prog_uoa=prog['program_uoa']
        engine_key=prog['engine-deps-key']
        engine_lib=prog.get('engine-lib','')

        # Check if should prune
        if p_tos!='' and p_tos!=os_uoa:
           continue

        if p_engine!='' and p_engine!=engine:
           continue

        if engine!=engine_state:
           uids={}
           found=False
           engine_state=engine

        ck.out(line)
        ck.out('Preparing "'+engine+'" engine with "'+abi+'" ABI for crowd-benchmarking and crowd-tuning ...')

        ck.out('')
        r=ck.inp({'text':'Press Enter to generate this scenario or N to skip this scenario: '})
        s=r['string']

        if s!='':
           continue

        # Compile classification (should compile all deps)
        ck.out('')
        ck.out('Compiling classification (and libs) ...')

        ii={'action':'compile',
            'module_uoa':cfg['module_deps']['program'],
            'data_uoa':prog_uoa,
            'host_os':hos,
            'target_os':os_uoa,
            'speed':'yes',
            'out':o}
        r=ck.access(ii)
        if r['return']>0: return r

        # Get various info
        cc=r.get('characteristics',{})

        cs=cc.get('compilation_success','')
        if cs!='yes':
           return {'return':1, 'error':'compilation failed'}

        md5=cc.get('md5_sum','')
        bs=cc.get('binary_size',0)

        misc=r.get('misc',{})

        pf=misc.get('path','')
        td=misc.get('tmp_dir','')
        of=misc.get('target_exe','')
        pv=misc.get('program_version','')

        pp=os.path.join(pf,td,of)
        if not os.path.isfile(pp):
           return {'return':1, 'error':'target binary not found ('+pp+')'}

        # Get info about deps
        deps=r.get('deps',{})

        # Get info about lib if needed
        cdeps=deps.get(engine_key,{})

        cfp=''
        lmd5=''
        ls=0

        if engine_lib!='':
           # Force .so (sometimes points to .a)
           cfp=cdeps.get('cus',{}).get('full_path','')
           cfp=os.path.join(os.path.dirname(cfp),engine_lib)

           if os.path.isfile(cfp):
              r=ck.run_and_get_stdout({'cmd':hosd['md5sum']+' '+cfp, 
                                    'shell':'no'})
              if r['return']>0: return r
              sto=r['stdout'].split(' ')

              if len(sto)==0:
                 return {'return':1, 'error':'can\'t get MD5 of '+engine_lib}

              lmd5=sto[0] # MD5 of caffe lib

              ls=os.path.getsize(cfp)

        # xopenme
        odeps=deps.get('xopenme',{})

        ofp=odeps.get('cus',{}).get('full_path','')

        # Force .so (sometimes points to .a)
        ofp=os.path.join(os.path.dirname(ofp),libxopenme)

        if not os.path.isfile(ofp):
           return {'return':1, 'error':'xopenme plugin not found ('+ofp+')'}

        r=ck.run_and_get_stdout({'cmd':hosd['md5sum']+' '+ofp, 
                                 'shell':'no'})
        if r['return']>0: return r
        sto=r['stdout'].split(' ')

        if len(sto)==0:
           return {'return':1, 'error':'can\'t get MD5 of librtlxopenme.so'}

        omd5=sto[0] # MD5 of caffe lib

        ops=os.path.getsize(ofp)

        # Get versions of all deps
        dv={}
        for x in deps:
            dv[x]={}
            cx=deps[x].get('cus',{})

            dv[x]['version']=cx.get('version','')
            dv[x]['revision']=cx.get('git_info',{}).get('revision','')
            dv[x]['iso_datetime_cut_revision']=cx.get('git_info',{}).get('iso_datetime_cut_revision','')
            dv[x]['tags']=deps[x].get('tags',[])

        # Prepare info pack about this experiment
        meta={'classification_version':pv,
              'deps':dv,
              'host_os':hos,
              'target_os':os_uoa}

        # Search caffe original code with a given ABI
        ck.out('')
        ck.out('Checking / updating scenario files ...')

        changed_files=[] # Which libs were substituted

        for q in lst:
           duid=q['data_uid']
           duoa=q['data_uoa']
           ruoa=q['repo_uid']

           d=q['meta']

           if d.get('outdated','')=='yes': # skip archived entries
              continue

           if d.get('engine','')!=engine:
              continue

           pe=q['path'] # Path to entry

           files=d.get('files',[])

           # Process main binary files (in code directory)
           for ff in files:
               fduoa=ff.get('from_data_uoa','')
               if fduoa=='':
                  sabi=ff.get('supported_abi',[])
                  if abi in sabi:
                     fn=ff.get('filename','')
                     p=ff.get('path','')

                     xfs=ff.get('file_size',0)
                     xmd5=ff.get('md5','')

                     pep=os.path.join(pe,p,fn)

                     if (fn==engine_lib and (not os.path.isfile(pep) or (xmd5!=lmd5 and xfs!=ls))) or \
                        (fn=='classification' and (not os.path.isfile(pep) or (xmd5!=md5 and xfs!=bs))) or \
                        (fn==libxopenme and (not os.path.isfile(pep) or (xmd5!=omd5 and xfs!=ops))):

                        if not found:
                           # If first time, tell that old scenario will be removed!
                           ck.out('')
                           ck.out('WARNING: we found OUTDATED binaries for this scenario')
                           ck.out('         and plan to remove them - make sure that you archived them!')

                           ck.out('')
                           r=ck.inp({'text':'Would you like to proceed and remove outdated binaries (Y/n): '})
                           if r['return']>0: return r

                           s=r['string'].strip().lower()

                           if s!='':
                              return {'return':0}

                           found=True

                        ck.out('')
                        ck.out('Updating '+fn+' in '+duoa+' ('+p+')')

                        oduid=p.split('/')[1]

                        nduid=uids.get(oduid,'')

                        # Generate new UID
                        if nduid=='':
                           r=ck.gen_uid({})
                           if r['return']>0: return r
                           nduid=r['data_uid']

                           uids[oduid]=nduid

                           ck.out('  * New code UID for '+oduid+' : '+nduid)
                        else:
                           ck.out('  * Reusing UID for '+oduid+' : '+nduid)

                        np=os.path.join(pe,'code',nduid,abi)
                        ck.out('  * New path: '+np)

                        # Create new dir and copy file
                        if not os.path.isdir(np):
                           os.makedirs(np)

                        fnp=os.path.join(np,fn)

                        if fn==engine_lib:
                           shutil.copy(cfp, fnp)
                        elif fn=='classification':
                           shutil.copy(pp, fnp)
                        else:
                           shutil.copy(ofp, fnp)

                        # Remove old path
                        px=os.path.join(pe,p)
                        if os.path.isdir(px):
                           ck.out('  * Removing dir: '+px)
                           shutil.rmtree(px)

                        # If whole directory is empty, remove it too
                        px=os.path.join(pe,'code',oduid)
                        if os.path.isdir(px) and len(os.listdir(px))==0:
                           ck.out('  * Removing dir: '+px)
                           shutil.rmtree(px)

                        # Changing meta
                        zp=np
                        if not zp.startswith('code') and not zp.startswith('data'):
                           j1=zp.find('code/')
                           if j1<0:
                              j1=zp.find('data/')
                           if j1>0:
                              zp=zp[j1:]

                        changed_before={'filename':fn,
                                        'from_data_uoa':duid,
                                        'path':p,
                                        'file_size':xfs,
                                        'md5':xmd5}

                        changed_after={'filename':fn,
                                       'from_data_uoa':duid,
                                       'path':zp}

                        if fn==engine_lib:
                           changed_after['file_size']=ls
                           changed_after['md5']=lmd5
                        elif fn=='classification':
                           changed_after['file_size']=bs
                           changed_after['md5']=md5
                        else:
                           changed_after['file_size']=ops
                           changed_after['md5']=omd5

                        ff.update(changed_after)
                        del(ff['from_data_uoa'])

                        # Updating global meta of engine
                        engine_meta[abi]={'program_version':pv, 'deps_versions':dv}

                        d['engine_meta']=engine_meta

                        # Add to changed
                        changed_files.append({'before':changed_before,
                                              'after':changed_after})

                     else:
                        ck.out('')
                        ck.out('*** Scenario binary '+fn+' is up to date! ***')

        # If changed original files, change them in all other meta
        if len(changed_files)>0:

           ck.out('')
           ck.out('Updating all scenarios with new files ...')
           ck.out('')

           for q in lst:
               duid=q['data_uid']
               duoa=q['data_uoa']
               muid=q['module_uid']
               ruoa=q['repo_uid']

               d=q['meta']

               if d.get('outdated','')=='yes': # skip archived entries
                  continue

               if d.get('engine','')!=engine:
                  continue

               ck.out('  * '+duoa)

               d['engine_meta']=engine_meta

               pp=q['path'] # Path to entry

               files=d.get('files',[])

               for ff in files:
                   fduoa=ff.get('from_data_uoa','')

                   if fduoa!='':
                      # Check if needs to be changed ...
                      for c in changed_files:
                          before=c['before']
                          after=c['after']

                          rx=ck.compare_dicts({'dict1':ff, 'dict2':before})
                          if rx['return']>0: return rx
                          if rx['equal']=='yes':
                             ff.update(after)

               # Update entry now (aggregating all above changes)
               r=ck.access({'action':'update',
                            'module_uoa':muid,
                            'data_uoa':duid,
                            'repo_uoa':ruoa,
                            'dict':d,
                            'substitute':'yes',
                            'ignore_update':'yes',
                            'sort_keys':'yes'})
               if r['return']>0: return r

    return {'return':0}
