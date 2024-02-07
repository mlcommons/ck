[ [Back to index](README.md) ]

# MLCommons Task force on Automation and Reproducibility

## Mission

* Develop [reusable automation recipes and workflows](https://access.cknowledge.org/playground/?action=components) 
  with [a common and human-friendly interface (Collective Mind aka CM)](https://github.com/mlcommons/ck) 
  to support MLCommons projects and help everyone assemble, run, reproduce, customize and optimize ML(Perf) benchmarks
  in a unified and automated way across diverse models, data sets, software and hardware from different vendors.
* Gradually extend a unified MLCommons CM interface to automate [all MLPerf inference submissions](https://github.com/mlcommons/ck/issues/1052) starting from v3.1.
* Continuously encode MLPerf rules and best practices in the [CM automation recipes and workflows for MLPerf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
  to reduce the burden for submitters to go through numerous README files 
  and track all the latest changes and updates.

## Chairs and Tech Leads

* [Grigori Fursin](https://cKnowledge.org/gfursin)
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh)

## Discussions

Since we already participate in many weekly conf-calls to support various MLCommons initiatives, 
we decided not to have yet another separate conf-call for our TF in 2024.
Instead, we discuss our progress on MLPerf automation and reproducibility at existing MLCommons conf-calls
where CM is used:
* [MLPerf inference WG](https://mlcommons.org/working-groups/benchmarks/inference): weekly conf-calls on Tuesday at 8:30am PST
* [MLPerf automotive WG](https://mlcommons.org/working-groups/benchmarks/automotive)
  * Automotive TF weekly conf-calls on Wednesday at 8am PST
  * Automotive implementation bi-weekly conf-calls on Friday at 9:30am PST
* [Croissant TF](https://github.com/mlcommons/croissant): weekly at 8am PST

You can participate in our discussions via [public Discord server](https://discord.gg/JjWNWXKxwT).

## Status

### 2023

Following our [regular public weekly conf-calls in 2023](https://docs.google.com/document/d/1zMNK1m_LhWm6jimZK6YE05hu4VH9usdbKJ3nBy-ZPAw), 
[Discord discussions](https://discord.gg/JjWNWXKxwT) and very useful feedback from the research community, 
Google, AMD, Neural Magic, OctoML, Nvidia, Qualcomm, Dell, HPE, Red Hat,
Intel, TTA, One Stop Systems and other organizations, we have developed a new version 
of the [Collective Mind automation framework (CM)](https://github.com/mlcommons/ck) as a very lightweight, 
non-intrusive and technology-agnostic workflow automation framework that provides a common, simple 
and human-readable interface to manage, run, reproduce and customize MLPerf benchmarks
across continuously changing models, datasets, software and hardware from different vendors:
[github.com/mlcommons/ck/tree/master/docs/mlperf](https://github.com/mlcommons/ck/tree/master/docs/mlperf).
 
#### Outcome

* We have released the new CM version 1.5.3 and successfully validated it with the community during MLPerf inference v3.1 submission 
  enabling the 1st mass submission of 12K+ performance and power results across 120+ system configurations.

* We continued extending [Modular C++ Inference Library for MLPerf (MIL)](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-cpp) 
  and validated it in the v3.1 round. We also developed a Python prototype of the reference network implementation
  with CM interface for BERT model and added it to the [main inference repository](https://github.com/mlcommons/inference/tree/master/language/bert#loadgen-over-the-network).

* We successfully introduced CM automation at the [ACM/IEEE International Symposium on Microarchitecture (MICRO'23)](https://cTuning.org/ae/micro2023.html)
  to reproduce results from accepted research papers: [GitHub](https://github.com/ctuning/cm-reproduce-research-projects/tree/main/script)
  
* We successfully introduced CM automation at the [Student Cluster Competition at SuperComputing'23](https://github.com/mlcommons/ck/blob/master/docs/tutorials/scc23-mlperf-inference-bert.md)
  to run MLPerf inference benchmarks across diverse hardware. It resulted in different contributions to improve MLPerf inference benchmarks
  (such as adding AMD GPU backend) and CM workflows.

* We gave invited keynote about CM at the 1st ACM Conference on Reproducibility and Replicability: 
  [Slides](https://doi.org/10.5281/zenodo.8105339), [ACM YouTube channel](https://www.youtube.com/watch?v=_1f9i_Bzjmg)


### 2024

We are requested to focus on the following tasks:

1) Continue extending CM interface and workflows to reproduce as many MLPerf inference v3.1 submissions as possible: see [current coverage](https://github.com/mlcommons/ck/issues/1052)
2) Help all MLPerf inference v4.0 submitters automate their submissions and provide a common CM interface to rerun them in a unified way
3) Apply standard [ACM artifact review and badging methodology](https://www.acm.org/publications/policies/artifact-review-and-badging-current) 
   with [cTuning extensions to ML and systems conferences](https://cTuning.org/ae) 
   to MLPerf inference v4.0 submission to make it easier to rerun experiments and reproduce results (see [ACM Tech Talk](https://www.youtube.com/watch?v=7zpeIVwICa4) 
   and [ACM REP keynote](https://doi.org/10.5281/zenodo.8105339) to learn more about our vision and related experience).
4) Add CM support for the new automotive benchmark
5) Extend [CM GUI](https://cknowledge.org/cm-gui/?tags=generic,app,mlperf,inference) to help users generate CM commands to customize and run MLPerf inference benchmarks
6) Extend [Modular C++ Inference Library for MLPerf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-cpp) to support more models and backends

## Resources

* [Invited keynote about CM framework at ACM REP'23](https://doi.org/10.5281/zenodo.8105339)
* [ACM artifact review and badging methodology](https://www.acm.org/publications/policies/artifact-review-and-badging-current) 
* [Artifact Evaluation at ML and systems conferences](https://cTuning.org/ae)
* [Terminology (ACM/NISO): Repeatability, Reproducibility and Replicability](artifact-evaluation/faq.md#what-is-the-difference-between-repeatability-reproducibility-and-replicability)
* [ACM TechTalk about reproducing 150+ research papers and validating them in the real world](https://www.youtube.com/watch?v=7zpeIVwICa4)
