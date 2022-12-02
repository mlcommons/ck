import os
import sys

if os.environ.get('CM_IMAGENET_QUANTIZED', '') == "yes":
    import generic_preprocess
    generic_preprocess.preprocess()
else:
    mlperf_vision_path = os.environ['CM_MLPERF_INFERENCE_VISION_PATH']
    python_path = os.path.join(mlperf_vision_path, "python")
    sys.path.insert(0, python_path)

    import imagenet
    import dataset

    dataset_path = os.environ['CM_DATASET_PATH']
    dataset_list = os.environ.get('CM_DATASET_IMAGES_LIST', None)
    img_format = os.environ.get('CM_ML_MODEL_DATA_LAYOUT', 'NHWC')
    count = int(os.environ.get('CM_DATASET_SIZE', 1))
    preprocessed_base_dir = os.environ.get('CM_DATASET_PREPROCESSED_PATH', os.getcwd())
    threads = os.environ.get('CM_NUM_THREADS', os.cpu_count())
    threads = int(os.environ.get('CM_NUM_PREPROCESS_THREADS', threads))

    if os.environ.get('CM_MODEL', 'resnet50') == 'resnet50':
        pre_process = dataset.pre_process_vgg
    elif os.environ.get('CM_MODEL') == 'mobilenet':
        pre_process = dataset.pre_process_mobilenet

    imagenet.Imagenet(data_path=dataset_path,
                        image_list=dataset_list,
                        name="imagenet",
                        image_format=img_format,
                        pre_process = pre_process,
                        use_cache=True,
                        count=count, 
                        threads=threads,
                        cache_dir=preprocessed_base_dir)
