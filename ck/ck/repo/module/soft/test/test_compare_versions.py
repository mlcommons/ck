#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Collective Knowledge
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#

import unittest

ck=None # Will be updated by CK (initialized CK kernel)

class CompareVersionsTests(unittest.TestCase):
    def test_get_version(self):
        """
            expected output format:
                ret_struct = {'version': ['1', '9', '4', '1'], 'return': 0, 'version_str': '1.9.4.1'}
        """

        ret_struct = ck.version( {} )
        self.assertEqual(   ret_struct['return'],               0,                          ret_struct.get('error', None) )
        self.assertEqual(   type(ret_struct['version']),        list,                       '["version"] should be a list' )
        self.assertGreater( len(ret_struct['version']),         0,                          '["version"] should contain at least one element' )
        self.assertEqual(   '.'.join(ret_struct['version']),    ret_struct['version_str'],  '["version"] is correctly parsed from ["version_str"]')

    def test_compare_versions(self):
        """
            expected output format:
                ret_struct = {'return': 0, 'result': '<'}
        """

        def compare_one_pair_one_way(left_version, right_version, expected_sign):
            "Run one verbose comparison"

            ret_struct = ck.access({
                'action':       'compare_versions',
                'module_uoa':   'soft',
                'version1':     left_version,
                'version2':     right_version
            })
            result = ret_struct['result']
            self.assertEqual(   ret_struct['return'],   0,          ret_struct.get('error', None) )
            outcome_text = ('(ok)' if expected_sign==result else '(expected '+expected_sign+')') if expected_sign else ''
            print('compare_versions:   %12s   %s  %12s      %s' % (str(left_version),result, str(right_version), outcome_text) )

            if expected_sign:
                self.assertEqual(   result,                 expected_sign,   "Expected '"+expected_sign+"', but got '"+result+"' instead")

        def compare_direct_and_reverse(left_version, right_version, expected_sign=None):
            "Try both directions to test for symmetry of < / > relation"

            compare_one_pair_one_way(left_version, right_version, expected_sign)
            compare_one_pair_one_way(right_version, left_version, {'>':'<', '<':'>', '=':'=', None:None}[expected_sign] )


        # Your favourite vectors go here:
        #
        ver_10ab    = [ 1, 0, 'ab' ]
        ver_103     = [ 1, 0, 3 ]
        ver_12      = [ 1, 2 ]
        ver_120     = [ 1, 2, 0 ]
        ver_125     = [ 1, 2, 5 ]
        ver_13      = [ 1, 3 ]
        ver_130     = [ 1, 3, 0 ]
        ver_2107    = [ 2, 10, 7 ]
        ver_2_27    = [ 2,  2, 7 ]

        compare_direct_and_reverse(ver_12,      ver_120,    '=')    # switched to new behaviour
        compare_direct_and_reverse(ver_120,     ver_120,    '=')
        compare_direct_and_reverse(ver_125,     ver_120,    '>')
        compare_direct_and_reverse(ver_103,     ver_13,     '<')
        compare_direct_and_reverse(ver_103,     ver_130,    '<')    # against an old bug where vector components were sorted first
        compare_direct_and_reverse(ver_103,     ver_10ab,   '>')    # any integer is higher than any letter combo
        compare_direct_and_reverse(ver_2107,    ver_2_27,   '>')    # against alphabetic ordering of integers

if __name__ == '__main__':
    import ck.kernel
    ck = ck.kernel
    unittest.main()
