#!/bin/bash

export KMP_BLOCKTIME=1
export KMP_AFFINITY=granularity=fine,compact,1,0
export LD_PRELOAD=${LD_PRELOAD}:${CONDA_PREFIX}/lib/libiomp5.so
# export LD_PRELOAD=${LD_PRELOAD}:${CONDA_PREFIX}/lib/libtcmalloc.so
#

BATCH_SIZE=${CM_MLPERF_LOADGEN_BATCH_SIZE}

export num_physical_cores=$(lscpu -b -p=Core,Socket | grep -v '^#' | sort -u | wc -l)
num_numa=$(numactl --hardware|grep available|awk -F' ' '{ print $2 }')



OUTPUT_DIR="${CM_MLPERF_OUTPUT_DIR}"
MODEL_PATH="${SDXL_CHECKPOINT_PATH}"
cd ${CM_HARNESS_CODE_ROOT}

NUM_PROC=1
CPUS_PER_PROC=16
WORKERS_PER_PROC=1
TOTAL_SAMPLE_COUNT=5000
BATCH_SIZE=8

FD_MAX=$(ulimit -n -H)
ulimit -n $((FD_MAX - 1))

echo "Start time: $(date)"
cmd="python -u main.py \
    --dtype bfloat16 \
    --device 'cpu' \
    --scenario ${CM_MLPERF_LOADGEN_SCENARIO} \
    --mode ${LOADGEN_MODE} \
	--num-proc ${NUM_PROC} \
	--cpus-per-proc ${CPUS_PER_PROC} \
	--model-path ${MODEL_PATH} \
	--batch-size ${BATCH_SIZE} \
	--mlperf-conf ${CM_MLPERF_CONF} \
	--user-conf ${CM_MLPERF_USER_CONF} \
	--workers-per-proc ${WORKERS_PER_PROC} \
	--total-sample-count ${TOTAL_SAMPLE_COUNT} \
	--log-dir ${OUTPUT_DIR} "

echo "$cmd"
eval "$cmd"
test $? -eq 0 || exit $?
echo "End time: $(date)"

