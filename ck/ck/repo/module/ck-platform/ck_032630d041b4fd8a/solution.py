#
# Support for portable solutions
#
# Developer(s): Grigori Fursin
#               Herve Guillou
#

from . import config
from . import comm
from . import obj
from . import graph

import ck.kernel as ck

import json
import zipfile
import os
import locale

############################################################################
# Get some parameters of a local platform

def get_platform_desc(i):

    # Get platform info
    # Check host/target OS/CPU
    hos=i.get('host_os','')
    tos=i.get('target_os','')
    tdid=i.get('device_id','')

    # Get some info about platforms
    ii={'action':'detect',
        'module_uoa':'platform.os',
        'host_os':hos,
        'target_os':tos,
        'device_id':tdid}

    if i.get('skip_info_collection','')!='':
       ii['skip_info_collection']=i['skip_info_collection']

    r=ck.access(ii)
    if r['return']>0: return r

    hosd=r['host_os_dict']
    host_os_name=hosd.get('ck_name3','')
    if host_os_name=='': 
       host_os_name=hosd.get('ck_name2','')
       if host_os_name=='win': host_os_name='windows'

    if host_os_name=='': 
       return {'return':1, 'error':'your CK OS component is outdated! Try "ck pull repo:ck-env"'}

    # Extra info
    host_desc={}

    if host_os_name=='windows':
       host_desc['extra_cmd']='call '
       host_desc['venv_bin']='Scripts'
       host_desc['venv_activate']='activate.bat'
       host_desc['python_bin']='python.exe'
       host_desc['activate_cmd']='cmd'
    else:
       host_desc['extra_cmd']=''
       host_desc['venv_bin']='bin'
       host_desc['venv_activate']='activate'
       host_desc['python_bin']='python'
       host_desc['activate_cmd']='bash'

    r['host_desc']=host_desc

    return r

############################################################################
# Initialize solution (portable workflow)
#  Try to download existing one from the platform
#  If doesn't exist, initialize the new one locally

def init(i):
    """
    Input:  {
              uid [str] - platform identifier of the solution
            }

    Output: {
              return  [int]    - return code = 0 if success or >0 if error
              (error) [str]    - error string if return>0 
            }
    """

    # Save current directory
    cur_dir=os.getcwd()

    # Get main configuration
    r=config.load({})
    if r['return']>0: return r
    cfg=r.get('dict',{})
    pcfg=r.get('path','')

    # Get platform info 
    ck.out(config.CR_LINE)
    ck.out('Detecting minimal platform info ...')

    i['skip_info_collection']='yes'
    rplat=get_platform_desc(i) # Pass input from init
    if rplat['return']>0: return rplat

    hos=rplat['host_os_uid']
    hosx=rplat['host_os_uoa']
    hosd=rplat['host_os_dict']
    hosd_extra=rplat['host_desc']

    hplat=hosd['ck_name']

    tos=rplat['os_uid']
    tosx=rplat['os_uoa']
    tosd=rplat['os_dict']

    tdid=rplat.get('device_id','')

    resume=i.get('resume')
    if resume==None: resume=False

    # Get solution UID
    uid=i['uid']
    if uid==None: 
       r=ck.gen_uid({})
       if r['return']>0: return r
       uid=r['data_uid']

    # Check if entry already exists
    ii={'action':'load',
        'module_uoa':config.CR_MODULE_UOA,
        'data_uoa':uid}
    r=ck.access(ii)
    if r['return']==0: 
       p=r['path']
       px=os.path.join(p, '.cm', 'meta.json')

       dd=r['dict']

       ck.out(config.CR_LINE)
       ck.out("Preloaded solution meta from "+px)
    else:
       if r['return']!=16: return r

       ck.out(config.CR_LINE)
       r=ck.out('Solution "'+uid+'" is not found locally. Attempting to download from the portal ...')

       dd = {}

       r=obj.download({'cid':'local:solution:'+uid})
       if r['return']>0: 
          if r['return']!=16: return r

          ck.out('')
          r=ck.inp({'text':'Warning: solution was not found on the portal. Do you want to initialize the new one (Y/n): '})
          if r['return']>0: return r

          x=r['string'].strip()
          if x=='n' or x=='N':
             return {'return':16, 'error':'Solution was not found on the portal'}

       else:
          ii={'action':'load',
              'module_uoa':config.CR_MODULE_UOA,
              'data_uoa':uid}
          r=ck.access(ii)
          if r['return']>0: return r

          p=r['path']
          px=os.path.join(p, '.cm', 'meta.json')

          dd=r['dict']

          ck.out(config.CR_LINE)
          ck.out("Preloaded solution meta from "+px)

    # Get extra vars
    workflow=i.get('workflow','')
    if workflow=='': workflow=dd.get('workflow','')

    workflow_repo_url=i.get('workflow_repo_url','')
    if workflow_repo_url=='': workflow_repo_url=dd.get('workflow_repo_url','')

    workflow_cmd=i.get('workflow_cmd','')
    if workflow_cmd=='': workflow_cmd=dd.get('workflow_cmd','')

    workflow_cmd_before=i.get('workflow_cmd_before','')
    if workflow_cmd_before=='': workflow_cmd_before=dd.get('workflow_cmd_before','')

    workflow_cmd_after=i.get('workflow_cmd_after','')
    if workflow_cmd_after=='': workflow_cmd_after=dd.get('workflow_cmd_after','')

    workflow_cmd_extra=i.get('workflow_cmd_extra','')
    if workflow_cmd_extra=='': workflow_cmd_extra=dd.get('workflow_cmd_extra','')

    workflow_input=i.get('workflow_input','')
    if workflow_input=='': workflow_input=dd.get('workflow_input','')

    workflow_input_dir=i.get('workflow_input_dir','')
    if workflow_input_dir=='': workflow_input_dir=dd.get('workflow_input_dir','')

    workflow_output_dir=i.get('workflow_output_dir','')
    if workflow_output_dir=='': workflow_output_dir=dd.get('workflow_output_dir','')

    python_version=i.get('python_version','')
    #    if python_version!='':
    #       i['python_version_from']=python_version
    #       i['python_version_to']=python_version

    python_version_from=i.get('python_version_from','')
    if python_version_from=='': python_version_from=dd.get('python_version_from','')
    if python_version_from==' ': python_version_from=''

    python_version_to=i.get('python_version_to','')
    if python_version_to=='': python_version_to=dd.get('python_version_to','')
    if python_version_to==' ': python_version_to=''

    # Check graphs
    graphs=i.get('graphs','')
    if graphs=='': 
       graphs=dd.get('graphs',[])
    else:
       graphs=graphs.split(',')
       i['graphs']=graphs

    tos=i.get('target_os','')
    if tos=='': tos=dd.get('target_os','')

    # Update meta and create entry for a solution
    name=i.get('name','')
    tags=i.get('tags','')

    for k in ['host_os', 'target_os', 'device_id', 'hostname',
              'workflow', 'workflow_repo_url', 
              'workflow_cmd_before', 'workflow_cmd_after',
              'workflow_cmd', 'workflow_cmd_extra', 'workflow_input', 
              'workflow_input_dir', 'workflow_output_dir', 'result_file',
              'python_version', 'python_version_from', 'python_version_to',
              'graphs']:
        v=i.get(k)
        if v!=None and v!='':
           dd[k]=v

    #    dd['detected_platform_info']=rplat

    dd['tags']=["solution"]

    from . import __version__
    dd['client_version']=__version__

    # Check if extra meta
    add_extra_meta_from_file=i.get('add_extra_meta_from_file','')
    if add_extra_meta_from_file!='':
       r=ck.load_json_file({'json_file':add_extra_meta_from_file})
       if r['return']>0: return r
       dd.update(r['dict'])

    # Add/update CK entry for the solution
    update_dict={'action':'update',
                 'module_uoa':config.CR_MODULE_UOA,
                 'data_uoa':uid,
                 'dict':dd,
                 'sort_keys':'yes'}
    if name!='': update_dict['data_name']=name
    if tags!='': 
       dd['tags']+=tags.split(',')

    r=ck.access(update_dict)
    if r['return']>0: return r

    solution_uoa=r['data_uoa']
    solution_uid=r['data_uid']

    p=r['path']

    ck.out(config.CR_LINE)
    ck.out('Path to the solution: '+p)

    ##############################################################
    # Process graph description
    desc_graph=i.get('desc_graph','')
    if desc_graph!='':
       ##############################################################
       # Graphs
       ck.out(config.CR_LINE)
       ck.out('Initializing graphs:')

       if not os.path.isfile(desc_graph):
          return {'return':1, 'error':'can\'t find file "'+desc_graph+'"'}

       r=ck.load_json_file({'json_file':desc_graph})
       if r['return']>0: return r

       d=r['dict']

       pdesc=os.path.join(p, 'graph-desc.json')

       r=ck.save_json_to_file({'json_file':pdesc, 'dict':d, 'sort_keys':'yes'})
       if r['return']>0: return r

