
# Getting Started with CM Script Automation

## Running CM Scripts

To execute a simple script in CM that captures OS details, use the following command:

```bash
cm run script --tags=detect,os -j
```

This command gathers details about the system on which it's run, such as:

```json
{
    "CM_HOST_OS_TYPE": "linux",
    "CM_HOST_OS_BITS": "64",
    "CM_HOST_OS_FLAVOR": "ubuntu",
    "CM_HOST_OS_FLAVOR_LIKE": "debian",
    "CM_HOST_OS_VERSION": "24.04",
    "CM_HOST_OS_KERNEL_VERSION": "6.8.0-45-generic",
    "CM_HOST_OS_GLIBC_VERSION": "2.39",
    "CM_HOST_OS_MACHINE": "x86_64",
    "CM_HOST_OS_PACKAGE_MANAGER": "apt",
    "CM_HOST_OS_PACKAGE_MANAGER_INSTALL_CMD": "DEBIAN_FRONTEND=noninteractive apt-get install -y",
    "CM_HOST_OS_PACKAGE_MANAGER_UPDATE_CMD": "apt-get update -y",
    "+CM_HOST_OS_DEFAULT_LIBRARY_PATH": [
      "/usr/local/lib/x86_64-linux-gnu",
      "/lib/x86_64-linux-gnu",
      "/usr/lib/x86_64-linux-gnu",
      "/usr/lib/x86_64-linux-gnu64",
      "/usr/local/lib64",
      "/lib64",
      "/usr/lib64",
      "/usr/local/lib",
      "/lib",
      "/usr/lib",
      "/usr/x86_64-linux-gnu/lib64",
      "/usr/x86_64-linux-gnu/lib"
    ],
    "CM_HOST_PLATFORM_FLAVOR": "x86_64",
    "CM_HOST_PYTHON_BITS": "64",
    "CM_HOST_SYSTEM_NAME": "intel-spr-i9"
}
```

For more details on CM scripts, see the [CM documentation](index.md).

### Adding New CM Scripts

CM aims to provide lightweight connectors between existing automation scripts and tools without substituting them. You can add your own scripts to CM with the following command, which creates a script named `hello-world`:

```bash
cm add script hello-world --tags=hello-world,display,test
```

This command initializes a CM script in the local repository with the following structure:

```
└── CM
    ├── index.json
    ├── repos
    │   ├── local
    │   │   ├── cfg
    │   │   ├── cache
    │   │   ├── cmr.yaml
    │   │   └── script
    │   │       └── hello-world
    │   │           ├── _cm.yaml
    │   │           ├── customize.py
    │   │           ├── README-extra.md
    │   │           ├── run.bat
    │   │           └── run.sh
    │   └── mlcommons@cm4mlops
    └── repos.json
```

You can also execute the script from Python as follows:

```python
import cmind
output = cmind.access({'action':'run', 'automation':'script', 'tags':'hello-world,display,test'})
if output['return'] == 0:
    print(output)
```

If you discover that your new script is similar to an existing script in any CM repository, you can clone an existing script using the following command:

```bash
cm copy script <source_script> .:<target_script>
```

Here, `<source_script>` is the name of the existing script, and `<target_script>` is the name of the new script you're creating. Existing script names in the `cm4mlops` repository can be found [here](https://github.com/mlcommons/cm4mlops/tree/mlperf-inference/script).

## Caching and Reusing CM Script Outputs

By default, CM scripts run in the current directory and record all new files there. For example, a universal download script might download an image to the current directory:

```bash
cm run script --tags=download,file,_wget --url=https://cKnowledge.org/ai/data/computer_mouse.jpg --verify=no --env.CM_DOWNLOAD_CHECKSUM=45ae5c940233892c2f860efdf0b66e7e
```

To cache and reuse the output of scripts, CM offers a `cache` automation feature similar to `script`. When `"cache":true` is specified in a script's metadata, CM will create a `cache` directory in `$HOME/CM/repos/local` with a unique ID and the same tags as `script`, and execute the script there.

Subsequent executions of the same script will reuse files from the cache, avoiding redundancy. This is especially useful for large files or data sets.

You can manage cache entries and find specific ones using commands like:

```bash
cm show cache
cm show cache --tags=get,ml-model,resnet50,_onnx
cm find cache --tags=download,file,ml-model,resnet50,_onnx
cm info cache --tags=download,file,ml-model,resnet50,_onnx
```

To clean cache entries:

```bash
cm rm cache --tags=ml-model,resnet50
cm rm cache -f  # Clean all entries
```

You can completely reset the CM framework by removing the `$HOME/CM` directory, which deletes all downloaded repositories and cached entries.

## Integration with Containers

CM scripts are designed to run natively or inside containers with the same commands. You can substitute `cm run script` with `cm docker script` to execute a script inside an automatically-generated container:

```bash
cm docker script --tags=python,app,image-classification,onnx,_cpu
```

CM automatically handles the generation of Dockerfiles, building of containers, and execution within containers, providing a seamless experience whether running scripts natively or in containers. 

This approach simplifies the development process by eliminating the need for separate Dockerfile maintenance and allows for the use of native scripts and workflows directly within containers.
