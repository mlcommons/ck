#!/bin/bash

echo "Set tp size is ${CM_NVIDIA_TP_SIZE}"

if [[ ! -e ${CM_NVIDIA_MLPERF_SCRATCH_PATH}/models/Llama2/Llama-2-70b-chat-hf ]]; then
  mkdir -p ${CM_NVIDIA_MLPERF_SCRATCH_PATH}/models/Llama2/Llama-2-70b-chat-hf
  cd ${LLAMA2_CHECKPOINT_PATH}
  cp -r ${LLAMA2_CHECKPOINT_PATH}/* ${CM_NVIDIA_MLPERF_SCRATCH_PATH}/models/Llama2/Llama-2-70b-chat-hf
  test $? -eq 0 || exit $?
fi

echo "cd ${CM_TENSORRT_LLM_CHECKOUT_PATH}"
cd ${CM_TENSORRT_LLM_CHECKOUT_PATH}

make -C docker build
test $? -eq 0 || exit $?

if [ "${CM_NVIDIA_TP_SIZE}" -eq 1 ]; then
  RUN_CMD="bash -c 'python3 scripts/build_wheel.py -a=${CM_GPU_ARCH} --clean --install --trt_root /usr/local/tensorrt/ && python examples/quantization/quantize.py --dtype=float16  --output_dir=/mnt/models/Llama2/fp8-quantized-ammo/llama2-70b-chat-hf-tp${CM_NVIDIA_TP_SIZE}pp1-fp8-02072024 --model_dir=/mnt/models/Llama2/Llama-2-70b-chat-hf --qformat=fp8 --kv_cache_dtype=fp8 --tp_size ${CM_NVIDIA_TP_SIZE}'"
else
  RUN_CMD="bash -c 'python3 scripts/build_wheel.py -a=${CM_GPU_ARCH} --clean --install --trt_root /usr/local/tensorrt/ && python examples/quantization/quantize.py --dtype=float16  --output_dir=/mnt/models/Llama2/fp8-quantized-ammo/llama2-70b-chat-hf-tp${CM_NVIDIA_TP_SIZE}pp1-fp8 --model_dir=/mnt/models/Llama2/Llama-2-70b-chat-hf --qformat=fp8 --kv_cache_dtype=fp8 --tp_size ${CM_NVIDIA_TP_SIZE}'"
fi
DOCKER_RUN_ARGS=" -v ${CM_NVIDIA_MLPERF_SCRATCH_PATH}:/mnt"
export DOCKER_RUN_ARGS="$DOCKER_RUN_ARGS"
export RUN_CMD="$RUN_CMD"
make -C docker run LOCAL_USER=1
test $? -eq 0 || exit $?

echo "MLPerf Nvidia scratch path is:${CM_NVIDIA_MLPERF_SCRATCH_PATH}"
