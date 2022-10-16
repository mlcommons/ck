import cmind
import os
import pathlib
current_file_path = pathlib.Path(__file__).parent.resolve()
docker_os = {
        "ubuntu": ["18.04","20.04","22.04"], 
        "rhel": ["9"] 
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
                "cpu": [ "python"] 
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
                for device in variations[model][backend]:
                    for lang in variations[model][backend][device]:
                        variation_string=",_"+model+",_"+backend+",_"+device+",_"+lang
                        file_name_ext = backend+"_"+device+"_"+lang
                        dockerfile_path = os.path.join(current_file_path,'dockerfiles', model, file_name_ext+ "_" + _os +'_'+version+'.Dockerfile')
                        r = cmind.access({'action': 'run', 
                            'automation': 'script', 
                            'tags': 'build,dockerfile', 
                            'docker_os': _os, 
                            'docker_os_version': version, 
                            'file_path': dockerfile_path,
                            'script_tags': 'app,mlperf,inference,reference'+variation_string,
                            'adr': {'compiler.tags': 'gcc'},
                            'real_run': True
                            })
                        if r['return'] > 0:
                            exit(1)
                        print("Dockerfile generated at "+dockerfile_path)


