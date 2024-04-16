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

    public_taskforce = '[Public MLCommons Task Force on Automation and Reproducibility](https://github.com/mlcommons/ck/blob/master/docs/taskforce.md)'

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

        path = artifact.path
        meta = artifact.meta
        original_meta = artifact.original_meta

        print ('Documenting {}'.format(path))

        alias = meta.get('alias','')
        uid = meta.get('uid','')

        script_meta[alias] = meta

        name = meta.get('name','')
        developers = meta.get('developers','')

        # Check if has tags help otherwise all tags
        tags = meta.get('tags_help','').strip()
        if tags=='':
            tags = meta.get('tags',[])
        else:
            tags = tags.split(' ')

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
            url_repo = 'https://github.com/mlcommons/ck/tree/dev/cm/cmind/repo'
            url = url_repo+'/script/'
        elif '@' in repo_alias:
            url_repo = 'https://github.com/'+repo_alias.replace('@','/')+'/tree/dev'
            if repo_meta.get('prefix','')!='': url_repo+='/'+repo_meta['prefix']
            url = url_repo+ '/script/'

        if url!='':
            url+=alias

        urls[alias]=url

        # Check if there is about doc
        path_readme = os.path.join(path, 'README.md')
        path_readme_extra = os.path.join(path, 'README-extra.md')
        path_readme_about = os.path.join(path, 'README-about.md')

        readme_about = ''
        if os.path.isfile(path_readme_about):
            r = utils.load_txt(path_readme_about, split = True)
            if r['return']>0: return 
        
            s = r['string']
            readme_about = r['list']

        
        #######################################################################
        # Start automatically generated README
        md_script_readme = [
#                            '<details>',
#                            '<summary>Click here to see the table of contents.</summary>',
#                            '{{CM_README_TOC}}',
#                            '</details>',
#                            '',
                            '**Note that this script is archived and moved [here](https://github.com/mlcommons/cm4mlops/tree/main/script/{}).**'.format(meta['alias']),
                            '',
                            '',
                            '',
                            'Automatically generated README for this automation recipe: **{}**'.format(meta['alias']), 
                            ]


        md_script.append('## '+alias)
        md_script.append('')

#        x = 'About'
#        md_script_readme.append('___')
#        md_script_readme.append('### '+x)
#        md_script_readme.append('')
#        toc_readme.append(x)

#        x = 'About'
#        md_script_readme.append('#### '+x)
#        md_script_readme.append('')
#        toc_readme.append(' '+x)

        if name!='':
            name += '.'
            md_script.append('*'+name+'*')
            md_script.append('')

#            md_script_readme.append('*'+name+'*')
#            md_script_readme.append('')
        
        
            
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
        


        if category!='':
            md_script_readme.append('')
            md_script_readme.append('Category: **{}**'.format(category))
                            
        md_script_readme.append('')
        md_script_readme.append('License: **Apache 2.0**')

        
        md_script_readme.append('')

        if developers == '':
            md_script_readme.append('Maintainers: ' + public_taskforce)
        else:
            md_script_readme.append('Developers: ' + developers)

        x = '* [{}]({})'.format(alias, url)
        if name !='': x+=' *('+name+')*'
        toc.append(x)
        

        
        cm_readme_extra = '[ [Online info and GUI to run this CM script](https://access.cknowledge.org/playground/?action=scripts&name={},{}) ] '.format(alias, uid)

        if os.path.isfile(path_readme_extra):
            readme_extra_url = url+'/README-extra.md'

            x = '* Notes from the authors, contributors and users: [*GitHub*]({})'.format(readme_extra_url)
            md_script.append(x)

            cm_readme_extra += '[ [Notes from the authors, contributors and users](README-extra.md) ] '

        md_script_readme.append('')
        md_script_readme.append('---')
        md_script_readme.append('*'+cm_readme_extra.strip()+'*')


        if readme_about!='':
            md_script_readme += ['', '---', ''] + readme_about



        x = 'Summary'
        md_script_readme.append('')
        md_script_readme.append('---')
        md_script_readme += [
#                             '<details>',
#                             '<summary>Click to see the summary</summary>',
                             '#### Summary',
                             ''
                            ]
        toc_readme.append(x)

        
#        if category != '':
#            x = 'Category'
#            md_script_readme.append('___')
#            md_script_readme.append('#### '+x)
#            md_script_readme.append(' ')
#            md_script_readme.append(category+'.')
#            toc_readme.append(x)

