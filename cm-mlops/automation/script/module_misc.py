import os
from cmind import utils
    
# Meta deps
def process_deps(self_module, meta, meta_url, md_script_readme, key, extra_space='', skip_from_meta=False, skip_if_empty=False):

    x = ''
    y = []
    if len(meta.get(key,{}))>0:
        x = '***'
    
        for d in meta[key]:
            d_tags = d.get('tags', '')

            z = extra_space+'     * '+d_tags

            names = d.get('names', [])
            enable_if_env = d.get('enable_if_env', {})
            skip_if_env = d.get('skip_if_env', {})

            q = ''
            
            q1 = ''
            for e in enable_if_env:
                if q1!='': q1 += ' AND '
                q1 += e+' '
                v = enable_if_env[e]
                q1 += ' == '+str(v[0]) if len(v)==1 else 'in '+str(v)
            if q1!='': q1 = '('+q1+')'

            q2 = ''
            for e in skip_if_env:
                if q2!='': q2 += ' OR '
                q2 += e+' '
                v = skip_if_env[e]
                q2 += ' != '+str(v[0]) if len(v)==1 else 'not in '+str(v)

            if q2!='': q2 = '('+q2+')'

            if q1!='' or q2!='':
               q = 'if '

               if q1!='': q+=q1
               if q2!='':
                  if q1!='': q+=' AND '
                  q+=q2


            
            y.append(z)

            if q!='': 
               y.append(extra_space+'       * `'+q+'`')

            if len(names)>0:
               y.append(extra_space+'       * CM names: `--adr.'+str(names)+'...`')


            # Attempt to find related CM scripts
            r = self_module.cmind.access({'action':'find',
                                          'automation':'script',
                                          'tags':d_tags})
            if r['return']==0:
                lst = r['list']
                
                if len(lst)==0:
                    y.append(extra_space+'       - *Warning: no scripts found*')
                else:
                    for s in lst:
                        s_repo_meta = s.repo_meta

                        s_repo_alias = s_repo_meta.get('alias','')
                        s_repo_uid = s_repo_meta.get('uid','')

                        # Check URL
                        s_url = ''
                        s_url_repo = ''
                        if s_repo_alias == 'internal':
                            s_url_repo = 'https://github.com/mlcommons/ck/tree/master/cm/cmind/repo'
                            s_url = s_url_repo+'/script/'
                        elif '@' in s_repo_alias:
                            s_url_repo = 'https://github.com/'+s_repo_alias.replace('@','/')+'/tree/master'
                            if s_repo_meta.get('prefix','')!='': s_url_repo+='/'+s_repo_meta['prefix']
                            s_url = s_url_repo+ '/script/'

                        s_alias = s.meta['alias']
                        y.append(extra_space+'       - CM script: [{}]({})'.format(s_alias, s_url+s_alias))

                

    z = ''
    if not skip_from_meta:
        z = ' from [meta]({})'.format(meta_url)
    
    if not skip_if_empty or len(y)>0:
        md_script_readme.append((extra_space+'  1. '+x+'Read "{}" on other CM scripts'+z+x).format(key))
        md_script_readme += y

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
    
    template_file = 'template_list_of_scripts.md'
    list_file = 'list_of_scripts.md'

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

    ii = utils.sub_input(i, self_module.cmind.cfg['artifact_keys'] + ['tags'])

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
    urls = {}

    for artifact in sorted(lst, key = lambda x: x.meta.get('alias','')):

        toc_readme = []

        # Common index for all scripts
        md_script = []

        # This readme
        md_script_readme = [
                            '<details>',
                            '<summary>Click here to see the table of contents.</summary>',
                            '{{CM_README_TOC}}',
                            '</details>',
                            '',
                            '*Note that this README is automatically generated - don\'t edit! {{CM_SEE_README_EXTRA}}.*', 
                            ''
                            ]
        
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

        input_mapping = meta.get('input_mapping', {})
        input_description = meta.get('input_description', {})

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

        urls[alias]=url

        x = '* [{}]({})'.format(alias, url)
        if name !='': x+=' *('+name+')*'
        toc.append(x)

        md_script.append('## '+alias)
        md_script.append('')

        x = 'Description'
