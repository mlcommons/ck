import os
from cmind import utils
    
############################################################
def doc(i):
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

    self_module = i['self_module']

    cur_dir = os.getcwd()
    
    template_file = 'list_of_scripts.md'

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

    md = []

    toc = []

    toc_category = {}
    toc_category_sort = {}
    script_meta = {}

    for artifact in sorted(lst, key = lambda x: x.meta.get('alias','')):

        md_script = []
        md_script_readme = ['*This README is automatically generated - don\'t edit! {CM_SEE_README_EXTRA} for extra notes!*', '']
        
        path = artifact.path
        meta = artifact.meta
        original_meta = artifact.original_meta

        print ('Documenting {}'.format(path))

        alias = meta.get('alias','')
        uid = meta.get('uid','')

        script_meta[alias] = meta

        name = meta.get('name','')
        developers = meta.get('developers','')

        tags = meta.get('tags',[])

        variations = meta.get('variations',{})
        
        variation_keys = sorted(list(variations.keys()))
        version_keys = sorted(list(meta.get('versions',{}).keys()))

        default_variation = meta.get('default_variation','')
        default_version = meta.get('default_version','')



        category = meta.get('category', '').strip()
        category_sort = meta.get('category_sort', 0)
        if category != '':
            if category not in toc_category:
                toc_category[category]=[]

            if category not in toc_category_sort or category_sort>0:
                toc_category_sort[category]=category_sort

            if alias not in toc_category[category]:
                toc_category[category].append(alias)

        repo_path = artifact.repo_path
        repo_meta = artifact.repo_meta

        repo_alias = repo_meta.get('alias','')
        repo_uid = repo_meta.get('uid','')


        # Check URL
        url = ''
        url_repo = ''
        if repo_alias == 'internal':
            url_repo = 'https://github.com/mlcommons/ck/tree/master/cm/cmind/repo'
            url = url_repo+'/script/'
        elif '@' in repo_alias:
            url_repo = 'https://github.com/'+repo_alias.replace('@','/')+'/tree/master'
            if repo_meta.get('prefix','')!='': url_repo+='/'+repo_meta['prefix']
            url = url_repo+ '/script/'

        if url!='':
            url+=alias

        x = '* [{}](#{})'.format(alias, alias)
        if name !='': x+=' *('+name+')*'

        toc.append(x)

        md_script.append('## '+alias)
        md_script.append('')

        md_script_readme.append('### About')
        md_script_readme.append('')

        if name!='':
            name += '.'
            md_script.append('*'+name+'*')
            md_script.append('')

            md_script_readme.append(name)
            md_script_readme.append('{CM_README_EXTRA}')

