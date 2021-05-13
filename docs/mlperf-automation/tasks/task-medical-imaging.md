# MLPerf Inference v1.0: medical imaging

## Official models

| model | reference app | framework | dataset |
| ---- | ---- | ---- | ---- |
| 3d-unet | [vision/medical_imageing/3d-unet](https://github.com/mlperf/inference/tree/r1.0/vision/medical_imaging/3d-unet) | pytorch, tensorflow(?), onnx(?) | BraTS 2019 |

## Common CK setup

```
python3 -m pip install ck
ck pull repo:octoml@venv

ck create venv:mlperf-inference --template=mlperf-inference-1.0

ck activate venv:mlperf-inference
```




**TBD**
