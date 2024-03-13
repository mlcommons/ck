* Configure Windows 10+ to [support long paths](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry#enable-long-paths-in-windows-10-version-1607-and-later) from command line as admin:
  ```bash
  reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem" /v LongPathsEnabled /t REG_DWORD /d 1 /f
  ```
* Download and install Git from [git-for-windows.github.io](https://git-for-windows.github.io).
  * Configure Git to accept long file names: `git config --system core.longpaths true`
* Download and install Python 3+ from [www.python.org/downloads/windows](https://www.python.org/downloads/windows).
  * Don't forget to select option to add Python binaries to PATH environment!
  * Configure Windows to accept long fie names during Python installation!

*Note that we [have reports](https://github.com/mlcommons/ck/issues/844) 
 that CM does not work when Python was first installed from the Microsoft Store.
 If CM fails to run, you can find a fix [here](https://stackoverflow.com/questions/57485491/python-python3-executes-in-command-prompt-but-does-not-run-correctly)*.

*We plan to provide a self-sustained package in the future to simplify CM installation on Windows.*
