Collective Knowledge Infrastructure - simplifying collaborative 
and reproducible experimentation, knowledge management 
and predictive analytics.

License
=======
* Permissive 3-clause BSD license (see LICENSE file).

Introduction
============

We have developed Collective Knowledge Framework and Repository (CK)
primarily to solve numerous problems we faced during past 20 years
of our research on building self-optimizing computer systems
(combining performance autotuning, machine learning and run-time adaptation):

* numerous and ever changing hardware
* black-box compilers
* ad-hoc tools with evolving and incompatible interfaces
* multiple heterogeneous and possibly proprietary data formats
* raising number of design and optimization choices
* raising amount of experimental data to process
* ad-hoc, outdated and non-representative benchmarks with limited data sets
* lack of unified and reproducible mechanisms for exchange of experimental results

Eventually, we created CK as an open-source and light-weight SDK
(~200K python code) to help our colleagues preserve, organize, describe,
cross-link and share their code, data and experimental results
as reusable Python-based components with a very simple API 
(just one one function with JSON in and JSON out) 
and JSON-based schema-free meta description, as shown in the
following examples:
* https://github.com/ctuning/ctuning-programs 
* https://github.com/ctuning/ctuning-datasets-min
* https://github.com/ctuning/ck-analytics
* https://github.com/ctuning/ck-autotuning

CK also helps to abstract access to ever-changing tools and
hardware via wrappers with the same JSON API while protecting
experimental setups from low-level interface/data changes
(wrappers handle such changes as well as setting up environment
for multiple versions of a given tool or library).

All components has DOI-style UID and can be transparently indexed and 
searched via third-party Hadoop-based ElasticSearch, shared via GIT, 
and connected together into experimental pipelines (workflows) 
just as LEGO(TM) to quickly prototype various research ideas, 
crowdsource experiments, reproduce and improve past techniques.

Furthermore, CK can simplify connection of unified experiments 
to powerful predictive analytics tools such as scikit-learn 
and R (statistical analysis, data mining,  machine learning)
thus helping non-specialists perform statistical analysis of results,
automate  exploration of large, multi-dimensional design 
and optimization choices and speed up decision making,
as described in our CK-powered interactive articles:
* http://cknowledge.org/repo/web.php?wcid=29db2248aba45e59:6f40bc99c4f7df58
* http://cknowledge.org/repo/web.php?wcid=29db2248aba45e59:6f40bc99c4f7df58

Unlike existing centralized web-based services 
that force users to upload all their code and data before
being processed, CK allows users organize their local artifacts 
and always keep track of them on their own machine 
while sharing them only if needed as P2P or via existing
private and public repositories.

CK can also complement existing technology such as Docker 
and VM images as a higher-level light weight wrapper
technology with simple, extensible and unified JSON API.

CK can be invoked in a unified way via CMD or JSON web service.
It can also be directly invoked from other programs and tools written in practically 
any language including C, C++, Fortran, PHP and Java using OpenME event-based
plugin framework (we worked with the community to add similar plugin 
interface to GCC 4.6+ and plan to add it to LLVM). 

Eventually, unified mechanisms of artifact and knowledge exchange
in the CK allows the community to gradually validate and improve
shared techniques and data sets thus enabling truly open,
collaborative, interdisciplinary and reproducible research
similar to physics and other natural sciences. To some extent,
it can help computer engineers and researchers become data scientists 
and focus on innovation while liberating them from ad-hoc,
repetitive, boring and time consuming tasks.

You may check out our motivation as well as real usage scenarios 
and CK-powered interactive papers (some are based on previous 
version aka Collective Mind) here:

* [Interactive article 1] http://cknowledge.org/repo/web.php?wcid=29db2248aba45e59:6f40bc99c4f7df58
* [Interactive article 2] http://cknowledge.org/repo/web.php?wcid=29db2248aba45e59:cd11e3a188574d80
* [All shared artifacts via CK]: http://github.com/ctuning/reproduce-ck-paper
* [Our open publication model] http://arxiv.org/abs/1406.4020
* [Live CK repository] http://cknowledge.org/repo
* [Android client for crowd-benchmarking] https://play.google.com/store/apps/details?id=com.collective_mind.node

Further details about CK including getting started guide, 
real usage scenarios, and developer guide is available here:

* https://github.com/ctuning/ck/wiki

Copyright
=========
This software is being developed by the non-profit 
cTuning foundation and its volunteers.

(C)opyright 2014-2015 Grigori Fursin, 
cTuning foundation and contributors

http://cTuning.org

