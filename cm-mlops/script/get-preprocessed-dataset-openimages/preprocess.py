import os
import sys
import os.path
mlperf_vision_path = os.environ['CM_MLPERF_INFERENCE_VISION_PATH']
python_path = os.path.join(mlperf_vision_path, "python")
sys.path.insert(0, python_path)

import openimages
import dataset
import shutil

dataset_path = os.environ['CM_DATASET_PATH']
dataset_list = os.environ.get('CM_DATASET_IMAGES_LIST', None)
img_format = os.environ.get('CM_ML_MODEL_DATA_LAYOUT', 'NHWC')
count = int(os.environ.get('CM_DATASET_SIZE', 0)) or None
preprocessed_base_dir = os.environ.get('CM_DATASET_PREPROCESSED_PATH', os.getcwd())
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
                        cache_dir=preprocessed_base_dir)
org_path = os.path.join(preprocessed_base_dir,"preprocessed", name)
alternate_names = [ "openimages-" + str(image_width) + "-retinanet-onnx" ]
for alt_name in alternate_names:
    alt_path = os.path.join(preprocessed_base_dir,"preprocessed", alt_name)
    if not os.path.exists(alt_path):
        os.symlink(org_path, alt_path)
src_path=os.path.join(dataset_path, "annotations")
dest_path=os.path.join(preprocessed_base_dir, "annotations")
shutil.copytree(src_path, dest_path)
