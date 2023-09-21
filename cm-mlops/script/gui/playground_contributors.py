# Developer(s): Grigori Fursin

import cmind
import misc
import os

def page(st, params):

    url_prefix = st.config.get_option('server.baseUrlPath')+'/'

    name = params.get('name',[''])[0].lower()

    list_all = False

    if name!='':
        r=cmind.access({'action':'load',
                        'automation':'contributor,68eae17b590d4f8f',
                        'artifact':name})
        if r['return']>0 and r['return']!=16:
            return r

        end_html = ''

        if r['return']==0:
            meta = r['meta']

            path = r['path']

            name = meta.get('name',meta.get('organization',''))
            if name!='':
                st.markdown("#### "+name)

                x=''
                for t in meta.get('trophies',[]):
                    url = t.get('url','')
                    if url != '':
                        x+='<a href="{}">&#127942</a>&nbsp;'.format(url)

                if x!='':
                    st.write('<h2>'+x+'</h2>', unsafe_allow_html = True)

                end_html='''
                 <center>
                  <small><a href="{}"><i>Self link</i></a></small>
                 </center>
                 '''.format(misc.make_url(meta['uid'], action='contributors', md=False))

                org = meta.get('organization','')
                if org!='':
                    st.markdown("* **Organization:** "+org)

                urls = meta.get('urls',[])

                url = meta.get('url', '')
                if url!='': urls.append(url)

                if len(urls)>0:
                    x = '* **Web page:** '
                    md = ''
                    if len(urls)>1:
                        md = '* **Web pages:**\n'
                        x='   * '

                    for u in urls:
                        md+=x+'[{}]({})\n'.format(u,u)

                    st.markdown(md)

                ongoing = meta.get('ongoing',[])

                x = str(calculate_points(meta))
                y1 =''
                y2 = ''
                if len(ongoing)>0:
                    y1 = '*'
                    y2 = ' (ongoing)*'
                st.markdown("* **Points: {}{}{}**".format(y1,x,y2))
#                st.write('<h2>'+x+'</h2>', unsafe_allow_html = True)

                if len(ongoing)>0:
                    x = "* **Ongoing challenges:**\n"

                    for t in ongoing:
                        if t != '':
                            x+="   - {}\n".format(misc.make_url(t, action='challenges', key='tags'))

                    st.markdown(x)

                challenges = meta.get('challenges',[])
                if len(challenges)>0:
                    md = "* **Contributions:**\n"

                    for c in sorted(challenges):
                        md+="  * {}\n".format(misc.make_url(c, action='challenges', key='tags'))

                    st.markdown(md)

                # Check if README
                md = ''
                
                readme = os.path.join(path, 'README.md')
                if os.path.isfile(readme):
                    
                    r = cmind.utils.load_txt(readme)
                    if r['return']>0: return r

                    md += r['string']

                st.markdown('---')
                st.markdown(md)


        else:
           st.markdown('**Warning:** Contributor "{}" not found!'.format(name))

        return {'return':0, 'end_html':end_html}


    return page_list(st, params)


def page_list(st, params):
    import pandas as pd
    import numpy as np

    # Read all contributors
    r = cmind.access({'action':'find',
                      'automation':'contributor,68eae17b590d4f8f'})
    if r['return']>0: return r

    lst = r['list']

    # Prepare the latest contributors
    all_data = []
    keys = [
            ('name', 'Name', 400, 'leftAligned'),
            ('points', 'Points', 80,'rightAligned'),
#            ('ongoing_number', 'Ongoing challenges', 80, 'rightAligned'),
            ('trophies', 'Trophies', 80,'rightAligned')
           ]


    url_prefix = st.config.get_option('server.baseUrlPath')+'/'

    md_people = ''
    md_org = ''
#    for l in sorted(lst, key=lambda x: (-int(x.meta.get('last_participation_date','0')),
#    for l in sorted(lst, key=lambda x: x.meta.get('name', x.meta.get('organization','')).lower()):

    for l in lst:

        row = {}

        m = l.meta

        # Skip from stats 
        if m.get('skip', False):
            continue

        lpd = m.get('last_participation_date', '')
        trophies = m.get('trophies', [])
        ongoing = m.get('ongoing', [])

#        if lpd=='-' or (lpd!='' and int(lpd)<2023) :
#            continue
#
#        if len(ongoing)==0 and len(trophies)==0:
#            continue

