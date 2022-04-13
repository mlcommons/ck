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

    cm = CM()

    if argv is None:
        argv = sys.argv[1:]
    
    r = cm.access(argv, out='con')

    sys.exit(r['return'])


if __name__ == "__main__":
    run()
