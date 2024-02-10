from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    dlrm_data_path = env.get('CM_DLRM_DATA_PATH', '')
    if dlrm_data_path == '' or not os.path.exists(dlrm_data_path):
        return {'return': 1, 'error': f'Please input a valid path as --dlrm_data_path'} 
    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    variation = env['CM_DLRM_DATA_VARIATION']

    if variation == "nvidia":
        if not os.path.exists(os.path.join(dlrm_data_path, "model")):
            return {'return': 1, 'error': f'model directory is missing inside {dlrm_data_path}'} 
        if not os.path.exists(os.path.join(dlrm_data_path, "criteo")):
            return {'return': 1, 'error': f'criteo directory is missing inside {dlrm_data_path}'} 
        if not os.path.exists(os.path.join(dlrm_data_path, "model", "model_weights")):
            return {'return': 1, 'error': f'model_weights directory is missing inside {dlrm_data_path}/model'} 
        if not os.path.exists(os.path.join(dlrm_data_path, "criteo", "day23")):
            return {'return': 1, 'error': f'day23 directory is missing inside {dlrm_data_path}/day23'} 
        if not os.path.exists(os.path.join(dlrm_data_path, "criteo", "day23", "fp32")):
            return {'return': 1, 'error': f'fp32 directory is missing inside {dlrm_data_path}/day23'} 

        if not os.path.exists(os.path.join(dlrm_data_path, "criteo", "day23", "fp32", "day_23_sparse_multi_hot.npz")) and not os.path.exists(os.path.join(dlrm_data_path, "criteo", "day23", "fp32", "day_23_sparse_multi_hot_unpacked")):
            return {'return': 1, 'error': f'day_23_sparse_multi_hot.npz is missing inside {dlrm_data_path}/criteo/day23/fp32'} 
        if not os.path.exists(os.path.join(dlrm_data_path, "criteo", "day23", "fp32", "day_23_dense.npy")):
            return {'return': 1, 'error': f'day_23_dense.npy is missing inside {dlrm_data_path}/criteo/day23/fp32'} 
        if not os.path.exists(os.path.join(dlrm_data_path, "criteo", "day23", "fp32", "day_23_labels.npy")):
            return {'return': 1, 'error': f'day_23_labels.npy is missing inside {dlrm_data_path}/criteo/day23/fp32'} 
        if not os.path.exists(os.path.join(dlrm_data_path, "criteo", "day23", "raw_data")):
            return {'return': 1, 'error': f'raw_data is missing inside {dlrm_data_path}/criteo/day23'} 


        if not os.path.exists(os.path.join(dlrm_data_path, "criteo", "day23", "fp32", "day_23_sparse_multi_hot_unpacked")):
            os.system(f"unzip {os.path.join(dlrm_data_path, 'criteo', 'day23', 'fp32', 'day_23_sparse_multi_hot.npz')} -d {os.path.join(dlrm_data_path, 'criteo', 'day23', 'fp32', 'day_23_sparse_multi_hot_unpacked')}")

        xsep = ' && '
        run_cmd = ''
        if os.path.exists(os.path.join(dlrm_data_path, "criteo", "day23", "fp32", "day_23_sparse_multi_hot.npz")):
            file_path = os.path.join(dlrm_data_path, "criteo", "day23", "fp32", "day_23_sparse_multi_hot.npz")
            run_cmd = ("echo {} {} | md5sum -c").format('c46b7e31ec6f2f8768fa60bdfc0f6e40', file_path)

        if run_cmd != '':
            run_cmd += xsep

        file_path = os.path.join(dlrm_data_path, "criteo", "day23", "fp32", "day_23_dense.npy")
        run_cmd +=  ("echo {} {} | md5sum -c").format('cdf7af87cbc7e9b468c0be46b1767601', file_path)

        file_path = os.path.join(dlrm_data_path, "criteo", "day23", "fp32", "day_23_labels.npy")
        run_cmd += xsep + ("echo {} {} | md5sum -c").format('dd68f93301812026ed6f58dfb0757fa7', file_path)

        env['CM_RUN_CMD'] = run_cmd

    return {'return':0}

def postprocess(i):

    env = i['env']

    env['CM_GET_DEPENDENT_CACHED_PATH'] = env['CM_DLRM_DATA_PATH']

    return {'return':0}
