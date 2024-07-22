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
                "cpu": [ ]
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
                "cpu": [ "python" ]
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
                for device in variations[model][backend]:
                    for implementation in variations[model][backend][device]:
                        variation_string=",_"+model+",_"+backend+",_"+device+",_"+implementation
                        file_name_ext = "_" + implementation + "_" + backend+"_"+device
                        dockerfile_path = os.path.join(current_file_path,'dockerfiles', model, _os +'_'+version+ file_name_ext +'.Dockerfile')
                        cm_input = {'action': 'run', 
                            'automation': 'script',
                            'tags': 'app,mlperf,inference,generic'+variation_string,
                            'adr': {'compiler': 
                                      {'tags': 'gcc'},
                                    'inference-src': 
                                      {'tags': '_octoml'},
                                      'openimages-preprocessed':
                                      {'tags': '_50'}
                                    },
                            'print_deps': True,
                            'quiet': True,
                            'silent': True,
                            'fake_run': True
                            }
                        r = cmind.access(cm_input)
                        print_deps = r['new_state']['print_deps']
                        comments = [ "#RUN " + dep for dep in print_deps ]
                        comments.append("")
                        comments.append("# Run CM workflow for MLPerf inference")
                        cm_docker_input = {'action': 'run', 
                            'automation': 'script', 
                            'tags': 'build,dockerfile', 
                            'docker_os': _os, 
                            'docker_os_version': version, 
                            'file_path': dockerfile_path,
                            'comments': comments,
                            'run_cmd': 'cm run script --tags=app,mlperf,inference,generic'+variation_string+' --adr.compiler.tags=gcc --adr.inference-src.tags=_octoml',
                            'script_tags': 'app,mlperf,inference,generic',
                            'quiet': True,
                            'print_deps': True,
                            'real_run': True
                            }
                        r = cmind.access(cm_docker_input)
                        if r['return'] > 0:
                            print(r)
                            exit(1)

                        print ('')
                        print ("Dockerfile generated at " + dockerfile_path)

