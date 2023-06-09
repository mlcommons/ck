# CM "experiment" automation

*We suggest you to check [CM introduction](https://github.com/mlcommons/ck/blob/master/docs/introduction-cm.md), 
 [CM CLI/API](https://github.com/mlcommons/ck/blob/master/docs/interface.md) 
 and [CM scripts](../script/README-extra.md) to understand CM motivation and concepts.
 You can also try [CM tutorials](https://github.com/mlcommons/ck/blob/master/docs/tutorials/README.md) 
 to run some applications and benchmarks on your platform using CM scripts.*

## Introducing CM experiment automation


Researchers, engineers and students spend considerable amount of their time experimenting with 
many different settings of applications, tools, compilers, software and hardware 
to find the optimal combination suitable for their use cases.

Based on their feedback, our [MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md) 
started developing a CM automation called "experiment". 
The goal is to provide a common interface to run, record, share, visualize and reproduce experiments
on any platform with any software, hardware and data.

The community helped us test a prototype of our "experiment" automation to record results in a unified CM format 
from [several MLPerf benchmarks](https://github.com/mlcommons/cm_inference_results) 
including [MLPerf inference](https://github.com/mlcommons/inference) and [MLPerf Tiny](https://github.com/mlcommons/tiny),
visualize them at the [MLCommons CM platform](https://access.cknowledge.org/playground/?action=experiments&tags=all),
and improve them by the community via [public reproducibility and optimization challenges](https://access.cknowledge.org/playground/?action=challenges).



## Installing CM with ResearchOps/DevOps/MLOps automations

This CM automation is available in the most commonly used `mlcommons@ck` repository. 

First, install CM automation language as described [here](https://github.com/mlcommons/ck/blob/master/docs/installation.md).
Then, install or update this repository as follows:
```bash
cm pull repo mlcommons@ck
```

You can now test that CM experiment automation is available as follows:
```bash
cm run experiment --help
```
or using `cme` shortcut in CM V1.4.1+
```bash
cme --help
```



## Understanding CM experiments

CM experiment wraps any user command line, creates an associated CM `experiment` artifact with some user tags and {date}{time} subdirectory,
records input in `cm-input.json`, and executes the user command line inside this subdirectory.

The following command will print "Hello World!" while recording all the provenance in CM format in the local CM repository:

```bash
cme --tags=my,experiment,hello-world -- echo "Hello World!"
```
or
```bash
cm run experiment --tags=my,experiment,hello-world -- echo "Hello World!"
```

You should see the output similar to the following:
```bash

Path to CM experiment artifact: C:\Users\gfursin\CM\repos\local\experiment\b83a1fb24dbf4945
Path to experiment: C:\Users\gfursin\CM\repos\local\experiment\b83a1fb24dbf4945\2023-06-09.09-58-02.863466
================================================================
Experiment step: 1 out of 1

Path to experiment step: C:\Users\gfursin\CM\repos\local\experiment\b83a1fb24dbf4945\2023-06-09.09-58-02.863466\7ed0ea0edd6b4dd7

"Hello World!"
```

You can find and explore the newly created CM artifact as follows:
```bash
cm find experiment --tags=my,experiment,hello-world
```
or using UID
```bash
cm find experiment b83a1fb24dbf4945
```

When running the same experiment again, CM will find existing artifact by tags and create new {date}{time} directory there:
```bash
cme --tags=my,experiment,hello-world -- echo "Hello World!"

Path to CM experiment artifact: C:\Users\gfursin\CM\repos\local\experiment\b83a1fb24dbf4945
Path to experiment: C:\Users\gfursin\CM\repos\local\experiment\b83a1fb24dbf4945\2023-06-09.10-02-08.911210
================================================================
Experiment step: 1 out of 1

Path to experiment step: C:\Users\gfursin\CM\repos\local\experiment\b83a1fb24dbf4945\2023-06-09.10-02-08.911210\7ed0ea0edd6b4dd7

"Hello World!"
```

You can now replay this experiment as follows:
```bash
cm replay experiment --tags=my,experiment,hello-world
```

Note that you can obtain current directory where you called CM 
(rather than the CM experiment artifact directory) via {{CD}} variable as follows:
```bash
cme --tags=my,experiment,hello-world -- echo {{CD}}
``


## Exploring combinations of parameters (autotuning, design space exploration)

One of the most common tasks is computer engineering (and other sciences)
is to explore various combinations of parameters of some applications 
and systems to select the optimal ones to trade off performance, accuracy, 
power consumption, memory usage and other characteristics.

As a starting point, we have implemented a very simple explorer as a cartesian product
of any number of specified variables that are passed to a user command line via double curly braces `{{VAR}}` similar to GitHub.

You just need to create a simple JSON file `cm-input.json` to describe sets/ranges for each variable as follows:
```json
{
  "explore": {
    "VAR1": [
      1,
      2,
      3
    ],
    "VAR2": [
      "a",
      "b"
    ],
    "VAR3": "[2**i for i in range(0,6)]"
  }
}
```

or YAML `cm-input.yaml`:

```yaml
explore:
  VAR1: [1,2,3]
  VAR2: ["a","b"]
  VAR3: "[2**i for i in range(0,6)]"
```

You can then run the following example to see all iterations:
```bash
cm run experiment --tags=my,experiment,hello-world @test_input.yaml \
     -- echo %VAR1% --batch_size={{VAR1}} {{VAR2}} {{VAR4{['xx','yy','zz']}}}-%%VAR3%%
```

Note that you can also define a Python list of range for other variables 
directly in the command line as demonstrated in above example for `VAR4` - `{{VAR4{['xx','yy','zz']}}}`.

CM will create or reuse experiment artifact with tags `my,experiment,hello-world`
and will then iterate in a cartesian product of all detected variables.

For each iteration, CM will create a `{date}{time}` subdirectory in a given experiment artifact
and will then run a user command line with substituted variables there.

You can then replay any of the exploration experiment as follows:
```bash
cm replay experiment --tags={tags} --dir={sub directory}
```



## Aggregating and unifying results


, and aggregates results from `cm-result.json` 
if produced by a user application, tool or script.



## Visualizing results

cm run script "gui _playground"



## Participating in further developments

