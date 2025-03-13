#
# Copyright: https://github.com/mlcommons/ck/blob/master/cm-mlops/COPYRIGHT.md
# License: https://github.com/mlcommons/ck/blob/master/cm-mlops/LICENSE.md
#
# White paper: https://arxiv.org/abs/2406.16791
# History: https://github.com/mlcommons/ck/blob/master/HISTORY.CM.md
# Original repository: https://github.com/mlcommons/ck/tree/master/cm-mlops
#
# CK and CM project contributors: https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md
#

from cmind import utils
import os
import subprocess


def escape_special_chars(text, tool=None):
    special_chars = [
        '&', '|', '(', ')'
    ]

    for char in special_chars:
        text = text.replace(char, f'^{char}')

    # handle URL special cases
    if tool != "rclone":
        text = text.replace('%', "%%")

    return text


def preprocess(i):

    os_info = i['os_info']
    env = i['env']

    # env to be passed to the  subprocess
    subprocess_env = os.environ.copy()
    subprocess_env['PATH'] += os.pathsep + \
        os.pathsep.join(env.get('+PATH', ''))

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    tool = env.get('CM_DOWNLOAD_TOOL', '')
    pre_clean = env.get('CM_PRE_DOWNLOAD_CLEAN', False)

    #    xsep = '^&^&' if windows else '&&'
    xsep = '&&'

    q = '"' if os_info['platform'] == 'windows' else "'"

    x = '*' if os_info['platform'] == 'windows' else ''
    x_c = '-s' if os_info['platform'] == 'darwin_off' else ''

    # command for deleting file in windows and linux is different
    if os_info['platform'] == 'windows':
        del_cmd = "del /f"
    else:
        del_cmd = "rm -f"

    if env.get('CM_DOWNLOAD_LOCAL_FILE_PATH'):
        filepath = env['CM_DOWNLOAD_LOCAL_FILE_PATH']

        if not os.path.exists(filepath):
            return {'return': 1,
                    'error': 'Local file {} doesn\'t exist'.format(filepath)}

        env['CM_DOWNLOAD_CMD'] = ""

        env['CM_DOWNLOAD_FILENAME'] = filepath

        if not quiet:
            print('')
            print('Using local file: {}'.format(filepath))
    else:
        url = env.get('CM_DOWNLOAD_URL', '')

        if url == '':
            return {
                'return': 1, 'error': 'please specify URL using --url={URL} or --env.CM_DOWNLOAD_URL={URL}'}

        print('')
        print('Downloading from {}'.format(url))

        if '&' in url and tool != "cmutil":
            if os_info['platform'] == 'windows':
                url = '"' + url + '"'
            else:
                url = url.replace('&', '\\&')

        extra_download_options = env.get('CM_DOWNLOAD_EXTRA_OPTIONS', '')

        verify_ssl = env.get('CM_VERIFY_SSL', "True")
        if str(verify_ssl).lower() in [
                "no", "false"] or os_info['platform'] == 'windows':
            verify_ssl = False
        else:
            verify_ssl = True

        if env.get('CM_DOWNLOAD_PATH', '') != '':
            download_path = env['CM_DOWNLOAD_PATH']
            if not os.path.exists(download_path):
                os.makedirs(download_path, exist_ok=True)
            os.chdir(download_path)

        if env.get('CM_DOWNLOAD_FILENAME', '') == '':
            urltail = os.path.basename(env['CM_DOWNLOAD_URL'])
            urlhead = os.path.dirname(env['CM_DOWNLOAD_URL'])
            if "." in urltail and "/" in urlhead:
                # Check if ? after filename
                j = urltail.find('?')
                if j > 0:
                    urltail = urltail[:j]
                env['CM_DOWNLOAD_FILENAME'] = urltail
            elif env.get('CM_DOWNLOAD_TOOL', '') == "rclone":
                env['CM_DOWNLOAD_FILENAME'] = urltail
            else:
                env['CM_DOWNLOAD_FILENAME'] = "index.html"

        if tool == "cmutil":
            cmutil_require_download = 0
            if env.get('CM_DOWNLOAD_CHECKSUM_FILE', '') != '':
                if os_info['platform'] == 'windows':
                    checksum_cmd = f"cd {q}{filepath}{q} {xsep}  md5sum -c{x_c} {x}{escape_special_chars(env['CM_DOWNLOAD_CHECKSUM_FILE'])}"
                else:
                    checksum_cmd = f"cd {q}{filepath}{q} {xsep}  md5sum -c{x_c} {x}{q}{env['CM_DOWNLOAD_CHECKSUM_FILE']}{q}"
                checksum_result = subprocess.run(
                    checksum_cmd,
                    cwd=f'{q}{filepath}{q}',
                    capture_output=True,
                    text=True,
                    shell=True,
                    env=subprocess_env)
            elif env.get('CM_DOWNLOAD_CHECKSUM', '') != '':
                if os_info['platform'] == 'windows':
                    checksum_cmd = f"echo {env.get('CM_DOWNLOAD_CHECKSUM')} {x}{escape_special_chars(env['CM_DOWNLOAD_FILENAME'])} | md5sum -c{x_c} -"
                else:
                    checksum_cmd = f"echo {env.get('CM_DOWNLOAD_CHECKSUM')} {x}{q}{env['CM_DOWNLOAD_FILENAME']}{q} | md5sum -c{x_c} -"
                checksum_result = subprocess.run(
                    checksum_cmd,
                    capture_output=True,
                    text=True,
                    shell=True,
                    env=subprocess_env)
            if env.get('CM_DOWNLOAD_CHECKSUM_FILE', '') != '' or env.get(
                    'CM_DOWNLOAD_CHECKSUM', '') != '':
                # print(checksum_result) #for debugging
                if "checksum did not match" in checksum_result.stderr.lower():
                    computed_checksum = subprocess.run(
                        f"md5sum {env['CM_DOWNLOAD_FILENAME']}",
                        capture_output=True,
                        text=True,
                        shell=True).stdout.split(" ")[0]
                    print(
                        f"WARNING: File already present, mismatch between original checksum({env.get('CM_DOWNLOAD_CHECKSUM')}) and computed checksum({computed_checksum}). Deleting the already present file and downloading new.")
                    try:
                        os.remove(env['CM_DOWNLOAD_FILENAME'])
                        print(
                            f"File {env['CM_DOWNLOAD_FILENAME']} deleted successfully.")
                    except PermissionError:
                        return {
                            "return": 1, "error": f"Permission denied to delete file {env['CM_DOWNLOAD_FILENAME']}."}
                    cmutil_require_download = 1
                elif "no such file" in checksum_result.stderr.lower():
                    # print(f"No file {env['CM_DOWNLOAD_FILENAME']}. Downloading through cmutil.")
                    cmutil_require_download = 1
                elif checksum_result.returncode > 0:
                    return {
                        "return": 1, "error": f"Error while checking checksum: {checksum_result.stderr}"}
                else:
                    print(
                        f"File {env['CM_DOWNLOAD_FILENAME']} already present, original checksum and computed checksum matches! Skipping Download..")
            else:
                cmutil_require_download = 1

            if cmutil_require_download == 1:
                cm = automation.cmind
                for i in range(1, 5):
                    r = cm.access({'action': 'download_file',
                                   'automation': 'utils,dc2743f8450541e3',
                                   'url': url,
                                   'verify': verify_ssl})
                    if r['return'] == 0:
                        break
                    oldurl = url
                    url = env.get('CM_DOWNLOAD_URL' + str(i), '')
                    if url == '':
                        break
                    print(f"Download from {oldurl} failed, trying from {url}")

                if r['return'] > 0:
                    return r

                env['CM_DOWNLOAD_CMD'] = ""
                env['CM_DOWNLOAD_FILENAME'] = r['filename']

        elif tool == "wget":
            if env.get('CM_DOWNLOAD_FILENAME', '') != '':
                extra_download_options += f" --tries=3 -O {q}{env['CM_DOWNLOAD_FILENAME']}{q} "
                if not verify_ssl:
                    extra_download_options += "--no-check-certificate "
            env['CM_DOWNLOAD_CMD'] = f"wget -nc {extra_download_options} {url}"
            for i in range(1, 5):
                url = env.get('CM_DOWNLOAD_URL' + str(i), '')
                if url == '':
                    break
                env['CM_DOWNLOAD_CMD'] += f" || (({del_cmd} {env['CM_DOWNLOAD_FILENAME']} || true) && wget -nc {extra_download_options} {url})"
            print(env['CM_DOWNLOAD_CMD'])

        elif tool == "curl":
            if env.get('CM_DOWNLOAD_FILENAME', '') != '':
                extra_download_options += f" --output {q}{env['CM_DOWNLOAD_FILENAME']}{q} "

            env['CM_DOWNLOAD_CMD'] = f"curl {extra_download_options} {url}"
            for i in range(1, 5):
                url = env.get('CM_DOWNLOAD_URL' + str(i), '')
                if url == '':
                    break
                env['CM_DOWNLOAD_CMD'] += f" || (({del_cmd} {env['CM_DOWNLOAD_FILENAME']} || true) && curl {extra_download_options} {url})"

        elif tool == "gdown":
            if not verify_ssl:
                extra_download_options += "--no-check-certificate "
            env['CM_DOWNLOAD_CMD'] = f"gdown {extra_download_options} {url}"
            for i in range(1, 5):
                url = env.get('CM_DOWNLOAD_URL' + str(i), '')
                if url == '':
                    break
                env['CM_DOWNLOAD_CMD'] += f" || (({del_cmd} {env['CM_DOWNLOAD_FILENAME']} || true) && gdown {extra_download_options} {url})"

        elif tool == "rclone":
            # keeping this for backward compatibility. Ideally should be done
            # via get,rclone-config script
            if env.get('CM_RCLONE_CONFIG_CMD', '') != '':
                env['CM_DOWNLOAD_CONFIG_CMD'] = env['CM_RCLONE_CONFIG_CMD']
            rclone_copy_using = env.get('CM_RCLONE_COPY_USING', 'sync')
            if rclone_copy_using == "sync":
                pre_clean = False
            if env["CM_HOST_OS_TYPE"] == "windows":
                # have to modify the variable from url to temp_url if it is
                # going to be used anywhere after this point
                url = url.replace("%", "%%")
                temp_download_file = env['CM_DOWNLOAD_FILENAME'].replace(
                    "%", "%%")
                env['CM_DOWNLOAD_CMD'] = f"rclone {rclone_copy_using} {q}{url}{q} {q}{os.path.join(os.getcwd(), temp_download_file)}{q} -P --error-on-no-transfer"
            else:
                env['CM_DOWNLOAD_CMD'] = f"rclone {rclone_copy_using} {q}{url}{q} {q}{os.path.join(os.getcwd(), env['CM_DOWNLOAD_FILENAME'])}{q} -P --error-on-no-transfer"

        filename = env['CM_DOWNLOAD_FILENAME']
        env['CM_DOWNLOAD_DOWNLOADED_FILENAME'] = filename

        filename = os.path.basename(env['CM_DOWNLOAD_FILENAME'])
        filepath = os.path.join(os.getcwd(), filename)

    env['CM_DOWNLOAD_DOWNLOADED_PATH'] = filepath

    # verify checksum if file already present
    if env.get('CM_DOWNLOAD_CHECKSUM_FILE', '') != '':
        env['CM_DOWNLOAD_CHECKSUM_CMD'] = f"cd {q}{filepath}{q} {xsep}  md5sum -c {x_c} {x}{q}{env['CM_DOWNLOAD_CHECKSUM_FILE']}{q}"
    elif env.get('CM_DOWNLOAD_CHECKSUM', '') != '':
        if os_info['platform'] == 'windows':
            env['CM_DOWNLOAD_CHECKSUM_CMD'] = "echo {} {}{} | md5sum {} -c -".format(
                env.get('CM_DOWNLOAD_CHECKSUM'), x, escape_special_chars(
                    env['CM_DOWNLOAD_FILENAME']), x_c)
        else:
            env['CM_DOWNLOAD_CHECKSUM_CMD'] = "echo {} {}{}{}{} | md5sum {} -c -".format(
                env.get('CM_DOWNLOAD_CHECKSUM'), x, q, env['CM_DOWNLOAD_FILENAME'], q, x_c)
        for i in range(1, 5):
            if env.get('CM_DOWNLOAD_CHECKSUM' + str(i), '') == '':
                break
            if os_info['platform'] == 'windows':
                env['CM_DOWNLOAD_CHECKSUM_CMD'] += " || echo {} {}{} | md5sum {} -c -".format(
                    env.get(
                        'CM_DOWNLOAD_CHECKSUM' +
                        str(i)),
                    x,
                    escape_special_chars(
                        env['CM_DOWNLOAD_FILENAME']),
                    x_c)
            else:
                env['CM_DOWNLOAD_CHECKSUM_CMD'] += " || echo {} {}{}{}{} | md5sum {} -c -".format(
                    env.get(
                        'CM_DOWNLOAD_CHECKSUM' +
                        str(i)),
                    x,
                    q,
                    env['CM_DOWNLOAD_FILENAME'].replace(
                        "%",
                        "%%"),
                    q,
                    x_c)
        # print(env['CM_DOWNLOAD_CHECKSUM_CMD'])
    else:
        env['CM_DOWNLOAD_CHECKSUM_CMD'] = ""

    if not pre_clean:
        env['CM_PRE_DOWNLOAD_CMD'] = ''

    if os_info['platform'] == 'windows' and env.get(
            'CM_DOWNLOAD_CMD', '') != '':
        env['CM_DOWNLOAD_CMD'] = escape_special_chars(
            env['CM_DOWNLOAD_CMD'], tool)
        if pre_clean:
            env['CM_PRE_DOWNLOAD_CLEAN_CMD'] = "del /Q %CM_DOWNLOAD_FILENAME%"
        # Check that if empty CMD, should add ""
        for x in ['CM_DOWNLOAD_CMD', 'CM_DOWNLOAD_CHECKSUM_CMD']:
            env[x + '_USED'] = 'YES' if env.get(x, '') != '' else 'NO'
    else:
        env['CM_PRE_DOWNLOAD_CLEAN_CMD'] = "rm -f {}".format(
            env['CM_DOWNLOAD_FILENAME'])

    return {'return': 0}


def postprocess(i):

    automation = i['automation']

    env = i['env']

    filepath = env['CM_DOWNLOAD_DOWNLOADED_PATH']

    if not os.path.exists(filepath):
        return {
            'return': 1, 'error': 'Downloaded path {} does not exist. Probably CM_DOWNLOAD_FILENAME is not set and CM_DOWNLOAD_URL given is not pointing to a file'.format(filepath)}

    if env.get('CM_DOWNLOAD_RENAME_FILE', '') != '':
        file_dir = os.path.dirname(filepath)
        new_file_name = env['CM_DOWNLOAD_RENAME_FILE']
        new_file_path = os.path.join(file_dir, new_file_name)
        os.rename(filepath, new_file_path)
        filepath = new_file_path

    if env.get('CM_DOWNLOAD_FINAL_ENV_NAME', '') != '':
        env[env['CM_DOWNLOAD_FINAL_ENV_NAME']] = filepath

    env['CM_GET_DEPENDENT_CACHED_PATH'] = filepath

    # Since may change directory, check if need to clean some temporal files
    automation.clean_some_tmp_files({'env': env})

    return {'return': 0}
