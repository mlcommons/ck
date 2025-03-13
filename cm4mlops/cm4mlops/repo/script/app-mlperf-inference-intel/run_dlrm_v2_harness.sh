#!/bin/bash
export MODEL_DIR=${CM_ML_MODEL_FILE_WITH_PATH}
export DATA_DIR=/mnt/dlrm_data


NUM_SOCKETS=${CM_HOST_CPU_SOCKETS:-2}
export NUM_SOCKETS=$NUM_SOCKETS
export num_physical_cores=`lscpu -b -p=Core,Socket | grep -v '^#' | sort -u | wc -l`
export CPUS_PER_SOCKET=$((num_physical_cores/NUM_SOCKETS))
echo $CPUS_PER_SOCKET
export CPUS_PER_PROCESS=24
#${CPUS_PER_SOCKET}
export CPUS_PER_INSTANCE=1
export CPUS_FOR_LOADGEN=1
export BATCH_SIZE=100
export DNNL_MAX_CPU_ISA=AVX512_CORE_AMX

export LD_PRELOAD=${CM_CONDA_LIB_PATH}/libiomp5.so

export KMP_BLOCKTIME=1
export OMP_NUM_THREADS=$CPUS_PER_INSTANCE
export KMP_AFFINITY="granularity=fine,compact,1,0"
export DNNL_PRIMITIVE_CACHE_CAPACITY=20971520
export DLRM_DIR=$PWD/python/model
#export TCMALLOC_LARGE_ALLOC_REPORT_THRESHOLD=30469645312

mode="Offline"
extra_option="--samples-per-query-offline=204800"

int8_cfg="--int8-configure-dir=int8_configure.json"
echo "Running $mode bs=$batch_size $dtype $test_type $DNNL_MAX_CPU_ISA"

export CUDA_VISIBLE_DEVICES=""
extra_option=" $extra_option --use-int8"
export EXTRA_OPS="$extra_option"

#export number_cores=`lscpu -b -p=Core,Socket | grep -v '^#' | sort -u | wc -l`

model_path="$MODEL_DIR/dlrm-multihot-pytorch.pt"
profile=dlrm-multihot-pytorch
cd ${CM_HARNESS_CODE_ROOT}
OUTPUT_DIR="${CM_MLPERF_OUTPUT_DIR}"

if [[ "${CM_MLPERF_LOADGEN_MODE}" == "accuracy" ]]; then
  accuracy_opt=" --accuracy"
else
  accuracy_opt=""
fi

USER_CONF="${CM_MLPERF_USER_CONF}"
cmd="python -u python/runner.py --profile $profile $common_opt --model dlrm --model-path $model_path \
--config ${CM_MLPERF_CONF} --user-config ${CM_MLPERF_USER_CONF} \
--dataset multihot-criteo --dataset-path $DATA_DIR --output $OUTPUT_DIR $EXTRA_OPS \
--max-ind-range=40000000 --samples-to-aggregate-quantile-file=${PWD}/tools/dist_quantile.txt \
--max-batchsize=$BATCH_SIZE --scenario=${CM_MLPERF_LOADGEN_SCENARIO} ${accuracy_opt}"


echo "$cmd"
#exit 1
eval "$cmd"
