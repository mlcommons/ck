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
            info['bat_rem']='rem ${rem}'
            info['run_local_bat']='call ${bat_file}'
            info['run_bat']='call ${bat_file}'
        else:
            platform = 'linux'
            info['bat_ext']='.sh'
            info['set_env']='export ${key}="${value}"'
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

