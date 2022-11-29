#!/usr/bin/env python3
# Copyright (c) 2022, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


__doc__ = """Scripts that take a retinanet engine and openImage input, infer the output and test the accuracy
"""

import argparse
import json
import os
import sys
import glob
import random
import time
import pycuda
from PIL import Image
from importlib import import_module
from typing import Dict, Tuple, List, Optional

from code.common.fix_sys_path import ScopedRestrictedImport
#with ScopedRestrictedImport():
import numpy as np
import torch  # Retinanet model source requires GPU installation of PyTorch 1.10
from torchvision.transforms import functional as F
import onnx
import tensorrt as trt
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

from code.common import logging
from code.common.constants import TRT_LOGGER, Scenario
from code.common.systems.system_list import DETECTED_SYSTEM
from code.common.runner import EngineRunner, get_input_format
from code.common.systems.system_list import SystemClassifications
from code.plugin import load_trt_plugin
RetinanetEntropyCalibrator = import_module("code.retinanet.tensorrt.calibrator").RetinanetEntropyCalibrator

G_RETINANET_NUM_CLASSES = 264
G_RETINANET_IMG_SIZE = (800, 800)
G_RETINANET_INPUT_SHAPE = (3, 800, 800)
G_OPENIMAGE_CALSET_PATH = "build/data/open-images-v6-mlperf/calibration/train/data"
G_OPENIMAGE_CALMAP_PATH = "data_maps/open-images-v6-mlperf/cal_map.txt"
G_OPENIMAGE_VALSET_PATH = os.path.join(os.environ.get("CM_DATASET_PATH", "build/data/open-images-v6-mlperf"), "validation", "data")
G_OPENIMAGE_VALMAP_PATH = "data_maps/open-images-v6-mlperf/val_map.txt"
G_OPENIMAGE_ANNO_PATH = os.path.join(os.environ.get("CM_DATASET_PATH","build/data/open-images-v6-mlperf"), "annotations", "openimages-mlperf.json")
G_OPENIMAGE_PREPROCESSED_INT8_PATH = "build/preprocessed_data/open-images-v6-mlperf/validation/Retinanet/int8_linear"
# Using EfficientNMS now
G_RETINANET_CALIBRATION_CACHE_PATH = "code/retinanet/tensorrt/calibrator.cache"


def load_img_pytorch(fpath: str, do_transform=False) -> torch.tensor:
    """
    Load the image from file into torch tensor
    From mlcommon training repo:
    https://github.com/mlcommons/training/blob/master/single_stage_detector/ssd/model/transform.py#L66

    Args:
        fpath (str): the path to the image file
        do_transform (bool): whether to do postprocess (resize + normalize)
    """
    loaded_tensor = F.to_tensor(Image.open(fpath).convert("RGB"))
    if do_transform:
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
        return img_resize

    return loaded_tensor


