#
# Collective Knowledge (Unified modeling using R)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin
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
# build model

def build(i):
    """

    Input:  {
              model_name            - model name
              (model_file)          - model output file, otherwise generated as tmp file

              features_table        - features table (in experiment module format)
              features_keys         - features flat keys 
              characteristics_table - characteristics table (in experiment module format)
              characteristics_keys  - characteristics flat keys

              (keep_temp_files)     - if 'yes', keep temp files 
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              model_input_file - temp input file (csv) - can be deleted if not keep_temp_files
              model_file       - output model file 
            }

    """

    import tempfile
    import os

    o=i.get('out','')

    mn=i['model_name']
    mf=i.get('model_file','')
    mf1=i['model_file']+'.r.obj'
    mf4=i['model_file']+'.r.ft.txt'

    ftable=i['features_table']
    fkeys=i['features_keys']
    ctable=i['characteristics_table']
    ckeys=i['characteristics_keys']

    lftable=len(ftable)
    lctable=len(ctable)

    # Enumerate features
    s=''

    fk=1
    for fx in sorted(fkeys): # Needed to be sorted
        s+='V'+str(fk)+') '+fx
        s+='\n'
        fk+=1

    if s!='':
       r=ck.save_text_file({'text_file':mf4, 'string':s})
       if r['return']>0: return r

    if o=='con':
       ck.out('*******************************************************')
       ck.out('Feature key convertion:')
       ck.out('')
       ck.out(s)

    if lftable!=lctable:
       return {'return':1, 'error':'length of feature table ('+str(lftable)+') is not the same as length of characteristics table ('+str(lctable)+')'}

#    if len(ckeys)>1:
#       return {'return':1, 'error':'currently we support only modeling for 1 characteristic'}

    ktf=i.get('keep_temp_files','')

    # First convert to CSV for R ***********************************
    # Prepare common table from features and characteristics
    dim=[]
    for q in range(0, lftable): 
        vv=[]
        for v in ftable[q]:
            vv.append(v)
        for v in ctable[q]:
            vv.append(v)
        dim.append(vv)

    # Prepare common keys
    keys=[]
    for q in fkeys:
        keys.append(q)
    for q in ckeys:
        keys.append(q)

    # Prepare temporary CSV file
    if ktf=='yes' and mf!='':
       fn1=mf+'.build.in.csv'
    else:
       fd1, fn1=tempfile.mkstemp(suffix='.tmp', prefix='ck-')
       os.close(fd1)
       os.remove(fn1)

    if ktf=='yes' and o=='con': 
       ck.out('')
       ck.out('  Temporary CSV file = '+fn1)
       ck.out('')

    ii={'action':'convert_table_to_csv',
        'module_uoa':cfg['module_deps']['experiment'],
        'table':dim,
        'keys':keys,
        'file_name':fn1,
        'csv_no_header':'yes',
        'csv_separator':';',
        'csv_decimal_mark':'.'
       }
    r=ck.access(ii)
    if r['return']>0: return r

    # Prepare (temporary) out model file
    fn2=mf
    if fn2=='' or i.get('web','')=='yes':
       fd2, fn2=tempfile.mkstemp(suffix='.tmp', prefix='ck-')
       os.close(fd2)
       os.remove(fn2)
    else:
       fn2=mf1
       if os.path.isfile(fn2): os.remove(fn2)

    # Calling R
    p=work['path']
    model_code=cfg['model_code_build'].replace('$#model_name#$',mn)

    pmc=os.path.join(p, model_code)
    
    cmd='R --vanilla --args '+fn1+' '+fn2+' < '+pmc
    os.system(cmd)

    if ktf=='yes' and o=='con': 
       ck.out('')
       ck.out('  Executed command:')
       ck.out(cmd)
       ck.out('')

    if ktf!='yes' and os.path.isfile(fn1): os.remove(fn1)

    if not os.path.isfile(fn2): 
       if ktf=='yes' and o=='con': 
          ck.out('')
          ck.out('  Temporary input CSV file = '+fn1)
          ck.out('')

       return {'return':1, 'error':'model was not created'}

    return {'return':0, 'model_input_file':fn1, 'model_file':fn2}

##############################################################################
# validate model

def validate(i):
    """

    Input:  {
              model_name            - model name:
                                                  earth
                                                  lm
                                                  nnet
                                                  party
                                                  randomforest
                                                  rpart
                                                  svm

              model_file            - file with model (object) code

              features_table        - features table (in experiment module format)
              features_keys         - features flat keys 

              (keep_temp_files)     - if 'yes', keep temp files 
            }

    Output: {
              return           - return code =  0, if successful
                                             >  0, if error
              (error)          - error text if return > 0

              prediction_table - experiment table with predictions
            }

    """

    import tempfile
    import os
    import csv
    import sys

    mn=i['model_name']
    mf=i['model_file']
    mf1=i['model_file']+'.r.obj'

    ftable=i['features_table']
    fkeys=i['features_keys']

    ktf=i.get('keep_temp_files','')

    lftable=len(ftable)

    # First convert to CSV for R ***********************************
    # Prepare temporary CSV file
    if ktf=='yes':
       fn1=mf+'.validate.in.csv'
    else:
       fd1, fn1=tempfile.mkstemp(suffix='.tmp', prefix='ck-')
       os.close(fd1)
       os.remove(fn1)

    ii={'action':'convert_table_to_csv',
        'module_uoa':cfg['module_deps']['experiment'],
        'table':ftable,
        'keys':fkeys,
        'file_name':fn1,
        'csv_no_header':'yes',
        'csv_separator':';',
        'csv_decimal_mark':'.'
       }
    r=ck.access(ii)
    if r['return']>0: return r

    # Prepare temporary out file
    if ktf=='yes':
       fn2=mf+'.validate.out.csv'
       if os.path.isfile(fn2): os.remove(fn2)
    else:
       fd2, fn2=tempfile.mkstemp(suffix='.tmp', prefix='ck-')
       os.close(fd2)
       os.remove(fn2)

    # Calling R
    p=work['path']
    model_code=cfg['model_code_predict'].replace('$#model_name#$',mn)

    pmc=os.path.join(p, model_code)
    
    cmd='R --vanilla --args '+mf1+' '+fn1+' '+fn2+' < '+pmc
    print (cmd)
    os.system(cmd)

    if ktf!='yes' and os.path.isfile(fn1): os.remove(fn1)

    if not os.path.isfile(fn2): 
       return {'return':1, 'error':'output prediction file was not created'}

    # Parse CSV and convert to experiment format
    # Read predictions
    pr=[]
    f=open(fn2, 'r')
    c=csv.DictReader(f, delimiter=',')
    for a in c:
        k=list(a.keys())
        if len(k)>0:
           pr.append([a[k[1]]])
    f.close()

    if ktf!='yes': os.remove(fn2)

    return {'return':0, 'prediction_table':pr}
