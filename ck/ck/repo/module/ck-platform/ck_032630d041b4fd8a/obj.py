#
# Support for components
#
# Developer(s): Grigori Fursin, https://fursin.net
#

from . import config
from . import comm

import ck.kernel as ck

import json
import zipfile
import os
import time

skip_words_in_files=[
 'tmp',
 '.git',
 '.pyc',
 '__pycache__',
 '.cache'
]


##############################################################################
# Delete CK component from the portal if not permanent

def delete(i):

    """
    Input:  {
              cid [str] - CK CID of format (repo UOA:)module UOA:data UOA
            }

    Output: {
              return  [int]    - return code = 0 if success or >0 if error
              (error) [str]    - error string if return>0 
            }
    """

    # Get current directory (since will be changing it to get info about Git repo)
    cur_dir=os.getcwd()

    # Get current configuration
    r=config.load({})
    if r['return']>0: return r
    cfg=r['dict']

    # Check commands
    # Username ##########################################################
    username=cfg.get('username','')
    if i.get('username')!=None: username=i['username']

    if username=='' or username==None: 
       return {'return':1, 'error':'Username is not defined'}

    cfg['username']=username

    # API key ###########################################################        
    api_key=cfg.get('api_key','')

    if i.get('api_key')!=None: api_key=i['api_key']

    if api_key=='' or api_key==None: 
       return {'return':1, 'error':'API key is not defined'}

    cfg['api_key']=api_key

    # CID ###########################################################        
    cid=i.get('cid')

    if cid=='' or cid==None: 
       return {'return':1, 'error':'CK entry (CID) is not defined'}


    # Sending request to download
    r=comm.send({'config':cfg,
                 'action':'delete',
                 'dict':{
                   'cid':cid
                 }
                })
    if r['return']>0: return r

    ck.out('  Successfully deleted component(s) from the portal!')

    return {'return':0}

##############################################################################
# Publish CK component to the portal

