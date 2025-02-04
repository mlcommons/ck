"""
Original code was extended by Grigori Fursin to support cognata data set
"""

import json
import logging
import os
import time

import cv2
from PIL import Image

import numpy as np
from pycocotools.cocoeval import COCOeval
# import pycoco
import dataset

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("cognata")


class Cognata(dataset.Dataset):
    def __init__(self, data_path, image_list, name, use_cache=0, image_size=None,
                 image_format="NHWC", pre_process=None, count=None, cache_dir=None, preprocessed_dir=None, use_label_map=False, threads=os.cpu_count(),
                 model_config=None, model_num_classes=None, model_image_size=None):  # For ABTF
        super().__init__()

        self.image_size = image_size
        self.image_list = []
        self.label_list = []
        self.image_ids = []
        self.image_sizes = []
        self.count = count
        self.use_cache = use_cache
        self.data_path = data_path
        self.pre_process = pre_process
        self.use_label_map = use_label_map

        self.model_config = model_config
        self.model_num_classes = model_num_classes
        self.model_image_size = model_image_size
        self.ignore_classes = None
        self.files = None
        self.dboxes = None
        self.transform = None
        self.label_map = None
        self.label_info = None
        self.image_bin = []
        self.encoder = None
        self.targets = []

        #######################################################################
        # From ABTF source

        import torch
        from src.utils import generate_dboxes, Encoder
        from src.transform import SSDTransformer
        from src.dataset import prepare_cognata
        import cognata_labels
        import csv
        import ast

        self.dboxes = generate_dboxes(model_config.model, model="ssd")
        self.transform = SSDTransformer(
            self.dboxes, self.model_image_size, val=True)
        self.encoder = Encoder(self.dboxes)

        folders = model_config.dataset['folders']
        cameras = model_config.dataset['cameras']
        self.ignore_classes = [2, 25, 31]
        if 'ignore_classes' in model_config.dataset:
            self.ignore_classes = model_config.dataset['ignore_classes']

        # Grigori added for tests
        # Check if overridden by extrnal environment for tests
        x = os.environ.get(
            'CM_DATASET_MLCOMMONS_COGNATA_SERIAL_NUMBERS',
            '').strip()
        if x != '':
            folders = x.split(';') if ';' in x else [x]

        x = os.environ.get(
            'CM_DATASET_MLCOMMONS_COGNATA_GROUP_NAMES',
            '').strip()
        if x != '':
            cameras = x.split(';') if ';' in x else [x]

        print('')
        print('Cognata folders: {}'.format(str(folders)))
        print('Cognata cameras: {}'.format(str(cameras)))
        print('')

        # From ABTF source
        print('')
        print('Scanning Cognata dataset ...')
        start = time.time()
        files, label_map, label_info = prepare_cognata(
            data_path, folders, cameras, self.ignore_classes)

        self.files = files

        print('  Number of files found: {}'.format(len(files)))
        print('  Time: {:.2f} sec.'.format(time.time() - start))

        if os.environ.get(
                'CM_ABTF_ML_MODEL_TRAINING_FORCE_COGNATA_LABELS', '') == 'yes':
            label_map = cognata_labels.label_map
            label_info = cognata_labels.label_info

        self.label_map = label_map
        self.label_info = label_info

        if self.model_num_classes is not None:
            self.model_num_classes = len(label_map.keys())

        print('')
        print('Preloading and preprocessing Cognata dataset on the fly ...')

        start = time.time()

        idx = 0

        for f in self.files:

            image_name = self.files[idx]['img']

            img = Image.open(image_name).convert('RGB')

            width, height = img.size
            boxes = []
            boxes2 = []
            labels = []
            gt_boxes = []
            targets = []
            with open(self.files[idx]['ann']) as f:
                reader = csv.reader(f)
                rows = list(reader)
                header = rows[0]
                annotations = rows[1:]
                bbox_index = header.index('bounding_box_2D')
                class_index = header.index('object_class')
                distance_index = header.index('center_distance')
                for annotation in annotations:
                    bbox = annotation[bbox_index]
                    bbox = ast.literal_eval(bbox)
                    object_width = bbox[2] - bbox[0]
                    object_height = bbox[3] - bbox[1]
                    object_area = object_width * object_height
                    label = ast.literal_eval(annotation[class_index])
                    distance = ast.literal_eval(annotation[distance_index])
                    if object_area < 50 or int(
                            label) in self.ignore_classes or object_height < 8 or object_width < 8 or distance > 300:
                        continue
                    label = self.label_map[label]
                    boxes.append([bbox[0] / width, bbox[1] / height,
                                 bbox[2] / width, bbox[3] / height])
                    boxes2.append([bbox[0], bbox[1], bbox[2], bbox[3]])
                    gt_boxes.append(
                        [bbox[0], bbox[1], bbox[2], bbox[3], label, 0, 0])
                    labels.append(label)

                boxes = torch.tensor(boxes)
                boxes2 = torch.tensor(boxes2)
                labels = torch.tensor(labels)
                gt_boxes = torch.tensor(gt_boxes)

                targets.append({'boxes': boxes2.to(device='cpu'),
                                'labels': labels.to(device='cpu',
                                                    dtype=torch.int32)})

            img, (height, width), boxes, labels = self.transform(
                img, (height, width), boxes, labels, max_num=500)

            _, height, width = img.shape

            self.image_bin.append(img)
            self.image_ids.append(idx)
            self.image_list.append(image_name)
            self.image_sizes.append((height, width))

            self.label_list.append((labels, boxes))

            self.targets.append(targets)

            # limit the dataset if requested
            idx += 1
            if self.count is not None and idx >= self.count:
                break

        print('  Time: {:.2f} sec.'.format(time.time() - start))
        print('')

        return

    def get_item(self, nr):
        """Get image by number in the list."""

        return self.image_bin[nr], self.label_list[nr]

    def get_item_loc(self, nr):

        return self.files[nr]['img']

    # Grigori added here to be able to return Torch tensor and not Numpy

    def get_samples(self, id_list):

        data = [self.image_list_inmemory[idx] for idx in id_list]
        labels = [self.label_list[idx] for idx in id_list]

        return data, labels


