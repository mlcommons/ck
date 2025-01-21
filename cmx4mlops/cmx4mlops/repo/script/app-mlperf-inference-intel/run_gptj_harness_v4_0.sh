#!/bin/bash
export PATH=${CM_CONDA_BIN_PATH}:$PATH

export KMP_BLOCKTIME=1
export KMP_AFFINITY=granularity=fine,compact,1,0
export LD_PRELOAD=${LD_PRELOAD}:${CONDA_PREFIX}/lib/libiomp5.so
# export LD_PRELOAD=${LD_PRELOAD}:${CONDA_PREFIX}/lib/libtcmalloc.so
#

BATCH_SIZE=${CM_MLPERF_LOADGEN_BATCH_SIZE}

DIR_SCRIPT=$(dirname "${BASH_SOURCE[0]}")
[ -z $DIR_NS ] && DIR_NS="$DIR_SCRIPT/gpt-j-env/neural-speed"
[ -z $VALIDATION_DATA_JSON ] && VALIDATION_DATA_JSON="$DIR_SCRIPT/gpt-j-env/cnn_dailymail_validation.json"
[ -z $CHECKPOINT_DIR ] && CHECKPOINT_DIR="$DIR_SCRIPT/gpt-j-env/finetuned_gptj"

# num_numa=$(numactl --hardware|grep available|awk -F' ' '{ print $2 }')

export num_physical_cores=$(lscpu -b -p=Core,Socket | grep -v '^#' | sort -u | wc -l)
IFS=', ' read -r -a available_nodes_list <<<"$(numactl -s | grep nodebind | sed -E 's/^nodebind: (.+)$/\1/')"
declare -p available_nodes_list
num_numa="${#available_nodes_list[@]}"
declare -p num_numa

find "$DIR_NS" -name CMakeCache.txt -exec rm {} \;
CMAKE_ARGS="-DNS_PROFILING=ON" pip install -e "$DIR_NS"

[ -z $NUM_PROC ] && NUM_PROC=$num_numa
CPUS_PER_PROC=$((num_physical_cores / num_numa))
[ -z $WORKERS_PER_PROC ] && WORKERS_PER_PROC=1
[ -z $CPUS_PER_WORKER ] && CPUS_PER_WORKER=                            # e.g. 8:8:8:8:8:8:8
[ -z $BATCH_PROC_ALLOC ] && BATCH_PROC_ALLOC=                          # e.g. 12:12:12:12:12:12:12
[ -z $LOGICAL_CORES_START ] && LOGICAL_CORES_START=-1                  # set to -1 to disable / or use $num_physical_cores
[ -z $CORES_OFFSET ] && CORES_OFFSET=0

[ -z $BATCH_SIZE ] && BATCH_SIZE=12
[ -z $BEAM_SIZE ] && BEAM_SIZE=4

OUTPUT_DIR="${CM_MLPERF_OUTPUT_DIR}"
MODEL_PATH="${CM_ML_MODEL_FILE_WITH_PATH}"
cd ${CM_HARNESS_CODE_ROOT}
export WORKLOAD_DATA=${CM_HARNESS_CODE_ROOT}/data
export VALIDATION_DATA_JSON=${WORKLOAD_DATA}/validation-data/cnn_dailymail_validation.json


for i in $(seq 0 $(($NUM_PROC - 1))); do
	[[ ! -e "${MODEL_PATH}${i}" ]] && ln -fs "$(basename $MODEL_PATH)" "${MODEL_PATH}${i}"
done

echo "Start time: $(date)"
cmd="python runner.py --workload-name gptj \
        --scenario ${CM_MLPERF_LOADGEN_SCENARIO} \
        --mode ${LOADGEN_MODE} \
	--num-proc ${NUM_PROC} \
	--cpus-per-proc ${CPUS_PER_PROC} \
	--dataset-path ${VALIDATION_DATA_JSON} \
	--model-path ${MODEL_PATH} \
	--model-checkpoint ${CHECKPOINT_DIR} \
	--batch-size ${BATCH_SIZE} \
	--beam-size ${BEAM_SIZE} \
	--mlperf-conf ${CM_MLPERF_CONF} \
	--user-conf ${CM_MLPERF_USER_CONF} \
	--workers-per-proc ${WORKERS_PER_PROC} \
	--total-sample-count ${TOTAL_SAMPLE_COUNT} \
	--output-dir ${OUTPUT_DIR} \
	--cores-offset ${CORES_OFFSET} \
	--logical-cores-start \"${LOGICAL_CORES_START}\" \
	--cpus-per-worker \"${CPUS_PER_WORKER}\" \
	--batch-proc-alloc \"${BATCH_PROC_ALLOC}\" \
	2>&1 | tee ${OUTPUT_DIR}.log"
echo "$cmd"
eval "$cmd"
test $? -eq 0 || exit $?
echo "End time: $(date)"

