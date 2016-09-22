#
# Collective Knowledge
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin
#

import unittest
import sys
import os
from contextlib import contextmanager

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
# Run tests for all modules in all repos

def run(i):
    """
    Input:  {
              (out)                 - output
              (repo_uoa)            - repository for run tests for. If not set, runs tests for all repositories
              (test_module_uoa)     - module for tun tests for. If not set, runs tests for all modules
              (test_file_pattern)   - test file pattern. If not given, the default if 'test*.py'. 
                                      Only tests from files that comply with the pattern, will be executed.
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
        r = run_data_tests({'list_data': list_data, 'out': out, 'test_file_pattern': test_file_pattern})
        if r['return']>0: 
           ret['return'] = r['return']
           ret['error'] = r['error']
           return ret

        ret['stats']['tests_run'] += r['stats']['tests_run']
        ret['stats']['tests_failed'] += r['stats']['tests_failed']
        ret['repo_results'].append(r)

    return ret

##############################################################################
# Run tests for modules/repos specified by the given criteria

def run_data_tests(i):
    """
    Input:  {
              list_data             - the same dict as the input of ck.list_data()
              (out)                 - output
              (test_file_pattern)   - test file pattern. If not given, the default if 'test*.py'. 
                                      Only tests from files that comply with the pattern, will be executed.
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
        r = run_module_tests({'module': m, 'repo_uoa': repo_uoa, 'out': out, 'test_file_pattern': test_file_pattern})
        if r['return']>0:
           ret['return'] = r['return']
           ret['error'] = r['error']
           return ret

        ret['stats']['tests_run'] += r['stats']['tests_run']
        ret['stats']['tests_failed'] += r['stats']['tests_failed']
        ret['module_results'].append(r)

    return ret

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

    suite = CkTestLoader().discover(tests_path, pattern=test_file_pattern)
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

    return ret

def convert_error_tuples(list): # pragma: no cover
    ret = []
    for t in list:
        test_case, traceback = t
        ret.append({'test': test_case.id(), 'traceback': traceback})
    return ret

def dummy_exit(code):
    print('Exit code: ' + str(code))

class CkTestUtil:

  def get_io(self, buf=''):
      if sys.version_info[0]>2:
         import io
         return io.StringIO(buf)
      else:
         from StringIO import StringIO
         return StringIO(buf)

  @contextmanager
  def tmp_file(self, suffix='', prefix='ck-test-', content=''):
      fname = ck.gen_tmp_file({'suffix': suffix, 'prefix': prefix})['file_name']
      try:
          if content != '':
             with open(fname, 'w') as f:
                 f.write(content)            
          yield fname
      finally:
          try:
              os.remove(fname)
          except OSError:
              pass

  @contextmanager
  def tmp_dir(self, suffix='', prefix='ck-test-', cwd=False):
      import shutil
      import tempfile

      saved_cwd = os.getcwd()
      dname = tempfile.mkdtemp()
      try:
          if cwd:
             os.chdir(dname)
          yield dname
      finally:
          if cwd:
             os.chdir(saved_cwd)
             
          try:
              shutil.rmtree(dname)
          except OSError:
              pass

  @contextmanager
  def tmp_sys(self, input_buf=''):
      saved_stdout = sys.stdout
      saved_stdin = sys.stdin
      saved_exit = sys.exit
      try:
          out_stream = self.get_io()
          in_stream = self.get_io(input_buf)
          if not hasattr(in_stream, 'encoding'):
              in_stream.encoding = 'utf8'
          sys.stdout = out_stream
          sys.stdin = in_stream
          sys.exit = dummy_exit

          yield
      finally:
          sys.stdout = saved_stdout
          sys.stdin = saved_stdin
          sys.exit = saved_exit

  @contextmanager
  def tmp_cfg(self, cfg_key, cfg_value='yes'):
      saved_value = ck.cfg.get(cfg_key, None)
      try:
          ck.cfg[cfg_key] = cfg_value
          yield
      finally:
          if saved_value is None:
             ck.cfg.pop(cfg_key, None)
          else:
             ck.cfg[cfg_key] = saved_value

  @contextmanager
  def tmp_repo(self, name='ck-test-repo'):
      r = ck.access({'module_uoa': 'repo', 'quiet': 'yes', 'data_uoa': name, 'action': 'add'})
      if 0 != r['return']:
         raise AssertionError('Failed to create a temporary repo ' + name)
      path = r['dict']['path']
      try:
          yield r
      finally:
          r = ck.access({'module_uoa': 'repo', 'quiet': 'yes', 'data_uoa': name, 'action': 'remove'})
          if 0 != r['return']:
             raise AssertionError('Failed to remove temporary repo ' + name + ' at location ' + path)

class CkTestLoader(unittest.TestLoader):
  def loadTestsFromModule(self, module, pattern=None):
      module.ck = ck
      module.cfg = cfg
      module.work = work
      module.test_util = CkTestUtil()
      return unittest.TestLoader.loadTestsFromModule(self, module, pattern)

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
