# Author and developer: Grigori Fursin

import os

from cmind.automation import Automation
from cmind import utils

class CAutomation(Automation):
    """
    Automation actions
    """

    ############################################################
    def __init__(self, cmind, automation_file):
        super().__init__(cmind, __file__)

    ############################################################
    def test(self, i):
        """
        Test automation

        Args:
          i (dict): CM input dict

             action (str): CM action
             automation (str): CM automation
             artifact (str): CM artifact
             artifacts (list): list of extra CM artifacts

             control: (dict): various CM control
              (out) (str): if 'con', output to console
              ...

             (flags)
          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          * Output from this automation action

        """

        # Access CM
        print (self.cmind)

        # Print self path
        print (self.path)

        # Print self meta
        print (self.meta)

        # Print self automation module path
        print (self.automation_file_path)

        # Print self automation module path
        print (self.full_path)

        # Print self artifact
        print (self.artifact)

        # Print input

        import json
        print (json.dumps(i, indent=2))

        return {'return':0}

    ############################################################
    def select_artifact(self, i):
        """
        Select CMX artifact


        TBD

        (selected_uid) (str): if this UID for sub_meta


        """

        import copy

        _input = i['control'].get('_input', {})

        console = i['control'].get('out', '') == 'con'

        selected_text = _input.pop('selected_text', '')
        selected_automation = _input.pop('selected_automation', '')
        selected_artifact = _input.pop('selected_artifact', '')
        selected_tags = _input.pop('selected_tags', '')
        selected_uid = _input.pop('selected_uid', '')
        sub_meta = _input.pop('sub_meta', False)
        selected_choices = _input.pop('selected_choices', {})
        quiet = _input.pop('quiet', False)
        create_if_not_found = _input.pop('create_if_not_found', False)
        create_meta = _input.pop('create_meta', {})
        show_tags = _input.pop('show_tags', False)

        r = utils.test_input(_input)
        if r['return']>0: return self.cmind.embed_error(r)

        # Search CM artifact
        ii = {'automation': selected_automation,
              'action': 'find'}

        if selected_artifact != '': 
            ii['artifact'] = selected_artifact

        if selected_tags != '':
            ii['tags'] = selected_tags

        import copy
        iii = copy.deepcopy(ii)

        r = self.cmind.x(ii)
        if r['return'] > 0: return r

        # Do extra filtering
        lst = []

        for l in r['list']:
            if not l.meta.get('skip', False):
                metas = []

                if sub_meta:
                    files = [f for f in os.listdir(l.path) if f.startswith('_cm_')]

                    for f in files:
                        fpath = os.path.join(l.path, f) 
                        r = utils.load_json_or_yaml(fpath)
                        if r['return'] == 0:
                            meta = r['meta']
                            meta['sub_file'] = fpath
                            metas.append(meta)
                else:
                    metas.append(l.meta)

                metas2 = []

                for meta in metas:
                    if selected_uid!='' and meta.get('uid', '') != selected_uid:
                        continue

                    add = True
                    for k in selected_choices:
                        if k in meta.get('choices', {}):
                            if selected_choices[k] not in meta['choices'][k]:
                                add = False
                                break
                    if add:
                        metas2.append(meta)

                for meta in metas2:
