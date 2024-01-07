#!/usr/bin/env python3

supported_extensions = ['jpeg', 'jpg', 'gif', 'png']

import os
import cv2
import numpy as np

# Load and preprocess image
def load_image(image_path,            # Full path to processing image
               target_size,           # Desired size of resulting image
               intermediate_size = 0, # Scale to this size then crop to target size
               crop_percentage = 87.5,# Crop to this percentage then scale to target size
               data_type = 'uint8',   # Data type to store
               data_layout = 'nhwc',  # Data layout to store
               convert_to_bgr = False,# Swap image channel RGB -> BGR
               interpolation_method = cv2.INTER_LINEAR # Interpolation method.
               ):

    out_height = target_size
    out_width  = target_size

    def resize_with_aspectratio(img):
        height, width, _ = img.shape
        new_height = int(100. * out_height / crop_percentage)   # intermediate oversized image from which to crop
        new_width = int(100. * out_width / crop_percentage)     # ---------------------- ,, ---------------------
        if height > width:
            w = new_width
            h = int(new_height * height / width)
        else:
            h = new_height
            w = int(new_width * width / height)
        img = cv2.resize(img, (w, h), interpolation = interpolation_method)
        return img

    def center_crop(img):
        height, width, _ = img.shape
        left = int((width - out_width) / 2)
        right = int((width + out_width) / 2)
        top = int((height - out_height) / 2)
        bottom = int((height + out_height) / 2)
        img = img[top:bottom, left:right]
        return img


    img = cv2.imread(image_path)

    if len(img.shape) < 3 or img.shape[2] != 3:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Mimic preprocessing steps from the official reference code.
    img = resize_with_aspectratio(img)
    img = center_crop(img)

    # Convert to BGR.
    if convert_to_bgr:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    return img


def preprocess_files(selected_filenames, source_dir, destination_dir, crop_percentage, square_side, inter_size, convert_to_bgr,
    data_type, data_layout, new_file_extension, normalize_data, subtract_mean, given_channel_means, given_channel_stds, quantize, quant_scale, quant_offset, convert_to_unsigned, interpolation_method):
    "Go through the selected_filenames and preprocess all the files (optionally normalize and subtract mean)"

    output_filenames = []

    for current_idx in range(len(selected_filenames)):
        input_filename = selected_filenames[current_idx]

        full_input_path = os.path.join(source_dir, input_filename)

        image_data = load_image(image_path = full_input_path,
                              target_size = square_side,
                              intermediate_size = inter_size,
                              crop_percentage = crop_percentage,
                              data_type = data_type,
                              convert_to_bgr = convert_to_bgr,
                              interpolation_method = interpolation_method)

        image_data = np.asarray(image_data, dtype=data_type)

        # Normalize.
        if normalize_data:
            image_data = image_data/127.5 - 1.0

        # Subtract mean value.
        if subtract_mean:
            if len(given_channel_means):
                image_data -= given_channel_means
            else:
                image_data -= np.mean(image_data)

        # Subtract standard deviations.
        if len(given_channel_stds):
            image_data /= given_channel_stds

        # NHWC -> NCHW.
        if data_layout == 'nchw':
            image_data = image_data[:,:,0:3].transpose(2, 0, 1)
        
        # Value 1 for quantization to int8
        if quantize == 1:
            image_data = quantize_to_int8(image_data, quant_scale, quant_offset)

        # Value 1 to convert from int8 to uint8
        if convert_to_unsigned == 1:
            image_data = int8_to_uint8(image_data)

        output_filename = input_filename.rsplit('.', 1)[0] + '.' + new_file_extension if new_file_extension else input_filename

        full_output_path = os.path.join(destination_dir, output_filename)
        image_data.tofile(full_output_path)

        print("[{}]:  Stored {}".format(current_idx+1, full_output_path) )

        output_filenames.append(output_filename)

    return output_filenames

def quantize_to_int8(image, scale, offset):
    quant_image = (image/scale + offset).astype(np.float32)
    output = np.copy(quant_image)
    gtZero = (quant_image > 0).astype(int)
    gtZero = gtZero * 0.5
    output=output+gtZero
    ltZero = (quant_image < 0).astype(int)
    ltZero = ltZero * (-0.5)
    output=output+ltZero
    return output.astype(np.int8)


def int8_to_uint8(image):
    image = (image+128).astype(np.uint8)
    return image

