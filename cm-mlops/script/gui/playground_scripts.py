# Developer(s): Grigori Fursin

import cmind
import os
import datetime
import misc

def page(st, params):

    url_prefix = st.config.get_option('server.baseUrlPath')+'/'
    url_prefix_script = url_prefix + '?action=scripts'

    script_name = ''
    x = params.get('name',[''])
    if len(x)>0 and x[0]!='': script_name = x[0].strip()

    script_tags = ''
    if script_name == '':
        x = params.get('tags',[''])
        if len(x)>0 and x[0]!='': script_tags = x[0].strip()


    if script_tags == 'modular,app':
        x = '''
             <i>
             <small>
             This is a new project to automatically compose AI applications that can run across diverse models, data sets, software and hardware
             - please check our presentation at the <a href="https://sites.google.com/g.harvard.edu/mlperf-bench-hpca24/home">MLPerf-Bench workshop @ HPCA'24</a>
             and get in touch via <a href="https://discord.gg/JjWNWXKxwT">Discord</a>!
             </small>
             </i>
              <br>
              <br>
            '''

    else:
        x = '''
             <i>
             <small>
             <a href="https://github.com/mlcommons/ck/tree/master/cm-mlops/script">Collective Mind</a> is a collection of open-source, portable, extensible and ready-to-use 
             automation scripts with a human-friendly interface and minimal dependencies to make it easier to compose, benchmark and optimize 
             complex AI, ML and other applications and systems across diverse and continuously changing models, data sets, software and hardware.
             Note that this is a <a href="https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md">collaborative engineering effort</a> 
             to make sure that they work across all possible versions and configurations 
             - please report encountered issues and provide feedback
             <a href="https://github.com/mlcommons/ck/issues">here</a>
             and get in touch via <a href="https://discord.gg/JjWNWXKxwT">Discord</a>!
             </small>
             </i>
              <br>
              <br>
            '''

    st.write(x, unsafe_allow_html = True)


    script_tags = st.text_input('Search open-source automation recipes by tags:', value=script_tags, key='script_tags').strip()

    # Searching automation recipes
    
    ii = {'action':'find',
          'automation':'script,5b4e0237da074764'}

    if script_tags!='':
        script_tags=script_tags.replace(' ',',')
        ii['tags']=script_tags
    elif script_name!='':
        ii['artifact']=script_name

    # Check variations for later:
    variations = [v for v in script_tags.split(',') if v.startswith('_')]

    r = cmind.access(ii)
    if r['return']>0: return r

    lst2 = r['list']

    lst = [v for v in lst2 if not v.meta.get('private', False)]

    end_html = ''

    if len(lst)==0:
        st.markdown('CM scripts were not found!')
    else:
        artifact = None

        if len(lst)==1:
            # Individual script
            recipe = lst[0]

            meta = recipe.meta
            
            alias = meta['alias']
            uid = meta['uid']

            use_gui = False
            x = params.get('gui',[''])
            if len(x)>0 and (x[0].lower()=='true' or x[0].lower()=='yes'):
                import script

                script_path = recipe.path
                script_alias = alias

