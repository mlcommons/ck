```bash
cm run script \
--tags=app,mlperf,_resnet50,_onnxruntime  \
--env.CM_OUTPUT_DIR=$HOME/final_results \
--env.CM_LOADGEN_MODE=accuracy \
--env.CM_LOADGEN_SCENARIO=Offline \
--add_deps.loadgen.version=r2.1 \
--add_deps_recursive.inference-src.tags=_octoml
```