#        if lpd!='':
        if True:
            uid = m['uid']
            alias = m['alias']
            name = m.get('name', '')
            org = m.get('organization', '')

            row['name_to_print'] = name if name!='' else org


            # Registration in the CK challenges gives 1 point
            y1 =''
            y2 = ''
            if len(ongoing)>0:
                y1 = '*'
                y2 = ' (ongoing)*'

            row['points'] = calculate_points(m)

            row['ongoing_number'] = len(ongoing)
            x = ''
            for t in ongoing:
                if t != '':
                    url = url_prefix + '?action=challenges&tags={}'.format(t)
                    x+='<a href="{}" target="_blank">{}</a><br>'.format(url,t.replace('-', '&nbsp;').replace(',','&nbsp;'))

            row['ongoing'] = x

            name2 = ''

            if name!='':
                url = misc.make_url(name, alias=uid, md = False)
                md_people += '* '+ misc.make_url(name, alias=uid) +'\n'

                if org!='':
                    name2 = ' ({})'.format(org)

            elif org!='':
                url = misc.make_url(org, alias=alias, md = False)
                md_org += '* '+ misc.make_url(org, alias=alias) +'\n'
                name = org

            row['name'] = '<a href="{}" target="_blank">{}</a><i>{}</i>'.format(url_prefix + url, name, name2)

            row['trophies_number'] = len(trophies)
            x = ''
            for t in trophies:
                url = t.get('url','')
                if url != '':
                    x+='<a href="{}" target="_blank">&#127942;</a>&nbsp;'.format(url)

            row['trophies'] = x


            all_data.append(row)


    # Visualize table
    pd_keys = [v[0] for v in keys]
    pd_key_names = [v[1] for v in keys]
    pd_all_data = []
    for row in sorted(all_data, key=lambda row: (row.get('ongoing_number',0)<=0,
                                                 -row.get('points',0),
                                                 -row.get('trophies_number',0),
                                                 name_to_sort(row))):
        pd_row=[]
        for k in pd_keys:
            pd_row.append(row.get(k))
        pd_all_data.append(pd_row)

    df = pd.DataFrame(pd_all_data, columns = pd_key_names)

    df.index+=1

    x = '''
        <center>
         <i>
          <i>
           Check <a href="{}?action=challenges">on-going challenges</a> 
           and register <a href="https://github.com/mlcommons/ck/blob/master/platform/register.md">here</a>
           to be added to this leaderboard.
          </i>
         </i>
        </center>
        <br>
        '''.format(url_prefix)

    st.write(x, unsafe_allow_html = True)

    st.write('<center>'+df.to_html(escape=False, justify='left')+'</center>', unsafe_allow_html=True)
    


#    from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
#    from st_aggrid.shared import JsCode
#
#    gb = GridOptionsBuilder.from_dataframe(df, editable=False)
#
#    for k in keys:
#        gb.configure_column(
#            k[1],
#            headerName=k[1],
#            width=k[2],
#            type=k[3],
#            cellRenderer=JsCode("""
#                class UrlCellRenderer {
#                  init(params) {
#                    this.eGui = document.createElement('a');
#                    this.eGui.innerHTML = params.value;
#                  }
#                  getGui() {
#                    return this.eGui;
#                  }
#                }
#            """)
#        )
#
#    AgGrid(df,
#           gridOptions=gb.build(),
#           updateMode=GridUpdateMode.VALUE_CHANGED,
#           enable_enterprise_modules=False,
#           allow_unsafe_jscode=True)

#    st.write(grid) #, unsafe_allow_html = True)

#    st.dataframe(df)
#    st.write(df.to_html(escape = False), unsafe_allow_html = True)


#    if md_people!='':
#        st.markdown("### The latest contributors (individuals)")
#        st.markdown('Huge thanks to all our contributors for supporing this community project:')
#        st.markdown(md_people)


#    if md_org!='':
#        st.markdown("### The latest contributors (organizations)")
#        st.markdown(md_org)

    # Prepare list of all contributors

#    md = ''
#    for l in sorted(lst, key=lambda x: x.meta.get('name',x.meta.get('organization','')).lower()):
#        md += prepare_name(l.meta)
#
#    if md!='':
#       st.markdown("### All contributors (individuals and orgs)")
#       st.markdown(md)

    return {'return':0}


def name_to_sort(meta):
    name = meta.get('name_to_print', '')

    xname = name.split(' ')

    sname = xname[-1].lower()

    return sname


def calculate_points(meta):

    points = 1

    xpoints = meta.get('points',[])
    for x in xpoints:
        points += int(x.get('point',0))

    # Automatic challenges
    points += len(meta.get('challenges',[]))
    points += len(meta.get('ongoing',[]))
    
    return points


def prepare_name(meta):
    alias = meta['alias']
    name = meta.get('name', '')
    org = meta.get('organization', '')

    md = ''
    if name!='':
        md = '* '+misc.make_url(name, alias=alias)+'\n'
    elif org!='':
        md = '* *'+misc.make_url(org, alias=alias)+'*\n'
  
    return md
