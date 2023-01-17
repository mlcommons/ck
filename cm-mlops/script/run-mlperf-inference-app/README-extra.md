# Current Coverage
<table>
<thead>
  <tr>
    <th>Model</th>
    <th>Device</th>
    <th>Backend</th>
    <th>Qunatized</th>
    <th>Status</th>
    <th>Comments</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="6"><a href="https://github.com/mlcommons/inference/blob/master/.github/workflows/test-resnet50.yml">ResNet50</a></td>
    <td rowspan="3">CPU</td>
    <td>Onnxruntime</td>
    <td>N</td>
    <td>✅</td>
    <td>Works on all tested versions</td>
  </tr>
  <tr>
    <td>Tensorflow</td>
    <td>N</td>
    <td>✅</td>
    <td>Works on all tested versions</td>
  </tr>
  <tr>
    <td>Pytorch</td>
    <td>N</td>
    <td>❌</td>
    <td><a href="https://github.com/mlcommons/inference/issues/828">Reference Implementation missing?</a></td>
  </tr>
  <tr>
    <td rowspan="3">CUDA</td>
    <td>Onnxruntime</td>
    <td>N</td>
    <td>✅</td>
    <td>Works on all tested versions</td>
  </tr>
  <tr>
    <td>Tensorflow</td>
    <td>N</td>
    <td>?</td>
    <td>Not tested</td>
  </tr>
  <tr>
    <td>Pytorch</td>
    <td>N</td>
    <td>❌</td>
    <td><a href="https://github.com/mlcommons/inference/issues/828">Reference Implementation missing?</a></td>
  </tr>
  <tr>
    <td rowspan="6"><a href="https://github.com/mlcommons/inference/blob/master/.github/workflows/test-retinanet.yml">RetinaNet</a></td>
    <td rowspan="3">CPU</td>
    <td>Onnxruntime</td>
    <td>N</td>
    <td>✅</td>
    <td>Works on all tested versions</td>
  </tr>
  <tr>
    <td>Tensorflow</td>
    <td>N</td>
    <td>❌</td>
    <td>Not Implementted</td>
  </tr>
  <tr>
    <td>Pytorch</td>
    <td>N</td>
    <td>✅</td>
    <td>Works on all tested versions</td>
  </tr>
  <tr>
    <td rowspan="3">CUDA</td>
    <td>Onnxruntime</td>
    <td>N</td>
    <td>✅</td>
    <td>Works on all tested versions</td>
  </tr>
  <tr>
    <td>Tensorflow</td>
    <td>N</td>
    <td>❌</td>
    <td>Not Implemented</td>
  </tr>
  <tr>
    <td>Pytorch</td>
    <td>N</td>
    <td>✅</td>
    <td>Works on all tested versions</td>
  </tr>
  <tr>
    <td rowspan="8">Bert</td>
    <td rowspan="4">CPU</td>
    <td rowspan="2">Onnxruntime</td>
    <td>N</td>
    <td>✅</td>
    <td>Works on all tested versions</td>
  </tr>
  <tr>
    <td>Y</td>
    <td>✅</td>
    <td>Works on all tested versions</td>
  </tr>
  <tr>
    <td>Tensorflow</td>
    <td>N</td>
    <td>✅</td>
    <td>
Works with protobuf 3.19. Issue mentioned <a href="https://github.com/mlcommons/inference/issues/1276">here</a>
    </td>
  </tr>
  <tr>
    <td>Pytorch</td>
    <td>N</td>
    <td>✅</td>
    <td>
Works but with <a href="https://github.com/mlcommons/inference/issues/1288">strict check disabled</a>
</td>
  </tr>
  <tr>
    <td rowspan="4">CUDA</td>
    <td rowspan="2">Onnxruntime</td>
    <td>N</td>
    <td>?</td>
    <td>Not tested</td>
  </tr>
  <tr>
    <td>Y</td>
    <td>?</td>
    <td>Not tested</td>
  </tr>
  <tr>
    <td>Tensorflow</td>
    <td>N</td>
    <td>?</td>
    <td>Not tested</td>
  </tr>
  <tr>
    <td>Pytorch</td>
    <td>N</td>
    <td>?</td>
    <td>Not tested</td>
  </tr>
</tbody>
</table>

