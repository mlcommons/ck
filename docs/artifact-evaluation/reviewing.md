[ [Back to index](https://cTuning.org/ae) ]

# Artifact evaluation

This document provides the guidelines to evaluate artifacts at ACM and IEEE conferences.

## Overview

Shortly after the artifact submission deadline, the AE committee members 
will bid on artifacts they would like to evaluate based on their competencies 
and the information provided in the artifact abstract such as software and hardware dependencies
while avoiding possible conflicts of interest.

Within a few days, the AE chairs will make the final selection of evaluators
to ensure at least two or more evaluators per artifact.

Evaluators will then have approximately 1 months to review artifacts via HotCRP,
discuss with the authors about all encountered issues and help them fix all the issues.
Remember that our philosophy of artifact evaluation is not to fail problematic artifacts 
but to help the authors improve their public artifacts, pass evaluation
and improve their Artifact Appendix.

In the end, the AE chairs will decide on a set of the standard ACM reproducibility badges (see below)
to award to a given artifact based on all reviews and the authors' responses.
Such badges will be printed on the 1st page of the paper and will be available 
as meta information in the [ACM Digital Library](https://dl.acm.org)

Authors and reviewers are encouraged to check the [AE FAQ](faq.md)
and contact chairs and the community via our [Discord server for automation and reproducibility](https://discord.gg/JjWNWXKxwT) 
or the [dedicated AE google group](https://groups.google.com/forum/#!forum/artifact-evaluation)
in case of questions or suggestions.


## ACM reproducibility badges

Reviewers must read a paper and then thoroughly go through the Artifact Appendix 
to evaluate shared artifacts. They should then describe their experience 
at each stage (success or failure, encountered problems and how they were possibly solved, 
and questions or suggestions to the authors), and give a score on scale -1 .. +1:

- *+1* if exceeded expectations
- *0* if met expectations (or inapplicable)
- *-1* if fell below expectations

### Artifacts available

* Are all artifacts related to this paper publicly available?

*Note that it is not obligatory to make artifacts publicly available!*

![](https://www.acm.org/binaries/content/gallery/acm/publications/replication-badges/artifacts_available_dl.jpg)

The author-created artifacts relevant to this paper will receive an ACM "artifact available" badge 
**only if** they have been placed on a publicly accessible archival repository
such as [Zenodo](https://zenodo.org), [FigShare](https://figshare.com),
and [Dryad](http://datadryad.org).

A DOI will be then assigned to their artifacts and must be provided in the Artifact Appendix!

*Notes:*

* ACM does not mandate the use of above repositories. However, publisher repositories,
  institutional repositories, or open commercial repositories are acceptable
  **only** if they have a declared plan to enable permanent accessibility!
  **Personal web pages, GitHub, GitLab and BitBucket are not acceptable for this purpose.**
* Artifacts do not need to have been formally evaluated in order for an article
  to receive this badge. In addition, they need not be complete in the sense
  described above. They simply need to be relevant to the study and add value
  beyond the text in the article. Such artifacts could be something as simple
  as the data from which the figures are drawn, or as complex as a complete
  software system under study.
* The authors can provide the DOI at the very end of the AE process 
  and use GitHub or any other convenient way to access their artifacts 
  during AE.


### Artifacts functional

* Are all components relevant to evaluation included in the package? 
* Well documented? Enough to understand, install and evaluate artifact?
* Exercisable? Includes scripts and/or software to perform appropriate experiments and generate results?
* Consistent? Artifacts are relevant to the associated paper and contribute in some inherent way to the generation of its main results?

![](https://www.acm.org/binaries/content/gallery/acm/publications/replication-badges/artifacts_evaluated_functional_dl.jpg)

*Note that proprietary artifacts need not be included. If they are required
to exercise the package then this should be documented, along with instructions
on how to obtain them. Proxies for proprietary data should be included so as to
demonstrate the analysis.*

The artifacts associated with the paper will receive an 
"Artifacts Evaluated - Functional" badge *only if* they are found to be documented, consistent,
complete, exercisable, and include appropriate evidence of verification and validation.

We usually ask the authors to provide a small/sample data set to validate at least
some results from the paper to make sure that their artifact is functional.

### Results reproduced

* Was it possible to validate the key results from the paper using provided artifacts? 

![](https://www.acm.org/binaries/content/gallery/acm/publications/replication-badges/results_reproduced_dl.jpg)

*You should report any unexpected artifact behavior to the authors (depends on the type of artifact such as unexpected output, scalability issues, crashes, performance variation, etc).*

The artifacts associated with the paper will receive a "Results reproduced" badge *only if* the key results 
of the paper have been obtained in a subsequent study by a person or team other than the authors, using 
artifacts provided by the author.

Some variation of empirical and numerical results is tolerated.
In fact it is often unavoidable in computer systems research - see
"how to report and compare empirical results" in the
[AE FAQ](faq.md) page,  the [SIGPLAN Empirical Evaluation Guidelines](https://www.sigplan.org/Resources/EmpiricalEvaluation),
and the [NeurIPS reproducibility checklist](https://www.cs.mcgill.ca/~jpineau/ReproducibilityChecklist.pdf).

*Since it may take weeks and even months to rerun some complex experiments 
 such as deep learning model training, we are discussing a staged AE where we will first validate that
 artifacts are functional before the camera ready paper deadline, and then
 use a separate AE with the full validation of all experimental results 
 with open reviewing and without strict deadlines. We successfully validated
 a similar approach at the [MLCommons open reproducibility and optimization challenges)](https://access.cKnowledge.org)
 and there is a related initiative at the [NeurIPS conference](https://openreview.net/group?id=NeurIPS.cc/2019/Reproducibility_Challenge).*

### Artifacts reusable (pilot project with MLCommons)

Since the criteria for the ACM "Artifacts Evaluated – Reusable" badge are very vague, we have partnered with
[MLCommons](https://mlcommons.org) to add their [unified and technology-agnostic Collective Mind automation interface (MLCommons CM)](https://doi.org/10.5281/zenodo.8105339)
to the shared artifacts.

This non-intrusive interface was successfully validated to automate and unify the [Student Cluster Competition at SuperComputing'22](https://github.com/mlcommons/ck/blob/master/docs/tutorials/sc22-scc-mlperf.md)
and diverse [MLPerf benchmark community submissions and recent research papers](https://access.cknowledge.org/playground).

That is why we would like to test it as a possible criteria to obtain the ACM "Artifacts Evaluated – Reusable" badge.

Our goal is to help the community access diverse research projects, reproduce results and reuse artifacts
in a unified and automated way across continuously evolving software and hardware.

*Note that it will be possible to prepare and run experiments without this interface too.*

The authors will get free help from MLCommons and the community via the [public Discord server](https://discord.gg/JjWNWXKxwT)
and/or can try to add the MLCommons CM interface to their artifacts themselves using this [https://github.com/mlcommons/ck/blob/master/docs/tutorials/common-interface-to-reproduce-research-projects.mdtutorial).




## Distinguished artifact award

When arranged by the event, an artifact can receive a distinguished artifact award if it is functional, well-documented, portable, easily reproducible and reusable by the community.

----

*This document was prepared by [Grigori Fursin](https://cKnowledge.org/gfursin)
 with contributions from [Bruce Childers](https://people.cs.pitt.edu/~childers), 
 [Michael Heroux](https://www.sandia.gov/~maherou), 
 [Michela Taufer](https://gcl.cis.udel.edu/personal/taufer) and others.
 It is maintained by the [cTuning foundation](https://cTuning.org/ae) and the 
 [open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md).*
