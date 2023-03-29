# Collective Knowledge Platform

*Note that this is on-going and heavily evolving project - please join our public
 [Discord server](https://discord.gg/JjWNWXKxwT) to discuss this platform,
 request new features, add support for your tools and participate in developments
 and collaborative benchmarking and optimization of AI/ML Systems.*

The [Collective Knowledge Playground (CK)](https://x.cknowledge.org) is a free, open-source and technology-agnostic platform
being developed by the [open MLCommons taskforce on education and reproducibility](https://cKnowledge.org/mlcommons-taskforce).

Our goal is to  empower all software and hardware companies, their partners and users to automatically generate, benchmark and optimize 
full stack AI/ML solutions with any model, data, software and hardware in a unified and reproducible way via public and private optimization 
challenges while slashing development, deployment and operational costs.

This platform is powered by the technology-agnostic [MLCommons Collective Mind workflow automation framework (CM or CK2)](https://github.com/mlcommons/ck)
with [portable and reusable automation recipes](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
developed by the community to solve the "AI/ML dependency hell". 

We continue developing this framework with the community to automatically connect then MLPerf benchmarking  infrastructure with diverse and rapidly evolving models, 
software, hardware, data sets, best practices and optimization techniques in a transparent and non-intrusive way. 


## Private (in-house) use

Install the MLCommons CK2 (CM) framework as described [here](https://github.com/mlcommons/ck/blob/master/docs/installation.md).

Pull CM repository with portable MLOps automation recipes from the community:
```bash
cm pull repo mlcommons@ck
```

Run CK playground GUI on your local machine to aggregate, visualize and reproduce experiments:
```bash
cm run script "gui _playground" 
```

Check [this script](scripts/2-run-in-a-cloud.sh) If you want to run the CK playground 
as a public or private server to run optimization experiments
with your colleagues, external teams and users.

