**[ [TOC](../README.md) ]**

# Upgrade the CK framework

If you have CK installed, you can update it and all related CK repositories as follows:
```
python3 -m pip install ck -U
```

# Update all CK components

You can update all installed CK components from Git repositories at any time as follows:
```
ck pull all
```

# Install CK for the first time

Install [CK](https://github.com/mlcommons/ck) and dependencies as described [here](https://ck.readthedocs.io/en/latest/src/installation.html):

```
pip3 install ck
```
or 
```
python3 -m pip install ck
```
or
```
pip3 install ck
```

Check that ck CLI is available:
```
fursin@rpi4:~$ ck

CK version: 1.55.12

Python executable used by CK: /home/fursin/.pyenv/versions/3.7.6/bin/python3.7

Python version used by CK: 3.7.6 (default, Mar  9 2021, 04:42:58)
   [GCC 7.5.0]

Path to the default repo: /home/fursin/.pyenv/versions/3.7.6/lib/python3.7/site-packages/ck/repo
Path to the local repo:   /home/fursin/CK/local/venv/ck-octoml-amd/CK/local
Path to CK repositories:  /home/fursin/CK/local/venv/ck-octoml-amd/CK

Documentation:        https://github.com/mlcommons/ck/wiki
CK Google group:      https://bit.ly/ck-google-group
CK Slack channel:     https://cKnowledge.org/join-slack
Stable CK components: https://cknow.io
```

Sometimes you may need to add "~.local/bin/ck" to your PATH or restart your shell.

