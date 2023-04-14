# Developer(s): Grigori Fursin

import cmind

def page(st, params, parent):

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
                 '''.format(parent.make_url(meta['uid'], action='contributors', md=False))

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
                        md+="  * {}\n".format(parent.make_url(c, action='challenges', key='tags'))

                    st.markdown(md)

        else:
           st.markdown('**Warning:** Contributor "{}" not found!'.format(name))

        return {'return':0, 'end_html':end_html}


    return page_list(st, params, parent)


def page_list(st, params, parent):
    # Read all contributors
    r = cmind.access({'action':'find',
                      'automation':'contributor,68eae17b590d4f8f'})
    if r['return']>0: return r

    lst = r['list']

    # Prepare the latest contributors

    md_people = ''
    md_org = ''
#    for l in sorted(lst, key=lambda x: (-int(x.meta.get('last_participation_date','0')),
    for l in sorted(lst, key=lambda x: x.meta.get('name',x.meta.get('organization','')).lower()):
        lpd = l.meta.get('last_participation_date','')

        if lpd=='2022' or lpd=='-':
            continue

        if lpd!='':
            uid = l.meta['uid']
            alias = l.meta['alias']
            name = l.meta.get('name', '')
            org = l.meta.get('organization', '')

            if name!='':
                md_people += '* '+parent.make_url(name, alias=uid)+'\n'
            elif org!='':
                md_org += '* '+parent.make_url(org, alias=alias)+'\n'


    if md_people!='':
        st.markdown("### The latest contributors (individuals)")
        st.markdown('Huge thanks to all our contributors for supporing this community project:')
        st.markdown(md_people)


    if md_org!='':
        st.markdown("### The latest contributors (organizations)")
        st.markdown(md_org)

    # Prepare list of all contributors

    md = ''
    for l in sorted(lst, key=lambda x: x.meta.get('name',x.meta.get('organization','')).lower()):
        md += prepare_name(parent, l.meta)

    if md!='':
       st.markdown("### All contributors")
       st.markdown(md)

    return {'return':0}


def prepare_name(parent, meta):
    alias = meta['alias']
    name = meta.get('name', '')
    org = meta.get('organization', '')

    md = ''
    if name!='':
        md = '* '+parent.make_url(name, alias=alias)+'\n'
    elif org!='':
        md = '* *'+parent.make_url(org, alias=alias)+'*\n'
  
    return md
