*Note that CM currently does not work with Python installed from the Apple Store.
 Please install Python via brew as described below.*

If `brew` package manager is not installed, please install it as follows (see details [here](https://brew.sh/)):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Don't forget to add brew to PATH environment as described in the end.

Then install python, pip, git and wget:

```bash
brew install python3 git wget curl

python3 -m pip install cmind
```

*Sometimes python does not add `cm` and `cmr` binaries to the `PATH` environment variable.
 You may need to find these files and add their path to `PATH` variable.
 We plan to simplify this installation in the future.*

