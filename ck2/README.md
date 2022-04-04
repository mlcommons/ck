# Collective Mind toolkit (CM or CK2)

The CM toolkit transforms Git repositories, Docker containers, Jupyter notebooks and zip/tar files
into a database of reusable artifacts and automations with a unified CLI and extensible meta descriptions.

It is motivated by our tedious experience reproducing [150+ ML and Systems papers](https://www.youtube.com/watch?v=7zpeIVwICa4)
and spending many months analyzing the structure of ad-hoc projects
to validate and reuse them in the real world with different environments, settings, 
data sets, libraries, tools and platforms.

That is why we have decided to provide a very simple and common structure for shared projects
that makes it possible to exchange all artifacts, knowledge, experience and best practices 
between researchers, engineers, teams and organizations 
in an automated, reusable and reproducible way.

CM toolkit is based on the [Collective Knowledge concept](https://arxiv.org/abs/2011.01149)
that was successfully validated in the past few years to [enable collaborative ML and Systems R&D](https://cKnowledge.org/partners.html)
and modularize the [MLPerf inference benchmark](https://github.com/mlcommons/ck/tree/master/docs/mlperf-automation).

# How it works

## Install CM

CM toolkit is implemented as a small Python library with a unified CLI and a simple API.

It requires minimal dependencies (Python 3+, pip, pyyaml and a Git client) 
and should work with any OS including Linux, CentOS, Debian, RedHat and Windows.

```bash
pip3 install cmind
```

You can find more details about the installation process [here](docs/installation.md).








# News

* **2022 April 20:** Join us at the public MLCommons community meeting. Register [here](https://docs.google.com/spreadsheets/d/1bb7qWgWM-6gop1Mwjm4u8LZtC7uqbee8C30DHipkkms/edit#gid=533252977).

* **2022 April 3:** We presented our approach to bridge the growing gap between ML Systems research and production 
  at the HPCA'22 workshop on [benchmarking deep learning systems](https://sites.google.com/g.harvard.edu/mlperf-bench-hpca22/home).

* **2022 March:** We presented our concept to [enable collaborative and reproducible ML Systems R&D](https://meetings.siam.org/sess/dsp_programsess.cfm?SESSIONCODE=73126) 
  at the SIAM'22 workshop on "Research Challenges and Opportunities within Software Productivity, Sustainability, and Reproducibility"

* **2022 March:** we've released the first prototype of [our toolkit ](https://github.com/mlcommons/ck/tree/master/ck2)
  based on your feedback and our practical experience [reproducing 150+ ML and Systems papers and validating them in the real world](https://www.youtube.com/watch?v=7zpeIVwICa4).
! 


# Research and development

## CM core enhancements

We use [GitHub tickets](https://github.com/mlcommons/ck/issues) 
to improve and enhance the CM core based on the feedback from our users!

## CM-based automation recipes

* We work with the community to convert projects [from ML and Systems papers](https://cTuning.org/ae) 
  into [reusable CM artifacts and automation recipes](docs/reusable-components.md). 
  Feel free to suggest your own automation recipes to be reused by the community.

## CM-based projects

* [Towards modular MLPerf benchmark](docs/projects/modular-mlperf.md).
* [MLPerf design space exploration](docs/projects/mlperf-dse.md).
* [Automated deployment of Pareto-efficient ML Systems](docs/projects/production-deployment.md).

# Resources

* [MLOps projects](docs/KB/MLOps.md)

# Acknowledgments and feedback

We thank the [CK users](https://cKnowledge.org/partners.html), [OctoML](https://octoml.ai), [MLCommons](https://mlcommons.org) 
and all our colleagues for their valuable feedback and support!

Please don't hesitate to share your ideas and report encountered issues [here](https://github.com/mlcommons/ck/issues).

# Contacts

* [Grigori Fursin](https://cKnowledge.io/@gfursin) - author and coordinator
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) - coordinator and maintainer
