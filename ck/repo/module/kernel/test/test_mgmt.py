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

            r = ck.remove(merge(entry, {'module_uoa': 'test'}))
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
