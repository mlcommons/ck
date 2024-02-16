# Developer(s): Grigori Fursin

import cmind
import os
import misc

import streamlit.components.v1 as components

import streamlit as st

announcement = 'Under development - please get in touch via [Discord](https://discord.gg/JjWNWXKxwT) for more details ...'

initialized = False
external_module_path = ''
external_module_meta = {}

def main():
    params = misc.get_params(st)

    # Set title
    st.title('How to run benchmarks')

    st.markdown(announcement)

    return page(st, params)




def make_selection(st, selection, param_key, text, x_uid):

    x_meta = {}
    
    if len(selection)>0:
         selection = sorted(selection, key = lambda v: v['name'])

         if x_uid != '':
             x_meta = selection[0]
             st.markdown('Selected {}: {}'.format(text, x_meta['name']))
         else:
             x_selection = [{'name':''}]
             x_selection += selection
             
             x_id = st.selectbox('Select {}:'.format(text),
                                 range(len(x_selection)), 
                                 format_func=lambda x: x_selection[x]['name'],
                                 index = 0,
                                 key = param_key)

             if x_id>0:
                 x_meta = x_selection[x_id]

    return {'return':0, 'meta':x_meta}


def page(st, params, action = ''):

    global initialized, external_module_path, external_module_meta

    end_html = ''
    
    # Announcement
    st.markdown('----')
    st.markdown(announcement)
    

    ############################################################################################
    # Select target hardware
    compute_uid = ''
    x = params.get('compute_uid',[''])
    if len(x)>0 and x[0]!='': compute_uid = x[0].strip()
    
    ii = {'action':'load_cfg',
          'automation':'utils',
          'tags':'benchmark,compute',
          'skip_files':False}

    if compute_uid!='':
        ii['prune']={'uid':compute_uid}

    r = cmind.access(ii)
    if r['return']>0: return r

    r = make_selection(st, r['selection'], 'compute', 'target hardware', compute_uid)
    if r['return']>0: return r

    compute_meta = r['meta']
#    st.markdown(compute_meta)

    ############################################################################################
    # Select benchmark
    bench_uid = ''
    x = params.get('bench_uid',[''])
    if len(x)>0 and x[0]!='': bench_uid = x[0].strip()
    
    ii = {'action':'load_cfg',
          'automation':'utils',
          'tags':'benchmark,list',
          'skip_files':False}

    if bench_uid!='':
        ii['prune']={'uid':bench_uid}

    r = cmind.access(ii)
    if r['return']>0: return r

    # Prune by supported compute
    selection = r['selection']
    pruned_selection = []

    if len(compute_meta)==0 or compute_meta.get('tags','')=='':
        pruned_selection = selection
    else:
        xtags = set(compute_meta['tags'].split(','))

#        st.markdown(str(xtags))
        
        for s in selection:
            add = True

            supported_compute = s.get('supported_compute',[])
            if len(supported_compute)>0:
                add = False

                for c in supported_compute:
                    cc = set(c.split(','))
                    if cc.issubset(xtags):
                        add = True
                        break
            
            if add:
                pruned_selection.append(s)

    r = make_selection(st, pruned_selection, 'benchmark', 'benchmark', bench_uid)
    if r['return']>0: return r

    bench_meta = r['meta']
#    st.markdown(bench_meta)

    if len(bench_meta)>0:
        ############################################################################################
        # Check common CM interface

        st.markdown('---')

        urls = bench_meta.get('urls',[])

        script_name = bench_meta.get('script_name','')
        if script_name!='':
            ii = {'action':'find',
                  'automation':'script',
                  'artifact':script_name}
            r = cmind.access(ii)
            if r['return']>0: return r

            lst = r['list']

            if len(lst)>0:


                url_script = misc.make_url(script_name, key='name', action='scripts', md=False)
                url_script += '&gui=true'
                
                urls.append({'name': 'Universal CM GUI to run this benchmark',
                             'url': url_script})

                # Check if has README extra
                script_path = lst[0].path

                script_path_readme_extra = os.path.join(script_path, 'README-extra.md')

                if os.path.isfile(script_path_readme_extra):
                    repo_meta = lst[0].repo_meta
                    
                    alias = lst[0].meta['alias']

                    url = repo_meta.get('url','')
                    if url=='' and repo_meta.get('git', False):
                        url = 'https://github.com/'+repo_meta['alias'].replace('@','/')

                    if url!='':
                        # Recreate GitHub path
                        if not url.endswith('/'): url=url+'/'

                        url += 'tree/master/'

                        if repo_meta.get('prefix','')!='':
                            url += repo_meta['prefix']

                        if not url.endswith('/'): url=url+'/'
                        
                        url += 'script/'+alias

                        # Check README.extra.md
                        url_readme_extra = url+'/README-extra.md'

                        urls.append({'name': 'Notes about how to run this script',
                                     'url': url_readme_extra})

        
        # Check URLS
        if len(urls)>0:
            x = '\n'
            for u in urls:
                name = u['name']
                url = u['url']

                x+=' [ [{}]({}) ] '.format(name, url)
            x+='\n'

            st.markdown(x)



    return {'return':0, 'end_html':end_html}
