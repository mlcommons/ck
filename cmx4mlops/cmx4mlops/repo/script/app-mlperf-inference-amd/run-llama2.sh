#!/bin/bash

set -xeu

N_SAMPLES=${N_SAMPLES:-24576} #24576 #3072 #2457 #6
TP=1
DP=${DP:-8}

export HIP_FORCE_DEV_KERNARG=1
export VLLM_USE_TRITON_FLASH_ATTN=0
export VLLM_FP8_PADDING=1
export VLLM_FP8_ACT_PADDING=1
export VLLM_FP8_WEIGHT_PADDING=1
export VLLM_FP8_REDUCE_CONV=1

export HARNESS_DISABLE_VLLM_LOGS=1
export VLLM_LOGGING_LEVEL=ERROR

MODEL_PATH=${LLAMA2_CHECKPOINT_PATH:-/data/llm/llama2-70b-chat/}
DATASET_PATH=${CM_DATASET_OPENORCA_PREPROCESSED_PATH:-/data/open_orca/open_orca_gpt4_tokenized_llama.sampled_24576.pkl.gz}
QUANTIZED_WEIGHTS_PATH=${CM_LLAMA2_FINAL_SAFE_TENSORS_PATH:-quantized/quark_share/modelzoo/llama2_70b_wfp8_afp8_ofp8_nomerge/json-safetensors/llama.safetensors}
QUANTIZATION_PARAM_PATH=${QUANTIZATION_PARAM_PATH:-/app/kv_cache_scales.json}

MLPERF_CONF="${CM_MLPERF_CONF:-/app/mlperf_inference/mlperf.conf}"
USER_CONF="${CM_MLPERF_USER_CONF:-/lab-mlperf-inference/code/llama2-70b-99.9/mlperf_config_VllmFp8/user.conf}"

SUBMISSION=${SUBMISSION:-0}

LOG_DIR=${CM_MLPERF_OUTPUT_DIR}

cp $USER_CONF ${LOG_DIR}/user.conf

COMMON_CMD_OPTIONS="\
    --scenario ${CM_MLPERF_LOADGEN_SCENARIO} \
    --output-log-dir ${LOG_DIR} \
    --model-path $MODEL_PATH \
    --mlperf-conf $MLPERF_CONF \
    --user-conf $USER_CONF \
    --total-sample-count $N_SAMPLES \
    --dataset-path $DATASET_PATH \
    --dtype float16 \
    --backend vllm \
    --device cuda:0 \
    --kv-cache-dtype fp8 \
    -tp ${TP} \
    -dp ${DP} \
    --quantization fp8 \
    --quantized-weights-path ${QUANTIZED_WEIGHTS_PATH} \
    --quantization-param-path ${QUANTIZATION_PARAM_PATH}"

if [ "${CM_MLPERF_LOADGEN_MODE}" == "accuracy" ]; then
    COMMON_CMD_OPTIONS+=" --accuracy"
fi

if [ "${CM_MLPERF_LOADGEN_SCENARIO}" == "Offline" ]; then
    WD=${WD:-0}
    SORTING=${SORTING:-descending} #ascending #descending #lexicographic #skip
    export VLLM_SCHED_PREFILL_KVC_FREEPCT=31.0
    # generate run command
    cmd="${CM_PYTHON_BIN_WITH_PATH} ${CM_MLPERF_AMD_LLAMA2_CODE_PATH}/mainVllmFp8_Offline.py \
    ${COMMON_CMD_OPTIONS} \
    --warmup-duration ${WD} \
    --sorting ${SORTING} \
    --enforce-eager True \
    --gpu-memory-utilization 0.99" 
else
    # generate run command
    cmd="${CM_PYTHON_BIN_WITH_PATH} ${CM_MLPERF_AMD_LLAMA2_CODE_PATH}/mainVllmFp8_SyncServer.py \
    ${COMMON_CMD_OPTIONS} \
    --enable-warm-up \
    --enable-batcher"
fi

echo "${cmd}"
# uncomment the below lines for testing 
#eval "${cmd}"
