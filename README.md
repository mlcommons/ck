Introduction
====================
Collective Knowledge (CK) is an open-source, community-driven,
light-weight, plugin-based and technology neutral framework and 
repository for low-level knowledge management and exchange.
It is intended to help users organize, describe, preserve, 
cross-link, find, share, exchange and reuse any code and 
data as reusable components with unified API.

CK helps users gradually organize their files (code and data)
locally into cross-linked entries with DOI-style UIDs, simple and
unified API (through CK modules written in Python), and
JSON-based, schema-free and extensible meta-description, thus
protecting them from continuous changes in the system.

These entries can be transparently indexed and searched
by third-party ElasticSearch tool, shared via GIT and connected
together as LEGO(R) into pipelines (workflows) to quickly and
collaboratively prototype various research ideas, replay past
experiments, and take advantage of powerful third-party
statistical analysis and big data predictive analytics tools
including R and SciPy.

CK can be invoked either through universal command line
front-end, as a web-service or from other programs and tools
written in practically any language including C, C++, Fortran, 
PHP  and Java using OpenME event-based plugin framework
developed separately:
* https://github.com/ctuning/openme

We tested CK with Python 2.x and 3.x on various platforms
including Ubuntu, OpenSUSE, CentOS, Android (partial
support through web services) and Windows 7. 

We use CK to systematize our own R&D in the following projects 
and initiatives:
* software and hardware performance and energy 
auto-tuning and co-design combined with machine learning 
(http://hal.inria.fr/hal-01054763)
* crowdsourcing benchmarking of new compilers for new architectures 
(https://play.google.com/store/apps/details?id=com.collective_mind.node)
* collaborative and reproducible R&D in computer engineering
(http://c-mind.org/reproducibility)

Live demo of the Collective Knowledge browser:
* http://cknowledge.org/repo

Further information (documentation, user scenarios 
and developer guide):
* https://github.com/ctuning/ck/wiki

Developers
==========
This software is being developed by the non-profit 
cTuning foundation and its volunteers.

(C)opyright 2014-2015 Grigori Fursin, 
cTuning foundation and contributors

License
=======
* CK is distributed under new 3-clause BSD license.

Where to get
============
* https://github.com/ctuning/ck
* git clone https://github.com/ctuning/ck.git ck

Minimal requirements
====================
* Python > 2.6 (Python 2.x may have some issues with Unicode support)

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

Collaborative R&D scenarios:
===============================

Users can assemble various R&D scenarios (workflows, pipelines) 
from shared code and data as LEGO(R) using simple CK API.
Pipelines are also implemented as CK modules and can be shared
with all dependencies via GIT(HUB).

We currently work on the following public scenarios:
* unified experimentation combined with predictive analytics: http://github.com/ctuning/ck-analytics

 This CK repo can be easily imported using:

 > ck add repo:ck-analytics --share --quiet

* auto-tuning and crowd-tuning: https://github.com/ctuning/ck-auto-tuning

 This CK repo can also be imported using 

 > ck add repo:ck-auto-tuning --share --quiet

All shared repositories can be updated from time to time using:

 > ck pull repo

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
* https://hal.inria.fr/inria-00436029

If you found CK interesting and possibly useful, you are welcome 
to reference above publications in your reports.

Fun
===
* See CK development as a video: http://cknowledge.org/soft/commits/ck-visualization.mp4

Acknowledgments
===============
This project has been initially funded by EU FP7 609491 TETRACOM
project. We would like to thank all volunteers for their valuable
feedback and support.

Full documentation and usage scenarios
======================================
* https://github.com/ctuning/ck/wiki
