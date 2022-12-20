#
# Support for graphs
#
# Developer(s): Grigori Fursin, https://fursin.net
#

from . import config
from . import comm
from . import obj

import ck.kernel as ck

import json
import os
import copy

meta_template={
    "meta": {
      "scenario": "universal",
      "scenario_uid": "3bf7371412455a8f",
      "viz_engine": "ck_beta"
    },
    "tags": [
      "result"
    ]
  }

desc_template={
  "data_config": {
    "default_key_x": "x",
    "default_key_y": "y",
    "default_sort_key": "x",
    "table_view": [
      {
        "key": "x",
        "name": "X",
        "type": "int"
      },
      {
        "key": "y",
        "name": "Y",
        "format": "%.2f",
        "type": "float"
      },
      {
        "key": "submitter",
        "name": "Submitter"
      }
    ]
  }
}

extra_info_desc=[{'key':'copyright', 'name':'copyright (optional)'},
                 {'key':'license', 'name':'license (optional)'},
                 {'key':'author', 'name':'author (optional)'},
                 {'key':'author_email', 'name':'author email (optional)'},
                 {'key':'author_webpage', 'name':'author webpage (optional)'}]

##############################################################################
# Initialize a graph on a portal

def init(i):

    """
    Input:  {
              uid [str] - graph identifyer
              (version) [str] - graph version
              (desc_file) [str] - file with graph description
              (tags) [str] - tags separated by comma
            }

    Output: {
              return  [int]    - return code = 0 if success or >0 if error
              (error) [str]    - error string if return>0 

              dict    [dict]   - configuration dictionary
              path    [str]    - path to CK cfg entry
            }
    """

    # Get main configuration
    r=config.load({})
    if r['return']>0: return r
    cfg=r.get('dict',{})
    pcfg=r.get('path','')

    # CID ###########################################################        
    uid=i['uid']
    if uid==None: uid=''

    version=i.get('version')
    if version==None: version=''

    desc_file=i.get('desc_file','')
    if desc_file==None: desc_file=''

    # If UID!='', check if already exists ...
    found=False
    meta=meta_template
    path=''
    data_name=''
    tags=[]
    meta_info=''
    source=''
    extra_info={}

    if uid!='':
       r=ck.access({'action':'load',
                    'module_uoa':'result',
                    'data_uoa':uid})
       if r['return']>0:
          if r['return']!=16: return r
       else:
          found=True
          meta=r['dict']
          path=r['path']
          data_name=r['data_name']

          tags=meta.get('tags',[])
          source=meta.get('source','')
          meta_info=meta.get('meta',{}).get('info','')

          extra_info=r['info'].get('control',{})

    # Check if init from scratch and no title
    if i.get('name')!=None and i.get('name','')!='':
       data_name=i['name'].strip()
    elif not found or data_name=='':
       r=ck.inp({'text':'Select a title for your graph: '})
       if r['return']>0: return r

       data_name=r['string'].strip()

       meta['meta']['title']=data_name

    # Check if init from scratch and no title
    if not found or meta_info=='':
       r=ck.inp({'text':'Enter general info about your graph: '})
       if r['return']>0: return r

       x=r['string'].strip()

       if x=='': x=' '

       meta['meta']['info']=x

    # Adding tags
    if i.get('tags')!=None and i.get('tags','')!='':
       xtags=i['tags'].strip().split(',')

       for t in xtags:
           t1=t.strip()
           if t1!='' and t1 not in tags:
              tags.append(t1)

       meta['tags']=tags

    elif not found or (len(tags)==1 and 'result' in tags):
       r=ck.inp({'text':'Enter tags for your graph separated by commas: '})
       if r['return']>0: return r

       xtags=r['string'].strip().split(',')

       for t in xtags:
           t1=t.strip()
           if t1!='' and t1 not in tags:
              tags.append(t1)

       meta['tags']=tags

    # Checking source
    if not found or source=='':
       r=ck.inp({'text':'Enter source of results for your graph (can be URL): '})
       if r['return']>0: return r

       source=r['string'].strip()

       meta['source']=source

    # Checking authors
    for x in extra_info_desc:
        k=x['key']
        n=x['name']

        if not found or extra_info.get(k,'')=='':
           r=ck.inp({'text':'Enter '+n+': '})
           if r['return']>0: return r

           s=r['string'].strip()

           extra_info[k]=s

    # Creating/updating graph
    a='add'
    if found: a='update'

    ii={'action':a,
        'module_uoa':'result',
        'data_uoa':uid,
        'dict':meta,
        'sort_keys':'yes',
        'data_name':data_name,
        'substitute':'yes',
        'extra_info':extra_info}

    r=ck.access(ii)
    if r['return']>0: return r

    data_uoa=r['data_uoa']
    data_uid=r['data_uid']
    path=r['path']

    x='initialized'
    if found: x='updated'

    ck.out('Graph was successfully '+x+':')
    ck.out('')
    ck.out('  CK UID:  '+data_uid)
    ck.out('  CK name: '+data_uoa)
    ck.out('  CK path: '+path)

    # Add desc
    p1=os.path.join(path, 'desc.json')

    dt=copy.deepcopy(desc_template)
    if desc_file!='':
       rx=ck.load_json_file({'json_file':desc_file})
       if rx['return']>0: return rx
       dx=rx['dict']
       dt['data_config'].update(dx)

    if desc_file!='' or not os.path.isfile(p1):
       rx=ck.save_json_to_file({'json_file':p1, 'dict':dt, 'sort_keys':'yes'})
       if rx['return']>0: return rx

    p2=os.path.join(path, '.cm', 'meta.json')

    ck.out('')
    ck.out('You can continue updating graph using following files: ')
    ck.out('')
    ck.out('  Graph general meta info: '+p1)
    ck.out('     See example at '+config.CR_DEFAULT_SERVER+'/result/sota-mlperf-inference-results-v0.5-open-available/?action=download&filename=.cm/meta.json')
    ck.out('')
    ck.out('  Graph axes info: '+p2)
    ck.out('     See example at '+config.CR_DEFAULT_SERVER+'/result/sota-mlperf-inference-results-v0.5-open-available/?action=download&filename=desc.json')

    # Need to publish
    ck.out('')
    rx=ck.inp({'text':'Publish graph on the portal (Y/n)?'})
    if rx['return']>0: return rx
    s=rx['string'].strip().lower()

    if s=='' or s=='y':
       ck.out('')
       r=obj.publish({'cid':'result:'+data_uoa,
                      'version':version,
                      'force':True})

    else:
       ck.out('')
       ck.out('You can publish your graph on the portal using the following commands when ready: ')
       ck.out('')
       ck.out('  cb publish result:'+data_uoa+' --version=1.0.0 --force (--private)')

    return r

