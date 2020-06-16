# CK Portal API

The cKnowledge portal features an open JSON API to download and publish AI/ML/systems components, workflows and solutions, 
and to create customizable dashboards for auto-generated live papers, collaborative and reproducible benchmarking,
and MLSysOps.

cKnowledge API URL: [http://cKnowledge.io/api/v1/?](http://cKnowledge.io/api/v1/?)

[cBench](https://github.com/ctuning/cbench) provides a user-friendly access to this API. 

You can also use Curl to test it as follows:
```
curl -d @cbench-input.json -H "Content-Type: application/json"  https://cKnowledge.io/api/v1/? -o cbench-output.json
```
where *cbench-input.json* contains a Json dictionary with commands listed below.

If you have cBench installed, you can use the following command to test the low-level access to this API instead of Curl:
```
cr access --json="{'action':'get_obj_info', 'dict':{'module_uoa':'package', 'data_uoa':'lib-tensorflow-1.14.0-src-cuda'}}"

```

## JSON Input

The Json input has the following format:
```
{
  "action" [str] - See cKnowledge API actions below

  "dict" [dict] - Action parameters

  ("username") [str] - cKnowledge username
  ("api_key") [str] - cKnowledge API key

}
```

## JSON Output

The Json output has the following format if operation was successful:

```
{
  "return" [int] - 0 if success
  ...
  action output
}
```

Whenever there is an error, this Json output will have the following format:
```
{
  "return" [int] - >0 if error
  "error" [str] - Error text
}
```

## Available actions

### Test login

*Test the login to the cKnowledge platform.*

You can register [here](https://cKnowledge.io/register)
and then get your cKnowledge username and the API key [here](https://cKnowledge.io/settings).

JSON input:

```
{
  "action":"login",
  "username" [str] - cKnowledge username,
  "api_key" [str] - cKnowledge API key
}
```

JSON output:
```
{
  "return":0
}
```

### List cKnowledge AI/ML/systems components

*List CK components abstracted by a given CK module*

You can see the list of shared CK modules [here](https://cKnowledge.io/c/module).

JSON input:

```
{
  "action":"list_components",

  "dict":{
    "module_uoa" [str] - Module name from above list
  }
}
```

JSON output:
```
{
  "return":0,
  "lst": [
    list of CK components in the open CK format
  ]
}
```

### Download components

*Download a given component*

You can see the list of shared CK components [here](https://cKnowledge.io).

JSON input:

```
{
  "action":"download",

  "dict":{
    "module_uoa" [str] - Module name from above list
    "data_uoa" [str] - Data name from above list
    ("version") [str] - component version
  }
}
```

JSON output:
```
{
  "return":0,
  "components": [
    {
      "file_base64" [str]
      "file_md5" [str]
      "data_uid" [str]
      "data_uoa" [str]
      "module_uid" [str]
      "module_uoa" [str]
      "dependencies" [list]
    },
    ...
  ]
}
```

### Get component info

*Get meta description of a given component*

You can see the list of shared CK components [here](https://cKnowledge.io).

JSON input:

```
{
  "action":"get_obj_info",

  "dict":{
    "module_uoa" [str] - Module name from above list
    "data_uoa" [str] - Data name from above list
    ("version") [str] - component version
    ("load_json_file") [str] - load specific JSON file and add it to the output
  }
}
```

JSON output:
```
{
  "return":0,

  "data_uid" [str]
  "data_uoa" [str]

  "module_uid" [str]
  "module_uoa" [str]

  "component_dict" [dict]

  "version" [str] - latest version if not specified in the input

  ("json_from_file") [dict] - 
}
```

### Publish components

*Publish a new component*

JSON input:

```
{
  "action":"publish",

  "dict":{
    "publish_module_uoa" [str] - Module name
    "publish_module_uid" [str] - Module UID

    "publish_data_uoa" [str] - Data name
    "publish_data_uid" [str] - Data UID
    "publish_data_name" [str] - Data short and user-friendly description

    "publish_pack" [str] - CK component zip file in the base64 format 
    "publish_pack_size" [str] - size of the above zip file

    "version" [str] - component version
  }

  (
   "ownership":{
     private [bool] - private component, if True
     workspaces [list] - list of cKnowledge workspaces
   }
  )

}
```

JSON output:
```
{
  "return":0
}
```

### Get results

*Get results from a public dashboard*

You can find a list of dashboards with data names [here](https://cKnowledge.io/results).

JSON input:

```
{
  "action":"get_result",

  "dict":{
    "data_uoa" [str] - Result data name from the above list
    ("version") [str] - Result version
    ("stat_analysis") [bool] - Perform statistical analysis of results
  }
}
```

JSON output:
```
{
  "return":0
  "table": [
    list of experimental results
  ],
  "number_of_users" [int] - number of cKnowledge users pushing results to the entry
}
```

Example:
```
cr access --json="{'action':'get_result', 'dict':{'data_uoa':'demo-obj-detection-coco-tf-cpu-benchmark-linux-demo'}}"

cr access --json="{'action':'get_result', 'dict':{'data_uoa':'demo-obj-detection-coco-tf-cpu-benchmark-linux-demo', 'stat_analysis':'yes'}}"
```

### Publish results

*Push results to a cKnowledge dashboard*

JSON input:

```
{
  "action":"push_result",

  "dict":{
    "data_uoa" [str] - Result data name from the above list
    ("version") [str] - Result version
    "data" [dict] - Dictionary with all results
    ("point") [str] - overwrite existing data point
  }
}
```

JSON output:
```
{
  "return":0
}
```
