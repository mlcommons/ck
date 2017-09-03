#
# Collective Knowledge
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin
#

import unittest
import os

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel) 

# The value added to the number of failed tests to form the return code, when some tests are failed.
# If return code is less or equal than this value (but more than 0), this means execution error.
# If return code is more, than this value, this means (return code - this value) tests failed.
# E.g. return code 113 would mean 13 failed tests. This may be convenient for writing shell scripts.
# If return code is 0, this means everything's fine and all tests passed.
test_fail_retcode_addition = 100

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
# Run tests for all modules in all repos

def run(i):
    """
    Input:  {
              (out)                 - output
              (repo_uoa)            - repository for run tests for. If not set, runs tests for all repositories
              (test_module_uoa)     - module for tun tests for. If not set, runs tests for all modules
              (test_file_pattern)   - test file pattern. If not given, the default if 'test*.py'. 
                                      Only tests from files that comply with the pattern, will be executed.
              (test_names)          - comma-separated names of the test methods to run. If not set, all methods are run
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error. This error means test execution failed.
                                            If some tests are failed, but the process overall succeded,
                                            the return value is 0.
              
              (error)      - error message

              (stats) {
                        tests_run      - integer, total number of tests run
                        tests_failed   - integer, total number of tests failed by all reasons. Detailed results are
                                         provided in the 'results' field (see below)
                      }

              (repo_results)   - list of results for each repo. 
                                 Each list item is what 'run_data_tests' returned for this repo.
            }

    """

    ret_code = 0
    test_module_uoa = i.get('test_module_uoa', '')
    test_file_pattern = i.get('test_file_pattern', '')
    test_names = i.get('test_names', '')

    repo_uoas = []
    if '' == i.get('repo_uoa', ''):
       r = ck.list_data({'module_uoa': 'repo', 'cid': 'repo:*', 'data_uoa': '*'})
       if r['return']>0:
          return r
       repo_uoas = map(lambda r: r['data_uoa'], r['lst'])
    else:
       repo_uoas = [i['repo_uoa']]

    ret = {
       'return': 0,
       'stats': { 'tests_run': 0, 'tests_failed': 0 },
       'repo_results': []
    }
    out = 'con' if i.get('out','') == 'con' else ''
    for repo_uoa in repo_uoas:
        list_data = {'repo_uoa': repo_uoa}
        if '' != test_module_uoa:
           list_data['data_uoa'] = test_module_uoa
        r = run_data_tests({'list_data': list_data, 'out': out, 
                            'test_file_pattern': test_file_pattern, 'test_names': test_names})
        if is_execution_error(r):
           # execution error happened - fail fast
           ret['return'] = r['return']
           ret['error'] = r.get('error', '')
           return ret

        ret['stats']['tests_run'] += r['stats']['tests_run']
        ret['stats']['tests_failed'] += r['stats']['tests_failed']
        ret['repo_results'].append(r)

    return polish_return_value(ret)

##############################################################################
# Run tests for modules/repos specified by the given criteria

def run_data_tests(i):
    """
    Input:  {
              list_data             - the same dict as the input of ck.list_data()
              (out)                 - output
              (test_file_pattern)   - test file pattern. If not given, the default if 'test*.py'. 
                                      Only tests from files that comply with the pattern, will be executed.
              (test_names)          - comma-separated names of the test methods to run. If not set, all methods are run
            }

    Output: {
              return         - return code =  0, if successful
                                           >  0, if error. This error means test execution failed.
                                              If some tests are failed, but the process overall succeded,
                                              the return value is 0.

              (error)        - error message
              
              (repo_uoa)     - repo_uoa, if provided in the input
              
              (stats) {
                        tests_run      - integer, total number of tests run
                        tests_failed   - integer, total number of tests failed by all reasons. Detailed results are
                                         provided in the 'results' field (see below)
                      }

              (module_results)   - list of results for each module. 
                                   Each list item is what 'run_module_tests' returned for this module.
            }

    """

    repo_uoa = i['list_data'].get('repo_uoa', '')
    test_file_pattern = i.get('test_file_pattern', '')
    test_names = i.get('test_names', '')

    r = ck.list_data(i['list_data'])
    if r['return']>0:
       return r

    modules_lst = r['lst']

    ret = {
       'return': 0,
       'stats': { 'tests_run': 0, 'tests_failed': 0 },
       'module_results': []
    }
    out = 'con' if i.get('out','') == 'con' else ''
    for m in modules_lst:
#        print (m,repo_uoa,out,test_file_pattern, test_names)
        r = run_module_tests({'module': m, 'repo_uoa': repo_uoa, 'out': out, 
                              'test_file_pattern': test_file_pattern, 'test_names': test_names})
        if is_execution_error(r):
           # execution error happened - fail fast
           ret['return'] = r['return']
           ret['error'] = r.get('error', '')
           return ret

        ret['stats']['tests_run'] += r['stats']['tests_run']
        ret['stats']['tests_failed'] += r['stats']['tests_failed']
        ret['module_results'].append(r)

    return polish_return_value(ret)

