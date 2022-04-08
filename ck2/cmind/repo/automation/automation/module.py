import os

from cmind.module import Module
from cmind import utils

class CModule(Module):
    """
    Automation actions for the automation module
    """

    ############################################################
    def __init__(self, cmind, module_name):
        super().__init__(cmind, module_name)

    ############################################################
    def add(self, i):
        """
        Add automation

        Args:
           (artifact) (str) - repository name
           
        """

        import shutil

        con = True if self.cmind.con and not i.get('skip_con', False) else False

        parsed_artifact = i.get('parsed_artifact',[])

        artifact_obj = parsed_artifact[0] if len(parsed_artifact)>0 else ('','')

        module_name = 'module.py'
        
        # Add placeholder
        i['skip_con']=True
        i['default']=True
        
        i['meta']={'automation_alias':self.meta['alias'],
                   'automation_uid':self.meta['uid'],
                   'tags':['automation',module_name]}

        r_obj=self.cmind.access(i)
        if r_obj['return']>0: return r_obj

        new_automation_path = r_obj['path']

        if con:
            print ('Created automation in {}'.format(new_automation_path))

        # Create Python module holder
        module_holder_path = new_automation_path

        # Copy support files
        original_path = os.path.dirname(self.path)

        # Copy module files
        for f in ['module_dummy.py']:
            f1 = os.path.join(self.path, f)
            f2 = os.path.join(new_automation_path, f.replace('_dummy',''))

            if con:
                print ('  * Copying {} to {}'.format(f1, f2))

            shutil.copyfile(f1,f2)

        return r_obj
