# Examples

First download images:

```bash
cmr "download file _wget" --url=https://cKnowledge.org/ai/data/data.pgm --ssl-verify=no --md5sum=0af279e557a8de252d7ff0751a999379
cmr "download file _wget" --url=https://cKnowledge.org/ai/data/computer_mouse.jpg --ssl-verify=no --md5sum=45ae5c940233892c2f860efdf0b66e7e
cmr "download file _wget" --url=https://cKnowledge.org/ai/data/computer_mouse2.jpg --ssl-verify=no --md5sum=e7e2050b41e0b85cedca3ca87ab55390
cmr "download file _wget" --url=https://cKnowledge.org/ai/data/computer_mouse2.pgm --ssl-verify=no --md5sum=a4e48556d3eb09402bfc98e375b41311
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

## Debugging scripts without CM

```bash
cmr "app image corner-detection" --debug_script_tags=compile,cpp-program
cmr "app image corner-detection" --debug-script-tags=benchmark,program
```

