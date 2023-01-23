# Copyright (c) 2022, NVIDIA CORPORATION. All rights reserved.
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

import torch
import onnx
import argparse
import json
import re

import onnx_graphsurgeon as gs
import numpy as np
import os


# in_onnx = "/work/code/retinanet/tensorrt/onnx_retina/ref_fpn_transreshapeconcat.onnx"
in_onnx = os.environ.get("CM_ML_MODEL_DYN_BATCHSIZE_PATH", "build/models/retinanet-resnext50-32x4d/new/retinanet_resnext50_32x4d_fpn.opset11.dyn_bs.800x800.onnx")
out_onnx = os.environ.get("CM_NVIDIA_MODEL_PATCHED_PATH", "/work/code/retinanet/tensorrt/onnx_generator/test_fpn_efficientnms_concatall.onnx")
# Anchor at [1, 1]
anchor_xywh_1x1_npy = os.environ.get("CM_ML_MODEL_ANCHOR_PATH", "/work/code/retinanet/tensorrt/onnx_generator/retinanet_anchor_xywh_1x1.npy")

graph = gs.import_onnx(onnx.load(in_onnx))

op = 'EfficientNMS_TRT'
node_name = 'efficientNMS'

# (PluginField("score_threshold", nullptr, PluginFieldType::kFLOAT32, 1));
# (PluginField("iou_threshold", nullptr, PluginFieldType::kFLOAT32, 1));
# (PluginField("max_output_boxes", nullptr, PluginFieldType::kINT32, 1));
# (PluginField("background_class", nullptr, PluginFieldType::kINT32, 1));
# (PluginField("score_activation", nullptr, PluginFieldType::kINT32, 1));
# (PluginField("box_coding", nullptr, PluginFieldType::kINT32, 1));

node_attrs = { 
    "background_class": -1,
    "score_threshold" : 0.05,
    "iou_threshold" :  0.5,
    "max_output_boxes" :  1000,
    "score_activation" :  True,
    "box_coding" :  1,
}
attrs = {
    "plugin_version": "1",
    "plugin_namespace": "",
}
attrs.update(node_attrs)

anchors = np.load(anchor_xywh_1x1_npy)
print(f"anchors shape: {anchors.shape}, top 4: {anchors[0, :]}")
anchors = np.expand_dims(anchors, axis=0)
print(f"anchors shape: {anchors.shape}")

anchor_tensor = gs.Constant(name="anchor", values=anchors)

tensors = graph.tensors()

# Add EfficientNMS layer
# output tensors
num_detections = gs.Variable(name="num_detections",
                                 dtype=np.int32,
                                 shape=["batch_size", 1])
detection_boxes = gs.Variable(name="detection_boxes",
                                  dtype=np.float32,
                                  shape=["batch_size", 1000, 4])
detection_scores = gs.Variable(name="detection_scores",
                                   dtype=np.float32,
                                   shape=["batch_size", 1000])
detection_classes = gs.Variable(name="detection_classes",
                                    dtype=np.int32,
                                    shape=["batch_size", 1000])

nms_inputs = [tensors["bbox_regression"], tensors["cls_logits"], anchor_tensor]
nms_outputs = [num_detections, detection_boxes, detection_scores, detection_classes]

graph.layer(op="EfficientNMS_TRT",
            name="EfficientNMS",
            inputs=nms_inputs,
            outputs=nms_outputs,
            attrs=attrs)

# Add Concat plugin to concat all 4 tensors
concat_final_output = gs.Variable(name="concat_final_output",
                                  dtype=np.float32,
                                  shape=["batch_size", 7001])
attrs = {
    "plugin_version": "1",
    "plugin_namespace": "",
}
graph.layer(op="RetinanetConcatNmsOutputsPlugin",
            name="RetinanetConcatNmsOutputsPlugin",
            inputs=[num_detections, detection_boxes, detection_scores, detection_classes],
            outputs=[concat_final_output],
            attrs=attrs)

graph.outputs = [concat_final_output]

graph.cleanup().toposort()

onnx.save_model(gs.export_onnx(graph), out_onnx)
