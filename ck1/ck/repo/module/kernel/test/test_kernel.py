#
# Collective Knowledge
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#

import unittest
import sys
import os

ck = None           # Will be updated by CK (initialized CK kernel)
test_util = None    # Will be updated by CK (initialized CK test utils)

# Contains new kernel tests. Add new tests here!


class TestKernel(unittest.TestCase):

    def test_out(self):
        with test_util.tmp_sys():
            ck.out('test')
            self.assertEqual('test', sys.stdout.getvalue().strip())

    def test_eout(self):
        with test_util.tmp_sys():
            ck.eout('test')
            self.assertEqual('test', sys.stderr.getvalue().strip())

    def test_err(self):
        with test_util.tmp_sys():
            ck.err({'return': 2, 'error': 'test.'})
            self.assertEqual('Error: test.\nExit code: 2',
                             sys.stdout.getvalue().strip())

    def test_jerr(self):
        with test_util.tmp_sys():
            with self.assertRaises(KeyboardInterrupt):
                ck.jerr({'return': 2, 'error': 'test.'})
            self.assertEqual('Error: test.', sys.stdout.getvalue().strip())

    def test_safe_float(self):
        import math

        self.assertEqual(ck.safe_float(1, 0), 1.0)
        self.assertEqual(ck.safe_float('a', 0), 0)
        self.assertEqual(ck.safe_float('-5.35', 0), -5.35)
        self.assertEqual(ck.safe_float('Infinity', 0), float('inf'))
        self.assertTrue(math.isnan(ck.safe_float('nan', 0)))

    def test_safe_int(self):
        self.assertEqual(ck.safe_int(1, 0), 1)
        self.assertEqual(ck.safe_int('a', 0), 0)
        self.assertEqual(ck.safe_int('-5', 0), -5)

    def test_safe_get_val_from_list(self):
        self.assertEqual(ck.safe_get_val_from_list([1, 2], 0, 0), 1)
        self.assertEqual(ck.safe_get_val_from_list([1, 2], 1, 0), 2)
        self.assertEqual(ck.safe_get_val_from_list([], 1, 0), 0)

    def test_system_with_timeout(self):
        r = ck.system_with_timeout({'cmd': 'exit 2'})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual(2, r['return_code'])

        r = ck.system_with_timeout({'cmd': 'sleep 5', 'timeout': 0.05})
        self.assertEqual(8, r['return'])

    def test_run_and_get_stdout(self):
        r = ck.run_and_get_stdout(
            {'cmd': ['sh', '-c', 'echo abcd && >&2 echo err && exit 2']})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual(2, r['return_code'])
        self.assertEqual('abcd\n', r['stdout'])
        self.assertEqual('err\n', r['stderr'])

        r = ck.run_and_get_stdout(
            {'cmd': 'sh -c "echo abcd && >&2 echo err && exit 2"'})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual(2, r['return_code'])
        self.assertEqual('abcd\n', r['stdout'])
        self.assertEqual('err\n', r['stderr'])

    def test_get_from_dicts(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'c': 3}
        r = ck.get_from_dicts(d1, 'a', '', d2)
        self.assertEqual(d1, {'b': 2})
        self.assertEqual(d2, {'a': 1, 'c': 3})
        self.assertEqual(1, r)

        ck.get_from_dicts(d1, 'a', 4, d2)
        self.assertEqual(d1, {'b': 2})
        self.assertEqual(d2, {'a': 1, 'c': 3})
        self.assertEqual(1, r)

    def test_convert_iso_time(self):
        r = ck.convert_iso_time({'iso_datetime': 'invalid'})
        self.assertEqual(1, r['return'])

        r = ck.convert_iso_time({'iso_datetime': '2016-09-07T13:47:34.5'})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual(2016, r['datetime_obj'].year)

    def test_convert_str_key_to_int(self):
        self.assertEqual(5, ck.convert_str_key_to_int('5'))
        self.assertEqual(0, ck.convert_str_key_to_int('a'))

    def test_inp(self):
        with test_util.tmp_sys('test input'):
            r = ck.inp({'text': 'test output'})
            self.assertEqual('test output', sys.stdout.getvalue().strip())
            self.assertEqual('test input', r['string'])
            self.assertEqual(0, r['return'], r.get('error', None))

    def test_select(self):
        d = {
            'key0': {'name': 'n0', 'sort': 1},
            'key1': {'name': 'n1', 'sort': 0}
        }
        with test_util.tmp_sys('1\n'):
            r = ck.select({'dict': d, 'title': 'Select:'})

            self.assertEqual(
                'Select:\n\n0) n1\n1) n0\n\nMake your selection (or press Enter for 0):', sys.stdout.getvalue().strip())
            self.assertEqual(0, r['return'], r.get('error', None))
            self.assertEqual('key0', r['string'])

        with test_util.tmp_sys('\n'):
            r = ck.select({'dict': d, 'title': 'Select:',
                           'error_if_empty': 'yes'})
            self.assertEqual(1, r['return'])
            self.assertEqual('selection is empty', r['error'])

        with test_util.tmp_sys('\n'):
            r = ck.select({'dict': d, 'title': 'Select:'})
            self.assertEqual(0, r['return'], r.get('error', None))
            self.assertEqual('key1', r['string'])

        with test_util.tmp_sys('2\n'):
            r = ck.select({'dict': d, 'title': 'Select:'})
            self.assertEqual(1, r['return'])
            self.assertEqual('selection is not recognized', r['error'])

    def test_select_uoa(self):
        lst = [
            {'data_uid': 'uid1', 'data_uoa': 'b'},
            {'data_uid': 'uid2', 'data_uoa': 'a'}
        ]
        with test_util.tmp_sys('1\n'):
            r = ck.select_uoa({'choices': lst})

            self.assertEqual(
                '0) a (uid2)\n1) b (uid1)\n\nSelect UOA (or press Enter for 0):', sys.stdout.getvalue().strip())
            self.assertEqual(0, r['return'], r.get('error', None))
            self.assertEqual('uid1', r['choice'])

        with test_util.tmp_sys('2\n'):
            r = ck.select_uoa({'choices': lst})
            self.assertEqual(1, r['return'])
            self.assertEqual('number is not recognized', r['error'])

    def test_convert_str_tags_to_list(self):
        self.assertEqual([1, 2], ck.convert_str_tags_to_list([1, 2]))
        self.assertEqual(['1', '2'], ck.convert_str_tags_to_list('  1 , 2  '))

    def test_check_writing(self):
        with test_util.tmp_cfg('forbid_global_delete'):
            r = ck.check_writing({'delete': 'yes'})
            self.assertEqual(1, r['return'])

        with test_util.tmp_cfg('forbid_global_writing'):
            r = ck.check_writing({})
            self.assertEqual(1, r['return'])

        with test_util.tmp_cfg('forbid_writing_modules'):
            r = ck.check_writing({'module_uoa': 'module'})
            self.assertEqual(1, r['return'])

        with test_util.tmp_cfg('forbid_writing_to_default_repo'):
            r = ck.check_writing({'repo_uoa': 'default'})
            self.assertEqual(1, r['return'])

        with test_util.tmp_cfg('forbid_writing_to_local_repo'):
            r = ck.check_writing({'repo_uoa': 'local'})
            self.assertEqual(1, r['return'])

        with test_util.tmp_cfg('allow_writing_only_to_allowed'):
            r = ck.check_writing({'repo_uoa': 'default'})
            self.assertEqual(1, r['return'])

        r = ck.check_writing({'repo_uoa': 'default', 'delete': 'yes', 'repo_dict': {
                             'forbid_deleting': 'yes'}})
        self.assertEqual(1, r['return'])

    def test_gen_tmp_file(self):
        with test_util.tmp_file(suffix='.txt') as fname:
            # check we can write to the file
            with open(fname, 'w') as f:
                f.write('test')

        fname = ck.gen_tmp_file({})['file_name']
        self.assertIn(os.sep, fname)

        fname = ck.gen_tmp_file({'remove_dir': 'yes'})['file_name']
        self.assertNotIn(os.sep, fname)

    def test_gen_uid(self):
        r = ck.gen_uid({})
        self.assertEqual(0, r['return'], r.get('error', None))

        uid = r['data_uid']
        self.assertEqual(16, len(uid))

        chars = '0123456789abcdef'
        for c in uid:
            self.assertIn(c, chars)

    def test_is_uid(self):
        self.assertTrue(ck.is_uid('5eac2a24f4a98e90'))

        self.assertFalse(ck.is_uid('a'))
        self.assertFalse(ck.is_uid('5evc2a24f4a98e90'))

    def test_is_uoa(self):
        self.assertTrue(ck.is_uoa('5evac2a24f4a98e90'))
        self.assertTrue(ck.is_uoa(''))

        self.assertFalse(ck.is_uoa('ab#12'))
        self.assertFalse(ck.is_uoa('ab^12'))
        self.assertFalse(ck.is_uoa('5evc2*a24f4a98e90'))
        self.assertFalse(ck.is_uoa('5evc2?a24f4a98e90'))

    def test_prepare_special_info_about_entry(self):
        r = ck.prepare_special_info_about_entry({})
        self.assertEqual(0, r['return'], r.get('error', None))