#            x = '* Category: *{}*'.format(category + '.')
#            md_script_readme.append(x)


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
            variation_pointer2="[variations]"
        else:
            variation_pointer=''
            variation_pointer2=''

        if len(input_mapping)>0:
            input_mapping_pointer="[--input_flags]"
        else:
            input_mapping_pointer=''
        
        cli_all_tags = '`cm run script --tags={}`'.format(','.join(tags))
        cli_all_tags3 = '`cm run script --tags={}{} {}`'.format(','.join(tags), variation_pointer, input_mapping_pointer)
        x = '* CM CLI with all tags: {}*'.format(cli_all_tags)
        md_script.append(x)

        cli_help_tags_alternative = '`cmr "{}" --help`'.format(' '.join(tags))

        cli_all_tags_alternative = '`cmr "{}"`'.format(' '.join(tags))
        cli_all_tags_alternative3 = '`cmr "{} {}" {}`'.format(' '.join(tags), variation_pointer2, input_mapping_pointer)
        cli_all_tags_alternative_j = '`cmr "{} {}" {} -j`'.format(' '.join(tags), variation_pointer, input_mapping_pointer)
        x = '* CM CLI alternative: {}*'.format(cli_all_tags_alternative)
        md_script.append(x)

        cli_all_tags_alternative_docker = '`cm docker script "{}{}" {}`'.format(' '.join(tags), variation_pointer2, input_mapping_pointer)


#        cli_uid = '`cm run script {} {}`'.format(meta['uid'], input_mapping_pointer)
#        x = '* CM CLI with alias and UID: {}*'.format(cli_uid)
#        md_script.append(x)

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
        md_script_readme.append('* All CM tags to find and reuse this script (see in above meta description): *{}*'.format(','.join(tags)))
#        md_script_readme.append('')
#        toc_readme.append(x)


        cache = meta.get('cache', False)
        md_script_readme.append('* Output cached? *{}*'.format(str(cache)))

        md_script_readme.append('* See [pipeline of dependencies]({}) on other CM scripts'.format('#dependencies-on-other-cm-scripts'))

        md_script_readme += ['',
#                             '</details>'
                             ]

        
        
        # Add usage
        x1 = 'Reuse this script in your project'
        x1a = 'Install MLCommons CM automation meta-framework'
        x1aa = 'Pull CM repository with this automation recipe (CM script)'
        x1b = 'Print CM help from the command line'
        x2 = 'Customize and run this script from the command line with different variations and flags'
        x3 = 'Run this script from Python'
        x3a = 'Run this script via GUI'
        x4 = 'Run this script via Docker (beta)'
        md_script_readme += [
                             '',
                             '---',
                             '### '+x1,
                             '',
                             '#### '+x1a,
                             '',
                             '* [Install CM](https://access.cknowledge.org/playground/?action=install)',
                             '* [CM Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)',
                             '',
                             '#### '+x1aa,
                             '',
                             '```cm pull repo {}```'.format(repo_alias),
                             '',
                             '#### '+x1b,
                             '',
                             '```{}```'.format(cli_help_tags_alternative),
                             '',
                             '#### '+x2,
                             '',
                             '{}'.format(cli_all_tags),
                             '',
                             '{}'.format(cli_all_tags3),
                             '',
                             '*or*',
                             '',
                             '{}'.format(cli_all_tags_alternative),
                             '',
                             '{}'.format(cli_all_tags_alternative3),
                             '',
#                             '3. {}'.format(cli_uid),
                             '']

        
        x = ' and check the [Gettings Started Guide](https://github.com/mlcommons/ck/blob/dev/docs/getting-started.md) for more details.'
        if len(variation_keys)>0:
            md_script_readme += ['* *See the list of `variations` [here](#variations)'+x+'*',
                                 ''
                                 ]

        if input_description and len(input_description)>0:
            x = 'Input Flags'
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

                md_script_readme.append('* --**{}**={}'.format(key,desc))

            md_script_readme.append('')
            md_script_readme.append('**Above CLI flags can be used in the Python CM API as follows:**')
            md_script_readme.append('')

            x = '```python\nr=cm.access({... , "'+key0+'":...}\n```'
            md_script_readme.append(x)

        
        
        
        
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
                             '```cmr "cm gui" --script="'+','.join(tags)+'"```',
                             '',
                             'Use this [online GUI](https://cKnowledge.org/cm-gui/?tags={}) to generate CM CMD.'.format(','.join(tags)),
                             '',
                             '#### '+x4,
                             '',
                             '{}'.format(cli_all_tags_alternative_docker),
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



        
        
        # Check input flags
        if input_mapping and len(input_mapping)>0:
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
        x = 'Dependencies on other CM scripts'
        md_script_readme += ['___',
                             '### '+x,
                             '']
        toc_readme.append(x)

