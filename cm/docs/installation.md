# CM installation

Our goal is to keep the CM automation meta-framework as simple and portable as possible
with minimal dependencies: python 3+, pip, git and wget.

Here are typical installation procedures across different operating systems:

* [Ubuntu, Debian](#ubuntu-debian)
* [Red Hat](#red-hat)
* [MacOS](#macos)
* [Windows](#windows)


You can find Docker containers for CM [here](../../docker).

You can customize CM installation using environment variables described [here](#cm-customization).

You can reuse misc CM utils listed [here](#misc-cm-utils).

## Ubuntu, Debian

*We have successfully tested CM on Ubuntu 18.x, 20.x, 22.x:*

```bash
sudo apt update && sudo apt upgrade

sudo apt install python3 python3-pip git wget

python3 -m pip install cmind
```

Note that you may need to restart your shell to update PATH to the "cm" binary. 
Alternatively you can run 

```bash
source .profile
```

```
gfursin@mlcommons-ck-cm-dev:~$ cm

cm {action} {automation} {artifact(s)} {--flags} @input.yaml @input.json
```

You are ready to use CM automation meta-framework.



## Red Hat

*We have successfully tested CM on Red Hat 9 and CentOS 8*

```bash
sudo dnf update

sudo dnf install python3 python-pip git wget

python3 -m pip install cmind --user

```

## MacOS

```bash
brew install python3 python3-pip git wget

python3 -m pip install cmind
```


## Windows

* Download and install Git from [git-for-windows.github.io](https://git-for-windows.github.io).
* Download and install Python 3+ from [www.python.org/downloads/windows](https://www.python.org/downloads/windows).

```bash
python -m pip install cmind
```



# CM testing

If the installation is successful, you can run cm CLI as follows:

```bash
gfursin@cmind:~$ cm

cm {action} {automation} {artifact(s)} {flags} @input.yaml @input.json
```

*Note that you may need to relogin to your shell to update the PATH to the CM CLI!*

You can also quickly test the installation and check the version as follows:
```bash
gfursin@mlcommons-ck-cm-dev:~$ cm test core

CM version: 1.0.3

Python executable used by CK: /usr/bin/python3

Path to CM package:         /home/user/.local/lib/python3.9/site-packages/cmind
Path to CM core module:     /home/user/.local/lib/python3.9/site-packages/cmind/core.py
Path to CM internal repo:   /home/user/.local/lib/python3.9/site-packages/cmind/repo

Path to CM repositories:    /home/user/CM

GitHub for CM developments:        https://github.com/mlcommons/ck/tree/master/cm
GitHub for CM automation scripts:  https://github.com/mlcommons/ck/tree/master/cm-mlops
Reporting issues and ideas:        https://github.com/mlcommons/ck/issues
Joining the open MLPerf workgroup: http://bit.ly/mlperf-edu-wg
```


# CM customization

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


# Misc CM utils

We implemented and shared the following misc CM utils:

### CM UID generator

```bash
cm uid core
```

### json2yaml converter

```bash
cm pull repo mlcommons@ck

cm json2yaml utils --input={json file}
```

### yaml2json converter

```bash
cm pull repo mlcommons@ck

cm json2yaml utils --input={yaml file}
```

### sort json file

```bash
cm pull repo mlcommons@ck

cm sort-json utils --input={json file}
```

### dos2unix

Remove \r from txt files on Windows:

```bash
cm pull repo mlcommons@ck

cm dos2unix utils --input={txt file}
```


# Target platform support

* x8664
* Arm64
* CUDA-based devices
* Mobile devices with Arm64, GPU and DSP (*on-going development*)
* TinyML devices (*on-going development*)
* Simulators (*on-going development*)

