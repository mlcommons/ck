# About

This portable CM script is being developed by the [MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)
to modularize the *python reference implementations* of the [MLPerf inference benchmark](https://github.com/mlcommons/inference) 
using the [MLCommons CM automation meta-framework](https://github.com/mlcommons/ck).
The goal is to make it easier to run, optimize and reproduce MLPerf benchmarks 
across diverse platforms with continuously changing software and hardware.

# Current Coverage
<table>
<thead>
  <tr>
    <th>Model</th>
    <th>Device</th>
    <th>Backend</th>
    <th>Model Precision</th>
    <th>Status</th>
    <th>Comments</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="6"><a href="https://github.com/mlcommons/inference/blob/master/.github/workflows/test-resnet50.yml">ResNet50</a></td>
    <td rowspan="3">CPU</td>
    <td>Onnxruntime</td>
    <td>fp32</td>
    <td>✅</td>
    <td>Works on all tested versions</td>
  </tr>
  <tr>
    <td>Tensorflow</td>
    <td>fp32</td>
    <td>✅</td>
    <td>Works on all tested versions</td>
  </tr>
  <tr>
    <td>Pytorch</td>
    <td>N</td>
    <td>❌</td>
    <td><a href="https://github.com/mlcommons/inference/issues/828">Reference Implementation missing</a></td>
  </tr>
  <tr>
    <td rowspan="3">CUDA</td>
    <td>Onnxruntime</td>
    <td>fp32</td>
    <td>✅</td>
    <td>Works on all tested versions</td>
  </tr>
  <tr>
    <td>Tensorflow</td>
    <td>fp32</td>
    <td>✅</td>
    <td>Works on all tested versions</td>
  </tr>
  <tr>
    <td>Pytorch</td>
    <td>N</td>
    <td>❌</td>
    <td><a href="https://github.com/mlcommons/inference/issues/828">Reference Implementation missing</a></td>
  </tr>
  <tr>
    <td rowspan="6"><a href="https://github.com/mlcommons/inference/blob/master/.github/workflows/test-retinanet.yml">RetinaNet</a></td>
    <td rowspan="3">CPU</td>
    <td>Onnxruntime</td>
    <td>fp32</td>
    <td>✅</td>
    <td>Works on all tested versions</td>
  </tr>
  <tr>
    <td>Tensorflow</td>
    <td>fp32</td>
    <td>❌</td>
    <td>Not Implemented</td>
  </tr>
  <tr>
    <td>Pytorch</td>
    <td>fp32</td>
    <td>✅</td>
    <td>Works on all tested versions</td>
  </tr>
  <tr>
    <td rowspan="3">CUDA</td>
    <td>Onnxruntime</td>
    <td>fp32</td>
    <td>✅</td>
    <td>Works on all tested versions</td>
  </tr>
  <tr>
    <td>Tensorflow</td>
    <td>fp32</td>
    <td>❌</td>
    <td>Not Implemented</td>
  </tr>
  <tr>
    <td>Pytorch</td>
    <td>fp32</td>
    <td>✅</td>
    <td>Works on all tested versions</td>
  </tr>
  <tr>
    <td rowspan="8">Bert</td>
    <td rowspan="4">CPU</td>
    <td rowspan="2">Onnxruntime</td>
    <td>fp32</td>
    <td>✅</td>
    <td>Works on all tested versions</td>
  </tr>
  <tr>
    <td>int8</td>
    <td>✅</td>
    <td>Works on all tested versions</td>
  </tr>
  <tr>
    <td>Tensorflow</td>
    <td>fp32</td>
    <td>✅</td>
    <td>
Works with protobuf 3.19. Issue mentioned <a href="https://github.com/mlcommons/inference/issues/1276">here</a>
    </td>
  </tr>
  <tr>
    <td>Pytorch</td>
    <td>fp32</td>
    <td>✅</td>
    <td>
Works on all tested versions
</td>
  </tr>
  <tr>
    <td rowspan="4">CUDA</td>
    <td rowspan="2">Onnxruntime</td>
    <td>fp32</td>
    <td>✅</td>
    <td>Works on all tested versions
</td>
  </tr>
  <tr>
    <td>int8</td>
    <td>✅</td>
    <td>Works on all tested versions
</td>
  </tr>
  <tr>
    <td>Tensorflow</td>
    <td>fp32</td>
    <td>✅</td>
    <td>Not tested</td>
  </tr>
  <tr>
    <td>Pytorch</td>
    <td>fp32</td>
    <td>✅</td>
    <td>Works on all tested versions
</td>
  </tr>
  <tr>
    <td rowspan="6">3d-unet</td>
    <td rowspan="3">CPU</td>
    <td>Onnxruntime</td>
    <td>fp32</td>
    <td>✅</td>
    <td>Works on all tested versions</td>
  </tr>
  <tr>
    <td>Tensorflow</td>
    <td>fp32</td>
    <td>✅</td>
    <td>
Works on all tested versions
    </td>
  </tr>
  <tr>
    <td>Pytorch</td>
    <td>fp32</td>
    <td>✅</td>
    <td>
Works on all tested versions
</td>
  </tr>
  <tr>
    <td rowspan="3">CUDA</td>
    <td>Onnxruntime</td>
    <td>fp32</td>
   <td>✅</td>
    <td>
Works on all tested versions
</td>  </tr>
  <tr>
    <td>Tensorflow</td>
    <td>fp32</td>
   <td>✅</td>
    <td>
Works on all tested versions
</td>  </tr>
  <tr>
    <td>Pytorch</td>
    <td>fp32</td>
   <td>✅</td>
    <td>
Works on all tested versions
</td>  </tr>
  
  
   <tr>
    <td rowspan="1">Rnnt</td>
    <td rowspan="1">CPU</td>
    <td>Pytorch</td>
    <td>fp32</td>
    <td>✅</td>
    <td>Works on all tested versions</td>
  </tr>
  
  <tr>
    <td rowspan="2">DLRM</td>
    <td>CPU</td>
    <td>Pytorch</td>
    <td>fp32</td>
    <td>✅</td>
    <td>Works with torch 1.10 and numpy 1.19</td>
  </tr>
  <tr>
    <td>CUDA</td>
    <td>Pytorch</td>
    <td>fp32</td>
    <td>?</td>
    <td>Needs GPU with high memory capacity</td>
  </tr>

</tbody>
</table>

Please follow our R&D roadmap [here](https://github.com/mlcommons/ck/issues/536).