##############################################################################
# Push result to a graph on a portal

def push(i):

    """
    Input:  {
              uid [str] - graph identifyer
              (version) [str] - graph version
              (filename) [str] - JSON file with results
              (json) [str] - JSON string from command line (use ' instead of ")
              (point) [str] - specific point name to add/update
            }

    Output: {
              return  [int]    - return code = 0 if success or >0 if error
              (error) [str]    - error string if return>0 

              dict    [dict]   - configuration dictionary
              path    [str]    - path to CK cfg entry
            }
    """

    # CID ###########################################################        
    uid=i['uid']
    if uid=='':
       return {'return':1, 'error':'graph UID is not defined!'}

    version=i.get('version')
    if version==None: version=''

    filename=i.get('filename','')
    json_string=i.get('json','')

    if filename=='' and json_string=='':
       return {'return':1, 'error':'either "filename" or "json" should define results to be pushed'}

    point=i.get('point','')

    # Prepare data
    data=[]

    if filename!='':
       r=ck.load_json_file({'json_file':filename})
       if r['return']>0: return r

       data2=r['dict']
       if type(data2)==dict:
          data2=[data2]

       data+=data2

    if json_string!='':
       import json

       json_string=json_string.replace("'", '"')

       data2=json.loads(json_string)

       if type(data2)==dict:
          data2=[data2]

       data+=data2

    # Send request
    r=config.load({})
    if r['return']>0: return r
    cfg=r['dict']

    # Check if username and API_Key are empty and then use default crowd-user ...
    username=cfg.get('username','')
    if username=='' or username==None:
       cfg['username']=config.CR_DEFAULT_SERVER_USER
       cfg['api_key']=config.CR_DEFAULT_SERVER_API_KEY

    # Sending request to download
    r=comm.send({'config':cfg,
                 'action':'push_result',
                 'dict':{
                   'data_uoa':uid,
                   'version':version,
                   'point':point,
                   'data':data
                 }
                })
    if r['return']>0: return r
    url=r.get('url','')

    ck.out('  Successfully pushed your point to a graph!')
    if url!='':
       ck.out('    URL: '+url)

    return r