#            if developers!='':
#                md_script.append('Developers: '+developers)
#                md_script.append('')
        else:
            md_script_readme.append('*TBD*')

        if category != '':
            md_script_readme.append('')
            md_script_readme.append('### Category')
            md_script_readme.append('')
            md_script_readme.append(category+'.')

        md_script_readme.append('')
        md_script_readme.append('### Maintainers')
        md_script_readme.append('')
        md_script_readme.append('* [Open MLCommons taskforce on education and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md).')


        md_script_readme.append('')
        md_script_readme.append('### Origin')
        md_script_readme.append('')

        x = '* GitHub repository: *[{}]({})*'.format(repo_alias, url_repo)
        md_script.append(x)
        md_script_readme.append(x)

        x = '* CM artifact for this script (interoperability module, native scripts and meta): *[GitHub]({})*'.format(url)
        md_script.append(x)
        md_script_readme.append(x)

        # Check meta
        meta_file = self_module.cmind.cfg['file_cmeta']
        meta_path = os.path.join(path, meta_file)

        meta_file += '.yaml' if os.path.isfile(meta_path+'.yaml') else '.json'

        meta_url = url+'/'+meta_file

        x = '* Meta description: *[GitHub]({})*'.format(meta_url)
        md_script.append(x)

        x = '* CM automation "script": *[Docs]({})*'.format('https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script')
        md_script.append(x)
        md_script_readme.append(x)
        
        all_tags = '`cm run script --tags="{}"`'.format(','.join(tags))
        x = '* CM CLI with all tags: {}*'.format(all_tags)
        md_script.append(x)

        all_tags_alternative = '`cm run script "{}"`'.format(' '.join(tags))
        x = '* CM CLI alternative: {}*'.format(all_tags_alternative)
        md_script.append(x)


        if len(variation_keys)>0:
            x=''
            for variation in variation_keys:
                if x!='': x+=';&nbsp; '
                x+='_'+variation
            md_script.append('* Variations: *{}*'.format(x))

        if default_variation!='':
            md_script.append('* Default variation: *{}*'.format(default_variation))

        if len(version_keys)>0:
            md_script.append('* Versions: *{}*'.format(';&nbsp; '.join(version_keys)))

        if default_version!='':
            md_script.append('* Default version: *{}*'.format(default_version))






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

            x = '* Extra README: [*GitHub*]({})'.format(readme_extra_url)
            md_script.append(x)

            cm_see_readme_extra = 'See [extra README](README-extra.md)'
            cm_readme_extra='\n'+cm_see_readme_extra+'.\n'


        md_script.append('')
        md_script_readme.append('')

        # Add extra to README
        md_script_readme.append('')
        md_script_readme.append('### Meta description')
        md_script_readme.append('[{}]({})'.format(meta_file, meta_file))
        md_script_readme.append('')

        md_script_readme.append('')
        md_script_readme.append('### Tags')
        md_script_readme.append('* All CM script tags: *{}*'.format(','.join(tags)))
        md_script_readme.append('* CM CLI: *{}*'.format(all_tags))
        md_script_readme.append('* CM CLI alternative: *{}*'.format(all_tags_alternative))
        md_script_readme.append('')

        if len(variation_keys)>0:
            md_script_readme.append('')
            md_script_readme.append('### Variations')

            variation_groups = {}
            internal_variations = []
            default_variations = []
            variation_md = {}

            md_script_readme.append('#### All variations')

            # Normally should not use anymore. Should use default:true inside individual variations.
            default_variation = meta.get('default_variation','')
            
            for variation_key in sorted(variation_keys):
                if variation_key.endswith('_'):
                    internal_variations.append(variation_key)
                    continue
                
                variation = variations[variation_key]
                
                default = variation.get('default', False)

                extra1 = ''
                extra2 = ''
                if default:
                    extra1 = '**'
                    extra2 = '** (default)'

                    default_variations.append(variation_key)

                md_var = []
                
                md_var.append('* {}{}{}'.format(extra1, variation_key, extra2))

                variation_md[variation_key] = md_var

                md_script_readme.append('\n'.join(md_var))

                group = variation.get('group','')

                if group !='':
                    if group not in variation_groups:
                        variation_groups[group]=[]

                    variation_groups[group].append(variation_key)

               
            if len(variation_groups)>0:
                md_script_readme.append('')
                md_script_readme.append('#### Variations by groups')

                for group_key in sorted(variation_groups):
                    md_script_readme.append('')
                    md_script_readme.append('  * {}'.format(group_key))

                    for variation_key in sorted(variation_groups[group_key]):
                        md = variation_md[variation_key]

                        for x in md:
                            md_script_readme.append('    '+x)
                        
#            if len(default_variations)>0:
#                md_script_readme.append('')
#                md_script_readme.append('#### Default variations')
#                md_script_readme.append('')
#
#                for variation_key in sorted(default_variations):
#                    md_script_readme.append('* {}'.format(variation_key))

            if len(internal_variations)>0:
                md_script_readme.append('')
                md_script_readme.append('#### Internal variations')
                md_script_readme.append('')

                for variation_key in sorted(internal_variations):
                    md_script_readme.append('* {}'.format(variation_key))




        if len(version_keys)>0 or default_version!='':
            md_script_readme.append('')
            md_script_readme.append('### Versions')

            if default_version!='':
                md_script_readme.append('Default version: *{}*'.format(default_version))
                md_script_readme.append('')

            if len(version_keys)>0:
                for version in version_keys:
                    md_script_readme.append('* {}'.format(version))

        
        
        # Add to the total list
        md += md_script

        s = '\n'.join(md_script_readme)

        s = s.replace('{CM_README_EXTRA}', cm_readme_extra)
        s = s.replace('{CM_SEE_README_EXTRA}', cm_see_readme_extra)
        
        r = utils.save_txt(path_readme, s)
        if r['return']>0: return r

        # Add to Git (if in git)
        os.chdir(path)
        os.system('git add README.md')
        os.chdir(cur_dir)


    # Recreate TOC with categories
    toc2 = []

    for category in sorted(toc_category, key = lambda x: -toc_category_sort[x]):
        toc2.append('### '+category)
        toc2.append('')

        for script in sorted(toc_category[category]):

            meta = script_meta[script]

            name = meta.get('name','')

            x = '* [{}](#{})'.format(script, script)
            if name !='': x+=' *('+name+')*'

            toc2.append(x)

        toc2.append('')

    # Load template
    r = utils.load_txt(os.path.join(self_module.path, template_file))
    if r['return']>0: return r

    s = r['string']

    s = s.replace('{{CM_TOC2}}', '\n'.join(toc2))
    s = s.replace('{{CM_TOC}}', '\n'.join(toc))
    s = s.replace('{{CM_MAIN}}', '\n'.join(md))

    # Output
    output_dir = i.get('output_dir','')

    if output_dir == '': output_dir = '..'

    output_file = os.path.join(output_dir, template_file)

    r = utils.save_txt(output_file, s)
    if r['return']>0: return r

    return {'return':0}
