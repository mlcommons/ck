import cmind
import os
import copy

base_path={}
base_path_meta={}

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
    prune_key_uid = prune.get('key_uid', '')
    prune_uid = prune.get('uid', '')
    prune_list = prune.get('list',[])
    
    # Checking individual files inside CM entry
    selection = []
 
    if i.get('skip_files', False):
        for l in lst:
             meta = l.meta
             full_path = l.path

             meta['full_path']=full_path

             add = True
             
             if prune_key!='' and prune_key_uid!='':
                 if prune_key_uid not in meta.get(prune_key, []):
                     add = False
             
             if add:
                 selection.append(meta)
    else:
        for l in lst:
            path = l.path

            main_meta = l.meta
            all_tags = main_meta.get('tags',[])

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

                    # Check base
                    r = process_base(meta, full_path)
                    if r['return']>0: return r
                    meta = r['meta']
                    
                    uid = meta['uid']

                    # Check pruning
                    add = True

                    if len(prune)>0:
                        if prune_uid!='' and uid != prune_uid:
                            add = False
                            
                        if add and len(prune_list)>0 and uid not in prune_list:
                            add = False

                        if add and prune_key!='' and prune_key_uid!='' and prune_key_uid != meta.get(prune_key, None):
                            add = False

                    if add:
                        meta['full_path']=full_path

                        add_all_tags = copy.deepcopy(all_tags)
                        
                        name = meta.get('name','')
                        if name=='':
                            name = ' '.join(meta.get('tags',[]))
                        name = name.strip()
                        meta['name'] = name

                        file_tags = meta.get('tags', '').strip()
                        if file_tags=='':
                            if name!='':
                                add_all_tags += [v.lower() for v in name.split(' ')]
                        else:
                            add_all_tags += file_tags.split(',')
                            
                        meta['all_tags']=add_all_tags

                        meta['main_meta']=main_meta

                        selection.append(meta)

    return {'return':0, 'lst':lst, 'selection':selection}

##################################################################################
def process_base(meta, full_path):

    global base_path, base_path_meta

    _base = meta.get('_base', '')
    if _base != '':
        name = ''

        filename = _base
        full_path_base = os.path.dirname(full_path)
 
        if not filename.endswith('.yaml') and not filename.endswith('.json'):
            return {'return':1, 'error':'_base file {} in {} must be .yaml or .json'.format(filename, full_path)}
        
        if ':' in _base:
            x = _base.split(':')
            name = x[0]

            full_path_base = base_path.get(name, '')
            if full_path_base == '':
                
                # Find artifact
                r = cmind.access({'action':'find',
                                  'automation':'cfg',
                                  'artifact':name})
                if r['return']>0: return r

                lst = r['list']

                if len(lst)==0:
                    if not os.path.isfile(path): 
                        return {'return':1, 'error':'_base artifact {} not found in {}'.format(name, full_path)}

                full_path_base = lst[0].path
            
                base_path[name] = full_path_base
            
            filename = x[1]
       
        # Load base
        path = os.path.join(full_path_base, filename)

        if not os.path.isfile(path): 
            return {'return':1, 'error':'_base file {} not found in {}'.format(filename, full_path)}
            
        if path in base_path_meta:
            base = copy.deepcopy(base_path_meta[path])
        else:
            path_without_ext = path[:-5]

            r = cmind.utils.load_yaml_and_json(path_without_ext)
            if r['return']>0: return r

            base = r['meta']

            base_path_meta[path]=copy.deepcopy(base)

        for k in meta:
            v = meta[k]

            if k not in base:
                base[k]=v
            else:
                if isinstance(v, str):
                    # Only merge a few special keys and overwrite the rest
                    if k in ['tags','name']:
                        base[k] += meta[k]
                    else:
                        base[k] = meta[k]

                elif type(v) == list:
                    for vv in v:
                        base[k].append(vv)
                elif type(v) == dict:
                    base[k].merge(v)

        meta = base

    return {'return':0, 'meta':meta}




##################################################################################
def get_with_complex_key(meta, key):

    j = key.find('.')
    
    if j<0:
        return meta.get(key)

    key0 = key[:j]

    if key0 not in meta:
        return None

    return get_with_complex_key(meta[key0], key[j+1:])

