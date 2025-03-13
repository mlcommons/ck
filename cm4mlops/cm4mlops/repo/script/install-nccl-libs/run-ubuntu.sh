CM_SUDO=${CM_SUDO:-sudo}
${CM_SUDO} apt install -y --allow-downgrades libnccl2=2.18.3-1+cuda${CM_CUDA_VERSION} libnccl-dev=2.18.3-1+cuda${CM_CUDA_VERSION}
