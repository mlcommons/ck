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

    if os_info['platform'] != 'windows':
        if os_info['platform'] == 'linux':
            sys_cmd = "ld --verbose | grep SEARCH_DIR "
            result = subprocess.check_output(sys_cmd, shell=True).decode("utf-8")
            result = result.replace("SEARCH_DIR(\"=", "")
            result = result.replace("SEARCH_DIR(\"", "")
            result = result.replace("\")", "")
            result = result.replace(" ", "")
            result = result.replace("\n", "")
            dirs = result.split(';')
            lib_dir = []
            for _dir in dirs:
                if _dir != '' and  _dir not in lib_dir:
                    lib_dir.append(_dir)
            env['+CM_HOST_OS_DEFAULT_LIBRARY_PATH'] = lib_dir

        r = utils.load_txt(file_name='tmp-run.out',
                           check_if_exists = True,
                           split = True)
        if r['return']>0: return r

        s = r['list']

        state['os_uname_machine'] = s[0]
        state['os_uname_all'] = s[1]

        env['CM_HOST_OS_MACHINE'] = state['os_uname_machine']
    import platform
    env['CM_HOST_SYSTEM_NAME'] = platform.node()
    if 'CM_HOST_OS_PACKAGE_MANAGER' not in env:
        if env.get('CM_HOST_OS_FLAVOR','') == "ubuntu" or env.get('CM_HOST_OS_FLAVOR_LIKE','') == "debian":
            env['CM_HOST_OS_PACKAGE_MANAGER'] = "apt"
        if env.get('CM_HOST_OS_FLAVOR','') == "rhel":
            env['CM_HOST_OS_PACKAGE_MANAGER'] = "dnf"
        if env.get('CM_HOST_OS_FLAVOR_LIKE','') == "arch":
            env['CM_HOST_OS_PACKAGE_MANAGER'] = "arch"
        if env.get('CM_HOST_OS_FLAVOR','') == "macos":
            env['CM_HOST_OS_PACKAGE_MANAGER'] = "brew"
    if env.get('CM_HOST_OS_PACKAGE_MANAGER', '') == "apt":
        env['CM_HOST_OS_PACKAGE_MANAGER_INSTALL_CMD'] = "apt-get install -y"
        env['CM_HOST_OS_PACKAGE_MANAGER_UPDATE_CMD'] = "apt-get update -y"
    elif env.get('CM_HOST_OS_PACKAGE_MANAGER', '') == "dnf":
        env['CM_HOST_OS_PACKAGE_MANAGER_INSTALL_CMD'] = "dnf install -y"
        env['CM_HOST_OS_PACKAGE_MANAGER_UPDATE_CMD'] = "dnf update -y"
    elif env.get('CM_HOST_OS_PACKAGE_MANAGER', '') == "pacman":
        env['CM_HOST_OS_PACKAGE_MANAGER_INSTALL_CMD'] = "pacman -Sy --noconfirm"
        env['CM_HOST_OS_PACKAGE_MANAGER_UPDATE_CMD'] = "pacman -Syu"
    elif env.get('CM_HOST_OS_PACKAGE_MANAGER', '') == "brew":
        env['CM_HOST_OS_PACKAGE_MANAGER_INSTALL_CMD'] = "brew install"
        env['CM_HOST_OS_PACKAGE_MANAGER_UPDATE_CMD'] = "brew update"

    return {'return':0}
