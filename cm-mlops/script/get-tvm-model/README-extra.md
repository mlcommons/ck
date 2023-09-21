# CM script

This script starts tuning (if specified) and compilation of any model using Apache TVM.

## How To
```bash
cm run script --tags=get,tvm-model,_[VARIATION]
```
where, `[VARIATION]` is one of 
1) Frontend frameworks name (`onnx`, `pytorch`, `tensorflow`, `tflite`)
2) Precision (`fp32`, `int8`)
3) TVM Runtime (`virtual_machine` or `graph_executor`)
4) `tune-model` variation if you want to start tuning the model using TVM MetaScheduler
5) Model name (`model.#`)
6) Batch size (`batch_size.#`)
in 5 and 6 you can insert any suitable value instead of the symbol `#`, e.g. `model.bert` or `batch_size.8`.

## Notes

For PyTorch and TensorFlow frontends you should specify evironment variable `CM_ML_MODEL_INPUT_SHAPES` with input shapes of the model you want to compile (e.g. `"input": (16, 3, 224, 224)`) or separate variables `CM_ML_MODEL_IMAGE_NUM_CHANNELS`, `CM_ML_MODEL_IMAGE_WIDTH`, `CM_ML_MODEL_IMAGE_HEIGHT` for 2D CV models and `CM_ML_MODEL_MAX_SEQ_LENGTH` for language models.    
If your model is in ONNX format then all input shapes can be extracted automatically.
