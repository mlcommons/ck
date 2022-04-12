import os

from cmind.automation import Automation
from cmind import utils

class CAutomation(Automation):
    """
    Automation actions for the automation module
    """

    ############################################################
    def __init__(self, cmind, automation_file):
        super().__init__(cmind, automation_file)

    ############################################################
    def add(self, i):
        """
        Add automation

        Args:
           (artifact) (str) - repository name
           
        """

        import shutil

        console = i.get('out') == 'con'

        parsed_artifact = i.get('parsed_artifact',[])

        artifact_obj = parsed_artifact[0] if len(parsed_artifact)>0 else ('','')

        module_name = 'module.py'
        
        # Add placeholder
        i['out']='con'
        i['default']=True
        
        i['meta']={'automation_alias':self.meta['alias'],
                   'automation_uid':self.meta['uid'],
                   'tags':['automation',module_name]}

        r_obj=self.cmind.access(i)
        if r_obj['return']>0: return r_obj

        new_automation_path = r_obj['path']

        if console:
            print ('Created automation in {}'.format(new_automation_path))

        # Create Python module holder
        module_holder_path = new_automation_path

        # Copy support files
        original_path = os.path.dirname(self.path)

        # Copy module files
        for f in ['module_dummy.py']:
            f1 = os.path.join(self.path, f)
            f2 = os.path.join(new_automation_path, f.replace('_dummy',''))

            if console:
                print ('  * Copying {} to {}'.format(f1, f2))

            shutil.copyfile(f1,f2)

        return r_obj
