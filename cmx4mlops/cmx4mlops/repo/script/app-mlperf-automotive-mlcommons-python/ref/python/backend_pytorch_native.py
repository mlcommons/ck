"""
Pytoch native backend
Extended by Grigori Fursin for the ABTF demo
"""
# pylint: disable=unused-argument,missing-docstring
import torch  # currently supports pytorch1.0
import torchvision
import backend

import os
import sys
import importlib


class BackendPytorchNative(backend.Backend):
    def __init__(self):
        super(BackendPytorchNative, self).__init__()
        self.sess = None
        self.model = None
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"

        # Grigori added for ABTF model
        self.config = None
        self.num_classes = None
        self.image_size = None

    def version(self):
        return torch.__version__

    def name(self):
        return "pytorch-native"

    def image_format(self):
        return "NCHW"

    def load(self, model_path, inputs=None, outputs=None):

        # From ABTF code
        sys.path.insert(0, os.environ['CM_ML_MODEL_CODE_WITH_PATH'])

        from src.transform import SSDTransformer
        from src.utils import generate_dboxes, Encoder, colors, coco_classes
        from src.model import SSD, ResNet

        abtf_model_config = os.environ.get('CM_ABTF_ML_MODEL_CONFIG', '')

        num_classes_str = os.environ.get('CM_ABTF_NUM_CLASSES', '').strip()
        self.num_classes = int(
            num_classes_str) if num_classes_str != '' else 15

        self.config = importlib.import_module('config.' + abtf_model_config)
        self.image_size = self.config.model['image_size']

        self.model = SSD(
            self.config.model,
            backbone=ResNet(
                self.config.model),
            num_classes=self.num_classes)

        checkpoint = torch.load(
            model_path,
            map_location=torch.device(
                self.device))

        self.model.load_state_dict(checkpoint["model_state_dict"])

        if self.device.startswith('cuda'):
            self.model.cuda()

        self.model.eval()

        self.model = self.model.to(self.device)

        self.inputs = inputs
        self.outputs = outputs

        return self

    def predict(self, feed):
        # For ABTF

        # Always first element for now (later may stack for batching)
        img = feed['image'][0]

        if torch.cuda.is_available():
            img = img.cuda()

        inp = img.unsqueeze(dim=0)

        with torch.no_grad():
            ploc, plabel = self.model(inp)

            output = (ploc, plabel)

        return output
