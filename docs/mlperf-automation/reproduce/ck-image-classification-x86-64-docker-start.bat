rem ck add repo:ck-experiments --quiet

FOR /F "tokens=*" %%a in ('ck where repo:ck-experiments') do SET CK_HOST_REPO_EXPERIMENTS=%%a

echo %CK_HOST_REPO_EXPERIMENTS%

set CK_LOCAL_DOCKER_SCRIPT=ck-image-classification-x86-64-docker-helper.sh
set CK_HOST_RUN_SCRIPT=%cd%\%CK_LOCAL_DOCKER_SCRIPT%
set CK_HOST_DATASETS=X:\datasets

docker run ^
       --volume %CK_HOST_REPO_EXPERIMENTS%:/home/ckuser/ck-experiments ^
       --volume %CK_HOST_RUN_SCRIPT%:/home/ckuser/%CK_LOCAL_DOCKER_SCRIPT% ^
       -it mlcommons/ck-mlperf-inference-v1.0-image-classification-small-imagenet-fcbc9a7708491791:ubuntu-20.04 ^
       "./%CK_LOCAL_DOCKER_SCRIPT%"