#                    ll = copy.deepcopy(l)
#                    ll.meta.update(meta)
#                    lst.append(ll)
                    l.meta.update(meta)
                    lst.append(l)

        new_index_int = 0

        if len(lst) == 0:
            if create_if_not_found:
                iii['action'] = 'add'
                if len(create_meta) > 0:
                    iii['meta'] = create_meta

                r = self.cmind.x(iii)
                if r['return'] >0 : return r

                uid = r['meta']['uid']

                r = self.cmind.x({'action': 'find',
                                  'automation': selected_automation,
                                  'artifact': uid})
                if r['return'] >0: return r

                lst = r['list']

            else:
                xtags = '' if selected_tags == '' else f' with tags "{selected_tags}"'
                return {'return':16, 'error': f'artifact(s) not found for the "{selected_automation}" automation{xtags}'}

        if len(lst) == 1:
            new_index_int = 0

        # Continue processing artifacts
        if len(lst) > 1:

            if selected_text == '':
                selected_text = 'Select artifact'

            selected_text += ':'

            if console:
                print ('')
                print (selected_text)
                print ('')

            index = 0

            lst = sorted(lst, key = lambda x: (x.meta.get('sort', 0),
                                               x.meta.get('name', ''),
                                               x.meta['alias']))

            for a in lst:
                meta = a.meta
                path = a.path

                name = meta.get('name', '')
                alias = meta['alias']
                uid = meta['uid']

                x = name if name != '' else alias

                xtags = '[' + ','.join(meta['tags']) + '] ' if show_tags else ''

                text = f'{index}) {x} {xtags}({uid})'

                if console:
                    print (text)

                index += 1

            if quiet:
                if console:
                    print ('')
                    print ('Quietly selected 0')
                new_index = 0

            else:
                print ('')

                new_index = input('Make your selection or press Enter for 0: ').strip()

                new_index_int = 0 if new_index == '' else int(new_index)

                if new_index_int < 0 or new_index_int >= index:
                    return {'return':1, 'error': 'selection out of range'}
 
        artifact = lst[new_index_int]

        return {'return':0, 
                'list': lst, 
                'selected_artifact_object': artifact,
                'index':new_index_int}

    ############################################################
    def get_date_time(self, i):
        """
        Get date and time as string
        """
        # Check input
        console = i['control'].get('out', '') == 'con'

        _input = i['control'].get('_input', {})

        r = utils.test_input(_input)
        if r['return']>0: return self.cmind.embed_error(r)

        r = utils.get_current_date_time({})
        if r['return']>0: return r

        iso_datetime = r['iso_datetime']

        s = iso_datetime

        j = s.rfind('.')
        if j>0: s = s[:j]

        s = s.replace(':','-')

        s1 = s

        s = s.replace('T','.')

        j = s1.find('T')
        if j>0:
            s1 = s1[:j]

        return {'return':0, 'date_time_str': s, 'date_str':s1, 'iso_datetime':iso_datetime}

    ############################################################
    def cmd(self, i):
        """
        Run CMD with environment

        Input:
          i (dict): unified CM input
            * (envs) (dict): 1st level of env to update global ENV
            * (env) (dict): 2nd (current) env to update global ENV
            * (genv) (dict): global ENV (force in the end)
            * (cmd) (str)
            * (capture_output) (bool): False by default
            * (timeout) (int): None by default
                               TBD: Current timeout doesn't terminate subprocesses
                               need to use POpen.
            * (verbose) (bool): if True, print extra info
            * (hide_in_cmd) (list): list keys in CMD to hide (for secrets)
            * (save_script) (str): save script for reproducibility
            * (run_script) (bool): run create script (useful for pipes)
            * (script_prefix) (str): add prefix string to script
            * (skip_run) (bool): if True, skip run
            * (print_cmd) (bool): if True, force print CMD

        Output:
          r (dict): unified CM output
            * return (int): 0 if success
            * (error) (str): error string if return > 0


        """

        import subprocess

        _input = i['control'].get('_input', {})

        console = i['control'].get('out', '') == 'con'

        env = _input.pop('env', {})
        envs = _input.pop('envs', {})
        genv = _input.pop('genv', {})
        cmd = _input.pop('cmd', '')
        print_cmd = _input.pop('print_cmd', False)
        capture_output = _input.pop('capture_output', False)

        verbose = _input.pop('verbose', False)

        hide_in_cmd = _input.pop('hide_in_cmd', [])

        timeout = _input.pop('timeout', None)
        # Just in case, check if input comes from CMD
        if timeout != None: timeout = int(timeout) 

        save_script = _input.pop('save_script', '')
        run_script = _input.pop('run_script', False)

        if run_script:
            if save_script == '': save_script = 'cmx-rt-run.sh'

        skip_run = _input.pop('skip_run', False)
        script_prefix = _input.pop('script_prefix', '')

        r = utils.test_input(_input)
        if r['return']>0: return self.cmind.embed_error(r)

