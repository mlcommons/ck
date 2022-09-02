# CM repository to modularize ML and AI Systems

[![CM repository](https://img.shields.io/badge/Collective%20Mind-compatible-blue)](https://github.com/mlcommons/ck/tree/master/cm)
[![CM artifact](https://img.shields.io/badge/Artifact-automated%20and%20reusable-blue)](https://github.com/mlcommons/ck/tree/master/cm)


It is becoming very challenging to co-design, optimize and deploy efficient AI and ML Systems in the real world:
["MLOps Is a Mess But That's to be Expected"](https://www.mihaileric.com/posts/mlops-is-a-mess).

However, [our experience](https://doi.org/10.5281/zenodo.6475385) 
suggests that it is possible to [apply DevOps principles to MLOps](https://www.datanami.com/2022/03/30/birds-arent-real-and-neither-is-mlops/)
if we treat all AI, ML and Systems artifacts including models, data sets, frameworks, libraries and scripts as "code" meta packages 
with dependencies on other artifacts, operating systems and hardware.

We use this [CM-based repository](https://github.com/mlcommons/cm-mlops) 
as a common playground and a common language to learn with the community
how to automate benchmarking, optimization, co-design and deployment
of complex ML Systems and make it more deterministic, portable and reproducible 
across continusly changing software and hardware stacks.


# How to use

## Install CM toolkit and dependencies

Install the CM toolkit as described [here](https://github.com/mlcommons/ck/blob/master/cm/docs/installation.md).

## Install this CM repository

Use CM to install this repository on your system:

```bash
$ cm pull repo mlcommons@ck
```

You can see this and other CM-compatible repositories installed on your system as follows:
```bash
$ cm list repo
```

You can list reusable automations as follows:
```bash
$ cm find automation
```

You can now list available MLOps automation scripts as follows:
```bash
$ cm list script
```

You can run any portable and reusable MLOps automation script as follows:
```bash
$ cm run script {CM script alias or UID}
```


*More to come soon ...*


## Check CM tutorials

TBD


# Contacts

* [Grigori Fursin](https://cKnowledge.io/@gfursin)
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh)
