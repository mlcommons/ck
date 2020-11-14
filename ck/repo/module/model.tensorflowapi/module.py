#
# Collective Knowledge (Tensorflow Model configured with Tensorflow Object Detection API)
#
# 
# 
#
# Developer: 
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel) 

# Local settings

def get_model_env(muid):
    menv_request={
        'module_uoa':'env',
        'data_uoa':muid,
        'action':'load'
    }
    menv=ck.access(menv_request)
    
    menv_return=menv.get('return','1')
    if menv_return != 0:
        return {'return':1, 'error':'Cannot load env: '+muid+'. Maybe this model it is not installed.'}
    return menv

def remove_all_files_from_dir(folder_path):
    import os    
    for the_file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, the_file)
        if os.path.isfile(file_path):
            os.remove(file_path)
    return 0
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
# Train model

def train(i):
    """
    Input:  {
              model_uid    - installed model UID(taken from ck show env)
              (retrain)    - removes previous training/evaluation results
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    import json

    muid=i.get('model_uid','')
    if muid == '':
        return {'return':1, 'error':'Wrong usage: call with --model_uid argument'}

    menv=get_model_env(muid)
    menv_name=menv.get('data_name','') 
   
    menv_dict=menv.get('dict','')
    menv_variables=menv_dict.get('env','')    
    mdir=menv_variables.get('CK_ENV_MODEL_TENSORFLOW_API_ROOT','')
    
    if i.get('retrain','')=='yes':
        ck.out('Model will be retrained...')
        mtdir=menv_variables.get('CK_ENV_MODEL_TENSORFLOW_API_MODEL','')+'/train'
        remove_all_files_from_dir(mtdir)
        medir=menv_variables.get('CK_ENV_MODEL_TENSORFLOW_API_MODEL','')+'/eval'
        remove_all_files_from_dir(medir)
    ck.out('Train model: '+menv_name)

    ck.out('')
    ck.out('Command line: ')
    ck.out('')

    pr={"module_uoa": "program", 
        "data_uoa": "tensorflow-api", 
        "action": "load"
    }
    r=ck.access(pr)
    if r.get('return',1) != 0:
        return {'return':1, 'error':'Cannot load program:tensorflow-api'}    
    r_dict=r.get("dict")
        
    ii={ "module_uoa": "program", 
        "data_uoa": "tensorflow-api", 
        "action": "run",
        "cmd_key":"train",
        "deps":{}}
    
    deps=r_dict.get('run_deps')
    ii['deps']=deps
    ii['deps']['tensorflow-api-model']['uoa']=muid
    
    duid = r.get('data_uid')
    ii['data_uid']=duid

    ck.out('For TensorBoard usage run in another terminal $ tensorboard --logdir='+mdir)
    out=ck.access(ii)
    return {'return':0}

##############################################################################
# Evaluate model 

def eval(i):
    """
    Input:  {
              model_uid    - installed model UID(taken from ck show env)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import json
   
    muid=i.get('model_uid','')
    if muid == '':
        return {'return':1, 'error':'Wrong usage: call with --model_uid argument'}

    menv=get_model_env(muid)
    menv_name=menv.get('data_name','')

    menv_dict=menv.get('dict','')
    menv_variables=menv_dict.get('env','')    
    mdir=menv_variables.get('CK_ENV_MODEL_TENSORFLOW_API_ROOT','')    

    ck.out('Evaluate model: '+menv_name)

    ck.out('')
    ck.out('Command line: ')
    ck.out('')

    pr={"module_uoa": "program", 
        "data_uoa": "tensorflow-api", 
        "action": "load"
    }
    r=ck.access(pr)
    if r.get('return',1) != 0:
        return {'return':1, 'error':'Cannot load program:tensorflow-api'}    
    r_dict=r.get("dict")
        
    ii={ "module_uoa": "program", 
        "data_uoa": "tensorflow-api", 
        "action": "run",
        "cmd_key":"evaluation",
        "deps":{}}
    
    deps=r_dict.get('run_deps')
    ii['deps']=deps
    ii['deps']['tensorflow-api-model']['uoa']=muid
    
    duid = r.get('data_uid')
    ii['data_uid']=duid
    
    ck.out('For TensorBoard usage run in another terminal $ tensorboard --logdir='+mdir)
    out=ck.access(ii)
    return {'return':0}

