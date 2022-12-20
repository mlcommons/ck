export CK_HOST_REPO_EXPERIMENTS=`ck where repo:ck-experiments`

echo ${CK_HOST_REPO_EXPERIMENTS}

export CK_LOCAL_DOCKER_SCRIPT=ck-image-classification-x86-64-docker-helper.sh
export CK_HOST_RUN_SCRIPT=$PWD/${CK_LOCAL_DOCKER_SCRIPT}
export CK_HOST_DATASETS=~/datasets

docker run \
       --volume ${CK_HOST_REPO_EXPERIMENTS}:/home/ckuser/ck-experiments \
       --volume ${CK_HOST_RUN_SCRIPT}:/home/ckuser/${CK_LOCAL_DOCKER_SCRIPT} \
       -it mlcommons/ck-mlperf-inference-v1.0-image-classification-small-imagenet-fcbc9a7708491791:ubuntu-20.04 \
       "./${CK_LOCAL_DOCKER_SCRIPT}"
