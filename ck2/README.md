# Collective Mind toolkit

[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/ck2)
[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://badge.fury.io/py/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](https://github.com/mlcommons/ck/tree/master/ck2)


CM transforms Git repositories, Docker containers, Jupyter notebooks, zip/tar files
and any local directory into a collective database of reusable artifacts 
and automation scripts with a unified interface and extensible meta descriptions.

Our goal is to help researchers and engineers exchange their artifacts, knowledge, 
experience and best practices in a more unified, automated, reusable, portable and reproducible way
across rapidly evolving software and hardware.

It is motivated by our tedious experience reproducing [150+ ML and Systems papers](https://www.youtube.com/watch?v=7zpeIVwICa4)
when we have spent many frustrating months communicating with researchers and engineers 
to understand numerous README files, specifications, SW/HW dependencies, ad-hoc scripts, tools, APIs, models and data sets
of their projects to be able to [reproduce experimental results](https://cTuning.org/ae) 
and [validate them in the real world](https://cKnowledge.org/partners.html) 
with continuously changing software, hardware, user environments, settings and data.

That is why we believe that having a simple, common and extensible format and API for shared projects 
will make it easier for researchers and engineers to communicate, collaborate and innovate
when developing complex computational systems.

The CM toolkit is based on the [Collective Knowledge concept]( https://arxiv.org/abs/2011.01149 )
that was successfully validated in the past few years to 
[enable collaborative ML and Systems R&D](https://cKnowledge.org/partners.html),
[connect MLOps and DevOps by treating models, datasets and other artifacts as "code" packages](https://github.com/mlcommons/ck-mlops),
modularize the [MLPerf inference benchmark](https://github.com/mlcommons/ck/tree/master/docs/mlperf-automation),
and [automate the development and deployment of Pareto-efficient ML Systems in the real world](https://www.youtube.com/watch?v=1ldgVZ64hEI).


See a few [related slides](docs/motivation.md) and a related article 
about ["MLOps Is a Mess But That's to be Expected"](https://www.mihaileric.com/posts/mlops-is-a-mess/) (March 2022).



# License

Apache 2.0



# How it works

* Check this [getting started tutorial](docs/getting-started.md) 
  to undestand the Collective Mind concepts and try this toolkit.


# Community meetings

* [Public notes](meetings/)
* [Regular conf-calls](meetings/conf-calls.md)


# News

* **2022 April 20:** Join us at the public MLCommons community meeting. Register [here](https://docs.google.com/spreadsheets/d/1bb7qWgWM-6gop1Mwjm4u8LZtC7uqbee8C30DHipkkms/edit#gid=533252977).

* **2022 April 3:** We presented our approach to bridge the growing gap between ML Systems research and production 
  at the HPCA'22 workshop on [benchmarking deep learning systems](https://sites.google.com/g.harvard.edu/mlperf-bench-hpca22/home).

* **2022 March:** We presented our concept to [enable collaborative and reproducible ML Systems R&D](https://meetings.siam.org/sess/dsp_programsess.cfm?SESSIONCODE=73126) 
  at the SIAM'22 workshop on "Research Challenges and Opportunities within Software Productivity, Sustainability, and Reproducibility"

* **2022 March:** we've released the first prototype of [the Collective Mind toolkit (CK2)](https://github.com/mlcommons/ck/tree/master/ck2)
  based on your feedback and our practical experience [reproducing 150+ ML and Systems papers and validating them in the real world](https://www.youtube.com/watch?v=7zpeIVwICa4).



# Documentation

* [User guide and API (under development)](https://cknowledge.org/docs/cm)



# Development

## CM core 

We use [GitHub tickets](https://github.com/mlcommons/ck/issues) 
to improve and enhance the CM core that manages shared projects
as a collective database of reusable artifacts and automations.
Please don't hesitate to share your ideas and report encountered issues!


## Reusable CM objects

* We work with the community to transform existing AI, ML and Systems projects
  into [reusable CM components](docs/reusable-cm-mlops-components.md).
  

## Modular CM-based projects

We work with the community to enable modular AI from reusable CM components 
and fully automate co-designing, benchmarking, optimization and deployment 
of intelligent and Pareto-efficient systems across continuously changing software and hardware stacks.

We participate in the following CM-based projects:

* [Enabling modular AI and automating their co-design, benchmarking, optimization and deployment](docs/projects/modular-ai.md).
  * [Enabling modular MLPerf benchmark](docs/projects/modular-mlperf.md).
  * [Automating MLPerf design space exploration](docs/projects/modular-mlperf-dse.md).
* [Automating artifact evaluation at ML and Systems conferences](docs/projects/automated-ae.md)



# Resources

* [MLOps projects](docs/KB/MLOps.md)


# Acknowledgments

We thank the [users and partners of the original CK framework](https://cKnowledge.org/partners.html), 
[OctoML](https://octoml.ai), [MLCommons](https://mlcommons.org) 
and all our colleagues for their valuable feedback and support!


# Contacts

* [Grigori Fursin](https://cKnowledge.io/@gfursin) - author and coordinator
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) - coordinator and maintainer