class FirstLayerConvActPoolTacticSelector(trt.IAlgorithmSelector):
    def select_algorithms(self, ctx, choices):
        if "Conv_0 + 1783 + Mul_1 + 1785 + Add_2 + Relu_3 + MaxPool_4" in ctx.name:  # Apply to the first layer
            # MLPINF-1833: Disabled CaskConvActPool for TRT 8.5.0.4
            # TRT 8.5.0.4 has a bug with CaskConvActPool which has been fixed since 8.5.0.5
            forbidden_set = {
                -3689373275198309793,  # 0xccccb68da7fc3a5f
                -4219016963003938541,  # 0xc5730a6ceacd8913
                -4709698786673109216,  # 0xbea3c9e81542d720
                8863348452769974412,  # 0x7b00f0752fdcc88c
                -216502845640484144,  # 0xfcfed3cf18bcdad0
                -2840175123683203852,  # 0xd895abc5dcf624f4
                4391967500208500226,  # 0x3cf3672bfafcee02
                -3076721233724812250,  # 0xd54d4a56ceee5426
                8268411641074121664,  # 0x72bf4c9462ed7bc0
                3484514246525022387,  # 0x305b7b3ed6e970b3
                679919370278938099,  # 0x096f8f109d6225f3
                1531503914513228020,  # 0x1540feb22cae60f4
                8162590574723450606,  # 0x714758e16557c6ee
                6137316588591593674,  # 0x552c20eba11d38ca
                -5252194382421728148,  # 0xb71c75095873646c
                -2136593403804660582,  # 0xe2594b9e90c7cc9a
                58603908831090367,  # 0x00d033f1d05396bf
                1454666201826561687,  # 0x1430033412a38e97
                -7506077189063215810,  # 0xd43db7d0f0e3ba45
                -3153162056066942395,  # 0x9521940f435d0c18
                -7700711094551245800,  # 0xf126325c0aa4aa02
                -1070112490556970494,  # 0x97d50e90c139753e
            }
            filtered_idxs = [idx for idx, choice in enumerate(choices) if choice.algorithm_variant.tactic not in forbidden_set]
            to_ret = filtered_idxs
        else:
            # By default, say that all tactics are acceptable:
            to_ret = [idx for idx, _ in enumerate(choices)]
        return to_ret

    def report_algorithms(self, ctx, choices):
        pass


