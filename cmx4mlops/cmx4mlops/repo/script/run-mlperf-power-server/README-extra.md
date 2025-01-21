# Run MLPerf Power Server Script
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/specs/script.md) runs the [MLPerf Power Server script](https://github.com/mlcommons/power-dev/tree/master/ptd_client_server).

## How To
```bash
cm run script --tags=run,mlperf,power,server [--interface_flag=<> \
--device_port=<> --outdir=<> --logfile=<> --outdir=<> --device_type=<> ]
```

### Default Values
1. `ntp_server`: `time.google.com`
2. `interface_flag`: ""
3. `device_port`: `/dev/usbtmc0`
4. `device_type`: `49`
5. `outdir`: `~/mlperf_power_logs`
6. `logfile`: `logs_ptdaemon.txt`

