# Developer(s): Grigori Fursin

import cmind
import os
import misc

import streamlit.components.v1 as components

import streamlit as st

announcement = 'Under development - please get in touch via [Discord](https://discord.gg/JjWNWXKxwT) for more details ...'

def main():
    params = misc.get_params(st)

    # Set title
    st.title('How to run benchmarks')

    st.markdown(announcement)

    return page(st, params)




def page(st, params, action = ''):

    end_html = ''
    
    # Announcement
#    st.markdown('----')

    url_script = misc.make_url('', key='', action='scripts', md=False)

    # Some info
    x = '''
         <i>
         <small>
         This interface will help you generate a command line or Python API 
         to run modular benchmarks composed from 
         <a href="{}">automation recipes (CM scripts)</a>.
         Note that this is a <a href="https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md">collaborative engineering effort</a> 
         to make sure that they work across all possible versions and configurations of models, data sets, software and hardware
         - please report encountered issues and provide feedback
         <a href="https://github.com/mlcommons/ck/issues">here</a>
         and get in touch via <a href="https://discord.gg/JjWNWXKxwT">Discord</a>!
         </small>
         </i>
          <br>
          <br>
        '''.format(url_script)

    st.write(x, unsafe_allow_html = True)
    
#    st.markdown(announcement)
    

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

    r = misc.make_selection(st, r['selection'], 'compute', 'target hardware', compute_uid)
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

    # Make default selection of MLPerf inference
    force_bench_index = 0
    if bench_uid == '':
        j = 0
        for q in sorted(pruned_selection, key = lambda v: v['name']):
            j += 1
            if q['uid'] == '39877bb63fb54725':
                force_bench_index = j
    
    r = misc.make_selection(st, pruned_selection, 'benchmark', 'benchmark', bench_uid, force_index = force_bench_index)
    if r['return']>0: return r

    bench_meta = r['meta']
#    st.markdown(bench_meta)

    if len(bench_meta)>0:
        ############################################################################################
        # Check common CM interface

#        st.markdown('---')

        urls = bench_meta.get('urls',[])

        script_path = ''
        script_name = bench_meta.get('script_name','')
        script_meta = {}
        script_obj = None
        script_url = ''
        if script_name!='':
            ii = {'action':'find',
                  'automation':'script',
                  'artifact':script_name}
            r = cmind.access(ii)
            if r['return']>0: return r

            lst = r['list']

            if len(lst)>0:

                script_obj = lst[0]

                script_meta = script_obj.meta
                script_path = script_obj.path
                script_repo_meta = script_obj.repo_meta

                script_alias = script_meta['alias']

                repo_meta = script_obj.repo_meta
                
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
                    
                    url += 'script/'+script_alias

                    script_url = url

                if not bench_meta.get('skip_extra_urls', False):
                    url_script = misc.make_url(script_name, key='name', action='scripts', md=False)
                    url_script += '&gui=true'
                    
                    urls.append({'name': 'Universal CM GUI to run this benchmark',
                                 'url': url_script})

                    # Check if extra README
                    script_path_readme_extra = os.path.join(script_path, 'README-extra.md')

                    if os.path.isfile(script_path_readme_extra):
                        # Check README.extra.md
                        url_readme_extra = url+'/README-extra.md'

                        urls.append({'name': 'Notes about how to run this benchmark from the command line',
                                     'url': url_readme_extra})

        
        # Check URLS
        if len(urls)>0:
            x = '\n'
            for u in urls:
                name = u['name']
                url = u['url']

                x+='* [{}]({})\n'.format(name, url)
            x+='\n'

            st.markdown(x)

        ############################################################################################
        # Check if has customization
        extra = {}
        skip = False
        
        script_tags = script_meta.get('tags_help','')
        if script_tags =='':
            script_tags = ','.join(script_meta.get('tags',[]))
        
        if script_obj!=None:
            ii = {'st': st,
                  'params': params,
                  'meta': script_obj.meta,
                  'misc_module': misc,
                  'compute_meta':compute_meta,
                  'bench_meta':bench_meta,
                  'script_path':script_path,
                  'script_tags':script_tags,
                  'script_url':script_url}

            import sys
            import importlib

            full_module_path = os.path.join(script_obj.path, 'customize.py')

            tmp_module = None
            try:
                found_automation_spec = importlib.util.spec_from_file_location('customize', full_module_path)
                if found_automation_spec != None:
                    tmp_module = importlib.util.module_from_spec(found_automation_spec)
                    found_automation_spec.loader.exec_module(tmp_module)
#               tmp_module=importlib.import_module('customize')
            except Exception as e:
               st.markdown('WARNING: {}'.format(e))
               pass

            if tmp_module!=None:
                if hasattr(tmp_module, 'gui'):
                    try:
                        func = getattr(tmp_module, 'gui')
                    except Exception as e:
                        return {'return':1, 'error':format(e)}

                    r = func(ii)
                    if r['return'] > 0 : return r

                    extra = r.get('extra', {})
                    skip = r.get('skip', False)

        ############################################################################################
        # Show official GUI
        if script_path!='' and not skip:
            import script

            ii = {'st': st,
                  'params': params,
                  'script_path': script_path, 
                  'script_alias': script_alias, 
                  'script_tags': script_tags, 
                  'script_meta': script_meta,
                  'script_repo_meta': script_repo_meta,
                  'skip_bottom': True,
                  'extra': extra}
            
            rr = script.page(ii)
            if rr['return']>0: return rr

            end_html += '\n'+rr.get('end_html','')

        ############################################################################################
        self_url = misc.make_url(bench_meta['uid'], action='howtorun', key='bench_uid', md=False)

        if len(compute_meta)>0:
            self_url += '&compute_uid='+compute_meta['uid']

        end_html='<center><small><i><a href="{}">Self link</a></i></small></center>'.format(self_url)


    return {'return':0, 'end_html':end_html}
