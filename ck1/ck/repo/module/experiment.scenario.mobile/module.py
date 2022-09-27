#
# Collective Knowledge (experiment scenarios to be executed on Android during crowdsourcing)
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
# get scenarios depending on user's mobile device features

def get(i):
    """
    Input:  {
              (data_uoa)
              (repo_uoa)

              (platform_features)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              scenarios    - list of scenarios and related files
            }

    """

    import copy

    pf=i.get('platform_features',{})

    abi=pf.get('cpu',{}).get('cpu_abi','')

    os_name=pf.get('os',{}).get('name','')
    os_ver=[]
    j=os_name.find(' ')
    if j>0:
        os_ver=os_name[j+1:].strip().split('.')

    duoa=i.get('data_uoa','')
    ruoa=i.get('repo_uoa','')

    r=ck.access({'action':'search',
                 'module_uoa':work['self_module_uid'],
                 'data_uoa':duoa,
                 'repo_uoa':ruoa,
                 'add_meta':'yes'})
    if r['return']>0: return r

    lst=r['lst']

    nlst=[]

    # Prepare URL from CK server
    rx=ck.access({'action':'form_url_prefix',
                  'module_uoa':'wfe',
                  'host':i.get('host',''), 
                  'port':i.get('port',''), 
                  'template':i.get('template','')})
    if rx['return']>0: return rx
    url0=rx['url']

    # Calculate total size
    for q in sorted(lst, key=lambda x: x.get('meta',{}).get('title','')):
        add=True

        meta=q['meta']

        if meta.get('skip','')!='yes' and meta.get('outdated','')!='yes':
            sabi=meta.get('supported_abi',[])
            if abi!='' and abi not in sabi:
                add=False

            if add:
                min_os_ver=meta.get('min_os_ver',[])
                # TBD: need to check all digits
                if len(min_os_ver)>0 and len(os_ver)>0 and os_ver[0]<min_os_ver[0]:
                    add=False

            if add:
                # Check engine_meta ->
                em=meta.get('engine_meta',{}).get(abi,{})
                if em>0:
                   meta['engine_meta_dict']=copy.deepcopy(em)
                   del(meta['engine_meta'])

                ff=meta.get('files',[])

                # Go through files and update
                nff=[]
                tfs=0 # Total file size

                for f in ff:
                    sabi=f.get('supported_abi',[])
                    if len(sabi)==0 or abi=='' or abi in sabi:
                        url=f.get('url','')
                        if url=='':
                            path=f.get('path','')
                            fn=f.get('filename','')

                            dduoa=q['data_uid']
                            if f.get('from_data_uoa','')!='':
                                dduoa=f['from_data_uoa']

                            url=url0+'action=pull&common_action=yes&cid='+q['module_uoa']+':'+dduoa+'&filename='+path+'/'+fn

                        f['url']=url
                        nff.append(f)

                        fs=int(f.get('file_size',0))
                        tfs+=fs

                q['total_file_size']=tfs

                tfs=int(tfs/1E6)

                if tfs>0:
                    title=meta.get('title','')
                    if title!='':
#                        title+=' ('+str(tfs+1)+' MB)'
                        meta['title']=title

                meta['files']=nff

                nlst.append(q)

    # Sort by title
    snlst=nlst
#[]
#    for q in sorted(nlst, key=lambda x: (x.get('total_file_size',0),x.get('meta',{}).get('title',''))):
#    for q in sorted(nlst, key=lambda x: x.get('meta',{}).get('title','')):
#        snlst.append(q)

#    ck.save_json_to_file({'json_file':'/tmp/xyz888.json','dict':snlst})

    return {'return':0, 'scenarios':snlst}

##############################################################################
# process all scenarios (check files, get md5, get length)

def process(i):
    """
    Input:  {
              (data_uoa)
              (repo_uoa)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    duoa=i.get('data_uoa','')
    ruoa=i.get('repo_uoa','')

    r=ck.access({'action':'search',
                 'module_uoa':work['self_module_uid'],
                 'data_uoa':duoa,
                 'repo_uoa':ruoa,
                 'add_meta':'yes'})
    if r['return']>0: return r

    lst=r['lst']

    nlst=[]

    # Prepare URL from CK server
    rx=ck.access({'action':'form_url_prefix',
                  'module_uoa':'wfe',
                  'host':i.get('host',''), 
                  'port':i.get('port',''), 
                  'template':i.get('template','')})
    if rx['return']>0: return rx
    url0=rx['url']

    for q in lst:
        meta=q['meta']

        if meta.get('outdated','')=='yes':
           continue

        ck.out('Processing '+q['data_uoa']+' ...')

        ff=meta.get('files',[])

        # Go through files and update
        for f in ff:
            fn=f.get('filename','')
            ck.out('  '+fn)

            url=f.get('url','')
            if url=='':
                p=f.get('path','')

                if not p.startswith('code') and not p.startswith('data'):
                   j1=p.find('code/')
                   if j1<0:
                      j1=p.find('data/')
                   if j1>0:
                      p=p[j1:]
                      f['path']=p

                md5x=f.get('md5','')

                dduoa=q['data_uid']
                if f.get('from_data_uoa','')!='':
                   dduoa=f['from_data_uoa']

                # Get path
                r=ck.access({'action':'load',
                             'data_uoa':dduoa,
                             'module_uoa':q['module_uoa']})
                if r['return']>0: return r

                pp=os.path.join(r['path'],p,fn)

                if not os.path.isfile(pp):
                    return {'return':1, 'error':'file ('+pp+') not found'}

                # Check MD5 sum
                md5=''

                r=ck.run_and_get_stdout({'cmd':'md5sum < '+pp})
                if r['return']>0: return r

                s=r['stdout'].split(' ')
                if len(s)>0:
                    md5=s[0]
                    if len(md5)>0 and md5.startswith('\\'):
                        md5=md5[1:]

                f['md5']=md5

                # Get file size
                fs=os.path.getsize(pp)
                f['file_size']=fs

                ck.out('    File size = '+str(fs))
                ck.out('    MD5       = '+md5)

        # Update entry
        r=ck.access({'action':'update',
                     'module_uoa':q['module_uid'],
                     'data_uoa':q['data_uid'],
                     'dict':meta,
                     'substitute':'yes',
                     'sort_key':'yes',
                     'ignore_update':'yes'})
        if r['return']>0: return r

    return {'return':0, 'scenarios':nlst}
