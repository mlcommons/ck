# cBench installation

You can install cBench on most platforms using PIP as follows:

```
pip install cbench
```

You can also install cBench using a specific Python version (for example, Python 3.6):
```
python3.6 -m pip install cbench
```

*You may need to add flag "--user" to install the client in the user space:*
```
pip install cbench --user
python3.6 -m pip install cbench --user
```

You should now be able to run this client using one of the following alternative commands:
```
cb

python3.6 -m cbench
```

If the installation is successful, you will see the list of all [available commands](../guide/commands).

### Prerequisites

The client requires minimal dependencies: Python 2.7+ or 3.x, PIP and Git. 

### Linux

You need to have the following packages installed (Ubuntu example):

```
sudo apt-get install python3 python3-pip git wget
```

### MacOS

```
brew install python3 python3-pip git wget
```

### Windows

* Download and install Git from [git-for-windows.github.io](https://git-for-windows.github.io).
* Download and install any Python from [www.python.org/downloads/windows](https://www.python.org/downloads/windows).

### Android (Linux host)

These dependencies are needed to cross-compile for Android (tested on Ubuntu 18.04 including Docker and Windows 10 Subsystem for Linux). 

```
 sudo apt update
 sudo apt install git wget libz-dev curl cmake
 sudo apt install gcc g++ autoconf autogen libtool
 sudo apt install android-sdk
 sudo apt install google-android-ndk-installer
```

### Docker

We prepared a Docker image with cBench installed:

* [CK-based MLPerf worklfow](https://hub.docker.com/repository/docker/ctuning/cbench-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows)
