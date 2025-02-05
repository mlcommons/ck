# Universal cfg for CM automations
#
# Author: Grigori Fursin
# Contributors: https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md
#
# Copyright: https://github.com/mlcommons/ck/blob/master/cm-mlops/COPYRIGHT.md
# License: https://github.com/mlcommons/ck/blob/master/cm-mlops/LICENSE.md
#
# White paper: https://arxiv.org/abs/2406.16791
# History: https://github.com/mlcommons/ck/blob/master/HISTORY.CM.md
# Original repository: https://github.com/mlcommons/ck/tree/master/cm-mlops
#
# CK and CM project contributors: https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md
#

import os

from cmind.automation import Automation
from cmind import utils


class CAutomation(Automation):
    """
    Automation actions
    """

    ############################################################
    def __init__(self, cmind, automation_file):
        super().__init__(cmind, __file__)

    ############################################################
    def test(self, i):
        """
        Test automation

        Args:
          (CM input dict):

          (out) (str): if 'con', output to console

          automation (str): automation as CM string object

          parsed_automation (list): prepared in CM CLI or CM access function
                                    [ (automation alias, automation UID) ] or
                                    [ (automation alias, automation UID), (automation repo alias, automation repo UID) ]

          (artifact) (str): artifact as CM string object

          (parsed_artifact) (list): prepared in CM CLI or CM access function
                                    [ (artifact alias, artifact UID) ] or
                                    [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          * Output from this automation action

        """

        import json
        print(json.dumps(i, indent=2))

        return {'return': 0}

    ############################################################
    def xset(self, i):
        """
        Set keys in configuration

        Args:
          (CM input dict):

            (out) (str): if 'con', output to console

            (artifact) (str): CM artifact with configuration
            (tags) (str): list of tags to find CM artifact with configuration

            (key) (dict): updating config
          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          * Output from this automation action

        """

        import json

        r = self._find_cfg_artifact(i)
        if r['return'] > 0:
            return r

        # Path to cfg
        path = r['path']
        path_to_config = r['path_to_config']
        config = r['config']

        # Clean input to leave only keys for the configuration
        new_config = i.get('key', {})

        # If new config is empty, just print existing config
        if len(new_config) > 0:
            # Check if need to delete some
            def check_to_delete(d):

                for k in list(d.keys()):
                    v = d[k]
                    if isinstance(v, dict):
                        check_to_delete(v)
                    else:
                        if k.endswith('-'):
                            if k[:-1] in d:
                                del (d[k[:-1]])
                            del (d[k])
                        else:
                            vsl = str(v).lower()
                            if vsl == 'none':
                                v = None
                            elif vsl == 'false':
                                v = False
                            elif vsl == 'true':
                                v = True

                            d[k] = v

            utils.merge_dicts({'dict1': config,
                               'dict2': new_config,
                               'append_lists': True,
                               'append_unique': True})

            check_to_delete(config)

            r = utils.save_json(path_to_config, config)
            if r['return'] > 0:
                return r

        # Print config
        print('Config:')
        print('')
        print(json.dumps(config, indent=2))

        return {'return': 0}

    ############################################################
    def load(self, i):
        """
        Load configuration

        Args:
          (CM input dict):

            (out) (str): if 'con', output to console

            (artifact) (str): CM artifact with configuration
            (tags) (str): list of tags to find CM artifact with configuration
          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          * Output from this automation action

        """

        return self._find_cfg_artifact(i)

    ############################################################
    def _find_cfg_artifact(self, i):
        """
        Args:
          (CM input dict):

            (out) (str): if 'con', output to console

            (artifact) (str): CM artifact with configuration
            (tags) (str): list of tags to find CM artifact with configuration
          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          * Output from this automation action

        """

        # Clean input to find artifact
        ii = utils.sub_input(i, self.cmind.cfg['artifact_keys'] + ['tags'])

        parsed_artifact = i.get('parsed_artifact', [])

        artifact_obj = parsed_artifact[0] if len(parsed_artifact) > 0 else None
        artifact_repo = parsed_artifact[1] if len(
            parsed_artifact) > 1 else None

        artifact = i.get('artifact', '')

        if artifact == '':
            ii['artifact'] = 'default'

        tags = ii.get('tags', '')

        if 'cm-universal-cfg' not in tags:
            if tags != '':
                tags += ','
            tags += 'cm-universal-cfg'

        ii['tags'] = tags

        automation = ii['automation']
        if automation != '.' and ',' not in automation:
            ii['automation'] = automation + ',' + self.meta['uid']

        # Add placeholder (use common action)

        ii['action'] = 'find'
        ii['out'] = ''
        # Avoid recursion - use internal CM add function to add the script
        # artifact
        ii['common'] = True

        r = self.cmind.access(ii)
        if r['return'] > 0:
            return r

        lst = r['list']

        if len(lst) == 0:
            ii['action'] = 'add'
            ii['meta'] = {}

            # Tags must be unique for default
            r = self.cmind.access(ii)
            if r['return'] > 0:
                return r

            path = r['path']
        elif len(lst) > 1:
            return {
                'return': 1, 'error': 'ambiguity in cfg name - more than 1 CM artifact found'}
        else:
            path = lst[0].path

        # Check if has config
        path_to_cfg = os.path.join(path, 'config.json')

        config = {}
        if os.path.isfile(path_to_cfg):
            r = utils.load_json(path_to_cfg)
            if r['return'] > 0:
                return r

            config = r['meta']

        return {'return': 0, 'path': path,
                'path_to_config': path_to_cfg, 'config': config}
