import cmind
import os
import sys

models = {
        "mobilenet": {
            "v1": {
                "multiplier": [ "multiplier-1.0", "multiplier-0.75", "multiplier-0.5", "multiplier-0.25" ],
                "resolution": [ "resolution-224", "resolution-192", "resolution-160", "resolution-128" ],
                "kind": [""]
                },
            "v2": {
                "multiplier": [ "multiplier-1.0", "multiplier-0.75", "multiplier-0.5", "multiplier-0.35" ],
                "resolution": [ "resolution-224", "resolution-192", "resolution-160", "resolution-128" ],
                "kind": [""]
                },
            "v3": {
                "multiplier": [""],
                "resolution": [""],
                "kind": [ "large", "large-minimalistic", "small", "small-minimalistic" ]
                }
            },
        "efficientnet": {
            "": {
                "multiplier": [""],
                "resolution": [""],
                "kind": [ "lite0", "lite1", "lite2", "lite3", "lite4" ]
                }
            }
        }
variation_strings = {}
for t1 in models:
    variation_strings[t1] = []
    variation_list = []
    variation_list.append(t1)
    for version in models[t1]:
        variation_list = []
        if version.strip():
            variation_list.append("_"+version)
        variation_list_saved = variation_list.copy()
        for k1 in models[t1][version]["multiplier"]:
            variation_list = variation_list_saved.copy()
            if k1.strip():
                variation_list.append("_"+k1)
            variation_list_saved_2 = variation_list.copy()
            for k2 in models[t1][version]["resolution"]:
                variation_list = variation_list_saved_2.copy()
                if k2.strip():
                    variation_list.append("_"+k2)
                variation_list_saved_3 = variation_list.copy()
                for k3 in models[t1][version]["kind"]:
                    variation_list = variation_list_saved_3.copy()
                    if k3.strip():
                        variation_list.append("_"+k3)
                    variation_strings[t1].append(",".join(variation_list))
args = sys.argv

opt=None
if len(args) > 1:
    opt = args[1]
if opt=="submission":
    var="_submission"
    execution_mode="valid"
else:
    var="_find-performance"
    execution_mode="test"

precisions = [ "fp32", "uint8" ]
for model in variation_strings:
    for v in variation_strings[model]:
        for precision in precisions:
            if "small-minimalistic" in v and precision == "uint8":
                continue;
            if model == "efficientnet" and precision == "uint8":
                precision = "int8"
            cm_input = {
                    'action': 'run',
                    'automation': 'script',
                    'tags': f'generate-run-cmds,mlperf,inference,{var}',
                    'quiet': True,
                    'implementation': 'tflite-cpp',
                    'precision': precision,
                    'model': model,
                    'scenario': 'SingleStream',
                    'execution_mode': execution_mode,
                    'test_query_count': '50',
                    'adr': {
                        'tflite-model': {
                            'tags': v
                            },
                        'compiler': {
                            'tags': 'gcc'
                            },
                        'mlperf-inference-implementation': {
                            'tags': '_armnn,_use-neon'
                            }
                        }
                    }
            print(cm_input)
            r = cmind.access(cm_input)
            if r['return'] > 0:
                print(r)
                #exit(1)



