# Support functions

##########################################################
def make_url(name, alias='', action='contributors', key='name', md=True, skip_url_quote=False):

    import urllib

    if alias == '': alias = name

    xaction = 'action={}&'.format(action) if action!='' else ''

    x = urllib.parse.quote_plus(alias) if not skip_url_quote else alias

    url = '?{}{}={}'.format(xaction, key, x)

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
