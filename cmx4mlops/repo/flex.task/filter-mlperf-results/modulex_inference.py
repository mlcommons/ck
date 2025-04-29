# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy

file_summary = 'summary.csv'
file_summary_json = 'mlperf-inference-summary-{}.json'
file_result = 'cm-result.json'

model2task = {
   "resnet":"image-classification",
   "retinanet":"object-detection",
   "ssd-small":"object-detection",
   "ssd-large": "object-detection",
   "rnnt":"speech-recognition",
   "bert-99":"language-processing",
   "bert-99.9":"language-processing",
   "gptj-99":"language-processing",
   "gptj-99.9":"language-processing",
   "llama2-70b-99":"language-processing",
   "llama2-70b-99.9":"language-processing",
   "dlrm-99":"recommendation",
   "dlrm-v2-99":"recommendation",
   "dlrm-99.9":"recommendation",
   "dlrm-v2-99.9":"recommendation",
   "3d-unet-99":"image-segmentation",
   "3d-unet-99.9":"image-segmentation",
   "stable-diffusion-xl":"text-to-image"
}

def process(i):


    print (i)


    return {'return':0}
