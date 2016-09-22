#
# Collective Knowledge
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#

import unittest
import sys
import os
from contextlib import contextmanager

ck=None # Will be updated by CK (initialized CK kernel) 

def dummy_exit(code):
    print('Exit code: ' + str(code))

def get_io(buf=''):
    if sys.version_info[0]>2:
       import io
       return io.StringIO(buf)
    else:
       from StringIO import StringIO
       return StringIO(buf)

@contextmanager
def tmp_file(suffix='', prefix='ck-test-', content=''):
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
def tmp_dir(suffix='', prefix='ck-test-', cwd=False):
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
def tmp_sys(input_buf=''):
    saved_stdout = sys.stdout
    saved_stdin = sys.stdin
    saved_exit = sys.exit
    try:
        out_stream = get_io()
        in_stream = get_io(input_buf)
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
def tmp_cfg(cfg_key, cfg_value='yes'):
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
def tmp_repo(name='ck-test-repo'):
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
