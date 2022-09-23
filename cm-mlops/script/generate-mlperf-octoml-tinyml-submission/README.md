This is a wrapper script to [Reproduce MLPerf OctoML TinyML Results](https://github.com/octoml/ck/tree/master/cm-mlops/script/reproduce-mlperf-octoml-tinyml-results)
which runs the script for the two microtvm variants and their supported models.

## Install
```
cm run script --tags=generate,tiny,submission
```

The above command should produce five elf binaries which can be located inside the respective cache entries given by the below command
```
cm find cache --tags=reproduce,tiny,octoml,mlperf
```

## Install and Flash
```
cm run script --tags=generate,tiny,submission --flash
```