def publish(i):

    """
    Input:  {
              cid [str] - CK CID of format (repo UOA:)module UOA:data UOA
                          (can use wildcards)
              (tags) [str] - search multiple CK components by these tags separated by comma
              (version) [str] - assign version
            }

    Output: {
              return  [int]    - return code = 0 if success or >0 if error
              (error) [str]    - error string if return>0 
            }
    """

    # Get current directory (since will be changing it to get info about Git repo)
    cur_dir=os.getcwd()

    # Get current configuration
    r=config.load({})
    if r['return']>0: return r
    cfg=r['dict']

    # Check commands
    # Username ##########################################################
    username=cfg.get('username','')
    if i.get('username')!=None: username=i['username']

    if username=='' or username==None: 
       return {'return':1, 'error':'Username is not defined'}

    cfg['username']=username

    # API key ###########################################################        
    api_key=cfg.get('api_key','')

    if i.get('api_key')!=None: api_key=i['api_key']

    if api_key=='' or api_key==None: 
       return {'return':1, 'error':'API key is not defined'}

    cfg['api_key']=api_key

    # CID ###########################################################        
    cid=i.get('cid')

    if cid=='' or cid==None: 
       return {'return':1, 'error':'CK entry (CID) is not defined'}

    tags=i.get('tags','')

    # Check if no module and use "solution" by default
    if cid.find(':')<0:
       cid='solution:'+cid

    # Version ###########################################################        
    version=i.get('version')
    if version=='' or version==None: 
       version='1.0.0'
       ck.out('Since --version is not defined, we use "1.0.0"')

    # Extra info about authors
    author=i.get('author','')
    if author==None: author=''

    author_id=i.get('author_id','')
    if author_id==None: author_id=''

    copyright=i.get('copyright','')
    if copyright==None: copyright=''

    license=i.get('license','')
    if license==None: license=''

    source=i.get('source','')
    if source==None: source=''

    sextra_tags=i.get('extra_tags','')
    if sextra_tags==None: sextra_tags=''

    quiet=i.get('quiet',False)
    force=i.get('force',False)
    permanent=i.get('permanent',False)

    # List CK components
    r=ck.access({'action':'search',
                 'cid':cid,
                 'tags':tags,
                 'add_info':'yes',
                 'add_meta':'yes',
                 'common_func':'yes'})
    if r['return']>0: return r

    lst=r['lst']
    llst=len(lst)

    if llst==0:
       ck.out('No CK objects found')

    num=0

    # Sort lst by modules and then data
    lst1=sorted(lst, key=lambda x: (x.get('repo_uoa',''), x.get('module_uoa',''), x.get('data_uoa','')))

    for obj in lst1:
        num+=1

        # Basic info about CK object
        repo_uoa=obj['repo_uoa']
        repo_uid=obj['repo_uid']

        module_uoa=obj['module_uoa']
        module_uid=obj['module_uid']

        data_uoa=obj['data_uoa']
        data_uid=obj['data_uid']

        # Print info
        ck.out(str(num)+' out of '+str(llst)+') '+repo_uoa+':'+module_uoa+':'+data_uoa)

        # Check name and date
        data_name=obj.get('info',{}).get('data_name','')
        if data_name==data_uoa: data_name=''

        data_meta=obj['meta']
        if data_name=='':
           if data_meta.get('misc',{}).get('title','')!='':
              data_name=data_meta['misc']['title']

        data_date=''
        if data_meta.get('misc',{}).get('date','')!='':
           data_date=data_meta['misc']['date']

        source2=data_meta.get('source','')
        if source2=='': source2=source

        license2=data_meta.get('license','')
        if license2=='': license2=license

        copyright2=data_meta.get('copyright','')
        if copyright2=='': copyright2=copyright

        # Specialize per specific modules
        not_digital_component=False
        extra_dict={}
        extra_tags=[]

        if module_uoa=='module':
           extra_dict['last_module_actions']=[]
           actions=data_meta.get('actions',{})
           for a in actions:
               extra_dict['last_module_actions'].append(a+' '+data_uoa)

        elif module_uoa=='lib':
           not_digital_component=True
           extra_tags=['library']

           if 'reproduced-papers' in data_meta.get('tags',[]):
              extra_tags.append('reproduced-papers')

           data_meta2=data_meta.get('meta',{})

           if data_name=='':
              data_name=data_meta2.get('title','')

           all_authors=data_meta2.get('authors','')
           if all_authors!='':
              extra_dict['all_authors']=[]
              for aa in all_authors.split(','):
                  if aa!='': aa=aa.strip()
                  if aa!='':
                     extra_dict['all_authors'].append(aa)

           for k in ['badge_acm_artifact_available', 'badge_acm_artifact_functional',
                     'badge_acm_artifact_reusable', 'badge_acm_results_replicated',
                     'badge_acm_results_reproduced']:
               if data_meta2.get(k,'')=='yes':
                  extra_tags.append(k)

        elif module_uoa=='event' or module_uoa=='repo':
           not_digital_component=True

        # Get info of the first creation
        first_creation=obj['info'].get('control',{})

        # Load info about repo
        repo_dict={}

        if not force and repo_uoa=='local' and module_uoa!='repo': # Normally skip everything from local unless we publish repos themselves
           ck.out('     SKIPPED')
           continue 

        if module_uoa=='repo':
           if not force and data_uoa=='local':
              ck.out('     SKIPPED')
              continue 

           repo_dict=obj['meta']

        elif repo_uoa!='default' and repo_uoa!='local':
           r=ck.access({'action':'load',
                        'repo_uoa':config.CK_CFG_REPO_UOA,
                        'module_uoa':config.CK_CFG_MODULE_REPO_UOA,
                        'data_uoa':repo_uid,
                        'common_func':'yes'})
           if r['return']>0: return r
           repo_dict=r['dict']
           if 'path' in repo_dict:
              del(repo_dict['path'])

        # Generate temp file to pack
        r=ck.gen_tmp_file({'prefix':'obj-', 'suffix':'.zip'})
        if r['return']>0: return r

        fn=r['file_name']

        # Pack component
        p=obj['path']

        zip_method=zipfile.ZIP_DEFLATED

        ii={'path':p, 'all':'yes'}

        # Prune files for solution
        if module_uoa=='solution':
           ii['ignore_names']=['CK','venv']

        r=ck.list_all_files(ii)
        if r['return']>0: return r

        fl=r['list']

        # Write archive
        try:
          f=open(fn, 'wb')
          z=zipfile.ZipFile(f, 'w', zip_method)
          for fx in fl:
              add=True
              for k in skip_words_in_files:
                  if k in fx:
                     add=False
                     break

              if add:
                 p1=os.path.join(p, fx)
                 z.write(p1, fx, zip_method)
          z.close()
          f.close()

        except Exception as e:
           return {'return':1, 'error':'failed to prepare archive ('+format(e)+')'}

        # Check size
        statinfo = os.stat(fn)
        pack_size=statinfo.st_size

        # Check problems with repository or components
        x=''
        if repo_dict.get('remote','')=='yes':
           x+='remote repo;'
        if repo_dict.get('private','')=='yes':
           x+='private repo;'
        if repo_dict.get('url','')=='' and repo_uoa!='default':
           x+='repo not shared;'
        if pack_size>config.PACK_SIZE_WARNING:
           x+='pack size ('+str(pack_size)+') > '+str(config.PACK_SIZE_WARNING)+';'

        skip_component=False
        if not force and x!='':
           if quiet:
              skip_component=True
           else:
              r=ck.inp({'text':'  This component has potential issues ('+x+'). Skip processing (Y/n)? '})
              if r['return']>0: return r
              s=r['string'].strip()
              if s=='' or s=='Y' or s=='y':
                 skip_component=True

        if skip_component:
           ck.out('    SKIPPED ('+x+')')

           if os.path.isfile(fn):
              os.remove(fn)

           continue

        # Convert to MIME to send over internet
        r=ck.convert_file_to_upload_string({'filename':fn})
        if r['return']>0: return r

        pack64=r['file_content_base64']

        if os.path.isfile(fn):
           os.remove(fn)

        # Check workspaces
        lworkspaces=[]
        workspaces=i.get('workspaces','')
        if workspaces!=None:
           lworkspaces=workspaces.strip().split(',')

        # Get extra info about repo
        os.chdir(p)

        repo_info={}

        if repo_dict.get('private','')!='yes':
           repo_info={'publish_repo_uoa':repo_uoa,
                      'publish_repo_uid':repo_uid}

           # Get current Git URL
           r=ck.run_and_get_stdout({'cmd':['git','config','--get','remote.origin.url']})
           if r['return']==0 and r['return_code']==0: 
              x=r['stdout'].strip()
              if x!='': repo_info['remote_git_url']=x

           # Get current Git branch
           r=ck.run_and_get_stdout({'cmd':['git','rev-parse','--abbrev-ref','HEAD']})
           if r['return']==0 and r['return_code']==0: 
              x=r['stdout'].strip()
              if x!='': repo_info['remote_git_branch']=x

           # Get current Git checkout
           r=ck.run_and_get_stdout({'cmd':['git','rev-parse','--short','HEAD']})
           if r['return']==0 and r['return_code']==0: 
              x=r['stdout'].strip()
              if x!='': repo_info['remote_git_checkout']=x

           repo_info['dict']=repo_dict

        # Add extra tags
        for et in sextra_tags.split(','):
            et=et.strip().lower()
            if et!='':
               extra_tags.append(et)

        #TBD: owner, version, info about repo
        # Sending request
        r=comm.send({'config':cfg,
                     'action':'publish',
                     'ownership':{
                       'private':i.get('private', False),
                       'workspaces':lworkspaces
                     },
                     'dict':{
                       'publish_module_uoa':module_uoa,
                       'publish_module_uid':module_uid,
                       'publish_data_uoa':data_uoa,
                       'publish_data_uid':data_uid,
                       'publish_data_name':data_name,
                       'publish_data_date':data_date,
                       'publish_pack':pack64,
                       'publish_pack_size':pack_size,
                       'repo_info':repo_info,
                       'first_creation':first_creation,
                       'version':version,
                       'author':author,
                       'author_id':author_id,
                       'copyright':copyright2,
                       'license':license2,
                       'source':source2,
                       'not_digital_component':not_digital_component,
                       'extra_dict':extra_dict,
                       'extra_tags':extra_tags,
                       'permanent':permanent
                     }
                    })
        if r['return']>0: 
           ck.out('    WARNING: Portal API returned error: '+r['error'])
        else:
           data_uid=r['data_uid']
           ck.out('    cK component ID:  '+data_uid)
           purl=r.get('url','')
           if purl!='':
              ck.out('    cK component URL: '+purl)

    os.chdir(cur_dir)

    return {'return':0}

