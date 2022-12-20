#
# Collective Knowledge (Check speedup of program versus various compiler flags and data sets)
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
sep='**********************************************************************'

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
# describe experiment

def describe(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    ck.out(cfg['full_desc'])

    return {'return':0}

##############################################################################
# reproduce experiment

def reproduce(i):
    """
    Input:  {
              program_uoa       - program UOA to check

              (cmd_key)         - cmd key
              (dataset_uoas)    - check dataset UOA

              (choices)         - dict['flags'] - list of combinations of compiler flags

              (host_os)         - host OS (detect, if omitted)
              (target_os)       - OS module to check (if omitted, analyze host)
              (device_id)       - device id if remote (such as adb)

              (stat_repeat)     - max statistical repetitions (4 by default)

              (check_speedup)   - if 'yes', check speedups for the first two optimizations ...

              (add_to_pipeline) - add this dict to pipeline 

              (force_record)    - if 'yes', force record even if behavior expected ...

              (experiment_repo_uoa)        - repo to record experiments (by default "remote-ck")
              (experiment_remote_repo_uoa) - if above repo is remote, repo on remote server to record experiments (by default "upload")
              (experiment_uoa)             - CK entry UOA to record experiments (by default "reproduce-ck-paper-filter-optimization")
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os
    curdir=os.getcwd()
    rf=os.path.join(curdir, cfg['report_file'])

    puoa=i.get('program_uoa','')
    if puoa=='':
       return {'return':1, 'error':'program_uoa is not defined.\n\nUse "ck list program" to see available programs.\nUse "ck pull repo:ck-programs" and "ck pull repo:ck-datasets-min" to get a small set of our benchmarks and datasets.'}

    choices=i.get('choices',{})
    if len(choices)==0:
       choices=cfg['choices']

    cflags=choices.get('flags',[])
    if len(cflags)==0:
       return {'return':1, 'error':'choices dictionary doesn\'t have "flags" list'}

    ap=i.get('add_to_pipeline',{})

    e_repo_uoa=cfg['repository_to_share_results']
    e_remote_repo_uoa=cfg['remote_repo_uoa']
    e_uoa=cfg['remote_experiment_uoa']

    if i.get('experiment_repo_uoa','')!='': e_repo_uoa=i['experiment_repo_uoa']
    if i.get('experiment_remote_repo_uoa','')!='': e_remote_repo_uoa=i['experiment_remote_repo_uoa']
    if i.get('experiment_uoa','')!='': e_uoa=i['experiment_uoa']

    ###################################################
    # Experiment table
    table=[]  # Strings (for printing)
    otable=[] # Original format

    ###################################################
    ck.out(sep)
    ck.out('Loading program meta info ...')

    r=ck.access({'action':'load',
                 'module_uoa':cfg['module_deps']['program'],
                 'data_uoa':puoa})
    if r['return']>0: return r
    pd=r['dict']

    cmd_key=i.get('cmd_key','')
    if cmd_key=='': cmd_key='default'

    ###################################################
    ck.out(sep)
    ck.out('Checking available data sets ...')

    dsets=i.get('dataset_uoas',[])

    dtags=pd.get('run_cmds',{}).get(cmd_key,{}).get('dataset_tags','')

    ii={'action':'search',
        'module_uoa':cfg['module_deps']['dataset']}
    if len(dsets)>0:
       ii['data_uoa_list']=dsets
    else:
       ii['tags']=dtags
    r=ck.access(ii)
    if r['return']>0: return r
    dlist=r['lst']

    # Prepare first and second line of table
    t=[]
    t.append('')
    t.append('')
    t.append('')
    for ds in dlist:
        t.append('Dataset '+ds['data_uoa']+':')
    table.append(t)

    t=[]
    t.append('Optimization:')
    t.append('Binary size:')
    t.append('MD5SUM:')
    for ds in dlist:
        t.append('min time (s); exp time (s); var (%):')
    table.append(t)

    # Number of statistical repetitions
    srepeat=int(i.get('stat_repeat',0))
    if srepeat<1: srepeat=4

    repeat=i.get('repeat',-1)

    hos=i.get('host_os','')
    tos=i.get('target_os','')
    tdid=i.get('device_id','')

    # will be updated later
    deps={}
    features={}
    xchoices={}

    dcomp=''

    for cf in cflags:
        ck.out(sep)
        ck.out('Checking flags "'+cf+'" ...')

        t=[]
        t.append(cf)

        ii={'action':'run',

            'module_uoa':cfg['module_deps']['pipeline'],
            'data_uoa':cfg['module_deps']['program'],

            'host_os':hos,
            'target_os':tos,
            'device_id':tdid,

            'repetitions': 1,

            'force_pipeline_update':'yes',

            'out':'con'}

        pipeline={'data_uoa':puoa,
                  'flags':cf,
                  'no_run':'yes'}

        if len(ap)>0: pipeline.update(ap)

        if len(deps)>0: pipeline['dependencies']=deps

        ii['pipeline']=pipeline

        r=ck.access(ii)
        if r['return']>0: return r

        lio=r.get('last_iteration_output',{})

        fail=lio.get('fail','')

        if fail=='yes':
           return {'return':1, 'error':'compilation failed ('+lio.get('fail_reason','')+')- check above output and possibly report to the authors!'}

        ed=r.get('experiment_desc',{})
        deps=ed.get('dependencies',{})

        cc=ed.get('choices',{})

        if len(xchoices)==0: xchoices=cc

        hos=cc['host_os']
        tos=cc['target_os']
        tdid=cc['device_id']

        ft=ed.get('features',{})
        if len(features)==0: features=ft

        if dcomp=='': dcomp=ft.get('compiler_version',{}).get('str','')

        lsa=r.get('last_stat_analysis',{})
        fresults=lsa.get('dict_flat',{})

        os=fresults.get('##characteristics#compile#binary_size#min',0)
        md5=fresults.get('##characteristics#compile#md5_sum#min','')

        t.append(os)
        t.append(md5)

        # Iterate over datasets
        oresults={}

        for ds in dlist:
            duoa=ds['data_uoa']
            duid=ds['data_uid']

            ck.out(sep)
            ck.out('Running with dataset '+duoa+' ...')
            ck.out('')

            ij={'action':'run',

                'module_uoa':cfg['module_deps']['pipeline'],
                'data_uoa':cfg['module_deps']['program'],
                'program_uoa':puoa,

                'host_os':hos,
                'target_os':tos,
                'device_id':tdid,

                'repetitions': srepeat,

                'force_pipeline_update':'yes',

                'out':'con'}

            pipeline={'data_uoa':puoa,
                      'cmd_key':cmd_key,
                      'dataset_uoa':duid,
                      'no_compile':'yes'}

            if len(ap)>0: pipeline.update(ap)

            if len(deps)>0: pipeline['dependencies']=deps

            if repeat>0: pipeline['repeat']=repeat

            ij['pipeline']=pipeline

            r=ck.access(ij)
            if r['return']>0: return r

            lio=r.get('last_iteration_output',{})

            fail=lio.get('fail','')

            if fail=='yes':
               return {'return':1, 'error':'execution failed ('+lio.get('fail_reason','')+')- check above output and possibly report to the authors!'}

            state=lio.get('state',{})
            repeat=state['repeat']

            lsa=r.get('last_stat_analysis',{})
            fresults=lsa.get('dict_flat',{})

            texp=fresults.get('##characteristics#run#execution_time_kernel_0#exp',0)
            tmin=fresults.get('##characteristics#run#execution_time_kernel_0#min',0)
            tdelta=fresults.get('##characteristics#run#execution_time_kernel_0#range_percent',0)

            oresults[duoa]=fresults

            t.append('      '+('%3.3f' % tmin) + ' ;       ' + ('%3.3f' % texp) + ' ;   ' + ('%4.1f' % (tdelta*100))+'%')

        otable.append(oresults)
        table.append(t)

    # Draw table
    ii={'action':'draw',
        'module_uoa':cfg['module_deps']['table'],
        'table':table,
        'out':'txt'}
    r=ck.access(ii)
    if r['return']>0: return r
    s=r['string']

    rft=rf+'.txt'
    rfh=rf+'.html'
    rfj=rf+'.json'

    ck.out(sep)
    ck.out('Raw results (exported to '+rf+'.txt, .html, .json):')

    if dcomp!='':
       ck.out('')
       ck.out('Detected compiler version: '+dcomp)

    ck.out('')
    ck.out(s)

    r=ck.save_text_file({'text_file':rft, 'string':s})
    if r['return']>0: return r

    ii['out']='html'
    r=ck.access(ii)
    if r['return']>0: return r
    html=r['string']

    r=ck.save_text_file({'text_file':rfh, 'string':html})
    if r['return']>0: return r

    # Checking if there is a speedup ...
    # Expect that otable[0] - -O3; otable[1] - -O3 -fno-if-conversion
    if i.get('check_speedup','')=='yes' and len(otable)>1:
       r0d0=otable[0][dlist[0]['data_uoa']]
       r0d1=otable[0][dlist[1]['data_uoa']]
       r1d0=otable[1][dlist[0]['data_uoa']]
       r1d1=otable[1][dlist[1]['data_uoa']]

#       t0d0=r0d0['##characteristics#run#execution_time_kernel_0#exp']/repeat
#       t0d1=r0d1['##characteristics#run#execution_time_kernel_0#exp']/repeat
#       t1d0=r1d0['##characteristics#run#execution_time_kernel_0#exp']/repeat
#       t1d1=r1d1['##characteristics#run#execution_time_kernel_0#exp']/repeat

       t0d0=r0d0['##characteristics#run#execution_time_kernel_0#min']/repeat
       t0d1=r0d1['##characteristics#run#execution_time_kernel_0#min']/repeat
       t1d0=r1d0['##characteristics#run#execution_time_kernel_0#min']/repeat
       t1d1=r1d1['##characteristics#run#execution_time_kernel_0#min']/repeat

       sd0=t0d0/t1d0
       sd1=t0d1/t1d1

       if sd0>1.08 or sd1>1.08 or sd0<0.92 or sd1<0.92 or i.get('force_record','')=='yes':
          ck.out(sep)
          ck.out('Found speedup or slow down for the first 2 optimizations:')
          ck.out('')
          ck.out('* Dataset 0 ('+dlist[0]['data_uoa']+') speedup (T_opt0/T_opt1) = '+('%2.2f' % sd0))
          ck.out('* Dataset 1 ('+dlist[1]['data_uoa']+') speedup (T_opt0/T_opt1) = '+('%2.2f' % sd1))

          ck.out('')
          r=ck.inp({'text':'Would you like to share this result with the community and author via public "remote-ck" web service (Y/n): '})
          x=r['string'].lower()
          if x=='' or x=='yes' or x=='y':
             xchoices['optimization_0']=cflags[0]
             xchoices['optimization_1']=cflags[1]

             xchoices['dataset_uoa_0']=dlist[0]['data_uoa']
             xchoices['dataset_uoa_1']=dlist[1]['data_uoa']

             xchoices['dataset_uid_0']=dlist[0]['data_uid']
             xchoices['dataset_uid_1']=dlist[1]['data_uid']

             xchoices['compiler_version']=dcomp

             ii={'action':'add',
                 'module_uoa':cfg['module_deps']['experiment'],

                 'repo_uoa':e_repo_uoa,
                 'experiment_repo_uoa':e_remote_repo_uoa,
                 'experiment_uoa':e_uoa,

                 'sort_keys':'yes',

                 'dict':{
                   'dict':{'subview_uoa':cfg['data_deps']['subview_uoa']},

                   'tags':['crowdsource experiments','ck-paper','filter','if-conversion','speedup'],

                   'features':features,
                   'choices':xchoices,
                   'characteristics': {
                      'speedup_0':sd0,
                      'speedup_1':sd1,
                      'execution_time_div_by_repeat_opt0_ds0':t0d0,
                      'execution_time_div_by_repeat_opt0_ds1':t0d1,
                      'execution_time_div_by_repeat_opt1_ds0':t1d0,
                      'execution_time_div_by_repeat_opt1_ds1':t1d1
                   }
                 }
                }

             r=ck.access(ii)
             if r['return']>0: return r

             ck.out('')
             ck.out('  Results shared successfully!')

             ck.out('')
             ck.out('  You can see all shared results at http://cknowledge.org/repo/web.php?wcid=bc0409fb61f0aa82:reproduce-ck-paper-filter-optimization')

       else:
          ck.out('')
          ck.out('Note: speedups/slowdowns were not detected on your platform!')

    ck.out('')
    ck.out('Thank you for participating in experiment crowdsourcing!')

    return {'return':0}
