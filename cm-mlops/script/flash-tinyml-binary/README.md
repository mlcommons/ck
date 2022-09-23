This script flashes the ELF binary using Zephyr. 
## Install 
```bash
cm run script --tags=flash,tiny --build_dir=[BUILD_DIR]
```
where,
* `[BUILD_DIR]` is the build folder containing the zephyr folder which in turn contains the built ELF binary
