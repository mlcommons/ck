**[ [TOC](../README.md) ]**

# x8664-based generic platforms with Yocto

## Prerequisites

The following configuration is needed in Yocto build to avoid the
["most close platform was not found in CK" problem](https://github.com/mlcommons/ck/issues/181):

```
...
PACKAGE_CLASSES ?= "package_deb"
CORE_IMAGE_EXTRA_INSTALL="dpkg"
EXTRA_IMAGE_FEATURES = "tools-sdk tools-debug"
```
