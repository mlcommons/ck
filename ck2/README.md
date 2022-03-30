# Collective Mind toolkit (CM or CK2)

We are developing the CM toolkit to help researchers and engineers automate their boring, repetitive and time-consuming tasks
and let them focus on innovation when prototyping complex computational systems and deploying them in the real world.

# Motivation

CM is heavily motivated by our very tedious experience when reproducing 150+ research papers
from the leading ML and Systems conferences and trying to validate some of them in the real world 
across rapidly evolving software, hardware, models and data sets
(see the [ACM TechTalk](https://www.youtube.com/watch?v=7zpeIVwICa4) 
and related [Reddit discussion](https://www.reddit.com/r/MachineLearning/comments/ioq8do/n_reproducing_150_research_papers_the_problems/)). 

We have noticed that nearly each research project used many ad-hoc scripts and artifacts to perform exactly the same tasks 
but just for different hardware, compilers, frameworks, applications, models and data sets including:
* detecting target hardware properties
* downloading various software and data
* detecting and/or installing numerous dependencies for a given host and target hardware
* substitute local paths in numerous scripts, YAML/JSON files and code
* preparing or modifying numerous configuration files
* setting environment variables
* preprocessing datasets
* preparing command lines and running applications
* monitoring execution time, accuracy, energy, memory usage, etc
* post-processing results, recording them to a database, comparing with some reference ones
* visualizing and comparing results
* connecting applications with existing DevOps and MLOps tools
* packing all those ad-hoc scripts and artifacts into containers and deploying them in production 
  using numerous existing solutions and platforms from cloud to edge.

That is why we have decided to design CM as a simple and collaborative playground with minimal dependencies 
to let researchers and practitioners convert their artifacts, knowledge and experience
(code, data, models, scripts, config files, experiments, reference results) 
into reusable automation recipes and objects with a simple API, unified CLI,
and extensible YAML/JSON meta descriptions similar to LEGO bricks.

Such unified bricks can be shared with the community to make it easier to assemble very complex computational systems, 
connect them with existing DevOps and MLOps tools, continuously improve and optimize all components
without breaking backwards compatibility.

One of our long-term goal is to use CM to enable modular AI and automatically synthesize Pareto-efficient ML and AI Systems 
for any platform from cloud to edge based on user requirements and constraints as described in [this article](https://arxiv.org/abs/2011.01149).

CM is the complete redesign of the [CK prototype](https://github.com/mlcommons/ck) that was successfully validated
by [a number of companies and organizations](https://cKnowledge.org/partners.html) 
to [make ML and Systems research more collaborative and reproducible](https://cTuning.org/ae),
modularize and automate the [MLPerf benchmark](https://github.com/mlcommons/ck/tree/master/docs/mlperf-automation),
and accelerate [design space exploration and deployment of efficient AI and ML Systems in production](https://www.youtube.com/watch?v=1ldgVZ64hEI)
from years and months to weeks and days.

# News

* **2022 April 20:** Join us at the public MLCommons community meeting. Register [here](https://docs.google.com/spreadsheets/d/1bb7qWgWM-6gop1Mwjm4u8LZtC7uqbee8C30DHipkkms/edit#gid=533252977).

* **2022 April 3:** Join us at the HPCA'22 workshop on [benchmarking deep learning systems](https://sites.google.com/g.harvard.edu/mlperf-bench-hpca22/home)
  where we will present the CK2 concept for MLPerf design space exploration and production deployment.

* **2022 March:** We presented our [CK concept to enable collaborative and reproducible ML Systems R&D](https://meetings.siam.org/sess/dsp_programsess.cfm?SESSIONCODE=73126) 
  at the SIAM'22 workshop on "Research Challenges and Opportunities within Software Productivity, Sustainability, and Reproducibility"

* **2022 March:** we've released the first prototype of the [CK2 framework](https://github.com/mlcommons/ck/tree/master/ck2)
  based on your feedback! Join this community effort to make it easier to bring research ideas to the real world!

# First steps

* [Installation](docs/first-steps.md)

# Research and development

## CM core

We use [GitHub tickets](https://github.com/mlcommons/ck/issues) to improve the CM core.

## CM-based reusable LEGO-like bricks

* We work with the community to convert research artifacts [from ML and Systems conferences](https://cTuning.org/ae) 
  into [reusable CM components](docs/reusable-components.md).

## Modular CM-based projects

* [Towards modular MLPerf benchmark](docs/projects/modular-mlperf.md).
* [MLPerf design space exploration](docs/projects/mlperf-dse.md).
* [Automated deployment of Pareto-efficient ML Systems](docs/projects/production-deployment.md).

# Resources

* [MLOps and MLPerf](docs/KB/MLOps.md)

# Acknowledgments

We thank the [CK users](https://cKnowledge.org/partners.html), [OctoML](https://octoml.ai), [MLCommons](https://mlcommons.org) 
and all our colleagues for their valuable feedback and support!

# Feedback

We develop the CM framework (CK2) based on the [valuable feedback from the community](https://www.youtube.com/watch?v=7zpeIVwICa4)! 
Please don't hesitate to share your ideas and report encountered issues [here](https://github.com/mlcommons/ck/issues).

# Contacts

* [Grigori Fursin](https://cKnowledge.io/@gfursin) - author and coordinator
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) - coordinator and maintainer
