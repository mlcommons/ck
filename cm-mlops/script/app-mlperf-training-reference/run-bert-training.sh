#!/bin/bash

export TF_XLA_FLAGS='--tf_xla_auto_jit=2'
train_batch_size=24
cmd="python run_pretraining.py \
  --bert_config_file=${CM_MLPERF_TRAINING_BERT_CONFIG_PATH} \
  --output_dir=/tmp/output/ \
  --input_file=${CM_MLPERF_TRAINING_BERT_TFRECORDS_PATH}/part* \
  --nodo_eval \
  --do_train \
  --eval_batch_size=8 \
  --learning_rate=0.0001 \
  --init_checkpoint=${CM_MLPERF_TRAINING_BERT_DATA_PATH}/phase1/model.ckpt-28252 \
  --iterations_per_loop=1000 \
  --max_predictions_per_seq=76 \
  --max_seq_length=512 \
  --num_train_steps=107538 \
  --num_warmup_steps=1562 \
  --optimizer=lamb \
  --save_checkpoints_steps=6250 \
  --start_warmup_step=0 \
  --num_gpus=1 \
  --train_batch_size=${train_batch_size}"
echo "${cmd}"
eval "${cmd}"
test $? -eq 0 || exit $?

