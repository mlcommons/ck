# Modular container with the MLCommons CM automation meta-framework

# Preparing OS
ARG cm_os_name="ubuntu"
ARG cm_os_version="22.04"

FROM ${cm_os_name}:${cm_os_version}

# Maintained by the MLCommons taskforce on education and reproducibility
LABEL github="https://github.com/mlcommons/ck"
LABEL maintainer="https://bit.ly/mlperf-edu-wg"

# Customization
ARG CM_GH_TOKEN

# Prepare shell and entry point
SHELL ["/bin/bash", "-c"]
ENTRYPOINT ["/bin/bash", "-c"]

# Install system dependencies
# Notes: https://runnable.com/blog/9-common-dockerfile-mistakes
RUN apt-get update -y
RUN apt-get install -y lsb-release
RUN apt-get install -y python3 python3-pip git wget sudo

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
RUN lsb_release -a > sys-version-os.log
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
RUN cm run script "get python3" --version=${cm_python_version}

# Build MLPerf loadgen (official with correct seed for submission)
ARG cm_mlperf_inference_loadgen_version=""
RUN cm run script "get mlperf loadgen" --adr.compiler.tags=gcc --version=${cm_mlperf_inference_loadgen_version} --adr.inference-src-loadgen.version=${cm_mlperf_inference_loadgen_version} -v

# Install MLPerf inference source (can be private development branch)
ARG cm_mlperf_inference_src_tags=""
ARG cm_mlperf_inference_src_version=""
RUN cm run script "get mlperf inference src ${cm_mlperf_inference_src_tags}" --version=${cm_mlperf_inference_src_version} -v

# Install ML engine
ARG cm_ml_engine=onnxruntime
ARG cm_ml_engine_version=
ARG cm_ml_model=resnet50
ARG cm_mlperf_implementation=python

# Get MLPerf inference deps for model and a dataset
RUN cm run script --tags=app,mlperf,inference,generic,reference,_${cm_mlperf_implementation},_${cm_ml_engine},_${cm_ml_model},_cpu, --adr.compiler.tags=gcc --fake_run --quiet -v

# Test MLPerf inference
RUN cm run script --tags=app,mlperf,inference,generic,reference,_${cm_mlperf_implementation},_${cm_ml_engine},_${cm_ml_model},_cpu, --adr.compiler.tags=gcc -v

# CMD entry point
CMD /bin/bash
