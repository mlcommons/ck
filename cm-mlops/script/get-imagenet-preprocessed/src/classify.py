"""
Developers:
 - grigori@octoml.ai
"""

import time
import os
import argparse
import json

from PIL import Image
import cv2

import numpy as np




# Image conversion from MLPerf(tm) vision
def center_crop(img, out_height, out_width):
    height, width, _ = img.shape
    left = int((width - out_width) / 2)
    right = int((width + out_width) / 2)
    top = int((height - out_height) / 2)
    bottom = int((height + out_height) / 2)
    img = img[top:bottom, left:right]
    return img


def resize_with_aspectratio(img, out_height, out_width, scale=87.5, inter_pol=cv2.INTER_LINEAR):
    height, width, _ = img.shape
    new_height = int(100. * out_height / scale)
    new_width = int(100. * out_width / scale)
    if height > width:
        w = new_width
        h = int(new_height * height / width)
    else:
        h = new_height
        w = int(new_width * width / height)
    img = cv2.resize(img, (w, h), interpolation=inter_pol)
    return img


# returns list of pairs (prob, class_index)
def get_top5(all_probs):
  probs_with_classes = []

  for class_index in range(len(all_probs)):
    prob = all_probs[class_index]
    probs_with_classes.append((prob, class_index))

  sorted_probs = sorted(probs_with_classes, key = lambda pair: pair[0], reverse=True)
  return sorted_probs[0:5]

def run_case(dtype, image, target):
    # Check image
    import os
    import json
    import sys

    STAT_REPEAT=os.environ.get('STAT_REPEAT','')
    if STAT_REPEAT=='' or STAT_REPEAT==None:
       STAT_REPEAT=10
    STAT_REPEAT=int(STAT_REPEAT)

    # FGG: set model files via CK env
    CATEG_FILE = 'synset.txt'
    synset = eval(open(os.path.join(CATEG_FILE)).read())

    files=[]
    val={}

    # FGG: set timers
    import time
    timers={}

    img_orig = cv2.imread(image)

    img = cv2.cvtColor(img_orig, cv2.COLOR_BGR2RGB)

    output_height, output_width, _ = 224, 224, 3
    img = resize_with_aspectratio(img, output_height, output_width, inter_pol=cv2.INTER_AREA)
    img = center_crop(img, output_height, output_width)
    img = np.asarray(img, dtype='float32')

    # normalize image
    means = np.array([123.68, 116.78, 103.94], dtype=np.float32)
    img -= means

    # transpose if needed
    img = img.transpose([2, 0, 1])
    image_file_name = os.path.basename(image)
    img.tofile("preprocessed/"+image_file_name+".raw")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', type=str, help="Path to JPEG image.", default=None, required=True)
    parser.add_argument('--target', type=str, help="Target", default=None)
    args = parser.parse_args()

    if args.image.strip().lower()=='':
        print ('Please specify path to an image using CK_IMAGE environment variable!')
        exit(1)

    # set parameter
    batch_size = 1
    num_classes = 1000
    image_shape = (3, 224, 224)

    # load model
    data_shape = (batch_size,) + image_shape
    out_shape = (batch_size, num_classes)

    dtype='float32'

    run_case(dtype, args.image, args.target)
