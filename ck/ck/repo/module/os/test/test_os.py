#
# Collective Knowledge
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#

import unittest

ck=None           # Will be updated by CK (initialized CK kernel)
work=None         # Will be updated by CK (initialized CK kernel)
test_util=None    # Will be updated by CK (initialized CK test utils)

# Contains new kernel tests. Add new tests here!
class TestOs(unittest.TestCase):

    def test_lib_path_export_script(self):
        h = { 
            "env_ld_library_path": "DYLD_LIBRARY_PATH",
            "env_library_path": "LIBRARY_PATH",
        }
        dyn_path = '/dyn/path'
        stat_path = '/stat/path'

        r = ck.access({
                'action': 'lib_path_export_script',
                'module_uoa': 'os',
                'host_os_dict': h,
                'dynamic_lib_path': dyn_path,
                'static_lib_path': stat_path
            })
        self.assertEqual(0, r['return'])
        script = '\nexport {dyn_name}="{dyn_val}":${dyn_name}\nexport {stat_name}="{stat_val}":${stat_name}\n\n'.format(
            dyn_name = h['env_ld_library_path'], dyn_val = dyn_path,
            stat_name = h['env_library_path'], stat_val = stat_path)
        self.assertEqual(script, r['script'])

        r = ck.access({
                'action': 'lib_path_export_script',
                'module_uoa': 'os',
                'host_os_dict': h,
                'lib_path': dyn_path
            })
        self.assertEqual(0, r['return'])
        script = '\nexport {dyn_name}="{dyn_val}":${dyn_name}\nexport {stat_name}="{stat_val}":${stat_name}\n\n'.format(
            dyn_name = h['env_ld_library_path'], dyn_val = dyn_path,
            stat_name = h['env_library_path'], stat_val = dyn_path)
        self.assertEqual(script, r['script'])

        h = { 
            "env_library_path": "LIBRARY_PATH",
        }
        r = ck.access({
                'action': 'lib_path_export_script',
                'module_uoa': 'os',
                'host_os_dict': h,
                'dynamic_lib_path': dyn_path
            })
        self.assertEqual(0, r['return'])
        script = '\nexport {dyn_name}="{dyn_val}":${dyn_name}\n\n'.format(
            dyn_name = 'LD_LIBRARY_PATH', dyn_val = dyn_path)
        self.assertEqual(script, r['script'])

        h = { 
            "env_library_path": "LIBRARY_PATH",
            "ck_name": "win"
        }
        r = ck.access({
                'action': 'lib_path_export_script',
                'module_uoa': 'os',
                'host_os_dict': h,
                'dynamic_lib_path': dyn_path
            })
        self.assertEqual(0, r['return'])
        self.assertEqual('', r['script'])

        r = ck.access({
                'action': 'lib_path_export_script',
                'module_uoa': 'os',
                'host_os_dict': {},
                'lib_path': ''
            })
        self.assertEqual(0, r['return'])
        self.assertEqual('', r['script'])

        r = ck.access({
                'action': 'lib_path_export_script',
                'module_uoa': 'os',
                'host_os_dict': {},
                'lib_path': ['a', 'b']
            })
        self.assertEqual(0, r['return'])
        self.assertEqual('\nexport LD_LIBRARY_PATH="a":"b":$LD_LIBRARY_PATH\nexport LIBRARY_PATH="a":"b":$LIBRARY_PATH\n\n', r['script'])
