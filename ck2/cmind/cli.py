# Collective Mind command line wrapper

import sys

def run(argv = None):
    """
    Run CM action from the command line.

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
