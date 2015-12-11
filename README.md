Collective Knowledge Infrastructure and Repository
is a small Python application (less than 1Mb)
with command line and web front-ends to help researchers:

* easily convert their research artifacts (benchmarks, data sets, scripts, tools, predictive models, graphs, articles) into reusable and interconnected components and customizable workflows with unified JSON API and meta information; 
* quickly prototype research ideas from shared components and exchange results; 
* crowdsource and reproduce experiments (such as empirical multi-objective autotuning and design space exploration);
* apply predictive analytics to accelerate knowledge discovery;
* design competitions with unified knowledge sharing;
* enable interactive graphs and articles.

Our long term goal is to enable truly open, collaborative and
reproducible research, experimentation and knowledge sharing
(currently focusing on computer engineering) while making it 
as simple and powerful as Wikipedia. 

See our recent short position paper at DATE'16, artifact evaluation initiative
for major computer systems' conferences, and live repository demo for more details: 
* http://bit.ly/ck-date16
* http://cTuning.org/ae
* http://cknowledge.org/repo

CK full documentation
=====================
* http://github.com/ctuning/ck/wiki

License
=======
* Permissive 3-clause BSD license (see LICENSE.txt file for more details).

Minimal requirements
====================
* Python >= 2.6 (3.0+ is natively supported)
* GIT command line client

If you would like to use shared repositories with already implemented
crowd-benchmarking, multi-objective autotuning, statistical analysis,
predictive analytics, interactive graphs, etc, you may need to install
extra Python packages: 

* 'matplotlib','scipy' and 'numpy' to plot graphs and perform statistical analysis (during performance/energy/accuracy autotuning and modeling)
* 'sklearn-kit' for predictive analytics
* 'psutil' to properly terminate running process on Windows after timeout (during program autotuning)
* 'Tkinter' or 'tkinter' or 'pyperclip' if copy to clipboard functionality is required (to reproduce CK experiments from the web)

Alternatively, you can use Anaconda python distribution
which includes all scientific packages required for CK-based
collaborative and reproducible experimentation.

We successfully validated CK on Linux, Windows, Max OS X and Android (partially).

Copyright
=========
(C)opyright 2014-2015 Grigori Fursin, 
cTuning foundation and contributors

http://cTuning.org

See COPYRIGHT.txt for more details.

Authors
=======
* Grigori Fursin, http://fursin.net
* Anton Lokhmotov, https://www.hipeac.net/~anton

Minimal installation
====================

Download latest CK from GitHub:

 $ git clone https://github.com/ctuning/ck.git ck

Add ck/bin directory to PATH variable

 $ export PATH=$PWD/ck/bin:$PATH

On Windows, you should manually add full path to ck/bin 
to you PATH environment variable.

If you would like to use CK from ipython notebook or other
python applications, you can install it as a standard 
Python library (you may need root privileges depending 
on how your Python is installed):

 $ cd ck

 $ sudo python setup.py install

By default, CK uses the latest version of installed Python, i.e.
v3 and then v2. You can force CK to use a given Python version
by changing environment variable "CK_PYTHON", i.e.:

 $ export CK_PYTHON=python3
 
 or

 $ export CK_PYTHON=python

Other installation possibilities (via PIP, Conda, Debian) are described
here: https://github.com/ctuning/ck/wiki/Installation 

Usage
=====

You can check that CK is installed correctly via:

 $ ck

You should see information about CK options.

If you have IPython installed, you can then check CK library 
installation as following:

 $ ipython

 $ import ck.kernel as ck

 $ ck.test()

 $ ck.access('list module')

 $ ck.access('load kernel default')

Now, you can use CK to pull various shared CK repositories
(code and data shared as reusable components via GitHub
or Bitbucket) and run shared experimental workflows
(for example, to crowd-benchmark and autotune programs,
build predictive models of performance, analyze representative
benchmarks and data sets, install missing tools, ...).

For example, compiling and running any shared benchmark 
on your Linux machine with GCC can be done simply as:

 $ ck pull repo:ctuning-programs

 $ ck compile program:cbench-automotive-susan --speed

 $ ck run program:cbench-automotive-susan

You will be asked a few questions and for now you can just press Enter 
to select the default choices.

Compiling and running such benchmarks on Windows or Android,
autotuning or crowdtuning them (performance, energy, accuracy, size, etc),
adding more data sets, applying machine learning to predict optimizations,
and any other shared scenario requires a few more steps 
as described in our "Getting Started Guide":

* https://github.com/ctuning/ck/wiki

Adding new CK modules as containers for own data, as a wrapper
for some tool or as a workflow is also straightforward. 
For example, you can add your own module 'hello' with an action 'say'
and with an entry 'world' as following (you can select all
default values by just pressing Enter):

 $ ck add module:hello

 $ ck add_action module --func=say

 $ ck add hello:world

 $ ck say hello:world

You can now find and customize Python dummy function 'say' 
in the CK module 'hello' (module.py) via
 
 $ ck find module:hello

You can also find associated CK entry hello:say and modify 
its meta information (.cm/meta.json) via

 $ ck find hello:world

Please, follow CK documentation (including various Getting Started Guides) for more details:

* https://github.com/ctuning/ck/wiki

Questions/comments/discussions?
===============================
Please, use our mailing lists:
* General topics of knowledge preservation, sharing and reuse
  as well as collaborative and reproducible R&D: http://groups.google.com/group/collective-knowledge
* Software and hardware multi-objective (performance/energy/accuracy/size/reliability/cost)
  benchmarking, autotuning, crowdtuning and run-time adaptation: http://groups.google.com/group/ctuning-discussions

Publications
============
Concepts has been described in the following publications:

* http://bit.ly/ck-date16
* http://arxiv.org/abs/1506.06256
* http://hal.inria.fr/hal-01054763
* http://arxiv.org/abs/1406.4020
* https://hal.inria.fr/inria-00436029

If you found CK useful and/or interesting, you are welcome
to reference any of the above publications in your articles
and reports.

CK-powered projects
===================

CK is currently used in the following projects:

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
(http://cTuning.org/ae , http://arxiv.org/abs/1406.4020 ,
http://adapt-workshop.org)

* enabling open, collaborative and reproducible research and experimentation
with interactive publications focusing on computer engineering
( http://cTuning.org/reproducibility-wiki )

* enabling interactive and reproducible articles for Digital Libraries
(http://cknowledge.org/repo/web.php?wcid=29db2248aba45e59:cd11e3a188574d80 ,
http://cknowledge.org/repo/web.php?wcid=29db2248aba45e59:6f40bc99c4f7df58)

* serving as a personal knowledge manager to organize, interconnect
and preserve all personal coda and data via simple JSON
meta with UIDs and semantic tags.

You are welcome to add your own CK-powered project here!

Acknowledgments
===============

CK development is coordinated by the non-profit cTuning foundation
(cTuning.org). We would like to thank the EU TETRACOM 609491 project
(www.tetracom.eu) for initial funding and dividiti (www.dividiti.com)
for continuing support. We are also extremely grateful to all volunteers
for their valuable feedback and contributions.
