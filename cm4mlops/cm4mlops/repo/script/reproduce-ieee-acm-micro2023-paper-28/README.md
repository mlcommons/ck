# CM script to run and reproduce experiments

Original repository: https://github.com/neel-patel-1/XFM_MICRO2023.git

### Reusability using MLCommons CM automation language

Install MLCommmons CM using [this guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md).

Install reusable MLCommons automations: 

```bash
cm pull repo mlcommons@ck
```

Install this repository with CM interface for reproduced experiments:
```bash
cm pull repo ctuning@cm4research
```

### Regenerate Figures via CM interface

1) Install deps:
```bash
cmr "reproduce project micro-2023 xfm _install_deps"
```

2) Run experiments:

```bash
cmr "reproduce project micro-2023 xfm _run" 
```

3) Plot results:

```bash
cmr "reproduce project micro-2023 xfm _plot"
```

You should find `XFM_Access_Distribution.png` and `results.csv` in the `results` folder current directory.

### Regenerate SPEC Workloads Experiments via CM Interface

* if hosted SPEC 2017 for artifact evaluation purposes is no longer available, provide path to a local install of SPEC:

1) (Optional) Provide path to local SPEC2017 .iso file
```bash
# if local spec is available, run below to avoid fetching remote SPEC, otherwise skip this step
cmr "download file _url.https://spec2017iso.s3.us-east-2.amazonaws.com/cpu2017-1_0_5.iso" --local_path=/path/to/local/cpu2017-1_0_5.iso
```

1) Install deps:
```bash
cmr "reproduce project micro-2023 xfm _install_spec_deps"
```

2) run:
```bash
cmr "reproduce project micro-2023 xfm _run_spec"
```

You should find `results.txt` in the `results` folder of current directory.