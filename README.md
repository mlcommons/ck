CK - simplifying collaborative and reproducible experimentation,
knowledge management and predictive analytics.

Note: the framework is stable but we are now working on
getting started guide, documentation and demos: https://github.com/ctuning/ck/wiki

License
=======
* Permissive simplified 3-clause BSD license (see LICENSE file).

Introduction
============

We've developed Collective Knowledge Framework and Repository (CK)
primarily to simplify code/data/model sharing and crowdsource 
our experimentation with machine learning in our own interdisciplinary 
research projects (such as designing faster, smaller, more power 
efficient and reliable computer systems using predictive analytics).
However, after our colleagues started successfully using it in other 
projects, we decided to make it public.

CK is an open-source, light-weight, portable, modular and python-based
framework, repository, web service and SDK to organize, describe,
cross-link and share user code, data, experimental setups and
meta information as unified, cross-linked and reusable components
with JSON API via standard Git services (such as GITHUB
or BitBucket).

Note, that unlike existing centralized web-based services 
that force users to upload all their code and data before
being processed, CK allows you to organize your artifacts 
and always keep track of them on your own machine 
while sharing them only if needed as P2P or via existing
private and public repositories.

CK can help non-specialists and professionals assemble experimental 
setups (aka workflows or pipelines) from their own or shared components 
just as LEGO(TM) to quickly prototype ideas while automating, 
preserving, distributing, crowdsourcing and reproducing experiments.

CK can also complement existing technology such as Docker 
and VM images as a higher-level light weight container
technology with simple, extensible and unified API.

Furthermore, CK can simplify connection of unified experiments 
to powerful predictive analytics tools such as scikit-learn 
and R (statistical analysis, data mining,  machine learning)
to automate and speed up exploration of multi-dimensional
experimental choices, analysis of results and decision making.

Finally, unified and integrated repository of knowledge allows 
community to systematize unstructured code and data while 
collaboratively validating experimental results, improving models, 
finding missing features and so on.

You may find motivation behind CK framework as well as real 
usage scenarios (some are based on previous version aka Collective Mind) 
in the following publications:

* [PDF, part I] https://hal.inria.fr/hal-01054763
* [PDF, part II] http://arxiv.org/abs/1506.06256
* [new publication model] http://arxiv.org/abs/1406.4020
* [Android app] https://play.google.com/store/apps/details?id=com.collective_mind.node

Further information including getting started guide, 
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
Python > 2.6 or 3.x.

Note: since user packages may require extra functionality
such as scipy and scikit-learn, we have been 
successfully using Anaconda python distribution
which includes all scientific packages required 
for predictive analytics in CK.

You can obtain the latest CK version from GITHUB:
 > git clone https://github.com/ctuning/ck.git ck

Note: we plan to add CK to standard Python distributions 
(Linux and Windows) and Debian - if you would like to help, 
please get in touch.

Now, you can simply add CK bin directory to your OS PATH 
environment variable and you are ready to go. For example,
try to envoke CK command line front end via:

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

Now, you can use CK to pull various shared repositories and run 
experimental workflows (such as autotuning programs, building
predictive models of performance, analyzing data sets, installing
missing tools, ...).

You can find further details, practical examples, motivation and 
specification in this wiki:

* https://github.com/ctuning/ck/wiki

Questions/comments/discussions?
===============================
Please, use our mailing lists:
* General topics of knowledge preservation, sharing and reuse
  as well as collaborative and reproducible R&D: http://groups.google.com/group/collective-mind
* Software and hardware performance/energy/size/reliability  
  (auto/crowd)-tuning: http://groups.google.com/group/ctuning-discussions

Publications
============
Concepts has been described in the following publications:

* http://arxiv.org/abs/1506.06256
* http://hal.inria.fr/hal-01054763
* http://arxiv.org/abs/1406.4020
* https://hal.inria.fr/inria-00436029

If you found CK useful and/or interesting, you are welcome 
to reference some of the above publications in your reports.

Fun
===
* CK GIT commits as a video: http://cknowledge.org/soft/commits/ck-visualization.mp4

Extra description
=================
CK is intended to enable open and collaborative
research and experimentation particularly in computer
engineering. It can help users preserve, organize, describe,
cross-link and share their code, data and experimental results
as reusable Python-based components with a very simple API (one
function with JSON in and JSON out) and JSON-based schema-free
meta description.

All components can be transparently indexed and searched via
third-party Hadoop-based ElasticSearch, shared via GIT, and
connected together into pipelines (workflows) just as LEGO(R)
to quickly prototype various research ideas, crowdsource
experiments, reproduce past results, perform statistical analysis
and apply predictive analytics (as described
in http://hal.inria.fr/hal-01054763).

CK can be invoked in a unified way via CMD, web service or from
other programs and tools written in practically any language
including C, C++, Fortran, PHP and Java using OpenME event-based
plugin framework developed separately
(https://github.com/ctuning/openme).

CK has been tested with Python 2.x and 3.x on various platforms
including Ubuntu, OpenSUSE, CentOS, Android (partial
support through web services and OpenME) and Windows 7. 

CK is extensively used in the following projects:

* building public repository of knowledge for computer engineering
(http://cknowledge.org/repo , http://c-mind.org/repo)

* implementing our universal multi-dimensional, multi-objective 
plugin-based autotuning approach combined with crowdsourcing, predictive
analytics and run-time adaptation. We support OpenCL, CUDA,
OpenMP, MPI, compiler and any other tuning for performance,
energy, size, reliability, cost and any other metrics across small
kernels/codelets and large applications.
(http://hal.inria.fr/hal-01054763)

* crowdsourcing automatic compiler optimization heuristic tuning
and benchmarking of new architectures across shared resources
such as mobile phones, tablets, cloud services, etc.
(https://play.google.com/store/apps/details?id=com.collective_mind.node)

* supporting artifact evaluation initiatives for major conferences
and journals where all artifacts are shared along with publications
to be validated by the community (http://ctuning.org/event/ae-ppopp2016 ,
http://arxiv.org/abs/1406.4020 )

* enabling open, collaborative and reproducible research and experimentation 
with interactive publications focusing on computer engineering 
(http://cknowledge.org/reproducibility)

Acknowledgments
===============
This project has been partially funded by EU FP7 609491 TETRACOM
project. We would like to thank all volunteers for their valuable
feedback and support.
