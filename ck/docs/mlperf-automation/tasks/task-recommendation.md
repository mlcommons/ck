**[ [TOC](../README.md) ]**

# MLPerf&trade; Inference v1.0: recommendation

## Official models

| model | reference app | framework | dataset |
| ---- | ---- | ---- | ---- |
| dlrm | [recommendation/dlrm](https://github.com/mlperf/inference/tree/r1.0/recommendation/dlrm/pytorch) | pytorch, tensorflow(?), onnx(?) | Criteo Terabyte |

## Common CK setup

```
python3 -m pip install ck
ck pull repo:mlcommons@ck-venv

ck create venv:mlperf-inference --template=mlperf-inference-1.0

ck activate venv:mlperf-inference
```


**TBD**


## Notes

* [20210420] DLRM inference README out of date
  * https://github.com/mlcommons/inference/issues/917
  * https://github.com/mlcommons/inference/issues/604

* CK components: 
  * [CK packages](https://cknow.io/?q=module_uoa%3A%22program%22+AND+dlrm)
  * [CK workflows](https://cknow.io/?q=module_uoa%3A%22program%22+AND+dlrm)
