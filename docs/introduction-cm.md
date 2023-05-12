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

This practical experience and the feedback from the community motivated 
us to establish the [MLCommons Task Force on Automation and Reproducibility](taskforce.md)
and develop a simple, technology agnostic, and English-like scripting language called Collective Mind (CM) 
powered by Python, JSON and/or YAML meta descriptions, and a unified CLI.

CM is intended to help researchers and practitioners describe, share, and reproduce experimental results 
in a unified, portable and automated way across any rapidly evolving software, hardware, and data
while automatically generating unified README files and synthesizing modular
containers with a unified CM API and CLI. 

Our goal is to use CM to facilitate reproducible AI/ML Systems research and minimizing 
manual and repetitive benchmarking and optimization efforts, reduce time and
costs for reproducible research, and simplify technology transfer
to production.




See a few real-world examples of using the CM scripting language:
- [README to reproduce published IPOL'22 paper](cm-mlops/script/app-ipol-reproducibility-2022-439)
- [README to reproduce MLPerf RetinaNet inference benchmark at Student Cluster Competition'22](docs/tutorials/sc22-scc-mlperf.md)
- [Auto-generated READMEs to reproduce official MLPerf BERT inference benchmark v3.0 submission with a model from the Hugging Face Zoo](https://github.com/mlcommons/submissions_inference_3.0/tree/main/open/cTuning/code/huggingface-bert/README.md)
- [Auto-generated Docker containers to run and reproduce MLPerf inference benchmark](cm-mlops/script/app-mlperf-inference/dockerfiles/retinanet)




# Archive (previous CK version before MLCommons)

* [Project overview](misc/overview.md)
* [History](misc/history.md)
