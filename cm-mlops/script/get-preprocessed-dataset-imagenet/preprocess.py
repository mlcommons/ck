import os
import sys

if os.environ.get('CM_DATASET_REFERENCE_PREPROCESSOR', '1') == "0":
    import generic_preprocess
    generic_preprocess.preprocess()
else:
    mlperf_src_path = os.environ['CM_MLPERF_INFERENCE_CLASSIFICATION_AND_DETECTION_PATH']
    python_path = os.path.join(mlperf_src_path, "python")
    sys.path.insert(0, python_path)

    import imagenet
    import dataset

    dataset_path = os.environ['CM_DATASET_PATH']
    dataset_list = os.environ.get('CM_DATASET_IMAGES_LIST', None)
    img_format = os.environ.get('CM_DATASET_DATA_LAYOUT', 'NHWC')
    count = int(os.environ.get('CM_DATASET_SIZE', 1))
    preprocessed_dir = os.environ.get('CM_DATASET_PREPROCESSED_PATH', os.getcwd())
    threads = os.environ.get('CM_NUM_THREADS', os.cpu_count())
    threads = int(os.environ.get('CM_NUM_PREPROCESS_THREADS', threads))

    if os.environ.get('CM_MODEL') == 'mobilenet':
        pre_process = dataset.pre_process_mobilenet
    elif os.environ.get('CM_MODEL', 'resnet50') == 'resnet50' and os.environ.get('CM_PREPROCESS_PYTORCH', '') == "yes":
        pre_process = dataset.pre_process_imagenet_pytorch
    elif os.environ.get('CM_MODEL', 'resnet50') == 'resnet50' and os.environ.get('CM_PREPROCESS_TFLITE_TPU', '') == "yes":
        pre_process = dataset.pre_process_imagenet_tflite_tpu
    else:
        pre_process = dataset.pre_process_vgg

    imagenet.Imagenet(data_path=dataset_path,
                        image_list=dataset_list,
                        name="imagenet",
                        image_format=img_format,
                        pre_process = pre_process,
                        use_cache=True,
                        count=count, 
                        threads=threads,
                        preprocessed_dir=preprocessed_dir)
