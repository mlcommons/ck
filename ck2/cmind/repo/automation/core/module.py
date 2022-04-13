import os

from cmind.automation import Automation
from cmind import utils

# This is just an example of how to import extra files from such a package
# We need to make it unique!
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cm_60cb625a46b38610 import misc

class CAutomation(Automation):
    """
    CM core automation actions
    """

    ############################################################
    def __init__(self, cmind, automation_file):
        super().__init__(cmind, __file__)


    ############################################################
    def uid(self, i):
        """
        Generate CM UID
        """

        return misc.uid(i)

    ############################################################
    def test(self, i):
        """
        Check CM status
        """

        import sys
        
        console = i.get('out') == 'con'

        import cmind
        version = cmind.__version__
        
        print ('CM version: {}'.format(version))
        
        # Check if repository is broken
        try:
            from cmind import net
            rn = net.request(
                {'get': {'action': 'get-cm-version-notes', 'version': version}})
            if rn['return'] == 0:
                notes = rn.get('dict', {}).get('notes', '')

                if notes !='':
                    print ('')
                    print (notes)
        except Exception as e:
            print ('error: {}'.format(e))
            pass

        x = sys.executable
        if x != None and x != '':
            print ('')
            print ('Python executable used by CK: {}'.format(x))


        print ('')
        print ('Path to CM package:         {}'.format(self.cmind.path_to_cmind))
        print ('Path to CM core:            {}'.format(self.cmind.path_to_cmind_kernel))
        print ('Path to CM internal repo:   {}'.format(self.cmind.repos.path_to_internal_repo))

        print ('')
        print ('Path to CM repositories:    {}'.format(self.cmind.home_path))

        print ('')
        print ('GitHub for CM development:  https://github.com/mlcommons/ck/tree/master/ck2')
        print ('Reporting issues and ideas: https://github.com/mlcommons/ck/issues')

        return {'return':0}