# Decided to add all graphs explicitly!
#       if solution_uoa not in graphs:
#          graphs.append(solution_uoa)

       sgi=i.get('skip_graph_init')
       if sgi!=None and not sgi:
          for gr in graphs:
              ck.out('')
              ck.out(' * Graph: '+gr)
              ck.out('')

              r=graph.init({'uid':gr, 'version':'1.0.0', 'desc_file':desc_graph})
              if r['return']>0: return r

    ##############################################################
    # Process graph convertor
    graph_convertor=i.get('graph_convertor','')
    if graph_convertor!='':
       ##############################################################
       # Graphs
       ck.out(config.CR_LINE)
       ck.out('Processing graph convertor:')

       if not os.path.isfile(graph_convertor):
          return {'return':1, 'error':'can\'t find file "'+graph_convertor+'"'}

       r=ck.load_json_file({'json_file':graph_convertor})
       if r['return']>0: return r

       d=r['dict']

       pconv=os.path.join(p, 'graph-convertor.json')

       r=ck.save_json_to_file({'json_file':pconv, 'dict':d, 'sort_keys':'yes'})
       if r['return']>0: return r

    ##############################################################
    # Init virtual environment
    ck.out(config.CR_LINE)
    ck.out('Setting (virtual) environment...')

    cmd0=hosd['change_dir']+' '+hosd['env_quotes_if_space']+p+hosd['env_quotes_if_space']+'\n'
    cmd0+=hosd['env_set']+' CK_REPOS='+hosd['env_quotes_if_space']+os.path.join(p, 'CK')+hosd['env_quotes_if_space']+'\n'

    python_path=i['python_path']

    encoding=locale.getdefaultlocale()[1]

    ii={'action':'shell',
        'module_uoa':'os',
        'encoding':encoding,
        'output_to_console':'yes'}

    if resume:
       if i['python_localenv'] is True:
             cmd0+=hosd['env_call']+' '+hosd['env_quotes_if_space']+os.path.join(p, 
                  'venv', 
                  hosd_extra['venv_bin'], 
                  hosd_extra['venv_activate'])+hosd['env_quotes_if_space']+'\n'

    else:
       if python_path=='':
         # Searching for python 
         ck.out('')
         ck.out('  Searching for the python installation')

         if python_version_from!='' and python_version_from!=' ':
            ck.out('    Version must be >= '+python_version_from+' (change with --python_version_from="version")')
         if python_version_from!='' and python_version_from!=' ':
            ck.out('    Version must be <= '+python_version_to+' (change with --python_version_to="version")')

         r=ck.access({'action':'detect',
                     'module_uoa':'soft',
                     'data_uoa':'compiler.python',
                     'version_from':python_version_from,
                     'version_to':python_version_to,
                     'out':'con'})
         if r['return']>0: return r

         r=ck.access({'action':'load',
                     'module_uoa':'env',
                     'data_uoa':r['env_data_uid']})
         if r['return']>0: return r
         python_path=r['dict']['env']['CK_ENV_COMPILER_PYTHON_FILE']

         ck.out(config.CR_LINE)

       cmd=cmd0
       if i['python_localenv'] is True:
         i_env=ck.inp({'text':'Do you want to create a new virtual environment (Y/n): '})
         if i_env['return']>0: return i_env

         x_env=i_env['string'].strip()

         if x_env=='n' or x_env=='N':
           i['python_localenv'] = False
         else:
           ck.out('creating virtual env')
           cmd+='virtualenv --python='+python_path+' venv\n'

       ii['cmd']=cmd

       print (config.CR_LINE)
       print ('Running the following commands to install the virtual env:')
       print ('')
       print (cmd)
       print (config.CR_LINE)

       r=ck.access(ii)
       if r['return']>0: return r

       ##############################################################
       # Install CK
       ck.out(config.CR_LINE)
       ck.out('Installing CK ...')

       if i['python_localenv'] is True:
             cmd0+=hosd['env_call']+' '+hosd['env_quotes_if_space']+os.path.join(p, 
                  'venv', 
                  hosd_extra['venv_bin'], 
                  hosd_extra['venv_activate'])+hosd['env_quotes_if_space']+'\n'

       cmd=cmd0
       cmd+='pip install ck\n'
       cmd+='\n'
       cmd+=hosd_extra['extra_cmd']+'ck\n'

       ii['cmd']=cmd
       r=ck.access(ii)
       if r['return']>0: return r

       ##############################################################
       # Initializing CB config ...
       ck.out(config.CR_LINE)
       ck.out('Initializing cBench client for this solution ...')

       if pcfg!='' and os.path.isdir(pcfg):
          pcfg2=os.path.join(pcfg, '.cm', 'meta.json')
          if os.path.isfile(pcfg2):
             rx=ck.gen_tmp_file({'prefix':'ck-tmp-', 'suffix':'.json'})
             if rx['return']>0: return rx

             pfn=rx['file_name']

             rx=ck.save_json_to_file({'json_file':pfn, 'dict':{'dict':cfg}})
             if rx['return']>0: return rx 

             # Update CB cfg of the solution
             cmd=cmd0
             cmd+='ck update cfg:'+config.CK_CFG_DATA_UOA+' @'+pfn+'\n'

             ck.out('')
             ck.out(cmd)

             ii['cmd']=cmd
             r=ck.access(ii)

             if os.path.isfile(pfn):
                os.remove(pfn)

             if r['return']>0: return r

