FROM ubuntu:18.04
SHELL ["/bin/bash", "-c"]
ARG CM_GH_TOKEN
ARG CM_LOADGEN_MODE=accuracy
ARG CM_LOADGEN_SCENARIO=offline
ARG CM_TEST_QUERY_COUNT=10

# Notes: https://runnable.com/blog/9-common-dockerfile-mistakes
# Install system dependencies
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip git sudo wget

# Install python packages
RUN python3 -m pip install cmind requests

# Setup docker environment
ENTRYPOINT ["/bin/bash", "-c"]
ENV TZ=US/Pacific
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ >/etc/timezone

# Setup docker user
RUN groupadd cm
RUN useradd  -g cm --create-home --shell /bin/bash cmuser
RUN echo "cmuser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
USER cmuser:cm
WORKDIR /home/cmuser

# Download CM repo for scripts
RUN cm pull repo mlcommons@ck

# Install all system dependencies
RUN cm run script --quiet --tags=get,sys-utils-cm

# Run commands
# Install/customize individual CM components for MLPerf
#RUN cm run script --tags=get,generic-python-lib,_onnxruntime
#RUN cm run script --tags=get-ml-model,resnet50,_onnxruntime
#RUN cm run script --tags=get,dataset,preprocessed,imagenet

# Run CM workflow for MLPerf inference
RUN cm run script --tags=app,mlperf,inference,generic,reference,_resnet50,_onnxruntime,_cpu,_cpp --adr.compiler.tags=gcc --mode=$CM_LOADGEN_MODE --scenario=$CM_LOADGEN_SCENARIO --test_query_count=$CM_TEST_QUERY_COUNT
