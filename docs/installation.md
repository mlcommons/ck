[ [Back to index](README.md) ]


<details>
<summary>Click here to see the table of contents.</summary>

* [CM installation](#cm-installation)
  * [Ubuntu, Debian](#ubuntu-debian)
  * [Red Hat](#red-hat)
  * [MacOS](#macos)
  * [Windows](#windows)
* [CM CLI testing](#cm-cli-testing)
* [CUDA installation](#cuda-installation)
* [CM customization](#cm-customization)
* [CM automation scripts](#cm-automation-scripts)
* [Running CM scripts via Docker](#running-cm-scripts-via-docker)

</details>


***Check our new [online installation GUI](https://access.cknowledge.org/playground/?action=install)***.


# CM installation




MLCommons Collective Mind framework requires minimal dependencies to run on any platform: `python 3+, pip, git, git-lfs, wget`.
However, most CM automation recipes shared by the community and MLCommons require Python 3.7+ .

***By default, CM will pull Git repositories and cache installations and downloaded files in your `$HOME/CM` directory (Linux/MacOS). 
   You can change it to any another directory using the `CM_REPOS` environment variable, for example `export CM_REPOS=/scratch/CM`.***

Here are typical installation procedures across different operating systems:

* [Ubuntu, Debian](#ubuntu-debian)
* [Red Hat](#red-hat)
* [MacOS](#macos)
* [Windows](#windows)

You can find some Docker containers for CM [here](../docker).

You can customize CM installation using environment variables described [here](#cm-customization).


You can reuse misc CM utils listed [here](#misc-cm-utils).

## Ubuntu, Debian


*We have successfully tested CM with the following system dependencies on Ubuntu 18.x, 20.x, 22.x , 23.x:*

```bash
sudo apt update && sudo apt upgrade

sudo apt install python3 python3-pip python3-venv git git-lfs wget curl
sudo apt install libgl1-mesa-dev
```

**Note that you must set up virtual env on Ubuntu 23+ before using any Python project:**
```bash
python3 -m venv cm
source cm/bin/activate
```

You can now install CM via PIP:

```bash
python3 -m pip install cmind
```

Note that you may need to restart your shell to update PATH to the "cm" binary. 
Alternatively you can run 

```bash
source $HOME/.profile
```

You can check that CM is available and print internal status as follows:

```bash
gfursin@mlcommons-ck-cm-dev:~$ cm test core

CM version: 2.3.0

Python executable used by CK: C:\!Progs\Python310\python.exe

Path to CM package:           C:\!Progs\Python310\lib\site-packages\cmind
Path to CM core module:       C:\!Progs\Python310\lib\site-packages\cmind\core.py
Path to CM internal repo:     C:\!Progs\Python310\lib\site-packages\cmind\repo

Path to CM repositories:      D:\Work1\CM

GitHub for CM developments:        https://github.com/mlcommons/ck/tree/master/cm
GitHub for CM automation scripts:  https://github.com/mlcommons/cm4mlops
Reporting issues and ideas:        https://github.com/mlcommons/ck/issues

```

You are ready to use CM automation meta-framework. 




## Red Hat

*We have successfully tested CM on Red Hat 9 and CentOS 8*

```bash
sudo dnf update

sudo dnf install python3 python-pip git git-lfs wget curl

python3 -m pip install cmind --user

```

## MacOS

*Note that CM currently does not work with Python installed from the Apple Store.
 Please install Python via brew as described below.*

If `brew` package manager is not installed, please install it as follows (see details [here](https://brew.sh/)):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Don't forget to add brew to PATH environment as described in the end.

Then install python, pip, git and wget:

```bash
brew install python3 git git-lfs wget curl

python3 -m pip install cmind
```

*Sometimes python does not add `cm` and `cmr` binaries to the `PATH` environment variable.
 You may need to find these files and add their path to `PATH` variable.
 We plan to simplify this installation in the future.*


## Windows

* Configure Windows 10+ to [support long paths](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry#enable-long-paths-in-windows-10-version-1607-and-later) from command line as admin:
  <small>
  <small>
  <small>
  ```bash
  reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem" /v LongPathsEnabled /t REG_DWORD /d 1 /f
  ```
  </small>
  </small>
  </small>
* Download and install Git from [git-for-windows.github.io](https://git-for-windows.github.io).
  * Configure Git to accept long file names: `git config --system core.longpaths true`
* Download and install Python 3+ from [www.python.org/downloads/windows](https://www.python.org/downloads/windows).
  * Don't forget to select option to add Python binaries to PATH environment!
  * Configure Windows to accept long fie names during Python installation!

* Install CM via PIP:

```bash
python -m pip install cmind
```

*Note that we [have reports](https://github.com/mlcommons/ck/issues/844) 
 that CM does not work when Python was first installed from the Microsoft Store.
 If CM fails to run, you can find a fix [here](https://stackoverflow.com/questions/57485491/python-python3-executes-in-command-prompt-but-does-not-run-correctly)*.


*We plan to provide a self-sustained package in the future to simplify CM installation on Windows.*


# CM CLI testing

If the installation is successful, you can run the CM CLI as follows:

```bash
gfursin@cmind:~$ cm

cm {action} {automation} {artifact(s)} {flags} @input.yaml @input.json
```

*Note that you may need to relogin to your shell to update the PATH to the CM CLI!*

You can also quickly test the installation and check the version as follows:
```bash
gfursin@mlcommons-ck-cm-dev:~$ cm test core

CM version: 1.5.0

Python executable used by CK: /usr/bin/python3

Path to CM package:         /home/user/.local/lib/python3.9/site-packages/cmind
Path to CM core module:     /home/user/.local/lib/python3.9/site-packages/cmind/core.py
Path to CM internal repo:   /home/user/.local/lib/python3.9/site-packages/cmind/repo

Path to CM repositories:    /home/user/CM

GitHub for CM developments:        https://github.com/mlcommons/ck/tree/master/cm
GitHub for CM automation scripts:  https://github.com/mlcommons/ck/tree/master/cm-mlops
Reporting issues and ideas:        https://github.com/mlcommons/ck/issues
Joining the open MLPerf workgroup: https://cKnowledge.org/mlcommons-taskforce
```

# CUDA installation

If you plan to use CUDA for your experiments, please follow [this guide](installation-cuda.md) 
to detect or install it and other related dependencies (cuDNN, TensorRT) using CM.

# CM customization

You can use the following environment variables to customize CM installation:

* `'CM_REPOS'` - change path to the CM repositories and *repos.json* file.

  By default, CM will keep CM repositories in:
  * `$HOME/CM` directory on Linux and MacOS
  * `%USERPROFILE%\CM` directory on Windows

* `'CM_CONFIG'` - provide full path to a JSON or YAML file with the CM configuration.
  The content of this file will be merged with the ["cfg" dictionary](https://github.com/mlcommons/ck/blob/master/cm/cmind/config.py#L23)
  from the *config.py*.

* `'CM_DEBUG'` - if set to 'yes', turn on internal CM debugging and raise errors 
  in CM automations instead of returning a dictionary with an error *{'return':ERROR CODE, 'error':'ERROR note'}*

* `'CM_HOME'` - change path to the CM python package with the default 'repo' directory.
  Useful to improve the default automations inside the CM package.

* `'CM_INDEX'` (*CM v1.3.0+*) - set to {off|no|false} to turn off CM indexing of all artifacts
  (when on, it speeds up artifact searching and execution of CM scripts by 10..50x)



# CM automation scripts

Please go [back to index](README.md) to continue learning about CM interface and scripts.

However, if you are already familiar with the CM/CK concepts, you can 
use these [CM automation scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script) 
for portable MLOps and DevOps from MLCommons directly by installing the following repository:
```bash
cm pull repo mlcommons@cm4mlops
```

You can switch to a development branch of this or any other CM repository as follows:

```bash
cm checkout repo mlcommons@cm4mlops --branch=dev
```

You can switch back to master branch as follows:

```bash
cm checkout repo mlcommons@cm4mlops --branch=master
```

If you plan to participate in our [reproducibility and optimization challenges](https://access.cknowledge.org/playground/?action=challenges),
we suggest you to create a fork of [github.com/mlcommons/ck](https://github.com/mlcommons/ck) and use it. 
In such case, you will be able to create PRs with your updates to the main repository.
If you already installed above repo, you will need delete it and install your fork as follows:

```bash
cm rm repo mlcommons@cm4mlops --all
cm pull repo --url={URL of the fork of github.com/mlcommons/ck}
```

If you want to use stable CM snapshots of reusable automation recipes (CM scripts), 
you can download a stable repository from Zenodo (~5MB):

```bash
cm rm repo mlcommons@cm4mlops --all
cm pull repo --url=https://zenodo.org/records/10787459/files/cm-mlops-repo-20240306.zip

```

You can pull repository and checkout a specific branch as follows:
```bash
cm rm repo mlcommons@cm4mlops --checkout=dev
cm pull repo --url=https://zenodo.org/records/10787459/files/cm-mlops-repo-20240306.zip
```

If you use CM scripts with Python outside containers, we suggest you to set up CM Python virtual
environment as described [here](../cm-mlops/automation/script/README-extra.md#using-python-virtual-environments).

Feel free to check [these CM tutorials](tutorials) to learn how to use CM to facilitate reproducible research,
run MLPerf out-of-the-box and accelerate technology transfer across rapidly evolving 
software, hardware, models and data.


# Running CM scripts via Docker

CM language allows users to run various automation workflows and applications in the same way either inside automatically generated container snapshots
or the latest software/hardware stacks (that may fail and then collaboratively improved by the community).

If you have Docker installed, you can run any CM script using Docker and stay in the container to continue running CM commands as follows:
```bash
cm docker script --tags=detect,os -j
```

You can see more examples of using CM with Docker containers in this [folder](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/build-docker-image/examples).

You can browse and reuse shared CM containers from cKnowledge and cTuning via [Docker hub](https://hub.docker.com/repositories/cknowledge).


# Problems

If you experience problems with CM installation, please report [here](https://github.com/mlcommons/ck/issues) 
or reach the community via [Discord server](https://discord.gg/JjWNWXKxwT) to help improve CM and the overall user experience!

