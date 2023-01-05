import os
import sys
import os.path
mlperf_src_path = os.environ['CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH']
python_path = os.path.join(mlperf_src_path, "python")
sys.path.insert(0, python_path)

import openimages
import dataset
import shutil

dataset_path = os.environ['CM_DATASET_PATH']
dataset_list = os.environ.get('CM_DATASET_ANNOTATIONS_FILE_PATH', None)
img_format = os.environ.get('CM_DATASET_DATA_LAYOUT', 'NHWC')
count = int(os.environ.get('CM_DATASET_SIZE', 0)) or None
preprocessed_dir = os.environ.get('CM_DATASET_PREPROCESSED_PATH', os.getcwd())
image_width = int(os.environ.get('CM_DATASET_OPENIMAGES_RESIZE', 800))
threads = os.environ.get('CM_NUM_THREADS', os.cpu_count())
threads = os.environ.get('CM_NUM_PREPROCESS_THREADS', threads)
name="openimages-" + str(image_width) + "-retinanet"

openimages.OpenImages(data_path=dataset_path,
                        image_list=dataset_list,
                        name=name,
                        image_format=img_format,
                        pre_process = dataset.pre_process_openimages_retinanet,
                        use_cache=True,
                        image_size=[image_width, image_width, 3],
                        count=count,
                        threads=threads,
                        preprocessed_dir=preprocessed_dir)
src_path=os.environ.get('CM_DATASET_ANNOTATIONS_DIR_PATH', os.path.join(dataset_path, "annotations"))
dest_path=os.path.join(preprocessed_dir, "annotations")
shutil.copytree(src_path, dest_path)
