This script flashes the ELF binary using Zephyr. 
## Install 
```bash
cm run script --tags=flash,tiny,_[VARIANT],_[MODEL]
```
where,
* `[VARIANT]` is one of `cmsis_nn`,`native`
* `[MODEL]` is one of `ad`, `ic`, `kws`, `vww`

We can also pass a known build directory like here:

```bash
cm run script --tags=flash,tiny --build_dir=[BUILD_DIR]
```
where,
* `[BUILD_DIR]` is the build folder containing the zephyr folder which in turn contains the built ELF binary
