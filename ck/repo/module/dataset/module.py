#
# Collective Knowledge (dataset)
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
# Import all files to meta

def import_all_files(i):
    """
    Input:  {
               data_uoa
               (repo_uoa)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    duoa=i['data_uoa']
    ruoa=i.get('repo_uoa','')

    r=ck.access({'action':'load',
                 'module_uoa':work['self_module_uid'],
                 'data_uoa':duoa,
                 'repo_uoa':ruoa})
    if r['return']>0: return r

    duid=r['data_uid']
    d=r['dict']
    p=r['path']

    if 'dataset_files' not in d: d['dataset_files']=[]
    dfiles=d['dataset_files']

    dirList=os.listdir(p)
    for fn in dirList:
         p1=os.path.join(p, fn)
         if os.path.isfile(p1):
            if fn not in dfiles:
               dfiles.append(fn)

    r=ck.access({'action':'update',
                 'module_uoa':work['self_module_uid'],
                 'data_uoa':duid,
                 'repo_uoa':ruoa,
                 'dict':d,
                 'substitute':'yes',
                 'sort_keys':'yes'})
    if r['return']>0: return r

    return {'return':0}

##############################################################################
# TBD: generate new data sets to cover unseen behavior
# See https://scholar.google.com/citations?view_op=view_citation&citation_for_view=IwcnpkwAAAAJ:hqOjcs7Dif8C
#     http://arxiv.org/abs/1506.06256

def generate(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    print ('TBD: generate new data sets to cover unseen behavior')

    ck.out('')
    ck.out('Command line: ')
    ck.out('')

    import json
    cmd=json.dumps(i, indent=2)

    ck.out(cmd)

    return {'return':0}

##############################################################################
# TBD: prune data sets to find minimal representative data set covering behavior
# See https://scholar.google.com/citations?view_op=view_citation&citation_for_view=IwcnpkwAAAAJ:hqOjcs7Dif8C
#     http://arxiv.org/abs/1506.06256

def prune(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    print ('prune data sets to find minimal representative data set covering behavior')

    ck.out('')
    ck.out('Command line: ')
    ck.out('')

    import json
    cmd=json.dumps(i, indent=2)

    ck.out(cmd)

    return {'return':0}

##############################################################################
# check size of all data sets and if less than threshold, add tag "small" - 
# needed not to send huge files during collaborative experiments (crowdtuning) via mobile devices

def check_size(i):
    """
    Input:  {
              (repo_uoa)        - repository UOA
              (data_uoa)        - dataset UOA (can be wildcards)

              (limit)           - size limit (to consider small). By default=500000
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              dict         - final dict with key 'features'={...} 
            }

    """

    import os
    import json

    o=i.get('out','')

    sl=i.get('limit','')
    if sl=='': sl=500000
    sl=int(sl)

    muoa=work['self_module_uid']
    duoa=i.get('data_uoa','')
    ruoa=i.get('repo_uoa','')

    rx=ck.access({'action':'search',
                  'repo_uoa':ruoa,
                  'module_uoa':muoa,
                  'data_uoa':duoa})
    if rx['return']>0: return rx

    lst=rx['lst']

    for q in lst:
        muid=q['module_uid']
        ruid=q['repo_uid']
        duid=q['data_uid']
        duoa=q['data_uoa']

        ck.out('Processing '+duoa+' ...')

        ii={'action':'load',
            'module_uoa':muid,
            'repo_uoa':ruid,
            'data_uoa':duid}

        rx=ck.access(ii) 
        if rx['return']>0: return rx

        dd=rx['dict']
        p=rx['path']

        dfiles=dd.get('dataset_files',[])
        tags=dd.get('tags',[])
        sz=0

        for df in dfiles:
            pp=os.path.join(p, df)
            if os.path.isfile(pp):
               sz+=os.path.getsize(pp) 

        x=''
        if sz<sl:
           x=' (SMALL)'

           if 'small' not in tags:
              tags.append('small')
              dd['tags']=tags

              ii['action']='update'
              ii['dict']=dd
              ii['sort_keys']='yes'
              ii['ignore_update']='yes'
              
              rx=ck.access(ii)
              if rx['return']>0: return rx

        ck.out('  Size: '+str(sz)+x)

    return {'return':0}

##############################################################################
# add file to a given dataset

def add_file_to(i):
    """
    Input:  {
              data_uoa   - dataset entry to add file to
              (repo_uoa) - repository of the entry
              file       - file to add
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import shutil
    import os

    o=i.get('out','')

    duoa=i.get('data_uoa','')
    muoa=i.get('module_uoa','')
    ruoa=i.get('repo_uoa','')

    fn=i.get('file','')

    if duoa=='' or fn=='':
       return {'return':1, 'error':'usage - ck add_file_to dataset:{dataset UOA} --file={filename}'}

    # Load entry
    r=ck.access({'action':'load',
                 'module_uoa':muoa,
                 'data_uoa':duoa,
                 'repo_uoa':ruoa})
    if r['return']>0: return r
    p=r['path']
    d=r['dict']

    # Copy file
    pn=os.path.join(p,fn)

    if o=='con':
       ck.out('Copying file '+fn+' to '+pn+' ...')

    shutil.copyfile(fn,pn)

    # Adding to dataset list
    df=d.get('dataset_files',[])
    df.append(fn)
    d['dataset_files']=df

    # Updating entry
    r=ck.access({'action':'update',
                 'module_uoa':muoa,
                 'data_uoa':duoa,
                 'repo_uoa':ruoa,
                 'dict':d,
                 'sort_keys':'yes'})
    if r['return']>0: return r

    return {'return':0}

##############################################################################
# add dataset 

def add(i):
    """
    Input:  {
               (tags) - use tags (string; tags separated by comma)
               (file) - add file
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    import os
    import shutil

    o=i.get('out','')

    duoa=i.get('data_uoa','')

    d=i.get('dict',{})

    # Check tags
    xtags=d.get('tags',[])
    if len(xtags)==0:
       tags=i.get('tags','').strip()
       if tags=='':
          if o=='con':
             rx=ck.inp({'text':'Enter tags for your data set separated by comma (such as image,jpeg): '})
             if rx['return']>0: return rx
             tags=rx['string'].strip()

       xtags=['dataset']
       for t in tags.split(','):
           t1=t.strip()
           if t1!='':
              if t1 not in xtags:
                 xtags.append(t1)

    d['tags']=xtags

    # Check files
    fn=i.get('file','')
    if fn!='':
       fn1=os.path.basename(fn)

       df=d.get('dataset_files',[])
       if fn1 not in df: 
          df.append(fn1)
       d['dataset_files']=df

    # Create entry
    i['dict']=d

    i['common_func']='yes'
    i['sort_keys']='yes'

    r=ck.access(i)
    if r['return']>0: return r
    p=r['path']

    # Copy file
    if fn!='':
       pn=os.path.join(p,fn1)

       if o=='con':
          ck.out('')
          ck.out('Copying file '+fn+' to '+pn+' ...')

       shutil.copyfile(fn,pn)

    return r