#       ##############################################################
#       # Downloading CK components
#       ck.out(config.CR_LINE)
#       ck.out('Downloading CK components from the portal ...')
#       ck.out('')
#
#       ck_components=config.CR_SOLUTION_CK_COMPONENTS
#
#       cmd=cmd0
#
#       for x in ck_components:
#           cmd+='\n'
#           cmd+='cb download '+x['cid']
#           if x.get('version','')!='':
#              cmd+=' --version='+x['version']
#           cmd+=' --force\n'
#           if hplat=='linux':
#              cmd+='if [[ $? != 0 ]]; then exit 1 ; fi\n'
#
#       ii['cmd']=cmd
#
#       r=ck.access(ii)
#       if r['return']>0: return r
#       rc=r['return_code']
#       if rc>0:
#          return {'return':99, 'error':'last command returned error'}

       ##############################################################
       # Downloading CK components
       ck.out(config.CR_LINE)
       ck.out('Extra bootstrap of stable CK components for this solution ...')
       ck.out('')

       ck_components=config.CR_SOLUTION_CK_COMPONENTS

       cmd=cmd0

       cmd+='\n'
       cmd+='cb update --force\n'
       if hplat=='linux':
          cmd+='if [[ $? != 0 ]]; then exit 1 ; fi\n'

       ii['cmd']=cmd

       r=ck.access(ii)
       if r['return']>0: return r
       rc=r['return_code']
       if rc>0:
          return {'return':99, 'error':'last command returned error'}

       ##############################################################
       # Install ck-env repo and detect python
       ck.out(config.CR_LINE)
       ck.out('Installing ck-env repo and detecting compiler ...')

       cmd=cmd0
       cmd+=hosd_extra['extra_cmd']+'ck set kernel var.install_to_env=yes\n'
       #    Now downloading from the portal
       #    cmd+=hosd_extra['extra_cmd']+'ck pull repo:ck-env\n'
       cmd+=hosd_extra['extra_cmd']+'ck detect soft:compiler.python --quiet --full_path='+hosd['env_quotes_if_space']+os.path.join(p,
              'venv',
              hosd_extra['venv_bin'], 
              hosd_extra['python_bin'])+hosd['env_quotes_if_space']+'\n'

       ii['cmd']=cmd
       r=ck.access(ii)
       if r['return']>0: return r

       ##############################################################
       # Pull workflow repo
       if workflow_repo_url==None or workflow_repo_url=='':
          return {'return':1, 'error':'workflow_repo_url is not defined'}

       if workflow_repo_url!='local':
          ck.out(config.CR_LINE)
          ck.out('Installing workflow repo ...')

          cmd=cmd0
          cmd+=hosd_extra['extra_cmd']+'ck pull repo --url='+workflow_repo_url+'\n'

          ii['cmd']=cmd
          r=ck.access(ii)
          if r['return']>0: return r

       ##############################################################
       # Copy extra scripts if needed
       es=i.get('add_extra_scripts','')
       if es!='':
          ck.out(config.CR_LINE)
          ck.out('Copying extra scripts ...')

          import glob
          import shutil

          ck.out('')
          for fl in glob.glob(es):
              ck.out('  * '+fl)
              shutil.copy(fl, p)

       ##############################################################
       # Describe workflow preparation steps
       desc_prereq=i.get('desc_prereq','')
       prereq_workflow=dd.get('prereq_workflow',[])
       if desc_prereq!='':
          if not os.path.isfile(desc_prereq):
             return {'return':1, 'error':'can\'t find file "'+desc_prereq+'"'}

          r=ck.load_text_file({'text_file':desc_prereq, 'split_to_list':'yes'})
          if r['return']>0: return r

          prereq_workflow=r['lst']

          ck.out('')
          ck.out('')
          ck.out('***************************************************')
          ck.out('***************************************************')
          ck.out('Prequisite steps:')

          ck.out('')
          for s in prereq_workflow:
              ck.out('  '+s)

          dd['prereq_workflow']=prereq_workflow

          update_dict['dict']=dd
          r=ck.access(update_dict)
          if r['return']>0: return r

          if not i.get('skip_stop',False):
             ck.out('')
             ck.out('***************************************************')
             ck.out('***************************************************')
             ck.out('We start virtual env to let you install above deps!')
             ck.out('Enter "exit" to continue solution preparation:')
             ck.out('***************************************************')
             ck.out('***************************************************')
             ck.out('')
             ck.out('')

             cmd=cmd0
             cmd+=hosd['env_call']+' '+hosd['env_quotes_if_space']+os.path.join(p, 'venv', hosd_extra['venv_bin'], hosd_extra['venv_activate'])+hosd['env_quotes_if_space']+'\n'
             cmd+=hosd_extra['activate_cmd']+'\n'

             ii['cmd']=cmd
             r=ck.access(ii)
             if r['return']>0: return r

    ##############################################################
    ck.out(config.CR_LINE)
    ck.out('Detecting complete platform info ...')

    pinfo=os.path.join(p, 'platform-info.json')
    if os.path.isfile(pinfo): os.remove(pinfo)

    cmd=cmd0

    # Need to do it from virtual env since it's the correct way for Android devices which may require specific files (adb)
    s='ck detect platform'
    if i.get('target_os','')!='': s+=' --target_os='+i['target_os']
    if tdid!='': s+=' --device_id='+tdid
    s+=' --out=json_file --out_file='+pinfo

    cmd+=s+'\n'

    ii['cmd']=cmd
    print (cmd)
    r=ck.access(ii)
    if r['return']>0: return r

    if not os.path.isfile(pinfo):
       return {'return':1, 'error':'platform info file was not created'}

    #    # Get some info about platforms
    #    ii={'action':'detect',
    #        'module_uoa':'platform',
    #        'host_os':hos,
    #        'target_os':tos,
    #        'device_id':tdid}
    #    r=ck.access(ii)
    #    if r['return']>0: return r
    #
    #    rx=ck.save_json_to_file({'json_file':pinfo, 'dict':r, 'sort_keys':'yes'})
    #    if rx['return']>0: return rx
    #
    ##############################################################
    ck.out(config.CR_LINE)
    ck.out('Detecting complete platform host OS info ...')

    pinfo2=os.path.join(p, 'platform-host-os-info.json')
    if os.path.isfile(pinfo2): os.remove(pinfo2)

    cmd=cmd0

    # Need to do it from virtual env since it's the correct way for Android devices which may require specific files (adb)
    s='ck detect platform.os'
    s+=' --out=json_file --out_file='+pinfo2

    cmd+=s+'\n'

    ii['cmd']=cmd
    r=ck.access(ii)
    if r['return']>0: return r

    if not os.path.isfile(pinfo2):
       return {'return':1, 'error':'platform info file was not created'}

    ##############################################################
    if i.get('update_meta_and_stop','')==True:
       ck.out(config.CR_LINE)
       ck.out('Skipping the rest by user request')
       return {'return':0}

    ##############################################################
    # Describe workflow preparation steps
    ck.out(config.CR_LINE)
    ck.out('Preparation steps:')
    ck.out('')

    desc_prepare=i.get('desc_prepare','')
    prepare_workflow=dd.get('prepare_workflow',[])
    if desc_prepare!='':
       if not os.path.isfile(desc_prepare):
          return {'return':1, 'error':'can\'t find file "'+desc_prepare+'"'}

       r=ck.load_text_file({'text_file':desc_prepare, 'split_to_list':'yes'})
       if r['return']>0: return r

       prepare_workflow=r['lst']

       for s in prepare_workflow:
           ck.out('  '+s)

       dd['prepare_workflow']=prepare_workflow

       update_dict['dict']=dd
       r=ck.access(update_dict)
       if r['return']>0: return r

    for s in prepare_workflow:
        if s=='': 
           ck.out('')
           continue

        ck.out(config.CR_LINE)
        ck.out(s)
        ck.out('')

        cmd=cmd0
        cmd+=s+'\n'
        if hplat=='linux':
           cmd+='if [[ $? != 0 ]]; then exit 1 ; fi\n'

        ii['cmd']=cmd
        r=ck.access(ii)
        if r['return']>0: return r

        rc=r['return_code']
        if rc>0:
           return {'return':99, 'error':'last command returned error'}

    ##############################################################
    # Check dependencies
    ck.out(config.CR_LINE)
    ck.out('Checking and recording workflow dependencies')

    pdeps=os.path.join(p, 'resolved-deps.json')

    s=''

    if workflow_cmd_before!='': s+=workflow_cmd_before+'\n'

    s+=hosd_extra['extra_cmd']+'ck run '+workflow+' --cmd_key='+workflow_cmd+' '+workflow_cmd_extra+' --record_deps="'+pdeps+'" --skip_exec'

    if hos!='': s+=' --host_os='+hos
    if tos!='': s+=' --target_os='+tos
    if tdid!='': s+=' --device_id='+tdid

    s+='\n'