#        if os.name == 'nt':
#            It allows lower letter that is difficult to update with all capital letters
#            import nt
#            cur_env = nt.environ.copy()
#        else:
        cur_env = os.environ.copy()

        print_env = {}

        for e in [envs, env, genv]:
            for k in e:
                v = e[k]

                if type(v) == list:
                    v = os.pathsep.join(v)
                elif v != None :
                    v = str(v)

                if k.startswith('+'):
                    if v != '':
                        k = k[1:].strip()
                        v1 = cur_env.get(k, '')
                        if v1 != '':
                            v += os.pathsep + v1
                    else:
                       v = None

                if v != None:
                    cur_env[k] = v

                    if console:
                        print_env[k] = v

        if save_script != '':
            script = '@echo off\n' if os.name == 'nt' else '#!/bin/bash\n'

            if script_prefix != '':
                script += '\n' + script_prefix

        if len(print_env)>0:
            if verbose:
                print ('')

            if save_script != '':
                script += '\n'

            for k in print_env:
                v = print_env[k]

                if verbose:
                    print (f'ENV {k}={v}')

                if save_script != '':
                    x = 'set' if os.name == 'nt' else 'export'
                    vv = v if ' ' not in v else '"' + v + '"'
                    script += f'{x} {k}={vv}\n'

            if save_script != '':
                script += '\n'

        returncode = 0
        stdout = ''
        stderr = ''

        # Hide secrets from CMD
        xcmd = cmd

        for h in hide_in_cmd:
            j = xcmd.find(h)
            if j >= 0:
                j1 = xcmd.find(' ', j + len(h))
                if j1<0: j1 = len(xcmd)
                if j1>=0:
                    xcmd = xcmd[:j+len(h)] + '***' + xcmd[j1:]

        if verbose or print_cmd:
            print ('')

            if skip_run:
                print (f'SKIP CMD {xcmd}')
            else:
                print (f'CMD {xcmd}')


        if save_script != '':
            script += cmd + '\n'

            r = utils.save_txt(save_script, script)
            if r['return']>0: return r

        if run_script:
            if os.name == 'nt':
                cmd = f'call {save_script}'
            else:
                x = '' if save_script.startswith('.') or save_script.startswith('/') else '. ./'
                cmd = f'bash -c "{x}{save_script}"'

            if verbose:
                x = 'SKIP ' if skip_run else ''
                print('')
                print(f'{x}RUN {cmd}')

        if not skip_run:

            try:
                # TBD: note that this code doesn't kill subprocesses
                # after timeout - must improve with POpen...
                result = subprocess.run(cmd,
                                        capture_output = capture_output,
                                        text = True,
                                        shell = True,
                                        env = cur_env,
                                        timeout = timeout)

            except Exception as e:
                stdout = ''
                stderr = format(e)
                returncode = -1

            else:
                returncode = result.returncode
                stdout = result.stdout
                stderr = result.stderr

        return {'return':0, 'returncode': returncode, 'stdout': stdout, 'stderr': stderr}

    ############################################################
    def get_dir_size(self, i):
        """
        Get directory size

        Input:
          i (dict): unified CM input
            * (path) (str)

        Output:
          r (dict): unified CM output
            * return (int): 0 if success
            * (error) (str): error string if return > 0

            * dir_size (int): size in bytes

        """

        import os

        start_dir = i['path']

        total_size = 0
        for dir_path, dir_names, file_names in os.walk(start_dir):
            for fn in file_names:
                fp = os.path.join(dir_path, fn)
                total_size += os.path.getsize(fp)

        return {'return':0, 'dir_size': total_size}

    ##############################################################################
    def get_host_os_info(self, i):
        """
        Get some host platform name (currently windows or linux) and OS bits

        Args:    
           (CM input dict):

           (bits) (str): force host platform bits

        Returns:
           (CM return dict):

           * return (int): return code == 0 if no error and >0 if error
           * (error) (str): error string if return>0

           * info (dict):
             * platform (str): "windows", "linux" or "darwin"
             * bat_ext (str): ".bat" or ".sh"
             * bits (str): 32 or 64 bits
             * python_bits 9str): python bits

        """

        import os
        import platform
        import struct

        info = {}

        pbits = str(8 * struct.calcsize("P"))

        if platform.system().lower().startswith('win'):
            platform = 'windows'
            info['bat_ext']='.bat'
            info['set_env']='set ${key}=${value}'
            info['env_separator']=';'
            info['env_var']='%env_var%'
            info['bat_rem']='rem ${rem}'
            info['run_local_bat']='call ${bat_file}'
            info['run_local_bat_from_python']='call ${bat_file}'
            info['run_bat']='call ${bat_file}'
            info['start_script']=['@echo off', '']
            info['env']={
              "CM_WINDOWS":"yes"
            }
        else:
            if platform.system().lower().startswith('darwin'):
                platform = 'darwin'
            else:
                platform = 'linux'

            info['bat_ext']='.sh'
            info['set_env']='export ${key}="${value}"'
            info['env_separator']=':'
            info['env_var']='${env_var}'
            info['set_exec_file']='chmod 755 "${file_name}"'
            info['bat_rem']='# ${rem}'
            info['run_local_bat']='. ./${bat_file}'
            info['run_local_bat_from_python']='bash -c ". ./${bat_file}"'
            info['run_bat']='. ${bat_file}'
            info['start_script']=['#!/bin/bash', '']
            info['env']={}

        info['platform'] = platform

        obits = i.get('bits', '')
        if obits == '':
            obits = '32'
            if platform == 'windows':
                # Trying to get fast way to detect bits
                if os.environ.get('ProgramW6432', '') != '' or os.environ.get('ProgramFiles(x86)', '') != '':  # pragma: no cover
                    obits = '64'
            else:
                # On Linux use first getconf LONG_BIT and if doesn't work use python bits

                obits = pbits

                r = utils.gen_tmp_file({})
                if r['return'] > 0:
                    return r

                fn = r['file_name']

                cmd = 'getconf LONG_BIT > '+fn
                rx = os.system(cmd)

                if rx == 0:
                    r = utils.load_txt(file_name = fn, remove_after_read = True)

                    if r['return'] == 0:
                        s = r['string'].strip()
                        if len(s) > 0 and len(s) < 4:
                            obits = s
                else:
                    if os.path.isfile(fn): os.remove(fn)

        info['bits'] = obits
        info['python_bits'] = pbits

        return {'return': 0, 'info': info}

    ##############################################################################
    def download_file(self, i):
        """
        Download file using requests

        Args:
           (CM input dict):

           url (str): URL with file
           (filename) (str): explicit file name
           (path) (str): path to record file (or current if empty)
           (chunk_size) (int): chunck size in bytes (65536 by default)
           (text) (str): print text before downloaded status ("Downloaded: " by default)
           (verify) (bool): verify SSL certificate if True (True by default)
                            can be switched by global env CM_UTILS_DOWNLOAD_VERIFY_SSL = no
           (verbose) (bool): print extra info

        Returns:
           (CM return dict):

           * return (int): return code == 0 if no error and >0 if error
           * (error) (str): error string if return>0

           * filename (str): file name
           * path (str): path to file
           * size (int): file size

        """

        import requests
        import time
        import sys
        from urllib import parse

        console = i['control'].get('out') == 'con'

        verbose = i.get('verbose', False)

        # Get URL
        url = i['url']

        # Check file name
        file_name = i.get('filename','')
        if file_name == '':
            parsed_url = parse.urlparse(url)
            file_name = os.path.basename(parsed_url.path)

        # Check path
        path = i.get('path','')
        if path is None or path=='':
            path = os.getcwd()

        # Output file
        path_to_file = os.path.join(path, file_name)

        if os.path.isfile(path_to_file):
            os.remove(path_to_file)

        if console:
            x = 'RUN ' if verbose else ''
            print ('')
            print (f'{x}Downloading file from "{url}" to "{path_to_file}" using internal CMX function ...')
            print ('')

        # Download
        size = -1
        downloaded = 0
        chunk_size = i.get('chunk_size', 65536)

        text = i.get('text','Downloaded: ')

        if 'CM_UTILS_DOWNLOAD_VERIFY_SSL' in os.environ:
            verify = os.environ['CM_UTILS_DOWNLOAD_VERIFY_SSL'] == 'yes'
        else:
            verify = i.get('verify', True)

        try:
            with requests.get(url, stream=True, allow_redirects=True, verify=verify) as download:
                download.raise_for_status()

                size_string = download.headers.get('Content-Length')

                if size_string is None:
                    transfer_encoding = download.headers.get('Transfer-Encoding', '')
                    if transfer_encoding != 'chunked':
                        return {'return':1, 'error':'did not receive file'}
                    else:
                        size_string = "0"

                size = int(size_string)

                with open(path_to_file, 'wb') as output:
                    for chunk in download.iter_content(chunk_size = chunk_size):

                        if chunk:
                            output.write(chunk)
                        if size == 0:
                            continue
                        downloaded+=1
                        percent = downloaded * chunk_size * 100 / size

                        if console:
                            sys.stdout.write("\r{}{:3.0f}%".format(text, percent))
                            sys.stdout.flush()

                    if console:
                        sys.stdout.write("\r{}{:3.0f}%".format(text, 100))
                        sys.stdout.flush()

        except Exception as e:
            return {'return':1, 'error':format(e)}

        print ('')
        if size == 0:
            file_stats=os.stat(path_to_file)
            size = file_stats.st_size

        return {'return': 0, 'filename':file_name, 'path': path_to_file, 'size':size}

    ##############################################################################
    def unzip_file(self, i):
        """
        Unzip file

        Args:    
           (CM input dict):

           filename (str): explicit file name
           (path) (str): path where to unzip file (current path otherwise)
           (strip_folders) (int): strip first folders

        Returns:
           (CM return dict):

           * return (int): return code == 0 if no error and >0 if error
           * (error) (str): error string if return>0

        """

        import zipfile

        # Check file name
        file_name = i['filename']

        if not os.path.isfile(file_name):
            return {'return':1, 'error':'file {} not found'.format(file_name)}

        console = i['control'].get('out') == 'con'

        # Attempt to read cmr.json 
        file_name_handle = open(file_name, 'rb')
        file_name_zip = zipfile.ZipFile(file_name_handle)

        info_files=file_name_zip.infolist()

        path=i.get('path','')
        if path is None or path=='':
            path=os.getcwd()

        strip_folders = i.get('strip_folders',0)

        # Unpacking zip
        for info in info_files:
            f = info.filename
            permissions = info.external_attr

            if not f.startswith('..') and not f.startswith('/') and not f.startswith('\\'):
                f_zip = f

                if strip_folders>0:
                    fsplit = f.split('/') # Zip standard on all OS
                    f = '/'.join(fsplit[strip_folders:])

                if f != '':
                    file_path = os.path.join(path, f)

                    if f.endswith('/'):
                        # create directory
                        if not os.path.exists(file_path):
                            os.makedirs(file_path)
                    else:
                        dir_name = os.path.dirname(file_path)
                        if not os.path.exists(dir_name):
                            os.makedirs(dir_name)

                        # extract file
                        file_out = open(file_path, 'wb')
                        file_out.write(file_name_zip.read(f_zip))
                        file_out.close()

                        if permissions > 0xffff:
                            os.chmod(file_path, permissions >> 16)

        file_name_zip.close()
        file_name_handle.close()

        return {'return':0}

    ##############################################################################
    def compare_versions(self, i):
        """
        Compare versions

        Args:    

           version1 (str): version 1
           version2 (str): version 2

        Returns:
           (CM return dict):

           * comparison (int):  1 - version 1 > version 2
                                0 - version 1 == version 2
                               -1 - version 1 < version 2

           * return (int): return code == 0 if no error and >0 if error
           * (error) (str): error string if return>0
        """

        version1 = i['version1']
        version2 = i['version2']

        l_version1 = version1.split('.')
        l_version2 = version2.split('.')

        # 3.9.6 vs 3.9
        # 3.9 vs 3.9.6

        i_version1 = [int(v) if v.isdigit() else v for v in l_version1]
        i_version2 = [int(v) if v.isdigit() else v for v in l_version2]

        comparison = 0

        for index in range(max(len(i_version1), len(i_version2))):
            v1 = i_version1[index] if index < len(i_version1) else 0
            v2 = i_version2[index] if index < len(i_version2) else 0

            if v1 > v2:
                comparison = 1
                break
            elif v1 < v2:
                comparison = -1
                break

        return {'return':0, 'comparison': comparison}

    ##############################################################################
    def json2yaml(self, i):
        """
        Convert JSON file to YAML

        Args:    

           input (str): input file (.json)
           (output) (str): output file (.yaml)

        Returns:
           (CM return dict):

           * return (int): return code == 0 if no error and >0 if error
           * (error) (str): error string if return>0
        """

        input_file = i.get('input','')

        if input_file == '':
            return {'return':1, 'error':'please specify --input={json file}'}

        output_file = i.get('output','')

        r = utils.load_json(input_file, check_if_exists = True)
        if r['return']>0: return r

        meta = r['meta']

        if output_file=='':
            output_file = input_file[:-5] if input_file.endswith('.json') else input_file
            output_file+='.yaml'

        r = utils.save_yaml(output_file, meta)
        if r['return']>0: return r

        return {'return':0}

    ##############################################################################
    def yaml2json(self, i):
        """
        Convert YAML file to JSON

        Args:    

           input (str): input file (.yaml)
           (output) (str): output file (.json)

        Returns:
           (CM return dict):

           * return (int): return code == 0 if no error and >0 if error
           * (error) (str): error string if return>0
        """

        input_file = i.get('input','')

        if input_file == '':
            return {'return':1, 'error':'please specify --input={yaml file}'}

        output_file = i.get('output','')

        r = utils.load_yaml(input_file, check_if_exists = True)
        if r['return']>0: return r

        meta = r['meta']

        if output_file=='':
            output_file = input_file[:-5] if input_file.endswith('.yaml') else input_file
            output_file+='.json'

        r = utils.save_json(output_file, meta)
        if r['return']>0: return r

        return {'return':0}

    ##############################################################################
    def sort_json(self, i):
        """
        Sort JSON file

        Args:    

           input (str): input file (.json)
           (output) (str): output file

        Returns:
           (CM return dict):

           * return (int): return code == 0 if no error and >0 if error
           * (error) (str): error string if return>0
        """

        input_file = i.get('input','')

        if input_file == '':
            return {'return':1, 'error':'please specify --input={json file}'}

        r = utils.load_json(input_file, check_if_exists = True)
        if r['return']>0: return r

        meta = r['meta']

        output_file = i.get('output','')

        if output_file=='':
            output_file = input_file

        r = utils.save_json(output_file, meta, sort_keys=True)
        if r['return']>0: return r

        return {'return':0}

    ##############################################################################
    def dos2unix(self, i):
        """
        Convert DOS file to UNIX (remove \r)

        Args:    

           input (str): input file (.txt)
           (output) (str): output file

        Returns:
           (CM return dict):

           * return (int): return code == 0 if no error and >0 if error
           * (error) (str): error string if return>0
        """

        input_file = i.get('input','')

        if input_file == '':
            return {'return':1, 'error':'please specify --input={txt file}'}

        r = utils.load_txt(input_file, check_if_exists = True)
        if r['return']>0: return r

        s = r['string'].replace('\r','')

        output_file = i.get('output','')

        if output_file=='':
            output_file = input_file

        r = utils.save_txt(output_file, s)
        if r['return']>0: return r

        return {'return':0}

    ##############################################################################
    def replace_string_in_file(self, i):
        """
        Convert DOS file to UNIX (remove \r)

        Args:    

           input (str): input file (.txt)
           (output) (str): output file
           string (str): string to replace
           replacement (str): replacement string

        Returns:
           (CM return dict):

           * return (int): return code == 0 if no error and >0 if error
           * (error) (str): error string if return>0

           (update) (bool): True if file was upated
        """

        input_file = i.get('input', '')
        if input_file == '':
            return {'return':1, 'error':'please specify --input={txt file}'}
        
        string = i.get('string', '')
        if string == '':
            return {'return':1, 'error':'please specify --string={string to replace}'}

        replacement = i.get('replacement', '')
        if replacement == '':
            return {'return':1, 'error':'please specify --replacement={string to replace}'}
        
        output_file = i.get('output','')

        if output_file=='':
            output_file = input_file
        
        r = utils.load_txt(input_file, check_if_exists = True)
        if r['return']>0: return r

        s = r['string'].replace('\r','')

        s = s.replace(string, replacement)

        r = utils.save_txt(output_file, s)
        if r['return']>0: return r

        return {'return':0}

    ##############################################################################
    def create_toc_from_md(self, i):
        """
        Convert DOS file to UNIX (remove \r)

        Args:    

           input (str): input file (.md)
           (output) (str): output file (input+'.toc)

        Returns:
           (CM return dict):

           * return (int): return code == 0 if no error and >0 if error
           * (error) (str): error string if return>0
        """

        input_file = i.get('input', '')
        if input_file == '':
            return {'return':1, 'error':'please specify --input={txt file}'}
        
        output_file = i.get('output','')

        if output_file=='':
            output_file = input_file + '.toc'
        
        r = utils.load_txt(input_file, check_if_exists = True)
        if r['return']>0: return r

        lines = r['string'].split('\n')

        toc = []

        toc.append('<details>')
        toc.append('<summary>Click here to see the table of contents.</summary>')
        toc.append('')

        for line in lines:
            line = line.strip()

            if line.startswith('#'):
                j = line.find(' ')
                if j>=0:
                    title = line[j:].strip()

                    x = title.lower().replace(' ','-')

                    for k in range(0,2):
                        if x.startswith('*'):
                            x=x[1:]
                        if x.endswith('*'):
                            x=x[:-1]

                    for z in [':', '+', '.', '(', ')', ',']:
                        x = x.replace(z, '')

                    y = ' '*(2*(j-1)) + '* ['+title+'](#'+x+')'
                    
                    toc.append(y)

        toc.append('')
        toc.append('</details>')
        
        r = utils.save_txt(output_file, '\n'.join(toc)+'\n')
        if r['return']>0: return r

        return {'return':0}

    ##############################################################################
    def copy_to_clipboard(self, i):
        """
        Copy string to a clipboard

        Args:    

           string (str): string to copy to a clipboard
           (add_quotes) (bool): add quotes to the string in a clipboard
           (skip_fail) (bool): if True, do not fail

        Returns:
           (CM return dict):

           * return (int): return code == 0 if no error and >0 if error
           * (error) (str): error string if return>0
        """

        s = i.get('string','')

        if i.get('add_quotes',False): s='"'+s+'"'

        failed = False
        warning = ''

        # Try to load pyperclip (seems to work fine on Windows)
        try:
            import pyperclip
        except Exception as e:
            warning = format(e)
            failed = True
            pass

        if not failed:
            pyperclip.copy(s)
        else:
            failed = False

            # Try to load Tkinter
            try:
                from Tkinter import Tk
            except ImportError as e:
                warning = format(e)
                failed = True
                pass

            if failed:
                failed = False
                try:
                    from tkinter import Tk
                except ImportError as e:
                    warning = format(e)
                    failed = True
                    pass

            if not failed:
                # Copy to clipboard
                try:
                    r = Tk()
                    r.withdraw()
                    r.clipboard_clear()
                    r.clipboard_append(s)
                    r.update()
                    r.destroy()
                except Exception as e:
                    failed = True
                    warning = format(e)

        rr = {'return':0}
        
        if failed:
            if not i.get('skip_fail',False):
                return {'return':1, 'error':warning}

            rr['warning']=warning 
        
        return rr

    ##############################################################################
    def list_files_recursively(self, i):
        """
        List files and concatenate into string separate by comma

        Args:    

        Returns:
           (CM return dict):

           * return (int): return code == 0 if no error and >0 if error
           * (error) (str): error string if return>0
        """

        files = os.walk('.')

        s = ''

        for (dir_path, dir_names, file_names) in files:
            for f in file_names:
                if s!='': s+=','

                if dir_path=='.':
                    dir_path2=''
                else:
                    dir_path2=dir_path[2:].replace('\\','/')+'/'

                s+=dir_path2+f

        print (s)

        return {'return':0}

    ##############################################################################
    def generate_secret(self, i):
        """
        Generate secret for web apps

        Args:    

        Returns:
           (CM return dict):

           secret (str): secret
           
           * return (int): return code == 0 if no error and >0 if error
           * (error) (str): error string if return>0
        """

        import secrets
        s = secrets.token_urlsafe(16)       

        print (s)

        return {'return':0, 'secret': s}

    ##############################################################################
    def uid(self, i):
        """
        Generate CM UID.

        Args:
          (CM input dict): empty dict

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          * uid (str): CM UID
        """

        console = i['control'].get('out') == 'con'

        r = utils.gen_uid()

        if console:
            print (r['uid'])

        return r

    ############################################################
    def print_yaml(self, i):
        """
        Print YAML file

        Args:
          (CM input dict):
            file (str): input file

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

        """

        filename = i.get('file', '')
        if filename == '':
            return {'return':1, 'error':'please specify --file={YAML file}'}
        
        r = utils.load_yaml(filename,check_if_exists = True)
        if r['return']>0: return r

        meta = r['meta']

        import json
        print (json.dumps(meta, indent=2))
        
        return {'return':0}

    ############################################################
    def print_json(self, i):
        """
        Print YAML file

        Args:
          (CM input dict):
            file (str): input file

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

        """

        filename = i.get('file', '')
        if filename == '':
            return {'return':1, 'error':'please specify --file={JSON file}'}
        
        r = utils.load_json(filename,check_if_exists = True)
        if r['return']>0: return r

        meta = r['meta']

        import json
        print (json.dumps(meta, indent=2))
        
        return {'return':0}

    ##############################################################################
    def md5sum(self, i):
        """
        Calculate md5sum

        Args:
           i (dict): CMX input dict

              filename (str): path to file

        Returns:
           (CM return dict):

           * return (int): return code == 0 if no error and >0 if error
           * (error) (str): error string if return>0

           * md5sum (str): md5sum of the give file

        """

        import sys
        import hashlib

        filename = i['filename']

        with open(filename, "rb") as f:
            file_hash = hashlib.md5()
            while chunk := f.read(100000):
                file_hash.update(chunk)

        md5sum = file_hash.hexdigest()

        return {'return':0, 'md5sum': md5sum}

    ############################################################
    def select_from_list(self, i):
        """
        Select from list

        Args:
          text (str):
          list (list):

        Returns:
          value (str)
        """

        console = i['control'].get('out', '') == 'con'

        _input = i['control'].get('_input', {})

        text = _input.pop('text', '')
        lst = _input.pop('list', [])
        quiet = _input.pop('quiet', False)

        r = utils.test_input(_input)
        if r['return']>0: return self.cmind.embed_error(r)

        # Prepare selection
        value = ''
        new_index_int = 0

        if len(lst) == 1:
            value = lst[0]

        elif len(lst) > 0:

            if text == '':
                text = 'Select'

            text += ':'

            if console:
                print ('')
                print (text)
                print ('')

            index = 0
            for value in lst:
                show = f'{index}) {value}'

                if console:
                    print (show)

                index += 1

            print ('')

            if quiet:
                if console:
                    print ('Quietly selected: 0')
            else:
                new_index = input('Make your selection or press Enter for 0: ').strip()

                new_index_int = 0 if new_index == '' else int(new_index)

                if new_index_int < 0 or new_index_int >= index:
                    return {'return':1, 'error': 'selection out of range'}
 
            value = lst[new_index_int]

        return {'return':0, 
                'index': new_index_int,
                'value': value}

    ############################################################
    def download_rclone_mlcommons(self, i):
        """
        Download MLCommons artifacts via rclone

        Args:

        Returns:
        """

        ii = {}
        for k in ['input', 'key']:
            if k in i: ii[k] = i[k]

        return utils.call_internal_module(self, __file__, 'modulex_rclone_mlcommons', 'process', ii)

    ############################################################
    def download_hf(self, i):
        """
        Download via HF

        Args:

        Returns:
        """

        ii = {}
        for k in ['input', 'key']:
            if k in i: ii[k] = i[k]

        return utils.call_internal_module(self, __file__, 'modulex_hf', 'process', ii)

    ############################################################
    def summarize_keys(self, i):
        """
        Summarize keys in a list of dictionaries

        Args:
          sumary (list): list of dictionaries

        Returns:
          keys (dict): all keys as lists of all sorted values
          total_results (int): total number of results

        """

        _input = i['control'].get('_input', {})

        summary = _input.pop('summary', [])

        keys = {}

        total_results = 0

        for result in summary:
            total_results += 1
            for k in result:
                v = result[k]

                if k not in keys:
                    keys[k] = []

                if v not in keys[k]:
                    keys[k].append(v)

        # Sort lists
        for k in keys:
            v = keys[k]

            numeric = True
            for vv in v:
                if type(vv) not in [int, float]:
                    numeric = False
                    break

            if numeric:
                keys[k] = sorted(v)
            else:
                keys[k] = sorted(v, key = lambda x: str(x))

        return {'return':0, 'keys': keys, 'total_results': total_results}