#        md_script_readme.append('<details>')
#        md_script_readme.append('<summary>Click here to expand this section.</summary>')

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
 #       md_script_readme.append('</details>')
        md_script_readme.append('')
                    
        # New environment
        new_env_keys = meta.get('new_env_keys',[])

        x = 'Script output'
        md_script_readme.append('___')
        md_script_readme.append('### '+x)
        toc_readme.append(x)

        md_script_readme.append(cli_all_tags_alternative_j)

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
#        x = 'Maintainers'
#        md_script_readme.append('___')
#        md_script_readme.append('### '+x)
#        md_script_readme.append('')
#        md_script_readme.append('* ' + public_taskforce)
#        toc_readme.append(x)

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
#        s = s.replace('{{CM_SEE_README_EXTRA}}', cm_see_readme_extra)
        s = s.replace('{{CM_README_TOC}}', toc_readme_string)
        
        r = utils.save_txt(path_readme, s)
        if r['return']>0: return r

        # Add to Git (if in git)
        os.chdir(path)
        os.system('git add README.md')
        os.chdir(cur_dir)


    # Recreate TOC with categories
    toc2 = []

    for category in sorted(toc_category):#, key = lambda x: -toc_category_sort[x]):
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



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def update_path_for_docker(path, mounts, force_path_target=''):

    path_orig = ''
    path_target = ''
    
    if path!='': # and (os.path.isfile(path) or os.path.isdir(path)):
        path = os.path.abspath(path)

        path_target = path
        path_orig = path

        if os.name == 'nt':
            from pathlib import PureWindowsPath, PurePosixPath
    
            x = PureWindowsPath(path_orig)
            path_target = str(PurePosixPath('/', *x.parts[1:]))

        if not path_target.startswith('/'): path_target='/'+path_target

        path_target='/cm-mount'+path_target if force_path_target=='' else force_path_target

        # If file, mount directory
        if os.path.isfile(path) or not os.path.isdir(path):
            x = os.path.dirname(path_orig) + ':' + os.path.dirname(path_target)
        else:
            x = path_orig + ':' + path_target

        # CHeck if no duplicates
        to_add = True
        for y in mounts:
            if y.lower()==x.lower():
                to_add = False
                break

        if to_add:
            mounts.append(x)

    
    return (path_orig, path_target)

############################################################
def process_inputs(i):

    import copy
    
    i_run_cmd_arc = i['run_cmd_arc']
    docker_settings = i['docker_settings']
    mounts = i['mounts']
    
    # Check if need to update/map/mount inputs and env
    i_run_cmd = copy.deepcopy(i_run_cmd_arc)

            
    def get_value_using_key_with_dots(d, k):
        v = None
        j = k.find('.')
        if j>=0:
            k1 = k[:j]
            k2 = k[j+1:]

            if k1 in d:
                v = d[k1]

                if '.' in k2:
                    v, d, k = get_value_using_key_with_dots(v, k2)
                else:
                    d = v
                    k = k2
                    if type(v)==dict:
                        v = v.get(k2)
                    else:
                        v = None
        else:
            if k == '':
                v = d
            else:
                v = d.get(k)

        return v, d, k
    
    docker_input_paths = docker_settings.get('input_paths',[])
    if len(i_run_cmd)>0:
        for k in docker_input_paths:
            v2, i_run_cmd2, k2 = get_value_using_key_with_dots(i_run_cmd, k)

            if v2!=None:
                v=i_run_cmd2[k2]

                path_orig, path_target = update_path_for_docker(v, mounts)

                if path_target!='':
                    i_run_cmd2[k2] = path_target
    
    return {'return':0, 'run_cmd':i_run_cmd}


############################################################
def regenerate_script_cmd(i):

    script_uid = i['script_uid']
    script_alias = i['script_alias']
    tags = i['tags']
    docker_settings = i['docker_settings']
    fake_run = i.get('fake_run', False)

    i_run_cmd = i['run_cmd']

    docker_run_cmd_prefix = i['docker_run_cmd_prefix']

    # Regenerate command from dictionary input
    run_cmd = 'cm run script'

    x = ''

    # Check if there are some tags without variation
    requested_tags = i_run_cmd.get('tags', [])

    tags_without_variation = False
    for t in requested_tags:
        if not t.startswith('_'):
            tags_without_variation = True
            break

    if not tags_without_variation:
        # If no tags without variation, add script alias and UID explicitly
        if script_uid!='': x=script_uid
        if script_alias!='':
            if x!='': x=','+x
            x = script_alias+x

    if x!='':
        run_cmd += ' ' + x + ' '


    skip_input_for_fake_run = docker_settings.get('skip_input_for_fake_run', [])
    add_quotes_to_keys = docker_settings.get('add_quotes_to_keys', [])
    

    def rebuild_flags(i_run_cmd, fake_run, skip_input_for_fake_run, add_quotes_to_keys, key_prefix):

        run_cmd = ''

        keys = list(i_run_cmd.keys())

        if 'tags' in keys:
            # Move tags first
            tags_position = keys.index('tags')
            del(keys[tags_position])
            keys = ['tags']+keys
        
        for k in keys:
            # Assemble long key if dictionary
            long_key = key_prefix
            if long_key!='': long_key+='.'
            long_key+=k

            if fake_run and long_key in skip_input_for_fake_run:
                continue    

            v = i_run_cmd[k]
            
            q = '\\"' if long_key in add_quotes_to_keys else ''
            
            if type(v)==dict:
                run_cmd += rebuild_flags(v, fake_run, skip_input_for_fake_run, add_quotes_to_keys, long_key)
            elif type(v)==list:
                x = ''
                for vv in v:
                    if x != '': x+=','
                    x+=q+str(vv)+q
                run_cmd+=' --'+long_key+',=' + x
            else:
                run_cmd+=' --'+long_key+'='+q+str(v)+q

        return run_cmd

    run_cmd += rebuild_flags(i_run_cmd, fake_run, skip_input_for_fake_run, add_quotes_to_keys, '')

    run_cmd = docker_run_cmd_prefix + ' && ' + run_cmd if docker_run_cmd_prefix!='' else run_cmd

    return {'return':0, 'run_cmd_string':run_cmd}