#    Here we do not need post-processing (often fail)
#    if workflow_cmd_after!='': s+=workflow_cmd_after+'\n'

    ck.out('')
    ck.out(s)

    ck.out('')
    cmd=cmd0
    cmd+=s+'\n'

    if hplat=='linux':
      cmd+='if [[ $? != 0 ]]; then exit 1 ; fi\n'

    ii['cmd']=cmd
    r=ck.access(ii)
    if r['return']>0: return r

    rc=r['return_code']
    if rc>0:
      return {'return':99, 'error':'last command returned error'}

    ##############################################################
    # Describe workflow run steps
    ck.out(config.CR_LINE)
    ck.out('Run steps:')
    ck.out('')

    desc_run=i.get('desc_run','')
    run_workflow=dd.get('run_workflow',[])
    if desc_run!='':
      if not os.path.isfile(desc_run):
        return {'return':1, 'error':'can\'t find file "'+desc_run+'"'}

      r=ck.load_text_file({'text_file':desc_run, 'split_to_list':'yes'})
      if r['return']>0: return r

      run_workflow=r['lst']

      for s in run_workflow:
          ck.out('  '+s)

      dd['run_workflow']=run_workflow

      update_dict['dict']=dd
      r=ck.access(update_dict)
      if r['return']>0: return r

    for s in run_workflow:
      if s=='': 
        ck.out('')
        continue

      ck.out(config.CR_LINE)
      ck.out('Command:  '+s)
      ck.out('')

      cmd=cmd0
      cmd+=s+'\n'

      ii['cmd']=cmd
      r=ck.access(ii)
      if r['return']>0: return r

    ##############################################################
    # Check dependencies
    ck.out(config.CR_LINE)
    ck.out('Solution was successfully prepared!')

    ck.out('')
    ck.out('You can crowd-benchmark this solution (if supported) as follows:')
    ck.out('cb benchmark '+uid)

    ck.out('')
    ck.out('You can run this solution locally as follows:')
    ck.out('cb run '+uid)

    ck.out('')
    ck.out('You can activate virtual env for this solution to debug/improve it as follows:')
    ck.out('cb activate '+uid)

    return {'return':0}

############################################################################
# Activate virtual environment for a solution

def activate(i):
    """
    Input:  {
              uid [str] - portal identifier of the solution
            }

    Output: {
              return  [int]    - return code = 0 if success or >0 if error
              (error) [str]    - error string if return>0 
            }
    """

    cur_dir=os.getcwd()

    # Check if Windows or Linux
    # Get platform info 
    r=get_platform_desc(i) # Pass input from init
    if r['return']>0: return r

    hos=r['host_os_uid']
    hosx=r['host_os_uoa']
    hosd=r['host_os_dict']
    hosd_extra=r['host_desc']

    tos=r['os_uid']
    tosx=r['os_uoa']
    tosd=r['os_dict']

    # Load entry with the solution
    uid=i['uid']

    r=ck.access({'action':'load',
                 'module_uoa':config.CR_MODULE_UOA,
                 'data_uoa':uid})
    if r['return']>0: return r

    p=r['path']

    ##############################################################
    ck.out(config.CR_LINE)
    ck.out('Activate solution: '+p)
    ck.out('')

    cmd0=hosd['change_dir']+' '+hosd['env_quotes_if_space']+p+hosd['env_quotes_if_space']+'\n'
    cmd0+=hosd['env_set']+' CK_REPOS='+hosd['env_quotes_if_space']+os.path.join(p, 'CK')+hosd['env_quotes_if_space']+'\n'

    cmd=cmd0
    cmd+=hosd['env_call']+' '+hosd['env_quotes_if_space']+os.path.join(p, 'venv', hosd_extra['venv_bin'], hosd_extra['venv_activate'])+hosd['env_quotes_if_space']+'\n'
    cmd+=hosd_extra['activate_cmd']+'\n'

    encoding=locale.getdefaultlocale()[1]

    ii={'action':'shell',
        'module_uoa':'os',
        'cmd':cmd,
        'encoding':encoding,
        'output_to_console':'yes'}

    r=ck.access(ii)
    if r['return']>0: return r

    return {'return':0}

