# This test covers version, variation, compilation from src,
# add_deps_recursive, post_deps

import cmind as cm
import check as checks

r = cm.access({'action': 'run',
               'automation': 'script',
               'tags': 'run,docker,container',
               'add_deps_recursive': {
                   'compiler': {'tags': "gcc"}
               },
               'docker_cm_repo': 'mlcommons@cm4mlops',
               'image_name': 'cm-script-app-image-classification-onnx-py',
               'env': {
                   'CM_DOCKER_RUN_SCRIPT_TAGS': 'app,image-classification,onnx,python',
                   'CM_DOCKER_IMAGE_BASE': 'ubuntu:22.04',
                   'CM_DOCKER_IMAGE_REPO': 'cknowledge'
               },
               'quiet': 'yes'
               })
checks.check_return(r)

r = cm.access({'action': 'run',
               'automation': 'script',
               'tags': 'run,docker,container',
               'add_deps_recursive': {
                   'compiler': {'tags': "gcc"}
               },
               'docker_cm_repo': 'mlcommons@cm4mlops',
               'image_name': 'cm-script-app-image-classification-onnx-py',
               'env': {
                   'CM_DOCKER_RUN_SCRIPT_TAGS': 'app,image-classification,onnx,python',
                   'CM_DOCKER_IMAGE_BASE': 'ubuntu:24.04',
                   'CM_DOCKER_IMAGE_REPO': 'local'
               },
               'quiet': 'yes'
               })
checks.check_return(r)
