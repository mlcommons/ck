#!/bin/bash

#not working
#"zoo:nlp/question_answering/oberta-base/pytorch/huggingface/squad/pruned90_quant-none" \
#"zoo:nlp/question_answering/roberta-base/pytorch/huggingface/squad/pruned85_quant-none" \
#zoo:nlp/question_answering/oberta-base/pytorch/huggingface/squad/pruned90-none \
#zoo:nlp/question_answering/roberta-base/pytorch/huggingface/squad/base_quant-none \
#"zoo:nlp/question_answering/roberta-base/pytorch/huggingface/squad/pruned85-none" \
#"zoo:nlp/question_answering/oberta-base/pytorch/huggingface/squad/base_quant-none" \
#"zoo:nlp/question_answering/oberta-medium/pytorch/huggingface/squad/base-none" \
#"zoo:nlp/question_answering/oberta-base/pytorch/huggingface/squad/base-none" \
#"zoo:nlp/question_answering/roberta-base/pytorch/huggingface/squad/base-none" \
#"zoo:nlp/question_answering/roberta-large/pytorch/huggingface/squad/base-none" \
#"zoo:nlp/question_answering/oberta-base/pytorch/huggingface/squad/pruned95-none" \
#"zoo:nlp/question_answering/distilbert-none/pytorch/huggingface/squad/pruned90-none" \
#"zoo:nlp/question_answering/oberta-small/pytorch/huggingface/squad/base-none" \
#"zoo:nlp/question_answering/roberta-base/pytorch/huggingface/squad/base_quant-none" \
#"zoo:nlp/question_answering/bert-base_cased/pytorch/huggingface/squad/pruned90-none" \

zoo_stub_list=( \
"zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/pruned95_quant-none-vnni" \
"zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/14layer_pruned50_quant-none-vnni" \
"zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/base_quant-none" \
"zoo:nlp/question_answering/bert-base/pytorch/huggingface/squad/pruned95_obs_quant-none" \
"zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/14layer_pruned50-none-vnni" \
"zoo:nlp/question_answering/obert-base/pytorch/huggingface/squad/pruned90-none" \
"zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/pruned97_quant-none" \
"zoo:nlp/question_answering/bert-base/pytorch/huggingface/squad/pruned90-none" \
"zoo:nlp/question_answering/bert-large/pytorch/huggingface/squad/pruned80_quant-none-vnni" \
"zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/pruned95-none-vnni" \
"zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/pruned97-none" \
"zoo:nlp/question_answering/bert-large/pytorch/huggingface/squad/base-none" \
"zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/base-none" \
"zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/base-none" \
)

rerun=""
power=" --power=yes --adr.mlperf-power-client.power_server=192.168.0.15 --env.CM_MLPERF_SKIP_POWER_CHECKS=yes"
power=" --power=yes --adr.mlperf-power-client.power_server=192.168.0.15"
power=""
max_batchsize=128
max_batchsize=1
scenario="Offline"
scenario="SingleStream"

if [[ $scenario == "Offline" ]]; then
for stub in ${zoo_stub_list[@]}; do
cmd="cm run script --tags=run,mlperf,inference,generate-run-cmds,_find-performance  \
   --adr.python.version_min=3.8 \
   --implementation=reference \
   --model=bert-99 \
   --precision=int8 \
   --backend=deepsparse \
   --device=cpu \
   --scenario=Offline \
   --test_query_count=15000 \
   --adr.mlperf-inference-implementation.max_batchsize=$max_batchsize \
   --results_dir=$HOME/results_dir \
   --env.CM_MLPERF_NEURALMAGIC_MODEL_ZOO_STUB=$stub \
   ${rerun} \
   --quiet"
  echo ${cmd}
  eval ${cmd}
done
fi

for stub in ${zoo_stub_list[@]}; do
 cmd="cm run script --tags=run,mlperf,inference,generate-run-cmds,_submission  \
   --adr.python.version_min=3.8 \
   --adr.compiler.tags=gcc \
   --implementation=reference \
   --model=bert-99 \
   --precision=int8 \
   --backend=deepsparse \
   --device=cpu \
   --scenario=$scenario \
   --execution_mode=valid \
   --adr.mlperf-inference-implementation.max_batchsize=$max_batchsize \
   ${power} \
   --results_dir=$HOME/results_dir \
   --env.CM_MLPERF_NEURALMAGIC_MODEL_ZOO_STUB=$stub \
   --quiet"
  echo ${cmd}
  eval ${cmd}
done
