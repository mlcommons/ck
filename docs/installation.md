[ [Back to index](README.md) ]

<details>
<summary>Click here to see the table of contents.</summary>

* [CM installation](#cm-installation)
  * [Ubuntu, Debian](#ubuntu-debian)
  * [Red Hat](#red-hat)
  * [MacOS](#macos)
  * [Windows](#windows)
* [CM CLI testing](#cm-cli-testing)
* [CM customization](#cm-customization)
* [CM automation scripts](#cm-automation-scripts)

</details>

# CM installation

The CM tool requires minimal dependencies to run on any platform: `python 3+, pip, git, wget`.

Here are typical installation procedures across different operating systems:

* [Ubuntu, Debian](#ubuntu-debian)
* [Red Hat](#red-hat)
* [MacOS](#macos)
* [Windows](#windows)

You can find some Docker containers for CM [here](../docker).

You can customize CM installation using environment variables described [here](#cm-customization).

You can reuse misc CM utils listed [here](#misc-cm-utils).

## Ubuntu, Debian

*We have successfully tested CM on Ubuntu 18.x, 20.x, 22.x:*

```bash
sudo apt update && sudo apt upgrade

sudo apt install python3 python3-pip python3-venv git wget

python3 -m pip install cmind
```

Note that you may need to restart your shell to update PATH to the "cm" binary. 
Alternatively you can run 

```bash
source $HOME/.profile
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
  * Configure Git to accept long file names: `git config --system core.longpaths true`
* Download and install Python 3+ from [www.python.org/downloads/windows](https://www.python.org/downloads/windows).
  * Configure Windows to accept long fie names during Python installation!
* Install CM via PIP:

```bash
python -m pip install cmind
```



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

CM version: 1.2.1

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

* `'CM_INDEX'` (*CM v1.2.0+*) - set to {on|yes|true} to turn on CM indexing of all artifacts
  to speed up search and scripts by 10..50x.



# CM automation scripts

You can use [CM automation scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script) 
for portable MLOps and DevOps from MLCommons by installing the following repository:
```bash
cm pull repo mlcommons@ck
```

If you use CM scripts with Python outside containers, we suggest you to set up CM Python virtual
environment as described [here](../cm-mlops/automation/script/README-extra.md#using-python-virtual-environments).