############################################################
def aux_search(i):

    self_module = i['self_module']

    inp = i['input']

    repos = inp.get('repos','')
# Grigori Fursin remarked on 20240412 because this line prevents 
# from searching for scripts in other public or private repositories.
# Not sure why we enforce just 2 repositories
# 
#    if repos == '': repos='internal,a4705959af8e447a'

    parsed_artifact = inp.get('parsed_artifact',[])

    if len(parsed_artifact)<1:
        parsed_artifact = [('',''), ('','')]
    elif len(parsed_artifact)<2:
        parsed_artifact.append(('',''))
    else:
        repos = parsed_artifact[1][0]

    list_of_repos = repos.split(',') if ',' in repos else [repos]

    ii = utils.sub_input(inp, self_module.cmind.cfg['artifact_keys'] + ['tags'])

    ii['out'] = None

    # Search for automations in repos
    lst = []
    for repo in list_of_repos:
        parsed_artifact[1] = ('',repo) if utils.is_cm_uid(repo) else (repo,'')
        ii['parsed_artifact'] = parsed_artifact
        r = self_module.search(ii)
        if r['return']>0: return r
        lst += r['list']

    return {'return':0, 'list':lst}


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

    import copy

    # Check simplified CMD: cm docker script "python app image-classification onnx"
    # If artifact has spaces, treat them as tags!
    self_module = i['self_module']
    self_module.cmind.access({'action':'detect_tags_in_artifact', 'automation':'utils', 'input':i})

    # Prepare "clean" input to replicate command
    r = self_module.cmind.access({'action':'prune_input', 'automation':'utils', 'input':i, 'extra_keys_starts_with':['docker_']})
    i_run_cmd_arc = r['new_input']

    cur_dir = os.getcwd()

    quiet = i.get('quiet', False)

    console = i.get('out') == 'con'

    cm_repo = i.get('docker_cm_repo', 'mlcommons@ck')
    cm_repo_flags = i.get('docker_cm_repo_flags', '')

    # Search for script(s)
    r = aux_search({'self_module': self_module, 'input': i})
    if r['return']>0: return r

    lst = r['list']

    if len(lst)==0:
        return {'return':1, 'error':'no scripts were found'}




