**[ [TOC](../README.md) ]**

# MLPerf&trade; Inference v1.0: speech recognition

## Official models

| model | reference app | framework | dataset |
| ---- | ---- | ---- | ---- |
| rnnt | [speech_recognition/rnnt](https://github.com/mlperf/inference/tree/r1.0/speech_recognition/rnnt) | pytorch | OpenSLR LibriSpeech Corpus |


## Common CK setup

```
python3 -m pip install ck
ck pull repo:mlcommons@ck-venv

ck create venv:mlperf-inference --template=mlperf-inference-1.0

ck activate venv:mlperf-inference
```



**TBD**
