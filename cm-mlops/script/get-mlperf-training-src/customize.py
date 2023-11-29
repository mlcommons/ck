from cmind import utils
import os
import shutil

def preprocess(i):

    env = i['env']

    script_path = i['run_script_input']['path']

    if env.get('CM_GIT_PATCH_FILENAMES', '') != '':
        patch_files = env['CM_GIT_PATCH_FILENAMES'].split(",")
        patch_files_full_paths = []
        for patch_file in patch_files:
            patch_file_full_path = os.path.join(script_path, "patch", patch_file)
            patch_files_full_paths.append(patch_file_full_path)
        env['CM_GIT_PATCH_FILEPATHS'] = ",".join(patch_files_full_paths)

    return {'return':0}


def postprocess(i):

    env = i['env']
    state = i['state']

    return {'return':0}
