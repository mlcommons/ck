# Author and developer: Grigori Fursin

from cmind import utils

import os
import platform
import sys
import struct

def run(i):

    ###################################################################
    # Prepare flow
    state = i['state']

    rt_cached = state['cmx'].get('detect_host_info_min', {})
    if len(rt_cached)>0: return rt_cached

    host_os = state['system']['os']

    cmind = i['cmind']
    misc = i['misc']

    out = misc.get('out', '')
    console = misc.get('console', False)

    self_meta = misc['meta']

    run_cmd = misc['helpers']['run_cmd']

    # Prepare inputs
    _input2 = i['input2']
    verbose = _input2.get('verbose', False)

    _input = i['input']

    env = _input2.get('env', {})

    # If on Windows
    #  * check that long file names are on
    #  * download and set up extra tools

    if os.name == 'nt':
        # Check if long paths are enabled
        r = cmind.x({'action':'run',
                     'automation':misc['flex.task'],
                     'control':{'out':''},
                     'verbose': verbose,
                     'tags':'use,long,paths,win'
                    })

        if r['return'] >0 : return r

        # Get min sys utils
        r = cmind.x({'action':'run',
                     'automation':misc['flex.task'],
                     'control':{'out':out},
                     'verbose': verbose,
                     'tags':'use,sys,tools,min,win'
                    })

        if r['return'] >0 : return r

        # Add to global paths
        path_to_bin = r['path_to_bin']

        paths = state['cmx']['envs']['+PATH']

        if path_to_bin not in paths:
            paths.append(path_to_bin)


    # Check various platform info
    pbits = 8 * struct.calcsize("P")

    obits = i.get('bits', '')
    if obits == '':
        obits = 32
        if os.name == 'nt':
            # Trying to get fast way to detect bits
            if os.environ.get('ProgramW6432', '') != '' or os.environ.get('ProgramFiles(x86)', '') != '':  # pragma: no cover
                obits = 64
        else:
            # On Linux use first getconf LONG_BIT and if doesn't work use python bits

            obits = pbits

            r = run_cmd(cmind, console, 'getconf LONG_BIT', env, None, capture_output = True, 
                        state = state, verbose = verbose)
            if r['return'] == 0:
                s = r['stdout'].strip()
                if len(s) > 0 and len(s) < 4:
                    try:
                        obits = int(s)
                    except:
                        pass

    host_os['python_bits'] = pbits
    host_os['bits'] = obits

    host_os['python_platform_architecture'] = platform.architecture()
    host_os['python_platform_machine'] = platform.machine()
    host_os['python_platform_node'] = platform.node()
    host_os['python_platform_system'] = platform.system()
    host_os['python_platform_release'] = platform.release()
    host_os['python_platform_version'] = platform.version()
    host_os['python_platform'] = platform.platform()
    host_os['python_platform_terse'] = platform.platform(terse = True)
    host_os['python_platform_aliased'] = platform.platform(aliased = True)
    host_os['python_platform_uname'] = platform.uname()
    host_os['python_os_name'] = os.name
    host_os['python_os_cpu_count'] = os.cpu_count()
    host_os['python_sys_platform'] = sys.platform
    host_os['python_platform_processor'] = platform.processor()

    # OS name
    uname = ''

    if os.name == 'nt':
        uname = 'windows'
    else:
        r = run_cmd(cmind, console, 'uname', env, None, capture_output = True, 
                    state = state, verbose = verbose)
        if r['return']>0: return r
        uname = r['stdout'].strip().lower()

    host_os['uname'] = uname

    # OS arch
    uarch = ''

    if os.name == 'nt':
        uarch = platform.machine().lower()
    else:
        # https://stackoverflow.com/questions/45125516/possible-values-for-uname-m

        r = run_cmd(cmind, console, 'uname -m', env, None, capture_output = True, 
                    state = state, verbose = verbose)
        if r['return']>0: return r
        uarch = r['stdout'].strip().lower()

        os_release = ''
        if os.path.isfile('/etc/os-release'):
            os_release_dict = {}
            try:
                with open("/etc/os-release") as f:
                   os_release_dict = dict(line.strip().split("=", 1) for line in f if "=" in line)
            except:
                pass

            host_os['release_name'] = f"{os_release_dict.get('PRETTY_NAME', 'Unknown')}".replace('"', '')

            kernel_version = os.uname().release

            host_os['release_name_with_kernel'] = f"{host_os['release_name']} ({kernel_version})"

    if uarch == 'x86_64': uarch = 'amd64'

    # May have armv6l, aarch64, riscv64 ...

    host_os['uarch'] = uarch

    # Finish automation
    rrr = {'return':0, 'host_os': host_os}

    state['cmx']['detect_host_info_min'] = rrr

    return rrr
