import cmind
import os
import pathlib
current_file_path = pathlib.Path(__file__).parent.resolve()
docker_os = {'ubuntu': ["18.04","20.04","22.04"], 'rhel': ["9"] }
for _os in docker_os:
    for version in docker_os[_os]:
        dockerfile_path = os.path.join(current_file_path,'dockerfiles', _os +'_'+version+'.Dockerfile')
        r = cmind.access({'action': 'run', 'automation': 'script', 'tags': 'build,dockerfile', 'docker_os': _os, 'docker_os_version': version, 'file_path': dockerfile_path})
        if r['return'] > 0:
            exit(1)
        print("Dockerfile generated at "+dockerfile_path)


