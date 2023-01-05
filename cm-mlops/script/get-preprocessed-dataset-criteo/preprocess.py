import os
import sys
mlperf_dlrm_path = os.environ['CM_MLPERF_INFERENCE_DLRM_PATH']
python_path = os.path.join(mlperf_dlrm_path, "pytorch", "python")
sys.path.insert(0, python_path)

import criteo
import dataset

dataset_name = os.environ['CM_DATASET']
dataset_path = os.environ['CM_DATASET_PATH']
dataset_list = os.environ.get('CM_DATASET_IMAGES_LIST', None)
samples_to_aggregate_fix = os.environ.get('CM_DATASET_SAMPLES_TO_AGGREGATE_FIX', None)
samples_to_aggregate_min = os.environ.get('CM_DATASET_SAMPLES_TO_AGGREGATE_MIN', None)
samples_to_aggregate_max = os.environ.get('CM_DATASET_SAMPLES_TO_AGGREGATE_MAX', None)
count = int(os.environ.get('CM_DATASET_SIZE', 0)) or None
max_ind_range = os.environ.get('CM_DATASET_MAX_IND_RANGE',-1)
threads = os.environ.get('CM_NUM_THREADS', os.cpu_count())
threads = os.environ.get('CM_NUM_PREPROCESS_THREADS', threads)

criteo.Criteo(data_path=dataset_path,
                        name=dataset_name,
                        pre_process = criteo.pre_process_criteo_dlrm,
                        use_cache=True,
                        samples_to_aggregate_fix=samples_to_aggregate_fix,
                        samples_to_aggregate_min=samples_to_aggregate_min,
                        samples_to_aggregate_max=samples_to_aggregate_max,
                        max_ind_range=max_ind_range,
                        count=count,
                        mlperf_bin_loader=False,
                        test_num_workers=threads
                        )
