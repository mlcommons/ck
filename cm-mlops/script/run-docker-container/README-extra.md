This script runs a docker container and launces the given CM script inside it. 
If the container image is not existing, corresponding build is initiated via CM dependencies.

## How to Run
```bash
cm run script \
--tags=run,docker,container
```
### Options
1. `--script_tags="get,gcc"`: Script tags for the CM script to be run inside the docker container. 
    If this is not set the cm command run inside the docker container is `cm version`
2. `--cm_repo=ctuning@mlcommons-ck`: To use a different repo for CM scripts like "ctuning@mlcommons-ck". Default: `mlcommons@ck`
3. `--base="ubuntu:22.04"`: Specify the base image for Dockerfile. Default: "ubuntu:20.04" 
4. `--recreate=yes`: To recreate docker image even when existing. Default: "no"
5. `--adr.build-docker-image.tags=_cache`: To use build cache for docker image build. Default: "" (`nocache`)
