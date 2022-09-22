## About
This is a modularized C++ implementation of an MLPerf Inference SUT. Each file corresponds to a different class that can be changed independently of other ones:
1. `Backend` runs the actual inference using a framework (ONNX Runtime, TF Lite, etc)
2. `Device` manages devices and memory (CPU, GPU, etc)
3. `Model` is a struct representing a model file (ResNet50, etc)
4. `SampleLibrary` is a dataset loader (ImageNet, COCO, etc)
5. `System` is the SUT interface to LoadGen which manages how input queries are issued
   1. `QueueSUT` enqueues queries and dequeues them to each backend thread (ideal for all scenarios except single-stream)
   2. `StreamSUT` calls the backend thread directly upon query (ideal for single-stream)

## Building the `main.cpp` demo
1. Build and install ONNX Runtime and MLCommons LoadGen
2. Edit flags near the top of the `main.cpp` file
3. Build command:
```sh
gcc++ -O3 -std=c++14 -I/path/to/loadgen/include -L/path/to/loadgen/lib -I/path/to/onnxruntime/include -L/path/to/onnxruntime/lib -lmlperf_loadgen -lonnxruntime -o main main.cpp
```
4. Run with `./main` and the outputs will be in `OUTPUT_DIR` set in `main.cpp` (default `./output`).

## Test results
Under the same settings for ResNet50 on reduced ImageNet (Offline, 8 running threads, max batch size 32, Mac M1 CPU):
* Reference implementation (Python) 38.3336 samples/second
* This implementation (C++) 40.0359 samples/second
