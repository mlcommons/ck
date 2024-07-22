# Documenting CM automations
#
# Written by Grigori Fursin

import os
from cmind import utils
    
############################################################
def doc(i):
    """
    Document CM automations.

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
    self_module = i['self_module']

    cur_dir = os.getcwd()

    template_file = 'template_list_of_automations.md'
    output_file = 'list_of_automations.md'

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
    
    ii = utils.sub_input(i, self_module.cmind.cfg['artifact_keys'])

    ii['out'] = None

    # Search for automations in repos
    lst = []
    for repo in list_of_repos:
        parsed_artifact[1] = ('',repo) if utils.is_cm_uid(repo) else (repo,'')
        ii['parsed_artifact'] = parsed_artifact
        r = self_module.search(ii)
        if r['return']>0: return r
        lst += r['list']

    toc = []
    toc2 = {}

    md = []
    
    for artifact in sorted(lst, key = lambda x: (-x.meta.get('sort',0), x.meta.get('alias',''))):
        md_script_readme = ['*This README is automatically generated - don\'t edit! {{CM_SEE_README_EXTRA}} for extra notes!*', 
                            '',
                            ]
        
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

        md.append('* GitHub repository with CM automations: *cm pull [{}]({})*'.format(repo_alias, url_repo))
        md.append('* CM automation code and meta: *[GitHub]({})*'.format(url))
        md.append('* CM automation actions:')

        x = 'Automation actions'
        md_script_readme.append('### Automation actions')
        md_script_readme.append('')
        
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

                    y = '[add flags (dict keys) from this API]({})'.format(module_url+'#L'+str(line_number))
                    y2 = '[add keys from this API]({})'.format(module_url+'#L'+str(line_number))
                    z = '({})'.format(y)
                    
                    md_script_readme.append('#### '+action)
                    md_script_readme.append('')
                    md_script_readme.append('  * CM CLI: ```cm '+action+' '+alias+'``` '+z)
                    md_script_readme.append('  * CM CLI with UID: ```cm '+action+' '+alias+','+uid+'``` '+z)
                    md_script_readme.append('  * CM Python API:')
                    md_script_readme.append('    ```python')
                    md_script_readme.append('    import cmind')
                    md_script_readme.append('')
                    md_script_readme.append("    r=cm.access({")
                    md_script_readme.append("                 'action':'{}'".format(action))
                    md_script_readme.append("                 'automation':'{},{}'".format(alias,uid))
                    md_script_readme.append("                 'out':'con'")
                    md_script_readme.append("    ```")
                    md_script_readme.append("    {}".format(y2))
                    md_script_readme.append("    ```python")
                    md_script_readme.append("                })")
                    md_script_readme.append("    if r['return']>0:")
                    md_script_readme.append("        print(r['error'])")
                    md_script_readme.append('    ```')
                    md_script_readme.append('')



            line_number+=1

        md.append('\n')

        # Add maintainers
        md_script_readme.append('### Maintainers')
        md_script_readme.append('')
        md_script_readme.append('* [MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)')


        # Check README and if it's already automatically generated
        path_readme = os.path.join(path, 'README.md')
        path_readme_extra = os.path.join(path, 'README-extra.md')

        if os.path.isfile(path_readme):
            r = utils.load_txt(path_readme, split = True)
            if r['return']>0: return 
        
            s = r['string']
            readme = r['list']

            if not 'automatically generated' in s.lower():
                found_path_readme_extra = True
                
                # Attempt to rename to README-extra.md

                if os.path.isfile(path_readme_extra):
                    return {'return':1, 'error':'README.md is not auto-generated and README-extra.md already exists - can\'t rename'}

                os.rename(path_readme, path_readme_extra)

                # Add to Git (if in git)
                os.chdir(path)
                os.system('git add README-extra.md')
                os.chdir(cur_dir)
    
        cm_readme_extra = ''
        cm_see_readme_extra = 'Use `README-extra.md`'

        if os.path.isfile(path_readme_extra):
            readme_extra_url = url+'/README-extra.md'

            cm_see_readme_extra = 'See [extra README](README-extra.md)'
            cm_readme_extra='\n'+cm_see_readme_extra+'.\n'


        s = '\n'.join(md_script_readme)

        s = s.replace('{{CM_SEE_README_EXTRA}}', cm_see_readme_extra)

        r = utils.save_txt(path_readme, s)
        if r['return']>0: return r

        # Add to Git (if in git)
        os.chdir(path)
        os.system('git add README.md')
        os.chdir(cur_dir)


    # Load template
    r = utils.load_txt(os.path.join(self_module.path, template_file))
    if r['return']>0: return r

    s = r['string']

    s = s.replace('{{CM_TOC}}', '\n'.join(toc))
    s = s.replace('{{CM_MAIN}}', '\n'.join(md))

    # Output
    output_dir = i.get('output_dir','')

    if output_dir == '': output_dir = '..'

    output_file = os.path.join(output_dir, output_file)

    r = utils.save_txt(output_file, s)
    if r['return']>0: return r

    return {'return':0}
