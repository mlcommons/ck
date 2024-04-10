### Challenge

Run MLPerf inference v3.0 benchmarks out-of-the-box across diverse implementations, software and hardware
using the [MLCommons CM automation language](https://github.com/mlcommons/ck)
and submit public results to the MLPerf inference v3.0 via [cTuning foundation](https://cTuning.org).

* [GUI to run MLPerf inference benchmarks](https://cknowledge.org/mlperf-inference-gui)
* [GUI to prepare MLPerf inference submissions](https://cknowledge.org/mlperf-inference-submission-gui)

Join this public [Discord server](https://discord.gg/JjWNWXKxwT) to discuss this challenge with the organizers.

### Organizers

* [MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)
* [cTuning foundation](https://cTuning.org)
* [cKnowledge](https://cKnowledge.org)

Contact [Grigori Fursin](https://cKnowledge.org/gfursin) and [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh)
for more details.

### Status

This challenge has been successfully completed.

### Results

Official results:
* https://github.com/mlcommons/inference_results_v3.0/tree/main/closed/cTuning
* https://github.com/mlcommons/inference_results_v3.0/tree/main/open/cTuning

Results in the MLCommons CK/CM format:
* https://github.com/mlcommons/cm4mlperf-results

Visualization and comparison with derived metrics:
* [MLCommons Collective Knowledge Playground](https://access.cknowledge.org/playground/?action=experiments&tags=mlperf-inference,v3.0).

### The outcome

We are very pleased to announce the successful outcome of the 1st
community challenge to run, reproduce and optimize MLPerf inference v3.0
benchmarks: our MLCommons CK/CM workflow automation framework has helped 
to prepare more than 80% of all submission results including 98% of power
results with very diverse technology and benchmark implementations from
Neural Magic, Qualcomm, cKnowledge Ltd, KRAI, cTuning foundation, Dell
Technologies, Hewlett Packard Enterprise, Lenovo, Hugging Face, NVIDIA,
Intel Corporation, AMD and Apple across diverse CPUs, GPUs and DSPs with
PyTorch, ONNX, QAIC, TF/TFLite, TVM and TensorRT using popular cloud
providers (GCP, AWS, Azure) and individual servers and edge devices
provided by our [volunteers](https://access.cknowledge.org/playground/?action=contributors).

You can now see and compare all MLPerf inference results v3.0, v2.1 and
v2.0 online together with reproducibility reports including the 
[MLPerf BERT model](https://huggingface.co/ctuning/mlperf-inference-bert-onnx-fp32-squad-v1.1) 
from the [Hugging Face Zoo](https://www.linkedin.com/company/huggingface/?lipi=urn%3Ali%3Apage%3Ad_flagship3_pulse_read%3B4CDUdiVxT7WqLJNXO%2BI5bQ%3D%3D) 
on [Nvidia Jetson Orin platform](https://github.com/mlcommons/ck/blob/master/cm-mlops/challenge/optimize-mlperf-inference-v3.0-2023/docs/setup-nvidia-jetson-orin.md#reproducing-the-nvidia-jetson-agx-orin-submission). 
You can even create your own derived metrics (such as performance per Watt),
provide your own constraints using this [MLCommons repository](https://github.com/mlcommons/cm_inference_results) and visualize
them as shown in [this example](https://access.cknowledge.org/playground/?action=experiments&name=e472410ee67c41f9&x=Result&y=Power_Efficiency&filter=result[%27Result_Power%27]%3C35&derived_metrics=result%5B%27Power_Efficiency%27%5D%3D1000%2Fresult%5B%27Result_Power%27%5D&c=accelerator_model_name&axis_key_s=version). 

Additional thanks to [Michael Goin](https://www.linkedin.com/in/michael-goin) 
from [Neural Magic](https://www.linkedin.com/company/neural-magic/?lipi=urn%3Ali%3Apage%3Ad_flagship3_pulse_read%3B4CDUdiVxT7WqLJNXO%2BI5bQ%3D%3D), our international
students including [Himanshu Dutta](https://www.linkedin.com/in/ACoAACpPCiMB7zUNStsqBmaOCtd100a7wXBGu_M?lipi=urn%3Ali%3Apage%3Ad_flagship3_pulse_read%3B4CDUdiVxT7WqLJNXO%2BI5bQ%3D%3D), 
[Aditya Kumar Shaw](https://www.linkedin.com/in/ACoAACJ3ikUBjuHqi35ibm8CG6IEYv-v_VsobIs?lipi=urn%3Ali%3Apage%3Ad_flagship3_pulse_read%3B4CDUdiVxT7WqLJNXO%2BI5bQ%3D%3D), 
Sachin Mudaliyar, [Thomas Zhu](https://www.linkedin.com/in/hanwen-zhu-483614189), 
and all [CK/CM users and contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md) for helping us to
validate, use and improve this open-source technology to automate
benchmarking and optimization of AI/ML systems in terms of performance,
accuracy, power and costs! We are also grateful to [HiPEAC](https://www.linkedin.com/company/hipeac) 
and [OctoML](https://www.linkedin.com/company/octoml) for
sponsoring initial development and Peter Mattson, David Kanter, Vijay
Janapa Reddi and Alexandros Karargyris for fruitful discussions.


### Dissemination

* [Forbes article](https://www.forbes.com/sites/karlfreund/2023/04/05/nvidia-performance-trounces-all-competitors-who-have-the-guts-to-submit-to-mlperf-inference-30/?sh=3c38d2866676)
* [ZDNet article](https://www.zdnet.com/article/nvidia-dell-qualcomm-speed-up-ai-results-in-latest-benchmark-tests)
* [LinkedIn article from Grigori Fursin (MLCommons Task Force co-chair)]( https://www.linkedin.com/pulse/announcing-my-new-project-reproducible-optimization-co-design-fursin )
* [Linkedin article from Arjun Suresh (MLCommons Task Force co-chair)](https://www.linkedin.com/posts/arjunsuresh_nvidia-performance-trounces-all-competitors-activity-7049500972275929088-nnnx?utm_source=share&utm_medium=member_desktop)
