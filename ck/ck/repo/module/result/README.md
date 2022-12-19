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

### Push data to a dashboard

```
ck push ai:result:demo.mlperf.inference --user=all @push_result.json
```

## Notes

### Variation

At the moment, X/Y variation can be plotted only when "colorDimension" 
is on due to our old implementation of the graph widget
(see meta in "result.cfg:demo.mlperf.explore-threads").

One can use "_const" dimension as a trick to turn on "colorDimension" 
but do not show different colors: "colorDimension":"_const"