class TRTTester:

    def __init__(self, engine_file, batch_size, precision, onnx_path,
                 skip_engine_build=False, verbose=False,
                 output_file="build/retinanet_trt.out"
                 ):
        """
        Test the accuracy using the onnx file and TensorRT runtime.
        The tester is able to build the engine from onnx.
        """
        self.batch_size = batch_size
        self.verbose = verbose
        self.onnx_path = onnx_path
        self.engine_file = engine_file
        self.cache_file = G_RETINANET_CALIBRATION_CACHE_PATH
        self.precision = precision

        # TensorRT engine related fields
        # Not supported on dla
        self.dla_core = None

        # Initiate the plugin and logger
        self.logger = TRT_LOGGER  # Use the global singleton, which is required by TRT.
        self.logger.min_severity = trt.Logger.VERBOSE if self.verbose else trt.Logger.INFO
        load_trt_plugin("retinanet")
        trt.init_libnvinfer_plugins(self.logger, "")

        if self.onnx_path is not None and not skip_engine_build:
            print(f"Creating engines from onnx: {self.onnx_path}")
            self.create_trt_engine()
        else:
            if not os.path.exists(engine_file):
                raise RuntimeError(f"Cannot find engine file {engine_file}. Please supply the onnx file or engine file.")

        self.runner = EngineRunner(self.engine_file, verbose=verbose)

        # OpenImage related fields
        self.image_dir = G_OPENIMAGE_VALSET_PATH
        self.val_annotate = G_OPENIMAGE_ANNO_PATH
        self.output_file = output_file

    def apply_flag(self, flag):
        """Apply a TRT builder flag."""
        self.builder_config.flags = (self.builder_config.flags) | (1 << int(flag))

    def clear_flag(self, flag):
        """Clear a TRT builder flag."""
        self.builder_config.flags = (self.builder_config.flags) & ~(1 << int(flag))

    # Helper function to build a TRT engine from ONNX file
    def create_trt_engine(self):
        self.builder = trt.Builder(self.logger)
        self.builder_config = self.builder.create_builder_config()
        self.builder_config.max_workspace_size = 8 << 30
        self.builder_config.profiling_verbosity = trt.ProfilingVerbosity.DETAILED if self.verbose else trt.ProfilingVerbosity.LAYER_NAMES_ONLY

        # Precision flags
        self.clear_flag(trt.BuilderFlag.TF32)
        if self.precision == "fp32":
            self.input_dtype = "fp32"
            self.input_format = "linear"
        elif self.precision == "int8":
            self.input_dtype = "int8"
            self.input_format = "linear"
            self.apply_flag(trt.BuilderFlag.INT8)

            # Calibrator for int8
            preprocessed_data_dir = "build/preprocessed_data"
            calib_image_dir = os.path.join(preprocessed_data_dir, "open-images-v6-mlperf/calibration/Retinanet/fp32")
            self.calibrator = RetinanetEntropyCalibrator(data_dir=calib_image_dir,
                                                         cache_file=self.cache_file, batch_size=10, max_batches=50,
                                                         force_calibration=False, calib_data_map=G_OPENIMAGE_CALMAP_PATH)
            self.builder_config.int8_calibrator = self.calibrator

            # Apply tactic selector bypassing conv act pool for Orin:
            if SystemClassifications.is_orin():
                tactic_selector = FirstLayerConvActPoolTacticSelector()
                self.builder_config.algorithm_selector = tactic_selector
        else:
            raise Exception(f"{self.precision} not supported yet.")

        self.network = self.builder.create_network(1 << int(trt.NetworkDefinitionCreationFlag.EXPLICIT_BATCH))
        model = onnx.load(self.onnx_path)
        parser = trt.OnnxParser(self.network, self.logger)
        success = parser.parse(onnx._serialize(model))
        if not success:
            err_desc = parser.get_error(0).desc()
            raise RuntimeError(f"Retinanet onnx model processing failed! Error: {err_desc}")

        # Set the network input type
        if self.precision == "int8":
            self.network.get_input(0).dtype = trt.int8

        # Add obey_precision_constraints flag to suppress reformat
        self.apply_flag(trt.BuilderFlag.OBEY_PRECISION_CONSTRAINTS)

        # Prepare the optimization profiles
        self.profiles = []
        self.num_profiles = 1   # Can create more profiles here if needed
        if self.dla_core is None:
            for i in range(self.num_profiles):
                profile = self.builder.create_optimization_profile()
                for input_idx in range(self.network.num_inputs):
                    input_shape = self.network.get_input(input_idx).shape
                    input_name = self.network.get_input(input_idx).name
                    min_shape = trt.Dims(input_shape)
                    min_shape[0] = 1
                    max_shape = trt.Dims(input_shape)
                    max_shape[0] = self.batch_size
                    profile.set_shape(input_name, min_shape, max_shape, max_shape)
                if not profile:
                    raise RuntimeError("Invalid optimization profile!")
                self.builder_config.add_optimization_profile(profile)
                self.profiles.append(profile)
        else:
            # Use fixed batch size if on DLA
            for input_idx in range(self.network.num_inputs):
                input_shape = self.network.get_input(input_idx).shape
                input_shape[0] = self.batch_size
                self.network.get_input(input_idx).shape = input_shape

        engine = self.builder.build_engine(self.network, self.builder_config)
        engine_inspector = engine.create_engine_inspector()
        layer_info = engine_inspector.get_engine_information(trt.LayerInformationFormat.ONELINE)
        logging.info("========= TensorRT Engine Layer Information =========")
        logging.info(layer_info)

        buf = engine.serialize()
        logging.info(f"Writing built engine to {self.engine_file}")
        with open(self.engine_file, 'wb') as f:
            f.write(buf)

    def run_openimage(self, num_samples=8):
        cocoGt = COCO(annotation_file=self.val_annotate)
        image_ids = cocoGt.getImgIds()
        cat_ids = cocoGt.getCatIds()
        num_images = min(num_samples, len(image_ids))
        print(f"Total number of images: {len(image_ids)}, number of categories: {len(cat_ids)}, running num_images: {num_images}")

        detections = []
        batch_idx = 0
        for image_idx in range(0, num_images, self.batch_size):
            # Print Progress
            if batch_idx % 20 == 0:
                print(f"Processing batch: {batch_idx} image: {image_idx}/{num_images}")

            end_idx = min(image_idx + self.batch_size, num_images)
            imgs = []
            img_original_sizes = []
            for idx in range(image_idx, end_idx):
                image_id = image_ids[idx]
                if self.precision == "fp32":
                    # Load the image using pytorch routine, but perform extra resize+normalize steps
                    img = load_img_pytorch(os.path.join(self.image_dir, cocoGt.imgs[image_id]["file_name"]), do_transform=True).numpy()
                elif self.precision == "int8":
                    img = np.load(os.path.join(G_OPENIMAGE_PREPROCESSED_INT8_PATH, cocoGt.imgs[image_id]["file_name"] + '.npy'))
                else:
                    raise Exception(f"Unsupported precision {self.precision}")
                imgs.append(img)
                img_original_sizes.append([cocoGt.imgs[image_id]["height"], cocoGt.imgs[image_id]["width"]])

            if self.precision == "fp32":
                imgs = np.ascontiguousarray(np.stack(imgs), dtype=np.float32)
            elif self.precision == "int8":
                imgs = np.stack(imgs)

            start_time = time.time()
            outputs = self.runner([imgs], batch_size=self.batch_size)

            if self.verbose:
                duration = time.time() - start_time
                logging.info(f"Batch {batch_idx} >>> Inference time:  {duration}")

            # Concatted outputs is in the shape of [BS, 7001]
            # image_ids (duplicate of score for loadgen): [BS, 1000, 1]
            # loc: [BS, 1000, 4]
            # score: [BS, 1000, 1]
            # label: [BS, 1000, 1]
            # Concatted into [BS, 1000, 7] then reshape to [BS, 7000]
            # keep_count: [BS, 1]
            concat_output = outputs[0]

            for idx in range(0, end_idx - image_idx):
                # keep_count = keep_counts[idx]
                keep_count = int(concat_output[idx * 7001 + 7000])
                image_height = img_original_sizes[idx][0]
                image_width = img_original_sizes[idx][1]

                for prediction_idx in range(0, keep_count):
                    # Each detection is in the order of [dummy_image_idx, xmin, ymin, xmax, ymax, score, label]
                    # This is pre-callback (otherwise x and y are swapped).
                    single_detection = concat_output[idx * 7001 + prediction_idx * 7: idx * 7001 + prediction_idx * 7 + 7]
                    loc = single_detection[1:5]
                    label = single_detection[6]
                    score = single_detection[5]

                    # Scale the image output from [0, 1] to (img_h, img_w)
                    # [ymin, xmin, ymax, xmax]
                    scale_h = image_height
                    scale_w = image_width
                    loc[0::2] = loc[0::2] * scale_h
                    loc[1::2] = loc[1::2] * scale_w
                    loc = loc.tolist()

                    # Convert from ltrb_xyinverted to [xmin, ymin, w, h]
                    bbox_coco_fmt = [
                        loc[1],
                        loc[0],
                        loc[3] - loc[1],
                        loc[2] - loc[0],
                    ]

                    coco_detection = {
                        "image_id": image_ids[image_idx + idx],
                        "category_id": cat_ids[int(label)],
                        "bbox": bbox_coco_fmt,
                        "score": float(score),
                    }
                    detections.append(coco_detection)
            batch_idx += 1

        output_dir = os.path.dirname(self.output_file)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        with open(self.output_file, "w") as f:
            json.dump(detections, f)
        cocoDt = cocoGt.loadRes(self.output_file)
        e = COCOeval(cocoGt, cocoDt, 'bbox')
        e.params.imgIds = image_ids[:num_images]
        e.evaluate()
        e.accumulate()
        e.summarize()
        map_score = e.stats[0]
        return map_score


