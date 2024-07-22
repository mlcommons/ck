# Collective Mind command line wrapper
#
# Written by Grigori Fursin

import sys

############################################################
def run(argv = None):
    """
    Run CM automation actions from the command line. 

    CM command line format:

    cm {action} {automation} (artifacts) (--flags) (@input.yaml) (@input.json)

    Args:
        argv (list | string): command line arguments

    Returns: 
        (CM return dict):

        * return (int): return code == 0 if no error and >0 if error
        * (error) (str): error string if return>0

        * Output from a CM automation action

    """

    # Access CM
    from cmind.core import CM

    cm = CM()

    if argv is None:
        argv = sys.argv[1:]

    r = cm.access(argv, out='con')

    # Check if save to json
    if cm.save_to_json != '':
        from cmind import utils
        utils.save_json(cm.save_to_json, meta=r)

    # Check if output to console
    if cm.output=='json':
        from cmind import utils
        utils.dump_safe_json(r)

    elif r['return']>0 and (cm.output is None or cm.output=='con'):
        cm.error(r)

    sys.exit(r['return'])

############################################################
def run_script(argv = None):
    """
    Shortcut to "cm run script ..."

    CM command line format:

    Args:
        argv (list | string): command line arguments

    Returns: 
        (CM return dict):

        * return (int): return code == 0 if no error and >0 if error
        * (error) (str): error string if return>0

        * Output from a CM automation action

    """

    # Access CM
    if argv is None:
        argv = sys.argv[1:]

    return run(['run', 'script'] + argv)

############################################################
def docker_script(argv = None):
    """
    Shortcut to "cm docker script ..."

    CM command line format:

    Args:
        argv (list | string): command line arguments

    Returns: 
        (CM return dict):

        * return (int): return code == 0 if no error and >0 if error
        * (error) (str): error string if return>0

        * Output from a CM automation action

    """

    # Access CM
    if argv is None:
        argv = sys.argv[1:]

    return run(['docker', 'script'] + argv)

############################################################
def gui_script(argv = None):
    """
    Shortcut to "cm gui script ..."

    CM command line format:

    Args:
        argv (list | string): command line arguments

    Returns: 
        (CM return dict):

        * return (int): return code == 0 if no error and >0 if error
        * (error) (str): error string if return>0

        * Output from a CM automation action

    """

    # Access CM
    if argv is None:
        argv = sys.argv[1:]

    return run(['gui', 'script'] + argv)

############################################################
def run_experiment(argv = None):
    """
    Shortcut to "cm run experiment ..."

    CM command line format:

    Args:
        argv (list | string): command line arguments

    Returns: 
        (CM return dict):

        * return (int): return code == 0 if no error and >0 if error
        * (error) (str): error string if return>0

        * Output from a CM automation action

    """

    # Access CM
    if argv is None:
        argv = sys.argv[1:]

    return run(['run', 'experiment'] + argv)

############################################################
def parse(cmd):
    """
    Parse CM command line into CM input dictionary.

    Args:
        cmd (str | list) : arguments as a string or list

    Returns:
        (CM return dict):

        * return (int): return code == 0 if no error and >0 if error
        * (error) (str): error string if return>0

        * cm_input (dict): CM unified input to the CM access function

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

    for index in range(0, len(argv)):
        a=argv[index]

        if a=='--':
            unparsed = [] if index>len(argv) else argv[index+1:]
            cm_input['unparsed_cmd']=unparsed
            break

        elif a.startswith('@'):
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
            else:
                artifacts.append(a)
        else:
            # flags
            j = a.find('=') # find first =
            if j>0:
               key = a[:j].strip()
               value = a[j+1:].strip()
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

    # Add extra artifacts if specified
    if len(artifacts) > 0:
        cm_input['artifacts'] = artifacts

    cm_input['cmd'] = cmd

    return {'return':0, 'cm_input':cm_input}

if __name__ == "__main__":
    run()
