#
# Collective Knowledge
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#

# This module contains function to help writing unit tests. 
# This module is automatically added to each unit test module during 
# execution as the 'test_util' variable (much like the 'ck' variable).
# For examples of the usage of this functions, please looks at the kernel tests 
# (ck/repo/kernel/test/test_*.py files).

import unittest
import sys
import os
from contextlib import contextmanager

ck=None # Will be updated by CK (initialized CK kernel) 

##############################################################################
# Temporary files helper.

@contextmanager
def tmp_file(suffix='', prefix='ck-test-', content=''):
    """
    Yields a temporary file name. If content is given (not empty), 
    creates the file with this content. Remove the file afterwards.
    """

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

##############################################################################
# Temporary directory helper.

@contextmanager
def tmp_dir(suffix='', prefix='ck-test-', cwd=False):
    """
    Yields a temporary directory name (the directory is created). 
    
    If 'cwd' is True, make this directory the working directory. Restores the
    original working directory afterwards.

    Removes the directory and all its content afterwards.
    """

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

##############################################################################
# System streams helper.

@contextmanager
def tmp_sys(input_buf=''):
    """
    Yields nothing, but substitutes standard input, output and error streams with 
    StringIO streams. If 'input_buf' is given, make sure the new input stream
    contains it.

    Also substitutes the standard exit() routine with
    the one which simple prints exit code. 

    Restores the original streams and exit() afterwards.
    """

    saved_stdout = sys.stdout
    saved_stderr = sys.stderr
    saved_stdin = sys.stdin
    saved_exit = sys.exit
    try:
        out_stream = get_io()
        err_stream = get_io()
        in_stream = get_io(input_buf)

        sys.stdout = out_stream
        sys.stderr = err_stream
        sys.stdin = in_stream
        sys.exit = dummy_exit

        yield
    finally:
        sys.stdout = saved_stdout
        sys.stderr = saved_stderr
        sys.stdin = saved_stdin
        sys.exit = saved_exit

##############################################################################
# Temporary configuration helper.

@contextmanager
def tmp_cfg(cfg_key, cfg_value='yes'):
    """
    Yields nothing, but assignes the given configuration key (ck.cfg[cfg_key])
    the given value. Restores the old value afterwards.
    """

    saved_value = ck.cfg.get(cfg_key, None)
    try:
        ck.cfg[cfg_key] = cfg_value
        yield
    finally:
        if saved_value is None:
           ck.cfg.pop(cfg_key, None)
        else:
           ck.cfg[cfg_key] = saved_value

##############################################################################
# Temporary repository helper.

@contextmanager
def tmp_repo(name='ck-test-repo', cfg={}):
    """
    Creates a new repository and yields the information about it.

    Removes the repository afterwards.
    """

    d = {'module_uoa': 'repo', 'quiet': 'yes', 'data_uoa': name, 'action': 'add'}
    d.update(cfg)
    r = ck.access(d)
    if 0 != r['return']:
       raise AssertionError('Failed to create a temporary repo ' + name + ' : ' + r.get('error', None))
    try:
        path = r['dict']['path']
    except Exception:
        path = '<unknown>'
    try:
        yield r
    finally:
        r = ck.access({'module_uoa': 'repo', 'quiet': 'yes', 'data_uoa': name, 'action': 'remove'})
        if 0 != r['return']:
           raise AssertionError('Failed to remove temporary repo ' + name + ' at location ' + path + ' : ' + r.get('error', None))

##############################################################################
# Prints exit code to the system output. Used internally

def dummy_exit(code):
    print('Exit code: ' + str(code))

##############################################################################
# Returns StringIO buffer. Used internnaly

def get_io(buf=''):
    r = ck.string_io(buf)
    if not hasattr(r, 'encoding'):
        r.encoding = 'utf8'
    return r
