#!/bin/bash

nvidia_code_path=${CM_MLPERF_INFERENCE_NVIDIA_CODE_PATH}
cd ${nvidia_code_path}
scenarios=${CM_TMP_LOADGEN_SCENARIOS}
#batchsize=$
python3 code/main.py --action generate_engines --benchmarks resnet50 --scenarios $scenarios --gpu_batch_size=256 --gpu_copy_streams=1 --workspace_size=4194304