#    if i.get('cmd'):
#        run_cmd = "cm run script " + " ".join( a for a in i['cmd'] if not a.startswith('--docker_') )
#    elif i.get('artifact'):
#        run_cmd = "cm run script "+i['artifact']
#    elif i.get('tags'):
#        run_cmd = "cm run script \""+" "+" ".join(i['tags']) + "\""
#    else:
#        run_cmd = ""
#
#    run_cmd = i.get('docker_run_cmd_prefix') + ' && ' + run_cmd if i.get('docker_run_cmd_prefix') else run_cmd





    env=i.get('env', {})
    state = i.get('state', {})
    script_automation = i['self_module']

    dockerfile_env=i.get('dockerfile_env', {})
    dockerfile_env['CM_RUN_STATE_DOCKER'] = True

    tags_split = i.get('tags', '').split(",")
    variation_tags = [ t[1:] for t in tags_split if t.startswith("_") ]

    for artifact in sorted(lst, key = lambda x: x.meta.get('alias','')):

        meta = artifact.meta

        script_path = artifact.path

        tags = meta.get("tags", [])
        tag_string=",".join(tags)

        script_alias = meta.get('alias', '')
        script_uid = meta.get('uid', '')


        variations = meta.get('variations', {})
        docker_settings = meta.get('docker', {})
        state['docker'] = docker_settings

        r = script_automation._update_state_from_variations(i, meta, variation_tags, variations, env, state, deps = [], post_deps = [], prehook_deps = [], posthook_deps = [], new_env_keys_from_meta = [], new_state_keys_from_meta = [], add_deps_recursive = {}, run_state = {}, recursion_spaces='', verbose = False)
        if r['return'] > 0:
            return r

        docker_settings = state['docker']

        if not docker_settings.get('run', True):
            print("docker.run set to False in _cm.json")
            continue
        '''run_config_path = os.path.join(script_path,'run_config.yml')
        if not os.path.exists(run_config_path):
            print("No run_config.yml file present in {}".format(script_path))
            continue
        import yaml
        with open(run_config_path, 'r') as run_config_file:
            run_config = yaml.safe_load(run_config_file)
        docker_settings = run_config.get('docker')
        if not docker_settings or not docker_settings.get('build') or not run_config.get('run_with_default_inputs'):
            print("Run config is not configured for docker run in {}".format(run_config_path))
            continue
        '''

        # Check if need to update/map/mount inputs and env
        r = process_inputs({'run_cmd_arc': i_run_cmd_arc,
                            'docker_settings': docker_settings,
                            'mounts':[]})
        if r['return']>0: return r

        i_run_cmd = r['run_cmd']

        docker_run_cmd_prefix = i.get('docker_run_cmd_prefix', docker_settings.get('run_cmd_prefix', ''))

        r = regenerate_script_cmd({'script_uid':script_uid,
                                   'script_alias':script_alias,
                                   'run_cmd':i_run_cmd,
                                   'tags':tags,
                                   'fake_run':True,
                                   'docker_settings':docker_settings,
                                   'docker_run_cmd_prefix':docker_run_cmd_prefix})
        if r['return']>0: return r

        run_cmd  = r['run_cmd_string']


        docker_base_image = i.get('docker_base_image', docker_settings.get('base_image'))
        docker_os = i.get('docker_os', docker_settings.get('docker_os', 'ubuntu'))
        docker_os_version = i.get('docker_os_version', docker_settings.get('docker_os_version', '22.04'))

        docker_cm_repos = i.get('docker_cm_repos', docker_settings.get('cm_repos', ''))

        docker_extra_sys_deps = i.get('docker_extra_sys_deps', '')

        if not docker_base_image:
            dockerfilename_suffix = docker_os +'_'+docker_os_version
        else:
            if os.name == 'nt':
                dockerfilename_suffix = docker_base_image.replace('/', '-').replace(':','-')
            else:
                dockerfilename_suffix = docker_base_image.split("/")
                dockerfilename_suffix = dockerfilename_suffix[len(dockerfilename_suffix) - 1]

        fake_run_deps = i.get('fake_run_deps', docker_settings.get('fake_run_deps', False))
        docker_run_final_cmds = docker_settings.get('docker_run_final_cmds', [])

        r = check_gh_token(i, docker_settings, quiet)
        if r['return'] >0 : return r
        gh_token = r['gh_token']
        i['docker_gh_token'] = gh_token # To pass to docker function if needed

        if i.get('docker_real_run', docker_settings.get('docker_real_run',False)):
            fake_run_option = " "
            fake_run_deps = False
        else:
            fake_run_option = " --fake_run"

        docker_copy_files = i.get('docker_copy_files', docker_settings.get('copy_files', []))

        env['CM_DOCKER_PRE_RUN_COMMANDS'] = docker_run_final_cmds

        docker_path = i.get('docker_path', '').strip()
        if docker_path == '': 
            docker_path = script_path

        dockerfile_path = os.path.join(docker_path, 'dockerfiles', dockerfilename_suffix +'.Dockerfile')

        if i.get('print_deps'):
            cm_input = {'action': 'run',
                    'automation': 'script',
                    'tags': f'{tag_string}',
                    'print_deps': True,
                    'quiet': True,
                    'silent': True,
                    'fake_run': True,
                    'fake_deps': True
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
                           'cm_repo_flags': cm_repo_flags,
                           'docker_base_image': docker_base_image,
                           'docker_os': docker_os,
                           'docker_os_version': docker_os_version,
                           'file_path': dockerfile_path,
                           'fake_run_option': fake_run_option,
                           'comments': comments,
                           'run_cmd': f'{run_cmd} --quiet',
                           'script_tags': f'{tag_string}',
                           'copy_files': docker_copy_files,
                           'quiet': True,
                           'env': env,
                           'dockerfile_env': dockerfile_env,
                           'v': i.get('v', False),
                           'fake_docker_deps': fake_run_deps,
                           'print_deps': True,
                           'real_run': True
                          }

        if docker_cm_repos != '':
            cm_docker_input['cm_repos'] = docker_cm_repos

        if gh_token != '':
            cm_docker_input['gh_token'] = gh_token

        if docker_extra_sys_deps != '':
            cm_docker_input['extra_sys_deps'] = docker_extra_sys_deps

        r = self_module.cmind.access(cm_docker_input)
        if r['return'] > 0:
            return r

        print ('')
        print ("Dockerfile generated at " + dockerfile_path)

    return {'return':0}