##################################################################################
def get_with_complex_key_safe(meta, key):
    v = get_with_complex_key(meta, key)

    if v == None: v=''

    return v

##################################################################################
def prepare_table(i):

    import pandas as pd
    import numpy as np

    selection = i['selection']
    misc = i['misc_module']

    html = ''

    all_data = []

#    dimensions = [('input.model', 'MLPerf model'),
#                  ('input.implementation', 'MLPerf implementation'),
#                  ('input.framework', 'MLPerf framework')]

    dimensions = i.get('dimensions', [])

    dimension_values = {}
    dimension_keys = []
                  
    if len(dimensions) == 0:
        keys = [('test', 'CM test', 400, 'leftAligned')]
    else:
        keys = [('test', 'CM test', 50, 'leftAligned')]

        for k in dimensions:
            key = k[0]

            keys.append((k[0], k[1], 100, 'leftAligned'))

            dimension_values[key] = []
            dimension_keys.append(key)

#        # assemble all values
#        for s in selection:
#            for k in dimensions:
#                key = k[0]
#
#                value = get_with_complex_key(selection, key)
#
#                if value!=None and value!='' and value not in dimension_values[key]:
#                    dimension_values.append(value)
                    
        # If dimensions, sort by dimensions
        for d in list(reversed(dimension_keys)):
            selection = sorted(selection, key = lambda x: get_with_complex_key_safe(selection, d))



    keys += [
             ('functional', '<a href="https://github.com/mlcommons/ck/blob/master/docs/artifact-evaluation/submission.md">Functional</a>', 80, ''),
             ('reproduced', '<a href="https://github.com/mlcommons/ck/blob/master/docs/artifact-evaluation/submission.md">Reproduced</a>', 80, ''),
             ('notes', 'Notes', 200, 'lefAligned'),
            ]

    j = 0

    badges_url={'functional':'https://cTuning.org/images/artifacts_evaluated_functional_v1_1_small.png',
                'reproduced':'https://cTuning.org/images/results_reproduced_v1_1_small.png'}


    
    
    

    for s in selection:
        row = {}

        j += 1

        uid = s['uid']

        url = misc.make_url(uid, key='uid', action='howtorun', md=False)

        name = s.get('name','')
        if name == '': name = uid


        if len(dimensions) == 0:
            row['test'] = '<a href="{}" target="_blank">{}</a>'.format(url, name)
        else:
            row['test'] = '<a href="{}" target="_blank">View</a>'.format(url)
            for k in dimensions:
                kk = k[0]

                v = get_with_complex_key_safe(s, kk)

                row[kk] = str(v)




        # Check ACM/IEEE functional badge
        x = ''
        if s.get('functional', False):
            x = '<center><a href="{}" target="_blank"><img src="{}" height="32"></a></center>'.format(url, badges_url['functional'])
        row['functional'] = x

        # Check ACM/IEEE reproduced badge
        x = ''
        if s.get('reproduced', False):
            x = '<center><a href="{}" target="_blank"><img src="{}" height="32"></a></center>'.format(url, badges_url['reproduced'])
        row['reproduced'] = x
        
        # Check misc notes
        row['notes']=s.get('notes','')
        
        # Finish row
        all_data.append(row)


    # Visualize table
    pd_keys = [v[0] for v in keys]
    pd_key_names = [v[1] for v in keys]

    pd_all_data = []
    for row in sorted(all_data, key=lambda row: (row.get('x1',0))):
        pd_row=[]
        for k in pd_keys:
            pd_row.append(row.get(k))
        pd_all_data.append(pd_row)

    df = pd.DataFrame(pd_all_data, columns = pd_key_names)

    df.index+=1

    return {'return':0, 'df':df}






