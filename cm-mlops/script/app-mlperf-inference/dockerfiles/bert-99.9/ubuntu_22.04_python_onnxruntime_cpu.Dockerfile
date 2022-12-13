FROM ubuntu:22.04
SHELL ["/bin/bash", "-c"]
ARG CM_GH_TOKEN

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
#RUN cm run script --tags=detect,os
#RUN cm run script --tags=detect,cpu
#RUN cm run script --tags=get,sys-utils-cm
#RUN cm run script --tags=get,python
#RUN cm run script --tags=get,generic-python-lib,_onnxruntime
#RUN cm run script --tags=get,generic-python-lib,_torch
#RUN cm run script --tags=get,generic-python-lib,_transformers
#RUN cm run script --tags=get,loadgen
#RUN cm run script --tags=get,mlcommons,inference,src,_deeplearningexamples,_octoml
#RUN cm run script --tags=get,sut,configs
#RUN cm run script --tags=get,dataset,squad,original
#RUN cm run script --tags=get,ml-model,language-processing,bert,_onnx-fp32
#RUN cm run script --tags=get,generic-python-lib,_tokenization

# Run CM workflow for MLPerf inference
RUN cm run script --tags=app,mlperf,inference,generic,_bert-99.9,_onnxruntime,_cpu,_python --adr.compiler.tags=gcc --adr.inference-src.tags=_octoml --fake_run 
RUN cm run script --tags=app,mlperf,inference,generic,_bert-99.9,_onnxruntime,_cpu,_python --adr.compiler.tags=gcc --adr.inference-src.tags=_octoml 
