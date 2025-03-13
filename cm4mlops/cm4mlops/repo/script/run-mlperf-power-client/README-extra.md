# Run MLPerf Power Client Script
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/specs/script.md) runs the [MLPerf Power Server script](https://github.com/mlcommons/power-dev/tree/master/ptd_client_server).

## How To
```bash
cm run script --tags=run,mlperf,power,client [--log_dir=<> --power_server=<> \
--loadgen_logs_dir=<> --ntp_server=<> --run_cmd=<>]
```

### Default Values
1. `log_dir`: `logs`
2. `power_server`: `localhost`
3. `loadgen_logs_dir`: `loadgen_logs`,
4. `ntp_server`: `time.google.com`
5. `run_cmd`: `dummy.sh`
