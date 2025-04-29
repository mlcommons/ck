# Author and developer: Grigori Fursin

from cmind import utils
import os

def run(i):

    ###################################################################
    # Prepare flow

    cmind = i['cmind']

    misc = i['misc']
    run_cmd = misc['helpers']['run_cmd']

    state = i['state']
    tmp = i['tmp']

    cmx = state['cmx']

    out = misc.get('out', '')
    console = misc.get('console', False)

    self_meta = misc['meta']
    self_path = misc['path']

    ###################################################################
    # Prepare main input
    _input = i['input']

    # Check device (either from select-compute or forced)
    force_overwrite = _input.get('force_overwrite', False)
    gpu_metrics_devices = _input.get('gpu_metrics_devices', '')
    output = _input.get('output', '')

    target_device = state['cmx']['use_compute']['target_device']

    ###################################################################
    # Prepare cmd
    nsys_path = state['cmx']['sys_tool_nsys']['sys_tool_nsys_with_path2']

    nsys_cmd = nsys_path + ' profile'

    output_file = ''
    if output != '':
        output_file = output + '.nsys-rep'

    if force_overwrite:
        nsys_cmd += ' --force-overwrite=true'

        if output_file != '' and os.path.isfile(output_file):
            try:
                os.remove(output_file)
            except:
                pass

    if target_device == 'cuda':
        if gpu_metrics_devices:
            nsys_cmd += f' --gpu-metrics-devices={gpu_metrics_devices}'

    if output:
        nsys_cmd += f' --output={output}'

    return {'return':0, 'nsys_profile_cmd_prefix':nsys_cmd, 'nsys_profile_output_file':output_file}
