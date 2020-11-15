#
# Collective Knowledge (APK entries)
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
# detect installed APKs

def detect(i):
    """
    Input:  {
              (data_uoa) or (name) - get params only for this APK
              (target_os)          - target Android OS (ck search os --tags=android) (default = android-32)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')
    oo=''
    if o=='con': oo='con'

    hos=i.get('host_os','')
    tos=i.get('target_os','')
    tdid=i.get('device_id','')
    target=i.get('target','')

    if target=='' and tos=='':
        tos='android-32'

    ii={'action':'shell',
        'module_uoa':cfg['module_deps']['os'],
        'host_os':hos,
        'target_os':tos,
        'device_id':tdid,
        'target':target,
        'split_to_list':'yes',
        'should_be_remote':'yes',
        'cmd':'pm list packages'}
    r=ck.access(ii)
    if r['return']>0: return r

    tosd=r['target_os_dict']

    lst=r['stdout_lst']

    params={}

    name=i.get('name','')
    if name=='':
        name=i.get('data_uoa','')

    iapk=0
    for package in sorted(lst):
        if package.startswith('package:'):
            package=package[8:]

        if (name!='' and package!=name) or package=='':
            continue

        iapk+=1
        if o=='con':
            ck.out(package)

        params[package]={}

        # Get parameters
        ii={'action':'shell',
            'module_uoa':cfg['module_deps']['os'],
            'host_os':hos,
            'target_os':tos,
            'device_id':tdid,
            'target':target,
            'split_to_list':'yes',
            'should_be_remote':'yes',
            'cmd':'dumpsys package '+package}

        r=ck.access(ii)
        if r['return']>0: return r

        ll=r['stdout_lst']

        for q in ll:
            j=q.find('=')
            if j>0:
                j1=q.rfind(' ', 0, j)
                k=q[j1+1:j]
                v=q[j+1:]

                j2=v.find(' targetSdk=')
                if j2>0:
                    vv=v[j2+11:]
                    v=v[:j2]
                    kk='targetSdk'

                    params[package][kk]=vv

                params[package][k]=v

    if name!='':
        if iapk==0:
            return {'return':16, 'error':'APK was not found on the target device', 'target_os_dict':tosd}

        if o=='con':
            ck.out('')
            ck.out('Parameters:')
            ck.out('')

            for k in sorted(params[name]):
                v=params[name][k]
                ck.out('  '+k+' = '+v)

    return {'return':0, 'params':params, 'target_os_dict':tosd}

##############################################################################
# check APK

def install(i):
    """
    Input:  {
              (host_os)
              (target_os)
              (device_id)

              name or data_uoa   - APK name
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    o=i.get('out','')
    oo=''
    if o=='con': oo=o

    name=i.get('name','')
    if name=='':
        name=i.get('data_uoa','')

    if name=='':
        return {'return':1, 'error':'APK "name" is not defined'}

    hos=i.get('host_os','')
    tos=i.get('target_os','')
    tdid=i.get('device_id','')
    target=i.get('target','')

    if target=='' and tos=='':
        tos='android19-arm'
        i['target_os']=tos
#        return {'return':1, 'error':'"target_os" or "target" is not specified'}

    xtdid=''
    if tdid!='': xtdid=' -s '+tdid

    rr={'return':0}

    # Detect if APK is installed
    r=detect(i)
    if r['return']>0 and r['return']!=16: return r

    if r['return']==0:
        rr['params']=r['params']

    if r['return']==16:
        # APK is not installed
        tosd=r['target_os_dict']

        abi=tosd.get('abi','')

        if o=='con':
            ck.out('Searching APK for "'+name+'" and ABI="'+abi+'" ...')

        # Check if available in the CK
        r=ck.access({'action':'load',
                     'module_uoa':work['self_module_uid'],
                     'data_uoa':name})
        if r['return']>0 and r['return']!=16: return r

        found=False
        if r['return']==0:
            p=r['path']
            d=r['dict']

            aname=''
            for apk in d.get('apks',[]):
                if abi in apk.get('abis',[]):
                    aname=apk.get('apk_name','')
                    break

            # If the preferred abi didn't match but is 64-bit,
            # look for a 32-bit binary (worst case won't install)
            alt_abi = ''
            if abi in ['arm64-v8a','arm64']:
                alt_abi='armeabi'
            elif abi=='x86-64':
                alt_abi='x86'
            if alt_abi!='':
                for apk in d.get('apks',[]):
                    if alt_abi in apk.get('abis',[]):
                        aname=apk.get('apk_name','')
                        break

            if aname!='':
                pp=os.path.join(p, aname)

                if os.path.isfile(pp):
                    # Trying to install
                    if o=='con':
                        ck.out('  APK found ('+aname+') - trying to install ...')
                        if alt_abi!='':
                            ck.out('  First choice ABI "'+abi+'" not found, using "'+alt_abi+'"')

                    ii={'action':'shell',
                        'module_uoa':cfg['module_deps']['os'],
                        'host_os':hos,
                        'target_os':hos,
                        'cmd':'adb '+xtdid+' install -r -d '+pp,
                        'out':oo}
                    r=ck.access(ii)
                    if r['return']>0: return r

                    rc=r['return_code']

                    if rc>0:
                        return {'return':1, 'error':'command may have failed (return code='+str(rc)+')'}

                    # Detecting params
                    r=detect(i)
                    if r['return']>0 and r['return']!=16: return r

                    if r['return']==0:
                        rr['params']=r['params']

                    found=True

        # If not found
        if not found:
            if o=='con':
                ck.out('')
                ck.out('APK "'+name+'" with abi "'+abi+'" was not found in CK.')
                ck.out('You can download it and then register in the CK via')
                ck.out(' $ ck add apk:{APK name} --path={full path to downloaded APK}')
                ck.out('')

            return {'return':16, 'error':'APK is not installed on target device and was not found in CK'}

    return rr

##############################################################################
# add apk

def add(i):
    """
    Input:  {
              (data_uoa)  - CK entry to add APK (should be official APK name, i.e. openscience.crowdsource.experiments)
              (repo_uoa)  - repo where to add APK

              (abi)       - list of ABI separated by comma (default=armeabi,armeabi-v7a,arm64-v8a)
              (version)   - version
              (versioncode) - versioncode

              (path)      - path to APK on local host (apk_name will be automatically detected)
              (apk_name)  - force APK name
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

    # Check APK name
    apk_name=i.get('apk_name','')
    path=i.get('path','')
    if path!='':
        if not os.path.isfile(path):
            return {'return':1, 'error':'APK is not found ('+path+')'}

        if apk_name=='':
            apk_name=os.path.basename(path)

    # Check ABI
    abi=i.get('abi','')

    if abi=='':
        r=ck.inp({'text':'Enter list of ABI separated by comma or Enter for "armeabi,armeabi-v7a,arm64-v8a"): '})
        if r['return']>0: return r
        abi=r['string'].strip()

        if abi=='':
            abi='armeabi,armeabi-v7a,arm64-v8a'

    if abi=='':
        return {'return':1, 'error':'"abi" is not specified'}

    abis=abi.split(',')

    # Version
    version=i.get('version','')

    if version=='':
        r=ck.inp({'text':'Enter APK version: '})
        if r['return']>0: return r
        version=r['string'].strip()

    if version=='':
        return {'return':1, 'error':'"version" is not specified'}

    # VersionCode
    versioncode=i.get('versioncode','')

    # Check CK entry name
    duoa=i.get('data_uoa','')
    ruoa=i.get('repo_uoa','')

    if duoa=='':
        r=ck.inp({'text':'Enter CK entry name (must be official APK name): '})
        if r['return']>0: return r
        duoa=r['string'].strip()

    # Check if already exists
    r=ck.access({'action':'load',
                 'module_uoa':work['self_module_uid'],
                 'data_uoa':duoa})
    if r['return']>0 and r['return']!=16: return r

    if r['return']==0:
        ruoa=r['repo_uid']
        pp=r['path']
        dd=r['dict']
    else:
        r=ck.access({'action':'add',
                     'module_uoa':work['self_module_uid'],
                     'common_func':'yes',
                     'data_uoa':duoa,
                     'repo_uoa':ruoa})
        if r['return']>0: return r
        pp=r['path']
        dd={}

    # Create dirs and copy files
    p2=os.path.join(pp,apk_name)

    shutil.copyfile(path, p2)

    # Update dict
    if 'apks' not in dd: dd['apks']=[]
    dd['apks'].append({'abis':abis,
                       'apk_name':apk_name,
                       'version':version,
                       'versioncode':versioncode})

    r=ck.access({'action':'update',
                 'module_uoa':work['self_module_uid'],
                 'data_uoa':duoa,
                 'repo_uoa':ruoa,
                 'dict':dd,
                 'sort_keys':'yes',
                 'substitute':'yes',
                 'ignore_update':'yes'})
    if r['return']>0: return r
    p=r['path']

    if o=='con':
        ck.out('')
        ck.out('APK successfully registered in the CK ('+p+')')

    return r

##############################################################################
# uninstall APK

def uninstall(i):
    """
    Input:  {
              (data_uoa) or (name) - get params only for this APK
              (target_os)          - target Android OS (ck search os --tags=android) (default = android-32)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    # First check if exists
    o=i.get('out','')
    oo=''
    if o=='con':
        i['out']=''
        oo=o

    r=detect(i)
    if r['return']>0: return r

    hos=i.get('host_os','')
    tos=i.get('target_os','')
    tdid=i.get('device_id','')
    target=i.get('target','')

    xtdid=''
    if tdid!='': xtdid=' -s '+tdid

    if target=='' and tos=='':
        tos='android-32'

    name=i.get('name','')
    if name=='':
        name=i.get('data_uoa','')

    ii={'action':'shell',
        'module_uoa':cfg['module_deps']['os'],
        'host_os':hos,
        'target_os':hos,
        'out':oo,
        'cmd':'adb '+xtdid+' uninstall '+name}
    r=ck.access(ii)
    if r['return']>0: return r

    rc=r['return_code']
    if rc>0:
        return {'return':1, 'error':'command may have failed (return code='+str(rc)+')'}

    return r

##############################################################################
# List the apks installed on a target device

def list_installed(i):
    """
    Input:  {
              (device_id)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    # First check if exists
    o=i.get('out','')
    oo=''
    if o=='con':
        i['out']=''
        oo=o

    # r=detect(i)
    # if r['return']>0: return r

    hos=i.get('host_os','')
    tos=i.get('target_os','')
    tdid=i.get('device_id','')
    target=i.get('target','')

    xtdid=''
    if tdid!='': xtdid=' -s '+tdid

    if target=='' and tos=='':
        tos='android-32'

    ii={'action':'shell',
        'module_uoa':cfg['module_deps']['os'],
        'host_os':hos,
        'target_os':hos,
        'out':oo,
        'cmd':'adb '+xtdid+' shell pm list packages -f'}
    r=ck.access(ii)
    if r['return']>0: return r

    rc=r['return_code']
    if rc>0:
        return {'return':1, 'error':'command may have failed (return code='+str(rc)+')'}

    output = r['stdout']

    # Output format is "package:[path]=[package]"
    packages = [ a.split('=')[1] for a in output.split('\n') if '=' in a ]

    if o=='con':
        for p in packages:
            ck.out(p)
    return { 'return':0, 'lst':packages}

##############################################################################
# Uninstall all applications on a target device

def uninstall_all(i):
    """
    Input:  {
              (device_id)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    Uninstall all applications on the device specified.

    """

    # First check if exists
    o=i.get('out','')
    oo=''
    if o=='con':
        i['out']=''
        oo=o

    hos=i.get('host_os','')
    tos=i.get('target_os','')
    tdid=i.get('device_id','')
    target=i.get('target','')

    r=list_installed({'device_id':tdid})
    if r['return']>0: return r

    for apk in r['lst']:
        ii={'data_uoa':apk,
            'device_id':tdid}
        uninstall(ii)
        if r['return']>0: return r

    return {'return':0}
