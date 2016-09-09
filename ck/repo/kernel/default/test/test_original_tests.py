# -*- coding: utf-8 -*-

import unittest

ck=None # Will be updated by CK (initialized CK kernel)

# Contains original tests, that where in the 'ck/tests' directory (not all of them).
# Some tests are simplified, because the original tests where in fact integration tests, which can not be easily
# represented as unit tests.
# Some tests are adapted to the API changes happened since then.
# Do *not* add new tests here.
# Methods are named like this: 'test_' + the original file name without extension.
class OriginalKernelTest(unittest.TestCase):

    def test_flatten_dict(self):
        a={'dyn_features':{'ft1':'1', 'ft2':'2'}, 'static_features':{'ft3':'3','ft4':'4'}}
        r=ck.flatten_dict({'dict':a})
        self.assertEqual(0, r['return'])

        x=r['dict']
        self.assertEqual({'##dyn_features#ft2': '2', '##static_features#ft3': '3', '##static_features#ft4': '4', '##dyn_features#ft1': '1'}, x)

        r=ck.restore_flattened_dict({'dict':x})
        self.assertEqual(0, r['return'])
        self.assertEqual(a, r['dict'])

    def test_list_with_ranges(self):
        r = ck.list_data({"repo_uoa_list":["default"],"module_uoa_list":["test", "index"],"data_uoa_list":["unicode"]})
        self.assertEqual(0, r['return'])

        lst = r['lst']
        self.assertEqual(1, len(lst))
        self.assertEqual('unicode', lst[0]['data_uoa'])

    def test_test(self):
        import os

        r = ck.get_version({})
        self.assertEqual(0, r['return'])
        self.assertEqual(ck.__version__, r['version_str'])
        self.assertEqual(ck.__version__.split('.'), r['version'])

        fname = ck.gen_tmp_file({'prefix': 'ck-test-', 'suffix': '.json'})['file_name']
        try:
            with open(fname, 'w') as f:
                f.write('{"key20":["value21","value22"],  "key12":"12"}')
            cmd="mv data cid1 cid2 key1=value1 -key10 --key13=value13 @" + fname
            i=cmd.split(' ')
            r=ck.convert_ck_list_to_dict(i)
            self.assertEqual({'cid': 'data', 'key1': 'value1', u'key20': [u'value21', u'value22'], 'action': 'mv', 'cids': ['cid1', 'cid2'], 'key13': 'value13', u'key12': u'12', 'key10': 'yes'}, r['ck_dict'])
        finally:
            os.remove(fname)

