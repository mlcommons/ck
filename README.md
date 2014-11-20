Collective Knowledge
====================
Collective Knowledge (CK) is a community-driven open platform
and web service intended to help researchers clean up, systematize 
and crowdsource their ad-hoc experiments (code and data). 

CK let users assign assign DOI-style UID to any available code
and data, make them searchable (using ElasticSearch), shareable
with the community through CK web-services and GITHUB (or any
other version control system), and expose them to powerful
third-party statistical analysis and big data predictive
analytics tools including R and SciPy.

We are trying to develop CK as a very light and technology
neutral, wrapper and  plugin-based framework, repository and web
service which should allow users to gradually sort all their
files, provide meta-description in popular JSON format together
with universal access API, and gradually classify and
interconnect together all available code and data in a unified
format.

CK is written in Python for productivity and can be invoked from
user programs written in practically any language including
C, C++, Fortran, PHP and Java using light event-based OpenME
interface available here:
* https://github.com/ctuning/openme

We tested CK with Python 2.x and 3.x on various platforms
including Ubuntu, OpenSUSE, CentOS, Windows 7. 

We hope it will help enable collaborative and reproducible
research and development projects particularly with continuously
changing code base and with large amounts of processed
heterogeneous data: 
* http://c-mind.org/reproducibility.

CK is a public research project and relies heavily
on the community involvement. We welcome your feedback
and participation. You may simple join our discussions as:
* https://groups.google.com/forum/#!forum/collective-mind

The proof of concept (cTuning and Collective Mind V1.x frameworks) 
has been successfully used in several collaborative academic and 
industrial research projects in computer engineering since 2007.
                     
As a proof of concept, we used this technology including previous
versions (MILEPOST, cTuning and Collective Mind) in several
academic and industrial projects to systematize and crowdsource
multi-dimensional multi-objective program and architecture
auto-tuning, behavior modeling and co-design:
* https://hal.inria.fr/hal-01054763
* http://hal.inria.fr/hal-00850880
* http://c-mind.org/repo
* https://play.google.com/store/apps/details?id=com.collective_mind.node

Further info is available online:
* https://github.com/ctuning/ck/wiki

Developers
==========
This software is being developed by the non-profit cTuning
foundation and its volunteers.

(C)opyright 2014 Grigori Fursin, cTuning foundation and contributors

License
=======
* CK is distributed under new 3-clause BSD license.

Where to get
============
* https://github.com/ctuning/ck
* git clone https://github.com/ctuning/ck.git

Minimal requirements
====================
* Python > 2.6 (Python 2.x may have some issues with Unicode support)

Requirements to improve functionality
=====================================
* ElasticSearch (speeding up search and queries).

  Note that latest ElasticSearch requires Java >= 7.60!

  Also JAVA_HOME environment variable should be set properly!

Installation
============
We made a special effort to make installation as simple as possible.

You need to:
* add environment variable CK_ROOT to the root CK directory.
* add CK_ROOT/bin to the PATH environment variable:

  Linux: export PATH=$CK_ROOT/bin:$PATH

  Windows: set PATH=%CK_ROOT%/bin;%PATH%

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

Documentation
=============
For end users:
* https://github.com/ctuning/ck/wiki/Usage
* https://github.com/ctuning/ck/wiki

For developers:
* CK kernel API: http://cknowledge.org/soft/docs/ck_kernel_api/html/namespaceck_1_1kernel.html
* CK modules API: http://cknowledge.org/soft/docs/ck_modules_api/html/files.html

Mailing list
============
* http://groups.google.com/group/collective-mind

Contributions
=============
See CONTRIBUTIONS.txt

Publication
===========
Framework concept (including internals) has been introduced in
* Grigori Fursin, Renato Miceli, Anton Lokhmotov, Michael Gerndt, 
  Marc Baboulin, Allen D. Malony, Zbigniew Chamski, 
  Diego Novillo, Davide Del Vento, 
  "Collective mind: Towards practical and collaborative auto-tuning", 
  Journal of Scientific Programming 22 (4), 2014
  http://hal.inria.fr/hal-01054763

First high-level concept has been presented in
* Grigori Fursin, "Collective Tuning Initiative: automating 
  and accelerating development and optimization of computing systems", 
  Proceedings of the GCC Summit, Montreal, Canada, 2009
  https://hal.inria.fr/inria-00436029

Acknowledgments
===============
This project has been funded by EU FP7 609491 TETRACOM project,
ARM and cTuning foundation. We would like to thank all volunteers
for their feedback and support.
