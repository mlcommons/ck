# Build CM Dockerfile
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/tutorial-scripts.md) builds a dockerfile with for using CM.

## How to use
```bash
cm run script --tags=build,dockerfile --docker_os=[DOCKER_OS] --docker_os_version=[DOCKER_OS_VERSION] [--build --image_repo=[IMAGE_REPO] --image_tag=[IMAGE_TAG]
```
where
1. [DOCKER_OS] is one of `ubuntu` or `rhel`
2. [DOCKER_OS_VERSION] is one of `18.04`, `20.04`, `22.04` for `ubuntu` and `9` for `rhel`
3. `--build` option calls the [CM docker container build script](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/build-docker-image) to build a docker image from the generated dockerfile
4. [IMAGE_REPO]: Repo name to add the docker image
5. [IMAGE_TAG]: Tag for the docker image

## Supported and Tested OS
1. Ubuntu 18.04, 20.04, 22.04
2. RHEL 9

## Sample dockerfiles
1. [Ubuntu 18.04](dockerfiles/ubuntu_18.04.Dockerfile)
2. [Ubuntu 20.04]()
1. [Ubuntu 22.04]()
1. [rhel9]()

