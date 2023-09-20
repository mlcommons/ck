On this page, we highlight some of the exciting submissions done by CTuning for the MLCommons Inference 3.1 round.

## Top Results in Edge Category

In the edge category, Rigel Supercomputers from One Stop Systems achieved the peak offline performance for the four submitted benchmarks - Image classification (ResNet50), Object detection (RetinaNet), Language processing (Bert) and Speech Recognition (RNNT). The below graph compares the peak performance of bert-99 model among the top 10 performing systems.  

![image](https://github.com/ctuning/mlcommons-ck/assets/4791823/9f8e3367-1ca4-4298-8545-285cdedfc991)


Nvidia RTX 4090 has the best performance for performance per accelerator, and this accelerator is assembled on a PC made by PCSPECIALIST UK. The below graph compares the performance per accelerator of bert-99 model among the top 10 performing systems.  

![image](https://github.com/ctuning/mlcommons-ck/assets/4791823/c02120cb-eda9-4eef-9e22-56fff4bf23a7)


Nvidia RTX 4090 wins the latency metric too for ResNet50, Bert and 3d-unet in the SingleStream scenario. 
![image](https://github.com/ctuning/mlcommons-ck/assets/4791823/6d4b39a0-9f39-474a-ac16-5498e281ebad)

![image](https://github.com/ctuning/mlcommons-ck/assets/4791823/8afb5609-581d-4ee8-be56-731af731f10f)

![image](https://github.com/ctuning/mlcommons-ck/assets/4791823/5cb88f53-9255-4a0b-98df-a192ba87b125)


## Best energy efficient results in Edge category

For the Speech Recognition model rnnt, CTuning submitted the best power-efficient result on Nvidia Jetson Orin AGX.

![image](https://github.com/ctuning/mlcommons-ck/assets/4791823/d485aa50-a0d4-4a40-a805-cc2ddc3e0ca6)


For the Medical Imaging model 3d-unet where the samples per second is quite low, the best 4 energy efficient results are by CTuning.

![image](https://github.com/ctuning/mlcommons-ck/assets/4791823/d15297fb-3eff-47c9-b188-68d438b7f248)

For the Language Processing model bert-99, gloria highend system from Qualcomm tops the energy efficiency metric and CTuning's Nvidia Jetson Orin AGX is at second place.

![image](https://github.com/ctuning/mlcommons-ck/assets/4791823/22c85404-51f5-44b7-b128-8df4579c635c)



## Benchmarking Rigel Supercomputer

Rigel Edge Supercomputer from OneStopSytems wins the peak performance for all four submitted models and comfortably beats the second-place system. It also wins the best latency for ResNet50 MultiStream scenario.


![image](https://github.com/ctuning/mlcommons-ck/assets/4791823/635f5f29-080f-4c7c-85a5-65fcf438f9e1)

![image](https://github.com/ctuning/mlcommons-ck/assets/4791823/c993c2f5-a8b7-4a11-b89f-35d96e357e42)





## Benchmarking MLPerf Inference Reference Implementations

We compared the performance of the reference implementation with that of the Nvidia optimized implementation by running both implementations on an Nvidia RTX 4090 GPU. Reference implementation uses fp32 models whereas Nvidia implementation uses quantized models.  

![image](https://github.com/ctuning/mlcommons-ck/assets/4791823/b46bc509-f242-4bc6-a9e8-ec318d09616b)

![image](https://github.com/ctuning/mlcommons-ck/assets/4791823/404b54d2-a04e-4e5e-861d-43c7d940faf8)

![image](https://github.com/ctuning/mlcommons-ck/assets/4791823/f5a04e85-269f-485a-8839-348dddcd5eb7)

## Showcasing Apple Metal Performance

We benchmarked the performance of Apple metal using Tensorflow-metal. The below graphs show the performance benefit of running inference on Apple meta using tensorflow-metal versus onnxruntime running only on CPUs. 

![image](https://github.com/ctuning/mlcommons-ck/assets/4791823/87385e24-b3b5-4694-8106-2c30eeb393de)

![image](https://github.com/ctuning/mlcommons-ck/assets/4791823/c9a38dc9-0986-461e-b81d-988297e1771e)

![image](https://github.com/ctuning/mlcommons-ck/assets/4791823/4b8565b4-7a23-4f29-b450-6eaf00d10f63)





## Design Space Exploration For NeuralMagic Deepsparse Library

Using CM experiment automation we did a design space exploration to find the optimal batch size for the bert-99 compatible sparse models.

![image](https://github.com/ctuning/mlcommons-ck/assets/4791823/a18088f2-c864-4c16-b714-5b375cf5fc94)

![image](https://github.com/ctuning/mlcommons-ck/assets/4791823/8bd95c5f-344f-4d9f-9f94-c3024efbce13)


## Comparing the performance of Modular MLPerf Inference C++ implementations

Here we compare the performance of MIL Library used by CTuning and the KILT library used by KRAI both on CPUs and GPUs. This is not an apple-to-apple comparison as KILT used Nvidia Nvidia A1000 GPU and MIL was run on Nvidia RTX 4090 GPU. For CPUs, KILT was run on a [24-core Dell server](https://github.com/mlcommons/inference_results_v3.1/blob/main/closed/Krai/systems/7920t-kilt-onnxruntime_cpu.json) with peak frequency of 4000 MHz whereas MIL was run on a [16 core PCSPECIALIST custom workstation](https://github.com/mlcommons/inference_results_v3.1/blob/main/closed/CTuning/systems/amd_ryzen_workstation-cpp-cpu-onnxruntime-vdefault-default_config.json) with peak frequency of 5900 MHz.

![image](https://github.com/ctuning/mlcommons-ck/assets/4791823/6d73360a-27ab-4158-b4cc-a5724d6d4c73)

![image](https://github.com/ctuning/mlcommons-ck/assets/4791823/d6b5516b-4861-4355-badf-65decbf8d3b0)

