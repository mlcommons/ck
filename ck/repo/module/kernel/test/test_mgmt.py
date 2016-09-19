import unittest
import os.path

ck=None # Will be updated by CK (initialized CK kernel)

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

            self.assertEqual('ck-test-abcd', r['data_uoa'])
            self.assertEqual('ck-test-abcd', r['data_name'])
            self.assertEqual('local', r['repo_uoa'])

            self.assertEqual({}, ck.load_meta_from_path({'path':path})['dict'])

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
            'action': 'search'})
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

            # TODO: uncomment this check, when remove_action is fixed
            # r = ck.list_actions(entry)
            # self.assertEqual(0, r['return'])
            # lst = r['actions']
            # self.assertEqual(0, len(lst))
        finally:
            r = ck.remove(entry)
            self.assertEqual(0, r['return'])


