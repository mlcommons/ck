#!/bin/bash

if [[ ! -e ${CM_NVIDIA_MLPERF_SCRATCH_PATH}/models/GPTJ-6B/checkpoint-final ]]; then
  mkdir -p ${CM_NVIDIA_MLPERF_SCRATCH_PATH}/models/GPTJ-6B/
  cp -r ${GPTJ_CHECKPOINT_PATH} ${CM_NVIDIA_MLPERF_SCRATCH_PATH}/models/GPTJ-6B/checkpoint-final
  test $? -eq 0 || exit $?
fi

echo "cd ${CM_TENSORRT_LLM_CHECKOUT_PATH}"
cd ${CM_TENSORRT_LLM_CHECKOUT_PATH}

make -C docker build
test $? -eq 0 || exit $?

export RUN_CMD="bash -c 'python3 scripts/build_wheel.py -a=${CM_GPU_ARCH} --clean --install --trt_root /usr/local/tensorrt/ && python examples/quantization/quantize.py --dtype=float16  --output_dir=/mnt/models/GPTJ-6B/fp8-quantized-ammo/GPTJ-FP8-quantized --model_dir=/mnt/models/GPTJ-6B/checkpoint-final --qformat=fp8 --kv_cache_dtype=fp8 '"
export DOCKER_RUN_ARGS=" -v ${CM_NVIDIA_MLPERF_SCRATCH_PATH}:/mnt"
make -C docker run LOCAL_USER=1
test $? -eq 0 || exit $?

${CM_PYTHON_BIN_WITH_PATH} ${CM_MLPERF_INFERENCE_NVIDIA_CODE_PATH}/code/gptj/tensorrt/onnx_tune.py --fp8-scalers-path=${CM_NVIDIA_MLPERF_SCRATCH_PATH}/models/GPTJ-6B/fp8-quantized-ammo/GPTJ-FP8-quantized/rank0.safetensors --scaler 1.005 --index 15
test $? -eq 0 || exit $?
