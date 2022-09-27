## 20210625: New examples

### CMDs

```
ck display dashboard --template=result --cfg=demo.mlperf.inference

ck display dashboard --template=result --cfg=demo.mlperf.mobilenets
ck display dashboard --template=result --cfg=demo.mlperf.mobilenets --experiment_uoa=mlperf-image-classification-single-stream-onnx-explore-threads

ck display dashboard --template=result --cfg=demo.request.asplos18
```

### URLS

```
ck start web
```

* http://localhost:3344/?template=result&cfg=demo.request.asplos18

* http://localhost:3344/?template=result&cfg=demo.mlperf.inference

* http://localhost:3344/?template=result&cfg=demo.mlperf.mobilenets
* http://localhost:3344/?template=result&cfg=demo.mlperf.mobilenets&repo_uoa=ai&data_uoa=xyz*&tags=abc

* http://localhost:3344/?template=result&cfg=demo.mlperf.mobilenets&experiment_uoa=mlperf-image-classification-single-stream-onnx-explore-threads
* http://localhost:3344/?template=result&cfg=demo.mlperf.mobilenets&data_uoa=-&experiment_uoa=mlperf-image-classification-single-stream-onnx-explore-threads
