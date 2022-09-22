# Installation


## Prerequisites

The CM framework (aka CK2) requires minimal dependencies: Python 3.x, PIP, Git and wget. 

### Ubuntu / Debian

You need to have the following packages installed:

```bash
sudo apt install python3 python3-pip git wget
```

You can use the following commands if you need to upgrade your system:
```bash
sudo apt update
sudo apt upgrade 

### Red Hat

```bash
sudo dnf install python python-pip git wget
```

### MacOS

```bash
brew install python3 python3-pip git wget
```

### Windows

* Download and install Git from [git-for-windows.github.io](https://git-for-windows.github.io).
* Download and install Python 3+ from [www.python.org/downloads/windows](https://www.python.org/downloads/windows).

### Android (Linux host)

These dependencies are needed to cross-compile for Android (tested on Ubuntu 18.04 including Docker and Windows 10 Subsystem for Linux). 

```bash
 sudo apt update
 sudo apt install git wget libz-dev curl cmake
 sudo apt install gcc g++ autoconf autogen libtool
 sudo apt install android-sdk
 sudo apt install google-android-ndk-installer
```



## CM installation

You can install the Collective Mind framework on most platforms using PIP as follows:

```bash
pip3 install cmind
```
or

```bash
python3 -m pip install cmind
```
or
```bash
pip install cmind
```

You can also install CM using a specific Python version (for example, Python 3.9):
```bash
python3.9 -m pip install cmind
```

*You may need to add flag "--user" to install the client in your user space:*
```bash
pip3 install cmind --user
```

If the installation is successful, you can run cm CLI as follows:

```bash
gfursin@cmind:~$ cm

cm {action} {automation} {artifact(s)} {flags} @input.yaml @input.json
```

*Note that you may need to relogin to your shell to update the PATH to the CM CLI!*

You can also quickly test the installation and check the version as follows:
```bash
gfursin@cmind:~$ cm test core

CM version: 1.0.2

Python executable used by CK: /usr/bin/python3

Path to CM package:         /home/user/.local/lib/python3.9/site-packages/cmind
Path to CM core module:     /home/user/.local/lib/python3.9/site-packages/cmind/core.py
Path to CM internal repo:   /home/user/.local/lib/python3.9/site-packages/cmind/repo

Path to CM repositories:    /home/user/CM

GitHub for CM developments:        https://github.com/mlcommons/ck/tree/master/cm
GitHub for CM automation scripts:  https://github.com/mlcommons/ck/tree/master/cm-mlops
Reporting issues and ideas:        https://github.com/mlcommons/ck/issues
```


## CM customization

You can use the following environment variables to customize CM installation:

* 'CM_REPOS' - change path to the CM repositories and *repos.json* file.

  By default, CM will keep CM repositories in:
  * *$HOME/CM* directory on Linux 
  * *%USERPROFILE%\CM* directory on Windows

* 'CM_CONFIG' - provide full path to a JSON or YAML file with the CM configuration.
  The content of this file will be merged with the ["cfg" dictionary](https://github.com/mlcommons/ck/blob/master/cm/cmind/config.py#L23)
  from the *config.py*.

* 'CM_DEBUG' - if set to 'yes', turn on internal CM debugging and raise errors 
  in CM automations instead of returning a dictionary with an error *{'return':ERROR CODE, 'error':'ERROR note'}*

* 'CM_HOME' - change path to the CM python package with the default 'repo' directory.
  Useful to improve the default automations inside the CM package.



## Target platform support

* x8664
* Arm64
* CUDA-based devices
* Mobile devices with Arm64, GPU and DSP (*on-going development*)
* Edge devices (*on-going development*)
* Simulators (*on-going development*)

