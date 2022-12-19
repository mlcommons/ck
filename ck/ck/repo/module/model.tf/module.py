#
# Collective Knowledge (Unified modeling using TensorFlow )
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
    oo=''
    if o=='con': oo=o

    mn=i['model_name']

    mf=i.get('model_file','')
    mf1=mf+'.tf'
    mf4=mf+'.tf.ft.txt'

    ftable=i['features_table']
    fkeys=i['features_keys']
    ctable=i['characteristics_table']
    ckeys=i['characteristics_keys']

    lftable=len(ftable)
    lctable=len(ctable)

    model_params=i.get('model_params',{})

    quiet=model_params.get('quiet','')

    # Prepare path to TF script
    xmn='module_'+mn+'.py'
    pmn=os.path.join(work['path'], xmn)
    if not os.path.isfile(pmn):
       return {'return':1, 'error': 'CK wrapper for "'+mn+'" not found ('+xmn+')'}

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

    # Prepare (temporary) out model file
    fn2=mf
    if fn2=='' or i.get('web','')=='yes':
       fd2, fn2=tempfile.mkstemp(suffix='.tmp', prefix='ck-')
       os.close(fd2)
    else:
       fn2=mf1

    fn2d=fn2+'.dir'
    if os.path.isdir(fn2d):
       import shutil
       shutil.rmtree(fn2d)

    fn2+='.json'
    if os.path.isfile(fn2): os.remove(fn2)

    # Prepare temporary CSV file
    if ktf=='yes' and mf!='':
       fn1f=mf+'.train.features.csv'
       fn1c=mf+'.train.classes.csv'
       fn1j=mf+'.train.json'
    else:
       fd1f, fn1f=tempfile.mkstemp(suffix='.tmp', prefix='ck-')
       fd1c, fn1c=tempfile.mkstemp(suffix='.tmp', prefix='ck-')
       fd1j, fn1j=tempfile.mkstemp(suffix='.tmp', prefix='ck-')

       os.close(fd1f)
       os.close(fd1c)
       os.close(fd1j)

       os.remove(fn1f)
       os.remove(fn1c)
       os.remove(fn1j)

    if ktf=='yes' and o=='con': 
       ck.out('')
       ck.out('  Temporary input features file (train, CSV) = '+fn1f)
       ck.out('  Temporary input classes file (train, CSV) = '+fn1c)
       ck.out('  Temporary input file (JSON) = '+fn1j)
       ck.out('')

    ii={'action':'convert_table_to_csv',
        'module_uoa':cfg['module_deps']['experiment'],
        'table':ftable,
        'keys':fkeys,
        'file_name':fn1f,
        'csv_no_header':'yes',
        'csv_separator':',',
        'csv_decimal_mark':'.'
       }
    r=ck.access(ii)
    if r['return']>0: return r

    ii={'action':'convert_table_to_csv',
        'module_uoa':cfg['module_deps']['experiment'],
        'table':ctable,
        'keys':ckeys,
        'file_name':fn1c,
        'csv_no_header':'yes',
        'csv_separator':';',
        'csv_decimal_mark':'.'
       }
    r=ck.access(ii)
    if r['return']>0: return r

    r=ck.save_json_to_file({'json_file':fn1j, 'dict':{"ftable":ftable, 
                                                      "ctable":ctable, 
                                                      "model_params":model_params,
                                                      "output_file":fn2,
                                                      "model_dir":fn2d}})
    if r['return']>0: return r

    # Set CK environment for TF
    r=prepare_tf({'out':oo, 
                  'mode':'train', 
                  'module_name':pmn, 
                  'input_file':fn1j, 
                  'output_file':fn2,
                  'quiet':quiet})
    if r['return']>0: return r

    if ktf!='yes':
       if os.path.isfile(fn1f): os.remove(fn1f)
       if os.path.isfile(fn1c): os.remove(fn1c)
       if os.path.isfile(fn1j): os.remove(fn1j)

    if not os.path.isfile(fn2): 
       if ktf=='yes' and o=='con': 
          ck.out('')
          ck.out('  Temporary input features file (train, CSV) = '+fn1f)
          ck.out('  Temporary input classes file (train, CSV) = '+fn1c)
          ck.out('  Temporary input file (JSON) = '+fn1j)
          ck.out('')

       return {'return':1, 'error':'model was not created'}

    return {'return':0, 'model_input_file':fn1j, 'model_file':fn2}

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

    o=i.get('out','')
    oo=''
    if o=='con': oo=o

    mn=i['model_name']

    mf=i.get('model_file','')
    mf1=mf+'.tf'

    ftable=i['features_table']
    fkeys=i.get('features_keys',[])

    ktf=i.get('keep_temp_files','')

    lftable=len(ftable)

    model_params=i.get('model_params',{})

    quiet=model_params.get('quiet','')

    # Prepare path to TF script
    xmn='module_'+mn+'.py'
    pmn=os.path.join(work['path'], xmn)
    if not os.path.isfile(pmn):
       return {'return':1, 'error': 'CK wrapper for "'+mn+'" not found ('+xmn+')'}

    # Prepare (temporary) out model file
    fn2=mf
    if fn2=='' or i.get('web','')=='yes':
       fd2, fn2=tempfile.mkstemp(suffix='.tmp', prefix='ck-')
       os.close(fd2)
    else:
       fn2=mf1

    fn2d=fn2+'.dir'
    if not os.path.isdir(fn2d):
       return {'return':1, 'error':'model directory not found ('+fn2d+')'}

    fn2+='.validate.json'
    if os.path.isfile(fn2): os.remove(fn2)

    if ktf=='yes':
       fn1f=mf+'.test.features.csv'
       fn1j=mf+'.test.json'
    else:
       fd1f, fn1f=tempfile.mkstemp(suffix='.tmp', prefix='ck-')
       fd1j, fn1j=tempfile.mkstemp(suffix='.tmp', prefix='ck-')

       os.close(fd1f)
       os.close(fd1j)

       os.remove(fn1f)
       os.remove(fn1j)

    if ktf=='yes' and o=='con': 
       ck.out('')
       ck.out('  Temporary input features file (test, CSV) = '+fn1f)
       ck.out('  Temporary input file (JSON) = '+fn1j)
       ck.out('')

    ii={'action':'convert_table_to_csv',
        'module_uoa':cfg['module_deps']['experiment'],
        'table':ftable,
        'keys':fkeys,
        'file_name':fn1f,
        'csv_no_header':'yes',
        'csv_separator':';',
        'csv_decimal_mark':'.'
       }
    r=ck.access(ii)
    if r['return']>0: return r

    r=ck.save_json_to_file({'json_file':fn1j, 'dict':{"ftable":ftable, 
                                                      "output_file":fn2,
                                                      "model_dir":fn2d}})
    if r['return']>0: return r

    # Set CK environment for TF
    r=prepare_tf({'out':oo, 
                  'mode':'prediction', 
                  'module_name':pmn, 
                  'input_file':fn1j, 
                  'output_file':fn2,
                  'quiet':quiet})
    if r['return']>0: return r

    if ktf!='yes':
       if os.path.isfile(fn1f): os.remove(fn1f)
       if os.path.isfile(fn1j): os.remove(fn1j)

    if not os.path.isfile(fn2): 
       if ktf=='yes' and o=='con': 
          ck.out('')
          ck.out('  Temporary input features file (test, CSV) = '+fn1f)
          ck.out('  Temporary input file (JSON) = '+fn1j)
          ck.out('')

       return {'return':1, 'error':'model was not created'}

    # Read output file
    r=ck.load_json_file({'json_file':fn2})
    if r['return']>0: return r

    pr=r['dict']['ctable']

    if ktf!='yes': os.remove(fn2)

    pr1=[]
    for q in pr:
        pr1.append([q])

    return {'return':0, 'prediction_table':pr1}

