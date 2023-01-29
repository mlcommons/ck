from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    full = env.get('CM_IMAGENET_FULL', '').strip() == 'yes'

    path = env.get('CM_INPUT', '').strip()

    if full:
        if path == '':
            # If full dataset but path to imagenet is not specified,
            # try IMAGENET_PATH

            path = env.get('IMAGENET_PATH', '')

        if path == '':
            return {'return':1, 'error':'Please rerun the last CM command with --env.IMAGENET_PATH={path the folder containing full ImageNet images} or envoke cm run script "get val dataset imagenet" --input={path to the folder containing ImageNet images}'}

        if not os.path.isdir(path):
            return {'return':1, 'error':'Path {} doesn\'t exist'.format(path)}

        path_image = os.path.join(path, 'ILSVRC2012_val_00000001.JPEG')

        if not os.path.isfile(path_image):
            return {'return':1, 'error':'ImageNet file {} not found'.format(path_image)}

        env['CM_DATASET_PATH'] = path
        env['CM_DATASET_IMAGENET_PATH'] = path

    return {'return':0}
