This script reproduces OctoML MLPerf TinyML Submission from v1.0. 
## Install 
```bash
cm run script --tags=reproduce,tiny,mlperf,octoml,_[VARIANT],_[MODEL]
```
where,
* `[VARIANT]` is one of `cmsis_nn`,`native`
* `[MODEL]` is one of `ad`, `ic`, `kws`, `vww`

The generated binary can be located inside
```bash
find `cm find cache --tags=reproduce,tiny,mlperf,octoml,_[VARIANT],_[MODEL]
```
