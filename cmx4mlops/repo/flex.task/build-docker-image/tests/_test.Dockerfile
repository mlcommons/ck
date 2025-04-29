FROM ubuntu:24.04

LABEL github=""
LABEL maintainer="Grigori Fursin"
LABEL license=""

SHELL ["/bin/bash", "-c"]

# Notes: https://runnable.com/blog/9-common-dockerfile-mistakes
# Install system dependencies for CMX
# https://access.cknowledge.org/playground/?action=install

# Setup docker environment
ENTRYPOINT ["/bin/bash", "-c"]
ENV TZ="US/Pacific"
ENV PATH="${PATH}:/home/cmuser/.local/bin"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ >/etc/timezone

RUN apt update -y
RUN apt install -y python3 python3-pip python3-venv git git-lfs wget curl
