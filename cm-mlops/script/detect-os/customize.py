from cmind import utils
import os
import subprocess

def preprocess(i):

    env = i['env']
    state = i['state']

    os_info = i['os_info']

    # Update env variables
    env['CM_HOST_OS_TYPE'] = os_info['platform']
    env['CM_HOST_OS_BITS'] = os_info['bits']
    env['CM_HOST_PYTHON_BITS'] = os_info['python_bits']

    # Update state (demo)
    # state['os_info'] = os_info

    return {'return':0}


def postprocess(i):

    env = i['env']
    state = i['state']

    os_info = i['os_info']

    if os_info['platform'] == 'windows':
        print ('Windows: TBD')

    else:
        if os_info['platform'] == 'linux':
            sys_cmd = "ld --verbose | grep SEARCH_DIR "
            result = subprocess.check_output(sys_cmd, shell=True).decode("utf-8")
            result = result.replace("SEARCH_DIR(\"=", "")
            result = result.replace("\")", "")
            result = result.replace(" ", "")
            result = result.replace("\n", "")
            dirs = result.split(';')
            lib_dir = []
            for _dir in dirs:
                if _dir != '' and  _dir not in lib_dir:
                    lib_dir.append(_dir)
            env['+CM_HOST_OS_DEFAULT_LIBRARY_DIR'] = ":".join(lib_dir)
            sys_cmd = "cpp -v /dev/null -o /dev/null 2>&1"
            result = subprocess.check_output(sys_cmd, shell=True).decode("utf-8")
            start = False
            inc_dir = []
            for out in result.split("\n"):
                if "> search starts here" not in out and not start:
                    continue
                if not start:
                    start = True
                    continue
                if "End of search list" in out:
                    break
                if 'gcc' not in out:
                    inc_dir.append(out.strip())
            env['+CM_HOST_OS_DEFAULT_INCLUDE_DIR'] = ":".join(inc_dir)
        r = utils.load_txt(file_name='tmp-run.out',
                           check_if_exists = True,
                           split = True)
        if r['return']>0: return r

        s = r['list']

        state['os_uname_machine'] = s[0]
        state['os_uname_all'] = s[1]

        env['CM_HOST_OS_MACHINE'] = state['os_uname_machine']

    return {'return':0}
