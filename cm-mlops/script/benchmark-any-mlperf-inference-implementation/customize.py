from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']
    state = i['state']
    meta = i['meta']
    script_path = i['run_script_input']['path']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    models = env['MODELS'].split(",")

    backends = env.get('BACKENDS')
    if backends:
        backends = backends.split(",")

    devices = env.get('DEVICES')
    if devices:
        devices = devices.split(",")

    print(backends)
    implementation = env['IMPLEMENTATION']

    power = env.get('POWER', '')

    if str(power).lower() in [ "yes", "true" ]:
        POWER_STRING = " --power yes --adr.mlperf-power-client.power_server=" + env.get('POWER_SERVER', '192.168.0.15') + " --adr.mlperf-power-client.port=" + env.get('POWER_SERVER_PORT', '4950') + " "
    else:
        POWER_STRING = ""

    if not devices:
        return {'return': 1, 'error': 'No device specified. Please set one or more (comma separated) of {cpu, qaic, cuda, rocm} for --env.DEVICES=<>'}

    for model in models:
        env['MODEL'] = model
        cmds = []
        run_script_content = '#!/bin/bash\nsource '+ os.path.join(script_path, "run-template.sh")

        if not backends:
            if implementation == "reference":
                if model == "resnet50":
                    backends = "tf,onnxruntime"
                elif model == "retinanet":
                    backends = "onnxruntime,pytorch"
                elif "bert" in model:
                    backends = "tf,onnxruntime,pytorch"
                elif "3d-unet" in model:
                    backends = "tf,onnxruntime,pytorch"
                elif model == "rnnt":
                    backends = "pytorch"
                elif "gptj" in model:
                    backends = "pytorch"
                elif "stable-diffusion-xl" in model:
                    backends = "pytorch"
                elif "llama2-70b" in model:
                    backends = "pytorch"
            backends = backends.split(",")

        for backend in backends:

            for device in devices:
                offline_target_qps = (((state.get(model, {})).get(device, {})).get(backend, {})).get('offline_target_qps')
                if offline_target_qps:
                    pass
                else: #try to do a test run with reasonable number of samples to get and record the actual system performance
                    if device == "cpu":
                        if model == "resnet50":
                            test_query_count = 1000
                        else:
                            test_query_count = 100
                    else:
                        if model == "resnet50":
                            test_query_count = 10000
                        else:
                            test_query_count = 1000
                    cmd = f'run_test "{backend}" "{test_query_count}" "{implementation}" "{device}" "$find_performance_cmd"'
                    cmds.append(cmd)
                    #second argument is unused for submission_cmd
                cmd = f'run_test "{backend}" "100" "{implementation}" "{device}" "$submission_cmd"'
                cmds.append(cmd)
                run_file_name = 'tmp-'+model+'-run'
                run_script_content += "\n\n" +"\n\n".join(cmds)
                with open(os.path.join(script_path, run_file_name+".sh"), 'w') as f:
                    f.write(run_script_content)
        print(cmds)




    
    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}