#        md_script_readme.append('___')
        md_script_readme.append('### '+x)
        md_script_readme.append('')
        toc_readme.append(x)

#        x = 'About'
#        md_script_readme.append('#### '+x)
#        md_script_readme.append('')
#        toc_readme.append(' '+x)

        if name!='':
            name += '.'
            md_script.append('*'+name+'*')
            md_script.append('')

            md_script_readme.append('*'+name+'*')
            md_script_readme.append('')
        
        # Check if there is about doc
        path_readme = os.path.join(path, 'README.md')
        path_readme_extra = os.path.join(path, 'README-extra.md')
        path_readme_about = os.path.join(path, 'README-about.md')

        if os.path.isfile(path_readme_about):
            r = utils.load_txt(path_readme_about, split = True)
            if r['return']>0: return 
        
            s = r['string']
            readme_about = r['list']

            md_script_readme += readme_about
            
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
        cm_see_readme_extra = 'Use `README-extra.md` to add more info'

        
        
        if os.path.isfile(path_readme_extra):
            md_script_readme.append('{{CM_README_EXTRA}}')

#        if developers!='':
#            md_script.append('Developers: '+developers)
#            md_script.append('')

        x = 'Information'
#        md_script_readme.append('___')
        md_script_readme.append('#### '+x)
        md_script_readme.append('')
        toc_readme.append(x)

        
        if category != '':
#            x = 'Category'
#            md_script_readme.append('___')
#            md_script_readme.append('#### '+x)
#            md_script_readme.append(' ')
#            md_script_readme.append(category+'.')
#            toc_readme.append(x)

            x = '* Category: *{}*'.format(category + '.')
            md_script_readme.append(x)


#        x = 'Origin'
#        md_script_readme.append('___')
#        md_script_readme.append('#### '+x)
#        md_script_readme.append('')
#        toc_readme.append(x)

        x = '* CM GitHub repository: *[{}]({})*'.format(repo_alias, url_repo)
        md_script.append(x)
        md_script_readme.append(x)

        
        x = '* GitHub directory for this script: *[GitHub]({})*'.format(url)
        md_script.append(x)
        md_script_readme.append(x)



        # Check meta
        meta_file = self_module.cmind.cfg['file_cmeta']
        meta_path = os.path.join(path, meta_file)

        meta_file += '.yaml' if os.path.isfile(meta_path+'.yaml') else '.json'

        meta_url = url+'/'+meta_file

        x = '* CM meta description of this script: *[GitHub]({})*'.format(meta_url)
        md_script.append(x)

#        x = '* CM automation "script": *[Docs]({})*'.format('https://github.com/octoml/ck/blob/master/docs/list_of_automations.md#script')
#        md_script.append(x)
#        md_script_readme.append(x)

        if len(variation_keys)>0:
            variation_pointer="[,variations]"
        else:
            variation_pointer=''

        if len(input_mapping)>0:
            input_mapping_pointer="[--input_flags]"
        else:
            input_mapping_pointer=''
        
        cli_all_tags = '`cm run script --tags={}{} {}`'.format(','.join(tags), variation_pointer, input_mapping_pointer)
        x = '* CM CLI with all tags: {}*'.format(cli_all_tags)
        md_script.append(x)

        cli_all_tags_alternative = '`cm run script "{}{}" {}`'.format(' '.join(tags), variation_pointer, input_mapping_pointer)
        x = '* CM CLI alternative: {}*'.format(cli_all_tags_alternative)
        md_script.append(x)

        cli_uid = '`cm run script {} {}`'.format(meta['uid'], input_mapping_pointer)
        x = '* CM CLI with alias and UID: {}*'.format(cli_uid)
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







        if os.path.isfile(path_readme_extra):
            readme_extra_url = url+'/README-extra.md'

            x = '* More info: [*GitHub*]({})'.format(readme_extra_url)
            md_script.append(x)

            cm_see_readme_extra = 'See [more info](README-extra.md)'
            cm_readme_extra='\n'+cm_see_readme_extra+'.\n'


        md_script.append('')
#        md_script_readme.append('')

        # Add extra to README
        x = 'Meta description'