##################################################################################
def gui(i):

    params = i['params']
    st = i['streamlit_module']
    misc = i['misc_module']
    meta = i['meta']
    gui_meta = meta['gui']
    skip_header = i.get('skip_title', False)

    end_html = ''

    if not skip_header:
        # Title
        title = gui_meta['title']

        st.title('[Collective Mind](https://github.com/mlcommons/ck)')

        st.markdown('### {}'.format(title))


    
    
    
    # Check if test uid is specified
    uid = ''
    x = params.get('uid',[''])
    if len(x)>0 and x[0]!='': uid = x[0].strip()

    bench_uid = ''
    x = params.get('bench_uid',[''])
    if len(x)>0 and x[0]!='': bench_uid = x[0].strip()

    compute_uid = ''
    x = params.get('compute_uid',[''])
    if len(x)>0 and x[0]!='': compute_uid = x[0].strip()
        

    
    
    ##############################################################
    # Check the first level of benchmarks
    ii = {'tags':'benchmark,run', 'skip_files':True, 'prune':{}}

    if uid != '':
        ii['skip_files'] = False
        ii['prune']['uid']=uid
    if bench_uid !='':
        ii['artifact']=bench_uid
    if compute_uid !='':
        ii['prune']['key']='supported_compute'
        ii['prune']['key_uid']=compute_uid

    r=load_cfg(ii)
    if r['return']>0: return r            

    lst = r['selection']

    if len(lst)==0:
        st.markdown('Warning: no benchmarks found!')
        return {'return':0}
    
    test_meta = {}

    bench_id = 0


    ###########################################################################################################
    if uid != '':
        if len(lst)==0:
            st.markdown('CM test with UID "{}" not found!'.format(uid))
            return {'return':0}
        elif len(lst)>1:
            st.markdown('Warning: More than 1 CM test found with UID "{}" - ambiguity!'.format(uid))
            return {'return':0}

        test_meta = lst[0]

        bench_id = 1
        compute_uid = test_meta['compute_uid']
        bench_supported_compute = [compute_uid]
    
    
    if uid == '':
        selection = sorted(lst, key = lambda v: v['name'])
        bench_selection = [{'name':''}] + selection

        if bench_uid !='':
            bench_id_index = 1
        else:
            # Check if want to force some benchmark by default
            # 27c06c35bceb4059 == MLPerf inference v4.0

            bench_id_index = 0

            j=0
            for b in bench_selection:
                if b.get('uid','')=='27c06c35bceb4059':
                    bench_id_index=j
                    break
                j+=1

        
        bench_id = st.selectbox('Select benchmark:',
                                 range(len(bench_selection)), 
                                 format_func=lambda x: bench_selection[x]['name'],
                                 index = bench_id_index,
                                 key = 'bench')

    
        bench_supported_compute = []
        bench_meta = {}
        if bench_id>0:
            bench_meta = bench_selection[bench_id]
            bench_supported_compute = bench_meta.get('supported_compute',[])

            urls = bench_meta.get('urls',[])
            if len(urls)>0:
                x = '\n'
                for u in urls:
                    name = u['name']
                    url = u['url']

                    x+=' [ [{}]({}) ] '.format(name, url)
                x+='\n'

                st.markdown(x)
    
    ###########################################################################################################
    if True==True:
        ##############################################################
        # Check compute

        ii = {'tags':'benchmark,compute'}
        if bench_id>0:
            if compute_uid !='':
                x = [compute_uid]
            else:
                x = bench_supported_compute
                if len(x) == 0:
                    st.markdown('Warning: no supported compute selected!')
                    return {'return':0}
            
            ii['prune']={'list':x}

        r=load_cfg(ii)
        if r['return']>0: return r            

        selection = sorted(r['selection'], key = lambda v: v['name'])

        if len(selection) == 0 :
            st.markdown('Warning: no supported compute found!')
            return {'return':0}
        
        compute_selection = [{'name':''}]
        if len(selection)>0:
             compute_selection += selection

        compute_id_index = 0 if compute_uid == '' else 1
        
        if uid == '':
            compute_id = st.selectbox('Select target hardware to benchmark:',
                                       range(len(compute_selection)), 
                                       format_func=lambda x: compute_selection[x]['name'],
                                       index = compute_id_index,
                                       key = 'compute')

            compute = {}
            if compute_id>0:
                compute = compute_selection[compute_id]
                compute_uid = compute['uid']
            
        compute_meta = {}
        for c in compute_selection:
            if c.get('uid','')!='':
                compute_meta[c['uid']]=c

    ###########################################################################################################
    if uid == '':

        ##############################################################
        # Check tests
        ii = {'tags':'benchmark,run'}

        if bench_id>0:
            bench_uid = bench_selection[bench_id]['uid']
            ii['artifact']=bench_uid
        if compute_uid!='':
            ii['prune']={'key':'compute_uid', 'key_uid':compute_uid}

        r=load_cfg(ii)
        if r['return']>0: return r            

        selection = sorted(r['selection'], key = lambda v: v['name'])

        # Check how many and prune
        if len(selection) == 0:
             st.markdown('No CM tests found')
             return {'return':0}

        for s in selection:
            c_uid = s.get('compute_uid','')
            if c_uid!='':
                c_tags = compute_meta[c_uid].get('tags','')
                if c_tags!='':
                    s['all_tags']+=c_tags.split(',')

                s['compute_meta']=compute_meta[c_uid]    

        
        if len(selection)>1:
            # Update selection with compute tags
            test_tags = ''
            x = params.get('tags',[''])
            if len(x)>0 and x[0]!='': test_tags = x[0].strip()
            
            test_tags = st.text_input('Found {} CM tests. Prune them by tags:'.format(str(len(selection))), value=test_tags, key='test_tags').strip()

            if test_tags!='':
                test_tags_list = test_tags.replace(' ',',').split(',')

                pruned_selection = []

                for s in selection:
                    all_tags = s['all_tags']

                    add = True

                    for t in test_tags_list:
                        if t not in all_tags:
                            add = False
                            break

                    if add:
                        pruned_selection.append(s)
        
                selection = pruned_selection

        test_selection = [{'name':''}] + selection
        
        
        
        if len(selection)<200:
            # Creating compute selector
            test_id_index = 1 if len(selection)==1 else 0
                
            test_id = st.selectbox('Select a test from {}:'.format(str(len(selection))),
                                     range(len(test_selection)), 
                                     format_func=lambda x: test_selection[x]['name'],
                                     index = test_id_index,
                                     key = 'test')
        
            
            if test_id >0:
                test_meta = test_selection[test_id]
            else:
                #########################################################################
                # View many (table)
                ii = {'selection':selection,
                      'misc_module':misc}
                
                # Check if dimensions in the bench
                dimensions = bench_meta.get('dimensions', [])
                if len(dimensions)>0:
                     viewer_selection = ['benchmark specific', 'universal']
                     
                     viewer = st.selectbox('Viewer:', viewer_selection, key = 'viewer')

                     if viewer == 'benchmark specific':
                         ii['dimensions'] = dimensions
                
                else:
                     st.markdown('---')

                r = prepare_table(ii)
                if r['return']>0: return r

                df = r['df']

                html=df.to_html(escape=False, justify='left')
                st.write(html, unsafe_allow_html = True)
            
