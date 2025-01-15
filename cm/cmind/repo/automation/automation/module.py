# CM automation module to add or document all automations
#
# Authors: Grigori Fursin
# Contributors:
#
# Copyright: https://github.com/mlcommons/ck/blob/master/COPYRIGHT.txt
# License: https://github.com/mlcommons/ck/blob/master/LICENSE.md
# History: https://github.com/mlcommons/ck/blob/master/HISTORY.CM.md
# White paper: https://arxiv.org/abs/2406.16791
# Project contributors: https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md

import os

from cmind.automation import Automation
from cmind import utils


class CAutomation(Automation):
    """
    CM "automation" automation actions
    """

    ############################################################
    def __init__(self, cmind, automation_file):
        super().__init__(cmind, automation_file)

    ############################################################
    def print_input(self, i):
        """
        Print unified CM input.

        Args:
          (CM input dict): 

          (out) (str): if 'con', output to console

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

        """

        import json
        print(json.dumps(i, indent=2))

        return {'return': 0}

    ############################################################

    def add(self, i):
        """
        Add CM automation.

        Args:
          (CM input dict): 

          (out) (str): if 'con', output to console

          parsed_artifact (list): prepared in CM CLI or CM access function
                                    [ (artifact alias, artifact UID) ] or
                                    [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

        """

        import shutil

        console = i.get('out') == 'con'

        parsed_artifact = i.get('parsed_artifact', [])

        artifact_obj = parsed_artifact[0] if len(
            parsed_artifact) > 0 else ('', '')

        module_name = 'module.py'

        tags_list = utils.convert_tags_to_list(i)
        if 'automation' not in tags_list:
            tags_list.append('automation')

        # Add placeholder (use common action)
        i['out'] = 'con'
        i['common'] = True

        i['meta'] = {'automation_alias': self.meta['alias'],
                     'automation_uid': self.meta['uid'],
                     'tags': tags_list}

        if 'tags' in i:
            del (i['tags'])

        automation = i['automation']
        if automation != '.' and ',' not in automation:
            i['automation'] = automation + ',' + self.meta['uid']

        r_obj = self.cmind.access(i)
        if r_obj['return'] > 0:
            return r_obj

        new_automation_path = r_obj['path']

        if console:
            print('Created automation in {}'.format(new_automation_path))

        # Create Python module holder
        module_holder_path = new_automation_path

        # Copy support files
        original_path = os.path.dirname(self.path)

        # Copy module files
        for f in ['module_dummy.py']:
            f1 = os.path.join(self.path, f)
            f2 = os.path.join(new_automation_path, f.replace('_dummy', ''))

            if console:
                print('  * Copying {} to {}'.format(f1, f2))

            shutil.copyfile(f1, f2)

        return r_obj

    ############################################################
    def add_cmx(self, i):
        """
        Add new automation in CMX format

        Args:
          (CMX input dict): 

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

        """

        import shutil

        console = i['control'].get('out', '') == 'con'

        # Prepare to call common function
        r = utils.process_input(i)
        if r['return'] > 0:
            return r

        # Take only out from original control
        i['control'] = {'out': i['control']['out'],
                        'common': True}

        tags_list = utils.convert_tags_to_list(i)
        if 'automation' not in tags_list:
            tags_list.append('automation')

        i['meta'] = {'automation_alias': self.meta['alias'],
                     'automation_uid': self.meta['uid'],
                     'tags': tags_list}

        if 'tags' in i:
            del (i['tags'])

        # Use yaml by default
        if 'yaml' not in i:
            i['yaml'] = True

        # Pass to common action
        r_obj = self.cmind.x(i)
        if r_obj['return'] > 0:
            return r_obj

        new_automation_path = r_obj['path']

        if console:
            print('Created automation in {}'.format(new_automation_path))

        module_name = 'modulex.py'

        # Create Python module holder
        module_holder_path = new_automation_path

        # Copy support files
        original_path = os.path.dirname(self.path)

        # Copy module files
        for f in ['modulex_dummy.py']:
            f1 = os.path.join(self.path, f)
            f2 = os.path.join(new_automation_path, f.replace('_dummy', ''))

            if console:
                print('  * Copying {} to {}'.format(f1, f2))

            shutil.copyfile(f1, f2)

        return r_obj

    ############################################################

    def doc(self, i):
        """
        Add CM automation.

        Args:
          (CM input dict): 

          (out) (str): if 'con', output to console

          parsed_artifact (list): prepared in CM CLI or CM access function
                                    [ (artifact alias, artifact UID) ] or
                                    [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

          (repos) (str): list of repositories to search for automations (internal & mlcommons@ck by default)

          (output_dir) (str): output directory (../docs by default)

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

        """

        return utils.call_internal_module(self, __file__, 'module_misc', 'doc', i)
