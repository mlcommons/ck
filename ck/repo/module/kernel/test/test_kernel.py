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

# Contains new kernel tests. Add new tests here!
class TestKernel(unittest.TestCase):

    def test_out(self):
        with tmp_sys():
            ck.out('test')
            self.assertEqual('test', sys.stdout.getvalue().strip())

    def test_err(self):
        with tmp_sys():
            ck.err({'return': 2, 'error': 'test.'})
            self.assertEqual('Error: test.\nExit code: 2', sys.stdout.getvalue().strip())

    def test_jerr(self):
        with tmp_sys():
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
        self.assertEqual(0, r['return'])
        self.assertEqual(2, r['return_code'])

        r = ck.system_with_timeout({'cmd': 'sleep 5', 'timeout': 0.05})
        self.assertEqual(8, r['return'])

    def test_run_and_get_stdout(self):
        r = ck.run_and_get_stdout({'cmd': ['sh', '-c', 'echo abcd && >&2 echo err && exit 2']})
        self.assertEqual(0, r['return'])
        self.assertEqual(2, r['return_code'])
        self.assertEqual('abcd\n', r['stdout'])
        self.assertEqual('err\n', r['stderr'])

        r = ck.run_and_get_stdout({'cmd': 'sh -c "echo abcd && >&2 echo err && exit 2"'})
        self.assertEqual(0, r['return'])
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
        self.assertEqual(0, r['return'])
        self.assertEqual(2016, r['datetime_obj'].year)

    def test_convert_str_key_to_int(self):
        self.assertEqual(5, ck.convert_str_key_to_int('5'))
        self.assertEqual(0, ck.convert_str_key_to_int('a'))

    def test_inp(self):
        with tmp_sys('test input'):
            r = ck.inp({'text': 'test output'})
            self.assertEqual('test output', sys.stdout.getvalue().strip())
            self.assertEqual('test input', r['string'])
            self.assertEqual(0, r['return'])

    def test_select(self):
        with tmp_sys('1\n'):
            d = {
                'key0': { 'name': 'n0', 'sort': 1 },
                'key1': { 'name': 'n1', 'sort': 0 }
            }
            r = ck.select({'dict': d, 'title': 'Select:'})

            self.assertEqual('Select:\n\n0) n1\n1) n0\n\nMake your selection (or press Enter for 0):', sys.stdout.getvalue().strip())
            self.assertEqual(0, r['return'])
            self.assertEqual('key0', r['string'])

    def test_select_uoa(self):
        with tmp_sys('1\n'):
            lst = [
                {'data_uid': 'uid1', 'data_uoa': 'b'},
                {'data_uid': 'uid2', 'data_uoa': 'a'}
            ]
            r = ck.select_uoa({'choices': lst})

            self.assertEqual('0) a (uid2)\n1) b (uid1)\n\nSelect UOA (or press Enter for 0):', sys.stdout.getvalue().strip())
            self.assertEqual(0, r['return'])
            self.assertEqual('uid1', r['choice'])

    def test_convert_str_tags_to_list(self):
        self.assertEqual([1, 2], ck.convert_str_tags_to_list([1, 2]))
        self.assertEqual(['1', '2'], ck.convert_str_tags_to_list('  1 , 2  '))

    def test_gen_tmp_file(self):
        with tmp_file(suffix='.txt') as fname:
            # check we can write to the file
            with open(fname, 'w') as f:
                f.write('test')

    def test_gen_uid(self):
        r = ck.gen_uid({})
        self.assertEqual(0, r['return'])

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
        self.assertEqual(0, r['return'])
        keys = sorted(['engine', 'version', 'author', 'author_email', 'author_webpage', 'license', 'copyright', 'iso_datetime'])
        self.assertEqual(keys, sorted(list(r['dict'].keys())))

    def test_convert_json_str_to_dict(self):
        r = ck.convert_json_str_to_dict({'str': "{'a': 1, 'b': [2, 3]}"})
        self.assertEqual(0, r['return'])
        self.assertEqual({'a': 1, 'b': [2, 3]}, r['dict'])

    def test_load_json_file(self):
        with tmp_file(suffix='.json', content='{"a": 1, "b": [2, 3]}') as fname:
            r = ck.load_json_file({'json_file': fname})
            self.assertEqual(0, r['return'])
            self.assertEqual({'a': 1, 'b': [2, 3]}, r['dict'])

    def test_load_yaml_file(self):
        with tmp_file(suffix='.yml', content='a: 1\nb:\n  - 2\n  - 3\n') as fname:
            r = ck.load_yaml_file({'yaml_file': fname})
            self.assertEqual(0, r['return'])
            self.assertEqual({'a': 1, 'b': [2, 3]}, r['dict'])

    def test_load_text_file(self):
        content = 'a\nb\nc'
        with tmp_file(suffix='.txt', content=content) as fname:
            r = ck.load_text_file({'text_file': fname, 'split_to_list': 'yes'})
            self.assertEqual(0, r['return'])
            self.assertEqual(str.encode(content.replace('\n', os.linesep)), r['bin'])
            self.assertEqual(content, r['string'])
            self.assertEqual(content.strip().split('\n'), r['lst'])

    def test_substitute_str_in_file(self):
        content = 'a\nb\nc'
        with tmp_file(suffix='.txt', content=content) as fname:
            r = ck.substitute_str_in_file({'filename': fname, 'string1': 'b', 'string2': 'd'})
            self.assertEqual(0, r['return'])
            self.assertEqual('a\nd\nc', ck.load_text_file({'text_file': fname})['string'])

    def test_dumps_json(self):
        d = {'a': 1, 'b': [2, 3]}
        json_str = ck.dumps_json({'dict': d, 'skip_indent': 'yes'})['string']
        parsed_dict = ck.convert_json_str_to_dict({'str': json_str, 'skip_quote_replacement': 'yes'})['dict']
        self.assertEqual(d, parsed_dict)

    def test_merge_dicts(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'c': 3}
        ck.merge_dicts({'dict1': d1, 'dict2': d2})
        self.assertEqual({'a': 1, 'b': 2, 'c': 3}, d1)

    def test_save_yaml_to_file(self):
        d = {'a': 1, 'b': [2, 3]}
        with tmp_file(suffix='.yml') as fname:
            r = ck.save_yaml_to_file({'yaml_file': fname, 'dict': d})
            self.assertEqual(0, r['return'])

            r = ck.load_yaml_file({'yaml_file': fname})
            self.assertEqual(0, r['return'])
            self.assertEqual(d, r['dict'])

    def test_convert_file_to_upload_string(self):
        with tmp_file(suffix='.txt', content='http://ctuning.org/') as fname:
            r = ck.convert_file_to_upload_string({'filename': fname})
            self.assertEqual(0, r['return'])
            self.assertEqual('aHR0cDovL2N0dW5pbmcub3JnLw==', r['file_content_base64'])

    def test_convert_upload_string_to_file(self):
        with tmp_file(suffix='.txt') as fname:
            r = ck.convert_upload_string_to_file({'file_content_base64': 'aHR0cDovL2N0dW5pbmcub3JnLw==', 'filename': fname})
            self.assertEqual(0, r['return'])
            self.assertEqual(fname, r['filename'])

            r = ck.load_text_file({'text_file': fname})
            self.assertEqual(0, r['return'])
            self.assertEqual('http://ctuning.org/', r['string'])

    def test_input_json(self):
        content = '{"a": 1, "b": [2, 3]}\n\n'
        with tmp_sys(content):
            r = ck.input_json({'text': 'input json'})
            self.assertEqual(0, r['return'])
            self.assertEqual('input json', sys.stdout.getvalue().strip())
            self.assertEqual(content.strip(), r['string'])
            self.assertEqual({'a': 1, 'b': [2, 3]}, r['dict'])

    def test_list_all_files(self):
        import shutil
        import tempfile

        fname = tempfile.mkdtemp()
        try:
            os.makedirs(fname + '/a')
            os.makedirs(fname + '/b')

            with open(fname + '/a/test.txt', 'a') as f:
                f.write('abc')

            with open(fname + '/b/test.log', 'a') as f:
                f.write('12')

            r = ck.list_all_files({'path': fname})
            self.assertEqual(0, r['return'])
            t = r['list']
            self.assertEqual({'size': 3}, t['a/test.txt'])
            self.assertEqual({'size': 2}, t['b/test.log'])

            r = ck.list_all_files({'path': fname, 'pattern': '*.txt'})
            self.assertEqual(0, r['return'])
            t = r['list']
            self.assertEqual({'size': 3}, t['a/test.txt'])
            self.assertEqual(None, t.get('b/test.log'))
        finally:
            shutil.rmtree(fname)

    def test_save_repo_cache(self):
        r = ck.save_repo_cache({})
        self.assertEqual(0, r['return'])

        r = ck.load_json_file({'json_file': ck.work['dir_cache_repo_uoa']})
        self.assertEqual(ck.cache_repo_uoa, r['dict'])

        r = ck.load_json_file({'json_file': ck.work['dir_cache_repo_info']})
        self.assertEqual(ck.cache_repo_info, r['dict'])

    def test_load_repo_info_from_cache(self):
        r = ck.load_repo_info_from_cache({'repo_uoa': 'default'})
        self.assertEqual(0, r['return'])
        self.assertEqual('default', r['data_alias'])
        self.assertEqual('default', r['data_uoa'])

    def test_find_repo_by_path(self):
        r = ck.find_path_to_repo({'repo_uoa': 'default'})
        r = ck.find_repo_by_path({'path': r['path']})
        self.assertEqual(0, r['return'])
        self.assertEqual('default', r['repo_uoa'])
        self.assertEqual('default', r['repo_alias'])

    def test_get_api(self):
        r = ck.get_api({'func': 'list_actions'})
        self.assertEqual(0, r['return'])
        self.assertEqual('List actions in a module', r['title'].strip())
        self.assertTrue(r['api'].strip().startswith('Input:  {'))

    def test_parse_cid(self):
        r = ck.parse_cid({'cid': 'a:b:c'})
        self.assertEqual(0, r['return'])
        self.assertEqual('a', r['repo_uoa'])
        self.assertEqual('b', r['module_uoa'])
        self.assertEqual('c', r['data_uoa'])

    def test_delete_directory(self):
        import shutil
        import tempfile

        fname = tempfile.mkdtemp()
        try:
            os.makedirs(fname + '/a')
            os.makedirs(fname + '/b')

            with open(fname + '/a/test.txt', 'a') as f:
                f.write('abc')

            with open(fname + '/b/test.log', 'a') as f:
                f.write('12')

            r = ck.delete_directory({'path': fname})
            self.assertEqual(0, r['return'])
            self.assertFalse(os.path.isdir(fname))
        except:
            shutil.rmtree(fname)

    def test_get_by_flat_key(self):
        a = {'dyn_features':{'ft1':'1', 'ft2':'2'}, 'static_features':{'ft3':'3','ft4':'4'}}
        r = ck.get_by_flat_key({'dict': a, 'key': '##dyn_features#ft2'})
        self.assertEqual(0, r['return'])
        self.assertEqual('2', r['value'])

    def test_detect_cid_in_current_path(self):
        r = ck.find_path_to_repo({'repo_uoa': 'default'})
        r = ck.detect_cid_in_current_path({'path': r['path']})
        self.assertEqual(0, r['return'])
        self.assertEqual('default', r['repo_uoa'])
        self.assertEqual('default', r['repo_alias'])

    def test_uid(self):
        r = ck.uid({})
        self.assertEqual(0, r['return'])

        uid = r['data_uid']
        self.assertEqual(16, len(uid))

        chars = '0123456789abcdef'
        for c in uid:
            self.assertIn(c, chars)
        
    def test_version(self):
        r = ck.get_version({})
        self.assertEqual(0, r['return'])
        self.assertEqual(ck.__version__, r['version_str'])
        self.assertEqual(ck.__version__.split('.'), r['version'])

    def test_check_version(self):
        r = ck.check_version({'version': '1.7.4'})
        self.assertEqual(0, r['return'])
        self.assertEqual('yes', r['ok'])
        self.assertEqual(ck.__version__, r['current_version'])

    def test_convert_entry_to_cid(self):
        r = ck.convert_entry_to_cid({'repo_uoa': 'a', 'module_uoa': 'b', 'data_uoa': 'c'})
        self.assertEqual(0, r['return'])
        self.assertEqual('a:b:c', r['xcuoa'])

    def test_help(self):
        r = ck.help({})
        self.assertEqual(0, r['return'])
        self.assertTrue('Usage:' in r['help'])
        self.assertTrue('Common actions:' in r['help'])
        for ca in ck.cfg['common_actions']:
            self.assertTrue(ca in r['help'])

    def test_print_input(self):
        d = {'a': 1, 'b': [2, 3]}
        r = ck.print_input(d)
        self.assertEqual(0, r['return'])
        parsed_dict = ck.convert_json_str_to_dict({'str': r['html'], 'skip_quote_replacement': 'yes'})['dict']
        self.assertEqual(d, parsed_dict)

    def test_info(self):
        r = ck.info({'module_uoa': 'kernel'})
        self.assertEqual(0, r['return'])
        self.assertEqual('kernel', r['data_uoa'])
        self.assertEqual('kernel', r['data_alias'])
