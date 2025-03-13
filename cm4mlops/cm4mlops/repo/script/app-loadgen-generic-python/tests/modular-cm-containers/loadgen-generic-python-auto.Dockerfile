FROM ubuntu:20.04
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
ENV PATH=${PATH}:$HOME/.local/bin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ >/etc/timezone

# Setup docker user
RUN groupadd cm
RUN useradd  -g cm --create-home --shell /bin/bash cmuser
RUN echo "cmuser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
USER cmuser:cm
WORKDIR /home/cmuser

# Download CM repo for scripts
RUN cm pull repo ctuning@mlcommons-ck

# Install all system dependencies
RUN cm run script --quiet --tags=get,sys-utils-cm

# Run commands
RUN cm run script --quiet --tags=python,app,loadgen-generic,_onnxruntime,_resnet50 --fake_run 
