# Collective Mind command line wrapper

import sys

############################################################
def run(argv = None):
    """
    Run CM commands from the command line.

    Args:
        argv (str | list): CM input
    
    Returns: 
        dict: CM output:
          - return (int): return code = 0 if successful 
                                      > 0 if error

          - (error) (str): error text if return > 0

          - ...: Output from a given CM automation
    
    """

    # Access CM
    from cmind.core import CM

    cm = CM()

    if argv is None:
        argv = sys.argv[1:]
    
    r = cm.access(argv, out='con')

    # Check if output to console
    if cm.output=='json':
        from cmind import utils
        utils.dump_safe_json(r)
    elif r['return']>0 and (cm.output is None or cm.output=='con'):
        cm.error(r)

    sys.exit(r['return'])


############################################################
def parse(cmd):
    """
    Parse CM command line.

    Args:
        cmd (str | list) : arguments as a string or list

    Returns:
        Dictionary:
            return (int): return code == 0 if no error 
                                      >0 if error

            (error) (str): error string if return>0

            cm_input (dict): CM input
    """

    # If input is string, convert to argv
    # We use shlex to properly convert ""
    if cmd is None:
        argv = []

    elif type(cmd) == str:
        import shlex
        argv = shlex.split(cmd)
    
    else:
        argv = cmd

    # Positional arguments
    cm_input = {}

    # First argument: automation
    special_cli_characters=['-', '@']

    for key in ['action', 'automation']:
        if len(argv) > 0:
            x = argv[0].strip()
            if x != '' and x[0] not in special_cli_characters:
                cm_input[key] = argv.pop(0)

    # Check if just one artifact or multiple ones
    artifact=''
    artifacts=[] # Only added if more than 1 artifact!
    
    for a in argv:
        if a.startswith('@'):
            # Load JSON or YAML file
            from cmind import utils
            r = utils.load_json_or_yaml(file_name = a[1:], check_if_exists=True)
            if r['return'] >0 : return r

            meta = r['meta']
            
            cm_input.update(meta)

        elif not a.startswith('-'):
            # artifact
            if artifact=='':
                artifact=a
                cm_input['artifact']=a

            artifacts.append(a)
        else:
            # flags
            if '=' in a:
               key,value = a.split('=')
               value=value.strip()
            else:
               key=a
               value=True

            if key.startswith('-'): key=key[1:]
            if key.startswith('-'): key=key[1:]

            if key.endswith(','): 
               key = key[:-1]
               value = value.split(',') if value!="" else []
           
            if '.' in key:
               keys = key.split('.')
               new_cm_input = cm_input

               first = True
               
               for key in keys[:-1]:
                   if first:
                       key = key.replace('-','_')
                       first = False
                   
                   if key not in new_cm_input:
                      new_cm_input[key] = {}
                   new_cm_input = new_cm_input[key]

               new_cm_input[keys[-1]]=value
            else:
               key = key.replace('-','_')
               cm_input[key] = value

    # Add artifacts if > 1
    if len(artifacts) > 1:
        cm_input['artifacts'] = artifacts

    return {'return':0, 'cm_input':cm_input}

if __name__ == "__main__":
    run()