#        md_script_readme.append('___')
#        md_script_readme.append('### '+x)
        md_script_readme.append('* CM meta description for this script: *[{}]({})*'.format(meta_file, meta_file))
#        md_script_readme.append('')
#        toc_readme.append(x)

        x = 'Tags'
#        md_script_readme.append('___')
#        md_script_readme.append('### '+x)
        md_script_readme.append('* CM "database" tags to find this script: *{}*'.format(','.join(tags)))
#        md_script_readme.append('')
#        toc_readme.append(x)


        cache = meta.get('cache', False)
        md_script_readme.append('* Output cached?: *{}*'.format(str(cache)))


        
        
        # Add usage
        x1 = 'Usage'
        x1a = 'CM installation'
        x1aa = 'CM pull repository'
        x1b = 'CM script automation help'
        x2 = 'CM CLI'
        x3 = 'CM Python API'
        x3a = 'CM GUI'
        x4 = 'CM modular Docker container'
        md_script_readme += ['___',
                             '### '+x1,
                             '',
                             '#### '+x1a,
                             '',
                             '[Guide](https://github.com/mlcommons/ck/blob/master/docs/installation.md)',
                             '',
                             '##### '+x1aa,
                             '',
                             '```cm pull repo {}```'.format(repo_alias),
                             '',
                             '##### '+x1b,
                             '',
                             '```cm run script --help```',
                             '',
                             '#### '+x2,
                             '',
                             '1. {}'.format(cli_all_tags),
                             '',
                             '2. {}'.format(cli_all_tags_alternative),
                             '',
                             '3. {}'.format(cli_uid),
                             '']
        md_script_readme += ['* `variations` can be seen [here](#variations)',
                             ''
                             ]
        md_script_readme += ['* `input_flags` can be seen [here](#script-flags-mapped-to-environment)',
                             ''
                             ]
        md_script_readme += ['#### '+x3,
                             '',
                             '<details>',
                             '<summary>Click here to expand this section.</summary>',
                             '',
                             '```python',
                             '',
                             'import cmind',
                             '',
                             "r = cmind.access({'action':'run'",
                             "                  'automation':'script',",
                             "                  'tags':'{}'".format(','.join(tags)),
                             "                  'out':'con',",
                             "                  ...",
                             "                  (other input keys for this script)",
                             "                  ...",
                             "                 })",
                             "",
                             "if r['return']>0:",
                             "    print (r['error'])",
                             '',
                             '```',
                             '',
                             '</details>',
                             '',

                             '',
                             '#### '+x3a,
                             '',
                             '```cm run script --tags=gui --script="'+','.join(tags)+'"```',
                             '',
                             'Use this [online GUI](https://cKnowledge.org/cm-gui/?tags={}) to generate CM CMD.'.format(','.join(tags)),
                             '',
                             '#### '+x4,
                             '',
                             '*TBD*',
                             ''
                            ]
        toc_readme.append(x1)
        toc_readme.append(' '+x1a)
        toc_readme.append(' '+x1b)
        toc_readme.append(' '+x2)
        toc_readme.append(' '+x3)
        toc_readme.append(' '+x3a)
        toc_readme.append(' '+x4)
                   
        x = 'Customization'
        md_script_readme.append('___')
        md_script_readme.append('### '+x)
        md_script_readme.append('')
        toc_readme.append(x)

        
        
        
        if len(variation_keys)>0:
#            x = 'Variation groups'
#            md_script_readme.append('___')
#            md_script_readme.append('### '+x)
#           toc_readme.append(x)

            variation_groups = {}
            default_variations = []
            variation_md = {}
            variation_alias = {}

            # Normally should not use anymore. Should use default:true inside individual variations.
            default_variation = meta.get('default_variation','')
            
            for variation_key in sorted(variation_keys):
                variation = variations[variation_key]

                alias = variation.get('alias','').strip()

                if alias!='':
                    aliases = variation_alias.get(alias, [])
                    if variation_key not in aliases: 
                        aliases.append(variation_key)
                    variation_alias[alias]=aliases

                    # Do not continue this loop if alias
                    continue

                default = variation.get('default', False)

                if not default:
                    # Check outdated
                    if default_variation == variation_key:
                        default = True
                
                extra1 = ''
                extra2 = ''
                if default:
                    extra1 = '**'
                    extra2 = '** (default)'

                    default_variations.append(variation_key)


                md_var = []
                
                md_var.append('* {}`_{}`{}'.format(extra1, variation_key, extra2))

                variation_md[variation_key] = md_var

