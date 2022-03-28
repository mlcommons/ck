# Collective Mind command line wrapper

import sys

def run(argv = None):
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

    # Access CM
    from cmind.kernel import CM

    cm = CM(out='con')

    if argv is None:
        argv = sys.argv[1:]

    r = cm.access(argv)

    ret = r['return']

    # Print error only in CLI
    if ret > 0:
       # Process error: either raise or just print to stderr
       # depending on settings
       cm.error(r)

    sys.exit(ret)


if __name__ == "__main__":
    run()
