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
    def show(self, i):
        """
        Show cache

        Args:
          (CM input dict): 

          (out) (str): if 'con', output to console

          (env) (bool): if True, show env from cm-cached-state.json
          ...

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

          * Output from this automation action

        """
        import json

        # Check parsed automation
        if 'parsed_automation' not in i:
           return {'return':1, 'error':'automation is not specified'}

        console = i.get('out') == 'con'

        show_env = i.get('env', False)

# Moved to search function
#        # Check simplified CMD: cm show cache "get python"
#        # If artifact has spaces, treat them as tags!
#        artifact = i.get('artifact','')
#        tags = i.get('tags','').strip()
#        if ' ' in artifact or ',' in artifact:
#            del(i['artifact'])
#            if 'parsed_artifact' in i: del(i['parsed_artifact'])
#
#            new_tags = artifact.replace(' ',',')
#            tags = new_tags if tags=='' else new_tags+','+tags
#
#            i['tags'] = tags

        # Find CM artifact(s)
        i['out'] = None
        r = self.search(i)

        if r['return']>0: return r

        lst = r['list']
        for artifact in sorted(lst, key = lambda x: sorted(x.meta['tags'])):
#        for artifact in lst:
            path = artifact.path
            meta = artifact.meta
            original_meta = artifact.original_meta

            alias = meta.get('alias','')
            uid = meta.get('uid','')

            tags = meta.get('tags',[])
            tags1 = sorted([x for x in tags if not x.startswith('_')])
            tags2 = sorted([x for x in tags if x.startswith('_')])
            tags = tags1 + tags2

            version = meta.get('version','')

            if console:
                print ('')
#                print ('* UID: {}'.format(uid))
                print ('* Tags: {}'.format(','.join(tags)))
                print ('  Path: {}'.format(path))
                if version!='':
                    print ('  Version: {}'.format(version))

            if show_env and console:
                path_to_cached_state_file = os.path.join(path, 'cm-cached-state.json')

                if os.path.isfile(path_to_cached_state_file):
                    r =  utils.load_json(file_name = path_to_cached_state_file)
                    if r['return']>0: return r

                    # Update env and state from cache!
                    cached_state = r['meta']

                    new_env = cached_state.get('new_env', {})
                    if len(new_env)>0:
                        print ('    New env:')
                        print (json.dumps(new_env, indent=6, sort_keys=True).replace('{','').replace('}',''))

                    new_state = cached_state.get('new_state', {})
                    if len(new_state)>0:
                        print ('    New state:')
                        print (json.dumps(new_env, indent=6, sort_keys=True))

        return {'return':0, 'list': lst}

    ############################################################
    def search(self, i):
        """
        Overriding the automation search function to add support for a simplified CMD with tags with spaces

        TBD: add input/output description
        """

        # Check simplified CMD: cm show cache "get python"
        # If artifact has spaces, treat them as tags!
        artifact = i.get('artifact','')
        tags = i.get('tags','')
        # Tags may be a list (if comes internally from CM scripts) or string if comes from CMD
        if type(tags)!=list:
            tags = tags.strip()
        if ' ' in artifact:# or ',' in artifact:
            del(i['artifact'])
            if 'parsed_artifact' in i: del(i['parsed_artifact'])

            new_tags = artifact.replace(' ',',')
            tags = new_tags if tags=='' else new_tags+','+tags

            i['tags'] = tags

        # Force automation when reruning access with processed input
        i['automation']='cache,541d6f712a6b464e'
        i['action']='search'
        i['common'] = True # Avoid recursion - use internal CM add function to add the script artifact

        # Find CM artifact(s)
        return self.cmind.access(i)


    ############################################################
    def copy_to_remote(self, i):
        """
        Add CM automation.

        Args:
          (CM input dict):

          (out) (str): if 'con', output to console

          parsed_artifact (list): prepared in CM CLI or CM access function
                                    [ (artifact alias, artifact UID) ] or
                                    [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

          (repos) (str): list of repositories to search for automations (internal & mlcommons@ck by default)

          (output_dir) (str): output directory (./ by default)

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

        """

        return utils.call_internal_module(self, __file__, 'module_misc', 'copy_to_remote', i)
