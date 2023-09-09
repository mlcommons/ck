[ [Back to index](README.md) ]

# Introduction to the MLCommons CK playground

[Collective Knowledge playground (MLCommons CK)](https://access.cKnowledge.org)
is an open-source and technology-agnostic automation platform
being developed by the [MLCommons Task Force on Automation and Reproducibility](taskforce.md),
[cTuning.org](https://cTuning.org) and [cKnowledge.org](https://cKnowledge.org).
 
CK is intended to help everyone automatically co-design optimal software and hardware for AI and ML 
and deploy them in the real-world in the fastest and most efficient way 
while slashing all research, development, optimization and operational costs.

CK playground is powered by the portable, technology-agnostic, human-readable and open-source
[Collective Mind automation language](introduction-cm.md) adopted and extended by [MLCommons (50+ companies and universities)](https://mlcommons.org)
to collaboratively benchmark and optimize AI and ML systems across diverse software, hardware, models and data from different vendors.

The community continuously extends and improves CM via [portable and reusable CM scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
solve the "AI/ML dependency hell", interconnect incompatible software, hardware, models and data, and encode best practices and optimization techniques 
into powerful automation workflows in a transparent and non-intrusive way. 

While still in the prototyping stage, our open-source technology already helps MLCommons organizations, students and researchers 
automate and optimize [MLPerf benchmark submissions](https://access.cknowledge.org/playground/?action=experiments)
while contributing to more than half of all performance and power results for MLPerf inference benchmark since the beginning.

We thank [the community](https://access.cknowledge.org/playground/?action=contributors) 
for helping us to validate a prototype of the MLCommons CK playground by running and reproducing 
[MLPerf inference v3.0 benchmarks](https://access.cknowledge.org/playground/?action=experiments&tags=mlperf-inference,v3.0,community-submission,open,edge,image-classification,singlestream):
CK has helped to automatically interconnect very diverse technology from Neural Magic, Qualcomm, Krai, cKnowledge, OctoML, Deelvin, DELL, HPE, Lenovo, Hugging Face, Nvidia and Apple 
and run it across diverse CPUs, GPUs and DSPs with PyTorch, 
ONNX, QAIC, TF/TFLite, TVM and TensorRT using popular cloud providers (GCP, AWS, Azure) and individual servers and edge devices 
via our [MLPerf inference v3.0 challenge](https://access.cknowledge.org/playground/?action=challenges&name=optimize-mlperf-inference-v3.0-2023).

Read more about our long-term vision and the next plans in our 
[ACM REP'23 keynote "Toward a common language to facilitate reproducible research and technology transfer: challenges and solutions"]( https://doi.org/10.5281/zenodo.8105339 ).

See a few real-world examples of using the CK playground powered by the CM language:

- [Organizing reproducibility, replicability and optimization challenges](https://access.cknowledge.org/playground/?action=challenges&name=57cbc3384d7640f9)
- [Reproducing MLPerf inference benchmark and automating submissions](https://cKnowledge.org/mlperf-inference-gui)
- [Visualizing and comparing MLPerf inference benchmark results](https://access.cKnowledge.org/playground/?action=experiments&tags=mlperf-inference,all,open,edge,image-classification,singlestream)
- [Sharing reproducibility reports]( https://cKnowledge.org/mlperf-inf-v3.0-reproducibility-report )
- [Adding derived metrics such as power efficiency and/or cost efficiency]( https://cKnowledge.org/mlcommons-inference-gui )

Feel free to join our [discord server](https://discord.gg/JjWNWXKxwT) 
and participate in the [reproducibility and optimization challenges](https://access.cknowledge.org/playground/?action=challenges)

