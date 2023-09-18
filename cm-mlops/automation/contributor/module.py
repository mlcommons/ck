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

    ############################################################
    def add(self, i):
        """
        Add CM script

        Args:
          (CM input dict): 

          (out) (str): if 'con', output to console

          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

        """

        self_automation = self.meta['alias']+','+self.meta['uid']

        console = i.get('out') == 'con'

        artifact = i.get('artifact','')
        if ':' not in artifact:
            artifact = 'mlcommons@ck:'+artifact

        j = artifact.find(':')
        name = artifact[j+1:]

        # Check info
        if name == '':
            name = input('Enter your name: ').strip()
            if name == '':
                return {'return':1, 'error':'name can\'t be empty'}

            artifact += name

        # Check if doesn't exist
        r = self.cmind.access({'action':'find',
                               'automation':self_automation,
                               'artifact':artifact})
        if r['return']>0: return r
        elif r['return']==0 and len(r['list'])>0:
            return {'return':1, 'error':'CM artifact with name {} already exists in {}'.format(name, r['list'][0].path)}
        
        meta = i.get('meta',{})
        
        # Prepare meta
        org = meta.get('organization','')
        if org=='':
            org = input('Enter your organization (optional): ').strip()

        url = input('Enter your webpage (optional): ').strip()

        tags = input('Enter tags of your challenges separate by comma (you can add them later): ').strip()

        if meta.get('name','')=='':
            meta = {'name':name}

        if org!='':
            meta['organization'] = org

        if url!='':
            meta['urls'] = [url]

        if tags!='':
            meta['ongoing'] = tags.split(',')

        # Add placeholder (use common action)
        i['out'] = 'con'
        i['common'] = True # Avoid recursion - use internal CM add function to add the script artifact

        i['action'] = 'add'
        i['automation'] = self_automation
        i['artifact'] = artifact
        
        i['meta'] = meta

        print ('')

        r = self.cmind.access(i)
        if r['return']>0: return r

        path = r['path']

        path2 = os.path.dirname(path)
        
        print ('')
        print ('Please go to {}, add your directory to Git, commit and create PR:'.format(path2))
        print ('')
        print ('cd {}'.format(path2))
        print ('git add "{}"'.format(name))
        print ('git commit "{}"'.format(name))
        print ('')
        print ('Please join https://discord.gg/JjWNWXKxwT to discuss challenges!')
        print ('Looking forward to your contributions!')

        return r
