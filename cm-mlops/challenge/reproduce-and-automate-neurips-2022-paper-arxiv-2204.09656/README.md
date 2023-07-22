### Challenge

Reproduce and automate NeurIPS 2022 paper "A Fast Post-Training Pruning Framework for Transformers" 
using the [CM automation language](https://doi.org/10.5281/zenodo.8105339).

Convert models to ONNX format acceptable by the MLPerf BERT inference benchmark.

Create multiple BERT variations in ONNX format for the MLPerf inference v3.1 submission
with different levels of sparsity.

Upload to the [cTuning space at Hugging Face](https://huggingface.co/ctuning).

Run MLPerf inference v3.1 with all BERT variations on any platform and submit results to MLPerf inference v3.1.

Join our public [Discord server](https://discord.gg/JjWNWXKxwT) and/or
our [weekly conf-calls](https://docs.google.com/document/d/1zMNK1m_LhWm6jimZK6YE05hu4VH9usdbKJ3nBy-ZPAw/edit)
to discuss this challenge with the organizers.

Read [this documentation](https://github.com/mlcommons/ck/blob/master/docs/mlperf/inference/README.md) 
to run reference implementations of MLPerf inference benchmarks 
using the CM automation language and use them as a base for your developments.

Check [this ACM REP'23 keynote](https://doi.org/10.5281/zenodo.8105339) to learn more about our open-source project and long-term vision.

### Prizes

* *All contributors will participate in writing a common white paper about running and comparing MLPerf inference benchmarks out-of-the-box.*
* *All contributors will receive 1 point for submitting valid results for 1 complete benchmark on one system.*
* *All contributors will receive an official MLCommons Collective Knowledge contributor award (see [this example](https://ctuning.org/awards/ck-award-202307-zhu.pdf)).*
* *The first implementation will receive 3 points and a prize of 300$.*


#### Organizers

* Grigori Fursin
* Arjun Suresh
* [cTuning foundation](https://cTuning.org)
* [cKnowledge Ltd](https://cKnowledge.org)

### Initial discussion and materials

* [ArXiv](https://arxiv.org/abs/2204.09656)
* [Code](https://github.com/WoosukKwon/retraining-free-pruning)

