**[ [TOC](../README.md) ]**

# Example of CK dashboards for ML Systems DSE

You can record experiments in the CK "experiment" entries and visualize them using CK dashboards 
either locally or using the [cKnowledge.io platform](https://cknow.io/?q="mlperf-inference-all")



## Demo of a Docker with MLPerf&trade; dashboards for ML Systems DSE (Linux and Windows)

Container: [docker:ck-mlperf-dashboard-demo](https://github.com/mlcommons/ck-mlops/tree/main/docker/ck-mlperf-dashboard-demo)

### Install CK
```
python3 -m pip install ck
```

### Pull CK repository
```
ck pull repo:mlcommons@ck-mlops
```

### Build this container
```
ck build docker:ck-mlperf-dashboard-demo
```

Note that it will build and run several MLPerf&trade; benchmarks while recording results
to the CK 'experiment' entries to be used in the CK dashboard.

### Run this continer
```
ck run docker:ck-mlperf-dashboard-demo
```

### View CK dashboard in your browser

Go to http://localhost:3355/?template=dashboard&scenario=mlperf.mobilenets



## Demo of a Docker with MLPerf&trade; dashboards for ML Systems DSE (Linux and Windows)

Container: [docker:ck-mlperf-dashboard-demo](https://github.com/mlcommons/ck-mlops/tree/main/docker/ck-mlperf-dashboard-demo)

This container demonstrates how to run CK experiments and record results 
from the Docker in the local "mlperf-mobilenets" repository on the host machine
to be processed in Jupyter notebooks or visualized using CK dashboards.

### Install CK
```
python3 -m pip install ck
```

### Pull ck-ml repository via CK
```
ck pull repo:mlcommons@ck-mlops
```

### Create local mlperf-mobilenets repo
```
ck add repo:mlperf-mobilenets --quiet
```

### Build this container
```
ck build docker:ck-mlperf-local-dashboard-demo
```

### Run this container

You must run this container using a special script from [this directory](https://github.com/mlcommons/ck-mlops/tree/main/docker/ck-mlperf-local-dashboard-demo):
```
cd `ck find docker:ck-mlperf-local-dashboard-demo
```

* Linux: [docker-start.sh](https://github.com/mlcommons/ck-mlops/tree/main/docker/ck-mlperf-local-dashboard-demo/docker-start.sh)
* Windows: [docker-start.bat](https://github.com/mlcommons/ck-mlops/tree/main/docker/ck-mlperf-local-dashboard-demo/docker-start.bat)

This script will mount local CK mlperf-mobilenets repo inside Docker
to be able to record experiments there from the Docker container.

This script will call a helper script [https://github.com/mlcommons/ck-mlops/tree/main/docker/ck-mlperf-local-dashboard-demo/docker-helper.sh] with benchmarks
that you can modify to run different experiments.

### View CK dashboard localy

Run the following command from your host machine to visualize results:
```
ck display dashboard --scenario=mlperf.mobilenets
```
