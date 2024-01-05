import json
import sys
import os

with open(sys.argv[1], "r") as f:
    data = json.load(f)

images= {}
for image in data['images']:
    images[image['id']] = image
    images[image['id']]['num_boxes'] = 0

annots = data['annotations']
for box in annots:
    imageid = box['image_id']
    images[imageid]['num_boxes']+=1

sorted_image_data = sorted(data['images'], key=lambda x: x['num_boxes'], reverse= os.environ.get('CM_CALIBRATION_FILTER_ORDER_BY_NUM_BOXES_ASC', '') == "yes")
for image in data['images']:
    print(image['file_name'])
