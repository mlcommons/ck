This script runs a docker container and launces the given CM script inside it. 
If the container image is not existing, corresponding build is initiated via CM dependencies.

## How to Run
```bash
cm run script \
--tags=run,docker,container
```
### Options
1. `--env.CM_DOCKER_RUN_SCRIPT_TAGS`: Script tags for the script to be run inside the docker container
2. `--env.CM_MLOPS_REPO=octoml@ck`: To use a different repo for CM scripts like "octoml@ck"
3. `--add_deps_recursive.build-docker-image.tags=_cache`: To use build cache for docker image build
