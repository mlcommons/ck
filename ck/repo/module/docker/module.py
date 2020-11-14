#
# Collective Knowledge (abstracting docker)
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
# build Docker image

def build(i):
    """
    Input:  {
              data_uoa   - CK entry with Docker description
              (scenario) - scenario to get CMD (default if empty)
              (org)      - organization (default - ctuning)
              (cmd)      - extra CMD
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    i['func']='build'
    return call(i)

##############################################################################
# run Docker image

def run(i):
    """
    Input:  {
              data_uoa   - CK entry with Docker description
              (scenario) - scenario to get CMD (default if empty)
              (cmd)      - extra CMD
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    i['func']='run'
    return call(i)

##############################################################################
# run Docker image

def call(i):
    """
    Input:  {
              data_uoa   - CK entry with Docker description
              func       - (build or run) 

              (scenario) - scenario to get CMD (default if empty)
              (org)      - organization (default - ctuning)

              (sudo)     - if 'yes', use sudo

              (cmd)      - extra CMD

              (browser)  - if 'yes', start browser

              (filename) - file to save/load external Docker image (data_uoa.tar by default)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os
    import platform

    o=i.get('out','')

    func=i['func']

    sudo=i.get('sudo','')

    duoa=i.get('data_uoa','')
    if duoa=='':
       return {'return':1, 'error':'please, specify CK entry with Docker description as following "ck build docker:{CK entry}"'}

    filename=i.get('filename','')
    if filename=='': filename='docker-image-'+duoa+'.tar'

    # Load CK entry
    r=ck.access({'action':'load',
                 'module_uoa':work['self_module_uid'],
                 'data_uoa':duoa})
    if r['return']>0: return r

    p=r['path']
    d=r['dict']

    duoa=r['data_uoa']
    duid=r['data_uid']

    # Check if reuse other entry
    re=d.get('reuse_another_entry','')
    if re!='':
       r=ck.access({'action':'find',
                    'module_uoa':work['self_module_uid'],
                    'data_uoa':re})
       if r['return']>0: return r
       p=r['path']

    # Choose scenario
    s=i.get('scenario','')
    if s=='': s='default'

    # Choose organization
    org=i.get('org','')
    if org=='': 
       org=ck.cfg.get('docker_org','')
       if org=='':
          org='ctuning'

    ecmd=i.get('cmd','')

    # Find scenario in meta
    cc=d.get('cmd',{}).get(s,{})
    c=cc.get(func,'')
    if c=='':
       return {'return':1, 'error':'CMD to '+func+' Docker image is not defined in the CK entry ('+duoa+')'}

    # Check if Windows
    pl=platform.system().lower()
    ps=d.get('platform_specific',{}).get(pl,{})
    for k in ps:
        v=ps[k]

        if v.startswith('$(') and v.endswith(')'):
           # Run and get var
           r=ck.gen_tmp_file({'prefix':'tmp-', 'suffix':'.tmp'})
           if r['return']>0: return r
           ftmp=r['file_name']

           os.system(v[2:-1]+' > '+ftmp)

           # Read file
           r=ck.load_text_file({'text_file':ftmp, 
                                 'delete_after_read':'yes'})
           if r['return']>0: return r
           v=r['string'].strip()

        i[k]=v

    cmd=cc.get(func+'_extra_cmd','')
    if ecmd!='': 
       cmd=ecmd

    # Update CMD
    c=c.replace('$#CK_DOCKER_ORGANIZATION#$',org)
    c=c.replace('$#CK_DOCKER_NAME#$',duoa)
    c=c.replace('$#CK_PATH#$',p)
    c=c.replace('$#CK_DOCKER_FILE#$',filename)

    if cmd!='':
       c=cmd+' '+c

    c='docker '+func+' '+c

    # Update vars from input
    citv=d.get('convert_input_to_vars',{})
    for k in citv:
        x=citv[k]

        ki=x.get('key','')
        kd=x.get('default','')

        vv=i.get(k,'')
        if vv=='':
           vv=kd
           i[k]=vv

        c=c.replace('$#'+ki+'#$',vv)

    if sudo=='yes':
       c='sudo '+c

    # Check if has browser
    if i.get('browser','')=='yes':
       url=d.get('browser',{}).get('url','')

       # Update vars:
       for k in citv:
           x=citv[k]

           ki=x.get('key','')
           vv=i.get(k,'')

           url=url.replace('$#'+ki+'#$',vv)

       import webbrowser
       webbrowser.open(url)

    if o=='con':
       ck.out('Executing command line:')
       ck.out('  '+c)
       ck.out('')

    # Run Docker
    r=os.system(c)

    return {'return':0}

##############################################################################
# login to Docker Hub

def login(i):
    """
    Input:  {
              (sudo) - if 'yes', add sudo
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    s='docker login'
    if i.get('sudo','')=='yes':
       s='sudo '+s

    os.system(s)

    return {'return':0}

##############################################################################
# push a given image to the Docker Hub

def push(i):
    """
    Input:  {
              data_uoa   - CK entry with Docker description
              (scenario) - scenario to get CMD (default if empty)
              (org)      - organization (default - ctuning)
              (cmd)      - extra CMD
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    i['func']='push'
    return call(i)

##############################################################################
# save Docker image (for example to share via external repositories and digital libraries)

def save(i):
    """
    Input:  {
              data_uoa   - CK entry with Docker description
              (scenario) - scenario to get CMD (default if empty)
              (cmd)      - extra CMD
              (filename) - file to save image (data_uoa.tar by default)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    i['func']='save'
    return call(i)

##############################################################################
# import external Docker image (tar file)

def ximport(i):
    """
    Input:  {
              data_uoa   - CK entry with Docker description
              (scenario) - scenario to get CMD (default if empty)
              (cmd)      - extra CMD
              (filename) - file to load image (data_uoa.tar by default)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    i['func']='import'
    return call(i)
