# Run commands on A100, SXM Edge system

## Bert-99

### Quick performance test
```
cmr "generate-run-cmds inference _performance-only"  \
--model=bert-99 --implementation=nvidia-original \
--device=cuda --backend=tensorrt --category=edge \
--division=open --quiet --scenario=Offline --execution_mode=fast \
--target_qps=1000 --rerun --gpu_name=a100 \
--adr.nvidia-harness.tags=_sxm
```

### Full run bert-99
This will do performance+accuracy+compliance for singlestream+offline scenarios. Please change the `target_qps` to the actual output value from the previous command.

```
cmr "generate-run-cmds inference _submission _all-scenarios"  \
--model=bert-99 --implementation=nvidia-original \
--device=cuda --backend=tensorrt --category=edge \
--division=open --quiet --execution_mode=valid \
--target_qps=1000 --rerun --gpu_name=a100 \
--adr.nvidia-harness.tags=_sxm
```

## Resnet50

### Quick performance test

Imagenet dataset must be downloaded separately and detected in cm using 
```
cmr "get dataset original imagenet _full" --input="<Path to imagenet dir containing 50000 validation images>"
```

```
cmr "generate-run-cmds inference _performance-only"  \
--model=resnet50 --implementation=nvidia-original \
--device=cuda --backend=tensorrt --category=edge \
--division=open --quiet --scenario=Offline --execution_mode=fast \
--target_qps=1000 --rerun --gpu_name=a100 \
--adr.nvidia-harness.tags=_sxm
```

### Full run resnet50
This will do performance+accuracy+compliance for singlestream+offline scenarios. Please change the `target_qps` to the actual output value from the previous command.

```
cmr "generate-run-cmds inference _submission _all-scenarios"  \
--model=resnet50 --implementation=nvidia-original \
--device=cuda --backend=tensorrt --category=edge \
--division=open --quiet --execution_mode=valid \
--target_qps=1000 --rerun --gpu_name=a100 \
--adr.nvidia-harness.tags=_sxm
```
