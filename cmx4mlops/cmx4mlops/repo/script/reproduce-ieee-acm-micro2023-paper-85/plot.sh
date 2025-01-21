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

#${container} run docker.io/hello-world


echo "==================  Build the Docker image to run the experiments =================="

#${container} build  -t ${image} -f "${CM_TMP_CURRENT_SCRIPT_PATH}/Dockerfile" .

echo "==================  Get All Results =================="

mkdir figures
##get all benchmarks
${container} run --rm -v $PWD/gpudata:/root/gpudata/ -v $PWD/figures:/root/figures/ ${image} /bin/bash -c "cd /root/artifact_evaluation/sampled-mgpu-sim/samples/sampledrunner;./testallbench.py -check;cd /root/artifact_evaluation/micro2023_figures/r9nano;./r9nano.py;./r9nanolevels.py;mv *.png /root/figures/;mv *.pdf /root/figures/"

##get all benchmarks with architecture mi100
${container} run --rm -v $PWD/gpudata:/root/gpudata/ -v $PWD/figures:/root/figures/ ${image} /bin/bash -c "cd /root/artifact_evaluation/sampled-mgpu-sim/samples/sampledrunner;./testallbench.py -arch=mi100 -check;cd /root/artifact_evaluation/micro2023_figures/mi100;./mi100.py;mv *.pdf /root/figures/;mv *.png /root/figures"
#
###vgg16
${container} run --rm -v $PWD/gpudata:/root/gpudata/ -v $PWD/figures:/root/figures/ ${image} /bin/bash -c "cd /root/artifact_evaluation/sampled-mgpu-sim/samples/sampledrunner;./testdlapps.py -bench=vgg16  -check;cd /root/artifact_evaluation/micro2023_figures/vgg16;./vgg16.py;./vgg16speedup.py;mv *.pdf /root/figures/;mv *.png /root/figures"
###vgg19
echo "Benchmarks    MGPUSim-Simtime    MGPUSim-Walltime    Photon-Simtime    Photon-Walltime"
${container} run --rm -v $PWD/gpudata:/root/gpudata/ -v $PWD/figures:/root/figures/ ${image} /bin/bash -c "cd /root/artifact_evaluation/sampled-mgpu-sim/samples/sampledrunner;./testdlapps.py -bench=vgg19  -check |grep Sum |awk -F Sum '{ printf \"vgg19\";print \$2}' "
###resnet18
${container} run --rm -v $PWD/gpudata:/root/gpudata/ -v $PWD/figures:/root/figures/ ${image} /bin/bash -c "cd /root/artifact_evaluation/sampled-mgpu-sim/samples/sampledrunner;./testdlapps.py -bench=resnet18 -check |grep Sum|awk -F Sum '{printf \"resnet18\";print \$2}'"
####resnet32
${container} run --rm -v $PWD/gpudata:/root/gpudata/ -v $PWD/figures:/root/figures/ ${image} /bin/bash -c "cd /root/artifact_evaluation/sampled-mgpu-sim/samples/sampledrunner;./testdlapps.py -bench=resnet32 -check |grep Sum|awk -F Sum '{printf \"resnet32\";print \$2}'"
####resnet50
${container} run --rm -v $PWD/gpudata:/root/gpudata/ -v $PWD/figures:/root/figures/ ${image} /bin/bash -c "cd /root/artifact_evaluation/sampled-mgpu-sim/samples/sampledrunner;./testdlapps.py -bench=resnet50 -check|grep Sum |awk -F Sum '{printf \"resnet50\";print \$2}'"
####resnet101
${container} run --rm -v $PWD/gpudata:/root/gpudata/ -v $PWD/figures:/root/figures/ ${image} /bin/bash -c "cd /root/artifact_evaluation/sampled-mgpu-sim/samples/sampledrunner;./testdlapps.py -bench=resnet101 -check|grep Sum|awk -F Sum '{printf \"resnet101\";print \$2}'"
####resnet152
${container} run --rm -v $PWD/gpudata:/root/gpudata/ -v $PWD/figures:/root/figures/ ${image} /bin/bash -c "cd /root/artifact_evaluation/sampled-mgpu-sim/samples/sampledrunner;./testdlapps.py -bench=resnet152 -check|grep Sum|awk -F Sum '{printf \"resnet152\";print \$2}'"
##
####
${container} run --rm -v $PWD/gpudata:/root/gpudata/ -v $PWD/figures:/root/figures/ ${image} /bin/bash -c "cd /root/artifact_evaluation/sampled-mgpu-sim/samples/sampledrunner;./testpagerank.py  -check|grep pagerank|grep -v __pagerank"
