import cmind
import os
import pathlib
current_file_path = pathlib.Path(__file__).parent.resolve()
docker_os = {
        "ubuntu": ["18.04","20.04","22.04"],
        "rhel": ["9"]
    }
dataset = {
        "resnet50": "imagenet",
        "retinanet": "openimages",
        "bert-99.9": "squad"
        }
variations =  {
        "resnet50": {
            "tensorflow": {
                "cpu": [ "python" ]
            },
            "onnxruntime": {
                "cpu": [ "python", "cpp" ]
            },
            "pytorch": {
                "cpu": [ "python" ]
            }
        },
        "retinanet": {
            "tensorflow": {
            },
            "onnxruntime": {
                "cpu": [ "python", "cpp" ]
            },
            "pytorch": {
                "cpu": [ "python" ]
            }
        },
        "bert-99.9": {
            "tensorflow": {
                "cpu": []
            },
            "onnxruntime": {
                "cpu": [ "python" ]
            },
            "pytorch": {
                "cpu": []
            }
        }
    }

for _os in docker_os:
    for version in docker_os[_os]:
        for model in variations:
            for backend in variations[model]:
                comments = []
                comments.append("# Install/customize individual CM components for MLPerf")
                comments.append("#RUN cm run script --tags=get,generic-python-lib,_"+backend)
                comments.append("#RUN cm run script --tags=get-ml-model,"+model+",_"+backend)
                comments.append("#RUN cm run script --tags=get,dataset,preprocessed,"+dataset[model])
                comments.append("")
                comments.append("# Run CM workflow for MLPerf inference")
                for device in variations[model][backend]:
                    for lang in variations[model][backend][device]:
                        variation_string=",_"+model+",_"+backend+",_"+device+",_"+lang
                        file_name_ext = "_" + lang + "_" + backend+"_"+device
                        dockerfile_path = os.path.join(current_file_path,'dockerfiles', model, _os +'_'+version+ file_name_ext +'.Dockerfile')
                        r = cmind.access({'action': 'run', 
                            'automation': 'script', 
                            'tags': 'build,dockerfile', 
                            'docker_os': _os, 
                            'docker_os_version': version, 
                            'file_path': dockerfile_path,
                            'comments': comments,
                            'run_cmd': 'cm run script --tags=app,mlperf,inference,generic,reference'+variation_string+' --adr.compiler.tags=gcc',
                            'script_tags': 'app,mlperf,inference,generic,reference',
                            'real_run': True
                            })
                        if r['return'] > 0:
                            print(r)
                            exit(1)
                        print("Dockerfile generated at "+dockerfile_path)


