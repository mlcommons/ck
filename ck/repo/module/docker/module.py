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
line='=========================================================================='

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
              (tag)      - tag of the docker image
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
              (tag)      - tag of the docker image
              (scenario) - scenario to get CMD (default if empty)
              (command)  - extra CMD (at the beginning of the docker command)
              (cmd)      - extra CMD (at the end of the docker command)
              (bash)     - if 'yes', add "bash" at the end of CMD
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

              (scenario) - scenario to get CMD ("default" if empty)
              (org)      - organization (default - ctuning)
              (tag)      - container tag

              (sudo)     - if 'yes', use sudo

              (cmd)      - extra CMD

              (browser)  - if 'yes', start browser

              (filename) - file to save/load external Docker image (data_uoa.tar by default)

              (no-cache) - if 'yes', add "--no-cache" to cmd

              (bash)     - if 'yes', add "basH' at the end of cmd
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

    ruoa=i.get('repo_uoa','')
    
    duoa=i.get('data_uoa','')
    if duoa=='':
       return {'return':1, 'error':'please, specify CK entry with Docker description as following "ck {action} docker:{CK entry}"'}

    filename=i.get('filename','')
    if filename=='': filename='docker-image-'+duoa+'.tar'

    # Load CK entry
    r=ck.access({'action':'load',
                 'repo_uoa':ruoa,
                 'module_uoa':work['self_module_uid'],
                 'data_uoa':duoa})
    if r['return']>0: return r

    p=r['path']
    d=r['dict']

    duoa=r['data_uoa']
    duid=r['data_uid']

    # Check if aging (may not work) or outdated (likely not working)
    if d.get('outdated','')=='yes' or d.get('aging','')=='yes':
        ck.out(line)
        if d.get('outdated','')=='yes':
            ck.out('WARNING: this container is marked as outdated and unlikely to work!')
        else:
            ck.out('WARNING: this container is marked as aiging and may not work!')
           
        ck.out('')

        r=ck.inp({'text':'Would you like to continue (y/N)? '})
        if r['return']>0: return r
        s=r['string'].strip().lower()
        if s!='y' and s!='yes':
            return {'return':0}
    
        ck.out('')

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
    if s=='':
        s='default'

    # Choose organization
    org=i.get('org','')
    if org=='':
        org=d.get('default_org','')
    if org=='': 
        org=ck.cfg.get('docker_org','')
    if org=='':
        org='ctuning'

    ecmd=i.get('cmd','')

    # Find scenario in meta
    cc=d.get('cmd',{}).get(s,{})
    c=cc.get(func,'')

    # Hack if pull not defined, try push
    if func=='pull':
        if c=='':
            c=cc.get('push','')

    if c=='':
       return {'return':1, 'error':'CMD to '+func+' Docker image is not defined in the CK entry ('+duoa+')'}

    # Check tag
    tags=d.get('docker_tags',[])
    tag=''

    if i.get('tag','')!='':
        tag=i['tag']
    
    elif len(tags)>0:
        ck.out(line)
        ck.out('Available tags:')
        ck.out('')

        k=0
        for t in tags:
            ck.out(str(k)+') '+t)
            k+=1

        ck.out('')
        if i.get('quiet','')=='yes':
            kk=0
        else:
            if len(tags)==1:
                kk=0
                ck.out('Selected: 0')
            else:
                r=ck.inp({'text':'Select a tag or press Enter to select 0: '})
                if r['return']>0: return r

                s=r['string'].strip()
                if s=='': s='0'

                kk=int(s)

                if kk<0 or kk>=k:
                    return {'return':1, 'error':'tag number is not recognized'}

        tag=tags[kk]

    stag_dot=''
    stag_colon=''
    if tag!='':
        ck.out('')
        ck.out('Selected tag: '+tag)
        ck.out('')

        stag_dot='.'+tag
        stag_colon=':'+tag

        c=c.replace('$#CK_TAG_DOT#$', stag_dot)
        c=c.replace('$#CK_TAG_COLON#$', stag_colon)

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

           ck.out('')
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

    if i.get('no-cache','')=='yes':
        c='--no-cache '+c

    if i.get('bash','')=='yes':
        c+=' bash'

    if i.get('command','')!='':
#        c+=' "'+i['command']+'"'
        x='"' if pl=='windows' else ''
        c+=' '+x+i['command']+x

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

##############################################################################
# rebuild a given container

def rebuild(i):
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
    i['no-cache']='yes'
    return call(i)

##############################################################################
# pull Docker image

def pull(i):
    """
    Input:  {
              data_uoa   - CK entry with Docker description
              (tag)      - tag of the docker image
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

    i['func']='pull'
    return call(i)
