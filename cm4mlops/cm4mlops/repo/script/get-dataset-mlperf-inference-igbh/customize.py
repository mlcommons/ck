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

from cmind import utils
import os


def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    if os_info['platform'] == "windows":
        return {'return': 1, 'error': 'Script not supported in windows yet!'}

    print("Using MLCommons Inference source from '" +
          env['CM_MLPERF_INFERENCE_SOURCE'] + "'")

    # run cmd
    run_cmd = ""
    graph_folder = os.path.join(
        env['CM_MLPERF_INFERENCE_SOURCE'], 'graph', 'R-GAT')

    download_loc = env.get('CM_IGBH_DATASET_OUT_PATH', os.getcwd())

    env['CM_IGBH_DATASET_DOWNLOAD_LOCATION'] = download_loc

    run_cmd += f"cd {graph_folder} "
    x_sep = " && "

    # download the model
    if env['CM_IGBH_DATASET_TYPE'] == "debug":
        run_cmd += x_sep + env['CM_PYTHON_BIN_WITH_PATH'] + \
            f" tools/download_igbh_test.py --target-path {download_loc} "

    # split seeds
    run_cmd += x_sep + \
        f"{env['CM_PYTHON_BIN_WITH_PATH']} tools/split_seeds.py --path {download_loc} --dataset_size {env['CM_IGBH_DATASET_SIZE']}"

    # compress graph(for glt implementation)
    if env.get('CM_IGBH_GRAPH_COMPRESS', '') == "yes":
        run_cmd += x_sep + \
            f"{env['CM_PYTHON_BIN_WITH_PATH']} tools/compress_graph.py --path {download_loc} --dataset_size {env['CM_IGBH_DATASET_SIZE']} --layout {env['CM_IGBH_GRAPH_COMPRESS_LAYOUT']}"

    env['CM_RUN_CMD'] = run_cmd

    return {'return': 0}


def postprocess(i):

    env = i['env']

    env['CM_IGBH_DATASET_PATH'] = env.get(
        'CM_IGBH_DATASET_OUT_PATH', os.getcwd())

    print(
        f"Path to the IGBH dataset: {os.path.join(env['CM_IGBH_DATASET_PATH'], env['CM_IGBH_DATASET_SIZE'])}")

    return {'return': 0}
