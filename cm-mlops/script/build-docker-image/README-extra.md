# Build CM Docker Image
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/specs/script.md) builds a dockerfile with for using CM.

## How to use
```bash
cm run script --tags=build,docker,image --dockerfile=[DOCKERFILEPATH] --gh_token=[GITHUB_AUTH_TOKEN] --image_repo=[IMAGE_REPO] --image_name=[IMAGE_NAME] --image_tag=[IMAGE_TAG] --cache=[yes,no]
```
where
* `[DOCKERFILEPATH]` is the path to the dockerfile. If not given, the [dockerfile build script](../build-dockerfile) will be called.
* `[GITHUB_AUTH_TOKEN]`: is passed as a build argument to docker build.
* `[IMAGE_REPO]`: Repo name to add the docker image. Default is `local`.
* `[IMAGE_NAME]`: Name to add the docker image. Default is `cm`.
* `[IMAGE_TAG]`: Tag for the docker image. Default is `latest`.
* `--cache`: If `no` turns off docker build caching. Default is cache on.
* `[--docker_os, --docker_os_version, --cm_repo and --script_tags]` are additional options which are passed to the [dockerfile build script](../build-dockerfile) if needed.

