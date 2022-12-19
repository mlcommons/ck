# Build CM Dockerfile
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/specs/script.md) builds a dockerfile with for using CM.

## How to use
```bash
cm run script --tags=build,dockerfile --docker_os=[DOCKER_OS] --docker_os_version=[DOCKER_OS_VERSION] --build --image_repo=[IMAGE_REPO] --image_tag=[IMAGE_TAG] --gh_token=[GITHUB_AUTH_TOKEN] --script_tags=[CM_SCRIPT_TAGS]
```
where
* `[DOCKER_OS]` is one of `ubuntu` or `rhel`. Default is `ubuntu`.
* `[DOCKER_OS_VERSION]` is one of `18.04`, `20.04`, `22.04` for `ubuntu` and `9` for `rhel`. Default is `20.04`.
* `--build` option calls the [CM docker image build script](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/build-docker-image) to build a docker image from the generated dockerfile. Default is off.
* `[GITHUB_AUTH_TOKEN]`: Github auth token to be passed to docker build to use as build argument. This is optional.
* `[CM_SCRIPT_TAGS]`: Tags for the CM script which should be run as the last command inside dockerfile. This script will do a fake run and set up all its dependencies in the docker image once built.
* `[IMAGE_REPO]`: Repo name to add the docker image. Default is `local`.
* `[IMAGE_TAG]`: Tag for the docker image. Default is `latest`.


## Supported and Tested OS
1. Ubuntu 18.04, 20.04, 22.04
2. RHEL 9

## Sample dockerfiles
1. [Ubuntu 18.04](dockerfiles/ubuntu_18.04.Dockerfile)
2. [Ubuntu 20.04](dockerfiles/ubuntu_20.04.Dockerfile)
1. [Ubuntu 22.04](dockerfiles/ubuntu_22.04.Dockerfile)
1. [rhel9](dockerfiles/rhel_9.Dockerfile)

