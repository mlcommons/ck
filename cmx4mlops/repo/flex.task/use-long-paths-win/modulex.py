# Author and developer: Grigori Fursin

from cmind import utils

import os
import copy

def run(i):

    ###################################################################
    # Prepare flow

    cmind = i['cmind']
    state = i['state']
    misc = i['misc']

    if os.name != 'nt':
        return {'return': 1, 'error': f"this task can run only on Windows: {misc['path']}"}

    console = misc.get('console', False)

    _input2 = i['input2']
    verbose = _input2.get('verbose', False)
    xinfo = 'INFO ' if verbose else ''

    # Check if long paths are enabled
    enabled = check_if_enabled()

    if not enabled:
        print (f'{xinfo}Windows long names are not enabled - trying to enable in admin mode!')

        run_cmd = misc['helpers']['run_cmd']

        # path to this script
        path = misc['path']
        path_to_script = os.path.join(path, 'update-reg.bat')

        cmd = f'powershell start {path_to_script} -v runas'

        run_cmd = misc['helpers']['run_cmd']

        r = run_cmd(cmind, console, cmd, {}, None, state = state, verbose = verbose)
        if r['return']>0: return r

        import time
        time.sleep(1)

        # Trying again
        enabled = check_if_enabled()

    if not enabled:
        return {'return':1, 'error': 'you may need to restart this Flex Task to check if long paths were enabled'}
    else:
        if console:
            print (f'{xinfo}Windows long paths are enabled!')

    return {'return':0, 'enabled': enabled}

###################################################################
def check_if_enabled():
    from importlib import reload
    import ctypes
    reload(ctypes)

    ntdll = ctypes.WinDLL('ntdll')

    enabled = False

    if hasattr(ntdll, 'RtlAreLongPathsEnabled'):
        ntdll.RtlAreLongPathsEnabled.restype = ctypes.c_ubyte
        ntdll.RtlAreLongPathsEnabled.argtypes = ()

        enabled = bool(ntdll.RtlAreLongPathsEnabled())

    return enabled
