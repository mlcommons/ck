FROM {{docker_base_image}}

LABEL github="{{docker_github}}"
LABEL maintainer="{{docker_maintainer}}"
LABEL license="{{docker_license}}"

SHELL ["/bin/bash", "-c"]
ENTRYPOINT ["/bin/bash", "-c"]

RUN apt update -y
RUN apt install -y python3 python3-pip python3-venv git git-lfs wget curl
