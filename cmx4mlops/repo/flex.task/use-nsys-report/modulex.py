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
    # Prepare aux input
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)

    # Prepare main input
    _input = i['input']

    # Check device (either from select-compute or forced)
    force_overwrite = _input.get('force_overwrite', False)
    force_export = _input.get('force_export', False)
    input_file = _input.get('input', '')
    output_file = _input.get('output', '')
    format_report = _input.get('format', '')

    ###################################################################
    # Prepare cmd
    nsys_path = state['cmx']['sys_tool_nsys']['sys_tool_nsys_with_path2']

    nsys_cmd = nsys_path + ' stats'

    if force_overwrite:
        nsys_cmd += ' --force-overwrite=true'

        if output_file != '' and os.path.isfile(output_file):
            try:
                os.remove(output_file)
            except:
                pass

    if force_export:
        nsys_cmd += ' --force-export=true'

        if output_file != '' and os.path.isfile(output_file):
            try:
                os.remove(output_file)
            except:
                pass

    if format_report != '':
        nsys_cmd += f' --format={format_report}'

    if output_file != '':
        nsys_cmd += f' --output={output_file}'

    if input_file != '':
        nsys_cmd += f' {input_file}'

    r = run_cmd(cmind, console, nsys_cmd, {}, None, state = state, verbose = verbose, capture_output = False, print_cmd = True)
    if r['return']>0: return cmind.embed_error(r)

    return {'return':0, 'nsys_report_cmd_prefix':nsys_cmd, 'nsys_report_output_file':output_file}
