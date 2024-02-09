This CM script allows you to add and select multiple target devices.


## Add new target

### Host CPU as a target (default)

```bash
cmr "get target device"
```

### CUDA as a target

```bash
cmr "get target device _cuda"
```

Change name:

```bash
cmr "get target device _cuda" --name=my-cuda-11.7-benchmark
```

## See available targets in cache

```bash
cm show cache "get target device"
```

## Get ENV and state of a target device

```bash
cmr "get target device" -j
```
