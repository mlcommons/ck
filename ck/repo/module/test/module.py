#
# Collective Knowledge
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin
#

import unittest

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
# Run tests

def run(i):
    """
    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    # run tests for default modules
    r = ck.list_data({'repo_uoa':'default'})
    kernel_modules_lst = r['lst']

    for kernel_module in kernel_modules_lst:
      run_module_tests('kernel:' + kernel_module['data_uoa'], kernel_module)

    return {'return':0}

def run_module_tests(name, module):
  import os

  tests_path = os.path.join(module['path'], 'test')
  if not os.path.isdir(tests_path):
    return {'return': 0}

  suite = CkTestLoader().discover(tests_path)
  ck.out('*** Running tests for ' + name)
  unittest.TextTestRunner().run(suite)

  return {'return':0}

class CkTestLoader(unittest.TestLoader):
  def loadTestsFromModule(self, module, pattern=None):
    module.ck = ck
    return unittest.TestLoader.loadTestsFromModule(self, module, pattern)

##############################################################################
# show cmd

def cmd(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    ck.out('Command line: ')
    ck.out('')

    import json
    cmd=json.dumps(i, indent=2)

    ck.out(cmd)

    return {'return':0}
