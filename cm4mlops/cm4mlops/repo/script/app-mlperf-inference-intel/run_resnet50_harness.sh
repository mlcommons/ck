#!/bin/bash

CPUS_PER_INSTANCE=1
number_threads=`nproc --all`
export number_cores=`lscpu -b -p=Core,Socket | grep -v '^#' | sort -u | wc -l`
number_sockets=`grep physical.id /proc/cpuinfo | sort -u | wc -l`
cpu_per_socket=$((number_cores/number_sockets))

WORKERS_PER_PROC=${WORKERS_PER_PROC:-4}
THREADS_PER_INSTANCE=$((( ${WORKERS_PER_PROC} * ${CM_HOST_CPU_THREADS_PER_CORE}) / ${CM_HOST_CPU_SOCKETS}))

export LD_PRELOAD=${CONDA_PREFIX}/lib/libjemalloc.so
export LD_PRELOAD=${CONDA_PREFIX}/lib/libiomp5.so
export MALLOC_CONF="oversize_threshold:1,background_thread:true,metadata_thp:auto,dirty_decay_ms:9000000000,muzzy_decay_ms:9000000000";

KMP_SETTING="KMP_AFFINITY=granularity=fine,compact,1,0"
export KMP_BLOCKTIME=1
export $KMP_SETTING


export DATA_DIR=${CM_HARNESS_CODE_ROOT}/ILSVRC2012_img_val
export RN50_START=${CM_HARNESS_CODE_ROOT}/models/resnet50-start-int8-model.pth
export RN50_END=${CM_HARNESS_CODE_ROOT}/models/resnet50-end-int8-model.pth
export RN50_FULL=${CM_HARNESS_CODE_ROOT}/models/resnet50-full.pth

export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${CONDA_PREFIX}/lib

rsync -avz  ${CM_HARNESS_CODE_ROOT}/val_data/ ${DATA_DIR}/
executable="${CM_HARNESS_CODE_ROOT}/build/bin/mlperf_runner"

number_threads=`nproc --all`
export number_cores=`lscpu -b -p=Core,Socket | grep -v '^#' | sort -u | wc -l`
num_numa=$(numactl --hardware|grep available|awk -F' ' '{ print $2 }')
num_instance=$(($number_cores / $THREADS_PER_INSTANCE))

scenario=${CM_MLPERF_LOADGEN_SCENARIO}
OUTDIR="${CM_MLPERF_OUTPUT_DIR}"
scenario="Offline"
#python ../../user_config.py

#--warmup_iters 20 \
CONFIG="  --scenario ${scenario} --mode ${LOADGEN_MODE} --model_name resnet50 \
	--rn50-part1 ${RN50_START} --rn50-part3 ${RN50_END} --rn50-full-model ${RN50_FULL} \
	--data_path ${DATA_DIR} \
    --mlperf_conf ${CM_MLPERF_CONF} --user_conf ${CM_MLPERF_USER_CONF} \
	--cpus_per_instance $CPUS_PER_INSTANCE \
    --num_instance $number_cores \
	--total_sample_count 50000 \
	--batch_size 256
	"

cmd=" ${executable} ${CONFIG}"
echo "$cmd"
eval "$cmd"
test "$?" -eq 0 || exit "$?"
