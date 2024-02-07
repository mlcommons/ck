import cmind
import os

##################################################################################
def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    return {'return':0}

##################################################################################
def postprocess(i):

    env = i['env']

    return {'return':0}


##################################################################################
def load_cfg(i):

    tags = i.get('tags','')
    artifact = i.get('artifact','')

    key = i.get('key','')

    ii={'action':'find',
        'automation':'cfg'}
    if artifact!='':
        ii['artifact']=artifact
    elif tags!='':
        ii['tags']=tags

    r=cmind.access(ii)
    if r['return']>0: return r

    lst = r['list']

    prune = i.get('prune',{})
    prune_key = prune.get('key', '')
    prune_list = prune.get('list',[])
    
    # Checking individual files inside CM entry
    selection = []
 
    if i.get('skip_files', False):
        for l in lst:
             meta = l.meta
             full_path = l.path

             meta['full_path']=full_path

             selection.append(meta)
    else:
        for l in lst:
            path = l.path

            files = os.listdir(path)

            for f in files:
                if key!='' and not f.startswith(key):
                    continue

                if f.startswith('_') or (not f.endswith('.json') and not f.endswith('.yaml')):
                    continue

                full_path = os.path.join(path, f)

                full_path_without_ext = full_path[:-5]

                r = cmind.utils.load_yaml_and_json(full_path_without_ext)
                if r['return']>0:
                    print ('Warning: problem loading file {}'.format(full_path))
                else:
                    meta = r['meta']

                    uid = meta['uid']

                    # Check pruning
                    add = True
                    if prune_key!='' and len(prune_list)>0 and uid not in prune_list:
                        add = False

                    if add:
                        meta['full_path']=full_path

                        name = meta.get('name','')
                        if name=='':
                            name = ' '.join(meta.get('tags',[]))
                        name = name.strip()
                        meta['name'] = name
                        
                        selection.append(meta)

    return {'return':0, 'lst':lst, 'selection':selection}


##################################################################################
def gui(i):

    st = i['streamlit_module']
    meta = i['meta']
    gui_meta = meta['gui']
    skip_header = i.get('skip_title', False)
    
    if not skip_header:
        # Title
        title = gui_meta['title']

        st.title('[Collective Mind](https://github.com/mlcommons/ck)')

        st.markdown('### {}'.format(title))

    # Preparing state
    if 'bench_id' not in st.session_state: st.session_state['bench_id']=0
    if 'compute_id' not in st.session_state: st.session_state['compute_id']=0
    
    ##############################################################
    # Check the first level of benchmarks
    r=load_cfg({'tags':'benchmark,run', 'skip_files':True})
    if r['return']>0: return r            

    selection = sorted(r['selection'], key = lambda v: v['name'])
    bench_selection = [{'name':''}] + selection

    # Creating compute selector
    bench_id = st.selectbox('Select benchmark:',
                             range(len(bench_selection)), 
                             format_func=lambda x: bench_selection[x]['name'],
                             index = 0,
                             key = 'bench')

    bench_supported_compute = []
    if bench_id != st.session_state['bench_id']:
        bench_meta = bench_selection[bench_id]
        bench_supported_compute = bench_meta.get('supported_compute',[])
    

    ##############################################################
    # Check compute
    r=load_cfg({'tags':'benchmark,compute', 
                'prune':{'key':'supported_compute', 'list':bench_supported_compute}})
    if r['return']>0: return r            

    selection = sorted(r['selection'], key = lambda v: v['name'])
    compute_selection = [{'name':''}] + selection


    # Creating compute selector
    compute_id = st.selectbox('Select target hardware:',
                               range(len(compute_selection)), 
                               format_func=lambda x: compute_selection[x]['name'],
                               index = 0,
                               key = 'compute')

    if compute_id!=st.session_state['compute_id']:
        st.session_state['compute_id']=compute_id

        try:
           st.rerun()
        except:
           st.experimental_rerun()


    ##############################################################
    # Check tests
    ii = {'tags':'benchmark,run'}

    if bench_id>0:
        bench_uid = bench_selection[bench_id]['uid']
        ii['artifact']=bench_uid


    r=load_cfg(ii)
    if r['return']>0: return r            

    selection = sorted(r['selection'], key = lambda v: v['name'])


    test_selection = [{'name':''}] + selection
    
    
    
    # Creating compute selector
    test_id = st.selectbox('Select test:',
                             range(len(test_selection)), 
                             format_func=lambda x: test_selection[x]['name'],
                             index = 0,
                             key = 'test')

    ##############################################################
    if test_id >0:
        test_meta = test_selection[test_id]

        test_path = test_meta['full_path']

        test_md = test_meta['full_path'][:-5]+'.md'
        if os.path.isfile(test_md):

            r = cmind.utils.load_txt(test_md)
            if r['return']>0: return r

            s = r['string']

            st.markdown('---')

            st.markdown(s)

        

    return {'return':0}

