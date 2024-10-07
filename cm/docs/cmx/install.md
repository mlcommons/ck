[ [Back to index](README.md) ]

# CM Installation

CM framework requires minimal dependencies to run on any platform: `python 3.7+, pip, venv, git, git-lfs, wget, curl`.

By default, CM will pull Git repositories and cache installations and downloaded files in your `$HOME/CM` directory on Linux and MacOS
or `%userprofile%\CM` directory on Windows.
You can change it to any another directory using the `CM_REPOS` environment variable, for example `export CM_REPOS=/scratch/CM`.

*Feel free to use the [online installation GUI](https://access.cknowledge.org/playground/?action=install-cmx)*.


## Ubuntu, Debian

*We have successfully tested CMX with the following system dependencies on Ubuntu 20.x, 22.x , 24.x:*

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv git git-lfs wget curl

python3 -m venv cm
source cm/bin/activate

python3 -m pip install cmind
```

Note that you may need to restart your shell to update PATH to the "cmx" binary. 

Alternatively you can run 

```bash
source $HOME/.profile
```

You can check that CMX works using the following command:
```bash
cmx test core
```



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
gfursin@cmind:~$ cmx

cmx {action} {automation} {artifact(s)} {flags} @input.yaml @input.json
```

