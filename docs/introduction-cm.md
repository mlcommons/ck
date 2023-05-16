[ [Back to index](README.md) ]

# Introduction to the MLCommons CM language

During the past 10 years, the community has considerably improved 
the reproducibility of experimental results from research projects and published papers
by introducing the [artifact evaluation process](https://cTuning.org/ae) 
with a [unified artifact appendix and reproducibility checklists](https://github.com/mlcommons/ck/blob/master/docs/artifact-evaluation/checklist.md), 
Jupyter notebooks, containers, and Git repositories. 

On the other hand, [our experience reproducing more than 150 papers](https://learning.acm.org/techtalks/reproducibility)
shows that it still takes weeks and months of painful and
repetitive interactions between teams to reproduce experimental results. 
This effort includes decrypting numerous README files, examining ad-hoc artifacts 
and containers, and figuring out how to reproduce computational results.
Furthermore, snapshot containers pose a challenge to optimize algorithms' performance, 
accuracy, power consumption and operational costs across diverse 
and rapidly evolving software, hardware, and data used in the real world.

![](https://raw.githubusercontent.com/ctuning/ck-guide-images/master/cm-ad-hoc-projects.png)

This practical experience and the feedback from the community motivated 
us to establish the [MLCommons Task Force on Automation and Reproducibility](taskforce.md)
and develop a simple, technology agnostic, and English-like automation language called Collective Mind (MLCommons CM).

This language provides a universal interface to any software project and transforms it 
into a database of [reusable automation actions](list_of_automations.md) 
and [portable scripts]( https://github.com/mlcommons/ck/tree/master/cm-mlops/script )
in a transparent and non-intrusive way.
Following [FAIR principles](https://www.go-fair.org/fair-principles), CM automation actions and scripts 
are simple wrappers around existing user scripts and artifacts to make them
* findable via human-readable tags, aliases and unique IDs;
* accessible via a unified CM CLI and Python API with JSON/YAML meta descriptions;
* interoperable and portable across any software, hardware, models and data;
* reusable across all projects.

CM is powered by Python, JSON and/or YAML meta descriptions, and a unified CLI
to minimize the learning curve and help researchers and practitioners describe, share, and reproduce experimental results 
in a unified, portable, and automated way across any rapidly evolving software, hardware, and data
while solving the "dependency hell" and automatically generating unified README files and modular containers.

![](https://raw.githubusercontent.com/ctuning/ck-guide-images/master/cm-unified-projects.png)

Our ultimate goal is to use CM language to facilitate reproducible AI/ML Systems research, 
minimize manual and repetitive benchmarking and optimization efforts, 
and reduce time and costs when transferring technology to production
across continuously changing software, hardware, models, and data.


See a few real-world examples of using the CM scripting language:
- [README to reproduce published IPOL'22 paper](cm-mlops/script/app-ipol-reproducibility-2022-439)
- [README to reproduce MLPerf RetinaNet inference benchmark at Student Cluster Competition'22](docs/tutorials/sc22-scc-mlperf.md)
- [Auto-generated READMEs to reproduce official MLPerf BERT inference benchmark v3.0 submission with a model from the Hugging Face Zoo](https://github.com/mlcommons/submissions_inference_3.0/tree/main/open/cTuning/code/huggingface-bert/README.md)
- [Auto-generated Docker containers to run and reproduce MLPerf inference benchmark](cm-mlops/script/app-mlperf-inference/dockerfiles/retinanet)




# Archive (previous CK version before MLCommons)

* [Project overview](misc/overview.md)
* [History](misc/history.md)
