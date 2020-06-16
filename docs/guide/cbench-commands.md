# cBench commands

After installing [cBench](../getting-started/installation) you can use the following commands:





## Setup and low-level access

### Check the client version

```
cb version
```

### Update client dependencies (CK components)

```
cb update
```

### Setup the cKnowledge account

*Setup your cKnowledge account to be able to publish new components and participate in crowd-benchmarking.*

```
cb setup --help
```

You can register your cKnowledge account [here](https://cKnowledge.io/register)
and get your *username* and *api_key* [here](https://cKnowledge.io/settings).

You can then setup your cKnowledge account as follows:
```
cb setup --username="{above username}" --api_key="{above key}"
```

### Test the login

*Test the login to the cKnowledge portal*

```
cb login --help
```

After you setup your account you can test the login as follows:
```
cb login
```

  access       CID:ck component identifier (repo UOA:)module UOA:data UOA
  start        Start the client to communicate with the cKnowledge portal


### Access the open cKnowledge API

*Test the low-level access to the open cKnowledge.io JSON API.*

```
cb access --help
```

You can access the [cKnowledge JSON API](../resources/api) using input JSON file as follows:

```
cb access --filename=input.json
```

You can also write JSON dictionary in the command line while substituting *"* with *'*:
```
cb access --json="{'action':'login'}"
```

### Start the local server

*Run internal server on a user machine to automate the communication with the cKnowledge portal.*

```
cb start
```

Note that you need to add flag "-h 0.0.0.0" if you start it from Docker:

```
cb start -h 0.0.0.0
```

See the [demo of cBench](https://cKnowledge.io/c/solution/demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows/) 
communicating with the cKnowledge portal to crowd-benchmark MLPerf.





## CK components

### Download components

*Download a given CK component to your local CK repository.*

```
cb download --help
```

You can download a given [CK component](https://github.com/ctuning/ck) 
from the [cKnowledge portal](https://cKnowledge.io) 
with a given version using the following command:
```
cb download {module name}:{data name} (--version=1.0.0)
```

For example, you can download SSD-mobilenet package:
```
cb download package:model-tf-mlperf-ssd-mobilenet --version=1.0.0
```

You can use wildcards in the names of the CK components.

If this component already exists you can overwrite it by adding the flag "--force" or "-f".

You can download the CK component with all related dependencies by adding the flag "--all" or "-a". 
For example you can download program:cbench-automotive-susan with all related components 
and related data sets, and then immediately compile and run it as follows:
```
cb download program:cbench-automotive-susan --all
cb download dataset:* --tags="image,dataset"

ck compile program:cbench-automotive-susan --speed
ck run program:cbench-automotive-susan
```

### Publish components

*Publish/update CK component on the cKnowledge portal.*


```
cb publish --help
```

You need to register at the cKnowledge portal (similar to PyPI or GitHub)
to publish your components or update existing ones as described [here](#setup-the-cknowledge-account).

When you create new CK components or update existing ones, 
you can then publish the stable version on the [cKnowledge portal](https://cKnowledge.io)
as follows:

```
cb publish {module name}:{data name} --version={version}
```

You can check the latest version of a given component at the cKnowledge portal as follows:
```
cb versions {module name}:{data name}
```

You can specify extra options describing your component:
```
 --author TEXT
 --author_id TEXT
 --copyright TEXT
 --license TEXT
 --source TEXT
```

You can make this component private by specifying the flag "--private". 
In such case, it will be only visible to you.

### List versions of a given component

*List versions of a given CK component at the cKnowledge portal.*


```
cb versions --help
```

You can list all shared versions of a given CK component shared at the [cKnowledge portal](https://cKnowledge.io)
as follows:

```
cb versions {module name}:{data name}
```

### Open a cKnowledge web page with a given component

*Open a cKnowledge.io web page with a given component.*


```
cb open {module name}:{data name}
```

## cKnowledge dashboards

The cKnowledge portal supports customizable dashboards to support 
MLSysOps, collaborative experimentation, and live research papers.

### Initialize a cKnowledge graph

*Create a new dashboard on the portal.*

```
cb init-graph --help
```

You can check examples of public cKnowledge dashboards [here](https://cKnowledge.io/results).
You can then create your own one as follows:
```
cb init-graph {some name for your dashboard} --version={version of your dashboard} --desc_file="$PWD/graph-desc.json"
```

Here is the example of the "graph-desc.json" to aggregate results from this [MLPerf crowd-benchmarking solution](https://cKnowledge.io/c/solution/demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows):


```
{
    "default_key_x": "avg_time_ms",
    "default_key_y": "mAP",
    "default_sort_key": "avg_time_ms",
    "table_view": [
      {"key": "platform_info", "name": "Platform info", "json_and_pre": "yes", "skip_pre": "yes"},
      {"key": "resolved_deps", "name": "Resolved deps", "json_and_pre": "yes", "skip_pre": "yes"},
      {"key": "avg_fps", "type":"float", "format": "%.2f", "name": "Average FPS"},
      {"key": "avg_time_ms", "type":"float", "format": "%.2f", "name": "Average time (ms.)"},
      {"key": "detection_time_avg_s", "type":"float", "format": "%.2f", "name": "Detection time (average, sec.)"},
      {"key": "detection_time_total_s", "type":"float", "format": "%.2f", "name": "Detection time (total, sec.)"},
      {"key": "graph_load_time_s", "type":"float", "format": "%.2f", "name": "Graph load time (sec.)"},
      {"key": "images_load_time_avg_s", "type":"float", "format": "%.2f", "name": "Images load time (average, sec.)"},
      {"key": "images_load_time_total_s", "type":"float", "format": "%.2f", "name": "Images load time (total, sec.)"},
      {"key": "mAP", "type":"float", "format": "%.2f", "name": "mAP"},
      {"key": "metrics#DetectionBoxes_Precision/mAP", "type":"float", "format": "%.2f", "name": "Detection Boxes Precision mAP"},
      {"key": "metrics#DetectionBoxes_Precision/mAP (large)", "type":"float", "format": "%.2f", "name": "Detection Boxes Precision mAP (large)"},
      {"key": "metrics#DetectionBoxes_Precision/mAP (medium)", "type":"float", "format": "%.2f", "name": "Detection Boxes Precision mAP (medium)"},
      {"key": "metrics#DetectionBoxes_Precision/mAP (small)", "type":"float", "format": "%.2f", "name": "Detection Boxes Precision mAP (small)"},
      {"key": "metrics#DetectionBoxes_Precision/mAP@.50IOU", "type":"float", "format": "%.2f", "name": "Detection Boxes Precision mAP (.50 IOU)"},
      {"key": "metrics#DetectionBoxes_Precision/mAP@.75IOU", "type":"float", "format": "%.2f", "name": "Detection Boxes Precision mAP (.75 IOU)"},
      {"key": "metrics#DetectionBoxes_Recall/AR@1", "type":"float", "format": "%.2f", "name": "Detection Boxes Recall AR@1"},
      {"key": "metrics#DetectionBoxes_Recall/AR@10", "type":"float", "format": "%.2f", "name": "Detection Boxes Recall AR@10"},
      {"key": "metrics#DetectionBoxes_Recall/AR@100", "type":"float", "format": "%.2f", "name": "Detection Boxes Recall AR@100"},
      {"key": "metrics#DetectionBoxes_Recall/AR@100 (large)", "type":"float", "format": "%.2f", "name": "Detection Boxes Recall AR@100 (large)"},
      {"key": "metrics#DetectionBoxes_Recall/AR@100 (medium)", "type":"float", "format": "%.2f", "name": "Detection Boxes Recall AR@100 (medium)"},
      {"key": "metrics#DetectionBoxes_Recall/AR@100 (small)", "type":"float", "format": "%.2f", "name": "Detection Boxes Recall AR@100 (small)"},
      {"key": "recall", "type":"float", "format": "%.2f", "name": "Recall"},
      {"key": "setup_time_s", "type":"float", "format": "%.2f", "name": "Setup time (sec.)"},
      {"key": "test_time_s", "type":"float", "format": "%.2f", "name": "Test time (sec.)"},
      {"key": "solution_run_date", "type":"string", "format": "%Y-%m-%dT%H:%M:%SZ", "name": "Start date"},
      {"key": "solution_duration", "type":"float", "format": "%.2f", "name": "Total bechmark time (sec.)"}
    ]
}

```

### Push results

*Push results to existing dashboards.*

```
cb push-result --help
```

First, you need to check the meta description of a given graph (dashboard or scoreboard) using the link "graph meta description".

You can push the new results to the [existing dashboard](https://cKnowledge.io/results) as follows:

```
cb push-result {name of the existing dashboard} --json="[{'key1':value1,'key2':value2 ...}]"

```

You can find the format of accepted values for keys in the "table_view" list in the graph meta description.


You can also push multiple blobs of results at the saemt time:

```
cb push-result {name of the existing dashboard} --json="[{'x':3,'y':-3}, {'x':4, 'y':5}]"

```
or
```
cb push-result {name of the existing dashboard} --file="$PWD/result.json"
```

where "result.json" contains a list of dictionaries with results.





## cKnowledge solutions

The client can help to initialize, download, test and run [AI/ML solutions](https://cKnowledge.io/c/solution)
across diverse platforms as shown in this [demo](https://cKnowledge.io/solution/demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows/).

### Download and initialize the existing solution

*Download existing or start the new cKnowledge solution*

```
cb init --help
```

You can download existing solution from this [list](https://cKnowledge.io/c/solution) as follows:

```
cb init demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows
```

Note that cBench will attempt to automatically download all required CK components 
(models, data sets, frameworks, packages, etc) and install missing software dependencies.
However, the installation of system packages is not yet automated and must be done manually 
(our future work).

### Run a solution

*Run initialized solution*

```
cb run --help
```

After a given solution is initialized on a user machine, it is possible to run it as follows:
```
cb run {name of the solution}
```

For example, it is possible to run the MLPerf inference benchmarking solution as follows:

```
cb init demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows
```

### Benchmark a solution

*Crowd-benchmark the solution and share results on a cKnowledge dashboard*

```
cb benchmark --help
```

When a given solution is initialized and can run on a given machine, it is possible
to participate in crowd-benchmarking and share results (speed, accuracy, energy, costs
and other exposed characteristics) using cKnowledge dashboards similar to SETI@home.

Do not forget to setup your cKnowledge account using "cb setup" before participating
in crowd-benchmarking.

For example, it is possible to participate in collaborative validation
of MLPerf inference benchmarking as follows:

```
cb benchmark demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows
```

You can view the crowd-benchmarked results and compare with the official ones 
at this [public cKnowledge dashboard](https://cKnowledge.io/c/result/sota-mlperf-object-detection-v0.5-crowd-benchmarking).

We are also working on a user-friendly GUI to enable MLSysOps and monitor ML in production.

### Activate a virtual environment for the solution

*Activate virtual environment for a given solution*

```
cb activate --help
```

After a given solution is initialized, all required software is detected and all missing packages are installed, 
it is possible to activate the virtual environment for this solution to continue testing and debugging it as follows:

```
cb activate {name of the solution}
```

Example:
```
cb activate demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows
```

You can then use [CK](https://github.com/ctuning/ck) as well as cBench
to improve/update this solution. 

We plan to provide a tutorial about that.

### List local solutions

You can list all local solutions using the following command:

```
cb ls
```

### Find local solutions

You can find the place where a given local solution is initialized together 
with all the components and a virtual environment as follows:

```
cb find {name of the solution}
```

Example:
```
cb find demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows
```

### Delete local solutions

You can delete a locally initialized solution as follows:

```
cb rm {name of the solution}
```

Example:

```
cb rm demo-obj-detection-coco-tf-cpu-benchmark-linux-portable-workflows
```

### Create a new solution

*To be updated*

At the moment it is possible to create a portable CK solution from CK [program pipelines](https://cKnowledge.io/programs).
We plan to add a possibility to create a CK solution for any workflow.

You can follow this [real example](https://github.com/ctuning/cbench/tree/master/examples/solutions/mlperf-inference-v0.5-detection-openvino-ssd-mobilenet-coco-500-linux)
to automate the MLPerf inference benchmark submissions. 
It shows how to create a CK solution to prepare object classification benchmark with Intel OpenVINO, SSD-Mobilenet, COCO data set and 500 images.

First you need to create a public scoreboard as described above.
You can initialize such scoreboard using [this script](https://github.com/ctuning/cbench/blob/master/examples/solutions/mlperf-inference-v0.5-detection-openvino-ssd-mobilenet-coco-500-linux/_init_graph.sh) 
and this [graph meta description](https://github.com/ctuning/cbench/blob/master/examples/solutions/mlperf-inference-v0.5-detection-openvino-ssd-mobilenet-coco-500-linux/graph-desc.json).

If you want to push crowd results to an existing [dashboard](https://cKnowledge.io/c/result), 
you need to create [graph-convertor.json](https://github.com/ctuning/cbench/blob/master/examples/solutions/mlperf-inference-v0.5-detection-openvino-ssd-mobilenet-coco-500-linux/graph-convertor.json).

After that you need to create two text files:
* [prereq.txt](https://github.com/ctuning/cbench/blob/master/examples/solutions/mlperf-inference-v0.5-detection-openvino-ssd-mobilenet-coco-500-linux/prereq.txt) 
  describing all OS-specific prerequisites
* [prepare.txt](https://github.com/ctuning/cbench/blob/master/examples/solutions/mlperf-inference-v0.5-detection-openvino-ssd-mobilenet-coco-500-linux/prepare.txt)
  describing CK components and installation procedures.

Finally, you need to initialize your solution as show in this [sample script](https://github.com/ctuning/cbench/blob/master/examples/solutions/mlperf-inference-v0.5-detection-openvino-ssd-mobilenet-coco-500-linux/_init.sh).

If you successfully initialized this solution on your machine, you can then push it to the cKnowledge.io platform 
as shown in this [sample script]( https://github.com/ctuning/cbench/blob/master/examples/solutions/mlperf-inference-v0.5-detection-openvino-ssd-mobilenet-coco-500-linux/_publish.sh ).
  
We plan to considerably improve this section. If you have questions or suggestions, do not hesitate to [get in touch](https://cKnowledge.org/contacts).
