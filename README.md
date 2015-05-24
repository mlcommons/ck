Introduction
============
Collective Knowledge (CK) is a light-weight, portable, modular
and python-based framework, repository, web service and SDK 
to organize, describe, cross-link and share user code, data,
experimental setups and meta information as unified 
and reusable components with JSON API via standard 
Git services (such as GITHUB or BitBucket).

Such unification can help researchers assemble experimental setups
(workflows, pipelines, etc) from shared components just as LEGO(TM)
to quickly prototype ideas while automating, preserving, 
distributing, crowdsourcing and reproducing experiments.

Furthermore, CK simplifies connection of unified experiments 
to powerful predictive analytics tools such as scikit-learn 
and R (statistical analysis, data mining,  machine learning)
to automate and speed up exploration of multi-dimensional
experimental choices, analysis of results and decision making.

Finally, unified and integrated repository of knowledge allows 
community to help validate experimental results, improve models, 
find missing features and so on.

For example, we use this framework primarily to systematize, open
and crowdsource our research and experimentation to design
faster, smaller, more power efficient and reliable software and
hardware (by combining autotuning, run-time adaptation, machine
learning and public repository of knowledge):

* [PDF] https://hal.inria.fr/hal-01054763
* [Android app] https://play.google.com/store/apps/details?id=com.collective_mind.node

Further information including documentation, user scenarios 
and developer guide:
* https://github.com/ctuning/ck/wiki

License
=======
* Permissive simplified 3-clause BSD license (see LICENSE.txt).

Author
======
Grigori Fursin, non-profit cTuning foundation, France
* http://cTuning.org/lab/people/gfursin

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

Developers
==========
This software is being developed by the non-profit 
cTuning foundation and its volunteers.

(C)opyright 2014-2015 Grigori Fursin, 
cTuning foundation and contributors

Where to get
============
* https://github.com/ctuning/ck
* git clone https://github.com/ctuning/ck.git ck

Minimal requirements
====================
* Python > 2.6 (Python 2.x may have some issues with Unicode support)
* Python 3.x is supported

We have been successfully using Anaconda python distribution
which includes all scientific packages required for predictive 
analytics in CK.

Installation
============
We made a special effort to make installation as simple as possible.

You need to:
* add environment variable CK_ROOT to the root CK directory.
* add CK_ROOT/bin to the PATH environment variable:
** Linux: export PATH=$CK_ROOT/bin:$PATH
** Windows: set PATH=%CK_ROOT%/bin;%PATH%

Now you should be able to run CK from command line:
 > ck

In case you use international characters, you can test your
console for UTF-8 unicode by viewing the following test entry:
 > ck load test:unicode

If you want to use CK as a python module or from IPython 
and IPython notebook, you need to execute the following command
from the CK root directory:
 > python setup.py install

In such case, if you have IPython installed, you can 
check CK as following:

 > ipython

 > import ck.kernel as ck

 > ck.test()

 > ck.access('load kernel default')

You can also easily clone or pull various external CK repositories
shared via GITHUB (see CK wiki for more details) to build
collaborative R&D scenarios:

 > ck pull repo:ck-env

 > ck pull repo:ck-web

 > ck pull repo:ck-auto-tuning

You can update the whole framework and all shared repos as following:

 > ck pull all

Collaborative R&D usage scenarios:
==================================

Users can assemble various R&D scenarios (workflows, pipelines) 
from shared code and data as LEGO(R) using simple CK API.
Pipelines are also implemented as CK modules and can be shared
with all dependencies via GIT(HUB). See more details at:

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

* http://hal.inria.fr/hal-01054763
* http://arxiv.org/abs/1406.4020
* https://hal.inria.fr/inria-00436029

If you found CK interesting and possibly useful, you are welcome 
to reference above publications in your reports.

Fun
===
* CK GIT commits as a video: http://cknowledge.org/soft/commits/ck-visualization.mp4

Acknowledgments
===============
This project has been initially funded by EU FP7 609491 TETRACOM
project. We would like to thank all volunteers for their valuable
feedback and support.