##############################################################################
# List versions of a given CK component at the portal

def versions(i):

    """
    Input:  {
              cid [str] - CK CID of format (repo UOA:)module UOA:data UOA
            }

    Output: {
              return  [int]    - return code = 0 if success or >0 if error
              (error) [str]    - error string if return>0 
            }
    """

    # Get current configuration
    r=config.load({})
    if r['return']>0: return r
    cfg=r['dict']

    # CID ###########################################################        
    cid=i.get('cid')

    if cid=='' or cid==None: 
       return {'return':1, 'error':'CK entry (CID) is not defined'}

    # Parse CID
    r=ck.parse_cid({'cid':cid})
    if r['return']>0: return r

    data_uoa=r.get('data_uoa','')
    module_uoa=r.get('module_uoa','')

    # Call Portal API
    r=comm.send({'config':cfg,
                 'action':'list_versions',
                 'dict':{
                   'module_uoa':module_uoa,
                   'data_uoa':data_uoa
                 }
                })
    if r['return']>0: return r

    versions=r.get('versions',[])
    for v in versions:
        vv=v.get('version','')
        dt=v.get('iso_datetime','').replace('T',' ')

        ck.out(vv+' ('+dt+')')

    return r

##############################################################################
# Open portal with a given CK component

def open_page(i):

    """
    Input:  {
              cid [str] - CK CID of format (repo UOA:)module UOA:data UOA
            }

    Output: {
              return  [int]    - return code = 0 if success or >0 if error
              (error) [str]    - error string if return>0 
            }
    """

    # Get current configuration
    r=config.load({})
    if r['return']>0: return r
    cfg=r['dict']

    # URL
    url=cfg.get('server_url','')
    if url!='':
       h=url.find('api/')
       if h>0:
          url=url[:h]
       else:
          url=''

    if url=='':
       url=config.CR_DEFAULT_SERVER

    # CID ###########################################################        
    cid=i.get('cid')

    if cid=='' or cid==None: 
       return {'return':1, 'error':'CK entry (CID) is not defined'}

    # Parse CID
    r=ck.parse_cid({'cid':cid})
    if r['return']>0: return r

    data_uoa=r.get('data_uoa','')
    module_uoa=r.get('module_uoa','')

    # Form URL
    url+='c/'+module_uoa+'/'+data_uoa

    ck.out('Opening web page '+url+' ...')

    import webbrowser
    webbrowser.open(url)

    return {'return':0}

