[ [Back to index](README.md) ]

# MLCommons Task Force on Automation and Reproducibility

**News (May 2024):** our task force has successfully accomplished the first goal 
 to provide a [stable CM interface for MLPerf benchmarks](https://docs.mlcommons.org/inference) 
 and discussing the next steps with MLCommons - please stay tuned for more details!



## Mission

* Extend [MLCommons CM workflow automation framework](https://github.com/mlcommons/ck) and
  [reusable automation recipes (CM scripts)](https://access.cknowledge.org/playground/?action=scripts)
  to automate MLCommons projects and make it easier to assemble, run, reproduce, customize and optimize ML(Perf) benchmarks
  in a unified and automated way across diverse models, data sets, software and hardware from different vendors.
* Extend [CM workflows](https://github.com/mlcommons/cm4mlops) 
  to automate and reproduce MLPerf inference submissions from different vendors starting from v3.1.
* Encode MLPerf rules and best practices in the [CM automation recipes and workflows for MLPerf](https://github.com/mlcommons/cm4mlops/tree/main/script)
  to help MLPerf submitters avoid going through many README files and track all the latest MLPerf changes and updates.

## Sponsors

We thank [cKnowledge.org](https://cKnowledge.org), [cTuning.org](https://cTuning.org),
and [MLCommons](https://mlcommons.org) for sponsoring this project!


### Citing CM

If you found CM useful, please cite this article: 
[ [ArXiv](https://arxiv.org/abs/2406.16791) ], [ [BibTex](https://github.com/mlcommons/ck/blob/master/citation.bib) ].


## Current projects

* Continue improving CM to support different MLCommons projects for universal benchmarking and optimization across different platforms.

* Extend CM workflows to reproduce MLPerf inference v4.0 submissions (Intel, Nvidia, Qualcomm, Google, Red Hat, etc) via a unified interface.

* Prepare tutorial for MLPerf inference v4.1 submissions via CM.

* Discuss how to introduce the [CM automation badge]( https://github.com/mlcommons/ck/blob/master/docs/artifact-evaluation/reviewing.md ) 
  to MLPerf inference v4.1 submission similar to ACM/IEEE/NeurIPS reproducibility badges to make it easier for
  all submitters to re-run and reproduce each others’ results before the publication date.

* Develop a more universal Python and C++ wrapper for the MLPerf loadgen
  with the CM automation to support different models, data sets, software
  and hardware: [Python prototype](https://github.com/mlcommons/cm4mlops/tree/main/script/app-loadgen-generic-python); 
  [C++ prototype](https://github.com/mlcommons/cm4mlops/tree/main/script/app-mlperf-inference-mlcommons-cpp).

* Collaborate with system vendors and cloud providers to help them benchmark
  their platforms using the best available MLPerf inference implementation.

* Collaborate with other MLCommons working groups to autoamte, modularize and unify
  their benchmarks using [CM automation recipes](https://access.cknowledge.org/playground/?action=scripts).

* Use CM to modularize and automate the upcoming [automotive benchmark](https://mlcommons.org/working-groups/benchmarks/automotive/).

* Use [MLCommons Croissant](https://mlcommons.org/working-groups/data/croissant/) 
  to unify [MLPerf datasets](https://access.cknowledge.org/playground/?action=scripts).


## Current tasks

* Improving CM workflow automation framework: [GitHub ticket](https://github.com/mlcommons/ck/issues/1229)
* Updating/refactoring CM docs (framework and MLPef workflows): [GitHub ticket](https://github.com/mlcommons/ck/issues/1220)
* Improving CM scripts to support MLPerf: [GitHub ticket](https://github.com/mlcommons/cm4mlops/issues/21)
* Adding profiling and performance analysis during benchmarking: [GitHub ticket](https://github.com/mlcommons/cm4mlops/issues/23)
* Improving universal build and run scripts to support cross-platform compilation: [GitHub ticket](https://github.com/mlcommons/cm4mlops/issues/24)
* Automate ABTF benchmarking via CM: [GitHub ticket](https://github.com/mlcommons/cm4abtf/issues/6)
* Help automate MLPerf inference benchmark at the Student Cluster Competition'24: [GitHub ticket](https://github.com/mlcommons/cm4mlops/issues/26)

## Completed deliverables

* Developed [reusable and technology-agnostic automation recipes and workflows](https://access.cknowledge.org/playground/?action=scripts) 
  with a common and human-friendly interface (MLCommons Collective Mind aka CM) to modularize
  MLPerf inference benchmarks and run them in a unified and automated way
  across diverse models, data sets, software and hardware from different
  vendors.

* Added [GitHub actions](https://github.com/mlcommons/inference/tree/master/.github/workflows) 
  to test MLPerf inference benchmarks using CM.

* Encoded MLPerf inference rules and best practices in the [CM automation
  recipes and workflows for MLPerf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script) 
  and reduced the burden for submitters to go through numerous README files 
  and track all the latest changes and reproduce results.

* Automated [MLPerf inference submissions](https://access.cknowledge.org/playground/?action=howtorun) 
  and made it easier to re-run and reproduce results 
  (see [submitters orientation](https://doi.org/10.5281/zenodo.10605079) 
  and [CM-MLPerf documentation](https://github.com/mlcommons/ck/tree/master/docs/mlperf)).

* Started developing an open-source platform to automatically compose
  high-performance and cost-effective AI applications and systems using
  MLPerf and CM (see our [presentation at MLPerf-Bench at HPCA’24](https://doi.org/10.5281/zenodo.10786893)).

* Supported AI, ML and Systems conferences to automate artifact evaluation
  and reproducibility initiatives (see CM at [ACM/IEEE MICRO’23](https://ctuning.org/ae/micro2023.html) 
  and [SCC’23/SuperComputing’23](https://github.com/mlcommons/ck/blob/master/docs/tutorials/scc23-mlperf-inference-bert.md)).



## Resources

* [CM GitHub project](https://github.com/mlcommons/ck)
* [CM concept (keynote at ACM REP'23)]( https://doi.org/10.5281/zenodo.8105339 )
* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)
* [CM-MLPerf commands](https://github.com/mlcommons/ck/tree/master/docs/mlperf)
* [CM-MLPerf GUI](https://access.cknowledge.org/playground/?action=howtorun)
* [ACM artifact review and badging methodology](https://www.acm.org/publications/policies/artifact-review-and-badging-current) 
* [Artifact Evaluation at ML and systems conferences](https://cTuning.org/ae)
* [Terminology (ACM/NISO): Repeatability, Reproducibility and Replicability](artifact-evaluation/faq.md#what-is-the-difference-between-repeatability-reproducibility-and-replicability)
* [CM motivation (ACM TechTalk about reproducing 150+ research papers and validating them in the real world)](https://www.youtube.com/watch?v=7zpeIVwICa4)

## Acknowledgments

This task force was established by [Grigori Fursin](https://cKnowledge.org/gfursin) 
after he donated his CK and CM automation technology to MLCommons in 2022 to benefit everyone.
Since then, this open-source technology is being developed as a community effort based on user feedback.
We would like to thank all our [volunteers, collaborators and contributors](../CONTRIBUTING.md) 
for their support, fruitful discussions, and useful feedback! 

