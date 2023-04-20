# Modular container with the MLCommons CM automation meta-framework

# Preparing OS
ARG cm_os_name="rhel"
ARG cm_os_version="9"

FROM registry.access.redhat.com/ubi${cm_os_version}

# Maintained by the MLCommons taskforce on automation and reproducibility
LABEL github="https://github.com/mlcommons/ck"
LABEL maintainer="https://cKnowledge.org/mlcommons-taskforce"

# Customization
ARG CM_GH_TOKEN

# Prepare shell and entry point
SHELL ["/bin/bash", "-c"]
ENTRYPOINT ["/bin/bash", "-c"]

# Install system dependencies
# Notes: https://runnable.com/blog/9-common-dockerfile-mistakes
RUN dnf update -y
RUN dnf install -y python3 python3-pip git wget sudo binutils

# Extra python deps
RUN python3 -m pip install requests

# CM version
ARG cm_version=""
ENV CM_VERSION="${cm_version}"
RUN if [ "${CM_VERSION}" != "" ] ; then \
      python3 -m pip install cmind==${CM_VERSION} ; \
    else \
      python3 -m pip install cmind ; \
    fi

# Setup docker environment
ENTRYPOINT ["/bin/bash", "-c"]
ENV TZ=US/Pacific
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ >/etc/timezone

# Setup docker user
# See example in https://github.com/mlcommons/GaNDLF/blob/master/Dockerfile-CPU
RUN groupadd --gid 10001 cm
RUN useradd  --uid 10000 -g cm --create-home --shell /bin/bash cmuser
RUN echo "cmuser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

USER cmuser:cm
WORKDIR /home/cmuser

# Check CM installation
RUN cat /etc/redhat-release > sys-version-os.log
RUN uname -a > sys-version-kernel.log
RUN python3 --version > sys-version-python3.log
RUN cm version > sys-version-cm.log

# Get CM automation repository
ARG cm_automation_repo="mlcommons@ck"
ARG cm_automation_repo_checkout=""
ENV CM_AUTOMATION_REPO=${cm_automation_repo}
ENV CM_AUTOMATION_REPO_CHECKOUT=${cm_automation_repo_checkout}
RUN echo ${CM_AUTOMATION_REPO}
RUN cm pull repo ${CM_AUTOMATION_REPO} --checkout=${CM_AUTOMATION_REPO_CHECKOUT}

# Install CM system dependencies
RUN cm run script "get sys-utils-cm" --quiet

# Detect/install python
ARG cm_python_version=""
ENV CM_PYTHON_VERSION=${cm_python_version}
RUN cm run script "get python3" --version=${CM_PYTHON_VERSION}

# CMD entry point
CMD /bin/bash
