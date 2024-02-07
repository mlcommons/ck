# Developer(s): Grigori Fursin

import cmind
import os
import datetime
import misc

def page(st, params):

    url_prefix = st.config.get_option('server.baseUrlPath')+'/'
    url_prefix_component = url_prefix + '?action=components'

    component_name = ''
    x = params.get('name',[''])
    if len(x)>0 and x[0]!='': component_name = x[0].strip()

    component_tags = ''
    if component_name == '':
        x = params.get('tags',[''])
        if len(x)>0 and x[0]!='': component_tags = x[0].strip()

    component_tags = st.text_input('Search open-source [Collective Mind](https://github.com/mlcommons/ck) automation recipes by tags:', value=component_tags, key='component_tags').strip()

    # Searching automation recipes
    
    ii = {'action':'find',
          'automation':'script,5b4e0237da074764'}

    if component_tags!='':
        ii['tags']=component_tags.replace(' ',',')
    elif component_name!='':
        ii['artifact']=component_name

    r = cmind.access(ii)
    if r['return']>0: return r

    lst2 = r['list']

    lst = [v for v in lst2 if not v.meta.get('private', False)]

    end_html = ''

    if len(lst)==0:
        st.markdown('Automation recipes were not found!')
    else:
        artifact = None

        if len(lst)==1:
            # Individual component
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

                script_tags = component_tags
                if component_tags=='':
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
                      'skip_bottom': True}
                
                return script.page(ii)

            else:
                
                st.markdown('### {} ({})'.format(alias, uid))

                # Check original link
                repo_meta = recipe.repo_meta

                url = repo_meta.get('url','')
                if url=='' and repo_meta.get('git', False):
                    url = 'https://github.com/'+repo_meta['alias'].replace('@','/')

                if url!='':
                    if not url.endswith('/'): url=url+'/'

                    url += 'tree/master/'

                    if repo_meta.get('prefix','')!='':
                        url += repo_meta['prefix']

                    if not url.endswith('/'): url=url+'/'
                    
                    url += 'script/'+alias

                    st.markdown('* View documentation and sources for this Collective Mind automation recipe at [GitHub]({}).'.format(url))

                
                url_gui = url_prefix_component+'&name='+alias+','+uid+'&gui=true'

                st.markdown('* View [CM GUI]({}) to run this script.'.format(url_gui))
        
        else:
            x = '''
                <small>
                 Found {} portable and reusable components (<a href="https://github.com/mlcommons/ck/tree/master/cm-mlops/script">GitHub sources</a>):
                </center>
                '''.format(len(lst))
            st.write(x, unsafe_allow_html = True)
            
            categories={}
            
            for l in sorted(lst, key=lambda x: (
                                                x.meta.get('alias','')
                                               )):

                category = l.meta.get('category','')
                if category == '': category = 'Unsorted'

                if category not in categories:
                    categories[category]=[]

                categories[category].append(l)
            
            for category in sorted(categories):
                md = '### {}'.format(category)+'\n'
                
                for recipe in categories[category]:
                    meta = recipe.meta

                    alias = meta['alias']
                    uid = meta['uid']

                    url = url_prefix_component+'&name='+alias+','+uid
                    
                    md += '* [{}]({})'.format(alias, url)+'\n'

                st.markdown(md)
    
    return {'return':0, 'end_html':end_html}
