from cmind import utils
import cmind as cm
import os
import shutil
import json

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    script_dir = i['run_script_input']['path']
    config_dir = os.path.join(script_dir, env.get('CM_TERRAFORM_CONFIG_DIR_NAME', ''))
    env['CM_TERRAFORM_CONFIG_DIR'] = config_dir
    cache_dir = os.getcwd()
    env['CM_TERRAFORM_RUN_DIR'] = cache_dir

    return {'return': 0}

def postprocess(i):
    env = i['env']
    state = i['state']
    with open("terraform.tfstate") as f:
        tfstate = json.load(f)
#    print(tfstate)
    resources = tfstate['resources']
    for resource in resources:
        if resource['type'] == 'aws_instance':
            aws_resource = resource
            break
    instances_state = aws_resource['instances']
    state['CM_TF_NEW_INSTANCES_STATE'] = []
    ssh_key_file = env.get('CM_SSH_KEY_FILE')
    user = 'ubuntu'
    for instance_state in instances_state:
        instance_attributes = instance_state['attributes']
        state['CM_TF_NEW_INSTANCES_STATE'].append(instance_attributes)
        public_ip = instance_attributes['public_ip']
        if env.get('CM_TERRAFORM_CM_INIT'):
            r = cm.access({
                'automation': 'script',
                'action': 'run',
                'tags': 'remote,run,ssh',
                'env': {
                    },
                'host': public_ip,
                'user': user,
                'skip_host_verify': True,
                'ssh_key_file': ssh_key_file,
                'quiet': True,
                'silent': True,
                'run_cmds': [
                    "sudo apt-get update",
                    "sudo apt-get install -y python3-pip",
                    "python3 -m pip install cmind",
                    "source ~/.profile",
                    "cm pull repo octoml@ck",
                    "cm run script --tags=get,sys-utils-cm"
                    ]
                })
            if r['return'] > 0:
                return r
            #print(r)
        print_attr(instance_attributes, "id")
        print_attr(instance_attributes, "instance_type")
        print_attr(instance_attributes, "public_ip")
        print_attr(instance_attributes, "public_dns")
        print_attr(instance_attributes, "security_groups")

    return {'return': 0}

def print_attr(instance_attributes, key):
    if key in instance_attributes:
        print(key.upper() + ": " + str(instance_attributes[key]))
