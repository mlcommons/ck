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

    input_backends = env.get('BACKENDS')
    if input_backends:
        input_backends = input_backends.split(",")

    devices = env.get('DEVICES')
    if devices:
        devices = devices.split(",")

    implementation = env['IMPLEMENTATION']

    power = env.get('POWER', '')

    if str(power).lower() in [ "yes", "true" ]:
        POWER_STRING = " --power=yes --adr.mlperf-power-client.power_server=" + env.get('POWER_SERVER', '192.168.0.15') + " --adr.mlperf-power-client.port=" + str(env.get('POWER_SERVER_PORT', '4950')) + " "
    else:
        POWER_STRING = ""

    if not devices:
        return {'return': 1, 'error': 'No device specified. Please set one or more (comma separated) of {cpu, qaic, cuda, rocm} for --env.DEVICES=<>'}

    cmds = []
    run_script_content = '#!/bin/bash\n\n'
    run_script_content += "POWER_STRING=\"" +POWER_STRING +"\"\n"
    run_script_content += "DIVISION=\"" + env['DIVISION'] +"\"\n"
    run_script_content += "CATEGORY=\"" + env['CATEGORY'] +"\"\n"
    run_script_content += "EXTRA_ARGS=\"" + env.get('EXTRA_ARGS', '') +"\"\n"
    run_script_content += 'source '+ os.path.join(script_path, "run-template.sh") + "\nPOWER_STRING=\"" +POWER_STRING +"\"\n\n"

    run_file_name = 'tmp-'+implementation+'-run'

    for model in models:
        env['MODEL'] = model

        if "mobilenets" in model:
            cmd = 'export extra_option=""'
            cmds.append(cmd)
            cmd = 'export extra_tags=""'
            cmds.append(cmd)
            assemble_tflite_cmds(cmds)
            cmd = 'export extra_option=" --adr.mlperf-inference-implementation.compressed_dataset=on"'
            cmds.append(cmd)
            assemble_tflite_cmds(cmds)

            if env.get('CM_HOST_CPU_ARCHITECTURE', '') == "aarch64":
                extra_tags=",_armnn,_use-neon"
                cmd = f'export extra_tags="{extra_tags}"'
                cmds.append(cmd)
                assemble_tflite_cmds(cmds)
                cmd = 'export extra_option=" --adr.mlperf-inference-implementation.compressed_dataset=on"'
                cmds.append(cmd)
                assemble_tflite_cmds(cmds)

            continue

        if not input_backends:
            backends = None
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
            if not backends:
                return {'return': 1, 'error': f'No backend specified for the model: {model}.'}
            backends = backends.split(",")

        else:
            backends = input_backends

        for backend in backends:

            for device in devices:
                add_to_run_cmd = ''
                offline_target_qps = (((state.get(model, {})).get(device, {})).get(backend, {})).get('offline_target_qps')
                if offline_target_qps:
                    add_to_run_cmd += f" --offline_target_qps={offline_target_qps}"
                server_target_qps = (((state.get(model, {})).get(device, {})).get(backend, {})).get('server_target_qps')
                if server_target_qps:
                    add_to_run_cmd += f" --server_target_qps={server_target_qps}"

                else: #try to do a test run with reasonable number of samples to get and record the actual system performance
                    if device == "cpu":
                        if model == "resnet50":
                            test_query_count = 1000
                        else:
                            test_query_count = 100
                    else:
                        if model == "resnet50":
                            test_query_count = 40000
                        else:
                            test_query_count = 2000
                    cmd = f'run_test "{model}" "{backend}" "{test_query_count}" "{implementation}" "{device}" "$find_performance_cmd"'
                    cmds.append(cmd)
                    #second argument is unused for submission_cmd
                cmd = f'run_test "{model}" "{backend}" "100" "{implementation}" "{device}" "$submission_cmd" "{add_to_run_cmd}"'

                singlestream_target_latency = (((state.get(model, {})).get(device, {})).get(backend, {})).get('singlestream_target_latency')
                if singlestream_target_latency:
                    cmd += f" --singlestream_target_latency={singlestream_target_latency}"

                cmds.append(cmd)

    run_script_content += "\n\n" +"\n\n".join(cmds)

    with open(os.path.join(script_path, run_file_name+".sh"), 'w') as f:
        f.write(run_script_content)
    print(run_script_content)

    run_script_input = i['run_script_input']
    r = automation.run_native_script({'run_script_input':run_script_input, 'env':env, 'script_name':run_file_name})

    if r['return']>0: return r
    
    return {'return':0}

def assemble_tflite_cmds(cmds):
    cmd = 'run "$tflite_accuracy_cmd"'
    cmds.append(cmd)
    cmd = 'run "$tflite_performance_cmd"'
    cmds.append(cmd)
    cmd = 'run "$tflite_readme_cmd"'
    cmds.append(cmd)
    return

def postprocess(i):

    env = i['env']

    return {'return':0}
