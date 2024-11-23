Some CM commands:


```bash

pip install cmind -U

cm init

cm run script "run-mlperf-inference _r4.1 _accuracy-only _short" \
   --device=cpu \
   --model=resnet50 \
   --precision=float32 \
   --implementation=reference \
   --backend=onnxruntime \
   --scenario=Offline \
   --clean \
   --quiet \
   --time

cm run script "run-mlperf-inference _r4.1 _submission _short" \
   --device=cpu \
   --model=resnet50 \
   --precision=float32 \
   --implementation=reference \
   --backend=onnxruntime \
   --scenario=Offline \
   --clean \
   --quiet \
   --time

...

                                                                           0
Organization                                                         CTuning
Availability                                                       available
Division                                                                open
SystemType                                                              edge
SystemName                                                   ip_172_31_87_92
Platform                   ip_172_31_87_92-reference-cpu-onnxruntime-v1.1...
Model                                                               resnet50
MlperfModel                                                           resnet
Scenario                                                             Offline
Result                                                               14.3978
Accuracy                                                                80.0
number_of_nodes                                                            1
host_processor_model_name     Intel(R) Xeon(R) Platinum 8259CL CPU @ 2.50GHz
host_processors_per_node                                                   1
host_processor_core_count                                                  2
accelerator_model_name                                                   NaN
accelerators_per_node                                                      0
Location                   open/CTuning/results/ip_172_31_87_92-reference...
framework                                                onnxruntime v1.18.1
operating_system               Ubuntu 24.04 (linux-6.8.0-1009-aws-glibc2.39)
notes                                     Automated by MLCommons CM v2.3.2.
compliance                                                                 1
errors                                                                     0
version                                                                 v4.1
inferred                                                                   0
has_power                                                              False
Units                                                              Samples/s


```

You can also run the same commands using a unified CM Python API:

```python
import cmind
output=cmind.access({
   'action':'run', 'automation':'script',
   'tags':'run-mlperf-inference,_r4.1,_performance-only,_short',
   'device':'cpu',
   'model':'resnet50',
   'precision':'float32',
   'implementation':'reference',
   'backend':'onnxruntime',
   'scenario':'Offline',
   'clean':True,
   'quiet':True,
   'time':True,
   'out':'con'
})
if output['return']==0: print (output)
```


We suggest you to use this [online CM interface](https://access.cknowledge.org/playground/?action=howtorun)
to generate CM commands that will prepare and run MLPerf benchmarks and AI applications across different platforms.


See more examples of CM scripts and workflows to download Stable Diffusion, GPT-J and LLAMA2 models, process datasets, install tools and compose AI applications:


```bash
pip install cmind -U

cm pull repo mlcommons@cm4mlops --branch=dev

cm show repo

cm run script "python app image-classification onnx"
cmr "python app image-classification onnx"

cmr "download file _wget" --url=https://cKnowledge.org/ai/data/computer_mouse.jpg --verify=no --env.CM_DOWNLOAD_CHECKSUM=45ae5c940233892c2f860efdf0b66e7e
cmr "python app image-classification onnx" --input=computer_mouse.jpg
cmr "python app image-classification onnx" --input=computer_mouse.jpg --debug

cm find script "python app image-classification onnx"
cm load script "python app image-classification onnx" --yaml

cmr "get python" --version_min=3.8.0 --name=mlperf-experiments
cmr "install python-venv" --version_max=3.10.11 --name=mlperf

cmr "get ml-model stable-diffusion"
cmr "get ml-model sdxl _fp16 _rclone"
cmr "get ml-model huggingface zoo _model-stub.alpindale/Llama-2-13b-ONNX" --model_filename=FP32/LlamaV2_13B_float32.onnx --skip_cache
cmr "get dataset coco _val _2014"
cmr "get dataset openimages" -j

cm show cache
cm show cache "get ml-model stable-diffusion"

cmr "get generic-python-lib _package.onnxruntime" --version_min=1.16.0
cmr "python app image-classification onnx" --input=computer_mouse.jpg

cm rm cache -f
cmr "python app image-classification onnx" --input=computer_mouse.jpg --adr.onnxruntime.version_max=1.16.0

cmr "get cuda" --version_min=12.0.0 --version_max=12.3.1
cmr "python app image-classification onnx _cuda" --input=computer_mouse.jpg

cm gui script "python app image-classification onnx"

cm docker script "python app image-classification onnx" --input=computer_mouse.jpg
cm docker script "python app image-classification onnx" --input=computer_mouse.jpg -j -docker_it

cm docker script "get coco dataset _val _2017" --to=d:\Downloads\COCO-2017-val --store=d:\Downloads --docker_cm_repo=ctuning@mlcommons-ck

cmr "run common mlperf inference" --implementation=nvidia --model=bert-99 --category=datacenter --division=closed
cm find script "run common mlperf inference"

cmr "get generic-python-lib _package.torch" --version=2.1.2
cmr "get generic-python-lib _package.torchvision" --version=0.16.2
cmr "python app image-classification torch" --input=computer_mouse.jpg


cm rm repo mlcommons@cm4mlops
cm pull repo --url=https://zenodo.org/records/12528908/files/cm4mlops-20240625.zip

cmr "install llvm prebuilt" --version=17.0.6
cmr "app image corner-detection"

cm run experiment --tags=tuning,experiment,batch_size -- echo --batch_size={{ print_str("VAR1{range(1,8)}") }}

cm replay experiment --tags=tuning,experiment,batch_size

cmr "get conda"

cm pull repo ctuning@cm4research
cmr "reproduce paper micro-2023 victima _install_deps"
cmr "reproduce paper micro-2023 victima _run" 

```


See a few examples of modular containers and GitHub actions with CM commands:

* [GitHub action with CM commands to test MLPerf inference benchmark](https://github.com/mlcommons/inference/blob/master/.github/workflows/test-bert.yml)
* [Dockerfile to run MLPerf inference benchmark via CM](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-mlperf-inference/dockerfiles/bert-99.9/ubuntu_22.04_python_onnxruntime_cpu.Dockerfile)


Please check the [**Getting Started Guide**](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md) 
to understand how CM automation recipes work, how to use them to automate your own projects,
and how to implement and share new automations in your public or private projects.