class PytorchTester:
    """
    The reference implementation of the retinanet from the mlcommon-training repo, from:
    https://github.com/mlcommons/training/tree/master/single_stage_detector/ssd/model

    To run this tester, you would need to clone the repo, and mount it to the container.
    """

    def __init__(self, pyt_ckpt_path, training_repo_path, batch_size=8, output_file="build/retinanet_pytorch.out"):
        ssd_model_path = os.path.join(training_repo_path, "single_stage_detector", "ssd")
        with ScopedRestrictedImport([ssd_model_path] + sys.path):
            from model.retinanet import retinanet_from_backbone
            pyt_model = retinanet_from_backbone(
                backbone="resnext50_32x4d",
                num_classes=G_RETINANET_NUM_CLASSES,
                image_size=[800, 800],
                data_layout="channels_last",
                pretrained=None,
                trainable_backbone_layers=3
            )

        self.training_repo_path = training_repo_path
        self.device = torch.device("cuda:0")
        pyt_model.to(self.device)
        if pyt_model.data_layout == "channels_last":
            pyt_model = pyt_model.to(memory_format=torch.channels_last)
        cpt = torch.load(pyt_ckpt_path, map_location='cpu')
        pyt_model.load_state_dict(cpt["model"])
        self.pyt_model = pyt_model
        self.val_annotate = G_OPENIMAGE_ANNO_PATH
        self.batch_size = batch_size
        self.output_file = output_file
        self.image_dir = G_OPENIMAGE_VALSET_PATH

    def run_openimage(self, num_samples=8):
        """
        Use openimage raw input to run the pytorch referene model for <num_samples> images.
        Note that the input image will be of different sizes, and the output bboxes are not normalized to 800,800
        The pytorch model handles the resize and postprocess internally. For more details, see:
        https://github.com/mlcommons/training/blob/master/single_stage_detector/ssd/model/retinanet.py#L475
        """
        self.pyt_model.eval()
        cocoGt = COCO(annotation_file=self.val_annotate)
        image_ids = cocoGt.getImgIds()
        cat_ids = cocoGt.getCatIds()
        num_images = min(num_samples, len(image_ids))
        print(f"Total number of images: {len(image_ids)}, number of categories: {len(cat_ids)}, running num_images: {num_images}")

        coco_detections = []
        for image_idx in range(0, num_images, self.batch_size):
            end_idx = min(image_idx + self.batch_size, num_images)
            # Load image and transfer to tensor (original image size)
            imgs = []
            for idx in range(image_idx, end_idx):
                image_id = image_ids[idx]
                image_path = os.path.join(self.image_dir, cocoGt.imgs[image_id]["file_name"])
                img = load_img_pytorch(image_path).to(self.device)
                imgs.append(img)
                # print(cocoGt.imgs[image_id]["height"], cocoGt.imgs[image_id]["width"])

            img = []
            for idx in range(image_idx, end_idx):
                image_id = image_ids[idx]
                tensor = load_img_pytorch(os.path.join(self.image_dir, cocoGt.imgs[image_id]["file_name"]), do_transform=True).numpy()
                print(tensor.shape)
                img.append(tensor)
            img = np.ascontiguousarray(np.stack(img), dtype=np.float32)

            start_time = time.time()
            with torch.no_grad():
                detections = self.pyt_model(imgs)

            for idx in range(0, end_idx - image_idx):
                boxes = detections[idx]["boxes"].detach().cpu().numpy()
                scores = detections[idx]["scores"].detach().cpu().numpy()
                labels = detections[idx]["labels"].detach().cpu().numpy()

                num_preds = boxes.shape[0]
                for pred_idx in range(num_preds):
                    # Convert from lrtb to [xmin, ymin, w, h] for cocoeval
                    box_pred = boxes[pred_idx][:]
                    xmin, ymin, xmax, ymax = box_pred
                    box_pred = np.array([xmin, ymin, xmax - xmin, ymax - ymin], dtype=np.float32)
                    score_pred = float(scores[pred_idx])
                    label_pred = int(labels[pred_idx])
                    coco_detection = {
                        "image_id": image_ids[image_idx + idx],
                        "category_id": cat_ids[label_pred],
                        "bbox": box_pred.tolist(),  # Convert ndarray to list
                        "score": score_pred
                    }
                    coco_detections.append(coco_detection)

        output_dir = os.path.dirname(self.output_file)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        with open(self.output_file, "w") as f:
            json.dump(coco_detections, f)
        cocoDt = cocoGt.loadRes(self.output_file)
        e = COCOeval(cocoGt, cocoDt, 'bbox')
        e.params.imgIds = image_ids[:num_images]
        e.evaluate()
        e.accumulate()
        e.summarize()
        map_score = e.stats[0]

        # Uncomment below to call reference implementation evaluate.
        # Import extra helper function from training repo.
        # ssd_model_path = os.path.join(self.training_repo_path, "single_stage_detector", "ssd")
        # with ScopedRestrictedImport([ssd_model_path] + sys.path):
        #     from coco_utils import get_openimages
        #     import presets
        #     from utils import collate_fn
        #     from engine import evaluate
        #     from coco_utils import get_coco_api_from_dataset
        #     from coco_eval import DefaultCocoEvaluator
        # coco_evaluator = evaluate(self.pyt_model, data_loader_test, device=self.device, epoch=None, args=Args)
        # map_score = coco_evaluator.get_stats()['bbox'][0]
        return map_score


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--engine_file",
                        help="Specify where the retinanet engine file is",
                        required=False)
    parser.add_argument("--onnx_path",
                        help="The path to the onnx, if building from onnx",
                        default="build/models/retinanet-resnext50-32x4d/submission/retinanet_resnext50_32x4d_efficientNMS.800x800.onnx",
                        required=False)
    parser.add_argument("--pyt_ckpt_path",
                        help="Specify where the PyTorch checkpoint file is",
                        default="build/models/retinanet-resnext50-32x4d/new/retinanet_model_10.pth")
    parser.add_argument("--training_repo_path",
                        help="Specify where the MLCommons training directory is (from https://github.com/mlcommons/training)",
                        default="/home/scratch.zhihanj_sw/gitlab_root/mlcommons-training"
                        )
    parser.add_argument("--batch_size",
                        help="batch size",
                        type=int,
                        default=8)
    parser.add_argument("--num_samples",
                        help="Number of samples to run. We have 24781 in total for openImages",
                        type=int,
                        default=24781)
    parser.add_argument("--trt_precision",
                        help="Run TensorRT in the specified precision",
                        choices=("fp32", "fp16", "int8"),
                        default="fp32")
    parser.add_argument("--skip_engine_build",
                        help="Skip the TRT engine build phase if possible.",
                        action="store_true")
    parser.add_argument("--pytorch",
                        help="whether to run pytorch inference",
                        action="store_true")
    parser.add_argument("--verbose",
                        help="verbose output",
                        action="store_true")
    args = parser.parse_args()

    # Pytorch Tester
    if args.pytorch:
        # TODO: Check existence of training repo.
        logging.info(f"Running Accuracy test for Pytorch reference implementation.")
        if args.training_repo_path is None or not os.path.exists(args.training_repo_path):
            raise RuntimeError("Please pull mlcommon training repo from https://github.com/mlcommons/training, and specify with --training_repo_path")
        pt_tester = PytorchTester(args.pyt_ckpt_path, args.training_repo_path, args.batch_size)
        pt_acc = pt_tester.run_openimage(args.num_samples)
        logging.info(f"Pytorch mAP Score: {pt_acc}, Reference: 0.375, % of ref: {pt_acc / 0.375}")
    else:
        # TRT Tester
        logging.info(f"Running accuracy test for retinanet using {args.engine_file} ...")
        tester = TRTTester(args.engine_file, args.batch_size, args.trt_precision, args.onnx_path, args.skip_engine_build, args.verbose)
        # acc = tester.run_openimage(args.num_samples)
        acc = tester.run_openimage(args.num_samples)
        logging.info(f"mAP Score: {acc}, Reference: 0.375, % of ref: {acc / 0.375}")

    # To run the TRT tester:
    # python3 -m code.retinanet.tensorrt.infer --engine_file /tmp/retina.b8.int8.engine --num_samples=1200 --batch_size=8 --trt_precision int8
    # To run the pytorch tester:
    # python3 -m code.retinanet.tensorrt.infer --pytorch --num_samples=1200 --batch_size=8


if __name__ == "__main__":
    main()