##############################################################################
# Download CK component from the portal to the local repository

def download(i):

    """
    Input:  {
              components - pre-loaded components from bootstrapping
               or
              cid [str] - CK CID of format (repo UOA:)module UOA:data UOA
                          (can use wildcards)


              (version) [str] - assign version
              (force) [bool] - if True, force download even if components already exists

              (tags) [str] - can search by tags (usually soft/package)

              (all) [bool] - if True, download dependencies (without force!)
            }

    Output: {
              return  [int]    - return code = 0 if success or >0 if error
              (error) [str]    - error string if return>0 
            }
    """

    sbf=os.environ.get('CB_SAVE_BOOTSTRAP_FILES','')

    force=i.get('force')
    al=i.get('all')

    skip_module_check=i.get('skip_module_check',False)

    tags=i.get('tags','')

    spaces=i.get('spaces','')

    lst=i.get('components',[])

    rr={'return':0}
 
    if len(lst)>0:
       preloaded=True
       msg='Processing'
       msg2='processed'
       skip_module_check=True

       repo_uoa='local'

       ck.cfg['check_missing_modules']='no' # Important not to check missing modules!
    else:
       preloaded=False
       msg='Downloading'
       msg2='downloaded'

       # CID ###########################################################        
       cid=i.get('cid')
       if cid=='' or cid==None: 
          return {'return':1, 'error':'CK entry (CID) is not defined'}

       version=i.get('version')
       if version==None: version=''

        # Parse CID
       r=ck.parse_cid({'cid':cid})
       if r['return']>0: return r

       repo_uoa=r.get('repo_uoa','')
       data_uoa=r.get('data_uoa','')
       module_uoa=r.get('module_uoa','')

       # Get current configuration
       r=config.load({})
       if r['return']>0: return r
       cfg=r['dict']

       # Sending request to download
       rr=comm.send({'config':cfg,
                     'action':'download',
                     'dict':{
                       'module_uoa':module_uoa,
                       'data_uoa':data_uoa,
                       'version':version,
                       'tags':tags
                     }
                    })
       if rr['return']>0: 
          return rr

       lst=rr['components']

    for l in lst:

        furl=l['file_url']
        fsize=l['file_size']

        fmd5=l['file_md5']

        muoa=l['module_uoa']
        muid=l['module_uid']

        duoa=l['data_uoa']
        duid=l['data_uid']

        dependencies=l.get('dependencies',[])

        xcid=muoa+':'+duoa

        ck.out('* '+msg+' CK component "'+xcid+'" ('+str(fsize)+' bytes)')

        # Check if module exists
        if not skip_module_check:
           r=ck.access({'action':'find',
                        'module_uoa':'module',
                        'data_uoa':muoa,
                        'common_func':'yes'})
           if r['return']>0:
              if r['return']!=16: return r

              x='module:'+muoa
              if repo_uoa!='': x=repo_uoa+':'+x

