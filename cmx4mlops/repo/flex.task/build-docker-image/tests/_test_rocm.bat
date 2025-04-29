docker run --rm -it  --device /dev/kfd --device /dev/dri --init  --net=host --uts=host --ipc=host --security-opt=seccomp=unconfined localhost/cmx  /bin/bash
