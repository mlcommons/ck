# Examples

First download images:

```bash
cmr "download file _wget" --url=https://cKnowledge.org/ai/data/data.pgm --verify=no --env.CM_DOWNLOAD_CHECKSUM=0af279e557a8de252d7ff0751a999379
cmr "download file _wget" --url=https://cKnowledge.org/ai/data/computer_mouse.jpg --verify=no --env.CM_DOWNLOAD_CHECKSUM=45ae5c940233892c2f860efdf0b66e7e
cmr "download file _wget" --url=https://cKnowledge.org/ai/data/computer_mouse2.jpg --verify=no --env.CM_DOWNLOAD_CHECKSUM=e7e2050b41e0b85cedca3ca87ab55390
cmr "download file _wget" --url=https://cKnowledge.org/ai/data/computer_mouse2.pgm --verify=no --env.CM_DOWNLOAD_CHECKSUM=a4e48556d3eb09402bfc98e375b41311
```

Then run app

```bash
cm run script "app image corner-detection"
cm run script "app image corner-detection" -add_deps_recursive.compiler.tags=llvm
cm run script "app image corner-detection" -add_deps_recursive.compiler.tags=gcc
cm run script "app image corner-detection" -add_deps_recursive.compiler.tags=llvm --add_deps_recursive.compiler.version_min=11.0.0 --add_deps_recursive.compiler.version_max=13.0.0
```

## Reproducibility matrix

* Ubuntu 22.04; x64; LLVM 17.06
* Windows 11; x64; LLVM 17.06

