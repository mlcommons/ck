#
# Collective Knowledge (module providing API to communicate with various ck-crowdnodes ...)
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
# push file to ck-crowdnode

def push(i):
    """
    Input:  {
              (url)      - URL to ck-crowdnode (http://localhost:3333 by default)
              (keyfile)  - path to key

              (filename)  - local file to push to crowd-node
              (filename2) - file with relative path (relative path will be extracted 
                            to 'extra_path') - needed for compatibility with ADB/SSH

              (extra_path)          - extra path inside entry (create if doesn't exist)
              (archive)             - if 'yes' push to entry and unzip ...
              (overwrite)           - if 'yes', overwrite files
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')

    url=i.get('url','')
    if url=='': url='http://localhost:3333'

    keyfile=i.get('keyfile','')
    key=''
    if keyfile!='':
        # Load keyfile
        r=ck.load_text_file({'text_file':keyfile})
        if r['return']>0: return r
        key=r['string'].strip()

    fn=i.get('filename','')
    if fn=='' or not os.path.isfile(fn):
        return {'return':1, 'error':'file '+fn+' not found'}

    ep=i.get('extra_path','')
    if ep=='':
        fn2=i.get('filename2','')
        if fn2!='':
            ep=os.path.dirname(fn2)

    ii={'action':'push',
        'remote_server_url':url,
        'secretkey':key,
        'extra_path':ep,
        'filename':fn}
    return ck.access(ii)

##############################################################################
# pull file from ck-crowdnode

def pull(i):
    """
    Input:  {
              (url)      - URL to ck-crowdnode (http://localhost:3333 by default)
              (keyfile)  - path to key

              (filename)  - file to pull from remote crowd-node
              (filename2) - local file to record (to current path)

              (extra_path)          - extra path inside entry (create if doesn't exist)
              (archive)             - if 'yes' push to entry and unzip ...
              (overwrite)           - if 'yes', overwrite files
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')

    url=i.get('url','')
    if url=='': url='http://localhost:3333'

    keyfile=i.get('keyfile','')
    key=''
    if keyfile!='':
        # Load keyfile
        r=ck.load_text_file({'text_file':keyfile})
        if r['return']>0: return r
        key=r['string'].strip()

    fn=i.get('filename','')
    if fn=='':
        return {'return':1, 'error':'remote file not specified'}

    ep=os.path.dirname(fn)
    fn=os.path.basename(fn)

    ii={'action':'pull',
        'remote_server_url':url,
        'secretkey':key,
        'filename':fn,
        'extra_path':ep}
    r=ck.access(ii)
    if r['return']>0: return r

    return {'return':0}

##############################################################################
# execute command on ck-crowdnode

def shell(i):
    """
    Input:  {
              (url)      - URL to ck-crowdnode (http://localhost:3333 by default)
              (keyfile)  - path to key

              (cmd)      - command line
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              stdout
              stderr
              return_code
            }

    """

    import base64

    o=i.get('out','')

    url=i.get('url','')
    if url=='': url='http://localhost:3333'

    keyfile=i.get('keyfile','')
    key=''
    if keyfile!='':
        # Load keyfile
        r=ck.load_text_file({'text_file':keyfile})
        if r['return']>0: return r
        key=r['string'].strip()

    cmd=i.get('cmd','').strip()
    if cmd=='':
        return {'return':1, 'error':'cmd is not specified'}

    ii={'action':'shell',
        'remote_server_url':url,
        'secretkey':key,
        'cmd':cmd,
        'out':''}
    r=ck.access(ii)
    if r['return']>0: return r

    rc=r.get('return_code','')
    if rc=='': rc='0'
    irc=int(rc)

    xso=str(r.get('stdout_base64',''))
    xse=str(r.get('stderr_base64',''))

    enc=r.get('encoding','')
    if enc=='': enc='UTF-8'

    so=''
    if xso!='':
        so=base64.urlsafe_b64decode(xso)
        if type(so)==bytes:
            so=so.decode(encoding=enc, errors='ignore')

    se=''
    if xse!='':
        se=base64.urlsafe_b64decode(xse)
        if type(se)==bytes:
            se=se.decode(encoding=enc, errors='ignore')

    if o=='con':
        if so!='': 
            ck.out(so)
        if se!='': 
            if getattr(ck, 'eout', None)==None:
                ck.out(se)
            else:
                ck.eout(se)

    # Check return code
    if irc>0:
        return {'return':irc, 'error':'remote command likely failed (return code > 0)'}

    return {'return':0, 'stdout':so, 'stderr':se}