##############################################################################
# Convert categorical values to floats

def prepare_tf(i):
    """
    Input:  {
              (tags)      - extra tags to select tensorflow

              module_name - CK wrapper for specific TF model
              mode        - train or predict
              input_file  - input file

              (quiet)     - if 'yes', select first available TF
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

            }

    """

    import locale

    o=i.get('out','')
    oo=''
    if o=='con': 
       oo=o
       ck.out('')
       ck.out('Detecting TensorFlow installations via CK ...')
       ck.out('')

    # Check if ck-tensorflow repo is there
    r=ck.access({'action':'load',
                 'module_uoa':cfg['module_deps']['soft'],
                 'data_uoa':cfg['data_deps']['soft_lib_tensorflow']})
    if r['return']>0:
       if r['return']!=16: return r
       return {'return':1, 'error':'ck-tensorflow repo is not installed. Please installed it using "ck pull repo:ck-tensorflow" and try again'}

    module_name=i['module_name']
    mode=i['mode']
    fi=i['input_file']

    # Prepare TF CK environment
    tags='lib,tensorflow'
    if i.get('tags','')!='': tags+=','+tags

    r=ck.access({'action':'set',
                 'module_uoa':cfg['module_deps']['env'],
                 'tags':tags,
                 'version_from':[1,4,0],
                 'quiet':i.get('quiet',''),
                 'out':oo})
    if r['return']>0: return r

    sb=r['bat']
    d=r['dict']

    # Check python
    pf=d.get('deps',{}).get('python',{}).get('dict',{}).get('env',{}).get('CK_ENV_COMPILER_PYTHON_FILE','')
    if pf=='':
       return {'return':1, 'error':'can\'t find associated python in the selected TF (maybe installed without python?)'}

    sb+='\n'
    sb+=pf+' '+module_name+' '+mode+' '+fi
    sb+='\n'

    if oo=='con':
       ck.out('')
       ck.out('  Executing command:')
       ck.out('')
       ck.out(sb)
       ck.out('')

    r=ck.access({'action':'shell',
                 'module_uoa':cfg['module_deps']['os'],
                 'encoding':locale.getdefaultlocale()[1],
                 'output_to_console':'yes',
                 'cmd':sb})
    if r['return']>0: return r
  
    return {'return':0, 'bat':sb, 'python_file':pf}
