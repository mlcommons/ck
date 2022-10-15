import os
import sys
mlc_vision_path = os.environ['CM_MLC_INFERENCE_VISION_PATH']
python_path = os.path.join(mlc_vision_path, "python")
sys.path.insert(0, python_path)

import imagenet
import dataset

dataset_path = os.environ['CM_DATASET_PATH']
dataset_list = os.environ.get('CM_DATASET_IMAGES_LIST', None)
img_format = os.environ.get('CM_ML_MODEL_DATA_LAYOUT', 'NHWC')
count = int(os.environ.get('CM_DATASET_SIZE', 1))
preprocessed_base_dir = os.environ.get('CM_DATASET_PREPROCESSED_PATH', os.getcwd())
threads = os.environ.get('CM_NUM_THREADS', os.cpu_count())
threads = os.environ.get('CM_NUM_PREPROCESS_THREADS', threads)

imagenet.Imagenet(data_path=dataset_path,
                        image_list=dataset_list,
                        name="imagenet",
                        image_format=img_format,
                        pre_process = dataset.pre_process_vgg,
                        use_cache=True,
                        count=count, 
                        threads=threads,
                        cache_dir=preprocessed_base_dir)
