#!/bin/bash

CPUS_PER_INSTANCE=8
number_threads=`nproc --all`
export number_cores=`lscpu -b -p=Core,Socket | grep -v '^#' | sort -u | wc -l`
number_sockets=`grep physical.id /proc/cpuinfo | sort -u | wc -l`
cpu_per_socket=$((number_cores/number_sockets))
number_instance=$((number_cores/CPUS_PER_INSTANCE))

WORKERS_PER_PROC=${WORKERS_PER_PROC:-4}
THREADS_PER_INSTANCE=$((( ${WORKERS_PER_PROC} * ${CM_HOST_CPU_THREADS_PER_CORE}) / ${CM_HOST_CPU_SOCKETS}))

export LD_PRELOAD=${CONDA_PREFIX}/lib/libjemalloc.so
export LD_PRELOAD=${CONDA_PREFIX}/lib/libiomp5.so
export MALLOC_CONF="oversize_threshold:1,background_thread:true,metadata_thp:auto,dirty_decay_ms:9000000000,muzzy_decay_ms:9000000000";

KMP_SETTING="KMP_AFFINITY=granularity=fine,compact,1,0"
export KMP_BLOCKTIME=1
export $KMP_SETTING


export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${CONDA_PREFIX}/lib

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
CONFIG="  --scenario ${scenario} --mode ${LOADGEN_MODE} --model_name retinanet \
	--model_path ${MODEL_PATH} \
	--data_path ${DATA_DIR} \
    --mlperf_conf ${CM_MLPERF_CONF} --user_conf ${CM_MLPERF_USER_CONF} \
	--cpus_per_instance $CPUS_PER_INSTANCE \
    --num_instance $number_instance \
	--total_sample_count 24781 \
	--batch_size 1
	"

cmd=" ${executable} ${CONFIG}"
echo "$cmd"
eval "$cmd"
test "$?" -eq 0 || exit "$?"
