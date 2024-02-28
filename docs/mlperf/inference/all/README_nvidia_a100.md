[ [Back to MLPerf inference benchmarks index](../README.md) ]

*Note: from Feb 2024, we suggest you to use [this GUI](https://access.cknowledge.org/playground/?action=howtorun&bench_uid=39877bb63fb54725)
 to configure MLPerf inference benchmark, generate CM commands to run it across different implementations, models, data sets, software
 and hardware, and prepare your submissions.*


# MLPerf inference benchmark

CM run commands to run MLPerf inference with main models 
on Nvidia A100, SXM Edge system using Nvidia implementation.

## Bert-99

### Quick performance test
```
cmr "run-mlperf inference _performance-only"  \
--model=bert-99 --implementation=nvidia-original \
--device=cuda --backend=tensorrt --category=edge \
--division=open --quiet --scenario=Offline --execution-mode=fast \
--target_qps=3560 --rerun --gpu_name=a100 \
--adr.nvidia-harness.tags=_sxm \
--results_dir=$HOME/results_dir
```

### Full run
This will do performance+accuracy+compliance for singlestream+offline scenarios. Please change the `target_qps` to the actual output value from the previous command.

```
cmr "run-mlperf inference _submission _all-scenarios"  \
--model=bert-99 --implementation=nvidia-original \
--device=cuda --backend=tensorrt --category=edge \
--division=open --quiet --execution-mode=valid \
--target_qps=3560 --rerun --gpu_name=a100 \
--adr.nvidia-harness.tags=_sxm \
--results_dir=$HOME/results_dir
```

## Resnet50

### Quick performance test

Imagenet dataset must be downloaded separately and detected in cm using 
```
cmr "get dataset original imagenet _full" --input="<Path to imagenet dir containing 50000 validation images>"
```

```
cmr "run-mlperf inference _performance-only"  \
--model=resnet50 --implementation=nvidia-original \
--device=cuda --backend=tensorrt --category=edge \
--division=open --quiet --scenario=Offline --execution-mode=fast \
--target_qps=43000 --rerun --gpu_name=a100 \
--adr.nvidia-harness.tags=_sxm \
--results_dir=$HOME/results_dir
```

### Full run
This will do performance+accuracy+compliance for singlestream+offline scenarios. Please change the `target_qps` to the actual output value from the previous command.

```
cmr "run-mlperf inference _submission _all-scenarios"  \
--model=resnet50 --implementation=nvidia-original \
--device=cuda --backend=tensorrt --category=edge \
--division=open --quiet --execution-mode=valid \
--target_qps=43000 --rerun --gpu_name=a100 \
--adr.nvidia-harness.tags=_sxm \
--results_dir=$HOME/results_dir
```

## Retinanet

### Quick performance test
```
cmr "run-mlperf inference _performance-only"  \
--model=retinanet --implementation=nvidia-original \
--device=cuda --backend=tensorrt --category=edge \
--division=open --quiet --scenario=Offline --execution-mode=fast \
--target_qps=715 --rerun --gpu_name=a100 \
--adr.nvidia-harness.tags=_sxm \
--results_dir=$HOME/results_dir
```

### Full run
This will do performance+accuracy+compliance for singlestream+offline scenarios. Please change the `target_qps` to the actual output value from the previous command.

```
cmr "run-mlperf inference _submission _all-scenarios"  \
--model=retinanet --implementation=nvidia-original \
--device=cuda --backend=tensorrt --category=edge \
--division=open --quiet --execution-mode=valid \
--target_qps=715 --rerun --gpu_name=a100 \
--adr.nvidia-harness.tags=_sxm \
--results_dir=$HOME/results_dir
```

## RNNT


### Quick performance test
```
cmr "run-mlperf inference _performance-only"  \
--model=rnnt --implementation=nvidia-original \
--device=cuda --backend=tensorrt --category=edge \
--division=open --quiet --scenario=Offline --execution-mode=fast \
--target_qps=14000 --rerun --gpu_name=a100 \
--adr.nvidia-harness.tags=_sxm \
--results_dir=$HOME/results_dir
```

### Full run
This will do performance+accuracy+compliance for singlestream+offline scenarios. Please change the `target_qps` to the actual output value from the previous command.

```
cmr "run-mlperf inference _submission _all-scenarios"  \
--model=rnnt --implementation=nvidia-original \
--device=cuda --backend=tensorrt --category=edge \
--division=open --quiet --execution-mode=valid \
--target_qps=14000 --rerun --gpu_name=a100 \
--adr.nvidia-harness.tags=_sxm \
--results_dir=$HOME/results_dir
```

## 3d-unet


### Quick performance test
```
cmr "run-mlperf inference _performance-only"  \
--model=3d-unet-99 --implementation=nvidia-original \
--device=cuda --backend=tensorrt --category=edge \
--division=open --quiet --scenario=Offline --execution-mode=fast \
--target_qps=3.7 --rerun --gpu_name=a100 \
--adr.nvidia-harness.tags=_sxm \
--results_dir=$HOME/results_dir
```

### Full run
This will do performance+accuracy+compliance for singlestream+offline scenarios. Please change the `target_qps` to the actual output value from the previous command.

```
cmr "run-mlperf inference _submission _all-scenarios"  \
--model=3d-unet-99 --implementation=nvidia-original \
--device=cuda --backend=tensorrt --category=edge \
--division=open --quiet --execution-mode=valid \
--target_qps=3.7 --rerun --gpu_name=a100 \
--adr.nvidia-harness.tags=_sxm \
--results_dir=$HOME/results_dir
```

Once all 5 model results are done, please follow [Submission](../Submission.md) to generate the required submission. 

### Questions? Suggestions?

Check the [MLCommons Task Force on Automation and Reproducibility](../../../taskforce.md) 
and get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT).
