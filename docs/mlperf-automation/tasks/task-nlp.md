**[ [TOC](../README.md) ]**

# MLPerf&trade; Inference v1.0: NLP

## Official models

| model | framework | accuracy | dataset | model link | model source | precision | notes |
| ----- | --------- | -------- | ------- | ---------- | ------------ | --------- | ----- |
| BERT-Large | TensorFlow | f1_score=90.874% | SQuAD v1.1 validation set | [from zenodo](https://zenodo.org/record/3733868) [from zenodo](https://zenodo.org/record/3939747) | [BERT-Large](https://github.com/google-research/bert), trained with [NVIDIA DeepLearningExamples](https://github.com/NVIDIA/DeepLearningExamples/tree/master/TensorFlow/LanguageModeling/BERT) | fp32 | |
| BERT-Large | PyTorch | f1_score=90.874% | SQuAD v1.1 validation set | [from zenodo](https://zenodo.org/record/3733896) | [BERT-Large](https://github.com/google-research/bert), trained with [NVIDIA DeepLearningExamples](https://github.com/NVIDIA/DeepLearningExamples/tree/master/TensorFlow/LanguageModeling/BERT), converted with [bert_tf_to_pytorch.py](bert_tf_to_pytorch.py) | fp32 | |
| BERT-Large | ONNX | f1_score=90.874% | SQuAD v1.1 validation set | [from zenodo](https://zenodo.org/record/3733910) | [BERT-Large](https://github.com/google-research/bert), trained with [NVIDIA DeepLearningExamples](https://github.com/NVIDIA/DeepLearningExamples/tree/master/TensorFlow/LanguageModeling/BERT), converted with [bert_tf_to_pytorch.py](bert_tf_to_pytorch.py) | fp32 | |
| BERT-Large | ONNX | f1_score=90.067% | SQuAD v1.1 validation set | [from zenodo](https://zenodo.org/record/3750364) | Fine-tuned based on the PyTorch model and converted with [bert_tf_to_pytorch.py](bert_tf_to_pytorch.py) | int8, symetrically per-tensor quantized without bias | See [MLPerf INT8 BERT Finetuning.pdf](MLPerf INT8 BERT Finetuning.pdf) for details about the fine-tuning process |


## Common CK setup

```
python3 -m pip install ck
ck pull repo:mlcommons@ck-venv

ck create venv:mlperf-inference --template=mlperf-inference-1.0

ck activate venv:mlperf-inference
```




**TBD**