#                script_tags = script_tags
                if script_tags=='':
                    script_tags = meta.get('tags_help','')
                    if script_tags !='':
                        script_tags=script_tags.replace(' ',',')
                    else:
                        script_tags = ','.join(meta.get('tags',[]))

                ii = {'st': st,
                      'params': params,
                      'script_path': script_path, 
                      'script_alias': script_alias, 
                      'script_tags': script_tags, 
                      'script_meta': meta,
                      'script_repo_meta': recipe.repo_meta,
                      'skip_bottom': True}

                return script.page(ii)

            else:
                
                st.markdown('### CM script "{}" ({})'.format(alias, uid))

                repo_meta = recipe.repo_meta

                # Basic run
                tags = meta['tags_help'] if meta.get('tags_help','')!='' else ' '.join(meta['tags'])

                x1 = misc.make_url(tags.replace(' ',','), key = 'tags', action='scripts', md=False, skip_url_quote=True)
                x2 = misc.make_url(meta['alias'], action='scripts', md=False)
                x3 = misc.make_url(meta['uid'], action='scripts', md=False)
                end_html='<center><small><i>Self links: <a href="{}">tags</a> or <a href="{}">alias</a> or <a href="{}">UID</a></i></small></center>'.format(x1,x2,x3)

                extra_repo = '' if repo_meta['alias']=='mlcommons@ck' else '\ncm pull repo '+repo_meta['alias']

                xtags = tags
                if len(variations)>0:
                   if xtags!='':
                       xtags+=' '
                   xtags+=' '.join(variations)

                x = '''
```bash
pip install cmind -U
cm pull repo mlcommons@ck{}

cm run script "{}"
```

A few other popular commands:
```bash
cmr "{}" --help
cmr "{}" --shell
cm run script "{}" --shell
cm docker script "{}"
cm gui script "{}"
```
                    
                    '''.format(extra_repo,xtags,xtags,xtags,xtags,xtags,xtags)


                
                
                # Check original link

                url = repo_meta.get('url','')
                if url=='' and repo_meta.get('git', False):
                    url = 'https://github.com/'+repo_meta['alias'].replace('@','/')

                url_readme = ''
                url_readme_extra = ''
                url_meta_description = ''
                url_customize = ''

                if url!='':
                    # Recreate GitHub path
                    if not url.endswith('/'): url=url+'/'

                    url += 'tree/master/'

                    if repo_meta.get('prefix','')!='':
                        url += repo_meta['prefix']

                    if not url.endswith('/'): url=url+'/'
                    
                    url += 'script/'+alias

                    # Check README.md
                    z = os.path.join(recipe.path, 'README.md')
                    if os.path.isfile(z):
                        url_readme = url+'/README.md'

                    # Check README.extra.md
                    z = os.path.join(recipe.path, 'README-extra.md')
                    if os.path.isfile(z):
                        url_readme_extra = url+'/README-extra.md'

                    # Check customize.py
                    z = os.path.join(recipe.path, 'customize.py')
                    if os.path.isfile(z):
                        url_customize = url+'/customize.py'

                    # Check _cm.yaml or _cm.json
                    for z in ['_cm.yaml', '_cm.json']:
                        y = os.path.join(recipe.path, z)
                        if os.path.isfile(y):
                            url_meta_description = url+'/'+z
                    
                url_gui = url_prefix_script+'&name='+alias+','+uid+'&gui=true'
                
                z  = '* ***Check [open source code (Apache 2.0 license)]({}) at GitHub.***\n'.format(url)
                z += '* ***Check [detailed auto-generated README on GitHub]({}).***\n'.format(url_readme)
                z += '* ***Check [experimental GUI]({}) to run this script.***\n'.format(url_gui)
                z += '---\n'
                
                st.markdown(z)
                
                st.markdown('Default run on Linux, Windows, MacOS and any other OS (check [CM installation guide]({}) for more details):\n{}\n'.format(url_prefix + '?action=install', x))

                st.markdown('*The [Collective Mind concept](https://doi.org/10.5281/zenodo.8105339) is to gradually improve portability and reproducibility of common automation recipes based on user feedback'
                             ' while keeping the same human-friendly interface. If you encounter issues, please report them [here](https://github.com/mlcommons/ck/issues) '
                             ' to help this community project!*')

                

                if url_readme_extra!='':
                    st.markdown('* See [extra README]({}) for this automation recipe at GitHub.'.format(url_readme_extra))

                if url_meta_description!='':
                    st.markdown('* See [meta description]({}) for this automation recipe at GitHub.'.format(url_meta_description))

                if url_customize!='':
                    st.markdown('* See [customization python code]({}) for this automation recipe at GitHub.'.format(url_customize))

                # Check dependencies
                r = misc.get_all_deps_tags({'meta':meta, 'st':st})
                if r['return']>0: return r

                all_deps_tags = r['all_deps_tags']

                if len(all_deps_tags)>0:
                    st.markdown('**Dependencies on other CM scripts:**')

                    x=''
                    for t in sorted(all_deps_tags):
                        # Test that it's not just extending tags:
                        if t.startswith('_') or ',' not in t:
                            continue

                        url_deps = url_prefix_script+'&tags='+t
                        
                        x+='* [{}]({})\n'.format(t, url_deps)
                                        
                    st.markdown(x)


        else:
            categories={}
            
            for l in sorted(lst, key=lambda x: (
                                                x.meta.get('alias','')
                                               )):

                category = l.meta.get('category','')
                if category == '': category = 'Unsorted'

                if category not in categories:
                    categories[category]=[]

                categories[category].append(l)
            
            if len(categories)>1:
                category_selection = [''] + sorted(list(categories.keys()), key = lambda v: v.upper())

                # Creating compute selector
                category_id = st.selectbox('Prune by category:',
                                           range(len(category_selection)), 
                                           format_func=lambda x: category_selection[x],
                                           index = 0,
                                           key = 'category')

                if category_id>0:
                    category_key = category_selection[category_id]
                    categories = {category_key:categories[category_key]}

            # Check number of recipes
            recipes = 0
            for category in sorted(categories, key = lambda v: v.upper()):
                recipes += len(categories[category])
            
            x = '''
                <small>
                 Found {} automation recipes:
                </center>
                '''.format(str(recipes))
            st.write(x, unsafe_allow_html = True)

            
            for category in sorted(categories, key = lambda v: v.upper()):
                md = '### {}'.format(category)+'\n'
                
                for recipe in categories[category]:
                    meta = recipe.meta

                    alias = meta['alias']
                    uid = meta['uid']

                    url = url_prefix_script+'&name='+alias+','+uid
                    
                    md += '* [{}]({})'.format(alias, url)+'\n'

                st.markdown(md)
    
    return {'return':0, 'end_html':end_html}