#        keys = sorted(['engine', 'version', 'author', 'author_email', 'author_webpage', 'license', 'copyright', 'iso_datetime'])
        # min set of keys to check, since other keys can differ depending on user configuration
        keys = ['engine', 'version', 'iso_datetime']
        xkeys = []

        xdict = r['dict'].keys()
        for k in keys:
            if k in xdict:
                xkeys.append(k)
        self.assertEqual(keys, xkeys)

    def test_convert_json_str_to_dict(self):
        r = ck.convert_json_str_to_dict({'str': "{'a': 1, 'b': [2, 3]}"})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual({'a': 1, 'b': [2, 3]}, r['dict'])

    def test_load_json_file(self):
        with test_util.tmp_file(suffix='.json', content='{"a": 1, "b": [2, 3]}') as fname:
            r = ck.load_json_file({'json_file': fname})
            self.assertEqual(0, r['return'], r.get('error', None))
            self.assertEqual({'a': 1, 'b': [2, 3]}, r['dict'])

    def test_load_yaml_file(self):
        with test_util.tmp_file(suffix='.yml', content='a: 1\nb:\n  - 2\n  - 3\n') as fname:
            r = ck.load_yaml_file({'yaml_file': fname})
            self.assertEqual(0, r['return'], r.get('error', None))
            self.assertEqual({'a': 1, 'b': [2, 3]}, r['dict'])

    def test_load_text_file(self):
        content = 'a\nb\nc'
        with test_util.tmp_file(suffix='.txt', content=content) as fname:
            r = ck.load_text_file({'text_file': fname, 'split_to_list': 'yes'})
            self.assertEqual(0, r['return'], r.get('error', None))
            self.assertEqual(str.encode(
                content.replace('\n', os.linesep)), r['bin'])
            self.assertEqual(content, r['string'])
            self.assertEqual(content.strip().split('\n'), r['lst'])

        content = 'a:1\nb:"z"\nc:2'
        with test_util.tmp_file(suffix='.txt', content=content) as fname:
            r = ck.load_text_file(
                {'text_file': fname, 'convert_to_dict': 'yes', 'remove_quotes': 'yes'})
            self.assertEqual(0, r['return'], r.get('error', None))
            self.assertEqual({'a': '1', 'b': 'z', 'c': '2'}, r['dict'])

    def test_substitute_str_in_file(self):
        content = 'a\nb\nc'
        with test_util.tmp_file(suffix='.txt', content=content) as fname:
            r = ck.substitute_str_in_file(
                {'filename': fname, 'string1': 'b', 'string2': 'd'})
            self.assertEqual(0, r['return'], r.get('error', None))
            self.assertEqual('a\nd\nc', ck.load_text_file(
                {'text_file': fname})['string'])

    def test_dumps_json(self):
        d = {'a': 1, 'b': [2, 3]}
        json_str = ck.dumps_json({'dict': d, 'skip_indent': 'yes'})['string']
        parsed_dict = ck.convert_json_str_to_dict(
            {'str': json_str, 'skip_quote_replacement': 'yes'})['dict']
        self.assertEqual(d, parsed_dict)

    def test_merge_dicts(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'c': 3, 'b': {}}
        ck.merge_dicts({'dict1': d1, 'dict2': d2})
        self.assertEqual({'a': 1, 'b': {}, 'c': 3}, d1)

    def test_save_yaml_to_file(self):
        d = {'a': 1, 'b': [2, 3]}
        with test_util.tmp_file(suffix='.yml') as fname:
            r = ck.save_yaml_to_file({'yaml_file': fname, 'dict': d})
            self.assertEqual(0, r['return'], r.get('error', None))

            r = ck.load_yaml_file({'yaml_file': fname})
            self.assertEqual(0, r['return'], r.get('error', None))
            self.assertEqual(d, r['dict'])

    def test_convert_file_to_upload_string(self):
        with test_util.tmp_file(suffix='.txt', content='http://ctuning.org/') as fname:
            r = ck.convert_file_to_upload_string({'filename': fname})
            self.assertEqual(0, r['return'], r.get('error', None))
            self.assertEqual('aHR0cDovL2N0dW5pbmcub3JnLw==',
                             r['file_content_base64'])

        with test_util.tmp_file() as fname:
            r = ck.convert_file_to_upload_string({'filename': fname})
            self.assertEqual(1, r['return'])

    def test_convert_upload_string_to_file(self):
        with test_util.tmp_file(suffix='.txt') as fname:
            r = ck.convert_upload_string_to_file(
                {'file_content_base64': 'aHR0cDovL2N0dW5pbmcub3JnLw==', 'filename': fname})
            self.assertEqual(0, r['return'], r.get('error', None))
            self.assertEqual(fname, r['filename'])

            r = ck.load_text_file({'text_file': fname})
            self.assertEqual(0, r['return'], r.get('error', None))
            self.assertEqual('http://ctuning.org/', r['string'])

        r = ck.convert_upload_string_to_file(
            {'file_content_base64': 'aHR0cDovL2N0dW5pbmcub3JnLw=='})
        fname = r['filename']
        try:
            self.assertEqual(0, r['return'], r.get('error', None))

            r = ck.load_text_file({'text_file': fname})
            self.assertEqual(0, r['return'], r.get('error', None))
            self.assertEqual('http://ctuning.org/', r['string'])
        finally:
            os.remove(fname)

        with test_util.tmp_file(suffix='.txt', content='test') as fname:
            r = ck.convert_upload_string_to_file(
                {'file_content_base64': 'aHR0cDovL2N0dW5pbmcub3JnLw==', 'filename': fname})
            self.assertEqual(1, r['return'])

    def test_convert_ck_list_to_dict(self):
        r = ck.convert_ck_list_to_dict(['a', '--', 1, '2'])
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual({'action': 'a', 'cids': [],
                          'unparsed': [1, '2']}, r['ck_dict'])

        r = ck.convert_ck_list_to_dict(['a', '-k=1'])
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual({'action': 'a', 'cids': [], 'k': '1'}, r['ck_dict'])

        r = ck.convert_ck_list_to_dict(['a', '@@@2'])
        self.assertEqual(1, r['return'])

        r = ck.convert_ck_list_to_dict(['a', '@@@{\'k\': 1}'])
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual({'action': 'a', 'cids': [], 'k': 1}, r['ck_dict'])

        with test_util.tmp_sys('{"k": 1}\n\n'):
            r = ck.convert_ck_list_to_dict(['a', '@@'])
            self.assertEqual(0, r['return'], r.get('error', None))
            self.assertEqual({'action': 'a', 'cids': [], 'k': 1}, r['ck_dict'])

        with test_util.tmp_sys('{"k": 1}\n\n'):
            r = ck.convert_ck_list_to_dict(['a', '@@q'])
            self.assertEqual(0, r['return'], r.get('error', None))
            self.assertEqual({'action': 'a', 'cids': [],
                              'q': {'k': 1}}, r['ck_dict'])

        r = ck.convert_ck_list_to_dict(['a', '@2'])
        self.assertEqual(1, r['return'])

        with test_util.tmp_file(suffix='.tmp', content='{"k": 1}') as fname:
            r = ck.convert_ck_list_to_dict(['a', '@' + fname])
            self.assertEqual(0, r['return'], r.get('error', None))
            self.assertEqual({'action': 'a', 'cids': [], 'k': 1}, r['ck_dict'])
            self.assertFalse(os.path.isfile(fname))

    def test_input_json(self):
        content = '{"a": 1, "b": [2, 3]}\n\n'
        with test_util.tmp_sys(content):
            r = ck.input_json({'text': 'input json'})
            self.assertEqual(0, r['return'], r.get('error', None))
            self.assertEqual('input json', sys.stdout.getvalue().strip())
            self.assertEqual(content.strip(), r['string'])
            self.assertEqual({'a': 1, 'b': [2, 3]}, r['dict'])

    def test_list_all_files(self):
        with test_util.tmp_dir() as fname:
            os.makedirs(fname + '/a')
            os.makedirs(fname + '/b')

            with open(fname + '/a/test.txt', 'a') as f:
                f.write('abc')

            with open(fname + '/b/test.log', 'a') as f:
                f.write('12')

            s = os.sep

            r = ck.list_all_files({'path': fname, 'limit': 10})
            self.assertEqual(0, r['return'], r.get('error', None))
            t = r['list']
            self.assertEqual({'size': 3}, t['a' + s + 'test.txt'])
            self.assertEqual({'size': 2}, t['b' + s + 'test.log'])

            r = ck.list_all_files({'path': fname, 'pattern': '*.txt'})
            self.assertEqual(0, r['return'], r.get('error', None))
            t = r['list']
            self.assertEqual({'size': 3}, t['a' + s + 'test.txt'])
            self.assertEqual(None, t.get('b' + s + 'test.log'))

            r = ck.list_all_files({'path': fname, 'file_name': 'test.txt'})
            self.assertEqual(0, r['return'], r.get('error', None))
            t = r['list']
            self.assertEqual({'size': 3}, t['a' + s + 'test.txt'])

        with test_util.tmp_dir() as fname:
            with open(fname + '/test.txt', 'a') as f:
                f.write('abc')
            with open(fname + '/test.log', 'a') as f:
                f.write('12')
            with open(fname + '/test.abc', 'a') as f:
                f.write('12')

            r = ck.list_all_files({'path': fname, 'limit': 1})
            self.assertEqual(0, r['return'], r.get('error', None))
            self.assertEqual(1, len(r['list']))

            os.makedirs(fname + '/a')
            os.makedirs(fname + '/b')

            with open(fname + '/a/1.txt', 'a') as f:
                f.write('abc')

            with open(fname + '/b/1.log', 'a') as f:
                f.write('12')

            r = ck.list_all_files({'path': fname, 'limit': 1})
            self.assertEqual(0, r['return'], r.get('error', None))
            self.assertEqual(1, len(r['list']))

    def test_save_repo_cache(self):
        r = ck.save_repo_cache({})
        self.assertEqual(0, r['return'], r.get('error', None))

        r = ck.load_json_file({'json_file': ck.work['dir_cache_repo_uoa']})
        self.assertEqual(ck.cache_repo_uoa, r['dict'])

        r = ck.load_json_file({'json_file': ck.work['dir_cache_repo_info']})
        self.assertEqual(ck.cache_repo_info, r['dict'])

    def test_load_repo_info_from_cache(self):
        r = ck.load_repo_info_from_cache({'repo_uoa': 'default'})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual('default', r['data_alias'])
        self.assertEqual('default', r['data_uoa'])

        missing_repo = ck.gen_uid({})['data_uid']
        r = ck.load_repo_info_from_cache({'repo_uoa': missing_repo})
        self.assertEqual(1, r['return'])

        r = ck.load_repo_info_from_cache({'repo_uoa': missing_repo + '='})
        self.assertEqual(1, r['return'])

    def test_find_repo_by_path(self):
        r = ck.find_path_to_repo({'repo_uoa': 'default'})
        r = ck.find_repo_by_path({'path': r['path']})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual('default', r['repo_uoa'])
        self.assertEqual('default', r['repo_alias'])

        r = ck.find_path_to_repo({'repo_uoa': 'local'})
        r = ck.find_repo_by_path({'path': r['path']})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual('local', r['repo_uoa'])
        self.assertEqual('local', r['repo_alias'])

        with test_util.tmp_file() as missing_repo_path:
            r = ck.find_repo_by_path({'path': missing_repo_path})
            self.assertEqual(16, r['return'])

        with test_util.tmp_repo() as r:
            path = r['dict']['path']
            name = r['data_name']
            r = ck.find_repo_by_path({'path': path})
            self.assertEqual(0, r['return'], r.get('error', None))
            self.assertEqual(name, r['repo_uoa'])
            self.assertEqual(name, r['repo_alias'])

    def test_find_path_to_repo(self):
        with test_util.tmp_repo() as r:
            path = r['dict']['path']
            name = r['data_name']
            r = ck.find_path_to_repo({'repo_uoa': name})
            self.assertEqual(0, r['return'], r.get('error', None))
            self.assertEqual(path, r['path'])

        missing_repo = ck.gen_uid({})['data_uid']
        r = ck.find_path_to_repo({'repo_uoa': missing_repo + '='})
        self.assertEqual(1, r['return'])

    def test_find_path_to_data(self):
        missing_data = ck.gen_uid({})['data_uid']
        r = ck.find_path_to_data(
            {'module_uoa': 'default', 'data_uoa': missing_data})
        self.assertEqual(16, r['return'])

    def test_load_module_from_path(self):
        repo_path = ck.find_path_to_repo({'repo_uoa': 'local'})['path']
        missing_module = ck.gen_uid({})['data_uid']
        r = ck.load_module_from_path(
            {'path': repo_path, 'module_code_name': missing_module})
        self.assertEqual(1, r['return'])

        with test_util.tmp_dir() as dname:
            module_name = 'test'
            module_file = os.path.join(dname, module_name + '.py')
            with open(module_file, 'w') as f:
                f.write('pass\n')
            r = ck.load_module_from_path(
                {'path': dname, 'module_code_name': 'test', 'cfg': {'min_kernel_dep': '10'}})
            self.assertEqual(1, r['return'])

    def test_perform_action(self):
        r = ck.perform_action({})
        self.assertEqual(0, r['return'], r.get('error', None))

        with test_util.tmp_dir(cwd=True):
            r = ck.perform_action({'cid': '#'})
            self.assertEqual(16, r['return'])
            self.assertEqual(
                'repository is not detected in the current path', r['error'])

        with test_util.tmp_dir(cwd=True):
            r = ck.perform_action({'cids': ['#']})
            self.assertEqual(16, r['return'])
            self.assertEqual(
                'repository is not detected in the current path', r['error'])

        with test_util.tmp_sys():
            r = ck.perform_action({'cid': 'default:test:', 'cids': [
                                  'default:test:'], 'action': 'cmd'})
            self.assertEqual(0, r['return'], r.get('error', None))
            self.assertTrue(sys.stdout.getvalue(
            ).strip().startswith('Command line:'))

    def test_get_api(self):
        r = ck.get_api({'func': 'list_actions'})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual(
            'List actions in the given CK module\n \nTARGET: should use via ck.kernel.access', r['title'].strip())
        self.assertTrue(
            r['api'].strip().lower().startswith('target audience:'))

        missing_file = ck.gen_uid({})['data_uid'] + '.py'
        with test_util.tmp_cfg('file_kernel_py', missing_file):
            r = ck.get_api({})
            self.assertEqual(1, r['return'])
            self.assertTrue(r['error'].strip().startswith(
                'kernel not found in'))

        r = ck.get_api({'module_uoa': 'test'})
        self.assertEqual(1, r['return'])
        self.assertEqual('function not found', r['error'])

