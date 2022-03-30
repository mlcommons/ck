# First steps


## Prerequisites

The CM toolkit (CK2 framework) requires minimal dependencies: Python 3.x, PIP and Git. 

### Linux

You need to have the following packages installed (Ubuntu example):

```bash
sudo apt-get install python3 python3-pip git wget
```

### MacOS

```bash
brew install python3 python3-pip git wget
```

### Windows

* Download and install Git from [git-for-windows.github.io](https://git-for-windows.github.io).
* Download and install any Python from [www.python.org/downloads/windows](https://www.python.org/downloads/windows).

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
pip install cmind
```

You can also install CM using a specific Python version (for example, Python 3.9):
```bash
python3.9 -m pip install cmind
```

*You may need to add flag "--user" to install the client in your user space:*
```bash
pip install cmind --user
python3.8 -m pip install cmind --user
```

You should now be able to run CM using one of the following alternative commands:
```bash
cmind
python3.6 -m cmind
```

If the installation is successful, you will see some internal information 
about the CM installation and a Python version used:

```bash
gfursin@cmind:~$ cmind

```


## Platform support
CK supports the following platforms:

|               | As a host platform | As a target platform |
|---------------|:------------------:|:--------------------:|
| Generic Linux | ✓ | ✓ |
| Linux (Arm)   | ✓ | ✓ |
| Raspberry Pi  | ✓ | ✓ |
| MacOS         | ✓ | ± |
| Windows       | ✓ | ✓ |
| Android       | Not required | TBD |
| iOS           | Not required | TBD |
| Bare-metal (edge devices)   | Not required | TBD |