def get_container_path(value):
    path_split = value.split(os.sep)
    if len(path_split) == 1:
        return value

    new_value = ''
    if "cache" in path_split and "local" in path_split:
        new_path_split = [ "", "home", "cmuser" ]
        repo_entry_index = path_split.index("local")
        new_path_split += path_split[repo_entry_index:]
        return "/".join(new_path_split)

    return value


############################################################
def docker(i):
    """
    CM automation to run CM scripts via Docker

    Args:
      (CM input dict):

      (out) (str): if 'con', output to console

      (docker_path) (str): where to create or find Dockerfile
      (docker_gh_token) (str): GitHub token for private repositories
      (docker_save_script) (str): if !='' name of script to save docker command

    Returns:
      (CM return dict):

      * return (int): return code == 0 if no error and >0 if error
      * (error) (str): error string if return>0

    """

    import copy
    import re

    quiet = i.get('quiet', False)

    detached = i.get('docker_detached', '')
    if detached=='':
        detached = i.get('docker_dt', '')
    if detached=='':
        detached='no'

    interactive = i.get('docker_interactive', '')
    if interactive == '':
        interactive = i.get('docker_it', '')

    verbose = i.get('v', False)
    show_time = i.get('show_time', False)

    # Check simplified CMD: cm docker script "python app image-classification onnx"
    # If artifact has spaces, treat them as tags!
    self_module = i['self_module']
    self_module.cmind.access({'action':'detect_tags_in_artifact', 'automation':'utils', 'input':i})

    # Prepare "clean" input to replicate command
    r = self_module.cmind.access({'action':'prune_input', 'automation':'utils', 'input':i, 'extra_keys_starts_with':['docker_']})
    i_run_cmd_arc = r['new_input']

    noregenerate_docker_file = i.get('docker_noregenerate', False)

    if not noregenerate_docker_file:
        r = utils.call_internal_module(self_module, __file__, 'module_misc', 'dockerfile', i)
        if r['return']>0: return r

    cur_dir = os.getcwd()

    console = i.get('out') == 'con'

    # Search for script(s)
    r = aux_search({'self_module': self_module, 'input': i})
    if r['return']>0: return r

    lst = r['list']

    if len(lst)==0:
        return {'return':1, 'error':'no scripts were found'}

    env=i.get('env', {})
    env['CM_RUN_STATE_DOCKER'] = False
    script_automation = i['self_module']
    state = i.get('state', {})

    tags_split = i.get('tags', '').split(",")
    variation_tags = [ t[1:] for t in tags_split if t.startswith("_") ]

    docker_cache = i.get('docker_cache', "yes")
    if docker_cache in ["no", False, "False" ]:
        if 'CM_DOCKER_CACHE' not in env:
            env['CM_DOCKER_CACHE'] = docker_cache

    image_repo = i.get('docker_image_repo','')
    if image_repo == '':
        image_repo = 'cknowledge'

    for artifact in sorted(lst, key = lambda x: x.meta.get('alias','')):

        meta = artifact.meta

        if i.get('help',False):
            return utils.call_internal_module(self_module, __file__, 'module_help', 'print_help', {'meta':meta, 'path':artifact.path})

        script_path = artifact.path

        tags = meta.get("tags", [])
        tag_string=",".join(tags)

        script_alias = meta.get('alias', '')
        script_uid = meta.get('uid', '')


        mounts = copy.deepcopy(i.get('docker_mounts', []))

        '''run_config_path = os.path.join(script_path,'run_config.yml')
        if not os.path.exists(run_config_path):
            print("No run_config.yml file present in {}".format(script_path))
            continue
        import yaml
        with open(run_config_path, 'r') as run_config_file:
            run_config = yaml.safe_load(run_config_file)
        '''

        variations = meta.get('variations', {})
        docker_settings = meta.get('docker', {})
        state['docker'] = docker_settings

        r = script_automation._update_state_from_variations(i, meta, variation_tags, variations, env, state, deps = [], post_deps = [], prehook_deps = [], posthook_deps = [], new_env_keys_from_meta = [], new_state_keys_from_meta = [], add_deps_recursive = {}, run_state = {}, recursion_spaces='', verbose = False)
        if r['return'] > 0:
            return r

        docker_settings = state['docker']

        if not docker_settings.get('run', True):
            print("docker.run set to False in _cm.json")
            continue
        '''
        if not docker_settings or not docker_settings.get('build') or not run_config.get('run_with_default_inputs'):
            print("Run config is not configured for docker run in {}".format(run_config_path))
            continue
        '''

        # Check if need to update/map/mount inputs and env
        r = process_inputs({'run_cmd_arc': i_run_cmd_arc,
                            'docker_settings': docker_settings,
                            'mounts':mounts})
        if r['return']>0: return r

        i_run_cmd = r['run_cmd']

        # Check if need to mount home directory
        current_path_target = '/cm-mount/current'
        if docker_settings.get('mount_current_dir','')=='yes':
            update_path_for_docker('.', mounts, force_path_target=current_path_target)


        _os = i.get('docker_os', docker_settings.get('docker_os', 'ubuntu'))
        version = i.get('docker_os_version', docker_settings.get('docker_os_version', '22.04'))

        deps = docker_settings.get('deps', [])
        if deps:
            # Todo: Support state, const and add_deps_recursive
            run_state = {'deps':[], 'fake_deps':[], 'parent': None}
            run_state['script_id'] = script_alias + "," + script_uid
            run_state['script_variation_tags'] = variation_tags
            r = script_automation._run_deps(deps, [], env, {}, {}, {}, {}, '', {}, '', False, '', verbose, show_time, ' ', run_state)
            if r['return'] > 0:
                return r

        for key in docker_settings.get('mounts', []):
            mounts.append(key)

        # Updating environment variables from CM input based on input_mapping from meta
        input_mapping = meta.get('input_mapping', {})

        for c_input in input_mapping:
            if c_input in i:
                env[input_mapping[c_input]] = i[c_input]

        # Updating environment variables from CM input based on docker_input_mapping from meta

        docker_input_mapping = docker_settings.get('docker_input_mapping', {})

        for c_input in docker_input_mapping:
            if c_input in i:
                env[docker_input_mapping[c_input]] = i[c_input]

        container_env_string = '' # env keys corresponding to container mounts are explicitly passed to the container run cmd
        for index in range(len(mounts)):
            mount = mounts[index]

            # Since windows may have 2 :, we search from the right
            j = mount.rfind(':')
            if j>0:
                mount_parts = [mount[:j], mount[j+1:]]
            else:
                return {'return':1, 'error': 'Can\'t find separator : in a mount string: {}'.format(mount)}

