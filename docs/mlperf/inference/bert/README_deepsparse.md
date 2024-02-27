[ [Back to index](README.md) ]

# BERT-Large

## BERT-99%: oBERT-Large Offline - DeepSparse
```
cm run script --tags=run,mlperf,inference,run-mlperf,_submission  \
   --adr.python.version_min=3.8 \
   --implementation=reference \
   --model=bert-99 \
   --precision=int8 \
   --backend=deepsparse \
   --device=cpu \
   --scenario=Offline \
   --mode=performance \
   --execution_mode=valid \
   --adr.mlperf-inference-implementation.max_batchsize=384 \
   --offline_target_qps=20 \
   --results_dir=$HOME/results_dir \
   --env.CM_MLPERF_NEURALMAGIC_MODEL_ZOO_STUB=zoo:nlp/question_answering/obert-large/pytorch/huggingface/squad/pruned95_quant-none-vnni
```

## BERT-99%: MobileBERT Offline

```
cm run script --tags=run,mlperf,inference,run-mlperf,_submission  \
   --adr.python.name=mlperf \
   --adr.python.version_min=3.8 \
   --implementation=reference \
   --model=bert-99 \
   --precision=int8 \
   --backend=deepsparse \
   --device=cpu \
   --scenario=Offline \
   --mode=performance \
   --execution_mode=valid \
   --adr.mlperf-inference-implementation.max_batchsize=384 \
   --offline_target_qps=20 \
   --results_dir=$HOME/results_dir \
   --env.CM_MLPERF_NEURALMAGIC_MODEL_ZOO_STUB=zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/14layer_pruned50_quant-none-vnni \
   --env.DEEPSPARSE_SEQLENS="64,128,192,256,384"
```

## BERT-99.9%: MobileBERT Offline - DeepSparse

```
cm run script --tags=run,mlperf,inference,run-mlperf,_submission  \
   --adr.python.version_min=3.8 \
   --implementation=reference \
   --compliance=no \
   --model=bert-99 \
   --precision=int8 \
   --backend=deepsparse \
   --device=cpu \
   --scenario=Offline \
   --mode=performance \
   --execution_mode=valid \
   --adr.mlperf-inference-implementation.max_batchsize=384 \
   --offline_target_qps=20 \
   --results_dir=$HOME/results_dir \
   --env.DEEPSPARSE_SEQLENS="64,128,192,256,384" \
   --env.CM_MLPERF_NEURALMAGIC_MODEL_ZOO_STUB=zoo:nlp/question_answering/mobilebert-none/pytorch/huggingface/squad/base_quant-none
```

# ResNet50

## ResNet50 Offline - DeepSparse

```
cm run script --tags=run,mlperf,inference,run-mlperf,_submission  \
   --adr.python.version_min=3.8 \
   --implementation=reference \
   --model=resnet50 \
   --precision=int8 \
   --backend=deepsparse \
   --device=cpu \
   --scenario=Offline \
   --mode=performance \
   --execution_mode=valid \
   --adr.imagenet-preprocessed.tags=_pytorch \
   --adr.mlperf-inference-implementation.dataset=imagenet_pytorch \
   --adr.mlperf-inference-implementation.model=zoo:cv/classification/resnet_v1-50/pytorch/sparseml/imagenet/pruned85_quant-none-vnni \
   --adr.mlperf-inference-implementation.max_batchsize=16 \
   --adr.mlperf-inference-implementation.num_threads=48 \
   --results_dir=$HOME/results_dir \
   --env.DEEPSPARSE_NUM_STREAMS=24 \
   --env.ENQUEUE_NUM_THREADS=2 \
   --offline_target_qps=204
```

### Generate and upload MLPerf submission

Follow [this guide](../Submission.md) to generate the submission tree and upload your results.

### Questions? Suggestions?

Check the [MLCommons Task Force on Automation and Reproducibility](../../../taskforce.md) 
and get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT).
