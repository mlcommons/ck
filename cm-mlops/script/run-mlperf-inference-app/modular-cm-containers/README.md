***Outdated***

# About

Prototyping modular and customizable CM containers for MLPerf.

# Build

```bash
./build.sh
```

# Run

```bash
./run.sh

cm run script --tags=run,mlperf,inference,generate-run-cmds,_submission,_dashboard \
         --adr.python.version_min=3.8 \
         --submitter="modular-cm-mlperf-container" \
         --lang=python \
         --hw_name=default \
         --model=resnet50 \
         --backend=onnxruntime \
         --device=cpu \
         --scenario=Offline \
         --test_query_count=500 \
         --quiet \
         --clean
```
