from cmind import utils
import os


def preprocess(i):
    env = i['env']
    if env.get('CM_HF_TOKEN', '') != '':
        env['CM_HF_LOGIN_CMD'] = f"""git config --global credential.helper store && huggingface-cli login --token {env['CM_HF_TOKEN']} --add-to-git-credential
"""
    elif str(env.get('CM_HF_DO_LOGIN')).lower() in ["yes", "1", "true"]:
        env['CM_HF_LOGIN_CMD'] = f"""git config --global credential.helper store && huggingface-cli login
"""
    return {'return': 0}


def postprocess(i):
    env = i['env']

    r = i['automation'].parse_version({'match_text': r'huggingface_hub\s*version:\s*([\d.]+)',
                                       'group_number': 1,
                                       'env_key': 'CM_GITHUBCLI_VERSION',
                                       'which_env': i['env']})
    if r['return'] > 0:
        return r

    version = r['version']

    print(i['recursion_spaces'] + '    Detected version: {}'.format(version))

    return {'return': 0, 'version': version}