class PostProcessCognata:
    """
    Post processing for tensorflow ssd-mobilenet style models
    """

    def __init__(self):
        self.results = []
        self.good = 0
        self.total = 0
        self.content_ids = []
        self.use_inv_map = False

    def add_results(self, results):
        self.results.extend(results)

    def __call__(self, results, ids, expected=None, result_dict=None, ):

        # Dummy
        processed_results = []
        return processed_results

    def start(self):
        self.results = []
        self.good = 0
        self.total = 0

    def finalize(self, result_dict, ds=None, output_dir=None):

        # To be improved

        from torchmetrics.detection.mean_ap import MeanAveragePrecision
        metric = MeanAveragePrecision(
            iou_type="bbox",
            class_metrics=True,
            backend='faster_coco_eval')

        result_dict["good"] += self.good
        result_dict["total"] += self.total

        preds = []
        targets = []
        # For now batch_size = 1
        for idx in range(0, len(self.results)):
            preds.append(self.results[idx][0])
            id = self.results[idx][0]['id']
            targets.append(ds.targets[id][0])
        metric.update(preds, targets)

        metrics = metric.compute()

        print('=================================================')
        import pprint
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(metrics)
        print('=================================================')

        classes = metrics['classes'].tolist()
        map_per_classes = metrics['map_per_class'].tolist()

        final_map = {}
        for c in range(0, len(classes)):
            final_map[ds.label_info[classes[c]]] = float(map_per_classes[c])

        result_dict["mAP"] = float(metrics['map'])
        result_dict["mAP_classes"] = final_map


class PostProcessCognataPt(PostProcessCognata):
    """
    Post processing required by ssd-resnet34 / pytorch
    """

    def __init__(self, nms_threshold, max_output,
                 score_threshold, height, width):
        super().__init__()
        self.nms_threshold = nms_threshold
        self.max_output = max_output
        self.score_threshold = score_threshold
        self.height = height
        self.width = width

    def __call__(self, results, ids, expected=None, result_dict=None):
        # results come as:
        #   detection_boxes,detection_classes,detection_scores

        import torch

        processed_results = []

        # For now 1 result (batch 1) - need to add support for batch size > 1
        # later
        ploc = results[0]
        plabel = results[1]

        # Get predictions (from cognata_eval)
#        ploc, plabel = model(img)
        ploc, plabel = ploc.float(), plabel.float()

        preds = []

        for i in range(ploc.shape[0]):
            dts = []
            labels = []
            scores = []

            ploc_i = ploc[i, :, :].unsqueeze(0)
            plabel_i = plabel[i, :, :].unsqueeze(0)

            result = self.encoder.decode_batch(
                ploc_i, plabel_i, self.nms_threshold, self.max_output)[0]

            loc, label, prob = [r.cpu().numpy() for r in result]
            for loc_, label_, prob_ in zip(loc, label, prob):
                if label_ in expected[i][0]:
                    self.good += 1
                self.total += 1
                dts.append([loc_[0] *
                            self.width, loc_[1] *
                            self.height, loc_[2] *
                            self.width, loc_[3] *
                            self.height,])
                labels.append(label_)
                scores.append(prob_)

            dts = torch.tensor(dts, device='cpu')
            labels = torch.tensor(labels, device='cpu', dtype=torch.int32)
            scores = torch.tensor(scores, device='cpu')
            preds.append({'boxes': dts, 'labels': labels,
                         'scores': scores, 'id': ids[i]})

        # Only batch size supported
        idx = 0

        processed_results.append(preds)

        # self.total += 1

        return processed_results
