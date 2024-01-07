#!/usr/bin/env python3

import os
import json
import numpy as np
from PIL import Image
import torch
import torchvision

SUPPORTED_EXTENSIONS = ['jpeg', 'jpg', 'gif', 'png']

def load_image(image_path, target_size, data_type='uint8', convert_to_bgr=False,
               normalize_data=False, normalize_lower=-1, normalize_upper=1,
               subtract_mean=False, given_channel_means='', given_channel_stds='',
               quantize=0, quant_scale=1, quant_offset=0, convert_to_unsigned=0):
    if not convert_to_bgr:
        image = Image.open(image_path).convert('RGB')
    else:
        image = Image.open(image_path).convert('BGR')

    tensor_image = torchvision.transforms.functional.to_tensor(image)
    mean = torch.as_tensor(given_channel_means)
    std = torch.as_tensor(given_channel_stds)
    normalized_image = (tensor_image - mean[:, None, None]) / std[:, None, None]

    resized_image = torch.nn.functional.interpolate(normalized_image[None],
                                                    size=(target_size, target_size),
                                                    mode='bilinear')[0].numpy()

    if quantize == 1:
        resized_image = quantize_to_uint8(resized_image, quant_scale, quant_offset)

    original_height, original_width, _ = resized_image.shape
    batch_shape = (1, target_size, target_size, 3)
    batch_data = resized_image.reshape(batch_shape)

    return batch_data, original_width, original_height

def quantize_to_uint8(image, scale, offset):
    quantized_image = (image.astype(np.float64) / scale + offset).astype(np.float64)
    output = np.round_(quantized_image)
    output = np.clip(output, 0, 255)
    return output.astype(np.uint8)

def preprocess_files(selected_filenames, source_dir, destination_dir, square_side,
                     data_type, convert_to_bgr, normalize_data, normalize_lower,
                     normalize_upper, subtract_mean, given_channel_means,
                     given_channel_stds, quantize, quant_scale, quant_offset,
                     convert_to_unsigned, new_file_extension):
    output_signatures = []

    for current_idx, input_filename in enumerate(selected_filenames):
        full_input_path = os.path.join(source_dir, input_filename)
        image_data, original_width, original_height = load_image(
            image_path=full_input_path,
            target_size=square_side,
            data_type=data_type,
            convert_to_bgr=convert_to_bgr,
            normalize_data=normalize_data,
            normalize_lower=normalize_lower,
            normalize_upper=normalize_upper,
            subtract_mean=subtract_mean,
            given_channel_means=given_channel_means,
            given_channel_stds=given_channel_stds,
            quantize=quantize,
            quant_scale=quant_scale,
            quant_offset=quant_offset,
            convert_to_unsigned=convert_to_unsigned
        )

        output_filename = f"{input_filename.rsplit('.', 1)[0]}.{new_file_extension}" if new_file_extension else input_filename
        full_output_path = os.path.join(destination_dir, output_filename)
        image_data.tofile(full_output_path)

        print(f"[{current_idx+1}]:  Stored {full_output_path}")
        output_signatures.append(f'{output_filename};{original_width};{original_height}')

    return output_signatures

