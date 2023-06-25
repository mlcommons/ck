[ [Back to index](https://cTuning.org/ae) ]

# Artifact submission

This document provides the guidelines to submit your artifacts for evaluation at ACM and IEEE conferences.



## Motivation


It's becoming increasingly difficult to [reproduce results from CS papers](https://learning.acm.org/techtalks/reproducibility). 
Voluntarily Artifact Evaluation (AE) was successfully introduced
at program languages, systems and machine learning conferences and tournaments 
to validate experimental results by the independent AE Committee, share unified Artifact Appendices, 
and assign reproducibility badges.


AE promotes the reproducibility of experimental results 
and encourages artifact sharing to help the community quickly validate and compare alternative approaches.
Authors are invited to formally describe all supporting material (code, data, models, workflows, results) 
using the [unified Artifact Appendix and the Reproducibility Checklist template](checklist.md)
and submit it to the [single-blind AE process](reviewing.md).
Reviewers will then collaborate with the authors to evaluate their artifacts and assign the following
[ACM reproducibility badges](https://www.acm.org/publications/policies/artifact-review-and-badging-current):

 
![](https://www.acm.org/binaries/content/gallery/acm/publications/replication-badges/artifacts_available_dl.jpg)
![](https://www.acm.org/binaries/content/gallery/acm/publications/replication-badges/artifacts_evaluated_functional_dl.jpg)
![](https://www.acm.org/binaries/content/gallery/acm/publications/replication-badges/results_reproduced_dl.jpg)



## Preparing your Artifact Appendix and the Reproducibility Checklist


You need to prepare the [Artifact Appendix](https://github.com/mlcommons/ck/blob/master/docs/artifact-evaluation/template/ae.tex)
describing all software, hardware and data set dependencies, key results to be reproduced, and how to prepare, run and validated experiments.

Though it is relatively intuitive and based on our 
[past AE experience and your feedback](https://cTuning.org/ae/prior_ae.html), 
we strongly encourage you to check the 
the [Artifact Appendix guide](checklist.md),
[artifact reviewing guide](reviewing.md),
the [SIGPLAN Empirical Evaluation Guidelines](https://www.sigplan.org/Resources/EmpiricalEvaluation),
the [NeurIPS reproducibility checklist](https://www.cs.mcgill.ca/~jpineau/ReproducibilityChecklist.pdf)
and [AE FAQs](faq.md) before submitting artifacts for evaluation!

You can find the examples of Artifact Appendices 
in the following [reproduced papers](https://cknow.io/reproduced-papers).

 
*Since the AE methodology is slightly different at different conferences, we introduced the unified Artifact Appendix
 with the Reproducibility Checklist in 2014 to help readers understand what was evaluated and how! 
 Furthermore, artifact evaluation often helps to discover some minor mistakes in accepted papers -
 in such case you have a chance to add related notes and corrections
 in the Artifact Appendix of your camera-ready paper!*



## Preparing your experimental workflow


**You can skip this step if you want to share your artifacts without the validation of experimental results - 
 in such case your paper can still be entitled for the "artifact available" badge!**

We strongly recommend you to provide at least some automation scripts to build your workflow, 
all inputs to run your workflow, and some expected outputs to validate results from your paper.
You can then describe the steps to evaluate your artifact 
using README files or [Jupyter Notebooks](https://jupyter.org "https://jupyter.org").

Feel free to reuse [portable CM scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script) 
being developed by the MLCommons to automate common steps to prepare and run various benchmarks 
across continously changing software, hardware and data.


## Making artifacts available to evaluators


Most of the time, the authors make their artifacts available to the evaluators via GitHub,
GitLab, BitBucket or private repositories. Public artifact sharing allows
optional "open evaluation" which we have successfully validated at [ADAPT'16]( https://adapt-workshop.org)
and [ASPLOS-REQUEST'18](https://cknow.io/c/event/request-reproducible-benchmarking-tournament).
It allows the authors to quickly fix encountered issues during evaluation
before submitting the final version to archival repositories.


Other acceptable methods include:
* Using zip or tar files with all related code and data, particularly when your artifact
 should be rebuilt on reviewers' machines (for example to have a non-virtualized access to a specific hardware).
* Using [Docker](https://www.docker.com "https://www.docker.com"), [Virtual Box](https://www.virtualbox.org "https://www.virtualbox.org") and other containers and VM images.
* Arranging remote access to the authors' machine with the pre-installed software 
 - this is an exceptional cases when rare or proprietary software and hardware is used.
 You will need to privately send the private access information to the AE chairs.


Note that your artifacts will receive the ACM "artifact available" badge
**only if** they have been placed on any publicly accessible archival repository
such as [Zenodo](https://zenodo.org "https://zenodo.org"), [FigShare](https://figshare.com "https://figshare.com"),
and [Dryad](http://datadryad.org "http://datadryad.org"). 
You will need to provide a DOI automatically assigned to your artifact by these repositories 
in your final Artifact Appendix!





## Submitting artifacts




Write a brief abstract describing your artifact, the minimal hardware and software requirements, 
how it supports your paper, how it can be validated and what the expected result is. 
Do not forget to specify if you use any proprietary software or hardware!
This abstract will be used by evaluators during artifact bidding to make sure that
they have an access to appropriate hardware and software and have required skills.


Submit the artifact abstract and the PDF of your paper with the Artifact Appendix attached 
using the AE submission website provided by the event.






## Asking questions

 If you have questions or suggestions, 
 do not hesitate to get in touch with the the AE chairs or the community using 
 the public [Discord server](https://discord.gg/JjWNWXKxwT),
 [Artifact Evaluation google group](https://groups.google.com/forum/#!forum/artifact-evaluation)
 and weekly conf-calls of the [open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md).

## Preparing your camera-ready paper

If you have successfully passed AE with at least one reproducibility badge, 
you will need to add up to 2 pages of your artifact appendix 
to your camera ready paper while removing all unnecessary or confidential information. 
This will help readers better understand what was evaluated and how.


If your paper is published in the ACM Digital Library,
you do not need to add reproducibility stamps - ACM will add them to your camera-ready paper
and will make this information available for search!

In other cases, AE chairs will tell you how to add stamps to the first page of your paper.




## Examples of reproduced papers with shared artifacts and Artifact Appendices:



* [Some papers from the past AE](https://cknow.io/?q=%22reproduced-papers%22) (ASPLOS, MICRO, MLSys, Supercomputing, CGO, PPoPP, PACT, IA3, ReQuEST)
* [Dashboards with reproduced results](https://cknow.io/?q=%22reproduced-results%22)
* Paper "Highly Efficient 8-bit Low Precision Inference of Convolutional Neural Networks with IntelCaffe" from ACM ASPLOS-ReQuEST'18  
  * [Paper DOI](https://doi.org/10.1145/3229762.3229763)
  * [Artifact DOI](https://doi.org/10.1145/3229769)
  * [Original artifact](https://github.com/intel/caffe/wiki/ReQuEST-Artifact-Installation-Guide)
  * [Portable automation](https://github.com/ctuning/ck-request-asplos18-caffe-intel)
  * [Expected results](https://github.com/ctuning/ck-request-asplos18-results-caffe-intel)
  * [Public scoreboard](https://cknow.io/result/pareto-efficient-ai-co-design-tournament-request-acm-asplos-2018)
* Paper "Software Prefetching for Indirect Memory Accesses" from CGO'17  
  * [Portable automation at GitHub](https://github.com/SamAinsworth/reproduce-cgo2017-paper)
  * [CK dashboard snapshot](https://github.com/SamAinsworth/reproduce-cgo2017-paper/files/618737/ck-aarch64-dashboard.pdf)




----

*This document was prepared by [Grigori Fursin](https://cKnowledge.org/gfursin "https://cKnowledge.org/gfursin")
 with contributions from [Bruce Childers](https://people.cs.pitt.edu/~childers "https://people.cs.pitt.edu/~childers"), 
 [Michael Heroux](https://www.sandia.gov/~maherou "https://www.sandia.gov/~maherou"), 
 [Michela Taufer](https://gcl.cis.udel.edu/personal/taufer/ "https://gcl.cis.udel.edu/personal/taufer/") and others.
 It is maintained by the [cTuning foundation](https://cTuning.org/ae) and the 
 [open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md).*
