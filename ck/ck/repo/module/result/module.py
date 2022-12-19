#
# Collective Knowledge (container for any result)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: cTuning foundation, admin@cTuning.org, http://cTuning.org
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel) 

# Local settings
import os

onchange='document.ck_result_form.submit();'

common_data_keys=['repo_uoa','data_uoa','tags']
common_data_keys2={'experiment_repo_uoa':'repo_uoa',
                   'experiment_uoa':'data_uoa',
                   'experiment_tags':'tags'}

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
# 

def get_raw_config(i):
    """
    Input:  {
               cfg_uoa - UOA of result.cfg
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    cfg_uoa=i['cfg_uoa']
    cfg_id=i.get('cfg_id','')

    r=load_cfg({'cfg':cfg_uoa, 'cfg_id':cfg_id})
    if r['return']>0: return r

    data_config=r['data_config']
    data_config['return'] = 0

    return data_config

##############################################################################
# 

def get_raw_data(i):
    """
    Input:  {
               cfg_uoa - UOA of result.cfg

               (repo_uoa)
               (data_uoa)
               (tags)
               (user)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    # Load cfg
    cfg_uoa=i['cfg_uoa']
    cfg_id=i.get('cfg_id','')

    r=load_cfg({'cfg':cfg_uoa, 'cfg_id':cfg_id})
    if r['return']>0: return r

    data_config=r['data_config']
    data_config['return'] = 0

    dd=r['dict']

    experiment_convertor=dd.get('experiment_convertor',[])

    # Get default parameters where to search for data (module "result")
    ii={'action':'search',
        'module_uoa':work['self_module_uid']}
    for k in common_data_keys:
        for where in [dd, i]:
            v=where.get(k,'')
            if v!='':
               ii[k]=v

    r=ck.access(ii)
    if r['return']>0: return r

    table=[]
    num_users=0

    user=i.get('user','')

    for l in r['lst']:
        
        path=l['path']

        # General files (for compatibility)
        files=os.listdir(path)
        for f in files:
            if f.startswith('result-') and f.endswith('.json'):
               pf=os.path.join(path, f)

               r=ck.load_json_file({'json_file':pf})
               if r['return']>0: return r

               result=r['dict'] # List even with 1 result

               table+=result

        # Per users
        path1=os.path.join(path, 'users')
        if os.path.isdir(path1):
           users=os.listdir(path1)
           for u in users:
               if user!='' and u!=user:
                  continue

               path2=os.path.join(path1, u)
               if os.path.isdir(path2):
                  files=os.listdir(path2)
                  new_user=True
                  for f in files:
                      if f.startswith('result-') and f.endswith('.json'):
                         if new_user:
                            new_user=False
                            num_users+=1

                         pf=os.path.join(path2, f)

                         r=ck.load_json_file({'json_file':pf})
                         if r['return']>0: return r

                         result=r['dict'] # List even with 1 result

                         for res in result:
                             table.append(res)

    # Get default parameters where to search for data (module "experiment")
    ii={}
    for k in common_data_keys2:
        for where in [dd, i]:
            v=where.get(k,'')
            if v!='':
               ii[common_data_keys2[k]]=v

    if len(ii)>0:
       ii['action']='search'
       ii['module_uoa']=cfg['module_deps']['experiment']

       r=ck.access(ii)
       if r['return']>0: return r

       for l in r['lst']:
           
           path=l['path']

           # General files (for compatibility)
           files=os.listdir(path)
           for f in files:
               if f.startswith('ckp-') and f.endswith('.flat.json'):
                  pf=os.path.join(path, f)

                  r=ck.load_json_file({'json_file':pf})
                  if r['return']>0: return r

                  flat_result=r['dict']

                  r=convert_experiment_to_result({'dict':flat_result,
                                                  'convertor':experiment_convertor})
                  if r['return']>0: return r

                  table+=r['table']

    # Merge if needed
    merge={}
    new_table=[]
    for t in range(0, len(table)):
        result=table[t]
        merge_id=result.get('_merge','')
        if merge_id=='':
           new_table.append(result)
        else:
           if merge_id not in merge:
              # Save position of the first merge
              merge[merge_id]=t 
              new_table.append(result)
           else:
              tmerge=merge[merge_id]
              table[tmerge].update(result)

    table=new_table

    # Add sequence numbers
    seq_number=1
    for t in table:
        t['seq_number']=seq_number
        t['_const']=1
        seq_number+=1

    return {'return':0, 'table':table}

##############################################################################
# post-process html

def postprocess_html(i):
    """
    Input:  {
              html - html to post-process

              original_input (dict) - passing extra parameters from URL
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              html - post-processed html
            }

    """

    h=i['html']

    # Substitutions
    sub={
      'ck_html_title':'',
      'ck_html_title_main':'',
      'ck_html_title_note':'',
      'ck_html_end_note':'',
      'ck_html_form':''
    }
    
    # Check cfg to customize input
    oi=i.get('original_input',{})

    result_cfg=oi.get('cfg','')
    cfg_id=oi.get('cfg_id','')
    
    if result_cfg!='':
       r=load_cfg({'cfg':result_cfg, 'cfg_id':cfg_id})
       if r['return']>0: return r

       dcfg=r['dict']

       update_html=dcfg.get('update_html',{})
       if len(update_html)>0:
          sub.update(update_html)

       sub['ck_cfg_uoa']=result_cfg
       sub['ck_cfg_id']=r['cfg_id']
       sub['ck_html_form']=r['html_selector']

    # Check other params in original input and pass them to HTML
    for k in common_data_keys + list(common_data_keys2.keys()) + ['user']:
        sub['ck_'+k]=oi.get(k,'')

    # Update html
    for s in sub:
        h=h.replace('$#'+s+'#$', sub[s])

    return {'return':0, 'html':h}


##############################################################################
# load cfg

def load_cfg(i):

    result_cfg=i['cfg']
    cfg_id=i.get('cfg_id','')

    r=ck.access({'action':'load',
                 'module_uoa':cfg['module_deps']['result.cfg'],
                 'data_uoa':result_cfg})
    if r['return']>0: return r

    p=r['path']
    
    dcfg=r['dict']

    data_config=dcfg.get('data_config',{})

    selector=[]
    html_selector=''

    if dcfg.get('multiple_configs','')=='yes' or len(data_config)==0:
       # Attempt to read multiple configs
       ii={'action':'create_selector',
           'module_uoa':cfg['module_deps']['wfe'],
           'data':selector,
           'name':'cfg_id',
           'onchange':onchange}

       first=True
       for f in os.listdir(p):
           if f.startswith('config-') and f.endswith('.json'):
               pf=os.path.join(p,f)

               r=ck.load_json_file({'json_file':pf})
               if r['return']>0: return r

               d=r['dict']

               name=d['name']
               value=d['id']

               if cfg_id==value or (cfg_id=='' and first):
                   ii['selected_value']=value
                   # Merge meta with this dict
                   merge_dicts_and_append_lists({'dict1': dcfg, 'dict2': d})

                   data_config=dcfg['data_config']
                   cfg_id=value

               selector.append({'name':name, 'value':value})

               first=False

       r=ck.access(ii)
       if r['return']>0: return r

       html_selector='<center>\n'+r['html']+'\n</center>\n<div id="vspace8">\n'

    return {'return':0, 'dict':dcfg, 'cfg_id':cfg_id, 'data_config':data_config, 'html_selector':html_selector}

##############################################################################
# Merge intelligently dict1 with dict2 key by key in contrast with dict1.update(dict2)
#
# TARGET: end users

def merge_dicts_and_append_lists(i):
    """Merge intelligently dict1 with dict2 key by key in contrast with dict1.update(dict2)
       Target audience: end users

       It can merge sub-dictionaries and lists instead of substituting them

    Args:    
              dict1 (dict): merge this dict with dict2 (will be directly modified!)
              dict2 (dict): dict to be merged

    Returns:
              (dict): Unified CK dictionary:

                return (int): return code =  0, if successful
                                          >  0, if error
                (error) (str): error text if return > 0

                dict1 (dict): dict1 passed through the function

    """

    a = i['dict1']
    b = i['dict2']

    for k in b:
        v = b[k]
        if type(v) is dict:
            if k not in a:
                a.update({k: b[k]})
            elif type(a[k]) == dict:
                merge_dicts_and_append_lists({'dict1': a[k], 'dict2': b[k]})
            else:
                a[k] = b[k]
        elif type(v) is list:
            if k not in a:
               a[k] = []
            for y in v:
                a[k].append(y)
        else:
            a[k] = b[k]

    return {'return': 0, 'dict1': a}

##############################################################################
# convert experiment to result

def convert_experiment_to_result(i):
    """
    Input:  {
              dict (dict) - dict with flat experiment
              convertor (dict) - dict with convertor
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              table - output table
            }

    """

    table=[]

    d=i.get('dict',{})
    convertor=i.get('convertor',[])

    result={}

    if len(convertor)>0:
       for k in convertor:
           ok=k.get('out_key','')
           if ok=='': ok=k['key1']

           kk=[k.get('key1',''), k.get('key2',''), k.get('key3',''), k.get('key4','')]

           vv=''
           v=k.get('value','')
           if v!='' and v!=None:
              vv=v

           first=True
           for kx in kk:
               if kx!='':
                  v=d.get(kx)

                  vm=k.get('multiply',0)
                  if vm!=0 and vm!='' and vm!=None and (type(v)==float or type(v)==int):
                     v=v*vm

                  if v!='' and v!=None:
                     if first:
                        first=False
                        if type(v)==float or type(v)==int:
                           vv=0
                     else:
                        vv+=', '

                     # Check if list or dict
                     if type(v)==list or type(v)==dict:
                        vv=v
                     else:
                        vv+=v

           if vv!='':
              result[ok]=vv

    else:
       for k in d:
           result[k]=d[k]

    if len(result)>0:
       table.append(result)

    return {'return':0, 'table':table}

##############################################################################
# push result

def push(i):
    """
    Input:  {
              (data_uoa) - result data UOA
                or
              (tags) - find data entry to record via tags

              (user) - 'all' by default
              (point) - force point to append data (result-{point}.json)

              (dict) - result dict
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    repo_uoa=i.get('repo_uoa','')
    data_uoa=i.get('data_uoa','')
    tags=i.get('tags','')

    if data_uoa=='' and tags=='':
       return {'return':1, 'error':'data_uoa and tags are not defined'}
    
    # Find data entry if exists
    ii={'action':'search',
        'module_uoa':work['self_module_uid'],
        'repo_uoa':repo_uoa,
        'data_uoa':data_uoa,
        'tags':tags}
    r=ck.access(ii)
    if r['return']>0: return 

    lst=r['lst']

    if len(lst)>1:
       return {'return':1, 'error':'ambiguity: more than 1 result entry found'}

    if len(lst)==0:
       if data_uoa=='':
          return {'return':1, 'error':'you must specify data_uoa'}

       ii={'action':'add',
           'module_uoa':work['self_module_uid'],
           'repo_uoa':repo_uoa,
           'data_uoa':data_uoa,
           'tags':tags}
       r=ck.access(ii)
       if r['return']>0: return r

       path=r['path']
    else:
       path=lst[0]['path']

    # Get result dict
    dresult=i.get('dict',{})

    # Check user
    user=i.get('user','')
    if user=='': user='all'
    
    path_results=os.path.join(path, 'users', user)

    # Check if directory exists
    if not os.path.isdir(path_results):
       os.makedirs(path_results)

    # Which result file
    point=i.get('point','')
    if point=='': point='1'

    result_file='result-'+point+'.json'

    path_file=os.path.join(path_results, result_file)

    table=[]
    # Try to load file
    if os.path.isfile(path_file):
       r=ck.load_json_file({'json_file':path_file})
       if r['return']>0: return r

       table=r['dict']

    table.append(dresult)

    # Save back
    r=ck.save_json_to_file({'json_file':path_file, 'dict':table, 'sort_keys':'yes'})
    if r['return']>0: return r

    return {'return':0, 'path':path, 'path_file':path_file, 'table':table}
