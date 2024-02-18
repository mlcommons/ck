[ [Back to index](../README.md) ]

***Draft Stage***
## Run Commands
### Quick submission run (short run)
```bash
cm run script --tags=run,mlperf,inference,generate-run-cmds,_submission,_short --submitter=name \
--lang=reference --model=bert-99 --backend=deepsparse --device=cpu --scenario=Offline  --quantized 
--results_dir=/home/cmuser/tmp2  --submission_dir=/home/cmuser/submission --clean
```
### Customizations
1. `_short` -> `_valid`: For full submission run
2. `--scenario` -> one of `SingleStream`, `Server` for changing the scenarios
3. `--backend` -> one of `onnxruntime`, `tf`, `pytorch`, `deepsparse`
4. `--quantized`: only works for `onnxruntime` and `deepsparse`
5. `--device` -> one of `cpu`, `cuda`
6. `--submitter`: Name of the submitter excluding spaces
7. `--clean`: Clean everything and do not reuse previous run results