#                md_script_readme+=md_var

                group = variation.get('group','')

                if variation_key.endswith('_'):
                    group = '*Internal group (variations should not be selected manually)*'
                elif group == '':
                    group = '*No group (any variation can be selected)*'

                if group not in variation_groups:
                    variation_groups[group]=[]

                variation_groups[group].append(variation_key)

               
            x = 'Variations'
            md_script_readme.append('')
            md_script_readme.append('#### '+x)
            toc_readme.append(' '+x)

            variation_groups_order = meta.get('variation_groups_order',[])
            for variation in sorted(variation_groups):
                if variation not in variation_groups_order:
                    variation_groups_order.append(variation)
            
            for group_key in variation_groups_order:
                md_script_readme.append('')

                if not group_key.startswith('*'):
                    md_script_readme.append('  * Group "**{}**"'.format(group_key))
                else:
                    md_script_readme.append('  * {}'.format(group_key))


                md_script_readme += [
                             '    <details>',
                             '    <summary>Click here to expand this section.</summary>',
                             ''
                             ]

                for variation_key in sorted(variation_groups[group_key]):
                    variation = variations[variation_key]

                    xmd = variation_md[variation_key]

                    aliases = variation_alias.get(variation_key,[])
                    aliases2 = ['_'+v for v in aliases]
                    
                    if len(aliases)>0:
                        xmd.append('  - Aliases: `{}`'.format(','.join(aliases2)))

                    if len(variation.get('env',{}))>0:
                        xmd.append('  - Environment variables:')
                        for key in variation['env']:
                            xmd.append('    - *{}*: `{}`'.format(key, variation['env'][key]))

                    xmd.append('  - Workflow:')

                    for dep in ['deps', 'prehook_deps', 'posthook_deps', 'post_deps']:
                         process_deps(self_module, variation, meta_url, xmd, dep, '  ', True, True)
                
                    for x in xmd:
                        md_script_readme.append('    '+x)

                md_script_readme.append('')
                md_script_readme.append('    </details>')
                md_script_readme.append('')

            # Check if has invalid_variation_combinations
            vvc = meta.get('invalid_variation_combinations', [])
            if len(vvc)>0:
                x = 'Unsupported or invalid variation combinations'
                md_script_readme.append('')
                md_script_readme.append('#### '+x)
                md_script_readme.append('')
                md_script_readme.append('')
                md_script_readme.append('')
                toc_readme.append(' '+x)
                
                for v in vvc:
                    vv = ['_'+x for x in v]
                    md_script_readme.append('* `'+','.join(vv)+'`')


            if len(default_variations)>0:
                md_script_readme.append('')
                md_script_readme.append('#### Default variations')
                md_script_readme.append('')

                dv = ['_'+x for x in sorted(default_variations)]

                md_script_readme.append('`{}`'.format(','.join(dv)))

        
        # Check if has valid_variation_combinations
        vvc = meta.get('valid_variation_combinations', [])
        if len(vvc)>0:
            x = 'Valid variation combinations checked by the community'
            md_script_readme.append('')
            md_script_readme.append('#### '+x)
            md_script_readme.append('')
            md_script_readme.append('')
            md_script_readme.append('')
            toc_readme.append(' '+x)
            
            for v in vvc:
                vv = ['_'+x for x in v]
                md_script_readme.append('* `'+','.join(vv)+'`')



        if len(input_description)>0:
            x = 'Input description'
            md_script_readme.append('')
            md_script_readme.append('#### '+x)
            toc_readme.append(' '+x)

            md_script_readme.append('')
            key0 = ''
            for key in input_description:
                if key0=='': key0=key

                value = input_description[key]
                desc = value

                if type(value) == dict:
                    desc = value['desc']

                    choices = value.get('choices', [])
                    if len(choices) > 0:
                        desc+=' {'+','.join(choices)+'}'

                    default = value.get('default','')
                    if default!='':
                        desc+=' (*'+str(default)+'*)'

                md_script_readme.append('* --**{}** {}'.format(key,desc))

            md_script_readme.append('')
            md_script_readme.append('**Above CLI flags can be used in the Python CM API as follows:**')
            md_script_readme.append('')

            x = '```python\nr=cm.access({... , "'+key0+'":...}\n```'
            md_script_readme.append(x)

        
        
        # Check input flags
        if len(input_mapping)>0:
            x = 'Script flags mapped to environment'
            md_script_readme.append('')
            md_script_readme.append('#### '+x)
            toc_readme.append(' '+x)

            md_script_readme.append('<details>')
            md_script_readme.append('<summary>Click here to expand this section.</summary>')

            md_script_readme.append('')
            key0 = ''
            for key in sorted(input_mapping):
                if key0=='': key0=key
                value = input_mapping[key]
                md_script_readme.append('* `--{}=value`  &rarr;  `{}=value`'.format(key,value))

            md_script_readme.append('')
            md_script_readme.append('**Above CLI flags can be used in the Python CM API as follows:**')
            md_script_readme.append('')

            x = '```python\nr=cm.access({... , "'+key0+'":...}\n```'
            md_script_readme.append(x)

            md_script_readme.append('')
            md_script_readme.append('</details>')
            md_script_readme.append('')
        
        
        # Default environment
        default_env = meta.get('default_env',{})

        x = 'Default environment'
