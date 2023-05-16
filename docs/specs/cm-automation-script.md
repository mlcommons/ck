[ [Back to Specs](README.md) ]

# CM scripts

*Please check the [CM introduction](../introduction-cm.md) to understand CM motivation and concepts.*




## Tags

```bash
cm (some actions) --tags={list of tags}
```

### Searching artifacts

* "-" prefix is used to exclude artifacts with this tag

### Differentiating ML artifacts

* "app-" is used to specify application script
* "_" is used to select variations


## Environment variables

### Converted from CLI

* CM_TMP_QUIET
* CM_PATH
* CM_INPUT
* CM_OUTPUT
* CM_NAME

### Local (removed from deps)

* CM_VERSION
* CM_VERSION_MIN
* CM_VERSION_MAX
* CM_VERSION_MAX_DEFAULT
* CM_GIT_*
* CM_TMP_*

### Automatically generated

* CM_TMP_CURRENT_PATH - script or cache
* CM_TMP_CURRENT_SCRIPT_PATH - script only

