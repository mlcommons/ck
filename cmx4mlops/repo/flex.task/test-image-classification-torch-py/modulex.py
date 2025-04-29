# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy

def run(i):

    ###################################################################
    # Prepare flow

    tmp = i['tmp']

    cmind = i['cmind']

    misc = i['misc']

    out = misc.get('out', '')
    console = misc.get('console', False)

    self_meta = misc['meta']
    self_path = misc['path']

    self_path_tmp = os.path.join(self_path, 'tmp')
    if not os.path.isdir(self_path_tmp):
        os.makedirs(self_path_tmp)

    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)

    _input = i['input']

    image = _input.get('image', '')
    url = _input.get('url', '')
    url_md5sum = _input.get('url_md5sum', '')
    device = _input.get('device', '')

    # Check device (either from select-compute or forced)
    if device == '':
        device = tmp['target_pytorch_device']

    if console:
        print ('')

    if image != '':
        image = os.path.abspath(image)
        if not os.path.isfile(image):
            return cmind.prepare_error(1, f'image {image} not found')

    if image == '':
        if url == '':
            url = 'https://cKnowledge.org/ai/data/computer_mouse.jpg'
            url_md5sum = '45ae5c940233892c2f860efdf0b66e7e'

        # Download test image
        r = cmind.x({'action':'run',
                     'automation':misc['flex.task'],
                     'control':{'out':out},
                     'verbose': verbose,
                     'tags':'download,file',
                     'url': url,
                     'md5sum': url_md5sum,
                     'tool': 'cmx',
                     'directory': self_path_tmp
                    })

        if r['return'] >0 : return r

        image = r['path_to_file']

    if console and verbose:
        print ('')
        print (f'INFO image: {image}')

    # Download classes
    r = cmind.x({'action':'run',
                 'automation':misc['flex.task'],
                 'control':{'out':out},
                 'verbose': verbose,
                 'tags':'download,file',
                 'url': 'https://cKnowledge.org/ai/data/imagenet_classes.txt',
                 'md5sum': '4b150cedb753f3cece10d19b0dd815fe',
                 'tool': 'cmx',
                 'directory': self_path_tmp
                })

    if r['return'] >0 : return r

    classes_with_path = r['path_to_file']

    rrr = {'return': 0}

    if console:
        print ('')

    rrr['_update_run_script_env'] = {
                                      'CMX_IMAGE_WITH_PATH':image,
                                      'CMX_CLASSES_WITH_PATH':classes_with_path,
                                      'CMX_PYTORCH_DEVICE': device
                                    }

    return rrr