#        md_script_readme.append('___')
        md_script_readme.append('#### '+x)
        toc_readme.append(' '+x)

        md_script_readme.append('')
        md_script_readme.append('<details>')
        md_script_readme.append('<summary>Click here to expand this section.</summary>')
        md_script_readme.append('')
        md_script_readme.append('These keys can be updated via `--env.KEY=VALUE` or `env` dictionary in `@input.json` or using script flags.')
        md_script_readme.append('')

        for key in default_env:
            value = default_env[key]
            md_script_readme.append('* {}: `{}`'.format(key,value))

        md_script_readme.append('')
        md_script_readme.append('</details>')
        md_script_readme.append('')
        
        
                



        
        if len(version_keys)>0 or default_version!='':
            x = 'Versions'
#            md_script_readme.append('___')
            md_script_readme.append('#### '+x)
            toc_readme.append(x)

            if default_version!='':
                md_script_readme.append('Default version: `{}`'.format(default_version))
                md_script_readme.append('')

            if len(version_keys)>0:
                for version in version_keys:
                    md_script_readme.append('* `{}`'.format(version))


        
        # Add workflow
        x = 'Script workflow, dependencies and native scripts'
        md_script_readme += ['___',
                             '### '+x,
                             '']
        toc_readme.append(x)

        md_script_readme.append('<details>')
        md_script_readme.append('<summary>Click here to expand this section.</summary>')

        md_script_readme.append('')

        # Check customize.py file
        path_customize = os.path.join(path, 'customize.py')
        found_customize = False
        found_customize_preprocess = False
        found_customize_postprocess = False
        found_output_env = []

        if os.path.isfile(path_customize):
            found_customize = True

            r = utils.load_txt(path_customize, split=True)
            if r['return']>0: return r
            
            customize  = r['string']
            customize_l = r['list']

            if 'def preprocess(' in customize:
                found_customize_preprocess = True

            if 'def postprocess(' in customize:
                found_customize_postprocess = True

            # Ugly attempt to get output env
            found_postprocess = False
            for l in customize_l:
