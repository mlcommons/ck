# Support functions

##########################################################
def make_url(name, alias='', action='contributors', key='name', md=True, skip_url_quote=False):

    import urllib

    if alias == '': alias = name

    x = urllib.parse.quote_plus(alias) if not skip_url_quote else alias

    xaction = ''
    if action != '':
        xaction = 'action={}'.format(action)
        if key!='':
            xaction+='&'


    url = '?{}'.format(xaction)

    if key!='':
        url+='{}={}'.format(key,x)

    if md:
        md = '[{}]({})'.format(name, url)
    else:
        md = url

    return md

##########################################################
def convert_date(date):
    # date: format YYYYMMDD to YYYY month day

    import calendar

    try:
        year = date[0:4]
        month = calendar.month_abbr[int(date[4:6])]
        day = str(int(date[6:8]))
    except Exception as e:
        return {'return':1, 'error':'date "{}" is not of format YYYYMMDD: {}'.format(date, format(e))}

    return {'return':0, 'string':year+' '+month+' '+day}

##########################################################
def get_params(st):
    compatibility = False

    try:
        params2 = st.query_params
        # Convert to old style
        params = {}
        for k in params2:
            v = params2[k]
            if type(v)!=list:
                params[k]=[v]
    except:
        compatibility = True

    if compatibility:
        params = st.experimental_get_query_params()

    return params

##########################################################
def get_all_deps_tags(i):
    meta = i['meta']
    all_deps_tags = i.get('all_deps_tags', [])

    for k in meta:
        v = meta[k]

        if k == 'tags':
            if type(v) == list:
                v = ','.join(v)

            if v not in all_deps_tags:
                all_deps_tags.append(v)

        elif type(v) == dict:
           r = get_all_deps_tags({'meta':v, 'all_deps_tags':all_deps_tags})
           all_deps_tags = r['all_deps_tags']

        elif type(v) == list:
           for vv in v:
               if type(vv) == dict:
                   r = get_all_deps_tags({'meta':vv, 'all_deps_tags':all_deps_tags})
                   all_deps_tags = r['all_deps_tags']

    return {'return':0, 'all_deps_tags':all_deps_tags}

##########################################################
def make_selector(i):

    key = i['key']
    value = i['desc']

    params = i['params']

    st = i['st']
    st_inputs = i['st_inputs']

    hide = i.get('hide', False)

    key2 = '@'+key

    value2 = None

    if type(value) == dict:
        desc = value['desc']

        choices = value.get('choices', [])
        boolean = value.get('boolean', False)
        default = value.get('default', '')
        force = value.get('force', None)

        if force != None:
            value2 = force
            if not hide:
                st.markdown('**{}:** {}'.format(desc, str(force)))
        
        else:
            if boolean:
                v = default
                x = params.get(key2, None)
                if x!=None and len(x)>0 and x[0]!=None:
                    if x[0].lower()=='true':
                        v = True
                    elif x[0].lower()=='false':
                        v = False
                if hide:
                    value2 = v
                else:
                    value2 = st.checkbox(desc, value=v, key=key2)
            elif len(choices)>0:
                x = params.get(key2, None)
                if x!=None and len(x)>0 and x[0]!=None:
                    x = x[0]
                    if x in choices:
                        selected_index = choices.index(x) if x in choices else 0
                    else:
                        selected_index = choices.index(default) if default!='' else 0
                else:
                    selected_index = choices.index(default) if default!='' else 0
                if hide:
                    value2 = choices[selected_index]
                else:
                    value2 = st.selectbox(desc, choices, index=selected_index, key=key2)
            else:
                v = default
                x = params.get(key2, None)
                if x!=None and len(x)>0 and x[0]!=None:
                    v = x[0]
                if hide:
                    value2 = v
                else:
                    value2 = st.text_input(desc, value=v, key=key2)

        st_inputs[key2] = value2

    else:
        desc = value
        if hide:
            value2 = desc
        else:
            value2 = st.text_input(desc)
        st_inputs[key2] = value2

    return {'return':0, 'key2': key2, 'value2': value2}

##########################################################
def make_selection(st, selection, param_key, text, x_uid, force_index=0):

    x_meta = {}
    
    if len(selection)>0:
         selection = sorted(selection, key = lambda v: v['name'])

         if x_uid != '':
             x_meta = selection[0]
             st.markdown('**Selected {}:** {}'.format(text, x_meta['name']))
         else:
             x_selection = [{'name':''}]
             x_selection += selection
             
             x_id = st.selectbox('Select {}:'.format(text),
                                 range(len(x_selection)), 
                                 format_func=lambda x: x_selection[x]['name'],
                                 index = force_index,
                                 key = param_key)

             if x_id>0:
                 x_meta = x_selection[x_id]

    return {'return':0, 'meta':x_meta}

##################################################################################
def get_with_complex_key_safe(meta, key):
    v = get_with_complex_key(meta, key)

    if v == None: v=''

    return v

##################################################################################
def get_with_complex_key(meta, key):

    j = key.find('.')
    
    if j<0:
        return meta.get(key)

    key0 = key[:j]

    if key0 not in meta:
        return None

    return get_with_complex_key(meta[key0], key[j+1:])