def preprocess():
    source_directory = os.environ['CM_DATASET_PATH']
    destination_directory = os.environ['CM_DATASET_PREPROCESSED_PATH']

    intermediate_data_type = os.environ.get('CM_DATASET_INTERMEDIATE_DATA_TYPE', np.float32)
    square_side = int(os.environ['CM_DATASET_INPUT_SQUARE_SIDE'])
    crop_percentage = float(os.environ['CM_DATASET_CROP_FACTOR'])
    inter_size = int(os.getenv('CM_DATASET_INTERMEDIATE_SIZE', 0))
    convert_to_bgr = int(os.getenv('CM_DATASET_CONVERT_TO_BGR', 0))
    offset = int(os.getenv('CM_DATASET_SUBSET_OFFSET', 0))
    volume = int(os.environ['CM_DATASET_SIZE'])
    fof_name = os.getenv('CM_DATASET_SUBSET_FOF', 'files.txt')
    data_type = os.getenv('CM_DATASET_DATA_TYPE_INPUT', 'float32')
    input_data_type = os.getenv('CM_DATASET_DATA_TYPE_INPUT', 'float32')
    data_layout = os.getenv('CM_DATASET_DATA_LAYOUT', '').lower()
    new_file_extension = os.getenv('CM_DATASET_PREPROCESSED_EXTENSION', '')
    normalize_data = int(os.getenv('CM_DATASET_NORMALIZE_DATA', '0'))
    subtract_mean = int(os.getenv('CM_DATASET_SUBTRACT_MEANS', '0'))
    given_channel_means = os.getenv('CM_DATASET_GIVEN_CHANNEL_MEANS', '')
    given_channel_stds = os.getenv('CM_DATASET_GIVEN_CHANNEL_STDS', '')
    quant_scale = float(os.environ['CM_DATASET_QUANT_SCALE'])
    quant_offset = float(os.environ['CM_DATASET_QUANT_OFFSET'])
    quantize = int(os.environ['CM_DATASET_QUANTIZE'])  # 1 for quantize to int8
    convert_to_unsigned = int(os.environ['CM_DATASET_CONVERT_TO_UNSIGNED'])  # 1 for int8 to uint8

    images_list = os.getenv('CM_DATASET_IMAGES_LIST')
    interpolation_method = os.getenv('CM_DATASET_INTERPOLATION_METHOD', '')

    annotations_filepath = os.environ['CM_DATASET_ANNOTATIONS_FILE_PATH']
    is_calibration = os.environ['CM_DATASET_TYPE'] == "calibration"
    image_file = os.getenv('CM_IMAGE_FILE', '')

    normalize_lower = float(os.getenv('CM_DATASET_NORMALIZE_LOWER', -1.0))
    normalize_upper = float(os.getenv('CM_DATASET_NORMALIZE_UPPER', 1.0))

    if given_channel_means:
        given_channel_means = np.fromstring(given_channel_means, dtype=np.float32, sep=' ').astype(intermediate_data_type)
        if convert_to_bgr:
            given_channel_means = given_channel_means[::-1]

    given_channel_stds = os.getenv('CM_DATASET_GIVEN_CHANNEL_STDS', '')
    if given_channel_stds:
        given_channel_stds = np.fromstring(given_channel_stds, dtype=np.float32, sep=' ').astype(intermediate_data_type)
        if convert_to_bgr:
            given_channel_stds = given_channel_stds[::-1]

    print(f"From: {source_directory}, To: {destination_directory}, Size: {square_side}, Crop: {crop_percentage}, InterSize: {inter_size}, 2BGR: {convert_to_bgr}, " +
      f"OFF: {offset}, VOL: '{volume}', FOF: {fof_name}, DTYPE: {data_type}, DLAYOUT: {data_layout}, EXT: {new_file_extension}, " +
      f"NORM: {normalize_data}, SMEAN: {subtract_mean}, GCM: {given_channel_means}, GSTD: {given_channel_stds}, QUANTIZE: {quantize}, QUANT_SCALE: {quant_scale}, " +
      f"QUANT_OFFSET: {quant_offset}, CONV_UNSIGNED: {convert_to_unsigned}, INTER: {interpolation_method}")


    if image_file:
        source_directory = os.path.dirname(image_file)
        selected_filenames = [os.path.basename(image_file)]
    else:
        if annotations_filepath and not is_calibration:
            with open(annotations_filepath, "r") as annotations_fh:
                annotations_struct = json.load(annotations_fh)
            ordered_filenames = [image_entry['file_name'] for image_entry in annotations_struct['images']]
        elif os.path.isdir(source_directory):
            ordered_filenames = [filename for filename in sorted(os.listdir(source_directory)) if any(filename.lower().endswith(extension) for extension in SUPPORTED_EXTENSIONS)]
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), source_directory)

        total_volume = len(ordered_filenames)

        if offset < 0:
            offset += total_volume

        if not volume:
            volume = total_volume - offset

        selected_filenames = ordered_filenames[offset:offset + volume]

    output_signatures = preprocess_files(selected_filenames, source_directory, destination_directory, square_side, data_type,
                                         convert_to_bgr, normalize_data, normalize_lower, normalize_upper,
                                         subtract_mean, given_channel_means, given_channel_stds, quantize,
                                         quant_scale, quant_offset, convert_to_unsigned, new_file_extension)

    fof_full_path = os.path.join(destination_directory, fof_name)
    with open(fof_full_path, 'w') as fof_file:
        for filename in output_signatures:
            fof_file.write(f'{filename}\n')

if __name__ == "__main__":
    preprocess()

