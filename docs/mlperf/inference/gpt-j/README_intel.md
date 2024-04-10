[ [Back to index](README.md) ]

## Run this benchmark via CM

You can use `cm docker` instead of `cm run` to run the Intel implementation inside a docker container. 
But for `gptj` we have found an issue of the code getting hanged when run on a 24 core machine but only when inside a docker container. 

### Do a test run to detect and record the system performance

```
cm run script --tags=run-mlperf,inference,_find-performance \
--scenario=Offline --model=gptj-99 --implementation=intel-original --backend=pytorch \
--category=datacenter --division=open --quiet
```
* Use `--division=closed` to run all scenarios for the closed division (compliance tests are skipped for `_find-performance` mode)
* Intel implementation currently supports only datacenter scenarios


### Do full accuracy and performance runs for all the Offline scenario

```
cm run script --tags=run-mlperf,inference,_submission \
--scenario=Offline --model=gptj-99 --implementation=intel-original --backend=pytorch \
--category=datacenter --division=open --execution-mode=valid --quiet
```

### Do full accuracy and performance runs for all the Server scenario

```
cm run script --tags=run-mlperf,inference,_submission \
--scenario=Server --model=gptj-99 --implementation=intel-original --backend=pytorch \
--category=datacenter --division=open --execution-mode=valid --server_target_qps=0.3 --quiet
```
* `--server_target_qps` can be adjusted to the maximum as per the given system (which produces a valid result)

### Generate and upload MLPerf submission

Follow [this guide](../Submission.md) to generate the submission tree and upload your results.

### Questions? Suggestions?

Check the [MLCommons Task Force on Automation and Reproducibility](../../../taskforce.md) 
and get in touch via [public Discord server](https://discord.gg/JjWNWXKxwT).

### Extra Examples

#### Test GPT-J int4 using Intel v3.1 code drop offline

```bash
python3 -m pip install cmind -U
cm pull repo mlcommons@ck
cm run script --tags=run-mlperf,inference --implementation=intel --model=gptj-99 --scenario=Offline --precision=int4 --docker --sut=sapphire-rapids.112c --docker_cache=no

```

We now use `--docker` to run the command inside the docker while the preparation (model or big dataset download) happens on the host. 

In order to use rclone copy (and not rclone sync) on your submission system, please add `--env.CM_RCLONE_COPY_USING=copy` to the run above command. 

You can use `--docker_cache=no` to force CM to pick up the latest changes inside automatically-generated container (`cm pull repo`).


Extra commands:
```

cm run script --tags=run-mlperf,inference,_submission \
  --scenario=Offline --model=gptj-99 --implementation=intel-original --backend=pytorch \
  --category=datacenter --division=open --execution-mode=valid --quiet

cm run script --tags=run-mlperf,inference,_submission \
  --scenario=Server --model=gptj-99 --implementation=intel-original --backend=pytorch \
  --category=datacenter --division=open --execution-mode=valid --server_target_qps=0.3 --quiet
```