##############################################################################
# Run tests for a single module

def run_module_tests(i):
    """
    Input:  {
              module                - module dict, must have 'path' and 'data_uoa' keys
              (repo_uoa)            - repo_uoa of that module. Will be printed on the console
              (out)                 - output
              (test_file_pattern)   - test file pattern. If not given, the default if 'test*.py'. 
                                      Only tests from files that comply with the pattern, will be executed.
              (test_names)          - comma-separated names of the test methods to run. If not set, all methods are run
            }

    Output: {
              return                 - return code =  0, if successful
                                                   >  0, if error. This error means test execution failed. 
                                                      If some tests are failed, but the process overall succeded,
                                                      the return value is 0.

              (error)                - error message
              
              (module_uoa)           - module UOA

              (repo_uoa)             - repo UOA (may be an empty string, if not provided in the input)

              (stats) {
                        tests_run      - integer, total number of tests run
                        tests_failed   - integer, total number of tests failed by all reasons. Detailed results are
                                         provided in the 'results' field (see below)
                      }

              (results) {
                          errors                - list of test errors (unexpected exceptions in tests)
                          failures              - list of test failures (cases when an assertion is failed in test)
                          unexpected_successes  - list of unexpected successes (when a test should fail but succeded)
                        }
            }

    """

    import os

    module = i['module']
    repo_uoa = i.get('repo_uoa', '')

    ret = {
       'return': 0,
       'module_uoa': module['data_uoa'],
       'repo_uoa': repo_uoa,
       'stats': { 
          'tests_run' : 0,
          'tests_failed': 0
       },
       'results': {
          'errors': [],
          'failures': [],
          'unexpected_successes': []
       }
    }

    o = i.get('out', '')

    tests_path = os.path.join(module['path'], 'test')
    if not os.path.isdir(tests_path):
       return ret

    test_file_pattern = i.get('test_file_pattern', '')
    if '' == test_file_pattern.strip():
       test_file_pattern = 'test*.py'

    test_names = i.get('test_names', '')
    test_names_list = None
    if '' != test_names:
      test_names_list = list(map(str.strip, test_names.split(',')))
    suite = CkTestLoader(test_names_list).discover(tests_path, pattern=test_file_pattern)

    prefix = repo_uoa
    if prefix != '':
       prefix += ':'

    if o == 'con':
       ck.out('*** Running tests for ' + prefix + module['data_uoa'])

    test_result = None
    if o == 'con':
       test_result = unittest.TextTestRunner().run(suite)
    else: # pragma: no cover
       # supress all output
       with open(os.devnull, 'w') as f:
          test_result = unittest.TextTestRunner(stream=f).run(suite)

    ret['stats']['tests_run'] = test_result.testsRun
    ret['stats']['tests_failed'] = len(test_result.errors) + len(test_result.failures) + len(test_result.unexpectedSuccesses)

    ret['results']['errors'] = convert_error_tuples(test_result.errors)
    ret['results']['failures'] = convert_error_tuples(test_result.failures)
    ret['results']['unexpected_successes'] = convert_error_tuples(test_result.unexpectedSuccesses)

    return polish_return_value(ret)

def is_execution_error(r):
    return 0 < r['return'] and r['return'] <= test_fail_retcode_addition

def polish_return_value(ret):
    failed_count = ret['stats']['tests_failed']
    if failed_count > 0:
       ret['return'] = test_fail_retcode_addition + failed_count
       ret['error'] = str(failed_count) + ' test(s) failed'
    return ret

def convert_error_tuples(list): # pragma: no cover
    ret = []
    for t in list:
        test_case, traceback = t
        ret.append({'test': test_case.id(), 'traceback': traceback})
    return ret

class CkTestLoader(unittest.TestLoader):
  def __init__(self, test_names=None):
      r = ck.load_module_from_path({'path': work['path'], 'module_code_name': 'test_util', 'skip_init': 'yes'})
      if r['return']>0:
        raise Exception('Failed to load test_util module')
      self.test_util = r['code']
      self.test_names = test_names

  def _is_test_name_accepted(self, n):
      return n in self.test_names

  def getTestCaseNames(self, testCaseClass):
      ret = super(CkTestLoader, self).getTestCaseNames(testCaseClass)
      if self.test_names is not None:
        ret = list(filter(self._is_test_name_accepted, ret))
      return ret

  def loadTestsFromModule(self, module, pattern=None):
      module.ck = ck
      module.cfg = cfg
      module.work = work
      module.test_util = self.test_util
      return super(CkTestLoader, self).loadTestsFromModule(module, pattern)

##############################################################################
# show cmd

def cmd(i): # pragma: no cover
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
