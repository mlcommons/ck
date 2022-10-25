import os
import sys
mlperf_vision_path = os.environ['CM_MLPERF_INFERENCE_VISION_PATH']
python_path = os.path.join(mlperf_vision_path, "python")
sys.path.insert(0, python_path)

import openimages
import dataset

dataset_path = os.environ['CM_DATASET_PATH']
dataset_list = os.environ.get('CM_DATASET_IMAGES_LIST', None)
img_format = os.environ.get('CM_ML_MODEL_DATA_LAYOUT', 'NHWC')
count = int(os.environ.get('CM_DATASET_SIZE', 0)) or None
preprocessed_base_dir = os.environ.get('CM_DATASET_PREPROCESSED_PATH', os.getcwd())
image_width = int(os.environ.get('CM_DATASET_OPENIMAGES_RESIZE', 800))
threads = os.environ.get('CM_NUM_THREADS', os.cpu_count())
threads = os.environ.get('CM_NUM_PREPROCESS_THREADS', threads)

openimages.OpenImages(data_path=dataset_path,
                        image_list=dataset_list,
                        name="openimages-" + str(image_width) + "-retinanet",
                        image_format=img_format,
                        pre_process = dataset.pre_process_openimages_retinanet,
                        use_cache=True,
                        image_size=[image_width, image_width, 3],
                        count=count,
                        threads=threads,
                        cache_dir=preprocessed_base_dir)
