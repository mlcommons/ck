#
# Collective Knowledge (pipeline)
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
sep1='---------------------------------------------------------------------------------------'

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
# setup pipeline

def setup(i):
    """
    Input:  {
              data_uoa     - pipeline module UOA (such as 'benchmark')
                or
              pipeline_uoa
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')

    puoa=i.get('data_uoa','')
    if puoa=='':
       puoa=i.get('pipeline_uoa','')
    if puoa=='':
       return {'return':1, 'error':'pipeline_uoa is not defined'}

    r={'return':0}

    setup_completed=False
    while not setup_completed:
       ii={'action':'pipeline',
           'module_uoa':puoa,
           'prepare':'yes',
           'out':o}
       r=ck.access(ii)
       if r['return']>0: return r

       ready=r.get('ready','')
       if ready=='yes':
          setup_completed=True

    return r

##############################################################################
# universal pipeline autotuning

def autotune(i):
    """
    Input:  {
               (data_uoa)             - pipeline module UOA

               (pipeline)             - prepared pipeline setup (already ready to run)
                     or 
               (pipeline_from_file)   - load prepared pipeline setup from file

               (pipeline_update)      - update pipeline with this dict (useful to update already prepared pipeline from file)

               (pipeline_flags)       - update pipeline directly from the CMD flags (will be parsed by CK)

               (iterations)           - limit number of iterations, otherwise infinite (default=10)
                                        if -1, infinite (or until all choices are explored)
               (start_from_iteration) - skip all iterations before this number
               (repetitions)          - statistical repetitions (default=4)

               (seed)                 - if !='', use as random seed (to reproduce experiments)

               Enforce exploration:
               (start)
               (stop)
               (step)
               (explore_type)         = random, parallel-random, loop, parallel-loop 
                                        Note: machine learning-based or customized autotuners 
                                        are now moved to external plugins 
                                        (see "custom_autotuner" vars below)

                    or
               (random)
               (parallel-random)
               (loop)
               (parallel-loop)

               (process_multi_keys)               - list of keys (starts with) to perform stat analysis on flat array,
                                                       by default ['##characteristics#*', '##features#*' '##choices#*'],
                                                       if empty, no stat analysis

               (record)                           - if 'yes', record results
               (record_uoa)                       - (data UOA or CID where module_uoa ignored!) explicitly record to this entry
               (record_repo)                      - (repo UOA) explicitly select this repo to record
               (record_experiment_repo)           - (repo UOA) explicitly select this repo to record
               (record_failed)                    - if 'yes', record even failed experiments
                                                    (for debugging, buildbots, detecting designed 
                                                     architecture failures, etc)
               (record_only_failed)               - if 'yes', record only failed experiments
                                                    (useful to crowdsource experiments when searching only 
                                                     for compiler/program/architecture bugs  
                                                     (for example fuzzing via random compiler flags))...
               (record_permanent)                 - if 'yes', mark recorded points as permanent (will not be deleted by Pareto filter)
               (record_ignore_update)             - (default=yes), if 'yes', skip recording date/author info for each update
               (tags)                             - record these tags to the entry description
               (subtags)                          - record these subtags to the point description

               (skip_record_pipeline)             - if 'yes', do not record pipeline (to avoid saving too much stuff during crowd-tuning)
               (skip_record_desc)                 - if 'yes', do not record desc (to avoid saving too much stuff during crowd-tuning)

               (record_params)                    - extra record parameters (to 'add experiment' function)

               (features_keys_to_process)         - list of keys for features (and choices) to process/search 
                                                         when recording experimental results (can be wildcards)
                                                         by default ['##features#*', '##choices#*', '##choices_order#*']

               (frontier_keys)                    - list of keys to leave only best points during multi-objective autotuning
                                                     (multi-objective optimization)

               (frontier_keys_reverse)            - list of values associated with above keys. If True, reverse sorting for a give key
                                                    (by default descending)

               (frontier_margins)                 - list of margins when comparing values, i.e. Vold/Vnew < this number (such as 1.10 instead of 1).
                                                    will be used if !=None  

               (frontier_features_keys_to_ignore) - list of keys to ignore from 'features_keys_to_process' 
                                                    when detecting subset of points to detect frontier
                                                    (usually removing optimization dimensions, such as compiler flags)

               (only_filter)                      - if 'yes', do not run pipeline, but run filters on data (for Pareto, for example)

               (skip_stat_analysis)               - if 'yes', just flatten array and add #min

               (stat_flat_dict)                   - pre-load flat dict from previous experiments to aggregate for stat analysis

               (features)                         - extra features
               (meta)                             - extra meta

               (record_dict)                      - extra dict when recording experiments (useful to set subview_uoa, for example)

               (state)                            - pre-load state preserved across iterations

               (save_to_file)                     - if !='', save output dictionary to this file

               (skip_done)                        - if 'yes', do not print 'done' at the end of autotuning

               (sleep)                            - set sleep before iterations ...

               (force_pipeline_update)            - if 'yes', re-check pipeline preparation - 
                                                    useful for replay not to ask for choices between statistical repetitions

               (ask_enter_after_each_iteration)   - if 'yes', ask to press Enter after each iteration

               (tmp_dir)                          - (default 'tmp') - if !='', use this tmp directory to clean, compile and run

               (flat_dict_for_improvements)       - add dict from previous experiment to compare improvements 

               (pause_if_fail)                    - if pipeline fails, ask to press Enter
                                                    (useful to analyze which flags fail during compiler flag autotuning)

               (pause)                            - if 'yes', pause after each iteration

               (aggregate_failed_cases)           - if pipeline fails, aggregate failed cases (to produce report 
                                                    during crowdtuning or automatic compiler bug detection)

               (solutions)                        - check solutions
               (ref_solution)                     - if 'yes', choose reference solution from above list
               (internal_ref)                     - if 'yes', try internal reference before checking solutions ...

               (prune)                            - prune solution (find minimal choices that give the same result)
               (reduce)                           - the same as above
               (reduce_bug)                       - reduce choices to localize bug (pipeline fail)
               (prune_ignore_choices)             - list of choices to ignore (such as base flag, for example)
               (prune_md5)                        - if 'yes', check if MD5 doesn't change
               (prune_invert)                     - if 'yes', prune all (switch off even unused - useful for collaborative machine learning)
               (prune_invert_add_iters)           - if 'yes', add extra needed iterations
               (prune_invert_do_not_remove_key)   - if 'yes', keep both on and off keys (to know exact solution)
               (prune_result_conditions)          - list of extra conditions to accept result (variation, performance/energy/code size constraints, etc)

               (print_keys_after_each_iteration)  - print values of keys from flat dict after each iteration (to monitor characteristics)

               (result_conditions)                - check results for condition
               (condition_objective)              - how to check results (#min,#max,#exp ...)

               (collect_all)                      - collect all experiments and record to 

               (custom_autotuner)                 - dictionary to customize autotuner (exploration, DSE, machine learning based tuning, etc)
               (custom_autotuner_vars)            - extra vars to customize autotuner (for example, set default vs. random)

               (preserve_deps_after_first_run)    - if 'yes', save deps after first run (useful for replay)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              last_iteration_output - output of last iteration
              last_stat_analysis    - flat dict with stat analysis
              experiment_desc       - dict with experiment description

              recorded_info         - {'points':{}, 
                                       'deleted_points':{},
                                       'recorded_uid'}

              (failed_cases)        - failed cases if aggregate_failed_cases=yes

              (solutions)           - updated solutions with reactions to optimizations (needed for classification of a given computing species)

              (all)                 - if i['collect_all']=='yes', list of results of all iterations [{experiment_desc ..},...]
            }

    """

    import os
    import copy
    import fnmatch
    import json
    import time
    from random import Random

    o=i.get('out','')
    oo=''
    if o=='con': oo='con'

    tmp_dir=i.get('tmp_dir','')

    ic=copy.deepcopy(i)
    ic['module_uoa']=''
    ic['action']=''
    ic['cid']=''
    ic['data_uoa']=''

    pifail=ck.get_from_dicts(ic, 'pause_if_fail', '', None)

    afc=ck.get_from_dicts(ic, 'aggregate_failed_cases', '', None)

    failed_cases=[]

    sols=ck.get_from_dicts(ic, 'solutions', [], None) # Check existing solutions
    isols=len(sols)
    rs=ck.get_from_dicts(ic, 'ref_solution', '', None) 
    iref=ck.get_from_dicts(ic, 'internal_ref', '', None) 

    pdafr=ck.get_from_dicts(ic, 'preserve_deps_after_first_run', '', None)

    prune=ck.get_from_dicts(ic, 'prune', '', None) # Prune existing solutions

    reduce=ck.get_from_dicts(ic, 'reduce', '', None) # Prune existing solutions
    if prune=='': prune=reduce

    reduce_bug=ck.get_from_dicts(ic, 'reduce_bug', '', None) # if 'yes', reduce choices to localize bugs (pipeline fail)

    prune_md5=ck.get_from_dicts(ic, 'prune_md5', '', None) # if 'yes', prune if MD5 doesn't change
    prune_ignore_choices=ck.get_from_dicts(ic, 'prune_ignore_choices', [], None) # Prune existing solutions
    prune_invert=ck.get_from_dicts(ic, 'prune_invert', [], None) # Prune existing solutions
    prune_invert_add_iters=ck.get_from_dicts(ic, 'prune_invert_add_iters', '', None)
    prune_result_conditions=ck.get_from_dicts(ic, 'prune_result_conditions', [], None)
    prune_invert_do_not_remove_key=ck.get_from_dicts(ic, 'prune_invert_do_not_remove_key', [], None)

    print_keys_after_each_iteration=ck.get_from_dicts(ic, 'print_keys_after_each_iteration', [], None)
    lprint_keys_after_each_iteration=-1
    if len(print_keys_after_each_iteration)>0:
       for k in print_keys_after_each_iteration:
           if lprint_keys_after_each_iteration==-1 or len(k)>lprint_keys_after_each_iteration:
              lprint_keys_after_each_iteration=len(k)

    number_of_original_choices=0
    started_prune_invert=False

    condition_objective=ck.get_from_dicts(ic, 'condition_objective', '', None)
    result_conditions=ck.get_from_dicts(ic, 'result_conditions', [], None)

    dsleep=3
    if i.get('sleep','')!='':
       dsleep=float(i['sleep'])

    tags=ck.get_from_dicts(ic, 'tags', [], None)
    tags=ck.convert_str_tags_to_list(tags) # if string, convert to list
    subtags=ck.get_from_dicts(ic, 'subtags', [], None)
    subtags=ck.convert_str_tags_to_list(subtags) # if string, convert to list

    stf=ck.get_from_dicts(ic, 'save_to_file', '', None)

    meta=ck.get_from_dicts(ic, 'meta', {}, None)

    pmk=ck.get_from_dicts(ic, 'process_multi_keys', '', None) # important, default should be '' to be processed later correctly ...

    fk=ck.get_from_dicts(ic, 'frontier_keys', [], None)
    fkr=ck.get_from_dicts(ic, 'frontier_keys_reverse', [], None)
    fmar=ck.get_from_dicts(ic, 'frontier_margins', [], None)

    fdfi=ck.get_from_dicts(ic, 'flat_dict_for_improvements', {}, None)

    record=ck.get_from_dicts(ic, 'record', '', None)
#    We experienced problems with this patch - the problem is somewhere else ...
#    if record=='yes' and len(meta)==0:
#       return {'return':1, 'error':'meta is not defined - can\'t aggregate'}

    record_uoa=ck.get_from_dicts(ic, 'record_uoa', '', None)
    record_repo=ck.get_from_dicts(ic, 'record_repo', '', None)
    record_experiment_repo=ck.get_from_dicts(ic, 'record_experiment_repo', '', None)
    if record.find(':')>=0:
       rx=ck.parse_cid({'cid':record})
       if rx['return']>0: return rx
       record=rx['data_uoa']
       record_repo=rx.get('repo_uoa','')
    record_failed=ck.get_from_dicts(ic, 'record_failed','', None)
    record_only_failed=ck.get_from_dicts(ic, 'record_only_failed','', None)
    record_ignore_update=ic.get('record_ignore_update','')
    if record_ignore_update=='': record_ignore_update='yes'
    if 'record_ignore_update' in ic: del(ic['record_ignore_update'])

    srp=ck.get_from_dicts(ic, 'skip_record_pipeline','', None)
    srd=ck.get_from_dicts(ic, 'skip_record_desc','', None)

    record_permanent=ck.get_from_dicts(ic, 'record_permanent', '', None)

    # Check if repo remote (to save in json rather than to out)
    remote='no'
    if record_repo!='':
       rx=ck.load_repo_info_from_cache({'repo_uoa':record_repo})
       if rx['return']>0: return rx
       remote=rx.get('dict',{}).get('remote','')

    rdict=ck.get_from_dicts(ic, 'record_params', {}, None)
    fkp=ck.get_from_dicts(ic, 'features_keys_to_process', [], None)
    ffki=ck.get_from_dicts(ic, 'frontier_features_keys_to_ignore', [], None)

    state=i.get('state',{})

    jtype=i.get('explore_type','')
    if i.get('random','')=='yes': jtype='random'
    elif i.get('loop','')=='yes': jtype='loop'
    elif i.get('parallel-loop','')=='yes': jtype='parallel-loop'
    elif i.get('parallel-random','')=='yes': jtype='parallel-random'
    cexp={'type':jtype, 
          'omit_probability':i.get('omit_probability',''),
          'start':i.get('start',''),
          'stop':i.get('stop',''),
          'step':i.get('step','')}

    # Check data_uoa
    puoa=i.get('data_uoa','')
    puid=''
    if puoa=='':
       # Try to get from current CID (as module!)
       r=ck.cid({})
       if r['return']==0:
          xruoa=r.get('repo_uoa','')
          xmuoa=r.get('module_uoa','')
          xduoa=r.get('data_uoa','')

          puoa=xmuoa

    if puoa=='':
       return {'return':1, 'error':'data_uoa is not set, i.e. no pipeline module'}

    # Check that data_uoa is module that exists
    r=ck.access({'action':'load',
                 'module_uoa':cfg['module_deps']['module'],
                 'data_uoa':puoa})
    if r['return']>0: return r
    d=r['dict']
    if d.get('pipeline','')!='yes':
       return {'return':1, 'error':'selected pipeline module is not pipeline'}
    puid=r['data_uid']

    # Check meta
    pipeline=i.get('pipeline',{})

    pff=i.get('pipeline_from_file','')
    if pff!='':
       r=ck.load_json_file({'json_file':pff})
       if r['return']>0: return r
       pipeline=r['dict']

    pipeline_update=i.get('pipeline_update',{})

    force_pipeline_update=False
    if len(pipeline_update)!=0:
       r=ck.merge_dicts({'dict1':pipeline, 'dict2':pipeline_update})
       if r['return']>0: return r
       pipeline=r['dict1']

       # Force pipeline update (for example, since changing dataset may change available files)
       force_pipeline_update=True

    pipeline['tmp_dir']=tmp_dir

    # Check if pipeline flags (to update pipeline directly)
    pipeline_flags=i.get('pipeline_flags','')
    if pipeline_flags!='':
       import shlex
       lpipeline_flags=shlex.split('dummy '+pipeline_flags)

       rr=ck.convert_ck_list_to_dict(lpipeline_flags)
       if rr['return']==0:
          dpipeline_flags=rr.get('ck_dict',{})
          if 'cids' in dpipeline_flags: del(dpipeline_flags['cids'])
          if 'action' in dpipeline_flags: del(dpipeline_flags['action'])

          pipeline.update(dpipeline_flags)

    call=ck.get_from_dicts(ic, 'collect_all', {}, None) # Collect all experiemnts
    ae=[]

    # Check customized autotuner
    cat=ck.get_from_dicts(ic, 'custom_autotuner', {}, None) 
    cats=None # script

    if len(cat)>0:
       cmuoa=cat.get('module_uoa','')
       if cmuoa=='':
          x=cat.get('module_uoa_from_pipeline_key','')
          if x!='':
             rx=ck.get_by_flat_key({'dict':pipeline, 'key':x})
             if rx['return']>0: return rx
             cmuoa=rx['value']

       cduoa=cat.get('data_uoa','')
       if cduoa=='':
          x=cat.get('data_uoa_from_pipeline_key','')
          if x!='':
             rx=ck.get_by_flat_key({'dict':pipeline, 'key':x})
             if rx['return']>0: return rx
             cduoa=rx['value']

       try:
           pcat=os.getcwd()
       except OSError:
           os.chdir('..')
           pcat=os.getcwd()

       if cmuoa!='' and cduoa!='':
          rx=ck.access({'action':'find',
                        'module_uoa':cmuoa,
                        'data_uoa':cduoa})
          if rx['return']>0: return rx
          pcat=rx['path']

       cscr=cat.get('script','')

       # Check if has custom script
       rx=ck.load_module_from_path({'path':pcat, 'module_code_name':cscr, 'skip_init':'yes'})
       if rx['return']==0: 
          if 'make' in dir(rx['code']):
             cats=rx['code']
          else:
             return {'return':1, 'error':'autotuner plugin does not have function "make" to make choices'}
       else:
          return rx

    # If pipeline meta is not defined, set up pipeline ...
    fpu=i.get('force_pipeline_update','')

    if len(pipeline)==0 or force_pipeline_update or fpu=='yes':
       if force_pipeline_update or fpu=='yes':
          ii=copy.deepcopy(pipeline)
       else:
          ii=copy.deepcopy(ic)

       ii['out']=o # My latest change (to be able to use local env)
       ii['module_uoa']=puoa
       ii['action']='pipeline'
       ii['prepare']='yes'

       pipeline=ck.access(ii)

       if pipeline['return']>0: return pipeline
       if pipeline.get('fail','')=='yes':
          return {'return':1, 'error':'pipeline setup failed'}
       if pipeline.get('ready','')!='yes':
          return {'return':1, 'error':'pipeline is not ready'}
       del(pipeline['return'])

    # Clean and copy pipeline before choice selection
    for q in cfg['clean_pipeline']:
        if q in pipeline: del(pipeline[q])
    pipelinec=copy.deepcopy(pipeline)

    # Check some vars ...
    ni=i.get('iterations','')
    if ni=='': ni=4
    try: ni=int(ni)
    except Exception as e: pass

    only_filter=ck.get_from_dicts(ic, 'only_filter', '', None)
    if only_filter=='yes':
       ni=1

    ssa=ck.get_from_dicts(ic, 'skip_stat_analysis', '', None)
    sfd=ck.get_from_dicts(ic, 'stat_flat_dict', {}, None)

    sfi=i.get('start_from_iteration','')
    if sfi=='': sfi=1
    if type(sfi)!=int: sfi=int(sfi)

    srm=i.get('repetitions','')
    if srm=='': srm=4

    try: srm=int(srm)
    except Exception as e: pass

    # Check choices descriptions and dimensions
    cdesc=pipeline.get('choices_desc',{})
    corder=copy.deepcopy(i.get('choices_order',[]))

    csel=i.get('choices_selection',{})
    ccur=[]
    pccur={} # pruned choices, if needed

    ref_stat_dict={} # if check with reference, save it
    ref_stat_out={}  # last iteration output for the reference
    ref_rrr={}       # ref characteristics
    ref_rr={}        # ref last iteration output
    keys=[]          # keys to check for conditions or during pruning

    # most likely just one iteration - then set defaults to generate random solutions
    if len(corder)==1 and len(csel)==0:
       csel=[{"type":"random"}]

    # Prepare multi-dimensional vector of choices
    dv1=[] # Current dimensions
    for iq1 in range(0,len(corder)):
        dv=[]
        q1=corder[iq1]
        zz=csel[iq1]
        ztags=[]
        if zz.get('tags','')!='': ztags=zz['tags'].split(',')
        znotags=[]
        if zz.get('notags','')!='': znotags=zz['notags'].split(',')
        zanytags=[]
        if zz.get('anytags','')!='': zanytags=zz['anytags'].split(',')
        for q2 in q1:
            if '*' in q2 or '?' in q2:
               for k in sorted(cdesc, key=lambda v: cdesc[v].get('sort',0)):
                   if fnmatch.fnmatch(k,q2):
                      # Check tags (must have)
                      yy=cdesc[k].get('tags',[])
                      add=True
                      for j in ztags:
                          j=j.strip()
                          if j!='' and j not in yy:
                             add=False
                             break
                      if add:
                         # Any of those
                         if len(zanytags)>0:
                            add=False
                            for j in zanytags:
                                j=j.strip()
                                if j!='' and j in yy:
                                   add=True
                                   break
                         if add:
                            # Check that none of those
                            for j in znotags:
                                j=j.strip()
                                if j!='' and j in yy:
                                   add=False
                                   break
                            if add:
                               dv.append(k)
            else:
               dv.append(q2)
        dv1.append(dv)
    corder=dv1

    # Save original
    ocorder=copy.deepcopy(corder)

    # Check seed
    seed=i.get('seed','')
    if seed=='':
       my_random=Random()
    else:
       my_random=Random(int(seed))

       if o=='con':
          ck.out('')
          ck.out('Random seed: '+str(seed))
          ck.out('')

    points={} # Keep best points if finding best points (possibly with Pareto)
    ppoint={} # Permanent (default point) to calculate improvements ...

    # Start iterations
    rr={'return':0}
    stat_dict={'return':0}
    rrr={'return':0}
    dd={}
    finish=False
    all_solutions=False

    removing_key=''
    removing_value=''
    default_removing_value=''
    cur_md5=''
    last_md5=''
    last_md5_fail_text='compilation returned object file with the same MD5'
    pruned_influence={}
    pruned_chars=[]
    prune_checked_keys=[]
    pruned_inversed_flags={}
    prune_check_all=[]

    sol={}

    increased_iterations=False

    recorded_info={}
    last_record_uid=''

    ref_keys={}

    m=-1
    while True:
        m+=1
        if ni!=-1 and m>=ni:
           break

        mm=m+1

        x='Pipeline iteration: '+str(mm)
        if ni!=-1: x+=' of '+str(ni) 

        ck.out(sep1)
        ck.out(x)

        time.sleep(0.5)

        # Copy original
        if m==0 or mm>=sfi:
           pipeline=copy.deepcopy(pipelinec)

        # Check if there is a pre-selection
        al=''
        suid=''
        if isols>0:
           if not (iref=='yes' and m==0) and not all_solutions:
              if o=='con':
                 x=''
                 if rs=='yes':
                    x=' reference'

                 ck.out('')
                 ck.out('  Checking pre-existing'+x+' solution ...')

              # Find choices (iterate over solutions since there can be more 
              #  than one point in each solution due to Pareto)

              nz=[] # remaining keys to select from (if 0, stop)

              if rs=='yes':
                 sol=sols[0]
                 corder1=sol.get('ref_choices_order',[])
                 cx1=sol.get('ref_choices',{})
                 suid=sol.get('solution_uid','')
              else:
                 if prune=='yes':
                    if len(pccur)>0:
                       if o=='con':
                          ck.out('')
                          ck.out('  Pruning or inverting solution (iteratively reducing complexity of the found solution) ...')

                       # Check non-zero ones:
                       if not started_prune_invert:
                          for g in range(0, len(corder1)):
                              k=corder1[g]
                              v=pccur.get(k, None)
                              if v!='' and v!=None and k not in prune_ignore_choices and k not in prune_checked_keys:
                                 nz.append(k)

                       # Remove one (random or one by one)
                       if len(nz)==0:
                          if not started_prune_invert:
                             if o=='con':
                                ck.out('')
                                ck.out('  ALL choices have been checked - main pruning finished !')

                          if prune_invert!='yes':
                             break

                          if not started_prune_invert:
                             ck.out('  ***')
                             ck.out('  Starting iteratively inverting all possible choices ...')

                             for q in ocorder[0]:
                                 if q not in corder1:
                                    corder1.append(q)

                             for q in corder1:
                                 if q not in prune_checked_keys and q not in pccur and q in cdesc:
                                    cddx=cdesc[q]
                                    if 'boolean' in cddx.get('tags',[]):
                                       prune_check_all.append(q)

                             started_prune_invert=True

                          if len(prune_check_all)==0:
                             ck.out('')
                             ck.out('  Pruning finished !')

                             break

                          # Switching off key
                          y=my_random.randrange(0,len(prune_check_all))

                          removing_key=prune_check_all[y]
                          del(prune_check_all[y])

                          cddx=cdesc.get(removing_key,{})
                          cccx=cddx.get('choice',[])

                          v=''
                          default_removing_value=''
                          if len(cccx)>0:
                             v=cccx[len(cccx)-1]
                             default_removing_value=cccx[0]

                          removing_value=v
                          pccur[removing_key]=v

                          cx1=copy.deepcopy(pccur)

                          if o=='con':
                             ck.out('')
                             ck.out('    Trying to invert key '+removing_key+' to default ('+v+') ...')

                       else:
                          y=my_random.randrange(0,len(nz))

                          removing_key=nz[y]
                          removing_value=pccur[removing_key]

                          del(nz[y])

                          pccur[removing_key]=''

                          prune_checked_keys.append(removing_key)

                          cx1=copy.deepcopy(pccur)

                          if o=='con':
                             ck.out('')
                             ck.out('    Trying to remove key '+removing_key+' ('+str(removing_value)+') ...')

                    # Increase iterations if check all
                    if len(nz)==0 and prune_invert_add_iters=='yes' and prune_invert=='yes' and not increased_iterations:
                       increased_iterations=True
                       for q in ocorder[0]:
                           if q not in prune_checked_keys and q not in pccur and q in cdesc:
                              cddx=cdesc[q]
                              if 'boolean' in cddx.get('tags',[]):
                                 ni+=1

                 if prune!='yes' or len(pccur)==0:
                    sol={}
                    bb=0
                    if iref=='yes': bb=1
                    for b in sols:
                        bp=b.get('points',[])
                        suid=b.get('solution_uid','')
                        for bx in bp:
                            if m==bb:
                               sol=bx
                               break
                            bb+=1
                        if len(sol)>0:
                           keys=list(sol.get('improvements',{}).keys())
                           break

                    if len(sol)==0:
                       all_solutions=True
                       suid=''
                    else:
                       corder1=sol.get('pruned_choices_order',[])
                       cx1=sol.get('pruned_choices',{})

                    if suid!='' and o=='con':
                       ck.out('     Solution UID: '+suid+' ...')

              if all_solutions:
                 # If checked all solutions, reset original choices and start (random) exploration
                 corder=copy.deepcopy(ocorder)
                 ccur=[]
                 al=''

                 if o=='con':
                    ck.out('')
                    ck.out('  ALL pre-existing solutions validated - restarting extra exploration ...')

              else:
                 corder2=[]
                 ccur2=[]

                 for b in corder1:
                     v=cx1.get(b,None)
                     if v!='' and v!=None:
                        ccur2.append(v)
                        corder2.append(b)

                 # Check if reuse ref choices
                 if sol.get('preset_ref_choices','')=='yes' and len(ref_keys)>0:
                    for k in sorted(ref_keys):
                        if k not in corder2:
                           corder2.append(k)
                           ccur2.append(ref_keys[k])

                 corder=[corder2]
                 ccur=[ccur2]

                 al='yes'

                 if prune=='yes' and len(pccur)==0:
                    pccur=copy.deepcopy(cx1)

        # Make selection
        jj={'module_uoa':cfg['module_deps']['choice'],
            'action':'make',
            'choices_desc':cdesc,
            'choices_order':corder,
            'choices_selection':csel,
            'choices_current':ccur,
            'custom_explore':cexp,
            'pipeline':pipeline,
            'random_module':my_random,
            'out':o}
        if al!='': jj['all']=al

        if cats!=None and al!='yes':
           # customized autotuning via external module (exploration)
           # specialize our autotuner to a given program (domain)

           jj['ck_kernel']=ck
           jj['state']=state
           jj['meta']=meta
           jj['autotuning_iteration']=m
           jj['tmp_dir']=tmp_dir
           jj['custom_autotuner_meta']=cat

           jj['vars']=i.get('custom_autotuner_vars',{})

           r=cats.make(jj)
           if r['return']>0: return r

           # Print keys and update pipeline!
           ks=r.get('keys',{})
           if len(ks)>0:
              if o=='con': 
                 ck.out('')

              for k in sorted(ks):
                  v=ks[k]
                  if o=='con': 
                     ck.out(' * '+k+' = '+str(v))

                  rx=ck.set_by_flat_key({'dict':pipeline, 'key':k, 'value':v})
                  if rx['return']>0: return rx

              if o=='con': 
                 ck.out('')

              # Save ref choices just in case
              if m==0:
                 ref_keys=copy.deepcopy(ks)

        else:
           # CK-based selection 
           r=ck.access(jj)
           if r['return']>0: return r

        if r.get('finish',True):
           finish=True
           break

        if i.get('ask_enter_after_choices','')=='yes':
           ck.out('')
           ck.inp({'text':'Press Enter to continue ...'})

        time.sleep(dsleep) # wait to see selection ...

        # Check if pass this iteration
        if mm<sfi:
           ck.out('')
           ck.out('  (skiped by request)')
           continue

        # Describing experiment
        dd={'tags':tags,
            'subtags':subtags,
            'meta':meta,
            'pipeline':pipelinec,
            'pipeline_uoa':puoa,
            'pipeline_uid':puid}

        ddcl=[] # characteristics list (from statistical repetitions)

        fail='no'
        fail_reason=''
        rr={}
        last_orders_from_pipeline=[]
        for sr in range(0, srm):
            if only_filter=='yes': continue

            ck.out('')
            ck.out('      ------------------- Statistical repetition: '+str(sr+1)+' of '+str(srm)+' -------------------')
            ck.out('')

            pipeline1=copy.deepcopy(pipeline)

            pipeline1['prepare']='no'
            pipeline1['module_uoa']=puoa
            pipeline1['action']='pipeline'
            pipeline1['out']=o
            pipeline1['state']=state
            pipeline1['meta']=meta
            pipeline1['autotuning_iteration']=m
            pipeline1['statistical_repetition_number']=sr
            pipeline1['tmp_dir']=tmp_dir

#            if prune_md5=='yes':

            # If last pruning iteration, compile and run code (to get all last characteristics)
            if prune_md5=='yes' and (len(nz)!=0 or len(prune_check_all)!=0):
               if o=='con' and last_md5!='':
                  ck.out('')
                  ck.out('      Checking MD5: '+last_md5)

               pipeline1['last_md5']=last_md5
               pipeline1['last_md5_fail_text']=last_md5_fail_text

            rr=ck.access(pipeline1)
            if rr['return']>0: return rr

            fail=rr.get('fail','')
            fail_reason=rr.get('fail_reason','')

            if pdafr=='yes' and m==0 and sr==0:
               # Preserve resolved deps (useful for replay)
               pipeline['dependencies']=copy.deepcopy(pipeline1.get('dependencies',{}))
               pipelinec['dependencies']=copy.deepcopy(pipeline1.get('dependencies',{}))

               # Check if reduce bug but pipeline didn't fail
               if reduce_bug=='yes' and fail!='yes':
                  return {'return':1, 'error':'trying to reduce bug but pipeline didn\'t fail'}

            xcur_md5=pipeline1.get('characteristics',{}).get('compile',{}).get('md5_sum','')
            if sr==0 and xcur_md5!='': cur_md5=xcur_md5

            state=rr.get('state',{})

            last_orders_from_pipeline=rr.get('choices_order',[])

            if (fail!='yes' and record_only_failed!='yes') or (fail=='yes' and (record_failed=='yes' or record_only_failed=='yes')):
               ddcl.append(pipeline1.get('characteristics',{}))

               if sr==0: # record for the first iteration otherwise pipeline may change via state ...
                  dd['dict']=i.get('record_dict',{}) # useful for subview_uoa
                  dd['choices']=rr.get('choices',{})
                  dd['choices_order']=rr.get('choices_order',[])
                  dd['choices_desc']=rr.get('choices_desc',{})
                  dd['features']=rr.get('features',{})
                  dd['features']['statistical_repetitions']=srm
                  if suid!='':
                     dd['features']['solution_uid']=suid
                  dd['features_desc']=rr.get('features_desc',{})
                  dd['dependencies']=rr.get('dependencies',{})
                  dd['characteristics_desc']=rr.get('characteristics_desc',{})

                  # TBD: CHECK HOW TO WRITE META HERE DEPENDING ON SCENARIOS ...

                  meta1=rr.get('meta',{})
                  if len(meta1)>0: meta.update(meta1)
                  dd['meta']=meta

            if fail=='yes': break

        # Record extra pipeline info
        fail_bool=False
        if fail=='yes': fail_bool=True
        dd['pipeline_state']={'repetitions':srm,
                              'fail_reason':fail_reason,
                              'fail':fail,
                              'fail_bool':fail_bool}

        # Record list of characteristics (from multiple reptitions)
        dd['characteristics_list']=ddcl

        if afc=='yes' and fail_bool:
           failed_cases.append({'choices':rr.get('choices',{}),
                                'choices_order':rr.get('choices_order',[]),
                                'features':rr.get('features',{}),
                                'characteristics':rr.get('characteristics',{}),
                                'pipeline_state':dd.get('pipeline_state',{})})

        if i.get('pause','')=='yes' or (fail_bool and pifail=='yes'):
           ck.out('')
           ck.inp({'text':'Press Enter to continue ...'})

        ##########################################################################################
        # Collect all results if needed to be processed by user (customized crowd-tuning, for example)
        if call=='yes':
           ae.append(dd)

        ##########################################################################################
        # Recording experiment if needed
        current_point=''
        current_record_uid=''

        stat_dict={}

        recorded_info={'points':[], 'deleted_points':[], 'recorded_uid':''}

        iec={'module_uoa':cfg['module_deps']['experiment'],

             'repo_uoa': record_repo,
             'experiment_repo_uoa': record_experiment_repo,
             'experiment_uoa':record_uoa,

             'record_permanent':record_permanent,

             'features_keys_to_process':fkp}
        fft={}

        if record=='yes' and only_filter!='yes':
           # Will be reused for frontier
           fft={} # flat features

           if (fail!='yes' and record_only_failed!='yes') or (fail=='yes' and (record_failed=='yes' or record_only_failed=='yes')):

              t1=time.time()

              if o=='con':
                 ck.out(sep)
                 ck.out('Recording experiment ...')
                 ck.out('')

              ie=copy.deepcopy(iec)

              if remote=='yes': ie['out']=''
              else: ie['out']=oo

              if len(fdfi)>0: 
                 dd['dict_to_compare']=fdfi

              ie['action']='add'
              ie['ignore_update']=record_ignore_update
              ie['sort_keys']='yes'
              ie['record_all_subpoints']='yes'
              ie['process_multi_keys']=pmk
              ie['dict']=dd

              if srp!='': ie['skip_record_pipeline']=srp
              if srd!='': ie['skip_record_desc']=srd

              if ssa!='': ie['skip_stat_analysis']=ssa

              # Update what we record and how we process data from external dict -> 
              #  may be customized depending on scenarios 
              #  (compiler flag tuning, OpenCL/MPI params, etc)
              ie.update(rdict)

              rx=ck.access(ie)
              if rx['return']>0: return rx

              current_point=rx.get('point','')
              current_record_uid=rx.get('recorded_uid','')

              if current_point!='': recorded_info['points'].append(current_point)
              if current_record_uid!='': 
                 recorded_info['recorded_uid']=current_record_uid
                 last_record_uid=current_record_uid

              stat_dict=rx['dict_flat']
              rrr=rx['stat_analysis']
              fft=rx['flat_features']

              tt=time.time()-t1
              if o=='con':
                 ck.out('')
                 ck.out('Recorded successfully in '+('%.2f'%tt)+' secs.')

        ##########################################################################################
        # If was not performed via recording, perform statistical analysis here
        if ssa!='yes' and fail!='yes' and len(stat_dict)==0:
           if o=='con':
              ck.out('')
              ck.out('Performing explicit statistical analysis of experiments ...')

           if prune=='yes': sfd={}

           ii={'action':'multi_stat_analysis',
               'module_uoa':cfg['module_deps']['experiment'],
               'dict':stat_dict,
               'flat_dict':sfd,
               'dict_to_add':dd,
               'dict_to_compare':fdfi,
               'process_multi_keys':pmk,
               'skip_stat_analysis':ssa}
           rrr=ck.access(ii)
           if rrr['return']>0: return rrr
           stat_dict=rrr['dict_flat']

        ##########################################################################################
        # Print various values to monitor iterations (if needed)
        if o=='con' and fail!='yes' and len(print_keys_after_each_iteration)>0:

           ck.out('')
           ck.out('Monitoring characteristics:')
           ck.out('')

           for k in print_keys_after_each_iteration:
               v=stat_dict.get(k,None)
               x='  * '+(' '*(lprint_keys_after_each_iteration-len(k)))+str(k)+' = '+str(v)

               vr=ref_stat_dict.get(k,None)
               if v!=None and vr!=None:
                  x+=' ('+str(vr)+')'

               ck.out(x)

        ##########################################################################################
        # Check conditions
        if current_point!='' and len(result_conditions)>0 and (prune!='yes' or m>0) and fail!='yes':
           if o=='con':
              ck.out('')
              ck.out('Check extra conditions on results ...')

           # Check conditions
           ii={'action':'check',
               'module_uoa':cfg['module_deps']['math.conditions'],
               'new_points':['0'],
               'results':[{'point_uid':'0', 'flat':stat_dict}],
               'conditions':result_conditions,
               'middle_key':condition_objective,
               'out':oo}
           ry=ck.access(ii)
           if ry['return']>0: return ry 

           xdpoints=ry['points_to_delete']
           if len(xdpoints)>0:
              if o=='con':
                 ck.out('')
                 ck.out('    WARNING: conditions on characteristics were not met!')

              # Delete point and fail
              rx=ck.access({'action':'delete_points',
                            'module_uoa':cfg['module_deps']['experiment'],
                            'points':[{'module_uid':cfg['module_deps']['experiment'], 
                                       'data_uid':current_record_uid,
                                       'point_uid':current_point}],
                            'out':oo})
              if rx['return']>0: return rx

              rr['fail']='yes'
              rr['fail_reason']='conditions were not met'

              fail=rr.get('fail','')
              fail_reason=rr.get('fail_reason','')

        ##########################################################################################
        # If checking pre-recoreded solutions, add result
        if prune!='yes' and isols>0 and m<isols:
           if o=='con':
              ck.out('')
              ck.out('Recording reaction to optimizations to a pre-existing solution (for automatic classification of computational species) ...')
              ck.out('')

           # Prepare improvements/degradations
           reaction=False
           bb=0
           for jb in range(0, len(sols)):
               b=sols[jb]
               bp=b.get('points',[])
               for by in range(0, len(bp)):
                   if m==bb:
                      bp[by]['reaction_raw_flat']=copy.deepcopy(stat_dict)
                      bp[by]['reaction_info']={'fail':fail, 'fail_reason':fail_reason}

                      imp=copy.deepcopy(bp[by].get('improvements',{}))
                      if len(imp)>0:
                         for k in imp:
                             imp[k]=stat_dict.get(k,None)
                         bp[by]['improvements_reaction']=imp

                      reaction=True
                   bb+=1
               if reaction:
                  sols[jb]['points']=bp
                  break

        # Check if need to leave only points on frontier 
        #   (our frontier is not 'Pareto efficient' since we have discreet characteristics)

#        if len(fk)>0 and (len(stat_dict)>0 or only_filter=='yes'): - otherwise doesn't work if last point is error

        # If checking pruning (that results didn't change much)
        if prune=='yes':
           # Rebuild list of current choices from last choices dict (since pipeline may change choices, such as base flag)
           if len(fft)>0:
              pccur={}
              for q in last_orders_from_pipeline:
                  q1='##choices'+q[1:]
                  v=fft.get(q1,'')
                  if v!='' and v!=None:
                     pccur[q]=v

           if m==0:
              # Saving reference stats
              ref_stat_dict=copy.deepcopy(stat_dict)
              ref_stat_out=copy.deepcopy(rr)
              fdfi=ref_stat_dict
              last_md5=cur_md5 #stat_dict.get('##characteristics#compile#md5_sum#min',None)

              for q in pccur:
                  if q!=None and q!='':
                     number_of_original_choices+=1

              if o=='con':
                 ck.out('')
                 ck.out('Preserving reference statistics to compare against during solution pruning ...')
                 ck.out('')

           else:
              if o=='con':
                 ck.out('')
                 ck.out('Checking if results have changed during pruning ...')
                 ck.out('')

                 result_the_same=False
                 if fail=='yes':
                    if reduce_bug=='yes' or (fail_reason==last_md5_fail_text):
                       result_the_same=True

                 if not result_the_same and fail!='yes':
                    if len(prune_result_conditions)==0:
                       result_the_same=True
                    else:
                       ck.out('')
                       ck.out('Check extra pruning conditions on results ...')
                       ck.out('')

                       # Check conditions
                       ii={'action':'check',
                           'module_uoa':cfg['module_deps']['math.conditions'],
                           'new_points':['0'],
                           'results':[{'point_uid':'0', 'flat':stat_dict}],
                           'conditions':prune_result_conditions,
                           'middle_key':condition_objective,
                           'out':oo}
                       ry=ck.access(ii)
                       if ry['return']>0: return ry 

                       gpoints=ry['good_points']
                       dpoints=ry['points_to_delete']
                       pruned_chars=ry['keys']

                       if len(dpoints)==0:
                          result_the_same=True

                 if o=='con':
                    ck.out('')
                    if result_the_same:
                       ck.out('    *** Result did not change!')
                    else:
                       ck.out('    *** Result changed!')

                 restore_stats=False
                 if started_prune_invert:
                    # We are in inverting mode ######################################################
                    if result_the_same:
                       if o=='con':
                          ck.out('')
                          ck.out('    Keeping default key "'+removing_key+'" ...')

                       pccur[removing_key]=removing_value

                       # If new compilation MD5 and new stats, make a new referneces point
                       if not (fail=='yes' and fail_reason==last_md5_fail_text):
                          ref_stat_dict=copy.deepcopy(stat_dict)
                          ref_stat_out=copy.deepcopy(rr)
                          ref_rrr=copy.deepcopy(rrr)
                          ref_rr=copy.deepcopy(rr)
                          fdfi=ref_stat_dict
                          last_md5=cur_md5

                          if o=='con':
                             ck.out('')
                             ck.out('         NEW REFERENCE POINT (MD5='+last_md5+')!')

                    else:
                       if prune_invert_do_not_remove_key=='yes':
                          prx1='Adding'
                          prx1a='to'
                          prx2=default_removing_value
                       else:
                          prx1='Removing'
                          prx1a='from'
                          prx2=''

                       if o=='con':
                          ck.out('')
                          ck.out('    '+prx1+' key "'+removing_key+'" '+prx1a+' choices ...')

                       pccur[removing_key]=prx2

                       pruned_inversed_flags[removing_key]=prx2

                 else:
                    # We are in standard pruning mode ###############################################
                    if result_the_same:
                       if o=='con':
                          ck.out('')
                          ck.out('    Removing key "'+removing_key+'" from choices ...')

                       pccur[removing_key]=''

                       pruned_inversed_flags[removing_key]=removing_value

                       # If new compilation MD5 and new stats, make a new referneces point
                       if not (fail=='yes' and fail_reason==last_md5_fail_text):
                          ref_stat_dict=copy.deepcopy(stat_dict)
                          ref_stat_out=copy.deepcopy(rr)
                          ref_rrr=copy.deepcopy(rrr)
                          ref_rr=copy.deepcopy(rr)
                          fdfi=ref_stat_dict
                          last_md5=cur_md5 #stat_dict.get('##characteristics#compile#md5_sum#min',None)

                          if o=='con':
                             ck.out('')
                             ck.out('         NEW REFERENCE POINT (MD5='+last_md5+')!')

                    else:
                       if o=='con':
                          ck.out('')
                          ck.out('    Keeping key "'+removing_key+'" ...')

                       pccur[removing_key]=removing_value

                       restore_stats=True

                 # Record influential optimization
                 if not result_the_same:
                    kky={}
                    if len(pruned_chars)>0:
                       for q in pruned_chars:
                           kky[q]=stat_dict.get(q,None)
                    pruned_influence[removing_key]=kky

                 # Restore stat dict (for comparison)
                 if restore_stats:
                    stat_dict=copy.deepcopy(ref_stat_dict)
                    rrr=copy.deepcopy(ref_rrr)
                    rr=copy.deepcopy(ref_rr)

        if prune!='yes' and (len(fk)>0 or only_filter=='yes'):
           # If data was recorded to repo, reload all points 
           opoints={} # original points with all info (used later to delete correct points)
           if record=='yes':
              if o=='con':
                 ck.out('')
                 ck.out('Reloading points to detect frontier ...')
                 ck.out('')

              ie=copy.deepcopy(iec)

              ie['action']='get'

              if only_filter=='yes':
                 ie['get_all_points']='yes'
              else:
                 # NOTE - I currently do not search points by features, i.e. all points are taken for Paretto
                 # should improve in the future ...
                 ie['flat_features']=fft
                 ie['features_keys_to_ignore']=ffki # Ignore parts of features to be able to create subset for frontier ...
                 if 'features_keys_to_process' in ie: del(ie['features_keys_to_process'])
                 ie['skip_processing']='yes'

              ie['separate_permanent_points']='yes'
              ie['load_json_files']=['flat','features']
              ie['get_keys_from_json_files']=fk
              ie['out']='con'

              rx=ck.access(ie)
              if rx['return']>0: return rx

              xpoints=rx['points']
              opoints=copy.deepcopy(xpoints) # original points

              points={}

              ppoints=rx['ppoints']
              ppoint={}
              if len(ppoints)>0:
                 ppoint=ppoints[0]

              for q in xpoints:
                  uid=q['point_uid']
                  points[uid]=q.get('flat',{})
           else:
              rx=ck.gen_uid({})
              if rx['return']>0: return rx
              uid=rx['data_uid']

              w={}
              for q in stat_dict: 
                  if q in fk: w[q]=stat_dict[q]

              points[uid]=w

           # Filtering ...
           if o=='con':
              ck.out(sep)
              ck.out('Filtering multiple characteristics on frontier (not necessarily Pareto) for multi-objective autotuning')
              ck.out('')

           # Save originals to know which ones to delete if recording ...
           rx=ck.access({'action':'filter',
                         'module_uoa':cfg['module_deps']['math.frontier'],
                         'points':points,
                         'frontier_keys':fk,
                         'reverse_keys':fkr,
                         'margins':fmar,
                         'out':oo})
           if rx['return']>0: return rx

           points=rx['points']
           dpoints=rx['deleted_points']

           recorded_info['deleted_points']=list(dpoints.keys())

           recorded_info['points']=list(points.keys())
           if len(ppoint)>0:
               recorded_info['points'].append(ppoint['point_uid'])

           # Delete filtered if record
           if record=='yes':
              xdpoints=[]
              for q in dpoints:
                  found=False
                  for qq in opoints:
                      if qq['point_uid']==q:
                         found=True
                         break
                  if found:
                     xdpoints.append(qq)

              # Attempt to delete non-optimal solutions
              rx=ck.access({'action':'delete_points',
                            'module_uoa':cfg['module_deps']['experiment'],
                            'points':xdpoints,
                            'out':oo})
              if rx['return']>0: return rx

        if i.get('ask_enter_after_each_iteration','')=='yes':
           ck.out('')
           ck.inp({'text':'Press Enter to continue autotuning or DSE ...'})

    # Mention, if all iterations were performed, or autotuning rached max number of iterations
    if finish:
       ck.out('')
       ck.out('All iterations are done!')

    recorded_info['last_recorded_uid']=last_record_uid
    rz={'return':0, 'last_iteration_output':rr, 'last_stat_analysis': rrr, 'experiment_desc':dd, 'recorded_info':recorded_info, 'failed_cases':failed_cases}

    if call=='yes':
       rz['all']=ae

    # If pruning, print last results
    report=''
    if prune=='yes' and o=='con':
       rz['last_stat_analysis']=ref_stat_dict
       rz['last_iteration_output']=ref_stat_out

       ll=0
       lx=0
       for k in corder1:
           if len(k)>ll: 
              ll=len(k)
           v=pccur.get(k, None)
           if v!='' and v!=None:
              lx+=1

       x=str(lx)
       if prune_invert!='yes':
          x+=' vs '+str(number_of_original_choices)

       report='\n  Final pruned choices ('+x+') :\n'

       report+='        Characteristics\' changes (in brackets):\n'
       for q in range(0, len(pruned_chars)):
           pc=pruned_chars[q]
           report+='           '+str(q)+' = '+pc+'\n'
       report+='\n'

       keys=[]
       pruned={}
       pruned_order=[]

       for k in corder1:
           v=pccur.get(k,None)
           if v!='' and v!=None:
              pruned_order.append(k)
              pruned[k]=v
              keys.append(k)

       for k in pruned_influence:
           if k not in keys:
              keys.append(k)

       compiler_flags=''

       for k in keys:

           v=pccur.get(k,None)
           v1=pruned_influence.get(k,None)

           if v!=None and k.startswith('##compiler_flags#'): 
              compiler_flags+=' '+v.strip()

           j=ll-len(k)

           x=' '*j

           y=''
           if v1!=None:
              for q in pruned_chars:
                  v1x=v1.get(q,0.0)
                  if v1x==None: v1x=0.0
                  if y!='': y+=';'
                  v2=float(v1x)
                  y+=('%1.3f' % v2)
           else:
              y='           '
           report+='    '+k+x+' ('+y+') : '+str(v)+'\n'

       compiler_flags=compiler_flags.strip()
       if compiler_flags!='':
          report+='\n        Compiler flags: '+compiler_flags+'\n'
          report+='\n'

       if o=='con':
          ck.out(report)

       rz['report']=report

       # Embedd to first solution:
       b=sols[0]['points'][0]

       b['pruned_choices_order']=pruned_order
       b['pruned_choices']=pruned

       b['pruned_influence']=pruned_influence
       b['pruned_chars']=pruned_chars
       b['pruned_inversed_flags']=pruned_inversed_flags

       sols[0]['points'][0]=b

    if m>0 and i.get('skip_done','')!='yes':
       ck.out(sep)
       ck.out('Done!')

    if len(sols)>0:
       rz['solutions']=sols

    if stf!='':
       rx=ck.save_json_to_file({'json_file':stf, 'dict':rz, 'sort_keys':'yes'})

    return rz

##############################################################################
# Run pipeline once ...

def run(i):
    """
    See "autotune" API with iterations=1
    """

    if i.get('iterations','')=='': i['iterations']=1
    return autotune(i)
