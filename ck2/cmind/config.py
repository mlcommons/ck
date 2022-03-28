# Collective Mind configuration

import os

class Config(object):
    """
    CM configuration class
    """

    def __init__(self, config_file: str = None):
        """
        Initialize Collective Mind configuration
        """

        self.cfg = {
                     "name": "cm",

                     "env_home": "CM_HOME",
                     "env_debug": "CM_DEBUG",
                     "env_kernel": "CM_KERNEL",

                     "flag_debug": "cm-debug",

                     "flag_out": "out",

                     "flag_help": "h",
                     "flag_help2": "help",

                     "error_prefix": "CM error:",
                     "info_cli": "cm {automation} {action} {artifact(s)} {flags}",

                     "default_home_dir": "CM",

                     "file_repos": "repos.json",
                     "dir_repos": "repos",
                     "cmind_repo": "repo",

                     "file_meta_repo": "cmr",

                     "cmind_python_module_prefix": "cmind_",
                     "cmind_python_module_uid": "cmind_uid",

                     "action_substitutions": {
                       "ls":"search",
                       "list":"search",
                       "find":"search",
                       "rm":"delete"
                     },

                     "action_substitutions_reverse": {
                       "search":["list", "ls", "find"],
                       "delete":["rm"]
                     },

                     "cmind_automation":"automation",

                     "file_cmeta":"_cm",

                     "local_repo_name": "local",
                     "local_repo_meta": {
                        "uid": "9a3280b14a4285c9",
                        "alias": "local",
                        "name": "local CM repository"
                     },

                     "default_repo_name": "default",

                     "default_repo_pack": "cm.zip",

                     "repo_url_prefix":"https://github.com/",
                     "repo_url_org":"mlcommons",

                     "line":"======================================================="
                   }

        # Attempt to update config from file if specified explicitly during initialization
        # or specified by the environment variable
        if config_file is None or config_file.strip() == '':
            config_file = os.environ.get(self.cfg['env_kernel'])

        if config_file is not None and config_file.strip() != '':
            from cmind import utils
            r = utils.load_json_or_yaml(config_file)
            if r['return'] > 0:
                # Raise here because it's an initializer of a class
                raise Exception(r['error'])

            meta = r.get('meta', {})

            self.cfg.update(meta)
