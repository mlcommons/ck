#!/bin/bash
zoo_stub_list=( \
"zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/pruned95_quant-none-vnni" \
"zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/14layer_pruned50_quant-none-vnni" \
"zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/base_quant-none" \
"zoo:nlp/question_answering/bert-base/pytorch/huggingface/squad/pruned95_obs_quant-none" \
"zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/base-none" \
"zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/14layer_pruned50-none-vnni" \
)

#the below ones are segfaulting
#"zoo:nlp/question_answering/oberta-base/pytorch/huggingface/squad/pruned90_quant-none" \
#"zoo:nlp/question_answering/roberta-base/pytorch/huggingface/squad/pruned85_quant-none" \

for stub in ${zoo_stub_list[@]}; do
cmd="cm run script --tags=run,mlperf,inference,run-mlperf,_find-performance  \
   --adr.python.version_min=3.8 \
   --adr.compiler.tags=gcc \
   --implementation=reference \
   --model=bert-99 \
   --precision=int8 \
   --backend=deepsparse \
   --device=cpu \
   --scenario=Offline \
   --test_query_count=15000 \
   --adr.mlperf-inference-implementation.max_batchsize=384 \
   --results_dir=$HOME/results_dir \
   --env.CM_MLPERF_NEURALMAGIC_MODEL_ZOO_STUB=$stub \
   --quiet"
  echo ${cmd}
  eval ${cmd}

 cmd="cm run script --tags=run,mlperf,inference,run-mlperf,_submission  \
   --adr.python.version_min=3.8 \
   --adr.compiler.tags=gcc \
   --implementation=reference \
   --model=bert-99 \
   --precision=int8 \
   --backend=deepsparse \
   --device=cpu \
   --scenario=Offline \
   --mode=performance \
   --execution_mode=valid \
   --adr.mlperf-inference-implementation.max_batchsize=384 \
   --power=yes --adr.mlperf-power-client.power_server=192.168.0.15 --adr.mlperf-power-client.port=4940 --env.CM_MLPERF_SKIP_POWER_CHECKS=yes \
   --results_dir=$HOME/results_dir \
   --env.CM_MLPERF_NEURALMAGIC_MODEL_ZOO_STUB=$stub \
   --quiet"
  echo ${cmd}
  eval ${cmd}
done
