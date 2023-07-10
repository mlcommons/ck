# Developer(s): Grigori Fursin

import cmind
import misc

def page(st, params):

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

            name = meta.get('name',meta.get('organization',''))
            if name!='':
                st.markdown("#### "+name)

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


                challenges = meta.get('challenges',[])
                if len(challenges)>0:
                    md = "* **Contributions:**\n"

                    for c in sorted(challenges):
                        md+="  * {}\n".format(misc.make_url(c, action='challenges', key='tags'))

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
    keys = [('name', 'Name', 250, 'leftAligned'),
            ('trophies', 'Trophies', 100, 'rightAligned'),
            ('points', 'Points', 100,'rightAligned'),
            ('ongoing', 'Ongoing challenges', 200, 'rightAligned')]


    md_people = ''
    md_org = ''
#    for l in sorted(lst, key=lambda x: (-int(x.meta.get('last_participation_date','0')),
    for l in sorted(lst, key=lambda x: x.meta.get('name', x.meta.get('organization','')).lower()):
        
        row = {}
        
        m = l.meta
        
        lpd = m.get('last_participation_date', '')
        trophies = m.get('trophies', [])
        ongoing = m.get('ongoing', [])

        if lpd=='-' or (lpd!='' and int(lpd)<2023) :
            continue

        if len(ongoing)==0 and len(trophies)==0:
            continue

        if lpd!='':
            uid = m['uid']
            alias = m['alias']
            name = m.get('name', '')
            org = m.get('organization', '')

            row['name'] = name if name!='' else org

            points = m.get('points',0)

            # Automatic challenges
            points += len(m.get('challenges',[]))
            points += len(m.get('ongoing',[]))
            
            row['points'] = points

            x = ''
            for t in ongoing:
                if t != '':
                    url = '/?action=challenges&tags={}'.format(t)
                    x+='<a href="{}" target="_blank">{}</a><br>\n'.format(url,t.replace('-', '&nbsp;'))
        
            row['ongoing'] = x
            
            x = ''
            for t in trophies:
                url = t.get('url','')
                if url != '':
                    x+='<a href="{}" target="_blank">&#127942;</a>&nbsp;\n'.format(url)

            row['trophies'] = x

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

            row['name'] = '<a href="{}" target="_blank">{}</a><i>{}</i>'.format('/'+url, name, name2)

            all_data.append(row)


    # Visualize table
    st.markdown("### Current Leaderboard")
    
    pd_keys = [v[0] for v in keys]
    pd_key_names = [v[1] for v in keys]
    pd_all_data = []
    for row in sorted(all_data, key=lambda row: (-len(row.get('ongoing',[])),
                                                 -row.get('points',0))):
        pd_row=[]
        for k in pd_keys:
            pd_row.append(row.get(k))
        pd_all_data.append(pd_row)

    df = pd.DataFrame(pd_all_data, columns = pd_key_names)
    
    from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
    from st_aggrid.shared import JsCode

    gb = GridOptionsBuilder.from_dataframe(df, editable=False)

    for k in keys:
        gb.configure_column(
            k[1],
            headerName=k[1],
            width=k[2],
            type=k[3],
            cellRenderer=JsCode("""
                class UrlCellRenderer {
                  init(params) {
                    this.eGui = document.createElement('a');
                    this.eGui.innerHTML = params.value;
                  }
                  getGui() {
                    return this.eGui;
                  }
                }
            """)
        )

    AgGrid(df,
           gridOptions=gb.build(),
           updateMode=GridUpdateMode.VALUE_CHANGED,
           enable_enterprise_modules=False,
           allow_unsafe_jscode=True)

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

    md = ''
    for l in sorted(lst, key=lambda x: x.meta.get('name',x.meta.get('organization','')).lower()):
        md += prepare_name(l.meta)

    if md!='':
       st.markdown("### All contributors (individuals and orgs)")
       st.markdown(md)

    return {'return':0}


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
