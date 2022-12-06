#!/usr/bin/env python3

import json
import time
import os
import shutil
import numpy as np


import torch
import torchvision.models as models

import imagenet_helper
from imagenet_helper import (load_preprocessed_batch, image_list, class_labels, BATCH_SIZE)

## Writing the results out:
#
RESULTS_DIR             = os.getenv('CM_RESULTS_DIR')
FULL_REPORT             = os.getenv('CM_SILENT_MODE', '0') in ('NO', 'no', 'OFF', 'off', '0')

## Processing by batches:
#
BATCH_COUNT             = int(os.getenv('CM_BATCH_COUNT', 1))

## Enabling GPU if available and not disabled:
#
USE_CUDA                = (os.getenv('USE_CUDA', '').strip()=='yes')


labels_path         = os.environ['CM_CAFFE_IMAGENET_SYNSET_WORDS_TXT']

def load_labels(labels_filepath):
    my_labels = []
    input_file = open(labels_filepath, 'r')
    for l in input_file:
        my_labels.append(l.strip())
    return my_labels


labels              = load_labels(labels_path)


data_layout         = os.environ['ML_MODEL_DATA_LAYOUT']



def main():
    global BATCH_SIZE
    global BATCH_COUNT

    setup_time_begin = time.time()

    bg_class_offset=0

    # Cleanup results directory
    if os.path.isdir(RESULTS_DIR):
        shutil.rmtree(RESULTS_DIR)
    os.mkdir(RESULTS_DIR)

    # Load the [cached] Torch model
    path_to_model_pth = os.environ['CM_ML_MODEL_FILE_WITH_PATH']

    model=models.resnet50(pretrained=False)
    model.load_state_dict(torch.load(path_to_model_pth))

    model.eval()

    # move the model to GPU for speed if available
    if USE_CUDA:
        model.to('cuda')

    setup_time = time.time() - setup_time_begin

    # Run batched mode
    test_time_begin = time.time()
    image_index = 0
    total_load_time = 0
    total_classification_time = 0
    first_classification_time = 0
    images_loaded = 0

    image_path = os.environ.get('CM_INPUT','')
    if image_path !='':

        normalize_data_bool=True
        subtract_mean_bool=False
        
        from PIL import Image

        def load_and_resize_image(image_filepath, height, width):
            pillow_img = Image.open(image_filepath).resize((width, height)) # sic! The order of dimensions in resize is (W,H)

            input_data = np.float32(pillow_img)

            # Normalize
            if normalize_data_bool:
                input_data = input_data/127.5 - 1.0

            # Subtract mean value
            if subtract_mean_bool:
                if len(given_channel_means):
                    input_data -= given_channel_means
                else:
                    input_data -= np.mean(input_data)

        #    print(np.array(pillow_img).shape)
            nhwc_data = np.expand_dims(input_data, axis=0)

            if data_layout == 'NHWC':
                # print(nhwc_data.shape)
                return nhwc_data
            else:
                nchw_data = nhwc_data.transpose(0,3,1,2)
                # print(nchw_data.shape)
                return nchw_data

        BATCH_COUNT=1
    
    
    for batch_index in range(BATCH_COUNT):
        batch_number = batch_index+1
        if FULL_REPORT or (batch_number % 10 == 0):
            print("\nBatch {} of {}".format(batch_number, BATCH_COUNT))
      
        begin_time = time.time()

        if image_path=='':
            batch_data, image_index = load_preprocessed_batch(image_list, image_index)
        else:
            batch_data = load_and_resize_image(image_path, 224, 224)
            image_index = 1

        torch_batch = torch.from_numpy( batch_data )

        load_time = time.time() - begin_time
        total_load_time += load_time
        images_loaded += BATCH_SIZE
        if FULL_REPORT:
            print("Batch loaded in %fs" % (load_time))

        # Classify one batch
        begin_time = time.time()

        # move the input to GPU for speed if available
        if USE_CUDA:
            torch_batch = torch_batch.to('cuda')

        with torch.no_grad():
            batch_results = model( torch_batch )

        classification_time = time.time() - begin_time
        if FULL_REPORT:
            print("Batch classified in %fs" % (classification_time))

        total_classification_time += classification_time
        # Remember first batch prediction time
        if batch_index == 0:
            first_classification_time = classification_time

        # Process results
        for index_in_batch in range(BATCH_SIZE):
            softmax_vector = batch_results[index_in_batch][bg_class_offset:]    # skipping the background class on the left (if present)
            global_index = batch_index * BATCH_SIZE + index_in_batch

            res_file = os.path.join(RESULTS_DIR, image_list[global_index])

            with open(res_file + '.txt', 'w') as f:
                for prob in softmax_vector:
                    f.write('{}\n'.format(prob))

            top5_indices = list(reversed(softmax_vector.argsort()))[:5]
            for class_idx in top5_indices:
                print("\t{}\t{}\t{}".format(class_idx, softmax_vector[class_idx], labels[class_idx]))
            print("")
                    

    test_time = time.time() - test_time_begin
 
    if BATCH_COUNT > 1:
        avg_classification_time = (total_classification_time - first_classification_time) / (images_loaded - BATCH_SIZE)
    else:
        avg_classification_time = total_classification_time / images_loaded

    avg_load_time = total_load_time / images_loaded

    # Store benchmarking results:
    output_dict = {
        'setup_time_s': setup_time,
        'test_time_s': test_time,
        'images_load_time_total_s': total_load_time,
        'images_load_time_avg_s': avg_load_time,
        'prediction_time_total_s': total_classification_time,
        'prediction_time_avg_s': avg_classification_time,

        'avg_time_ms': avg_classification_time * 1000,
        'avg_fps': 1.0 / avg_classification_time,
        'batch_time_ms': avg_classification_time * 1000 * BATCH_SIZE,
        'batch_size': BATCH_SIZE,
    }
    with open('tmp-ck-timer.json', 'w') as out_file:
        json.dump(output_dict, out_file, indent=4, sort_keys=True)


if __name__ == '__main__':
    main()
