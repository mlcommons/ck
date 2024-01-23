#!/usr/bin/env python3

# Extended by Grigori Fursin to support MLCommons CM workflow automation language

import os
import onnxruntime as rt
import numpy as np
import time
import json

from PIL import Image

model_path          = os.environ['CK_ENV_ONNX_MODEL_ONNX_FILEPATH']
input_layer_name    = os.environ['CK_ENV_ONNX_MODEL_INPUT_LAYER_NAME']
output_layer_name   = os.environ['CK_ENV_ONNX_MODEL_OUTPUT_LAYER_NAME']
normalize_data_bool = os.getenv('CK_ENV_ONNX_MODEL_NORMALIZE_DATA', '0') in ('YES', 'yes', 'ON', 'on', '1')
subtract_mean_bool  = os.getenv('CK_ENV_ONNX_MODEL_SUBTRACT_MEAN', '0') in ('YES', 'yes', 'ON', 'on', '1')
given_channel_means = os.getenv('ML_MODEL_GIVEN_CHANNEL_MEANS','')
if given_channel_means:
    given_channel_means = np.array(given_channel_means.split(' '), dtype=np.float32)

imagenet_path       = os.environ['CK_ENV_DATASET_IMAGENET_VAL']
labels_path         = os.environ['CK_CAFFE_IMAGENET_SYNSET_WORDS_TXT']
data_layout         = os.environ['ML_MODEL_DATA_LAYOUT']
batch_size          = int( os.environ['CK_BATCH_SIZE'] )
batch_count         = int( os.environ['CK_BATCH_COUNT'] )
CPU_THREADS         = int(os.getenv('CK_HOST_CPU_NUMBER_OF_PROCESSORS',0))


def load_labels(labels_filepath):
    my_labels = []
    input_file = open(labels_filepath, 'r')
    for l in input_file:
        my_labels.append(l.strip())
    return my_labels


def load_and_resize_image(image_filepath, height, width):
    pillow_img = Image.open(image_filepath).resize((width, height)) # sic! The order of dimensions in resize is (W,H)

    # Grigori fixed below
    #input_data = np.float32(pillow_img)
    input_data=np.asarray(pillow_img)
    input_data=np.asarray(input_data, np.float32)

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


def load_a_batch(batch_filenames):
    unconcatenated_batch_data = []
    for image_filename in batch_filenames:
        image_filepath = image_filename
        nchw_data = load_and_resize_image( image_filepath, height, width )
        unconcatenated_batch_data.append( nchw_data )
    batch_data = np.concatenate(unconcatenated_batch_data, axis=0)

    return batch_data



#print("Device: " + rt.get_device())

sess_options = rt.SessionOptions()

if CPU_THREADS > 0:
    sess_options.enable_sequential_execution = False
    sess_options.session_thread_pool_size = CPU_THREADS

if len(rt.get_all_providers()) > 1 and os.environ.get("USE_CUDA", "yes").lower() not in [ "0", "false", "off", "no" ]:
    #Currently considering only CUDAExecutionProvider
    sess = rt.InferenceSession(model_path, sess_options, providers=['CUDAExecutionProvider'])
else:
    sess = rt.InferenceSession(model_path, sess_options, providers=["CPUExecutionProvider"])

input_layer_names   = [ x.name for x in sess.get_inputs() ]     # FIXME: check that input_layer_name belongs to this list
input_layer_name    = input_layer_name or input_layer_names[0]

output_layer_names  = [ x.name for x in sess.get_outputs() ]    # FIXME: check that output_layer_name belongs to this list
output_layer_name   = output_layer_name or output_layer_names[0]

model_input_shape   = sess.get_inputs()[0].shape
model_classes       = sess.get_outputs()[1].shape[1]
labels              = load_labels(labels_path)
bg_class_offset     = model_classes-len(labels)  # 1 means the labels represent classes 1..1000 and the background class 0 has to be skipped

if data_layout == 'NHWC':
    (samples, height, width, channels) = model_input_shape
else:
    (samples, channels, height, width) = model_input_shape

print("")
print("Data layout: {}".format(data_layout) )
print("Input layers: {}".format([ str(x) for x in sess.get_inputs()]))
print("Output layers: {}".format([ str(x) for x in sess.get_outputs()]))
print("Input layer name: " + input_layer_name)
print("Expected input shape: {}".format(model_input_shape))
print("Output layer name: " + output_layer_name)
print("Data normalization: {}".format(normalize_data_bool))
print("Subtract mean: {}".format(subtract_mean_bool))
print('Per-channel means to subtract: {}'.format(given_channel_means))
print("Background/unlabelled classes to skip: {}".format(bg_class_offset))
print("")

starting_index = 1

start_time = time.time()

for batch_idx in range(batch_count):
    print ('')
    print ("Batch {}/{}:".format(batch_idx+1, batch_count))

    batch_filenames = [ imagenet_path + '/' + "ILSVRC2012_val_00000{:03d}.JPEG".format(starting_index + batch_idx*batch_size + i) for i in range(batch_size) ]

    # Grigori: trick to test models:
    if os.environ.get('CM_IMAGE','')!='':
        batch_filenames=[os.environ['CM_IMAGE']]

    batch_data = load_a_batch( batch_filenames )
    #print(batch_data.shape)

    batch_predictions = sess.run([output_layer_name], {input_layer_name: batch_data})[0]

    cm_status = {'classifications':[]}
    
    print ('')
    top_classification = ''
    for in_batch_idx in range(batch_size):
        softmax_vector = batch_predictions[in_batch_idx][bg_class_offset:]    # skipping the background class on the left (if present)
        top5_indices = list(reversed(softmax_vector.argsort()))[:5]

        print(' * ' + batch_filenames[in_batch_idx] + ' :')

        for class_idx in top5_indices:
            if top_classification == '':
                top_classification = labels[class_idx]

            print("\t{}\t{}\t{}".format(class_idx, softmax_vector[class_idx], labels[class_idx]))

            cm_status['classifications'].append({'class_idx':int(class_idx),
                                                 'softmax': float(softmax_vector[class_idx]),
                                                 'label':labels[class_idx]})

    print ('')
    print ('Top classification: {}'.format(top_classification))
    cm_status['top_classification'] = top_classification

avg_time = (time.time() - start_time) / batch_count
cm_status['avg_time'] = avg_time

# Record cm_status to embedded it into CM workflows
with open('tmp-run-state.json', 'w') as cm_file:
   cm_file.write(json.dumps({'cm_app_image_classification_onnx_py':cm_status}, sort_keys=True, indent=2))