#            mount_parts = mount.split(":")
#            if len(mount_parts) != 2:
#                return {'return': 1, 'error': f'Invalid mount specified in docker settings'}

            host_mount = mount_parts[0]
            new_host_mount = host_mount
            container_mount = mount_parts[1]
            new_container_mount = container_mount

            tmp_values = re.findall(r'\${{ (.*?) }}', str(host_mount))
            skip = False
            if tmp_values:
                for tmp_value in tmp_values:
                    if tmp_value in env:
                        new_host_mount = env[tmp_value]
                    else:# we skip those mounts
                        mounts[index] = None
                        skip = True
                        break

            tmp_values = re.findall(r'\${{ (.*?) }}', str(container_mount))
            if tmp_values:
                for tmp_value in tmp_values:
                    if tmp_value in env:
                        new_container_mount = get_container_path(env[tmp_value])
                        container_env_string += " --env.{}={} ".format(tmp_value, new_container_mount)
                    else:# we skip those mounts
                        mounts[index] = None
                        skip = True
                        break

            if skip:
                continue
            mounts[index] = new_host_mount+":"+new_container_mount

        mounts = list(filter(lambda item: item is not None, mounts))

        mount_string = "" if len(mounts)==0 else ",".join(mounts)

        #check for proxy settings and pass onto the docker
        proxy_keys = [ "ftp_proxy", "FTP_PROXY", "http_proxy", "HTTP_PROXY", "https_proxy", "HTTPS_PROXY", "no_proxy", "NO_PROXY", "socks_proxy", "SOCKS_PROXY", "GH_TOKEN" ]

        if env.get('+ CM_DOCKER_BUILD_ARGS', []) == []:
            env['+ CM_DOCKER_BUILD_ARGS'] = []

        for key in proxy_keys:
            if os.environ.get(key, '') != '':
                value = os.environ[key]
                container_env_string += " --env.{}={} ".format(key, value)
                env['+ CM_DOCKER_BUILD_ARGS'].append("{}={}".format(key, value))

        docker_use_host_group_id = i.get('docker_use_host_group_id', docker_settings.get('use_host_group_id'))
        if docker_use_host_group_id and os.name != 'nt':
            env['+ CM_DOCKER_BUILD_ARGS'].append("{}={}".format('CM_ADD_DOCKER_GROUP_ID', '\\"-g $(id -g $USER) -o\\"'))

        docker_base_image = i.get('docker_base_image', docker_settings.get('base_image'))
        docker_os = i.get('docker_os', docker_settings.get('docker_os', 'ubuntu'))
        docker_os_version = i.get('docker_os_version', docker_settings.get('docker_os_version', '22.04'))

        if not docker_base_image:
            dockerfilename_suffix = docker_os +'_'+docker_os_version
        else:
            if os.name == 'nt':
                dockerfilename_suffix = docker_base_image.replace('/', '-').replace(':','-')
            else:
                dockerfilename_suffix = docker_base_image.split("/")
                dockerfilename_suffix = dockerfilename_suffix[len(dockerfilename_suffix) - 1]


        cm_repo=i.get('docker_cm_repo', 'mlcommons@ck')

        docker_path = i.get('docker_path', '').strip()
        if docker_path == '': 
            docker_path = script_path

        dockerfile_path = os.path.join(docker_path, 'dockerfiles', dockerfilename_suffix +'.Dockerfile')

        docker_skip_run_cmd = i.get('docker_skip_run_cmd', docker_settings.get('skip_run_cmd', False)) #skips docker run cmd and gives an interactive shell to the user

        docker_pre_run_cmds = i.get('docker_pre_run_cmds', []) +  docker_settings.get('pre_run_cmds', [])

        docker_run_cmd_prefix = i.get('docker_run_cmd_prefix', docker_settings.get('run_cmd_prefix', ''))

        all_gpus = i.get('docker_all_gpus', docker_settings.get('all_gpus'))

        device = i.get('docker_device', docker_settings.get('device'))

        r = check_gh_token(i, docker_settings, quiet)
        if r['return'] >0 : return r
        gh_token = r['gh_token']


        port_maps = i.get('docker_port_maps', docker_settings.get('port_maps', []))

        shm_size = i.get('docker_shm_size', docker_settings.get('shm_size', ''))

        extra_run_args = i.get('docker_extra_run_args', docker_settings.get('extra_run_args', ''))

        if detached == '':
            detached = docker_settings.get('detached', '')

        if interactive == '':
            interactive = docker_settings.get('interactive', '')

