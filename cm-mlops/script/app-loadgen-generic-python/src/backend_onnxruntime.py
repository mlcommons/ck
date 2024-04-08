import typing

import numpy as np
import onnx
import onnxruntime as ort

from loadgen.model import Model, ModelFactory, ModelInput, ModelInputSampler

xinput = input

ONNX_TO_NP_TYPE_MAP = {
    "tensor(bool)": bool,
    "tensor(int)": np.int32,
    "tensor(int32)": np.int32,
    "tensor(int8)": np.int8,
    "tensor(uint8)": np.uint8,
    "tensor(int16)": np.int16,
    "tensor(uint16)": np.uint16,
    "tensor(uint64)": np.uint64,
    "tensor(int64)": np.int64,
    "tensor(float16)": np.float16,
    "tensor(float)": np.float32,
    "tensor(double)": np.float64,
    "tensor(string)": np.string_,
}


class XModel(Model):
    def __init__(self, session: ort.InferenceSession):
        assert session is not None
        self.session = session

    def predict(self, input: ModelInput):
        output = self.session.run(None, input)
        return output


class XModelFactory(ModelFactory):
    def __init__(
        self,
        model_path: str,
        execution_provider="CPUExecutionProvider",
        execution_mode="",
        intra_op_threads=0,
        inter_op_threads=0,
        model_code='',         # Not used here
        model_cfg={},          # Not used here
        model_sample_pickle='' # Not used here
    ):
        self.model_path = model_path
        self.execution_provider = execution_provider
        self.session_options = ort.SessionOptions()
        if execution_mode.lower() == "sequential":
            self.session_options.execution_mode = ort.ExecutionMode.ORT_SEQUENTIAL
        elif execution_mode.lower() == "parallel":
            self.session_options.execution_mode = ort.ExecutionMode.ORT_PARALLEL
        self.session_options.intra_op_num_threads = intra_op_threads
        self.session_options.inter_op_num_threads = inter_op_threads

    def create(self) -> Model:
        print ('Loading model: {}'.format(self.model_path))
#        model = onnx.load(self.model_path)
        session_eps = [self.execution_provider]
        session = ort.InferenceSession(
#            model.SerializeToString(), self.session_options, providers=session_eps
            self.model_path, self.session_options, providers=session_eps
        )
        return XModel(session)


class XModelInputSampler(ModelInputSampler):
    def __init__(self, model_factory: XModelFactory):
        model = model_factory.create()
        input_defs = model.session.get_inputs()
        self.inputs: typing.Dict[str, typing.Tuple[np.dtype, typing.List[int]]] = dict()
        for input in input_defs:
            input_name = input.name
            input_type = ONNX_TO_NP_TYPE_MAP[input.type]
            input_dim = [
                1 if (x is None or (type(x) is str)) else x for x in input.shape
            ]
            self.inputs[input_name] = (input_type, input_dim)

    def sample(self, id_: int) -> ModelInput:
        input = dict()
        for name, spec in self.inputs.items():
            val = np.random.random_sample(spec[1]).astype(spec[0])
            input[name] = val
        return input
