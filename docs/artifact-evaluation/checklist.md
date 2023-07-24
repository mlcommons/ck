[ [Back to index](https://cTuning.org/ae) ]

# Artifact Checklist


Here we provide a few informal suggestions to help you fill in the 
[Unified Artifact Appendix with the Reproducibility Checklist](https://github.com/mlcommons/ck/blob/master/docs/artifact-evaluation/template/ae.tex) 
for artifact evaluation while avoiding common pitfalls. 
We've introduced this appendix to [unify the description of experimental setups and results across different conferences](https://learning.acm.org/techtalks/reproducibility).




## Abstract

 Briefly and informally describe your artifacts including minimal hardware, software and other requirements, 
 how they support your paper and what are they key results to be reproduced.
 Note that evaluators will use artifact abstracts to bid on artifacts.
 The AE chairs will also use it to finalize artifact assignments.

 
## Checklist


 Together with the artifact abstract, this check-list will help us make sure that evaluators 
 have appropriate competency and an access to the technology required to evaluate your artifacts. 
 It can also be used as meta information to find your artifacts in Digital Libraries.

 ![](https://raw.githubusercontent.com/mlcommons/ck/master/docs/artifact-evaluation/image-general-workflow1.png)
  

 Fill in whatever is applicable with some informal keywords and remove unrelated items 
 (please consider questions below just as informal hints
 that reviewers are usually concerned about):

 
* **Algorithm:** Are you presenting a new algorithm?
* **Program:** Which benchmarks do you use 
 ([PARSEC](http://parsec.cs.princeton.edu "http://parsec.cs.princeton.edu"),
 [NAS](http://www.nas.nasa.gov/publications/npb.html "http://www.nas.nasa.gov/publications/npb.html"),
 [EEMBC](https://www.eembc.org "https://www.eembc.org"),
 [SPLASH](http://www.capsl.udel.edu/splash/index.html "http://www.capsl.udel.edu/splash/index.html"),
 [Rodinia](https://www.cs.virginia.edu/~skadron/wiki/rodinia "https://www.cs.virginia.edu/~skadron/wiki/rodinia"),
 [LINPACK](http://www.netlib.org/linpack "http://www.netlib.org/linpack"),
 [HPCG](http://hpcg-benchmark.org/ "http://hpcg-benchmark.org/"),
 [MiBench](http://wwweb.eecs.umich.edu/mibench "http://wwweb.eecs.umich.edu/mibench"),
 [SPEC](https://www.spec.org/cpu2006 "https://www.spec.org/cpu2006"),
 [cTuning](http://github.com/ctuning/ctuning-programs "http://github.com/ctuning/ctuning-programs"), etc)? 
 Are they included or should they be downloaded? Which version?
 Are they public or private? If they are private, 
 is there a public analog to evaluate your artifact?
 What is the approximate size?
* **Compilation:** Do you require a specific compiler? Public/private? Is it included? Which version?
* **Transformations:** Do you require a program transformation tool (source-to-source, binary-to-binary, compiler pass, etc)? 
 Public/private? Is it included? Which version?
* **Binary:** Are binaries included? OS-specific? Which version?
* **Model:** Do you use specific models (GPT-J, BERT, MobileNets ...)?
 Are they included? If not, how to download and install? 
 What is their approximate size?
* **Data set:** Do you use specific data sets?
 Are they included? If not, how to download and install? 
 What is their approximate size?
* **Run-time environment:** Is your artifact OS-specific (Linux, Windows, MacOS, Android, etc) ?
 Which version? Which are the main software dependencies (JIT, libs, run-time adaptation frameworks, etc);
 Do you need root access?
* **Hardware:** Do you need specific hardware (supercomputer, architecture simulator, CPU, GPU, neural network accelerator, FPGA) 
 or specific features (hardware counters
 to measure power consumption, SUDO access to CPU/GPU frequency, etc)? 
 Are they publicly available?
* **Run-time state:** Is your artifact sensitive to run-time state (cold/hot cache, network/cache contentions, etc.)
* **Execution:** Any specific conditions should be met during experiments (sole user, process pinning, profiling, adaptation, etc)? How long will it approximately run?
* **Metrics:** Which metrics will be evaluated (execution time, inference per second, Top1 accuracy, power consumption, etc). 
* **Output:** What is the output of your key experiments (console, file, table, graph) and what are your key results 
 (exact output, numerical results, empirical characteristics, etc)?
 Are expected results included?
* **Experiments:** How to prepare experiments and reproduce results
 (README, scripts, [IPython/Jupyter notebook](https://jupyter.org "https://jupyter.org"), 
 [MLCommons CM automation language](https://doi.org/10.5281/zenodo.8105339), containers etc)? 
 Do not forget to mention the maximum allowable variation of empirical results!
* **How much disk space required (approximately)?:** This can help evaluators and end-users to find appropriate resources.
* **How much time is needed to prepare workflow (approximately)?:** This can help evaluators and end-users to estimate resources needed to evaluate your artifact.
* **How much time is needed to complete experiments (approximately)?:** This can help evaluators and end-users to estimate resources needed to evaluate your artifact.
* **Publicly available?:** Will your artifact be publicly available? If yes, we may spend an extra effort to help you with the documentation.
* **Code licenses (if publicly available)?:** If you workflows and artifacts will be publicly available, please provide information about licenses.
 This will help the community to reuse your components.
* **Code licenses (if publicly available)?:** If you workflows and artifacts will be publicly available, please provide information about licenses.
 This will help the community to reuse your components.
* **Workflow frameworks used?** Did authors use any workflow framework which can automate and customize experiments?
* **Archived?:** 
 Note that the author-created artifacts relevant to this paper 
 will receive the ACM "artifact available" badge \*only if\* 
 they have been placed on a publicly 
 accessible archival repository such as [Zenodo](https://zenodo.org "https://zenodo.org"), 
 [FigShare](https://figshare.com "https://figshare.com")
 or [Dryad](http://datadryad.org "http://datadryad.org"). 
 A DOI will be then assigned to their artifacts and must be provided here! 
 Personal web pages, Google Drive, GitHub, GitLab and BitBucket 
 are not accepted for this badge. 
 Authors can provide the DOI for their artifacts at the end of the evaluation.




## Description



### How to access



Describe the way how reviewers will access your artifacts:

* Clone a repository from GitHub, GitLab or any similar service
* Download a package from a public website
* Download a package from a private website (you will need to send information how to access your artifacts to AE chairs)
* Access artifact via private machine with pre-installed software (only when access to rare or publicly unavailable hardware is required or proprietary
  software is used - you will need to send credentials to access your machine to the AE chairs)



 Please describe approximate disk space required after unpacking your artifact.


### Hardware dependencies



 Describe any specific hardware and specific features required to evaluate your artifact 
 (vendor, CPU/GPU/FPGA, number of processors/cores, interconnect, memory, 
 hardware counters, etc).


### Software dependencies



 Describe any specific OS and software packages required to evaluate your
 artifact. This is particularly important if you share your source code 
 and it must be compiled or if you rely on some proprietary software that you
 can not include to your package. In such case, we strongly suggest you 
 to describe how to obtain and to install all third-party software, data sets
 and models.

   
  

*Note that we are trying to obtain AE licenses for some commonly used proprietary tools 
and benchmarks - you will be informed in case of positive outcome.*

### Data sets



 If third-party data sets are not included in your packages (for example, 
 they are very large or proprietary), please provide details about how to download
 and install them. 

 *In case of proprietary data sets, we suggest you provide reviewers
 a public alternative subset for evaluation*.


### Models



 If third-party models are not included in your packages (for example, 
 they are very large or proprietary), please provide details about how to download
 and install them. 

 


## Installation



 Describe the setup procedures for your artifact (even when containers are used). 



## Experiment workflow



 Describe the experimental workflow and how it is implemented
 and executed, i.e. some OS scripts, 
 [IPython/Jupyter notebook](https://jupyter.org "https://jupyter.org"), 
 [MLCommons CM automation language](https://github.com/mlcommons/ck/tree/master/docs), etc.

 Check [examples of reproduced papers](https://cknow.io/reproduced-papers "https://cknow.io/reproduced-papers").
  




## Evaluation and expected result



 Describe all the steps necessary to reproduce the key results from your paper. 
 Describe expected results including maximum allowable variation
 of empirical results.
 See the [SIGPLAN Empirical Evaluation Guidelines](https://www.sigplan.org/Resources/EmpiricalEvaluation "https://www.sigplan.org/Resources/EmpiricalEvaluation"),
 the [NeurIPS reproducibility checklist](https://www.cs.mcgill.ca/~jpineau/ReproducibilityChecklist.pdf "https://www.cs.mcgill.ca/~jpineau/ReproducibilityChecklist.pdf")
 and the [AE FAQ](faq.md) for more details.



## Experiment customization



 It is optional but can be useful for the community if you describe all the knobs
 to customize and tune your experiments and maybe even trying them
 with a different data sets, benchmark/applications,
 machine learning models, software environment (compilers, libraries, 
 run-time systems) and hardware.


## Reusability

Please describe your experience if you decided to participate in our pilot project to add 
the non-intrusive [MLCommons Collective Mind interface (CM)](https://doi.org/10.5281/zenodo.8105339)
to your artifacts. Note that it will be possible to prepare and run your experiments with 
or without this interface!



## Notes



 You can add informal notes to draw the attention of evaluators.



----

*This document was prepared by [Grigori Fursin](https://cKnowledge.org/gfursin)
 with contributions from [Bruce Childers](https://people.cs.pitt.edu/~childers),
 [Michael Heroux](https://www.sandia.gov/~maherou), 
 [Michela Taufer](https://gcl.cis.udel.edu/personal/taufer) and other great colleagues.
 It is maintained by the [cTuning foundation](https://cTuning.org/ae) and the 
 [MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md).*
