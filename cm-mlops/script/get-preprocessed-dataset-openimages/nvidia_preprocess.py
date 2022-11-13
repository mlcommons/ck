#!/usr/bin/env python3
# Copyright (c) 2022, NVIDIA CORPORATION. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#           http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import math
import os
from PIL import Image
import shutil

from code.common.fix_sys_path import ScopedRestrictedImport
with ScopedRestrictedImport():
    import numpy as np
    import torch
    from torchvision.transforms import functional as F

from code.common import logging
from code.common.image_preprocessor import ImagePreprocessor, center_crop, resize_with_aspectratio


def preprocess_openimage_for_retinanet(data_dir, preprocessed_data_dir, formats, overwrite=False, cal_only=False, val_only=False):
    def loader(fpath):
        loaded_tensor = F.to_tensor(Image.open(fpath).convert("RGB"))
        dtype = torch.float32
        device = torch.device("cpu")
        image_size = [800, 800]
        image_std = [0.229, 0.224, 0.225]
        image_mean = [0.485, 0.456, 0.406]
        mean = torch.as_tensor(image_mean, dtype=dtype, device=device)
        std = torch.as_tensor(image_std, dtype=dtype, device=device)
        img_norm = (loaded_tensor - mean[:, None, None]) / std[:, None, None]
        img_resize = torch.nn.functional.interpolate(img_norm[None], size=image_size, scale_factor=None, mode='bilinear',
                                                     recompute_scale_factor=None, align_corners=False)[0]
        img = img_resize.numpy()
        return img


    def quantizer(image):
        # Dynamic range of image is [-2.64064, 2.64064] based on calibration cache.
        # Calculated by: 
        # np.uint32(int("3caa54fc", base=16)).view(np.dtype('float32')).item() * 127.0
        max_abs = 2.64064
        image_int8 = image.clip(-max_abs, max_abs) / max_abs * 127.0
        return image_int8.astype(dtype=np.int8, order='C')


    preprocessor = ImagePreprocessor(loader, quantizer)
    if not val_only:
        # Preprocess calibration set. FP32 only because calibrator always takes FP32 input.
        preprocessor.run(os.path.join(data_dir, "open-images-v6-mlperf", "calibration", "train", "data"),
                         os.path.join(preprocessed_data_dir, "open-images-v6-mlperf", "calibration", "Retinanet"),
                         "data_maps/open-images-v6-mlperf/cal_map.txt", ["fp32"], overwrite)
    if not cal_only:
        # Preprocess validation set.
        preprocessor.run(os.path.join(data_dir, "open-images-v6-mlperf", "validation", "data"),
                         os.path.join(preprocessed_data_dir, "open-images-v6-mlperf", "validation", "Retinanet"),
                         "data_maps/open-images-v6-mlperf/val_map.txt", formats, overwrite)


def copy_openimage_annotations(data_dir, preprocessed_data_dir):
    src_dir = os.path.join(data_dir, "open-images-v6-mlperf/annotations")
    dst_dir = os.path.join(preprocessed_data_dir, "open-images-v6-mlperf/annotations")
    if not os.path.exists(dst_dir):
        shutil.copytree(src_dir, dst_dir)


def main():
    # Parse arguments to identify the data directory with the input images
    #   and the output directory for the preprocessed images.
    # The data dicretory is assumed to have the following structure:
    # <data_dir>
    #  └── coco
    #      ├── annotations
    #      ├── calibration
    #      └── validation
    # And the output directory will have the following structure:
    # <preprocessed_data_dir>
    #  └── open-images-v6-mlperf
    #      ├── annotations
    #      ├── calibration
    #      │   └── Retinanet
    #      │       └── fp32
    #      └── validation
    #          └── Retinanet
    #              └── int8_linear
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data_dir", "-d",
        help="Specifies the directory containing the input images.",
        default="build/data"
    )
    parser.add_argument(
        "--preprocessed_data_dir", "-o",
        help="Specifies the output directory for the preprocessed data.",
        default="build/preprocessed_data"
    )
    parser.add_argument(
        "--formats", "-t",
        help="Comma-separated list of formats. Choices: fp32, int8_linear, int8_chw4.",
        default="default"
    )
    parser.add_argument(
        "--overwrite", "-f",
        help="Overwrite existing files.",
        action="store_true"
    )
    parser.add_argument(
        "--cal_only",
        help="Only preprocess calibration set.",
        action="store_true"
    )
    parser.add_argument(
        "--val_only",
        help="Only preprocess validation set.",
        action="store_true"
    )
    args = parser.parse_args()
    data_dir = args.data_dir
    preprocessed_data_dir = args.preprocessed_data_dir
    formats = args.formats.split(",")
    overwrite = args.overwrite
    cal_only = args.cal_only
    val_only = args.val_only
    default_formats = ["int8_linear"]

    # Now, actually preprocess the input images
    logging.info("Loading and preprocessing images. This might take a while...")
    if args.formats == "default":
        formats = default_formats
    preprocess_openimage_for_retinanet(data_dir, preprocessed_data_dir, formats, overwrite, cal_only, val_only)

    # Copy annotations from data_dir to preprocessed_data_dir.
    copy_openimage_annotations(data_dir, preprocessed_data_dir)

    logging.info("Preprocessing done.")


if __name__ == '__main__':
    main()
