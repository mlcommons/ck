**[ [TOC](../README.md) ]**

## Pull MLOps automation repo

```bash
ck pull repo:mlcommons@ck-mlops
```

## Plug CUDA into CK

You can detect already installed CUDA versions and automatically plug them to CK as follows:

```bash
ck detect soft --tags=compiler,cuda
```

Note that multiple versions of CUDA can coexist in CK. 
You can run the above command several times to register required versions

## Check registered versions

```bash
ck show env --tags=cuda
```

## Detect CUDA capabilities

```bash
ck detect platform.gpgpu --cuda
```

## Detect OpenCL capabilities

```bash
ck detect platform.gpgpu --opencl
```
