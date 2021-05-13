# MLPerf Inference v1.0: recommendation

## Official models

| model | reference app | framework | dataset |
| ---- | ---- | ---- | ---- |
| dlrm | [recommendation/dlrm](https://github.com/mlperf/inference/tree/r1.0/recommendation/dlrm/pytorch) | pytorch, tensorflow(?), onnx(?) | Criteo Terabyte |

## Common CK setup

```
python3 -m pip install ck
ck pull repo:octoml@venv

ck create venv:mlperf-inference --template=mlperf-inference-1.0

ck activate venv:mlperf-inference
```


**TBD**


## Notes

* [20210420] DLRM inference README out of date
  * https://github.com/mlcommons/inference/issues/917
  * https://github.com/mlcommons/inference/issues/604




