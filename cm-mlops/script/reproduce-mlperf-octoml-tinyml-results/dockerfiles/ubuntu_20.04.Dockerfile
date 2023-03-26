FROM ubuntu:20.04
SHELL ["/bin/bash", "-c"]
ARG CM_GH_TOKEN
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip git sudo wget
RUN python3 -m pip install cmind requests
ENTRYPOINT ["/bin/bash", "-c"]
ENV TZ=US/Pacific
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ >/etc/timezone
RUN groupadd cm
RUN useradd  -g cm --create-home --shell /bin/bash cmuser
RUN echo "cmuser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
USER cmuser:cm
WORKDIR /home/cmuser
RUN cm pull repo ctuning@mlcommons-ck
RUN cm run script --quiet --tags=get,sys-utils-cm
RUN cm run script --quiet --tags=reproduce,tiny,octoml --env.CM_GH_TOKEN=$CM_GH_TOKEN
