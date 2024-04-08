import typing
import importlib
import os
import psutil

import utils

import numpy as np

import torch

from loadgen.model import Model, ModelFactory, ModelInput, ModelInputSampler


xinput = input

class XModel(Model):
    def __init__(self, session):
        assert session is not None
        self.session = session

    def predict(self, input: ModelInput):
        
        print ('')
        utils.print_host_memory_use('Host memory used')
                                        
        print ('Running inference ...')
        with torch.no_grad():
            output = self.session(input)
        
        utils.print_host_memory_use('Host memory used')
        
        return output


class XModelFactory(ModelFactory):
    def __init__(
        self,
        model_path: str,
        execution_provider="CPUExecutionProvider",
        execution_mode="",
        intra_op_threads=0,
        inter_op_threads=0,
        model_code='',
        model_sample_pickle=''
    ):

        self.model_path = model_path
        self.model_code = model_code
        self.model_sample_pickle = model_sample_pickle
        self.execution_provider = execution_provider


    def create(self) -> Model:
        print ('')
        print ('Loading model: {}'.format(self.model_path))

        checkpoint = torch.load(self.model_path, map_location=torch.device('cpu'))

        if self.model_code == '':
            raise Exception('path to model code was not provided')

        if self.model_sample_pickle == '':
            raise Exception('path to model sample pickle was not provided')

        # Load sample
        import pickle
        with open (self.model_sample_pickle, 'rb') as handle:
           self.input_sample = pickle.load(handle)
                
        # Check if has CM interface
        cm_model_module = os.path.join(self.model_code, 'cm.py')
        if not os.path.isfile(cm_model_module):
            raise Exception('cm.py interface for a PyTorch model was not found in {}'.format(self.model_code))

        # Load CM interface for the model
        import sys
        sys.path.insert(0, self.model_code)
        model_module=importlib.import_module('cm')
        del(sys.path[0])

        # Init model
        model = model_module.model_init(checkpoint, 'model_state_dict')
        model.eval()

        return XModel(model)


class XModelInputSampler(ModelInputSampler):
    def __init__(self, model_factory: XModelFactory):
        model = model_factory.create()
        self.input_sample = model_factory.input_sample
        return

    def sample(self, id_: int) -> ModelInput:
        input = self.input_sample
        return input

