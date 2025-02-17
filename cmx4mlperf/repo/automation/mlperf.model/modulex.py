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

