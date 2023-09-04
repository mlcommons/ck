# Support functions

def make_url(name, alias='', action='contributors', key='name', md=True):

    import urllib

    if alias == '': alias = name

    xaction = 'action={}&'.format(action) if action!='' else ''

    url = '?{}{}={}'.format(xaction, key, urllib.parse.quote_plus(alias))

    if md:
        md = '[{}]({})'.format(name, url)
    else:
        md = url

    return md

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
