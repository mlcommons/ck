## About
This is a modularized C++ implementation of an MLPerf Inference SUT. Each file corresponds to a different class that can be changed independently of other ones:
1. `Backend` runs the actual inference using a framework (ONNX Runtime, TF Lite, etc)
2. `Device` manages devices and memory (CPU, GPU, etc)
3. `Model` is a struct representing a model file (ResNet50, etc)
4. `SampleLibrary` is a dataset loader (ImageNet, COCO, etc)
5. `System` is the SUT interface to LoadGen which manages how input queries are issued
   1. `QueueSUT` enqueues queries and dequeues them to each backend thread (ideal for all scenarios except single-stream)
   2. `StreamSUT` calls the backend thread directly upon query (ideal for single-stream)

## Test results
Under the same settings for ResNet50 on reduced ImageNet (Offline, 8 running threads, max batch size 32, Mac M1 CPU):
* Reference implementation (Python) 38.3336 samples/second
* This implementation (C++) 40.0359 samples/second