############################################################################
# Run prepared solution

def run(i):

    """
    Input:  {
              uid [str] - Portal identifier of the solution
            }

    Output: {
              return  [int]    - return code = 0 if success or >0 if error
              (error) [str]    - error string if return>0 
            }
    """

    # Get main configuration
    r=config.load({})
    if r['return']>0: return r
    cfg=r.get('dict',{})
    pcfg=r.get('path','')

    cur_dir=os.getcwd()

    # Check if Windows or Linux
    # Get platform info 
    r=get_platform_desc(i) # Pass input from init
    if r['return']>0: return r

    hos=r['host_os_uid']
    hosx=r['host_os_uoa']
    hosd=r['host_os_dict']
    hosd_extra=r['host_desc']

    tos=r['os_uid']
    tosx=r['os_uoa']
    tosd=r['os_dict']

    tdid=r.get('device_id','')

    xcmd=i.get('cmd','')
    if xcmd==None: xcmd=''
    xcmd=xcmd.strip()

    # Load entry with the solution
    uid=i['uid']

    r=ck.access({'action':'load',
                 'module_uoa':config.CR_MODULE_UOA,
                 'data_uoa':uid})
    if r['return']>0: return r

    p=r['path']
    dd=r['dict']

    # TBD: need to be checked from outside ...
    # host_os=dd.get('host_os','')
    tos=dd.get('target_os','')
    tdid=dd.get('device_id','')

    workflow=dd.get('workflow','')
    workflow_cmd_before=dd.get('workflow_cmd_before','')
    workflow_cmd_after=dd.get('workflow_cmd_after','')
    workflow_cmd=dd.get('workflow_cmd','')
    workflow_cmd_extra=dd.get('workflow_cmd_extra','')

    workflow_input_dir=dd.get('workflow_input_dir','')
    workflow_output_dir=dd.get('workflow_output_dir','')

    ##############################################################
    ck.out(config.CR_LINE)
    ck.out('Run solution: '+p)
    ck.out('')

    cmd0=hosd['change_dir']+' '+hosd['env_quotes_if_space']+p+hosd['env_quotes_if_space']+'\n'
    cmd0+=hosd['env_set']+' CK_REPOS='+hosd['env_quotes_if_space']+os.path.join(p, 'CK')+hosd['env_quotes_if_space']+'\n'

    cmd=cmd0
    cmd+=hosd['env_call']+' '+hosd['env_quotes_if_space']+os.path.join(p, 'venv', hosd_extra['venv_bin'], hosd_extra['venv_activate'])+hosd['env_quotes_if_space']+'\n'

    if workflow_cmd_before!='': cmd+=workflow_cmd_before+'\n'

    if xcmd!='':
      s=xcmd
    else:
      s=hosd_extra['extra_cmd']+'ck run '+workflow+' --cmd_key='+workflow_cmd

      if workflow_cmd_extra!='':
        s+=' '+workflow_cmd_extra

      if hos!='': s+=' --host_os='+hos
      if tos!='': s+=' --target_os='+tos
      if tdid!='': s+=' --device_id='+tdid

    cmd+=s+'\n'

    if workflow_cmd_after!='': cmd+=workflow_cmd_after+'\n'

    ck.out('')
    ck.out(s)
    ck.out('')

    encoding=locale.getdefaultlocale()[1]

    ii={'action':'shell',
        'module_uoa':'os',
        'cmd':cmd,
        'encoding':encoding,
        'output_to_console':'yes'}
    r=ck.access(ii)
    if r['return']>0: return r

    return r


############################################################################
# Benchmark prepared solution