def preprocess():
    import sys

    source_dir              = os.environ['CM_DATASET_PATH']
    destination_dir         = os.environ['CM_DATASET_PREPROCESSED_PATH']

    square_side             = int( os.environ['CM_DATASET_INPUT_SQUARE_SIDE'] )
    crop_percentage         = float( os.environ['CM_DATASET_CROP_FACTOR'] )
    inter_size              = int( os.getenv('CM_DATASET_INTERMEDIATE_SIZE', 0) )
    convert_to_bgr          = int( os.getenv('CM_DATASET_CONVERT_TO_BGR', 0) )
    offset                  = int( os.getenv('CM_DATASET_SUBSET_OFFSET', 0) )
    volume                  = int( os.environ['CM_DATASET_SIZE'] )
    fof_name                = os.getenv('CM_DATASET_SUBSET_FOF', 'files.txt')
    data_type               = os.getenv('CM_DATASET_DATA_TYPE_INPUT', 'float32')
    data_layout             = os.getenv('CM_DATASET_DATA_LAYOUT', '').lower()
    new_file_extension      = os.getenv('CM_DATASET_PREPROCESSED_EXTENSION', '')
    normalize_data          = int(os.getenv('CM_DATASET_NORMALIZE_DATA', '0'))
    subtract_mean           = int(os.getenv('CM_DATASET_SUBTRACT_MEANS', '0'))
    given_channel_means     = os.getenv('CM_DATASET_GIVEN_CHANNEL_MEANS', '')
    given_channel_stds     = os.getenv('CM_DATASET_GIVEN_CHANNEL_STDS', '')
    quant_scale             = float( os.environ['CM_DATASET_QUANT_SCALE'] )
    quant_offset            = float( os.environ['CM_DATASET_QUANT_OFFSET'] )
    quantize                = int( os.environ['CM_DATASET_QUANTIZE'] ) #1 for quantize to int8
    convert_to_unsigned     = int( os.environ['CM_DATASET_CONVERT_TO_UNSIGNED'] ) #1 for int8 to uint8

    images_list = os.getenv('CM_DATASET_IMAGES_LIST')

    if given_channel_means:
        given_channel_means = [ float(x) for x in given_channel_means.split(' ') ]

    if given_channel_stds:
        given_channel_stds = [ float(x) for x in given_channel_stds.split(' ') ]

    interpolation_method    = os.getenv('CM_DATASET_INTERPOLATION_METHOD', '')

    print(("From: {}, To: {}, Size: {}, Crop: {}, InterSize: {}, 2BGR: {}, OFF: {}, VOL: '{}', FOF: {},"+
        " DTYPE: {}, DLAYOUT: {}, EXT: {}, NORM: {}, SMEAN: {}, GCM: {}, GSTD: {}, QUANTIZE: {}, QUANT_SCALE: {}, QUANT_OFFSET: {}, CONV_UNSIGNED: {}, INTER: {}").format(
        source_dir, destination_dir, square_side, crop_percentage, inter_size, convert_to_bgr, offset, volume, fof_name,
        data_type, data_layout, new_file_extension, normalize_data, subtract_mean, given_channel_means, given_channel_stds, quantize, quant_scale, quant_offset, convert_to_unsigned, interpolation_method) )

    if interpolation_method == 'INTER_AREA':
        # Used for ResNet in pre_process_vgg.
        interpolation_method = cv2.INTER_AREA
    else:
        # Default interpolation method.
        interpolation_method = cv2.INTER_LINEAR

    filenames = []
    if images_list:
        with open(images_list) as f:
            filenames = f.read().splitlines()
    else:
        filenames = sorted(os.listdir(source_dir))


    if os.path.isdir(source_dir):
        sorted_filenames = [filename for filename in filenames if any(filename.lower().endswith(extension) for extension in supported_extensions) and not filename.startswith(".") ]

        total_volume = len(sorted_filenames)

        if offset<0:        # support offsets "from the right"
            offset += total_volume

        selected_filenames = sorted_filenames[offset:offset+volume]

    assert len(selected_filenames) == volume

    output_filenames = preprocess_files(
        selected_filenames, source_dir, destination_dir, crop_percentage, square_side, inter_size, convert_to_bgr,
        data_type, data_layout, new_file_extension, normalize_data, subtract_mean, given_channel_means, given_channel_stds, quantize, quant_scale, quant_offset, convert_to_unsigned, interpolation_method)

    fof_full_path = os.path.join(destination_dir, fof_name)
    with open(fof_full_path, 'w') as fof:
        for filename in output_filenames:
            fof.write(filename + '\n')
