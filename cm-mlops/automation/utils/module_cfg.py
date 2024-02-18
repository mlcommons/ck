import os
import cmind
import copy

base_path={}
base_path_meta={}

##################################################################################
def load_cfg(i):

    tags = i.get('tags','')
    artifact = i.get('artifact','')

    key = i.get('key', '')
    key_end = i.get('key_end', [])

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
    prune_meta_key = prune.get('meta_key', '')
    prune_meta_key_uid = prune.get('meta_key_uid', '')
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

            skip = False
            
            if prune_meta_key!='' and prune_meta_key_uid!='':
                if prune_meta_key_uid not in main_meta.get(prune_meta_key, []):
                    skip = True
            
            if skip:
                continue
            
            all_tags = main_meta.get('tags',[])

            files = os.listdir(path)

            for f in files:
                if key!='' and not f.startswith(key):
                    continue

                if f.startswith('_') or (not f.endswith('.json') and not f.endswith('.yaml')):
                    continue

                if len(key_end)>0:
                    skip = True
                    for ke in key_end:
                        if f.endswith(ke):
                            skip = False
                            break
                    if skip:
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
