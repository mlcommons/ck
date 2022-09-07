This script runs a docker container and launces the given CM script inside it. 
If the container image is not existing, corresponding build is initiated via CM dependencies.

## How to Run
```bash
cm run script \
--tags=run,docker,container
```
### Options
1. `--env.CM_DOCKER_RUN_SCRIPT_TAGS`: Script tags for the script to be run inside the docker container. Default is to print `cm version`
2. `--env.CM_MLOPS_REPO=octoml@ck`: To use a different repo for CM scripts like "octoml@ck". Default is `mlcommons@ck`
3. `--env.CM_DOCKER_IMAGE_BASE="ubuntu:22.04"`: Specify the base image for Dockerfile, default is "ubuntu:20.04" 
4. `--env.CM_DOCKER_IMAGE_RECREATE=yes`: To recreate docker image even when existing. Default is no recreate
5. `--add_deps_recursive.build-docker-image.tags=_cache`: To use build cache for docker image build. Default is to use `--no-cache`
