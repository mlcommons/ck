import os

from cmind.module import Module
from cmind import utils

class CModule(Module):
    """
    OS automation actions
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

        module_name = artifact_obj[0] if artifact_obj[0]!='' else artifact_obj[1]
        
        # Add placeholder
        i['skip_con']=True
        i['default']=True
        
        i['meta']={'automation_alias':self.meta['alias'],
                   'automation_uid':self.meta['uid'],
                   'module_name':self.cmind.cfg['cmind_python_module_prefix']+module_name, 
                   'tags':['automation',module_name]}

        r_obj=self.cmind.access(i)
        if r_obj['return']>0: return r_obj

        new_automation_path = r_obj['path']

        if con:
            print ('Created automation in {}'.format(new_automation_path))

        # Create Python module holder
        module_holder_path = os.path.join(new_automation_path, 
                                          self.cmind.cfg['cmind_python_module_prefix']+module_name)
        if not os.path.isdir(module_holder_path):
            os.makedirs(module_holder_path)

            if con:
                print ('Created module directory in {}'.format(module_holder_path))

        # Copy support files
        original_path = os.path.dirname(self.path)

        for f in ['requirements.txt', 'setup.py']:
            f1 = os.path.join(original_path, f)
            f2 = os.path.join(new_automation_path, f)

            if con:
                print ('  * Copying {} to {}'.format(f1, f2))

            shutil.copyfile(f1,f2)
       
        # Copy module files
        for f in ['__init__.py', 'module_dummy.py']:
            f1 = os.path.join(original_path, self.cmind.cfg['cmind_python_module_prefix']+'automation', f)
            f2 = os.path.join(new_automation_path, self.cmind.cfg['cmind_python_module_prefix']+module_name, f.replace('_dummy',''))

            if con:
                print ('  * Copying {} to {}'.format(f1, f2))

            shutil.copyfile(f1,f2)

        return r_obj
