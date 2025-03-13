This document narrates the history of the creation and design of CM, CM4MLOps and MLPerf automations (also known as CK2) 
by [Grigori Fursin](https://cKnowledge.org/gfursin). It also highlights the donation of this open-source technology to MLCommons, 
aimed at benefiting the broader community and fostering its ongoing development as a collaborative, community-driven initiative:

* Jan 28, 2021: After delivering an invited ACM TechTalk'21 about the Collective Knowledge framework (CK1) 
  and reproducibility initiatives for conferences, as well as CK-MLOps and MLPerf automations, 
  Grigori received useful feedback and suggestions for improvements to workflow automations:
  https://learning.acm.org/techtalks/reproducibility. 

  Following this, Grigori began prototyping CK2 (later CM) to streamline CK1, CK-MLOps and MLPerf benchmarking. 
  The goal was to dramatically simplify CK1 workflows by introducing just a few core and portable automations, 
  which eventually evolved into `CM script` and `CM cache`.

  At that time, the cTuning foundation hosted CK1 and all the prototypes for the CM framework at https://github.com/ctuning/ck:
  [ref1](https://github.com/mlcommons/ck/commit/9e57934f4999db23052531e92160772ab831463a), 
  [ref2](https://github.com/mlcommons/ck/tree/9e57934f4999db23052531e92160772ab831463a),
  [ref3](https://github.com/mlcommons/ck/tree/9e57934f4999db23052531e92160772ab831463a/incubator).

* Sep 23, 2021: donated CK1, CK-MLOps, MLPerf automations and early prototypes of CM from the cTuning repository to MLCommons:
  [ref1](https://web.archive.org/web/20240803140223/https://octo.ai/blog/octoml-joins-the-community-effort-to-democratize-mlperf-inference-benchmarking),
  [ref2](https://github.com/mlcommons/ck/tree/228f80b0bf44610c8244ff0c3f6bec5bbd25aa6c/incubator),
  [ref3](https://github.com/mlcommons/ck/tree/695c3843fd8121bbdde6c453cd6ec9503986b0c6?tab=readme-ov-file#author-and-coordinator),
  [ref4](https://github.com/mlcommons/ck/tree/master/ck),
  [ref5](https://github.com/mlcommons/ck-mlops).

  Prepared MLCommons proposal for the creation of the [MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md),
  aimed at fostering community-driven support for CK and CM developments to benefit everyone.

* Jan, 2022: hired Arjun Suresh at OctoML to support and maintain CK1 framework and help prepare OctoML's MLPerf submissions using CK1.
  Meanwhile, transitioned to focusing on CM and CM-MLOps development, building upon the prototypes created in 2021.

* Mar 1, 2022: started developing cm-mlops: [ref](https://github.com/octoml/cm-mlops/commit/0ae94736a420dfa84f7417fc62d323303b8760c6).

* Mar 24, 2022: after successfully stabilizing the initial prototype of CM, donated it to MLCommons to benefit the entire community:
  [ref1](https://github.com/mlcommons/ck/tree/c7918ad544f26b6c499c2fc9c07431a9640fca5a/ck2), 
  [ref2](https://github.com/mlcommons/ck/tree/c7918ad544f26b6c499c2fc9c07431a9640fca5a/ck2#coordinators),
  [ref3](https://github.com/mlcommons/ck/commit/3c146cb3c75a015363f7a96758adf6dcc43032d6),
  [ref4](https://github.com/mlcommons/ck/commit/3c146cb3c75a015363f7a96758adf6dcc43032d6#diff-d97f0f6f5a32f16d6ed18b9600ffc650f7b25512685f7a2373436c492c6b52b3R48).

* Apr 6, 2022: started transitioning previous MLOps and MLPerf automations from the mlcommons/ck-mlops format 
  to the new CM format using the cm-mlops repository (will be later renamed to cm4mlops):
  [ref1](https://github.com/octoml/cm-mlops/commit/d1efdc30fb535ce144020d4e88f3ed768c933176),
  [ref2](https://github.com/octoml/cm-mlops/blob/d1efdc30fb535ce144020d4e88f3ed768c933176/CONTRIBUTIONS).

* Apr 22, 2022: began architecting "Intelligent Components" in the CM-MLOps repository, 
  which will be renamed to `CM Script` at a later stage:
  [ref1](https://github.com/octoml/cm-mlops/commit/b335c609c47d2c547afe174d9df232652d57f4f8),
  [ref2](https://github.com/octoml/cm-mlops/tree/b335c609c47d2c547afe174d9df232652d57f4f8),
  [ref3](https://github.com/octoml/cm-mlops/blob/b335c609c47d2c547afe174d9df232652d57f4f8/CONTRIBUTIONS).

  At the same time, prototyped other core CM automations, including IC, Docker, and Experiment:
  [ref1](https://github.com/octoml/cm-mlops/tree/b335c609c47d2c547afe174d9df232652d57f4f8/automation),
  [ref2](https://github.com/mlcommons/ck/commits/master/?before=7f66e2438bfe21b4ce2d08326a5168bb9e3132f6+7001).

* Apr 28, 2022: donated CM-MLOps to MLCommons, which was later renamed to CM4MLOps:
  [ref](https://github.com/mlcommons/ck/commit/456e4861056c0e39c4d689c03da91f90a44be058).

* May 9, 2022: developed the initial set of core IC automations for MLOps (aka CM scripts):
 [ref1](https://github.com/octoml/cm-mlops/commit/4a4a027f4088ce7e7abcec29c39d98981bf09d4c),
 [ref2](https://github.com/octoml/cm-mlops/tree/4a4a027f4088ce7e7abcec29c39d98981bf09d4c),
 [ref3](https://github.com/octoml/cm-mlops/blob/7692240becd6397a96c3975388913ea082002e7a/CONTRIBUTIONS).

* May 11, 2022: After successfully prototyping CM and CM-MLOps, deprecated the CK1 framework in favor of CM. 
  Transferred Arjun Suresh to the CM project as a maintainer and tester for CM and CM-MLOps:
  [ref](https://github.com/octoml/cm-mlops/blob/17405833665bc1e93820f9ff76deb28a0f543bdb/CONTRIBUTIONS).

  Created a [file](https://github.com/mlcommons/ck/blob/master/cm-mlops/CHANGES.md) 
  to document and track our public developments at MLCommons.

* Jun 8, 2022: renamed the 'IC' automation to the more intuitive 'CM script' automation. 
  [ref1](https://github.com/mlcommons/ck/tree/5ca4e2c33e58a660ac20a545d8aa5143ab6e8e81/cm-devops/automation/script),
  [ref2](https://github.com/mlcommons/ck/tree/5ca4e2c33e58a660ac20a545d8aa5143ab6e8e81),
  [ref3](https://github.com/octoml/cm-mlops/commit/7910fb7ffc62a617d987d2f887d6f9981ff80187).

* Jun 16, 2022: prototyped the `CM cache` automation to facilitate caching and reuse of the outputs from CM scripts:
  [ref1](https://github.com/mlcommons/ck/commit/1f81aae8cebd5567ec4ca55f693beaf32b49fb48),
  [ref2](https://github.com/mlcommons/ck/tree/1f81aae8cebd5567ec4ca55f693beaf32b49fb48),
  [ref3](https://github.com/mlcommons/ck/tree/1f81aae8cebd5567ec4ca55f693beaf32b49fb48?tab=readme-ov-file#contacts).

* Sep 6, 2022: delivered CM demo to run MLPerf while deprecating CK1 automations for MLPerf:
  [ref1](https://github.com/mlcommons/ck/commit/2c5d5c5c944ae5f252113c62af457c7a4c5e877a#diff-faac2c4ecfd0bfb928dafc938d3dad5651762fbb504a2544752a337294ee2573R224),
  [ref2](https://github.com/mlcommons/ck/blob/2c5d5c5c944ae5f252113c62af457c7a4c5e877a/CONTRIBUTING.md#author-and-coordinator).

  Welcomed Arjun Suresh as a contributor to CM automations for MLPerf: [ref](https://github.com/mlcommons/ck/blob/2c5d5c5c944ae5f252113c62af457c7a4c5e877a/CONTRIBUTING.md#contributors-in-alphabetical-order).

* From September 2022: coordinated community development of CM and CM4MLOps 
  to [modularize and automate MLPerf benchmarks](https://docs.mlcommons.org/inference)
  and support [reproducibility initiatives at ML and Systems conferences](https://cTuning.or/ae) 
  through the [MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md).

  * Directed and financed the creation of (CM) automations to streamline the MLPerf power measurement processes.

  * Proposed to use MLPerf benchmarks for the Student Cluster Competition, led the developments 
    and prepared a tutorial to run MLPerf inference at SCC'22 via CM: [ref](https://github.com/mlcommons/ck/blob/master/docs/tutorials/sc22-scc-mlperf.md)

* April 2023: departed OctoML to focus on the development of the [CK playground](https://access.cKnowledge.org) and CM automations 
  to make Mlperf accessible to everyone. Hired Arjun Suresh to help with developments.

  * Initiated and funded development of the [MLPerf explorer](https://github.com/ctuning/q2a-mlperf-visualizer)
    to improve visualization of results

* August 2023: organized the 1st mass-scale MLPerf community submission of 12217 inference benchmark v3.1 results 
   out of total 13351 results (including 90% of all power results) across diverse models, software and hardware 
   from different vendors via [open challenges](https://access.cknowledge.org/playground/?action=challenges) funded by cTuning.org : 
   [LinkedIn article](https://www.linkedin.com/pulse/new-milestone-make-mlperf-benchmarks-accessible-everyone-fursin/) 
   with results visualized by the [MLPerf explorer](https://github.com/ctuning/q2a-mlperf-visualizer),
   [CM4MLOps challenges at GitHub](https://github.com/mlcommons/cm4mlops/tree/main/challenge). 

* February, 2024: proposed to use CM to automate [MLPerf automotive benchmark (ABTF)](https://mlcommons.org/working-groups/benchmarks/automotive/).

  * moved my prototypes of the CM automation for ABTF to cm4abtf repo: [ref](https://github.com/mlcommons/cm4abtf/commit/f92b9f464de89a38a4bde149290dede2d94c8631)
  * led further CM4ABTF developments funded by cTuning.org.

* Starting in April 2024, began the gradual transfer of ongoing maintenance and enhancement 
  responsibilities for CM and CM4MLOps, including MLPerf automations, to MLCommons.
  Welcomed Anandhu Sooraj as a maintainer and contributor to CM4MLOps with MLPerf automations.

* Took a break from all development activities.

* July 2024: started prototyping the next generation of CM (CMX and CMX4MLOps) with simpler interfaces 
  based on user feedback while maintaining backward compatibility.

* 2025: continue developing CMX and CMX4MLOPs to make it easier to run and customize MLPerf inference, training 
  and other benchmarks across diverse models, datasets, software and hardware.

For more details, please refer to the [white paper](https://arxiv.org/abs/2406.16791) 
and the [ACM REP'23 keynote](https://doi.org/10.5281/zenodo.8105339).