def benchmark(i):

    """
    Input:  {
              uid [str] - Portal identifier of the solution
            }

    Output: {
              return  [int]    - return code = 0 if success or >0 if error
              (error) [str]    - error string if return>0 
            }
    """
    import datetime
    import time 

    # Get main configuration
    r=config.load({})
    if r['return']>0: return r
    cfg=r.get('dict',{})
    pcfg=r.get('path','')

    sdate= datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    t = time.time()

    cur_dir=os.getcwd()

    # Check if Windows or Linux
    # Get platform info 
    r=get_platform_desc(i) # Pass input from init
    if r['return']>0: return r

    hos=r['host_os_uid']
    hosx=r['host_os_uoa']
    hosd=r['host_os_dict']
    hosd_extra=r['host_desc']

    tos=r['os_uid']
    tosx=r['os_uoa']
    tosd=r['os_dict']

    tdid=r.get('device_id','')

    xcmd=i.get('cmd','')
    if xcmd==None: xcmd=''
    xcmd=xcmd.strip()

    # Load entry with the solution
    uid=i['uid']

    r=ck.access({'action':'load',
                 'module_uoa':config.CR_MODULE_UOA,
                 'data_uoa':uid})
    if r['return']>0: return r

    solution_uoa=r['data_uoa']
    solution_uid=r['data_uid']

    p=r['path']
    dd=r['dict']

    # TBD: need to be checked from outside ...
    # host_os=dd.get('host_os','')
    tos=dd.get('target_os','')
    tdid=dd.get('device_id','')

    workflow=dd.get('workflow','')
    workflow_cmd_before=dd.get('workflow_cmd_before','')
    workflow_cmd_after=dd.get('workflow_cmd_after','')
    workflow_cmd=dd.get('workflow_cmd','')
    workflow_cmd_extra=dd.get('workflow_cmd_extra','')

    workflow_input_dir=dd.get('workflow_input_dir','')
    workflow_output_dir=dd.get('workflow_output_dir','')

    result_file=dd.get('result_file','')

    graphs=dd.get('graphs',[])

    ##############################################################
    ck.out(config.CR_LINE)
    ck.out('Find path to output file '+result_file+' ...')
    ck.out('')

    encoding=locale.getdefaultlocale()[1]

    cmd0=hosd['change_dir']+' '+hosd['env_quotes_if_space']+p+hosd['env_quotes_if_space']+'\n'
    cmd0+=hosd['env_set']+' CK_REPOS='+hosd['env_quotes_if_space']+os.path.join(p, 'CK')+hosd['env_quotes_if_space']+'\n'
    cmd0+=hosd['env_call']+' '+hosd['env_quotes_if_space']+os.path.join(p, 'venv', hosd_extra['venv_bin'], hosd_extra['venv_activate'])+hosd['env_quotes_if_space']+'\n'

    cmd=cmd0
    cmd+='ck find '+workflow+'\n'

    ii={'action':'shell',
        'module_uoa':'os',
        'cmd':cmd,
        'encoding':encoding}
    r=ck.access(ii)
    if r['return']>0: 
      status=-1
      return r

    path_result=r['stdout'].strip()
    path_result_file=os.path.join(path_result, result_file)

    ck.out('  Found path: '+path_result_file)

    ##############################################################
    ck.out(config.CR_LINE)
    ck.out('Detecting complete platform info ...')

    pinfo=os.path.join(p, 'platform-info.json')
    if os.path.isfile(pinfo): os.remove(pinfo)

    cmd=cmd0

    # Need to do it from virtual env since it's the correct way for Android devices which may require specific files (adb)
    s='ck detect platform'
    if tos!='': s+=' --target_os='+tos
    if tdid!='': s+=' --device_id='+tdid
    s+=' --out=json_file --out_file='+pinfo

    cmd+=s+'\n'

    ii['cmd']=cmd
    r=ck.access(ii)
    if r['return']>0: return r

    if not os.path.isfile(pinfo):
       return {'return':1, 'error':'platform info file was not created'}

    # Get some sub-info about deps and platforms
    dinfo={}
    if os.path.isfile(pinfo):
       r=ck.load_json_file({'json_file':pinfo})
       if r['return']==0:
          dinfo=r['dict'].get('features',{})
          for k in ['cpu_misc', 'cpu']:
              if k in dinfo: del(dinfo[k])

    pdeps=os.path.join(p, 'resolved-deps.json')
    ddeps={}
    if os.path.isfile(pdeps):
       r=ck.load_json_file({'json_file':pdeps})
       if r['return']==0:
          ddeps2=r['dict']

          r=deps_summary({'deps':ddeps2})
          if r['return']==0:
             ddeps=r['deps_summary']

    ##############################################################
    # status management

    path_tmpSol=os.path.join(p, "tmp")
    tmp_solStatus=os.path.join(path_tmpSol, "status.json")

    status = 0
    if not os.path.isdir(path_tmpSol): 
      os.mkdir(path_tmpSol)

    rdf_st={}
    rx=ck.load_json_file({'json_file':tmp_solStatus})
    if rx['return']>0: 
      rx=ck.save_json_to_file({'json_file':tmp_solStatus, 'dict':{'status': 0}})
      if rx['return']>0: return rx
    else:
      rdf_st=rx['dict']
      status = rdf_st.get('status','')

    run=True
    if status == 1:
      run=False
    elif status == 2:
      # To be done try to push the result to server 
      status=1

    rdf_st['status'] = 1
    rx=ck.save_json_to_file({'json_file':tmp_solStatus, 'dict':rdf_st})
    if rx['return']>0: return rx

    if os.path.isfile(path_result_file):
      ck.out('  Cleaning output ...')
      os.remove(path_result_file)

    ##############################################################
    rr={'return':0}
    if run is True:

      ck.out(config.CR_LINE)
      ck.out('Run solution: '+p)
      ck.out('')

      cmd=cmd0

      if workflow_cmd_before!='': cmd+=workflow_cmd_before+'\n'

      if xcmd!='':
        s=xcmd
      else:
        s=hosd_extra['extra_cmd']+'ck benchmark '+workflow+' --cmd_key='+workflow_cmd

        if workflow_cmd_extra!='':
          s+=' '+workflow_cmd_extra

        if hos!='': s+=' --host_os='+hos
        if tos!='': s+=' --target_os='+tos
        if tdid!='': s+=' --device_id='+tdid
      ck.out(config.CR_LINE)
      ck.out('Command: '+s)
      ck.out('')

      cmd+=s+'\n'

      if workflow_cmd_after!='': cmd+=workflow_cmd_after+'\n'

      ck.out('')
      ck.out(s)
      ck.out('')

      ii={'action':'shell',
          'module_uoa':'os',
          'cmd':cmd,
          'encoding':encoding,
          'output_to_console':'yes'}
      rr=ck.access(ii)

      if r['return']>0: 
        rdf_st['status'] = -1
        rx=ck.save_json_to_file({'json_file':tmp_solStatus, 'dict':rdf_st})
        if rx['return']>0: return rx
        return r
      else :
        rdf_st['status'] = 2
        rx=ck.save_json_to_file({'json_file':tmp_solStatus, 'dict':rdf_st})
        if rx['return']>0: return rx

      elapsed = time.time() - t

      ##############################################################
      ck.out(config.CR_LINE)
      ck.out('Reading output: '+path_result_file)
      ck.out('')

      if not os.path.isfile(path_result_file):
        ck.out('  Error: output file not found!')
        rdf_st['status'] = -2
        rx=ck.save_json_to_file({'json_file':tmp_solStatus, 'dict':rdf_st})
        if rx['return']>0: return rx
      else:
        rx=ck.load_json_file({'json_file':path_result_file})
        if rx['return']>0: return rx

        rd=rx['dict']

        # Add solution info
        rd['solution_uoa']=solution_uoa
        rd['solution_uid']=solution_uid
        rd['solution_run_date']=sdate
        rd['solution_duration']=elapsed

        sworkflow=workflow.split(':')
        if len(sworkflow)>1:
           rd['program_workflow_uoa']=sworkflow[1]

        from . import __version__
        rd['client_version']=__version__

        rx=ck.flatten_dict({'dict':rd})
        if rx['return']>0: return rx

        rdf=rx['dict']
        crdf={}

        crdf['platform_info']=dinfo
        crdf['resolved_deps']=ddeps

        # Remove first ## (do not need here)
        for k in rdf:
          v=rdf[k]
          if k.startswith('##'): k=k[2:]
          crdf[k]=v

        # Get some sub-info about deps and platforms
        if os.path.isfile(pinfo):
           r=ck.load_json_file({'json_file':pinfo})
           if r['return']==0:
              dx=r['dict']

        pdeps=os.path.join(p, 'resolved-deps.json')
        if os.path.isfile(pdeps):
           rx=ck.load_json_file({'json_file':pdeps})
           if rx['return']==0:
              dx=rx['dict']

        ck.out(json.dumps(crdf, indent=2))

        #over write the file 
        rx=ck.save_json_to_file({'json_file':path_result_file, 'dict':crdf})
        if rx['return']>0: return rx

        ################################################################
        if len(graphs)>0:
          ck.out(config.CR_LINE)
          ck.out('Pushing results to graphs...')

          rx=ck.gen_tmp_file({'prefix':'tmp-result-', 'suffix':'.json'})
          if rx['return']>0: return rx
          fn=rx['file_name']

          rx=ck.save_json_to_file({'json_file':fn, 'dict':crdf})
          if rx['return']>0: return rx

          if solution_uoa not in graphs:
            graphs.append(solution_uoa)

          for gr in graphs:
            ck.out('')
            ck.out('  * Graph: '+gr)

            ck.out('')
            rx=graph.push({'uid':gr, 'version':'1.0.0', 'filename':fn})
            if rx['return']>0: return rx

            if 'graphs' not in rr: rr['graphs']=[]
            rr['graphs'].append(rx)

            rdf_st['status'] = 3
            rx=ck.save_json_to_file({'json_file':tmp_solStatus, 'dict':rdf_st})
            if rx['return']>0: return rx

          # Clean temp data file
          if os.path.isfile(fn):
            os.remove(fn)

        ################################################################
        pconv=os.path.join(p, 'graph-convertor.json')
        if os.path.isfile(pconv):
           rx=ck.load_json_file({'json_file':pconv})
           if rx['return']==0:
              ck.out(config.CR_LINE)
              ck.out('Converting data for extra graphs ...')

              dconv=rx['dict']

              for eg in dconv:
                  gr=eg['graph_id']

                  ck.out('')
                  ck.out('  * Graph: '+gr)

                  keys=eg['keys']

                  cdata={}

                  for k in keys:
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
                             if kx.startswith('##'):
                                ry=ck.get_by_flat_key({'dict':crdf, 'key':kx})
                                if ry['return']>0: return ry
                                v=ry['value']
                             else:
                                v=crdf.get(kx)

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
                         cdata[ok]=vv

                  rx=ck.gen_tmp_file({'prefix':'tmp-result-', 'suffix':'.json'})
                  if rx['return']>0: return rx
                  fn=rx['file_name']

                  rx=ck.save_json_to_file({'json_file':fn, 'dict':cdata})
                  if rx['return']>0: return rx

                  ck.out('')
                  rx=graph.push({'uid':gr, 'version':'1.0.0', 'filename':fn})
                  if rx['return']>0: return rx

                  if 'graphs' not in rr: rr['graphs']=[]
                  rr['graphs'].append(rx)

                  # Clean temp data file
                  if os.path.isfile(fn):
                     os.remove(fn)

    return rr

