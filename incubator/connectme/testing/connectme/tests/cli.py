import os

###########################################################################
def run(argv=None):
    """
    Run CM from command line.

    Args:
        argv (str | list): CM input
    
    Returns:
        Dictionary:
            return (int): return code == 0 if no error 
                                      >0 if error

            (error) (str): error string if return>0

            data from a given action
    """

    # Aggregate CM input from argv
    i = {}

    con = False

    if not argv:
        import sys
        argv = sys.argv[1:]

        con = True

    # Parse command line
    r = parse(argv)

    args = r['args']
    options = r['options']
    extra = r['extra']

    # Useful if input is string
    argv = r['argv'] 

    # Check explicit help
    if (len(args)==0 and ('h' in options or 'help' in options)) or \
       (len(args)==0 and len(options)==0):
        print_help()
        exit(0)
        
    # Aggregate into 1 dict:
    i.update(options)

    i['extra_cmd'] = extra

    if len(args)>0:
        i['module']=args[0]
    if len(args)>1:
        i['action']=args[1]
    if len(args)>2:
        i['data']=args[2]
    if len(args)>3:
        i['args']=args[3:]
    
    # Access CM
    from connectme import CM

    cm = CM(con = con)

    r = cm.init()
    if r['return']>0: return r

    return cm.access(i, argv)

###########################################################################
def print_help():
    """
    Print command line help.
    """

    print('usage: cm [module (data class)] [action] [data] [arguments] [options]')


###########################################################################
def parse(cmd):
    """
    Parse command line.

    Args:
        cmd (str | list) : arguments as a string or list

    Returns:
        Dictionary::

            args (list) : list of positional arguments
            options (dict) : options
            extra (str): string after --
    """

    argv=cmd

    # If input is string, convert to argv
    if type(cmd) == str:
        import shlex
        argv=shlex.split(cmd)

    # Positional arguments
    args = []

    # Options
    options = {}

    # Extra after --
    extra = ''

    # Parse
    for i in range(0, len(argv)):
        a=argv[i]

        # Check if args or options
        j=a.find('=')

        if a=='--':
            extra = ' '.join(argv[i+1:])
            break

        elif a.startswith('@'):
            file_name=a[1:]

            if os.path.isfile(file_name):
                from connectme import io
                
                r = io.load_json_or_yaml(file_name)
                if r['return']>0: return r

                options.update(r['data'])
            
        elif j>0 or a.startswith('-') or a.startswith('--'):
            v=True

            k=a
            if j>0:
                v=a[j+1:]
                k=a[:j]

            if k.startswith('--'):
                k = k[2:]
            elif k.startswith('-'):
                k = k[1:]

            options[k] = v
        else:
            args.append(a)
             
    return {'return':0, 'args': args, 'options': options, 'extra': extra, 'argv': argv}

###########################################################################
if __name__ == "__main__":
   r = run()
   exit(r['return'])
