FROM registry.access.redhat.com/ubi9
SHELL ["/bin/bash", "-c"]
RUN dnf update
RUN dnf install -y python3 python-pip git wget sudo
RUN python3 -m pip install cmind requests
ENTRYPOINT ["/bin/bash", "-c"]
ENV TZ=US/Pacific
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ >/etc/timezone
RUN groupadd cm
RUN useradd  -g cm --create-home --shell ["/bin/bash", "-c"] cmuser
RUN echo "cmuser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
USER cmuser:cm
WORKDIR /home/cmuser
RUN cm pull repo mlcommons@ck
RUN cm run script --quiet --tags=get,sys-utils-cm
RUN cm version
