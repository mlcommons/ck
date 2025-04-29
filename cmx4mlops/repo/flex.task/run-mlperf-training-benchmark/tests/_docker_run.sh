docker run --rm -it --gpus all --init \
    --net=host --uts=host --ipc=host --security-opt=seccomp=unconfined \
    --volume=/persistent_storage/mlperf-assets:/artifacts \
    localhost/cmx-mlperf-training /bin/bash
