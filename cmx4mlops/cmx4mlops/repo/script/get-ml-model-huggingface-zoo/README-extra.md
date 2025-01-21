# Examples

```bash
cmr "get ml-model huggingface zoo _model-stub.alpindale/Llama-2-13b-ONNX" --model_filename=FP32/LlamaV2_13B_float32.onnx --full_subfolder=FP32
```

```bash
cmr "get ml-model huggingface zoo _model-stub.microsoft/Mistral-7B-v0.1-onnx" --model_filename=Mistral-7B-v0.1.onnx,Mistral-7B-v0.1.onnx.data
```

```bash
cmr "get ml-model huggingface zoo _model-stub.Intel/gpt-j-6B-int8-static" --model_filename=model.onnx --full_subfolder=.
```

```bash
cmr "get ml-model huggingface zoo _model-stub.runwayml/stable-diffusion-v1-5" --revision=onnx --model_filename=unet/model.onnx,unet/weights.pb
```

```bash
cmr "get ml-model huggingface zoo _model-stub.ctuning/mlperf-inference-bert-onnx-fp32-squad-v1.1" --model_filename=model.onnx
```
