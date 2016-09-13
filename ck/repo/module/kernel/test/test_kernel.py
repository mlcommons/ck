import unittest
import sys

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

# Contains new kernel tests. Add new tests here!
class TestKernel(unittest.TestCase):

    def test_out(self):
        saved_stdout = sys.stdout
        try:
            out = get_io()
            sys.stdout = out
            ck.out('test')
            self.assertEqual('test', out.getvalue().strip())
        finally:
            sys.stdout = saved_stdout


    def test_err(self):
        saved_stdout = sys.stdout
        saved_exit = sys.exit
        try:
            out = get_io()
            sys.stdout = out
            sys.exit = dummy_exit
            ck.err({'return': 2, 'error': 'test.'})
            self.assertEqual('Error: test.\nExit code: 2', out.getvalue().strip())
        finally:
            sys.stdout = saved_stdout
            sys.exit = saved_exit

    def test_jerr(self):
        saved_stdout = sys.stdout
        try:
            out = get_io()
            sys.stdout = out
            with self.assertRaises(KeyboardInterrupt):
                ck.jerr({'return': 2, 'error': 'test.'})
            self.assertEqual('Error: test.', out.getvalue().strip())
        finally:
            sys.stdout = saved_stdout

    def test_safe_float(self):
        import math

        self.assertEqual(ck.safe_float(1, 0), 1.0)
        self.assertEqual(ck.safe_float('a', 0), 0)
        self.assertEqual(ck.safe_float('-5.35', 0), -5.35)
        self.assertEqual(ck.safe_float('Infinity', 0), float('inf'))
        self.assertTrue(math.isnan(ck.safe_float('nan', 0)))

    def test_safe_int(self):
        import math

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
        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        try:
            out_stream = get_io()
            in_stream = get_io('test input')
            if not hasattr(in_stream, 'encoding'):
                in_stream.encoding = 'utf8'
            sys.stdout = out_stream
            sys.stdin = in_stream
            r = ck.inp({'text': 'test output'})
            self.assertEqual('test output', out_stream.getvalue().strip())
            self.assertEqual('test input', r['string'])
            self.assertEqual(0, r['return'])
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

    def test_select(self):
        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        try:
            out_stream = get_io()
            in_stream = get_io('1\n')
            if not hasattr(in_stream, 'encoding'):
                in_stream.encoding = 'utf8'
            sys.stdout = out_stream
            sys.stdin = in_stream

            d = {
                'key0': { 'name': 'n0', 'sort': 1 },
                'key1': { 'name': 'n1', 'sort': 0 }
            }
            r = ck.select({'dict': d, 'title': 'Select:'})

            self.assertEqual('Select:\n\n0) n1\n1) n0\n\nMake your selection (or press Enter for 0):', out_stream.getvalue().strip())
            self.assertEqual(0, r['return'])
            self.assertEqual('key0', r['string'])
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

    def test_select_uoa(self):
        saved_stdout = sys.stdout
        saved_stdin = sys.stdin
        try:
            out_stream = get_io()
            in_stream = get_io('1\n')
            if not hasattr(in_stream, 'encoding'):
                in_stream.encoding = 'utf8'
            sys.stdout = out_stream
            sys.stdin = in_stream

            lst = [
                {'data_uid': 'uid1', 'data_uoa': 'b'},
                {'data_uid': 'uid2', 'data_uoa': 'a'}
            ]
            r = ck.select_uoa({'choices': lst})

            self.assertEqual('0) a (uid2)\n1) b (uid1)\n\nSelect UOA (or press Enter for 0):', out_stream.getvalue().strip())
            self.assertEqual(0, r['return'])
            self.assertEqual('uid1', r['choice'])
        finally:
            sys.stdout = saved_stdout
            sys.stdin = saved_stdin

    def test_convert_str_tags_to_list(self):
        self.assertEqual([1, 2], ck.convert_str_tags_to_list([1, 2]))
        self.assertEqual(['1', '2'], ck.convert_str_tags_to_list('  1 , 2  '))

    def test_gen_tmp_file(self):
        import os

        r = ck.gen_tmp_file({'suffix': '.txt', 'prefix': 'ck-test-'})
        fname = r['file_name']
        try:
            self.assertEqual(0, r['return'])
            # check we can write to the file
            with open(fname, 'w') as f:
                f.write('test')
        finally:
            try:
                os.remove(fname)
            except OSError:
                pass

    def test_gen_uid(self):
        import uuid

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
        import os

        fname = ck.gen_tmp_file({'suffix': '.json', 'prefix': 'ck-test-'})['file_name']
        try:
            with open(fname, 'w') as f:
                f.write('{"a": 1, "b": [2, 3]}')

            r = ck.load_json_file({'json_file': fname})
            self.assertEqual(0, r['return'])
            self.assertEqual({'a': 1, 'b': [2, 3]}, r['dict'])
        finally:
            try:
                os.remove(fname)
            except OSError:
                pass

    def test_load_text_file(self):
        import os

        fname = ck.gen_tmp_file({'suffix': '.txt', 'prefix': 'ck-test-'})['file_name']
        try:
            content = 'a\nb\nc'
            with open(fname, 'w') as f:
                f.write(content)

            r = ck.load_text_file({'text_file': fname, 'split_to_list': 'yes'})
            self.assertEqual(0, r['return'])
            self.assertEqual(str.encode(content.replace('\n', os.linesep)), r['bin'])
            self.assertEqual(content, r['string'])
            self.assertEqual(content.strip().split('\n'), r['lst'])
        finally:
            try:
                os.remove(fname)
            except OSError:
                pass

    def test_substitute_str_in_file(self):
        import os

        fname = ck.gen_tmp_file({'suffix': '.txt', 'prefix': 'ck-test-'})['file_name']
        try:
            content = 'a\nb\nc'
            with open(fname, 'w') as f:
                f.write(content)

            r = ck.substitute_str_in_file({'filename': fname, 'string1': 'b', 'string2': 'd'})
            self.assertEqual(0, r['return'])
            self.assertEqual('a\nd\nc', ck.load_text_file({'text_file': fname})['string'])
        finally:
            try:
                os.remove(fname)
            except OSError:
                pass

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
