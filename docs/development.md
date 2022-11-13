[ [Back to index](README.md) ]

# CM internal architecture

Here is a diagram of the main CM classes, functions and automations (v1.0.5+):

![](https://cKnowledge.org/images/cm-diagram-v0.7.24.png)

The original chart is available [here](https://lucid.app/lucidchart/d95cf6bb-9beb-435b-80c0-1a7140dcf7ae/edit?invitationId=inv_4d177cce-595a-4a4a-8194-69abee06d2c7).


# CM script conventions

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

