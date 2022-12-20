#
# Collective Knowledge (pipeline demo)
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
# run pipeline

def pipeline(i):
    """
    Input:  {
               (cmd)            - cmd string or list
               (compiler_vars)  - will substitute dummies $#VAR#$ in cmd
               (compiler_flags) - assemble into string and substitute $#compiler_flags#$
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import json
    import os
    import time
    import sys

    o=i.get('out','')

    cmd=i.get('cmd','')

    if type(cmd)!=list:
       cmd=[cmd]

    # Checking some known vars 
    cv=i.get('compiler_vars',{})
    cf=i.get('compiler_flags',{})

    cflags=''
    for c in cf:
        cx='##compiler_flags#'+c
        cc=cf[c]
        if cc!='':
           if cflags!='': cflags+=' '
           cflags+=str(cc)

    # Parsing special vars $#var#$
    pcmd=[]
    for c in cmd:
        j=c.find('$#')
        while j>=0:
           j1=c.find('#$',j+1)
           if j1<0:
              return {'return':1, 'error':'inconsistent CK vars $# #$ in cmd ('+c+')'}

           k=c[j+2:j1]
 
           # Check special keys
           if k=='cflags':
              v=cflags
           else:
              v=cv.get(k,'') # for backwards compatibility 
              if v=='':
                 v=i.get(k,'')

           c=c[:j]+str(v)+c[j1+2:]

           j=c.find('$#')
           
        pcmd.append(c)

    # Print

    if o=='con':
       ck.out('Updated command line in the pipeline:')
       ck.out('')
       for c in pcmd:
           ck.out('  '+c)

       ck.out('')
       ck.out('Executing ...')
       ck.out('')

    start_time=time.time()

    sys.stdout.flush()

    for c in pcmd:
        os.system(c.strip())

    run_time=time.time()-start_time

    if o=='con':
       ck.out('')
       ck.out('Execution time: '+('%.3f'%run_time)+' sec.')
       ck.out('')


    return {'return':0, 'run_time':run_time}