Author
======
Grigori Fursin, http://fursin.net

Installation
============
We made a special effort to make CK installation 
as simple as possible - it requires only standard 
Python version 2.6 or above (3.x is supported).

CK has been successfully tested by volunteers on various 
platforms including Ubuntu, OpenSUSE, CentOS, MacOS X, 
Android (partial support through web services and OpenME) 
and most of the recent Windows versions. 

Note: since user packages may require extra functionality
such as scipy and scikit-learn, we have been 
successfully using Anaconda python distribution
which includes all scientific packages required 
for predictive analytics in CK.

You can obtain the latest CK version from GITHUB:
 > git clone https://github.com/ctuning/ck.git ck

Note: we plan to add CK to standard Python distributions 
(Linux and Windows) and Debian - any help is appreciated.

Now, you can simply add CK bin directory to your OS PATH 
environment variable and you are ready to go. For example,
you check CK's command line front-end via:

 > ck

If you want to use CK as a standard python module or from 
IPython/IPython notebook, just execute the following command
from the CK root directory (you will need sudo on Linux):
 > python setup.py install

If you have IPython installed, you can then check CK installation 
as following:

 > ipython

 > import ck.kernel as ck

 > ck.test()

 > ck.access('list module')

 > ck.access('load kernel default')

Now, you can use CK to pull various public CK repositories 
(code and data shared as reusable components via GITHUB
or BitBucket) and run shared experimental workflows 
(for example, to crowd-benchmark and autotune programs, 
build predictive models of performance, analyze representative
benchmarks and data sets, install missing tools, ...).

Please, check out CK documentation for more details
including motivation, Getting Started Guide and more practical
examples:

* https://github.com/ctuning/ck/wiki

Questions/comments/discussions?
===============================
Please, use our mailing lists:
* General topics of knowledge preservation, sharing and reuse
  as well as collaborative and reproducible R&D: http://groups.google.com/group/collective-mind
* Software and hardware performance/energy/size/reliability  
  (auto/crowd)tuning: http://groups.google.com/group/ctuning-discussions

Publications
============
Concepts has been described in the following publications:

* http://arxiv.org/abs/1506.06256
* http://hal.inria.fr/hal-01054763
* http://arxiv.org/abs/1406.4020
* https://hal.inria.fr/inria-00436029

If you found CK useful and/or interesting, you are welcome 
to reference some of the above publications in your articles 
and reports.

Fun
===
* CK GIT commits as a video: http://cknowledge.org/soft/commits/ck-visualization.mp4

CK-powered projects
===================

CK is currently used in the following public projects:

* building public repository of benchmarks, data sets, tools, predictive
models and optimization knowledge in a unified format with the help
of the computer engineering community
(http://cknowledge.org/repo , http://c-mind.org/repo)

* implementing universal multi-dimensional, multi-objective,
plugin-based autotuning combined with crowdsourcing, predictive
analytics and run-time adaptation (to enable self-optimizing
computer systems). We support OpenCL, CUDA, OpenMP, MPI, compiler
and any other tuning for performance, energy, size, reliability,
cost and any other metrics across small kernels/codelets and
large applications (http://cknowledge.org/repo/web.php?wcid=29db2248aba45e59:cd11e3a188574d80).

* implementing crowd-benchmarking (crowdsourcing workload characterization
and compiler heuristic construction across numerous architectures using shared 
computational resources such as mobile phones, tablets, cloud services, etc.
(https://play.google.com/store/apps/details?id=com.collective_mind.node ,
http://cknowledge.org/repo/web.php?wcid=29db2248aba45e59:cd11e3a188574d80)

* supporting artifact evaluation initiatives for major conferences
and journals where all artifacts are shared as reusable components (and not
just as black box virtual machine images) along with publications
(http://ctuning.org/event/ae-ppopp2016 , http://arxiv.org/abs/1406.4020 , 
http://adapt-workshop.org)

* enabling open, collaborative and reproducible research and experimentation 
with interactive publications focusing on computer engineering 
(http://cknowledge.org/reproducibility, )

* enabling interactive and reproducible articles for Digital Libraries
(http://cknowledge.org/repo/web.php?wcid=29db2248aba45e59:cd11e3a188574d80 , 
http://cknowledge.org/repo/web.php?wcid=29db2248aba45e59:6f40bc99c4f7df58)

You are welcome to add your own CK-powered project here!

Acknowledgments
===============
This project has been partially funded by EU FP7 609491 TETRACOM
project. We would like to thank all volunteers for their valuable
feedback and support.
