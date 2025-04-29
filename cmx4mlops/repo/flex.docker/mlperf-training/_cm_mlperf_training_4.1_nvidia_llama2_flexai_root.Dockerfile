FROM nvcr.io/nvidia/pytorch:24.01-py3

LABEL github=""
LABEL maintainer=""
LABEL license=""

SHELL ["/bin/bash", "-c"]
ENTRYPOINT ["/bin/bash", "-c"]

RUN apt update -y
RUN apt install -y python3 python3-pip python3-venv git git-lfs wget curl

#ENV VIRTUAL_ENV=/opt/cmx
# Reuse system site packages
#RUN python3 -m venv $VIRTUAL_ENV --system-site-packages
#ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ARG CMX_REBUILD_HERE=1
RUN pip install cmind
RUN cmx pull repo mlcommons@ck --dir=cmx4mlops
