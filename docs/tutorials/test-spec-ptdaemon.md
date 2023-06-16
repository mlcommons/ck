[ [Back to index](../README.md) ]

This tutorial describes how to test a power analyzer by manually giving the current and voltage ranges and thus avoiding a separate ranging mode run. If wrong values are given (tolerance is typically around 5 times), samples will be counted as uncertain and the number of uncertain samples are output in the `run_1/ptd_out.txt` file. 

## Requirements
Please see [this](./mlperf-inference-power-measurement.md) documentation for the requirements and system setup.

## Start Power Server (Yokogawa should be connected to this and PTDaemon runs here)
```
cm run script --tags=mlperf,power,server --device_type=49 --device_port=/dev/usbtmc0
```

## Start Power Client
```
cm run script --tags=mlperf,power,client --power_server=<POWER_SERVER_IP> --max_amps=0.1 --max_volts=250
```

If `--max_amps=0` or `--max_volts=0` is given, the limits are ignored and both ranging and testing modes are done. If both the values are positive, ranging mode is skipped and testing mode happens with the provided limits. 

For each sample of the testing run, uncertainty is measured and we get the total number of certain and uncertain samples during the run in the `run_1/ptd_out.txt` file. If any one sample is uncertain (uncertainty threshold is 1%), the test result can be considered invalid. 