#                if not found_postprocess:
#                    if 'def postprocess' in l:
#                        found_postprocess = True
#                else:
                 j = l.find(' env[')
                 if j>=0:
                     j1 = l.find(']', j+4)
                     if j1>=0:
                         j2 = l.find('=',j1+1)
                         if j2>=0:
                             key2 = l[j+5:j1].strip()
                             key=key2[1:-1]

                             if key.startswith('CM_') and 'TMP' not in key and key not in found_output_env:
                                 found_output_env.append(key)
                             
        process_deps(self_module, meta, meta_url, md_script_readme, 'deps')

        x = ''
        y = 'customize.py'
        if found_customize_preprocess:
            x = '***'
            y = '['+y+']('+url+'/'+y+')'
        md_script_readme.append(('  1. '+x+'Run "preprocess" function from {}'+x).format(y))

        process_deps(self_module, meta, meta_url, md_script_readme, 'prehook_deps')
        
        # Check scripts
        files = os.listdir(path)
        x = ''
        y = []
        for f in sorted(files):
            x = '***'
            if f.startswith('run') and (f.endswith('.sh') or f.endswith('.bat')):
                f_url = url+'/'+f
                y.append('     * [{}]({})'.format(f, f_url))

        md_script_readme.append(('  1. '+x+'Run native script if exists'+x).format(y))
        md_script_readme += y
        
        process_deps(self_module, meta, meta_url, md_script_readme, 'posthook_deps')

        x = ''
        y = 'customize.py'
        if found_customize_postprocess:
            x = '***'
            y = '['+y+']('+url+'/'+y+')'
        md_script_readme.append(('  1. '+x+'Run "postrocess" function from {}'+x).format(y))

        process_deps(self_module, meta, meta_url, md_script_readme, 'post_deps')
        md_script_readme.append('</details>')
        md_script_readme.append('')
                    
        # New environment
        new_env_keys = meta.get('new_env_keys',[])

        x = 'Script output'
        md_script_readme.append('___')
        md_script_readme.append('### '+x)
        toc_readme.append(x)
        
        x = 'New environment keys (filter)'
        md_script_readme.append('#### '+x)
        toc_readme.append(x)

        md_script_readme.append('')
        for key in sorted(new_env_keys):
            md_script_readme.append('* `{}`'.format(key))

        # Pass found_output_env through above filter
        found_output_env_filtered = []

        import fnmatch

        for key in found_output_env:
            add = False

            for f in new_env_keys:
                if fnmatch.fnmatch(key, f):
                    add = True
                    break

            if add:
                found_output_env_filtered.append(key)
                
        x = 'New environment keys auto-detected from customize'
        md_script_readme.append('#### '+x)
        toc_readme.append(x)

        md_script_readme.append('')
        for key in sorted(found_output_env_filtered):
            md_script_readme.append('* `{}`'.format(key))



        # Add maintainers
        x = 'Maintainers'
        md_script_readme.append('___')
        md_script_readme.append('### '+x)
        md_script_readme.append('')
        md_script_readme.append('* [Open MLCommons taskforce on automation and reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)')
        toc_readme.append(x)

        # Process TOC
        toc_readme_string = '\n'
        for x in toc_readme:
            x2 = x
            prefix = ''

            if x.startswith(' '):
                prefix = '  '
                x2 = x[1:]

            x2 = x2.lower().replace(' ','-').replace(',','')
            toc_readme_string += prefix + '* [{}](#{})\n'.format(x, x2)

        # Add to the total list
        md += md_script

        s = '\n'.join(md_script_readme)

        s = s.replace('{{CM_README_EXTRA}}', cm_readme_extra)
        s = s.replace('{{CM_SEE_README_EXTRA}}', cm_see_readme_extra)
        s = s.replace('{{CM_README_TOC}}', toc_readme_string)
        
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

            url = urls[script]

            x = '* [{}]({})'.format(script, url)
            if name !='': x+=' *('+name+')*'

            toc2.append(x)

        toc2.append('')

    toc_category_string = ''
    for category in sorted(toc_category):
        category_link = category.lower().replace(' ','-').replace('/','')
        toc_category_string += '* [{}](#{})\n'.format(category, category_link)

    
    # Load template
    r = utils.load_txt(os.path.join(self_module.path, template_file))
    if r['return']>0: return r

    s = r['string']

    s = s.replace('{{CM_TOC2}}', '\n'.join(toc2))
    s = s.replace('{{CM_TOC}}', '\n'.join(toc))
#    s = s.replace('{{CM_MAIN}}', '\n'.join(md))
    s = s.replace('{{CM_MAIN}}', '')
    s = s.replace('{{CM_TOC_CATEGORIES}}', toc_category_string)

    # Output
    output_dir = i.get('output_dir','')

    if output_dir == '': output_dir = '..'

    output_file = os.path.join(output_dir, list_file)

    r = utils.save_txt(output_file, s)
    if r['return']>0: return r

    return {'return':0}


