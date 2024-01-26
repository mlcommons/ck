### About

This is a source code of portable and reusable automation recipes 
from MLCommons projects with a [human-friendly CM interface](https://github.com/mlcommons/ck) -
you can find more details [here](../../docs/list_of_scripts.md).

### License

[Apache 2.0](../../LICENSE.md)

### Copyright

2022-2024 [MLCommons](https://mlcommons.org)

### Examples

```bash
pip install cmind

cm pull repo mlcommons@ck

cm run script "python app image-classification onnx"

cm run script "download file _wget" --url=https://cKnowledge.org/ai/data/computer_mouse.jpg --verify=no --env.CM_DOWNLOAD_CHECKSUM=45ae5c940233892c2f860efdf0b66e7e

cm run script "python app image-classification onnx" --input=computer_mouse.jpg

cm docker script "python app image-classification onnx" --input=computer_mouse.jpg
cm docker script "python app image-classification onnx" --input=computer_mouse.jpg -j -docker_it

cm run script "get generic-python-lib _package.onnxruntime"
cm run script "get coco dataset _val _2014"
cm run script "get ml-model stable-diffusion"
cm run script "get ml-model huggingface zoo _model-stub.alpindale/Llama-2-13b-ONNX" --model_filename=FP32/LlamaV2_13B_float32.onnx --skip_cache

cm show cache
cm show cache "get ml-model stable-diffusion"

cm run script "run common mlperf inference" --implementation=nvidia --model=bert-99 --category=datacenter --division=closed
cm find script "run common mlperf inference"

cm pull repo ctuning@cm-reproduce-research-projects
cmr "reproduce paper micro-2023 victima _install_deps"
cmr "reproduce paper micro-2023 victima _run" 

...

```

```python
import cmind
output=cmind.access({'action':'run', 'automation':'script',
                     'tags':'python,app,image-classification,onnx',
                     'input':'computer_mouse.jpg'})
if output['return']==0: print (output)
```
