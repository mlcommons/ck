**[ [TOC](../README.md) ]**

```
import tensorflow as tf

graph_def_file = "resnet50_v1.pb"
input_arrays = ["input_tensor"]
output_arrays = ["softmax_tensor"]

converter = tf.contrib.lite.TFLiteConverter.from_frozen_graph(
  graph_def_file, input_arrays, output_arrays)
tflite_model = converter.convert()
open("resnet50_v1.tflite", "wb").write(tflite_model)

```
