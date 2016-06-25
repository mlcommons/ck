Introduction
============

Collective Knowledge is our "swiss knife" for open, collaborative and reproducible experimentation.
CK is a small, portable and customizable research platform to
* share artifacts as reusable and indexable Python components with unified JSON API and meta information (programs, benchmarks, data sets, tools, predictive models, etc); 
* quickly prototype experimental workflows from shared components (such as customizable and multi-objective autotuning for DSL, OpenCL, CUDA, MPI, OpenMP and compiler flags);
* crowdsource experiments across diverse hardware and workloads provided by volunteers, and report "interesting" or unexpected behavior;
* unify and abstract access to continuously evolving software across Windows, Linux and Android (tools, programs, libraries);
* use the latest environment for experiments (rather than using quickly outdated virtual images);
* automate, reproduce and crowdsource empirical experiments (using CK JSON-based web services);
* unify access to predictive analytics via unified JSON API and CK web services (scikit-learn, R, DNN, etc);
* enable reproducible and interactive articles. 

Project homepage: 
* http://cknowledge.org
* http://cTuning.org

License
=======
* Permissive 3-clause BSD license. (See `LICENSE.txt` for more details).

Minimal installation
====================

The minimal installation requires:

* Python >= 2.6 (3.0+ is natively supported).
* Git command line client.

On Ubuntu, you can install these dependencies via

```
$ apt-get install -y python git
```

On Windows, you can download and install these tools from the following sites:

* Git: https://git-for-windows.github.io
* Minimal Python: https://www.python.org/downloads/windows
* Anaconda scientific Python with all packages: https://www.continuum.io/downloads#_windows

For example, you can install shared workflow for collaborative program optimization
with all related artifacts, and start participating in multi-objective crowdtuning 
simply as follows: 

```
 $ git clone https://github.com/ctuning/ck.git ck
 $ export PATH=$PWD/ck/bin:$PATH (on Linux)
```
or

```
 $ set PATH={CURRENT PATH}\ck\bin;%PATH% (on Windows)
 $ ck pull repo:ck-crowdtuning
 $ ck crowdsource experiment (to crowdsource any available experiment scenario on Linux)
```

or

```
 $ ck crowdtune program --gcc --target_os=mingw-64 (to crowdsource program optimization on Windows via GCC MingW compiler)
```

If you have GCC or LLVM compilers installed, you can start continuously crowd-tune 
their optimization heuristics in a quiet mode (for example overnight) via

```
$ ck crowdtune program --llvm --quiet
$ ck crowdtune program --gcc --quiet
```

This experimental workflow will be optimizing different shared workloads
for multiple objectives (execution time, code size, energy, compilation time, etc)
using all exposed design and optimization knobs, while sending best performing 
optimizations to the public CK-based server:

* http://cTuning.org/crowd-results
* http://cknowledge.org/interactive-report

CK server will, in turn, perform on-line learning to classify optimization 
versus workloads which can be useful for compiler/hardware designers and 
performance engineers (described in more detail in http://arxiv.org/abs/1506.06256 ).

You can even participate in collaborative experiments using your Android mobile phone
by installing the following application from the Google Play Store:

* https://play.google.com/store/apps/details?id=openscience.crowdsource.experiments

You can find already shared artifacts and repositories here:
* List of shared repositories: https://github.com/ctuning/ck/wiki/Shared_repos
* List of shared modules: https://github.com/ctuning/ck/wiki/Shared_modules

Please check out CK getting started guide and CK wiki for further details:
* https://github.com/ctuning/ck/wiki/Getting_started_guide_basic
* https://github.com/ctuning/ck/wiki

Trying CK using Docker image
============================

If you would like to try CK without installing it, 
you can run the following Docker image:

```
 $ docker run -it ctuning/ck
```

However, the idea of CK is to be able to rebuild user experimental workflows
natively to take advantage of the latest software environment.

Also note that we added Docker automation to CK (to help 
evaluate artifacts at the conferences, share interactive 
and reproducible articles or crowdsource experiments for example). 

Please check 'ck-docker' repository at GitHub:

```
 $ ck show repo:ck-docker
```

You can download and view one of our CK-based interactive and reproducible articles as following:
```
 $ ck pull repo:ck-docker
 $ ck run docker:ck-interactive-article --browser (--sudo)
```

Our related initiatives
=======================

* Artifact Evaluation for computer systems' conferences: http://cTuning.org/ae
* New publication model with the community-driven public reviewing: http://adapt-workshop.org

CK-powered projects
===================
* https://github.com/ctuning/ck/wiki/Summary_of_projects

Motivation
==========
* https://github.com/ctuning/ck/wiki/Motivation

Authors
=======
* Grigori Fursin, http://fursin.net
* Anton Lokhmotov, https://www.hipeac.net/~anton

Questions/comments/discussions?
===============================
Please subscribe to our mailing lists:
* Open, collaborative and reproducible R&D including knowledge preservation, sharing and reuse:
  http://groups.google.com/group/collective-knowledge
* Software and hardware multi-objective (performance/energy/accuracy/size/reliability/cost)
  benchmarking, autotuning, crowdtuning and run-time adaptation: http://groups.google.com/group/ctuning-discussions

Publications
============
The concepts has been described in the following publications:

* http://arxiv.org/abs/1506.06256 (CPC'15)
* http://bit.ly/ck-date16 (DATE'16)
* http://bit.ly/ck-multiprog16 (MULTIPROG'16)
* http://cknowledge.org/interactive-report
* http://hal.inria.fr/hal-01054763 (Journal of Scientific Programming'14)
* http://arxiv.org/abs/1406.4020 (TRUST'14 @ PLDI'14)
* https://hal.inria.fr/inria-00436029 (GCC Summit'09)

If you found CK useful and/or interesting, you are welcome
to reference any of the above publications in your articles
and reports. You can download the above references in the 
BibTex format here:

* https://raw.githubusercontent.com/ctuning/ck-guide-images/master/collective-knowledge-refs.bib

Testimonials and awards
=======================
* HiPEAC technology transfer award (2014, [HiPEAC TT winners](https://www.hipeac.net/research/technology-transfer-awards/2014))
* ARM and dividiti use CK to accelerate computer engineering (2016, [HiPEAC Info'45](https://www.hipeac.net/assets/public/publications/newsletter/hipeacinfo45.pdf), page 17)

Acknowledgments
===============

CK development is coordinated by the non-profit [cTuning
foundation](http://cTuning.org). We thank the [EU TETRACOM 609491 Coordination
Action](http://tetracom.eu) for initial funding and
[dividiti](http://dividiti.com) for continuing support. We would also like to
thank Microsoft Research program for one-year grant to host the CK public
repository in the Azure cloud.  We are also extremely grateful to all
volunteers for their valuable feedback and contributions.
