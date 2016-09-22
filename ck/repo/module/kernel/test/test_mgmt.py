import unittest
import os
import shutil
import tempfile
import sys
from contextlib import contextmanager

ck=None           # Will be updated by CK (initialized CK kernel)
test_util=None    # Will be updated by CK (initialized CK test utils)

def merge(dict1, dict2):
    ret = dict1.copy()
    ret.update(dict2)
    return ret

# Tests for repo/module/entry management operations like creating, adding actions, deleting, etc.
# Generally, these are more complex tests, then those from 'test_kernel.py'. These tests
# may take some time to execute, they may require Internet connection, etc.
class TestMgmt(unittest.TestCase):

    def test_entry_crud(self):
        entry = {'module_uoa': 'kernel', 'repo_uoa': 'local', 'data_uoa': 'ck-test-abcd'}
        r = ck.add(entry)
        self.assertEqual(0, r['return'])
        try:
            self.assertIn('data_uid', r)
            self.assertIn('data_name', r)
            self.assertIn('path_module', r)

            path = r['path']
            uid = r['data_uid']

            self.assertEqual('ck-test-abcd', r['data_uoa'])
            self.assertEqual('ck-test-abcd', r['data_name'])
            self.assertEqual('local', r['repo_uoa'])

            self.assertEqual({}, ck.load_meta_from_path({'path':path})['dict'])

            module_path = os.path.join(ck.find_path_to_repo({'repo_uoa': 'local'})['path'], 'kernel')
            r = ck.find_path_to_entry({'path': module_path, 'data_uoa': uid})
            self.assertEqual(0, r['return'])
            self.assertEqual(path, r['path'])

            missing_data = ck.gen_uid({})['data_uid']
            r = ck.find_path_to_entry({'path': module_path, 'data_uoa': missing_data})
            self.assertEqual(-1, r['return'])

            meta_dict = {'a': 1, 'b': [2, 3]}
            r = ck.update(merge(entry, {'dict': meta_dict}))
            self.assertEqual(0, r['return'])
            
            self.assertEqual(meta_dict, ck.load_meta_from_path({'path':path})['dict'])

            r = ck.rename(merge(entry, {'new_data_uoa': 'ck-test-0123'}))
            self.assertEqual(0, r['return'])

            self.assertNotEqual(meta_dict, ck.load_meta_from_path({'path':path})['return'])

            # rename back
            r = ck.rename(merge(entry, {'data_uoa': 'ck-test-0123', 'new_data_uoa': 'ck-test-abcd'}))
            self.assertEqual(0, r['return'])

            r = ck.copy(merge(entry, {'new_data_uoa': 'ck-test-abcd-copy'}))
            self.assertEqual(0, r['return'])
            self.assertEqual(path + '-copy', r['path'])

            r = ck.move(merge(entry, {'data_uoa': 'ck-test-abcd-copy', 'new_module_uoa': 'test', 'new_data_uoa': 'ck-test-abcd'}))
            self.assertEqual(0, r['return'])
            self.assertNotEqual(0, ck.load_meta_from_path({'path': path + '-copy'})['return'])
            self.assertEqual(meta_dict, ck.load_meta_from_path({'path': r['path']})['dict'])

            r = ck.delete(merge(entry, {'module_uoa': 'test'}))
            self.assertEqual(0, r['return'])

            fname = path + '/test.txt'
            with open(fname, 'w') as f:
                f.write('test\n')
            self.assertTrue(os.path.isfile(fname))

            r = ck.delete_file(merge(entry, {'filename': 'test.txt'}))
            self.assertEqual(0, r['return'])
            self.assertFalse(os.path.isfile(fname))

        finally:
            r = ck.remove(entry)
            self.assertEqual(0, r['return'])

    def test_perform_remote_action(self):
        r = ck.perform_remote_action({
            'module_uoa': 'kernel', 
            'remote_server_url': 'http://cknowledge.org/repo/ck.php?',
            'data_uoa': 'default',
            'repo_uoa': 'default',
            'action': 'search',
            'cid': 'invalid_cid_for_deletion'})
        self.assertEqual(0, r['return'])
        lst = r['lst']
        self.assertEqual(1, len(lst))
        r = lst[0]
        self.assertEqual('kernel', r['module_uoa'])
        self.assertEqual('default', r['data_uoa'])
        self.assertEqual('default', r['repo_uoa'])
        self.assertIn('repo_uid', r)
        self.assertIn('module_uid', r)
        self.assertIn('data_uid', r)
        self.assertIn('path', r)

        with test_util.tmp_sys():
            r = ck.perform_remote_action({
                'module_uoa': 'kernel',
                'remote_server_url': 'http://cknowledge.org/repo/ck.php?',
                'data_uoa': 'default',
                'repo_uoa': 'default',
                'action': 'search',
                'out': 'con'})
            self.assertEqual(0, r['return'])
            self.assertEqual('default:kernel:default', sys.stdout.getvalue().strip())

        r = ck.perform_remote_action({
            'module_uoa': 'kernel', 
            'remote_server_url': 'http://cknowledge.org/repo/ck.php?',
            'data_uoa': 'default',
            'repo_uoa': 'default',
            'action': 'push',
            'cids': ['']})
        self.assertEqual(1, r['return'])
        self.assertEqual('filename is empty', r['error'])

        missing_filename = ck.gen_uid({})['data_uid']
        r = ck.perform_remote_action({
            'module_uoa': 'kernel', 
            'remote_server_url': 'http://cknowledge.org/repo/ck.php?',
            'data_uoa': 'default',
            'repo_uoa': 'default',
            'action': 'push',
            'filename': missing_filename})
        self.assertEqual(1, r['return'])
        self.assertEqual('file '+missing_filename+' not found', r['error'])

        with test_util.tmp_file(content='abcd') as fname:
            missing_user = ck.gen_uid({})['data_uid']
            missing_pass = ck.gen_uid({})['data_uid']
            r = ck.perform_remote_action({
                'module_uoa': 'kernel', 
                'remote_server_url': 'http://cknowledge.org/repo/ck.php?',
                'data_uoa': 'default',
                'repo_uoa': 'default',
                'action': 'push',
                'filename': fname,
                'remote_server_user': missing_user,
                'remote_server_pass': missing_pass})
            self.assertEqual(1, r['return'])
            self.assertEqual('CK error: writing to default repo is forbidden!', r['error'].strip())

        with test_util.tmp_dir(cwd=True):
            r = ck.perform_remote_action({
                'module_uoa': 'kernel', 
                'remote_server_url': 'http://cknowledge.org/repo/ck.php?',
                'data_uoa': 'default',
                'repo_uoa': 'default',
                'action': 'pull',
                'filename': '.cm/meta.json',
                'out': 'con'})
            self.assertEqual(0, r['return'])

    def test_actions_crud(self):
        entry = {
            'module_uoa': 'module',
            'repo_uoa': 'local',
            'data_uoa': 'ck-test-abcd',
            'common_func': 'yes',
            'action': 'add',
            'dict': {'license': '1', 'copyright': '2', 'developer_email': '3', 'actions': {}, 'developer_webpage': '4', 'developer': '5', 'desc': 'abcd'}, 
            'sort_keys': 'yes'
        }
        r = ck.add(entry)
        self.assertEqual(0, r['return'])
        try:
            r = ck.add_action(merge(entry, {'func': 'test_func', 'desc': 'test descr', 'skip_appending_dummy_code': 'yes'}))
            self.assertEqual(0, r['return'])

            r = ck.list_actions(entry)
            self.assertEqual(0, r['return'])
            lst = r['actions']
            self.assertEqual(1, len(lst))
            self.assertEqual('test descr', lst['test_func']['desc'])

            r = ck.remove_action(merge(entry, {'func': 'test_func'}))
            self.assertEqual(0, r['return'])

            r = ck.list_actions(entry)
            self.assertEqual(0, r['return'])
            lst = r['actions']
            self.assertEqual(0, len(lst))
        finally:
            r = ck.remove(entry)
            self.assertEqual(0, r['return'])

    def test_zip_unzip(self):
        with test_util.tmp_file() as fname:
            r = ck.zip({'action': 'zip', 'repo_uoa': 'default', 'module_uoa': 'module', 'data_uoa': 'repo', 'archive_name': fname})
            self.assertEqual(0, r['return'])
            self.assertTrue(os.path.isfile(fname))

            dirname = tempfile.mkdtemp()
            self.assertEqual([], os.listdir(dirname))
            try:
                r = ck.unzip_file({'archive_file': fname, 'path': dirname})
                files = os.listdir(dirname)
                self.assertNotEqual([], files)
                self.assertIn('kernel', files)
                self.assertIn('module', files)
                self.assertIn('repo', files)
                self.assertIn('test', files)
            finally:
                shutil.rmtree(dirname)
