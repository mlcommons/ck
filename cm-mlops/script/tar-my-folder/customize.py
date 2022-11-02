from cmind import utils
import cmind as cm
import os
import subprocess
from os.path import exists

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    input_dir = env.get("CM_TAR_INPUT_DIR", "")
    if input_dir == "":
        return {'return': 1, 'error': 'Please set CM_TAR_INPUT_DIR'}
    output_dir = env.get("CM_TAR_OUTPUT_DIR", "")
    if output_dir == "":
        output_dir = os.getcwd()
    output_file = env.get("CM_TAR_OUTFILE", "")
    if output_file == "":
        output_file = os.path.basename(input_dir)+".gz"

    CMD =  'tar -cvzf ' + os.path.join(output_dir, output_file) + ' ' + input_dir
    ret = os.system(CMD)

    return {'return':0}