#        with test_util.tmp_sys():
#            r = ck.get_api({'module_uoa': 'test', 'func': 'cmd', 'out': 'con'})
#            self.assertEqual(0, r['return'], r.get('error', None))
#            self.assertTrue(r['api'].strip().startswith('Input:'))
#            self.assertTrue(sys.stdout.getvalue().strip().startswith('Function: show cmd'))
#
#        with test_util.tmp_sys():
#            r = ck.get_api({'module_uoa': 'test', 'func': 'cmd', 'out': 'web'})
#            self.assertEqual(0, r['return'], r.get('error', None))
#            self.assertTrue(r['api'].strip().startswith('Input:'))
#            self.assertTrue(sys.stdout.getvalue().strip().startswith('<B>Function:</B> show cmd'))

    def test_parse_cid(self):
        r = ck.parse_cid({'cid': 'a:b:c'})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual('a', r['repo_uoa'])
        self.assertEqual('b', r['module_uoa'])
        self.assertEqual('c', r['data_uoa'])

        r = ck.parse_cid({'cid': '#a'})
        self.assertEqual(1, r['return'])
        self.assertEqual('unknown CID format', r['error'])

        r = ck.parse_cid({'cid': '#a', 'ignore_error': 'yes'})
        self.assertEqual(0, r['return'], r.get('error', None))

        r = ck.parse_cid(
            {'cid': '', 'cur_cid': {'repo_uoa': 'r', 'module_uoa': 'm', 'data_uoa': 'd'}})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual('r', r['repo_uoa'])
        self.assertEqual('m', r['module_uoa'])
        self.assertEqual('d', r['data_uoa'])

        r = ck.parse_cid(
            {'cid': 'a', 'cur_cid': {'repo_uoa': 'r', 'module_uoa': 'm', 'data_uoa': 'd'}})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual('r', r['repo_uoa'])
        self.assertEqual('m', r['module_uoa'])
        self.assertEqual('a', r['data_uoa'])

        r = ck.parse_cid({'cid': 'a:b', 'cur_cid': {
                         'repo_uoa': 'r', 'module_uoa': 'm', 'data_uoa': 'd'}})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual('r', r['repo_uoa'])
        self.assertEqual('a', r['module_uoa'])
        self.assertEqual('b', r['data_uoa'])

        r = ck.parse_cid({'cid': 'a:b:c:d', 'cur_cid': {
                         'repo_uoa': 'r', 'module_uoa': 'm', 'data_uoa': 'd'}})
        self.assertEqual(1, r['return'])
        self.assertEqual('unknown CID format', r['error'])

    def test_delete_directory(self):
        with test_util.tmp_dir() as fname:
            os.makedirs(fname + '/a')
            os.makedirs(fname + '/b')

            with open(fname + '/a/test.txt', 'a') as f:
                f.write('abc')

            with open(fname + '/b/test.log', 'a') as f:
                f.write('12')

            r = ck.delete_directory({'path': fname})
            self.assertEqual(0, r['return'], r.get('error', None))
            self.assertFalse(os.path.isdir(fname))

    def test_get_by_flat_key(self):
        a = {'dyn_features': {'ft1': '1', 'ft2': '2'},
             'static_features': {'ft3': '3', 'ft4': '4'}}
        r = ck.get_by_flat_key({'dict': a, 'key': '##dyn_features#ft2'})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual('2', r['value'])

    def test_detect_cid_in_current_path(self):
        r = ck.find_path_to_repo({'repo_uoa': 'default'})
        r = ck.detect_cid_in_current_path({'path': r['path']})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual('default', r['repo_uoa'])
        self.assertEqual('default', r['repo_alias'])

    def test_uid(self):
        r = ck.uid({})
        self.assertEqual(0, r['return'], r.get('error', None))

        uid = r['data_uid']
        self.assertEqual(16, len(uid))

        chars = '0123456789abcdef'
        for c in uid:
            self.assertIn(c, chars)

    def test_version(self):
        r = ck.get_version({})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual(ck.__version__, r['version_str'])
        self.assertEqual(ck.__version__.split('.'), r['version'])

    def test_check_version(self):
        r = ck.check_version({'version': '1.7.4'})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual('yes', r['ok'])
        self.assertEqual(ck.__version__, r['current_version'])

    def test_convert_entry_to_cid(self):
        r = ck.convert_entry_to_cid(
            {'repo_uoa': 'a', 'module_uoa': 'b', 'data_uoa': 'c'})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual('a:b:c', r['xcuoa'])

    def test_help(self):
        r = ck.help({})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertTrue('Usage:' in r['help'])
        self.assertTrue('Common actions for' in r['help'])
        for ca in ck.cfg['common_actions']:
            self.assertTrue(ca in r['help'])

    def test_print_input(self):
        d = {'a': 1, 'b': [2, 3]}
        r = ck.print_input(d)
        self.assertEqual(0, r['return'], r.get('error', None))
        parsed_dict = ck.convert_json_str_to_dict(
            {'str': r['html'], 'skip_quote_replacement': 'yes'})['dict']
        self.assertEqual(d, parsed_dict)

    def test_info(self):
        r = ck.info({'module_uoa': 'kernel'})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual('kernel', r['data_uoa'])
        self.assertEqual('kernel', r['data_alias'])

    def test_path(self):
        r = ck.find_path_to_repo({'repo_uoa': 'default'})
        r = ck.path({'path': r['path']})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual('default', r['repo_uoa'])
        self.assertEqual('default', r['repo_alias'])

    def test_find(self):
        r = ck.find({'module_uoa': 'kernel', 'data_uoa': 'default'})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual(1, r['number_of_entries'])
        self.assertEqual('kernel', r['module_uoa'])
        self.assertEqual('kernel', r['module_alias'])
        self.assertEqual('default', r['data_uoa'])
        self.assertEqual('local', r['repo_alias'])
        self.assertEqual('local', r['repo_uoa'])
        self.assertIn('repo_uid', r)
        self.assertIn('module_uid', r)
        self.assertIn('data_uid', r)
        self.assertIn('path_repo', r)
        self.assertIn('path', r)

