import os
from cmind import utils
    

############################################################
def copy_to_remote(i):
    """
    Add CM automation.

    Args:
      (CM input dict):

      (out) (str): if 'con', output to console

      parsed_artifact (list): prepared in CM CLI or CM access function
                                [ (artifact alias, artifact UID) ] or
                                [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

      (repos) (str): list of repositories to search for automations (internal & mlcommons@ck by default)

      (output_dir) (str): output directory (./ by default)

    Returns:
      (CM return dict):

      * return (int): return code == 0 if no error and >0 if error
      * (error) (str): error string if return>0

    """

    self_module = i['self_module']

    remote_host =  i.get('remote_host')
    if not remote_host:
        return {'return':1, 'error': 'Please input remote host_name/IP via --remote_host'}
    remote_cm_repos_location = i.get('remote_cm_repos_location', os.path.join("/home", os.getlogin(), "CM", "repos"))
    remote_cm_cache_location = os.path.join(remote_cm_repos_location, "local", "cache")

    remote_port =  i.get('remote_port', '22')
    remote_user = i.get('remote_user', os.getlogin())

    tag_string = i['tags']
    tag_string += ",-tmp"

    cm_input = {'action': 'show',
                'automation': 'cache',
                'tags': f'{tag_string}',
                'quiet': True
                }
    r = self_module.cmind.access(cm_input)
    if r['return'] > 0:
        return r

    if len(r['list']) == 0:
        pass #fixme
    elif len(r['list']) > 1:
        print("Multiple cache entries found: ")
        for k in sorted(r['list'], key = lambda x: x.meta.get('alias','')):
            print(k.path)
        x = input("Would you like to copy them all? Y/n: ")
        if x.lower() == 'n':
            return {'return': 0}

    import json

    for k in sorted(r['list'], key = lambda x: x.meta.get('alias','')):
        path = k.path
        cacheid = os.path.basename(path)

        copy_cmd = f"rsync -avz --exclude cm-cached-state.json -e 'ssh -p {remote_port}' {path} {remote_user}@{remote_host}:{remote_cm_cache_location}"
        print(copy_cmd)
        os.system(copy_cmd)

        cm_cached_state_json_file = os.path.join(path, "cm-cached-state.json")
        if not os.path.exists(cm_cached_state_json_file):
            return {'return':1, 'error': f'cm-cached-state.json file missing in {path}'}

        with open(cm_cached_state_json_file, "r") as f:
            cm_cached_state = json.load(f)

        new_env = cm_cached_state['new_env']
        new_state = cm_cached_state['new_state'] # Todo fix new state
        cm_repos_path = os.environ.get('CM_REPOS', os.path.join(os.path.expanduser("~"), "CM", "repos"))
        cm_cache_path = os.path.realpath(os.path.join(cm_repos_path, "local", "cache"))

        for key,val in new_env.items():
            if type(val) == str and cm_cache_path in val:
                new_env[key] = val.replace(cm_cache_path, remote_cm_cache_location)

        with open("tmp_remote_cached_state.json", "w") as f:
            json.dump(cm_cached_state, f, indent=2)

        remote_cached_state_file_location = os.path.join(remote_cm_cache_location, cacheid, "cm-cached-state.json")
        copy_cmd = f"rsync -avz -e 'ssh -p {remote_port}' tmp_remote_cached_state.json {remote_user}@{remote_host}:{remote_cached_state_file_location}"
        print(copy_cmd)
        os.system(copy_cmd)

    return {'return':0}
