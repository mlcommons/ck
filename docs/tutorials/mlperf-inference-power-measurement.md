[ [Back to index](../README.md) ]

# Tutorial: Automating Power Measurements for MLPerf inference using MLCommons CM

*Prepared by the [MLCommons taskforce on automation and reproducibility](../taksforce.md) and [OctoML](https://octoml.ai)*.

## Requirements

1. Power analyzer (anyone [certified by SPEC PTDaemon](https://www.spec.org/power/docs/SPECpower-Device_List.html)). 
   Yokogawa is the one that most submitters have submitted with and a new single-channel model like 310E can cost around 3000$.
   The [MLCommons taskforce on automation and reproducibility ](../taksforce.md) 
   is also using the [Yokogawa 310E](https://tmi.yokogawa.com/solutions/products/power-analyzers/digital-power-meter-wt300e/) 
   to automate and simplify MLPerf submissions.

2. SPEC PTDaemon (can be downloaded from [here](https://github.com/mlcommons/power) after signing the EULA which can be requested 
   by sending an email to `support@mlcommons.org`). Once you have GitHub access to the MLCommons power repository then the CM workflow 
   will automatically download and configure the SPEC PTDaemon tool.

3. Access to the [MLCommons power-dev](https://github.com/mlcommons/power-dev) repository 
   which has the `server.py` to be run on the director node and `client.py` to be run on the SUT node. This repository being public will be 
   automatically pulled by the CM workflow.

## Connecting power analyzer to the computer

We need to connect the power analyzer to a director machine via USB and the machine must be running Linux 
(Ethernet mode is supported only on Windows which this workflow is not supporting yet). 
The power supply to the SUT is done through the power analyzer (current in series and voltage in parallel). 
An adapter like [this](https://amzn.to/3Cl2TV5) can help avoid cutting the electrical wires. 

![pages (14)](https://user-images.githubusercontent.com/4791823/210117283-82375460-5b3a-4e8a-bd85-9d33675a5843.png).

The director machine runs the `server.py` script and loads a server process that communicates with the SPEC PTDaemon. 
When a client connects to it (using `client.py`), it in turn connects to the PTDaemon and initiates a measurement run. 
Once the measurement ends, the power log files are transferred to the client. 

## Ranging mode and Testing mode

Power analyzers usually have different current and voltage ranges it supports and the exact ranges to be used 
depends on a given SUT and this needs some empirical data. We can do a ranging run where the current and voltage ranges 
are set to `Auto` and the power analyzer automatically figures out the correct ranges needed. 
These determined ranges are then used for a proper testing mode run. 
Using the 'auto' mode in a testing run is not allowed as it can mess up the measurements.

## Setup using MLCommons CM

## Install CM

Please follow these [instructions](https://github.com/mlcommons/ck/blob/master/docs/installation.md)
to install the MLCommons CM automation tool.

## Start Power Server (Power analyzer should be connected to this computer and PTDaemon runs here)

If you are having GitHub access to [MLCommons power](https://github.com/mlcommons/power) repository,
PTDaemon should be automatically installed using the following CM command:

PS: The below command will ask for `sudo` permission on Linux and should be run with administrator privilege on Windows (to do NTP time sync).
```bash
cm run script --tags=mlperf,power,server --device_type=49 --device_port=/dev/usbtmc0
```
* ``--interface_flag="-U" and `--device_port=1` (can change as per the USB slot used for connecting) can be used on Windows for USB connection
* `--device_type=49` corresponds to Yokogawa 310E and `ptd -h` should list the device_type for all supported devices. The location of `ptd` can be found using the below command
* `--device_port=20` and `--interface_flag="-g" can be used to connect to GPIB interface (currently supported only on Windows) with the serial address set to 20
```bash
cat `cm find cache --tags=get,spec,ptdaemon`/cm-cached-state.json
```


More configuration options can be found [here](https://github.com/mlcommons/power-dev/tree/master/ptd_client_server).

### Running the power server inside a docker container

```bash
cm docker script --tags=run,mlperf,power,server --docker_gh_token=<GITHUB AUTH_TOKEN> \
--docker_os=ubuntu --docker_os_version=22.04 --device=/dev/usbtmc0
```
* Device address may need to be changed depending on the USB port being used
* The above command uses a host-container port mapping 4950:4950 which can be changed by using `--docker_port_maps,=4950:4950`

## Running a dummy workload with power (on host machine)

```bash
cm run script --tags=mlperf,power,client --power_server=<POWER_SERVER_IP> 
```

### Run a dummy workload with power inside a docker container

```bash
cm run script --tags=run,docker,container --cm_repo=ctuning@mlcommons-ck \
--docker_os=ubuntu --docker_os_version=22.04  \
--run_cmd="cm run script --tags==mlperf,power,client --power_server=<POWER_SERVER_IP>"
```

## Running MLPerf Image Classification with power

```bash
cm run script --tags=app,mlperf,inference,_reference,_power,_resnet50,_onnxruntime,_cpu --mode=performance --power_server=<POWER_SERVER_IP>
```

### Running MLPerf Image Classification with power inside a docker container
```bash
cm run script --tags=run,docker,container --cm_repo=ctuning@mlcommons-ck  \
--docker_os=ubuntu --docker_os_version=22.04  \
--run_cmd="cm run script --tags=app,mlperf,inference,_reference,_power,_resnet50,_onnxruntime,_cpu --mode=performance --power_server=<POWER_SERVER_IP>"
```


### Using CM GUI to run MLPerf inference benchmarks and measure power

[Link](https://access.cknowledge.org/playground/?action=howtorun&bench_uid=39877bb63fb54725)

## Further questions?

If you have further questions, are interested in our development roadmap, or need help to automate, optimize and validate your MLPerf submission,
feel free to contact the [MLCommons taskforce on automation and reproducibility](../taskforce.md).
