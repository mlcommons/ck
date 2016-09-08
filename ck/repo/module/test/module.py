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

    ret_code = 0

    r = ck.list_data({'module_uoa': 'repo', 'cid': 'repo:*', 'data_uoa': '*'})
    if r['return']>0: return r

    for d in r['lst']:
      r = run_data_tests({'list_data': {'repo_uoa': d['data_uoa']}})
      if r['return']>0: 
        ret_code = r['return']

    return {'return':ret_code, 'error': '' if 0 == ret_code else 'Some tests failed'}

def run_data_tests(i):
    """
    Input:  {
              list_data    - the same dict as the input of ck.list_data()
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
            }

    """

    repo_uoa = i['list_data'].get('repo_uoa', '')

    r = ck.list_data(i['list_data'])
    if r['return']>0: return r
    modules_lst = r['lst']

    ret_code = 0
    for m in modules_lst:
      r = run_module_tests({'module': m, 'repo_uoa': repo_uoa})
      if r['return']>0: 
        ret_code = r['return']

    return {'return':ret_code, 'error': '' if 0 == ret_code else 'Some tests failed'}

def run_module_tests(i):
    """
    Input:  {
              module       - module dict, must have 'path' and 'data_uoa' keys
              (repo_uoa)   - repo_uoa of that module. Will be printed on the console
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
            }

    """

    import os

    module = i['module']

    tests_path = os.path.join(module['path'], 'test')
    if not os.path.isdir(tests_path):
      return {'return': 0}

    suite = CkTestLoader().discover(tests_path)
    prefix = i.get('repo_uoa', '')
    if prefix != '':
      prefix += ':'
    ck.out('*** Running tests for ' + prefix + module['data_uoa'])
    test_result = unittest.TextTestRunner().run(suite)

    return { 'return': 0 if test_result.wasSuccessful() else 1 }

class CkTestLoader(unittest.TestLoader):
  def loadTestsFromModule(self, module, pattern=None):
    module.ck = ck
    module.cfg = cfg
    module.work = work
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
