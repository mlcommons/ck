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
          (CM input dict): 

          (out) (str): if 'con', output to console

          automation (str): automation as CM string object

          parsed_automation (list): prepared in CM CLI or CM access function
                                    [ (automation alias, automation UID) ] or
                                    [ (automation alias, automation UID), (automation repo alias, automation repo UID) ]

          (artifact) (str): artifact as CM string object

          (parsed_artifact) (list): prepared in CM CLI or CM access function
                                    [ (artifact alias, artifact UID) ] or
                                    [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          * Output from this automation action

        """

        import json
        print (json.dumps(i, indent=2))

        return {'return':0}

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
             * platform (str): "windows" or "linux"
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
            info['run_bat']='call ${bat_file}'
        else:
            platform = 'linux'
            info['bat_ext']='.sh'
            info['set_env']='export ${key}="${value}"'
            info['env_separator']=':'
            info['env_var']='${env_var}'
            info['set_exec_file']='chmod 755 "${file_name}"'
            info['bat_rem']='# ${rem}'
            info['run_local_bat']='. ./${bat_file}'
            info['run_bat']='. ${bat_file}'

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

        # Download
        size = -1
        downloaded = 0
        chunk_size = i.get('chunk_size', 65536)

        text = i.get('text','Downloaded: ')

        try:
            with requests.get(url, stream=True, allow_redirects=True) as download:
                download.raise_for_status()

                size = int(download.headers.get('Content-Length'))

                with open(path_to_file, 'wb') as output:
                    for chunk in download.iter_content(chunk_size = chunk_size):

                        if chunk:
                            output.write(chunk)

                        downloaded+=1
                        percent = downloaded * chunk_size * 100 / size

                        sys.stdout.write("\r{}{:3.0f}%".format(text, percent))
                        sys.stdout.flush()

        except requests.exceptions.RequestException as e:
            return {'return':1, 'error':format(e)}

        print ('')

        return {'return': 0, 'filename':file_name, 'path': path_to_file, 'size':size}

    ##############################################################################
    def unzip_file(self, i):
        """
        Unzip file

        Args:    
           (CM input dict):

           filename (str): explicit file name
           (path) (str): path where to unzip file (current path otherwise)

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

        console = i.get('out') == 'con'

        # Attempt to read cmr.json 
        file_name_handle = open(file_name, 'rb')
        file_name_zip = zipfile.ZipFile(file_name_handle)

        files=file_name_zip.namelist()

        path=i.get('path','')
        if path is None or path=='':
            path=os.getcwd()

        # Unpacking zip
        for f in files:
            if not f.startswith('..') and not f.startswith('/') and not f.startswith('\\'):
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
                    file_out.write(file_name_zip.read(f))
                    file_out.close()

        file_name_zip.close()
        file_name_handle.close()

        return {'return':0}