############################################################################
# List local solutions

def ls(i):

    """
    Input:  {
              (uid) [str] - portal identifier of the solution (can have wiledcards)
            }

    Output: {
              return  [int]    - return code = 0 if success or >0 if error
              (error) [str]    - error string if return>0 
            }
    """

    # Create entry
    uid=i['uid']
    if uid==None: uid=''

    r=ck.access({'action':'ls',
                 'module_uoa':config.CR_MODULE_UOA,
                 'data_uoa':uid,
                 'common_func':'yes',
                 'all':'yes',
                 'out':'con'})
    return r

############################################################################
# Find solution

def find(i):

    """
    Input:  {
              uid [str] - Portal identifier of the solution
            }

    Output: {
              return  [int]    - return code = 0 if success or >0 if error
              (error) [str]    - error string if return>0 
            }
    """

    # Find entry
    uid=i['uid']

    r=ck.access({'action':'find',
                 'module_uoa':config.CR_MODULE_UOA,
                 'data_uoa':uid,
                 'common_func':'yes',
                 'out':'con'})
    return r

############################################################################
# Delete solution

def rm(i):

    """
    Input:  {
              uid [str] - Portal identifier of the solution
            }

    Output: {
              return  [int]    - return code = 0 if success or >0 if error
              (error) [str]    - error string if return>0 
            }
    """

    # Delete entry
    uid=i['uid']

    r=ck.access({'action':'rm',
                 'module_uoa':config.CR_MODULE_UOA,
                 'data_uoa':uid,
                 'common_func':'yes',
                 'out':'con'})
    return r

############################################################################
# Get solution directory

def get_solution_dir(i):
    uid=i['uid']

    # Get work dir
    r=config.get_work_dir({})
    if r['return']>0: return r

    work_dir=r['path']

    # Get solutions dir
    solutions_dir=os.path.join(work_dir, config.CR_SOLUTIONS_DIR)
    if not os.path.isdir(solutions_dir):
      os.makedirs(solutions_dir)

    # Get the solution dir
    solution_dir=os.path.join(solutions_dir, uid)
    if not os.path.isdir(solution_dir):
      os.makedirs(solution_dir)

    return {'return':0, 'solutions_dir':solutions_dir, 'solution_dir':solution_dir}

##############################################################################
# extracting summary of all deps

def deps_summary(i):
    """
    Input:  {
              deps - resolved deps
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              deps_summary - summary of deps
            }

    """

    deps=i['deps']
    ds=i.get('deps_summary',{})

    for x in deps:
        d=deps[x]
        dd=d.get('dict',{})

        ds[x]={}

        cx=dd.get('customize',{})

        ds[x]['tags']=d.get('tags',[])
        ds[x]['name']=d.get('name','')

        ds[x]['package_tags']=','.join(dd.get('tags',[]))
        ds[x]['data_name']=dd.get('data_name','')

        puoa=dd.get('package_uoa','')
        if puoa=='':
           puoa=d.get('cus',{}).get('used_package_uid','')
        ds[x]['package_uoa']=puoa

        ds[x]['version']=cx.get('version','')
        ds[x]['git_revision']=cx.get('git_info',{}).get('revision','')
        ds[x]['git_iso_datetime_cut_revision']=cx.get('git_info',{}).get('iso_datetime_cut_revision','')

        sdeps=dd.get('deps',{})
        if len(sdeps)>0:
           # Recursion
           r=deps_summary({'deps':sdeps})
           if r['return']>0: return r
           ds[x]['deps']=r['deps_summary']

    return {'return':0, 'deps_summary':ds}

##############################################################################
# publish result

