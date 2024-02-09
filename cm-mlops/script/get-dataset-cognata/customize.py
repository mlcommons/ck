from cmind import utils
import os
import shutil
import sys


def ask_user(question, default="yes"):
    valid = ["yes", "y", "no", "n"]
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return default.startswith('y')
        elif choice in valid:
            return choice.startswith('y')
        else:
            print("Please input y/n\n")

def preprocess(i):

    env = i['env']

    script_path = i['run_script_input']['path']

    with open(os.path.join(script_path, "license.txt"), "r") as f:
        print(f.read())

    response = ask_user("Do you accept?")

    print(response)


    return {'return': 0}

def postprocess(i):
    env = i['env']
    return {'return': -1} #todo
    if env.get('CM_DATASET_CALIBRATION','') == "no":
        env['CM_DATASET_PATH_ROOT'] = os.path.join(os.getcwd(), 'install')
        env['CM_DATASET_PATH'] = os.path.join(os.getcwd(), 'install', 'validation', 'data')
        env['CM_DATASET_CAPTIONS_DIR_PATH'] = os.path.join(os.getcwd(), 'install', 'captions')
        env['CM_DATASET_LATENTS_DIR_PATH'] = os.path.join(os.getcwd(), 'install', 'latents')
    else:
        env['CM_CALIBRATION_DATASET_PATH'] = os.path.join(os.getcwd(), 'install', 'calibration', 'data')

    return {'return': 0}
