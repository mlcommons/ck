os:         linux
dist:       xenial
language:   python

python:
#    - "2.7"
    - "3.6"
    - "3.7"

addons:
    apt:
        packages:
            - python-pip
        sources:
            - ubuntu-toolchain-r-test

before_install:
    - |
        if [ $TRAVIS_OS_NAME == "osx" ]; then
            brew update                                                         # this swaps python versions and makes 3 the default one

            if [ "$WANTED_PYTHON_VERSION" == "2.7" ]; then
                brew reinstall python\@2 || brew link --overwrite python\@2     # install and link python2 and pip2 to /usr/local/bin
                export PATH=/usr/local/opt/python\@2/bin:$PATH
                export PYTHON_EXE=python
                export PIP_EXE=pip
            else
                brew reinstall python                                           # install and link python3 and pip3 to /usr/local/bin
                export PATH=/usr/local/opt/python/bin:$PATH
                export PYTHON_EXE=python3
                export PIP_EXE=pip3
            fi

            export CK_PLATFORM_NAME="generic-macos "                            # used later by CK
        else
            sudo apt-get install python-pip
            export WANTED_PYTHON_VERSION=$TRAVIS_PYTHON_VERSION                 # since Python is supported in Linux, get it from Travis
            export CK_PLATFORM_NAME="generic-linux "                            # used later by CK (note the trailing space to make the choice unique)
            export PYTHON_EXE=python
            export PIP_EXE=pip
        fi

install: 
    - CWD=`pwd`
    - $PIP_EXE install coveralls
    - $PIP_EXE install pyyaml
    - echo "TRAVIS_OS_NAME=${TRAVIS_OS_NAME}, WANTED_PYTHON_VERSION=${WANTED_PYTHON_VERSION}"
    - which "${PYTHON_EXE}"
    - ${PYTHON_EXE} --version

script: 
    - ${PYTHON_EXE} -m pip install --ignore-installed --verbose pip setuptools
    - ${PYTHON_EXE} setup.py install
    - ck version
    - coverage run -m tests.test
    - ck pull repo:mlcommons@ck-mlops
    - echo "$CK_PLATFORM_NAME" | ck detect platform.os --update_platform_init
    - ck detect soft:compiler.python --full_path=`which ${PYTHON_EXE}`
    - ck install package --tags=lib,python-package,numpy
    - ck install package --tags=lib,python-package,scipy
    - ck install package --tags=lib,python-package,pillow
    - ck install package:lib-tensorflow-1.13.1-cpu
    - ck install package:imagenet-2012-val-min
    - ck install package --tags=imagenet,2012,aux,from.dividiti                     # (from.berkeley doesn't work)
    - ck install package --tags=dataset,imagenet,preprocessed,using-pillow,first.20
    - ck install package --quiet --tags=lib,python-package,onnx
    - ck install package --quiet --tags=model,image-classification,onnx,mobilenet,non-quantized,nchw,downloaded
    - ck install package --quiet --tags=model,onnx,mobilenet,nhwc,converted
    - ck install package --quiet --tags=model,onnx,resnet,nchw,converted
    - ck install package --quiet --tags=model,onnx,resnet,nhwc,converted
    - ck install package --quiet --tags=lib,python-package,onnxruntime,cpu

    - ck detect soft:compiler.gcc --full_path=`which gcc`
    - ck install package --tags=tool,cmake,prebuilt --quiet

    - ck install package --quiet --tags=mlperf,inference,src,r1.0

    - ck install package --tags=lib,python-package,absl

    - ck install package --tags=lib,python-package,mlperf,loadgen
    - ck install package --tags=lib,mlperf,loadgen,static

    - ck show env

    - ck compile program:cbench-automotive-susan --speed
    - ck run program:cbench-automotive-susan --cmd_key=corners --dataset_uoa=image-pgm-0001  --repeat=1 --env.MY_ENV=123 --env.TEST=xyz --return_error_if_external_fail
    
    - ck run program:image-classification-onnx-py --quiet --dep_add_tags.weights=mobilenet,converted --cmd_key=barebones --env.CK_BATCH_SIZE=3 --return_error_if_external_fail
    - ck run program:image-classification-onnx-py --dep_add_tags.weights=mobilenet,downloaded --cmd_key=preprocessed --env.CK_BATCH_COUNT=2 --return_error_if_external_fail
    - ck run program:image-classification-onnx-py --dep_add_tags.weights=resnet,nchw,converted --cmd_key=preprocessed --return_error_if_external_fail
    - ck run program:image-classification-onnx-py --dep_add_tags.weights=resnet,nhwc,converted --cmd_key=preprocessed --return_error_if_external_fail
    - ck run program:image-classification-onnx-py --cmd_key=preprocessed --dep_add_tags.weights=resnet,nchw,converted --env.CK_IMAGE_FILE=ILSVRC2012_val_00000003.JPEG --return_error_if_external_fail

after_success: coveralls