# FGG: we should not add "version" for dependencies or related components since it's not the same!
#              r=download({'cid':x, 'force':force, 'version':version, 'skip_module_check':True, 'all':al})

              r=download({'cid':x, 'force':force, 'skip_module_check':smc, 'all':al})
              if r['return']>0: return r

        # Check if entry already exists
        path=''
        r=ck.access({'action':'find',
                     'common_func':'yes',
                     'repo_uoa':repo_uoa,
#                     'module_uoa':muid,
                     'module_uoa':muoa,
                     'data_uoa':duoa})
        if r['return']==0:
           if not force:
              return {'return':8, 'error':'     Already exists locally ("'+xcid+'")'}
        else:
           if r['return']!=16: return r

           r=ck.access({'action':'add',
                        'common_func':'yes',
                        'repo_uoa':repo_uoa,
#                        'module_uoa':muid,
                        'module_uoa':muoa,
                        'data_uoa':duoa,
                        'data_uid':duid,
                        'ignore_update':'yes'})
           if r['return']>0: return r

        path=r['path']

        # Prepare pack
        ppz=os.path.join(path, config.PACK_FILE)

        if os.path.isfile(ppz):
#           if not force:
#              return {'return':1, 'error':'pack file already exists ('+ppz+')'}
           os.remove(ppz)

        # Download and save pack to file
        tstart=time.time()
        fpack64=l.get('file_base64','')

        if fpack64!='':
           rx=ck.convert_upload_string_to_file({'file_content_base64':fpack64, 'filename':ppz})
           if rx['return']>0: return rx
        else:
           rx=comm.download_file({'url':furl, 'file':ppz})
           if rx['return']>0: return rx

        # Save boostrap info (debug)
        if sbf!='':
           rx=ck.convert_file_to_upload_string({'filename':ppz})
           if rx['return']>0: return rx
           l['file_base64']=rx['file_content_base64']
 
        # MD5 of the pack
        rx=ck.load_text_file({'text_file':ppz, 'keep_as_bin':'yes'})
        if rx['return']>0: return rx
        bpack=rx['bin']

        import hashlib
        md5=hashlib.md5(bpack).hexdigest()

        if md5!=fmd5:
           return {'return':1, 'error':'MD5 of the newly created pack ('+md5+') did not match the one from the portal ('+fmd5+')'}

        # Unpack to src subdirectory
        import zipfile

        f=open(ppz,'rb')
        z=zipfile.ZipFile(f)
        for d in z.namelist():
            if d!='.' and d!='..' and not d.startswith('/') and not d.startswith('\\'):
               pp=os.path.join(path,d)
               if d.endswith('/'):
                  # create directory
                  if not os.path.exists(pp): os.makedirs(pp)
               else:
                  ppd=os.path.dirname(pp)
                  if not os.path.exists(ppd): os.makedirs(ppd)

                  # extract file
                  fo=open(pp, 'wb')
                  fo.write(z.read(d))
                  fo.close()

                  if pp.endswith('.sh') or pp.endswith('.bash'):
                     import stat
                     st=os.stat(pp)
                     os.chmod(pp, st.st_mode | stat.S_IEXEC)

        f.close()

        tstop=time.time()-tstart

        # Remove pack file
        os.remove(ppz)

        # Note
        if not preloaded:
           ck.out(spaces+'    Successfully '+msg2+' ('+('%.2f' % tstop)+' sec)!') # to '+path)

        # Check deps
        if al:
           if len(dependencies)>0:
              ck.out(spaces+'  Checking dependencies ...')

           for dep in dependencies:
               muoa=dep.get('module_uid','')
               duoa=dep.get('data_uid','')

               tags=dep.get('tags',[])
               xtags=''
               if len(tags)>0:
                  xtags=','.join(tags)
                  muoa='package'
                  duoa=''

               cid=muoa+':'+duoa
               rx=download({'cid':cid,
                            'all':al,
                            'tags':xtags,
                            'spaces':spaces+'    '})
               if rx['return']>0 and rx['return']!=8 and rx['return']!=16: return rx
               if rx['return']==16:
                  if xtags=='': return rx
                  rx=download({'cid':'soft:',
                               'all':al,
                               'tags':xtags,
                               'spaces':spaces+'    '})
                  if rx['return']>0 and rx['return']!=8: return rx

    return rr
