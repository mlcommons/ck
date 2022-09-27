#
# Collective Knowledge (script)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin, Grigori.Fursin@cTuning.org, http://fursin.net
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel) 

import os


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
# run a function in a Python script (main mode)

def run(i):
    """
    Input:  {
              data_uoa            - data UOA of the script entry
              (repo_uoa)          - repo UOA of the script entry
              (script_module_uoa) - module UOA of the script entry

              name                - subscript name (from entry desc - will be called via shell)
              (params)            - pass params to CMD

                or

              (code)              - Python script name (without .py)
              (func)              - Python function name in this script
              (dict)              - dict to pass to script
              (output_json_file)  - filename to save the output dictionary into

            }

    Output: {
              return        - return code =  0, if successful
                                          >  0, if error
              (error)       - error text if return > 0

              (return_code) - script's return code
            }

    """


    ruoa=i.get('repo_uoa','')
    muoa=i.get('script_module_uoa','')
    if muoa=='': muoa=work['self_module_uoa']
    duoa=i.get('data_uoa','')

    name=i.get('name','')
    params=i.get('params','')


    # Loading entry
    rx=ck.access({'action':'load',
                  'module_uoa': muoa,
                  'data_uoa':duoa})
    if rx['return']>0: return rx
    d=rx['dict']
    p=rx['path']

    python_script_name  = i.get('code', d.get('default_python_script_name') )
    function_name       = i.get('func', d.get('default_function_name') )

    if python_script_name and function_name:
       r=ck.load_module_from_path({'path':p, 'module_code_name':python_script_name, 'skip_init':'yes'})
       if r['return']>0: return r

       loaded_module=r.get('code')
       if not loaded_module:
          return {'return':1, 'error':'no python code found'}

       script_function=getattr(loaded_module, function_name)

       if not script_function:
          return {'return':1, 'error':'function '+function_name+' not found in python script '+python_script_name}

       func_input_data=i.get('dict',{})

       func_input_data['ck_kernel']=ck

       rr=script_function(func_input_data)
       if rr['return']>0:
            return {'return':1, 'error':'script failed ('+rr['error']+')'}      # LG: why not just return rr?

       rr['return_code']=rr['return']       # LG: for compatibility with a different protocol?

       output_json_file = i.get('output_json_file')
       if output_json_file:
            r=ck.save_json_to_file({'json_file': output_json_file, 'dict':rr})
            if r['return']>0: return r

    else:
       ss=d.get('sub_scripts',{})

       xs=ss.get(name,{})

       if len(xs)==0:
          return {'return':1, 'error':'subscript "'+name+'" is not found in entry "'+duoa+'"'}

       cmd=xs.get('cmd','')

       p1=p+os.path.sep

       cmd=cmd.replace('$#ck_path#$', p1)+' '+params

       rx=os.system(cmd)

       rr={'return':0, 'return_code':rx}

    return rr


##############################################################################
# run a function in a Python script via a CK wrapper

def _run_external(i):
    """
    Input:  {
                data_uoa            - data UOA of the script-containing entry
                (script_module_uoa) - module UOA of the script-containing entry ('script' by default)
                (prewrapper_lines)  - lines of the environment-setting pre-wrapper
                (script_module_uoa) - module UOA of the script entry
                (keep_tmp_files)    - "yes" will keep them, deleted otherwise

                (code)              - Python script name (without .py)
                (func)              - Python function name in this script
                (dict)              - dict to pass to script
                (output_json_file)  - filename to save the output dictionary into

            }

    Output: {
                return              - return code =  0, if successful
                                                  >  0, if error
                (error)             - error text if return > 0

                (return_code)       - script's return code
            }
    Test:
            ck _run_external script:debug @@@"{'prewrapper_lines': ['export CK_PYTHON=python3'], 'dict': {'alpha': 777}}"

    """

    module_uoa          = i.get('script_module_uoa', work['self_module_uoa'])
    data_uoa            = i['data_uoa']
    prewrapper_lines    = i.get('prewrapper_lines', [])
    keep_tmp_files      = i.get('keep_tmp_files', 'no')
    code                = i.get('code','')
    func                = i.get('func','')
    func_input_data     = i.get('dict', {})

    code = '--code=' + code if code else ''
    func = '--func=' + func if func else ''

    ## Generate one common seed for two temporary names for JSON files:
    #
    gentmp_adict = ck.gen_tmp_file({'prefix': 'ck_call_', 'suffix': '.json'})
    if gentmp_adict['return']>0: return gentmp_adict

    ## Keeping the second name in sync with the first one:
    #
    input_json_file = gentmp_adict['file_name']
    output_json_file = input_json_file.replace('ck_call_', 'ck_response_')

    ## Avoiding to serialize the kernel:
    #
    func_input_data.pop('ck_kernel')

    ## Fill in the input_json_file with input parameters:
    #
    input_adict = ck.save_json_to_file( {'json_file': input_json_file, 'dict': {'dict': func_input_data} } )
    if input_adict['return']>0: return input_adict

    ## Form and run the external ck command with the given Python:
    #
    shell_cmd = "ck run {}:{} {} {} @{} --output_json_file={}".format(module_uoa, data_uoa, code, func, input_json_file, output_json_file)

    ck.out("RPC call: {}".format(shell_cmd))
    envsecute_adict = ck.access({'action':'envsecute',
        'module_uoa':           'env',
        'prewrapper_lines':     prewrapper_lines,
        'shell_cmd':            shell_cmd,
    })
    ck.out("RPC returned: {}".format(envsecute_adict))
    return_code = envsecute_adict['return']

    if keep_tmp_files=='yes':
        ck.out("Temporary JSON files' generated: {} and {}".format(input_json_file, output_json_file))

    ## Parse the output_json_file and return its contents:
    #
    output_adict = ck.load_json_file( {'json_file': output_json_file} )
    if output_adict['return']>0: return output_adict

    output_dict = output_adict['dict']
    output_dict['return_code'] = return_code

    if return_code==0 and output_dict['return']==0 and keep_tmp_files!='yes':
        os.remove(input_json_file)
        os.remove(output_json_file)

    return output_dict
