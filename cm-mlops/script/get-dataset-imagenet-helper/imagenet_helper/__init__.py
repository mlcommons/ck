#!/usr/bin/env python3

import os
import numpy as np


## Processing in batches:
#
BATCH_SIZE              = int(os.getenv('CM_BATCH_SIZE', 1))


## Model properties:
#
MODEL_IMAGE_HEIGHT      = int(os.getenv('CM_ML_MODEL_IMAGE_HEIGHT',
                              os.getenv('CM_ONNX_MODEL_IMAGE_HEIGHT',
                              os.getenv('CM_TENSORFLOW_MODEL_IMAGE_HEIGHT',
                              ''))))
MODEL_IMAGE_WIDTH       = int(os.getenv('CM_ML_MODEL_IMAGE_WIDTH',
                              os.getenv('CM_ONNX_MODEL_IMAGE_WIDTH',
                              os.getenv('CM_TENSORFLOW_MODEL_IMAGE_WIDTH',
                              ''))))
MODEL_IMAGE_CHANNELS    = int(os.getenv('CM_ML_MODEL_IMAGE_CHANNELS', 3))
MODEL_DATA_LAYOUT       = os.getenv('CM_ML_MODEL_DATA_LAYOUT', 'NCHW')
MODEL_COLOURS_BGR       = os.getenv('CM_ML_MODEL_COLOUR_CHANNELS_BGR', 'NO') in ('YES', 'yes', 'ON', 'on', '1')
MODEL_INPUT_DATA_TYPE   = os.getenv('CM_ML_MODEL_INPUT_DATA_TYPE', 'float32')
MODEL_DATA_TYPE         = os.getenv('CM_ML_MODEL_DATA_TYPE', '(unknown)')
MODEL_USE_DLA           = os.getenv('CM_ML_MODEL_USE_DLA', 'NO') in ('YES', 'yes', 'ON', 'on', '1')
MODEL_MAX_BATCH_SIZE    = int(os.getenv('CM_ML_MODEL_MAX_BATCH_SIZE', BATCH_SIZE))


## Internal processing:
#
INTERMEDIATE_DATA_TYPE  = np.float32    # default for internal conversion
#INTERMEDIATE_DATA_TYPE  = np.int8       # affects the accuracy a bit


## Image normalization:
#
MODEL_NORMALIZE_DATA    = os.getenv('CM_ML_MODEL_NORMALIZE_DATA') in ('YES', 'yes', 'ON', 'on', '1')
MODEL_NORMALIZE_LOWER   = float(os.getenv('CM_ML_MODEL_NORMALIZE_LOWER', -1.0))
MODEL_NORMALIZE_UPPER   = float(os.getenv('CM_ML_MODEL_NORMALIZE_UPPER',  1.0))
SUBTRACT_MEAN           = os.getenv('CM_ML_MODEL_SUBTRACT_MEANS', 'YES') in ('YES', 'yes', 'ON', 'on', '1')
GIVEN_CHANNEL_MEANS     = os.getenv('CM_ML_MODEL_GIVEN_CHANNEL_MEANS', '')
if GIVEN_CHANNEL_MEANS:
    GIVEN_CHANNEL_MEANS = np.fromstring(GIVEN_CHANNEL_MEANS, dtype=np.float32, sep=' ').astype(INTERMEDIATE_DATA_TYPE)
    if MODEL_COLOURS_BGR:
        GIVEN_CHANNEL_MEANS = GIVEN_CHANNEL_MEANS[::-1]     # swapping Red and Blue colour channels

GIVEN_CHANNEL_STDS      = os.getenv('CM_ML_MODEL_GIVEN_CHANNEL_STDS', '')
if GIVEN_CHANNEL_STDS:
    GIVEN_CHANNEL_STDS = np.fromstring(GIVEN_CHANNEL_STDS, dtype=np.float32, sep=' ').astype(INTERMEDIATE_DATA_TYPE)
    if MODEL_COLOURS_BGR:
        GIVEN_CHANNEL_STDS  = GIVEN_CHANNEL_STDS[::-1]      # swapping Red and Blue colour channels



## ImageNet dataset properties:
#
LABELS_PATH             = os.environ['CM_CAFFE_IMAGENET_SYNSET_WORDS_TXT']


## Preprocessed input images' properties:
#
IMAGE_DIR               = os.getenv('CM_DATASET_PREPROCESSED_PATH')
IMAGE_DATA_TYPE         = os.getenv('CM_DATASET_PREPROCESSED_DATA_TYPE', 'float32')


def load_labels(labels_filepath):
    my_labels = []
    input_file = open(labels_filepath, 'r')
    for l in input_file:
        my_labels.append(l.strip())
    return my_labels

class_labels = load_labels(LABELS_PATH)


# Load preprocessed image filenames:
image_list = []
all_images = os.listdir(IMAGE_DIR)
for image_file in all_images:
    if image_file.endswith('.npy'):
        image_list.append(image_file)

def load_image_by_index_and_normalize(image_index):

    img_file = os.path.join(IMAGE_DIR, image_list[image_index])

    img = np.fromfile(img_file, np.dtype(IMAGE_DATA_TYPE))
    #img = img.reshape((1,MODEL_IMAGE_HEIGHT, MODEL_IMAGE_WIDTH, 3))
    img.resize(224*224*3)
    img = img.reshape((MODEL_IMAGE_HEIGHT, MODEL_IMAGE_WIDTH, MODEL_IMAGE_CHANNELS))
    if MODEL_COLOURS_BGR:
        img = img[...,::-1]     # swapping Red and Blue colour channels

    if IMAGE_DATA_TYPE != 'float32':
        img = img.astype(np.float32)

        # Normalize
        if MODEL_NORMALIZE_DATA:
            img /= (255.0/(MODEL_NORMALIZE_UPPER-MODEL_NORMALIZE_LOWER))
            img += MODEL_NORMALIZE_LOWER

        # Subtract mean value
        if len(GIVEN_CHANNEL_MEANS):
            img -= GIVEN_CHANNEL_MEANS
        elif SUBTRACT_MEAN:
            img -= np.mean(img, axis=(0,1), keepdims=True)

        if len(GIVEN_CHANNEL_STDS):
            img /= GIVEN_CHANNEL_STDS

    if MODEL_INPUT_DATA_TYPE == 'int8' or INTERMEDIATE_DATA_TYPE==np.int8:
        img = np.clip(img, -128, 127).astype(INTERMEDIATE_DATA_TYPE)

    if MODEL_DATA_LAYOUT == 'NCHW':
        img = img.transpose(2,0,1)
    elif MODEL_DATA_LAYOUT == 'CHW4':
        img = np.pad(img, ((0,0), (0,0), (0,1)), 'constant')

    # Add img to batch
    return img.astype(MODEL_INPUT_DATA_TYPE)


def load_preprocessed_batch(image_list, image_index):
    batch_data = None
    for in_batch_idx in range(BATCH_SIZE):
        img = load_image_by_index_and_normalize(image_index)
        if batch_data is None:
            batch_data = np.empty( (BATCH_SIZE, *img.shape), dtype=MODEL_INPUT_DATA_TYPE)
        batch_data[in_batch_idx] = img
        image_index += 1

    #print('Data shape: {}'.format(batch_data.shape))

    if MODEL_USE_DLA and MODEL_MAX_BATCH_SIZE>len(batch_data):
        return np.pad(batch_data, ((0,MODEL_MAX_BATCH_SIZE-len(batch_data)), (0,0), (0,0), (0,0)), 'constant'), image_index
    else:
        return batch_data, image_index