#    TBD: cd now opens new bash so need to check how to handle that
#         need to add exit command ...
#
#    def test_cd(self):
#        r = ck.get_os_ck({})
#        plat = r['platform']
#
#        with test_util.tmp_sys():
#            r = ck.cd({'module_uoa': 'kernel', 'data_uoa': 'default'})
#            self.assertEqual(0, r['return'], r.get('error', None))
#
#            if plat == 'win':
#                self.assertEqual('cd /D ' + r['path'], r['string'])
#            else:
#                self.assertEqual('cd ' + r['path'], r['string'])
#
#            # check for fields from ck.find:
#            self.assertEqual(1, r['number_of_entries'])
#            self.assertEqual('kernel', r['module_uoa'])
#            self.assertEqual('kernel', r['module_alias'])
#            self.assertEqual('default', r['data_uoa'])
#            self.assertEqual('local', r['repo_alias'])
#            self.assertEqual('local', r['repo_uoa'])
#            self.assertIn('repo_uid', r)
#            self.assertIn('module_uid', r)
#            self.assertIn('data_uid', r)
#            self.assertIn('path_repo', r)
#            self.assertIn('path', r)

    def test_search(self):
        r = ck.search({'repo_uoa': 'default', 'module_uoa': 'kernel'})
        self.assertEqual(0, r['return'], r.get('error', None))
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

    def test_compare_dicts(self):
        d1 = {'a': 1, 'b': [2, 3]}
        d2 = {'b': [2, 3], 'a': 1}

        r = ck.compare_dicts({'dict1': d1, 'dict2': d2})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual('yes', r['equal'])

        d2['b'][1] = 4
        r = ck.compare_dicts({'dict1': d1, 'dict2': d2})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual('no', r['equal'])

    def test_compare_flat_dicts(self):
        d1 = {'a': 1, 'b': [2, 3]}
        d2 = {'b': [2, 3], 'a': 1}

        r = ck.compare_flat_dicts({'dict1': d1, 'dict2': d2})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual('yes', r['equal'])

        d2['b'][1] = 4
        r = ck.compare_flat_dicts({'dict1': d1, 'dict2': d2})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual('no', r['equal'])

    def test_compare_flat_dicts(self):
        d1 = {'a': 1, 'b': [2, 3]}
        d2 = {'b': [2, 3], 'a': 1}

        r = ck.compare_flat_dicts({'dict1': d1, 'dict2': d2})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual('yes', r['equal'])

        d2['b'][1] = 4
        r = ck.compare_flat_dicts({'dict1': d1, 'dict2': d2})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual('no', r['equal'])

    def test_find_string_in_dict_or_list(self):
        d = {'a': 1, 'b': [2, 3]}

        r = ck.find_string_in_dict_or_list({'dict': d, 'search_string': '2'})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual('yes', r['found'])

        r = ck.find_string_in_dict_or_list({'dict': d, 'search_string': '4'})
        self.assertEqual(0, r['return'], r.get('error', None))
        self.assertEqual('no', r['found'])

    def test_list_files(self):
        s = os.sep

        r = ck.list_files(
            {'repo_uoa': 'default', 'module_uoa': 'module', 'data_uoa': 'kernel'})
        self.assertEqual(0, r['return'], r.get('error', None))
        lst = r['list']
        self.assertIn('module.py', lst)
        self.assertIn('test' + s + 'test_kernel.py', lst)
        self.assertIn('test' + s + 'test_original_tests.py', lst)
