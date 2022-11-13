import os

from cmind.automation import Automation
from cmind import utils

class CAutomation(Automation):
    """
    CM "automation" automation actions
    """

    ############################################################
    def __init__(self, cmind, automation_file):
        super().__init__(cmind, automation_file)

    ############################################################
    def add(self, i):
        """
        Add CM automation.

        Args:
          (CM input dict): 

          (out) (str): if 'con', output to console

          parsed_artifact (list): prepared in CM CLI or CM access function
                                    [ (artifact alias, artifact UID) ] or
                                    [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

        """

        import shutil

        console = i.get('out') == 'con'

        parsed_artifact = i.get('parsed_artifact',[])

        artifact_obj = parsed_artifact[0] if len(parsed_artifact)>0 else ('','')

        module_name = 'module.py'

        tags_list = utils.convert_tags_to_list(i)
        if 'automation' not in tags_list: tags_list.append('automation')

        # Add placeholder (use common action)
        i['out']='con'
        i['common']=True

        i['meta']={'automation_alias':self.meta['alias'],
                   'automation_uid':self.meta['uid'],
                   'tags':tags_list}

        if 'tags' in i: del(i['tags'])

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


    ############################################################
    def doc(self, i):
        """
        Add CM automation.

        Args:
          (CM input dict): 

          (out) (str): if 'con', output to console

          parsed_artifact (list): prepared in CM CLI or CM access function
                                    [ (artifact alias, artifact UID) ] or
                                    [ (artifact alias, artifact UID), (artifact repo alias, artifact repo UID) ]

          (repos) (str): list of repositories to search for automations (internal & mlcommons@ck by default)

          (output_dir) (str): output directory (../docs by default)

        Returns:
          (CM return dict):

          * return (int): return code == 0 if no error and >0 if error
          * (error) (str): error string if return>0

        """

        template_file = 'list_of_automations.md'

        # Check parsed automation
        if 'parsed_automation' not in i:
           return {'return':1, 'error':'automation is not specified'}

        console = i.get('out') == 'con'

        repos = i.get('repos','')
        if repos == '': repos='internal,a4705959af8e447a'

        parsed_artifact = i.get('parsed_artifact',[])
        
        if len(parsed_artifact)<1:
            parsed_artifact = [('',''), ('','')]
        elif len(parsed_artifact)<2:
            parsed_artifact.append(('',''))
        else:
            repos = parsed_artifact[1][0]

        list_of_repos = repos.split(',') if ',' in repos else [repos]
        
        ii = utils.sub_input(i, self.cmind.cfg['artifact_keys'])

        ii['out'] = None

        # Search for automations in repos
        lst = []
        for repo in list_of_repos:
            parsed_artifact[1] = ('',repo) if utils.is_cm_uid(repo) else (repo,'')
            ii['parsed_artifact'] = parsed_artifact
            r = self.search(ii)
            if r['return']>0: return r
            lst += r['list']

        toc = []
        toc2 = {}

        md = []
        
        for artifact in sorted(lst, key = lambda x: (-x.meta.get('sort',0), x.meta.get('alias',''))):
            path = artifact.path
            meta = artifact.meta
            original_meta = artifact.original_meta

            print ('Documenting {}'.format(path))

            alias = meta.get('alias','')
            uid = meta.get('uid','')

            desc = meta.get('desc','')
            developers = meta.get('developers','')

            repo_path = artifact.repo_path
            repo_meta = artifact.repo_meta

            repo_alias = repo_meta.get('alias','')
            repo_uid = repo_meta.get('uid','')

            # Check URL
            url = ''
            url_repo = ''
            if repo_alias == 'internal':
                url_repo = 'https://github.com/mlcommons/ck/tree/master/cm/cmind/repo'
                url = url_repo+ '/automation/'
            elif '@' in repo_alias:
                url_repo = 'https://github.com/'+repo_alias.replace('@','/')+'/tree/master'
                if repo_meta.get('prefix','')!='': url_repo+='/'+repo_meta['prefix']
                url = url_repo+ '/automation/'

            if url!='':
                url+=alias

            x = '* [{}](#{})'.format(alias, alias)
            if desc !='': x+=' *('+desc+')*'

            toc.append(x)

            md.append('## '+alias)
            md.append('\n')
            
            if desc!='':
                md.append('*'+desc+'.*')
                md.append('\n')

#            if developers!='':
#                md.append('Developers: '+developers)
#                md.append('\n')

            md.append('* CM GitHub repository: *[{}]({})*'.format(repo_alias, url_repo))
            md.append('* CM artifact (module and meta): *[GitHub]({})*'.format(url))
            md.append('* CM actions:')

            # Load module
            module_path = os.path.join(path, 'module.py')
            module_url = url+'/module.py'

            r = utils.load_txt(module_path)
            if r['return']>0: return r

            module_py = r['string']

            module_py_list = module_py.split('\n')

            line_number = 0
            for line in module_py_list:
                if line.startswith('    def '):
                    j=line.find('(')
                    action = line[8:j]

                    if not action.startswith('_'):
                        x = '  * cm **'+action+'** '+alias+'   &nbsp;&nbsp;&nbsp;*( [See CM API]({}) )*'.format(module_url+'#L'+str(line_number))
                        md.append(x)

                line_number+=1

            md.append('\n')

        # Load template
        r = utils.load_txt(os.path.join(self.path, template_file))
        if r['return']>0: return r

        s = r['string']

        s = s.replace('{{CM_TOC}}', '\n'.join(toc))
        s = s.replace('{{CM_MAIN}}', '\n'.join(md))

        # Output
        output_dir = i.get('output_dir','')

        if output_dir == '': output_dir = '..'

        output_file = os.path.join(output_dir, template_file)

        r = utils.save_txt(output_file, s)
        if r['return']>0: return r

        return {'return':0}
