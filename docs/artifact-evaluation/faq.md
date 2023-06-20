[ [Back to index](https://cTuning.org/ae) ]

# Artifact Evaluation FAQ

<details>
<summary>Click here to see the table of contents.</summary>

* [Artifact evaluation](#artifact-evaluation)
  * [Frequently Asked Questions](#frequently-asked-questions)
    * [What is the difference between Repeatability, Reproducibility and Replicability?](#what-is-the-difference-between-repeatability-reproducibility-and-replicability?)
    * [Do I have to open source my software artifacts?](#do-i-have-to-open-source-my-software-artifacts?)
    * [Is Artifact evaluation blind or double-blind?](#is-artifact-evaluation-blind-or-double-blind?)
    * [How to pack artifacts?](#how-to-pack-artifacts?)
    * [Is it possible to provide a remote access to a machine with pre-installed artifacts?](#is-it-possible-to-provide-a-remote-access-to-a-machine-with-pre-installed-artifacts?)
    * [Can I share commercial benchmarks or software with evaluators?](#can-i-share-commercial-benchmarks-or-software-with-evaluators?)
    * [Can I engage with the community to evaluate my artifacts?](#can-i-engage-with-the-community-to-evaluate-my-artifacts?)
    * [How to automate, customize and port experiments?](#how-to-automate-customize-and-port-experiments?)
    * [Do I have to make my artifacts public if they pass evaluation?](#do-i-have-to-make-my-artifacts-public-if-they-pass-evaluation?)
    * [How to report and compare empirical results?](#how-to-report-and-compare-empirical-results?)
    * [How to deal with numerical accuracy and instability?](#how-to-deal-with-numerical-accuracy-and-instability?)
    * [How to validate models or algorithm scalability?](#how-to-validate-models-or-algorithm-scalability?)
    * [Is there any page limit for my Artifact Evaluation Appendix?](#is-there-any-page-limit-for-my-artifact-evaluation-appendix?)
    * [Where can I find a sample HotCRP configuration to set up AE?](#where-can-i-find-a-sample-hotcrp-configuration-to-set-up-ae?)
    * [Questions and Feedback](#questions-and-feedback)

</details>

## Frequently Asked Questions


**If you have questions or suggestions which are not addressed here, please feel free 
to contact the [public MLCommons task force on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md) 
via this [Discord server](https://discord.gg/JjWNWXKxwT) or post them to the dedicated [AE google group](https://groups.google.com/forum/#!forum/artifact-evaluation).**


### What is the difference between Repeatability, Reproducibility and Replicability?

We use the following definitions [adopted by ACM and NISO](https://www.acm.org/publications/policies/artifact-review-badging):

* *Repeatability (Same team, same experimental setup)*

  The measurement can be obtained with stated precision by the same team using the same measurement procedure, 
  the same measuring system, under the same operating conditions, in the same location on multiple trials. 
  For computational experiments, this means that a researcher can reliably repeat her own computation.

* *Reproducibility (Different team, different experimental setup)*

  The measurement can be obtained with stated precision by a different team using the same measurement procedure, 
  the same measuring system, under the same operating conditions, in the same or a different location on multiple trials. 
  For computational experiments, this means that an independent group can obtain the same result using the author's own artifacts.

* *Replicability (Different team, same experimental setup)*

  The measurement can be obtained with stated precision by a different team, a different measuring system, 
  in a different location on multiple trials. For computational experiments, this means that an independent group 
  can obtain the same result using artifacts which they develop completely independently.



### Do I have to open source my software artifacts?



No, it is not strictly necessary and you can 
provide your software artifact as a binary.
However, in case of problems, reviewers may not be 
able to fix it and will likely give you a negative score.


### Is Artifact evaluation blind or double-blind?



AE is a single-blind process, i.e. authors' names are known to the evaluators
(there is no need to hide them since papers are accepted),
but names of evaluators are not known to authors.
AE chairs are usually used as a proxy between authors and evaluators
in case of questions and problems.


### How to pack artifacts?



We do not have strict requirements at this stage. You can pack 
your artifacts simply in a tar ball, zip file, Virtual Machine or Docker image.
You can also share artifacts via public services including GitHub, GitLab and BitBucket.

Please see [our submission guide](submission.md) for more details.


### Is it possible to provide a remote access to a machine with pre-installed artifacts?



Only in exceptional cases, i.e. when rare hardware or proprietary software/benchmarks are required,
or VM image is too large or when you are not authorized to move artifacts outside your organization.
In such case, you will need to send the access information 
to the AE chairs via private email or SMS. 
They will then pass this information to the evaluators.


### Can I share commercial benchmarks or software with evaluators?



Please check the license of your benchmarks, data sets and software. 
In case of any doubts, try to find a free alternative. In fact, 
we strongly suggest you provide a small subset of free benchmarks 
and data sets to simplify the evaluation process.


### Can I engage with the community to evaluate my artifacts?



Based on the community feedback, we allow open evaluation
to let the community validate artifacts which are publicly available 
at GitHub, GitLab, BitBuckets, etc, report issues and help the authors 
to fix them. 

Note, that in the end, these artifacts still go through traditional
evaluation process via the AE committee. We successfully validated 
at [ADAPT'16](http://adapt-workshop.org/motivation2016.html)
and CGO/PPoPP'17!


### How to automate, customize and port experiments?



From our [past experience reproducing research papers](https://www.reddit.com/r/MachineLearning/comments/ioq8do/n_reproducing_150_research_papers_the_problems), 
the major difficulty that evaluators face is the lack of a common and portable workflow framework
in ML and systems research. This means that each year they have 
to learn some ad-hoc scripts and formats in nearly 
all artifacts without even reusing such knowledge the following year.

Things get even worse if an evaluator would like to validate experiments 
using a different compiler, tool, library, data set, operating systems or hardware
rather than just reproducing quickly outdated results using 
VM and Docker images - our experience shows that most of the submitted scripts 
are not easy to change, customize or adapt to other platform.

That is why we collaborate with the [open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)
and [ACM](https://acm.org) to develop a [portable automation framework](https://github.com/mlcommons/ck/tree/master/docs) to make it easier to reproduce experiments
across continuously changing software, hardware and data.

Please join this [taskforce](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md)
or get in touch with [the AE community](https://groups.google.com/forum/#!forum/artifact-evaluation) 
to discuss how to automate your artifacts and make them more portable and reusable.


### Do I have to make my artifacts public if they pass evaluation?

No, you don't have to and it may be impossible in the case of commercial artifacts.
Nevertheless, we encourage you to make your artifacts publicly available upon publication, 
for example, by including them in a permanent repository (required to receive the "artifact available" badge)
to support open science as outlined in [our vision](http://dl.acm.org/citation.cfm?id=2618142).


Furthermore, if you make your artifacts publicly available at the time
of submission, you may profit from the "public review" option, where you are engaged
with the community to discuss, evaluate and use your software. See such
examples [here](https://cTuning.org/ae/artifacts.html) (search for "public evaluation").


### How to report and compare empirical results?


**News:** Please check the [SIGPLAN Empirical Evaluation Guidelines](https://www.sigplan.org/Resources/EmpiricalEvaluation)
and the [NeurIPS reproducibility checklist](https://www.cs.mcgill.ca/~jpineau/ReproducibilityChecklist.pdf).
  
  

First of all, you should undoubtedly run empirical experiments more than once 
(we still encounter many cases where researchers measure execution time only once).
and perform statistical analysis.

There is no universal recipe how many times you should repeat your empirical experiment 
since it heavily depends on the type of your experiments, platform and environment. 
You should then analyze the distribution of execution times as shown in the figure below:

![](https://raw.githubusercontent.com/mlcommons/ck/master/docs/artifact-evaluation/image-994e7359d7760ab1-cropped.png)
If you have more than one expected value (b), it means that you have several
run-time states in your system (such as adaptive frequency scaling) 
and you can not use average and reliably compare empirical results.

However, if there is only one expected value for a given experiment (a), 
then you can use it to compare multiple experiments. This is particularly
useful when running experiments across different platforms from different
users as described in this [article](https://cknow.io/c/report/rpi3-crowd-tuning-2017-interactive).
 

You should also report the variation of empirical results together with all expected values.
Furthermore, we strongly suggest you to pre-record results from your platform
and provide a script to automatically compare new results with the pre-recorded ones.
Otherwise, evaluators can spend considerable amount of time 
digging out and validating results from "stdout".

For example, see how new results are visualized and compared against the pre-recorded ones
using [some dashboard](https://github.com/SamAinsworth/reproduce-cgo2017-paper/files/618737/ck-aarch64-dashboard.pdf) 
in the [CGO'17 artifact](https://github.com/SamAinsworth/reproduce-cgo2017-paper).




### How to deal with numerical accuracy and instability?



If the accuracy of your results depends on a given machine, environment and optimizations 
(for example, when optimizing BLAS, DNN, etc), you should provide a script to automatically 
report unexpected loss in accuracy above provided threshold as well as any numerical instability.


### How to validate models or algorithm scalability?



If you present a novel parallel algorithm or some predictive model which should scale 
across a number of cores/processors/nodes, we suggest you 
to provide an experimental workflow that could automatically detect the topology 
of a user machine, validate your models or algorithm scalability, 
and report any unexpected behavior. 


### Is there any page limit for my Artifact Evaluation Appendix?



There is no limit for the AE Appendix at the time of the submission for Artifact Evaluation.


However, there is currently a 2 page limit for the AE Appendix in the camera-ready CGO, PPoPP, ASPLOS and MLSys papers.
There is no page limit for the AE Appendix in the camera-ready SC paper. We also expect 
that there will be no page limits for AE Appendices in the journals willing to participate 
in the AE initiative.


### Where can I find a sample HotCRP configuration to set up AE?



Please, check out our [PPoPP'19 HotCRP configuration for AE](https://www.linkedin.com/pulse/acm-ppopp19-artifact-evaluation-report-hotcrp-grigori-fursin) 
in case you need to set up your own HotCRP instance.




### Questions and Feedback



If you have any questions, do not hesitate to get in touch with the AE community 
using this [public discussion group](https://groups.google.com/forum/#!forum/artifact-evaluation)!

