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
def gui(i):

    st = i['streamlit_module']
    meta = i['meta']
    gui_meta = meta['gui']

    title = gui_meta['title']

    # Title
    st.title('[Collective Mind](https://github.com/mlcommons/ck)')

    st.markdown('### {}'.format(title))

    
    
    
    # Check compute
    r=load_cfg({'tags':'benchmark,compute'})
    if r['return']>0: return r            

    selection = r['selection']
    selection_desc = r['selection_desc']

    # Creating compute selector
    compute = st.selectbox('Select target hardware:',
                           range(len(selection_desc)), 
                           format_func=lambda x: selection_desc[x],
                           index = 0,
                           key = 'compute')

    
    
    
    return {'return':0}

##################################################################################
def load_cfg(i):

    tags = i['tags']

    key = i.get('key','')
    if key == '': key = 'cfg-'

    ii={'action':'find',
        'automation':'cfg',
        'tags':tags}

    r=cmind.access(ii)
    if r['return']>0: return r

    lst = r['list']

    # Checking individual files inside CM entry
    metas = []

    selection = ['']
    selection_desc = ['']
    
    for l in lst:
        path = l.path

        files = os.listdir(path)

        for f in files:
            if not f.endswith('.json') and not f.endswith('.yaml'):
                continue

            if key!='' and not f.startswith(key):
                continue

            full_path = os.path.join(path, f)

            full_path_without_ext = full_path[:-5]

            r = cmind.utils.load_yaml_and_json(full_path_without_ext)
            if r['return']>0:
                print ('Warning: problem loading file {}'.format(full_path))
            else:
                meta = r['meta']

                aux_tags = meta.get('tags',[])

                aux_tags_string = ','.join(aux_tags)

                aux_tags_print = ''
                for t in aux_tags:
                    if aux_tags_print!='': 
                        aux_tags_print+=' • '

                    # Beautify
                    if t == 'cpu': t = 'CPU'
                    elif t == 'gpu': t = 'GPU'
                    elif t == 'tpu': t = 'TPU'
                    elif t == 'ai 100': t = 'AI 100'
                    elif t == 'amd': t = 'AMD'
                    elif t == 'x64': t = 'x64'
                    else:
                        t = t.capitalize()
                    
                    aux_tags_print += t

                uid = meta['uid']    

                dd = {'full_path': full_path,
                      'uid': uid,
                      'tags': aux_tags_string,
                      'tags_print': aux_tags_print}

                selection.append(uid)
                selection_desc.append(aux_tags_print)      

                metas.append(dd)

    # Prepare selector



   
    return {'return':0, 'lst':lst, 'all_meta':metas, 'selection':selection, 'selection_desc':selection_desc}