def publish_result(i):

    """
    Input:  {
              uid [str] - portal identifier of the solution
            }

    Output: {
              return  [int]    - return code = 0 if success or >0 if error
              (error) [str]    - error string if return>0 
            }
    """

    # Get main configuration
    r=config.load({})
    if r['return']>0: return r
    cfg=r.get('dict',{})
    pcfg=r.get('path','')

    xcmd=i.get('cmd','')
    if xcmd==None: xcmd=''
    xcmd=xcmd.strip()

    cur_dir=os.getcwd()

    # Check if Windows or Linux
    # Get platform info 
    r=get_platform_desc(i) # Pass input from init
    if r['return']>0: return r

    hos=r['host_os_uid']
    hosx=r['host_os_uoa']
    hosd=r['host_os_dict']
    hosd_extra=r['host_desc']

    tos=r['os_uid']
    tosx=r['os_uoa']
    tosd=r['os_dict']

    # Load entry with the solution
    uid=i['uid']

    r=ck.access({'action':'load',
                 'module_uoa':config.CR_MODULE_UOA,
                 'data_uoa':uid})
    if r['return']>0: return r

    solution_uoa=r['data_uoa']
    solution_uid=r['data_uid']

    p=r['path']
    dd=r['dict']

    # TBD: need to be checked from outside ...
    host_os=dd.get('host_os','')
    tos=dd.get('target_os','')
    tdid=dd.get('device_id','')

    workflow=dd.get('workflow','')
    workflow_cmd=dd.get('workflow_cmd','')
    workflow_cmd_extra=dd.get('workflow_cmd_extra','')

    workflow_input_dir=dd.get('workflow_input_dir','')
    workflow_output_dir=dd.get('workflow_output_dir','')

    result_file=dd.get('result_file','')

    graphs=dd.get('graphs',[])

    ##############################################################
    ck.out(config.CR_LINE)
    ck.out('Find path to output file '+result_file+' ...')
    ck.out('')

    encoding=locale.getdefaultlocale()[1]

    cmd0=hosd['change_dir']+' '+hosd['env_quotes_if_space']+p+hosd['env_quotes_if_space']+'\n'
    cmd0+=hosd['env_set']+' CK_REPOS='+hosd['env_quotes_if_space']+os.path.join(p, 'CK')+hosd['env_quotes_if_space']+'\n'
    cmd0+=hosd['env_call']+' '+hosd['env_quotes_if_space']+os.path.join(p, 'venv', hosd_extra['venv_bin'], hosd_extra['venv_activate'])+hosd['env_quotes_if_space']+'\n'

    cmd=cmd0
    cmd+='ck find '+workflow+'\n'

    ii={'action':'shell',
        'module_uoa':'os',
        'cmd':cmd,
        'encoding':encoding}
    r=ck.access(ii)
    if r['return']>0: 
      status=-1
      return r

    path_result=r['stdout'].strip()
    path_result_file=os.path.join(path_result, result_file)

    ck.out('  Found path: '+path_result_file)

    # ##############################################################
    # ck.out(config.CR_LINE)
    # ck.out('Detecting complete platform info ...')

    # pinfo=os.path.join(p, 'platform-info.json')
    # if os.path.isfile(pinfo): os.remove(pinfo)

    # cmd=cmd0

    # # Need to do it from virtual env since it's the correct way for Android devices which may require specific files (adb)
    # s='ck detect platform'
    # if i.get('target_os','')!='': s+=' --target_os='+i['target_os']
    # if tdid!='': s+=' --device_id='+tdid
    # s+=' --out=json_file --out_file='+pinfo

    # cmd+=s+'\n'

    # ii['cmd']=cmd
    # r=ck.access(ii)
    # if r['return']>0: return r

    # if not os.path.isfile(pinfo):
    #    return {'return':1, 'error':'platform info file was not created'}

    # # Get some sub-info about deps and platforms
    # dinfo={}
    # if os.path.isfile(pinfo):
    #    r=ck.load_json_file({'json_file':pinfo})
    #    if r['return']==0:
    #       dinfo=r['dict'].get('features',{})
    #       for k in ['cpu_misc', 'cpu']:
    #           if k in dinfo: del(dinfo[k])

    # pdeps=os.path.join(p, 'resolved-deps.json')
    # ddeps={}
    # if os.path.isfile(pdeps):
    #    r=ck.load_json_file({'json_file':pdeps})
    #    if r['return']==0:
    #       ddeps2=r['dict']

    #       r=deps_summary({'deps':ddeps2})
    #       if r['return']==0:
    #          ddeps=r['deps_summary']

    ##############################################################
    # status management

    path_tmpSol=os.path.join(p, "tmp")
    tmp_solStatus=os.path.join(path_tmpSol, "status.json")

    status = 0
    if not os.path.isdir(path_tmpSol): 
      os.mkdir(path_tmpSol)

    rdf_st={}
    rx=ck.load_json_file({'json_file':tmp_solStatus})
    if rx['return']>0: 
      rx=ck.save_json_to_file({'json_file':tmp_solStatus, 'dict':{'status': 0}})
      return rx
    
    rdf_st=rx['dict']
    status = rdf_st.get('status','')

    if status == 2:
      ##############################################################
      ck.out(config.CR_LINE)
      ck.out('Reading output: '+path_result_file)
      ck.out('')

      if not os.path.isfile(path_result_file):
        ck.out('  Error: output file not found!')
        rdf_st['status'] = -2
        rx=ck.save_json_to_file({'json_file':tmp_solStatus, 'dict':rdf_st})
        if rx['return']>0: return rx
      else:
        rx=ck.load_json_file({'json_file':path_result_file})
        if rx['return']>0: return rx

        crdf=rx['dict']
        ################################################################
        if len(graphs)>0:
          ck.out(config.CR_LINE)
          ck.out('Pushing results to graphs...')

          rx=ck.gen_tmp_file({'prefix':'tmp-result-', 'suffix':'.json'})
          if rx['return']>0: return rx
          fn=rx['file_name']

          rx=ck.save_json_to_file({'json_file':fn, 'dict':crdf})
          if rx['return']>0: return rx

          if solution_uoa not in graphs:
            graphs.append(solution_uoa)

          for gr in graphs:
            ck.out('')
            ck.out('  * Graph: '+gr)

            ck.out('')
            rx=graph.push({'uid':gr, 'version':'1.0.0', 'filename':fn})
            if rx['return']>0: return rx

            rdf_st['status'] = 3
            rx=ck.save_json_to_file({'json_file':tmp_solStatus, 'dict':rdf_st})
            if rx['return']>0: return rx

          # Clean temp data file
          if os.path.isfile(fn):
            os.remove(fn)

        ################################################################
        pconv=os.path.join(p, 'graph-convertor.json')
        if os.path.isfile(pconv):
            rx=ck.load_json_file({'json_file':pconv})
            if rx['return']==0:
              ck.out(config.CR_LINE)
              ck.out('Converting data for extra graphs ...')

              dconv=rx['dict']

              for eg in dconv:
                gr=eg['graph_id']

                ck.out('')
                ck.out('  * Graph: '+gr)

                keys=eg['keys']

                cdata={}

                for k in keys:
                  ok=k['out_key']

                  kk=[k.get('key1',''), k.get('key2',''), k.get('key3',''), k.get('key4','')]

                  vv=''
                  v=k.get('value','')
                  if v!='' and v!=None:
                      vv=v

                  first=True
                  for kx in kk:
                    if kx!='':
                      if kx.startswith('##'):
                        ry=ck.get_by_flat_key({'dict':crdf, 'key':kx})
                        if ry['return']>0: return ry
                        v=ry['value']
                      else:
                        v=crdf.get(kx)

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
                        vv+=v

                  if vv!='':
                    cdata[ok]=vv

                rx=ck.gen_tmp_file({'prefix':'tmp-result-', 'suffix':'.json'})
                if rx['return']>0: return rx
                fn=rx['file_name']

                rx=ck.save_json_to_file({'json_file':fn, 'dict':cdata})
                if rx['return']>0: return rx

                ck.out('')
                rx=graph.push({'uid':gr, 'version':'1.0.0', 'filename':fn})
                if rx['return']>0: return rx

                # Clean temp data file
                if os.path.isfile(fn):
                  os.remove(fn)

      return r
    return {'return':0}
