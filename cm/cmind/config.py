# Collective Mind configuration
#
# Author(s): Grigori Fursin
# Contributor(s):
#
# Copyright: https://github.com/mlcommons/ck/blob/master/COPYRIGHT.txt
# License: https://github.com/mlcommons/ck/blob/master/LICENSE.md
# History: https://github.com/mlcommons/ck/blob/master/HISTORY.CM.md
# White paper: https://arxiv.org/abs/2406.16791
# Project contributors: https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md

import os

class Config(object):
    """
    CM configuration class
    """

    def __init__(self, config_file = None):
        """
        Initialize CM configuration class

        Args:
            (config_file) (str): If not None, merge this file with the internal configuration

        Returns:
            (python class) with the following vars:

            * cfg (dict): internal CM configuration
        """

        self.cfg = {
                     "name": "cm",

                     "env_home": "CM_HOME",
                     "env_repos": "CM_REPOS",
                     "env_debug": "CM_DEBUG",
                     "env_config": "CM_CONFIG",
                     "env_index": "CM_INDEX",

                     "flag_debug": "cm-debug",

                     "flag_help": "h",
                     "flag_help2": "help",

                     "error_prefix": "CM error:",
                     "error_prefix2": "CMX detected a problem",
                     "info_cli": "cm {action} {automation} {artifact(s)} {flags} @input.yaml @input.json",
                     "info_clix": "cmx {action} {automation} {artifact(s)} {CMX control flags (-)} {CMX automation flags (--)}\nRun `cmx -h` to display help",

                     "default_home_dir": "CM",

                     "file_repos": "repos.json",
                     "dir_repos": "repos",
                     "cmind_repo": "repo",

                     "file_index": "index.json",

                     "file_meta_repo": "cmr",

                     "common_automation_module_name": "module",
                     "common_automation_module_namex": "modulex",

                     "action_substitutions": {
                       "ls":"search",
                       "list":"search",
                       "find":"search",
                       "rm":"delete",
                       "mv":"move",
                       "ren":"move",
                       "rename":"move",
                       "cp":"copy"
                     },

                     "new_repo_requirements": "cmind >= 3.1.0\n",

                     "cmind_automation":"automation",

                     "file_cmeta":"_cm",

                     "local_repo_name": "local",
                     "local_repo_meta": {
                        "uid": "9a3280b14a4285c9",
                        "alias": "local",
                        "name": "local CM repository"
                     },

                     "default_repo_pack": "cm.zip",

                     "repo_url_prefix":"https://github.com/",
                     "repo_url_org":"mlcommons",

                     "fail_if_automation_not_found": True,
                     
                     "line":"=======================================================",

                     "artifact_keys":['automation', 'artifact', 'parsed_automation', 'parsed_artifact']
                   }

        # Attempt to update config from file if specified explicitly during initialization
        # or specified by the environment variable
        if config_file is None or config_file.strip() == '':
            config_file = os.environ.get(self.cfg['env_config'])

        if config_file is not None and config_file.strip() != '':
            from cmind import utils
            r = utils.load_json_or_yaml(config_file)
            if r['return'] > 0:
                # Raise here because it's an initializer of a class
                raise Exception(r['error'])

            meta = r.get('meta', {})

            self.cfg.update(meta)
