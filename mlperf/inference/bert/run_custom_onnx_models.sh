#!/bin/bash

onnx_file_path=XX
custom_model_name=YY
precision=int8

cmd="cm run script --tags=run,mlperf,inference,run-mlperf,_find-performance  \
   --adr.python.version_min=3.8 \
   --adr.compiler.tags=gcc \
   --implementation=reference \
   --model=bert-99 \
   --precision=$precision \
   --backend=deepsparse \
   --device=cpu \
   --scenario=Offline \
   --test_query_count=15000 \
   --adr.mlperf-inference-implementation.max_batchsize=384 \
   --results_dir=$HOME/results_dir \
   --env.CM_MLPERF_CUSTOM_MODEL_PATH=$onnx_file_path \
   --env.CM_ML_MODEL_FULL_NAME=$custom_model_name \
   --quiet"
  echo ${cmd}
  eval ${cmd}

 cmd="cm run script --tags=run,mlperf,inference,run-mlperf,_submission  \
   --adr.python.version_min=3.8 \
   --adr.compiler.tags=gcc \
   --implementation=reference \
   --model=bert-99 \
   --precision=$precision \
   --backend=deepsparse \
   --device=cpu \
   --scenario=Offline \
   --mode=performance \
   --execution_mode=valid \
   --adr.mlperf-inference-implementation.max_batchsize=384 \
   --power=yes --adr.mlperf-power-client.power_server=192.168.0.15
   --results_dir=$HOME/results_dir \
   --env.CM_MLPERF_CUSTOM_MODEL_PATH=$onnx_file_path \
   --env.CM_ML_MODEL_FULL_NAME=$custom_model_name \
   --quiet"
  echo ${cmd}
  eval ${cmd}