Please follow our R&D roadmap [here](https://github.com/mlcommons/ck/issues/536).


# Command line interface

Multiple choices are specified in `${}`.


```bash

python3 -m pip install cmind -U

cm pull repo mlcommons@ck --checkout=master

cm run script "get sys-utils-cm" --quiet

cm run script "install python-venv" --version=3.10.8 --name=mlperf

cm run script --tags=run,mlperf,inference,generate-run-cmds,${CM_MLPERF_CHOICE_SCRIPT} \
         --adr.python.name=mlperf \
         --adr.python.version_min=3.8 \
         --adr.compiler.tags=gcc \
         --submitter="${CM_MLPERF_CHOICE_SUBMITTER}" \
         --lang=${CM_MLPERF_CHOICE_IMPLEMENTATION} \
         --hw_name=${CM_MLPERF_CHOICE_HW_NAME} \
         --model=${CM_MLPERF_CHOICE_MODEL} \
         --backend=${CM_MLPERF_CHOICE_BACKEND} \
         --device=${CM_MLPERF_CHOICE_DEVICE} \
         --scenario=${CM_MLPERF_CHOICE_SCENARIO} \
         --mode=${CM_MLPERF_CHOICE_MODE} \
         --test_query_count=${CM_MLPERF_CHOICE_QUERY_COUNT} \
         --quiet \
         --clean

```

## Choices

* **CM_MLPERF_CHOICE_SCRIPT** : 
  * `""`
  * `_short` (to have a short run for testing)
  * `_submission` (to generate MLPerf submission)
  * `_dashboard` (to participate in MLPerf crowd-testing and submit results to a [live W&B dashboard](https://wandb.ai/cmind/cm-mlperf-dse-testing/table?workspace=user-gfursin)

* **CM_MLPERF_CHOICE_SUBMITTER** : 
  * submitter name

* **CM_MLPERF_CHOICE_IMPLEMENTATION** : 
  * `python` - for Python reference (unoptimized) implementation
  * `cpp` - for [C++ implementation](../app-mlperf-inference-cpp)


* **CM_MLPERF_CHOICE_HW_NAME** : 

  * is used to pick the runtime configuration value of the system as spefified for a given SUT 
    [here](../get-mlperf-inference-sut-configs).

* **CM_MLPERF_CHOICE_MODEL** :
  * `resnet50`
  * `retinanet`
  * `bert`


* **CM_MLPERF_CHOICE_BACKEND** :
  * `onnxruntime`
  * `pytorch`
  * `tf`
  * `tvm-onnx`


* **CM_MLPERF_CHOICE_DEVICE** :
  * `cpu`
  * `gpu`

* **CM_MLPERF_CHOICE_SCENARIO** :
  * `Offline`
  * `Server`
  * `SingleStream`
  * `MultiStream`

* **CM_MLPERF_CHOICE_MODE** :
  * `""`
  * `accuracy`
  * `performance`

* **CM_MLPERF_CHOICE_QUERY_COUNT** :
  * any number (typically 5, 50, 100, 500)



## Example

Here is an example of CM CLI to run the MLPerf inference benchmark
with object detection, RetinaNet FP32, small OpenImages, ONNX runtime and CPU:

```bash
cm run script --tags=run,mlperf,inference,generate-run-cmds,_submission,_short,_dashboard \
      --adr.python.name=mlperf \
      --adr.python.version_min=3.8 \
      --adr.compiler.tags=gcc \
      --adr.openimages-preprocessed.tags=_500 \
      --submitter="Community" \
      --hw_name=default \
      --model=retinanet \
      --backend=onnxruntime \
      --device=cpu \
      --scenario=Offline \
      --test_query_count=10 \
      --clean
```

In case of a successfull run, you should see your crowd-testing results at this 
[live W&B dashboard](https://wandb.ai/cmind/cm-mlperf-dse-testing/table?workspace=user-gfursin).

You can see other CLI examples to customize and run the MLPerf inference benchmark
in [these tutorials](https://github.com/mlcommons/ck/blob/master/docs/tutorials/sc22-scc-mlperf.md) 
successfully validated at the Student Cluster Competition at SuperComputing'22.


# Modular CM containers

Check prototypes of modular CM containers for MLPerf [here](modular-cm-containers).


# The next steps

You are welcome to join the [open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)
to contribute to this project and continue optimizing this benchmark and prepare an official submission 
for MLPerf inference v3.0 (March 2023) with the help of the community.

See the development roadmap [here](https://github.com/mlcommons/ck/issues/536).