#                st.dataframe(df, unsafe_allow_html = True)







    ##############################################################
    # Show individual test
    if len(test_meta)>0:
        if uid != '':
            c_uid = test_meta.get('compute_uid','')
            if c_uid!='':
                c_tags = compute_meta[c_uid].get('tags','')
                if c_tags!='':
                    test_meta['all_tags']+=c_tags.split(',')

                test_meta['compute_meta']=compute_meta[c_uid]    

        
        if uid == '':
            st.markdown('---')

            uid = test_meta['uid']
        
        # First, check if there is a README
        test_path = test_meta['full_path']

        test_md = test_meta['full_path'][:-5]+'.md'
        if os.path.isfile(test_md):

            r = cmind.utils.load_txt(test_md)
            if r['return']>0: return r

            s = r['string']

            st.markdown(s)

        # Next print some info (for now JSON)
        import json
        x = """
---
**CM test dictionary:**
```json
{}
```
            """.format(json.dumps(test_meta, indent=2))
        st.markdown(x)
        



        
        
        # Create self link
        # This misc module is in CM "gui" script
        x1 = misc.make_url(uid, key='uid', action='howtorun', md=False)
        end_html='<center><small><i><a href="{}">Self link</a></i></small></center>'.format(x1)

    return {'return':0, 'end_html': end_html}