############################################################
def dockerfile(i):
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

    self_module = i['self_module']

    cur_dir = os.getcwd()

    console = i.get('out') == 'con'
    cm_repo = i.get('cm_repo', 'mlcommons@ck')

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

    ii = utils.sub_input(i, self_module.cmind.cfg['artifact_keys'] + ['tags'])

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

    script_meta = {}
    urls = {}

    if i.get("all_os"):
        docker_os = {
            "ubuntu": ["18.04","20.04","22.04"],
            "rhel": ["9"]
        }
    else:
        docker_os = {}
        if i.get('docker_os'):
            docker_os[i['docker_os']] = []
        if i.get('docker_os_version'):
            docker_os[i['docker_os']] = [i.get('docker_os_version')]
        else:
            if docker_os == "ubuntu":
                docker_os["ubuntu"] = ["22.04"]

        if not docker_os:
          docker_os = {
            "ubuntu": ["22.04"],
          }

    for artifact in sorted(lst, key = lambda x: x.meta.get('alias','')):

        meta = artifact.meta
        script_path = artifact.path
        tags = meta.get("tags", [])
        tag_string=",".join(tags)

        for _os in docker_os:
            for version in docker_os[_os]:
                dockerfile_path = os.path.join(script_path,'dockerfiles', _os +'_'+version +'.Dockerfile')
                if i.get('print_deps'):
                  cm_input = {'action': 'run',
                            'automation': 'script',
                            'tags': f'{tag_string}',
                            'print_deps': True,
                            'quiet': True,
                            'silent': True,
                            'fake_run': True
                            }
                  r = self_module.cmind.access(cm_input)
                  if r['return'] > 0:
                    return r
                  print_deps = r['new_state']['print_deps']
                  comments = [ "#RUN " + dep for dep in print_deps ]
                  comments.append("")
                  comments.append("# Run CM workflow")
                else:
                  comments = []

                cm_docker_input = {'action': 'run',
                            'automation': 'script',
                            'tags': 'build,dockerfile',
                            'cm_repo': cm_repo,
                            'docker_os': _os,
                            'docker_os_version': version,
                            'file_path': dockerfile_path,
                            'comments': comments,
                            'run_cmd': f'cm run script --tags={tag_string} --quiet',
                            'script_tags': f'{tag_string}',
                            'quiet': True,
                            'print_deps': True,
                            'real_run': True
                            }

                r = self_module.cmind.access(cm_docker_input)
                if r['return'] > 0:
                    return r

                print("Dockerfile generated at "+dockerfile_path)

    return {'return':0}

############################################################
def docker(i):
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

    self_module = i['self_module']

    r = utils.call_internal_module(self_module, __file__, 'module_misc', 'dockerfile', i)
    if r['return']>0: return r

    cur_dir = os.getcwd()

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

    ii = utils.sub_input(i, self_module.cmind.cfg['artifact_keys'] + ['tags'])

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

    script_meta = {}
    urls = {}

    for artifact in sorted(lst, key = lambda x: x.meta.get('alias','')):

        meta = artifact.meta
        script_path = artifact.path
        tags = meta.get("tags", [])
        script_alias = meta.get('alias')
        tag_string=",".join(tags)

        _os=i.get('docker_os', 'ubuntu')
        version=i.get('docker_os_version', '22.04')

        dockerfile_path = os.path.join(script_path,'dockerfiles', _os +'_'+version +'.Dockerfile')

        cm_docker_input = {'action': 'run',
                            'automation': 'script',
                            'tags': 'run,docker,container',
                            'recreate': 'yes',
                            'docker_os': _os,
                            'image_repo': 'cm',
                            'image_tag': script_alias,
                            'docker_os_version': version,
                            'detached': 'no',
                            'script_tags': f'{tag_string}',
                            'quiet': True,
                            'real_run': True,
                            'add_deps_recursive': {
                                'build-docker-image': {
                                    'dockerfile': dockerfile_path
                                }
                            }
                        }

        r = self_module.cmind.access(cm_docker_input)
        if r['return'] > 0:
            return r


    return {'return':0}