#        # Regenerate run_cmd
#        if i.get('cmd'):
#            run_cmd = "cm run script " + " ".join( a for a in i['cmd'] if not a.startswith('--docker_') )
#        elif i.get('artifact'):
#            run_cmd = "cm run script "+i['artifact']
#        elif i.get('tags'):
#            run_cmd = "cm run script \""+" "+" ".join(i['tags']) + "\""
#        else:
#            run_cmd = ""



        r = regenerate_script_cmd({'script_uid':script_uid,
                                   'script_alias':script_alias,
                                   'tags':tags,
                                   'run_cmd':i_run_cmd,
                                   'docker_settings':docker_settings,
                                   'docker_run_cmd_prefix':i.get('docker_run_cmd_prefix','')})
        if r['return']>0: return r

        run_cmd  = r['run_cmd_string'] + ' ' + container_env_string + ' --docker_run_deps '

        env['CM_RUN_STATE_DOCKER'] = True

        if docker_settings.get('mount_current_dir','')=='yes':
            run_cmd = 'cd '+current_path_target+' && '+run_cmd

        final_run_cmd = run_cmd if docker_skip_run_cmd not in [ 'yes', True, 'True' ] else 'cm version'

        print ('')
        print ('CM command line regenerated to be used inside Docker:')
        print ('')
        print (final_run_cmd)
        print ('')


        cm_docker_input = {'action': 'run',
                           'automation': 'script',
                           'tags': 'run,docker,container',
                           'recreate': 'yes',
                           'docker_base_image': docker_base_image,
                           'docker_os': docker_os,
                           'docker_os_version': docker_os_version,
                           'cm_repo': cm_repo,
                           'env': env,
                           'image_repo': image_repo,
                           'interactive': interactive,
                           'mounts': mounts,
                           'image_name': 'cm-script-'+script_alias,
#                            'image_tag': script_alias,
                           'detached': detached,
                           'script_tags': f'{tag_string}',
                           'run_cmd': final_run_cmd,
                           'v': i.get('v', False),
                           'quiet': True,
                           'pre_run_cmds': docker_pre_run_cmds,
                           'real_run': True,
                           'add_deps_recursive': {
                               'build-docker-image': {
                                   'dockerfile': dockerfile_path
                               }
                           }
                        }

        if all_gpus:
            cm_docker_input['all_gpus'] = True

        if device:
            cm_docker_input['device'] = device

        if gh_token != '':
            cm_docker_input['gh_token'] = gh_token

        if port_maps:
            cm_docker_input['port_maps'] = port_maps

        if shm_size != '':
            cm_docker_input['shm_size'] = shm_size

        if extra_run_args != '':
            cm_docker_input['extra_run_args'] = extra_run_args

        if i.get('docker_save_script', ''):
            cm_docker_input['save_script'] = i['docker_save_script']

        print ('')

        r = self_module.cmind.access(cm_docker_input)
        if r['return'] > 0:
            return r


    return {'return':0}

############################################################
def check_gh_token(i, docker_settings, quiet):
    gh_token = i.get('docker_gh_token', '')

    if docker_settings.get('gh_token_required', False) and gh_token == '':
        rx = {'return':1, 'error':'GH token is required but not provided. Use --docker_gh_token to set it'}

        if quiet:
            return rx

        print ('')
        gh_token = input ('Enter GitHub token to access private CM repositories required for this CM script: ')

        if gh_token == '':
            return rx

    return {'return':0, 'gh_token': gh_token}
