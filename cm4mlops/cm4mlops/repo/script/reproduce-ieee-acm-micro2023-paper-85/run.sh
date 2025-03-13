#!/bin/bash

CUR_DIR=${PWD}

echo ""
echo "Current execution path: ${CUR_DIR}"
echo "Path to script: ${CM_TMP_CURRENT_SCRIPT_PATH}"



print_colorful_text() {
  local text="$1"
  local color_code="$2"
  echo "\e[${color_code}m${text}\e[0m"
}

container="docker"
image="micro2023-photon"
 
echo "==================  Run a container test to make sure container works =================="

${container} run docker.io/hello-world


echo "==================  Build the Docker image to run the experiments =================="

${container} build  -t ${image} -f "${CM_TMP_CURRENT_SCRIPT_PATH}/Dockerfile" .

echo "==================  Execute all benchmarks =================="
mkdir gpudata
##run all benchmarks
${container} run --rm -v $PWD/gpudata:/root/gpudata/ ${image} /bin/bash -c "cd /root/artifact_evaluation/sampled-mgpu-sim/samples/sampledrunner;./testallbench.py"

##run all benchmarks with architecture mi100
${container} run --rm -v $PWD/gpudata:/root/gpudata/ ${image} /bin/bash -c "cd /root/artifact_evaluation/sampled-mgpu-sim/samples/sampledrunner;./testallbench.py -arch=mi100"

##vgg16
${container} run --rm -v $PWD/gpudata:/root/gpudata/ ${image} /bin/bash -c "cd /root/artifact_evaluation/sampled-mgpu-sim/samples/sampledrunner;./testdlapps.py -bench=vgg16"
##vgg19
${container} run --rm -v $PWD/gpudata:/root/gpudata/ ${image} /bin/bash -c "cd /root/artifact_evaluation/sampled-mgpu-sim/samples/sampledrunner;./testdlapps.py -bench=vgg19"
##resnet18
${container} run --rm -v $PWD/gpudata:/root/gpudata/ ${image} /bin/bash -c "cd /root/artifact_evaluation/sampled-mgpu-sim/samples/sampledrunner;./testdlapps.py -bench=resnet18"
##resnet32
${container} run --rm -v $PWD/gpudata:/root/gpudata/ ${image} /bin/bash -c "cd /root/artifact_evaluation/sampled-mgpu-sim/samples/sampledrunner;./testdlapps.py -bench=resnet32"
##resnet50
${container} run --rm -v $PWD/gpudata:/root/gpudata/ ${image} /bin/bash -c "cd /root/artifact_evaluation/sampled-mgpu-sim/samples/sampledrunner;./testdlapps.py -bench=resnet50"
##resnet101
${container} run --rm -v $PWD/gpudata:/root/gpudata/ ${image} /bin/bash -c "cd /root/artifact_evaluation/sampled-mgpu-sim/samples/sampledrunner;./testdlapps.py -bench=resnet101"
##resnet152
${container} run --rm -v $PWD/gpudata:/root/gpudata/ ${image} /bin/bash -c "cd /root/artifact_evaluation/sampled-mgpu-sim/samples/sampledrunner;./testdlapps.py -bench=resnet152"
##pagerank
${container} run --rm -v $PWD/gpudata:/root/gpudata/ ${image} /bin/bash -c "cd /root/artifact_evaluation/sampled-mgpu-sim/samples/sampledrunner;./testpagerank.py"


