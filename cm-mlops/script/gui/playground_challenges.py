# Developer(s): Grigori Fursin

import cmind
import os

def page(st, params, parent):

    name = params.get('name',[''])[0].strip()
    tags = params.get('tags',[''])[0].lower()

    ii = {'action':'find',
          'automation':'challenge,3d84abd768f34e08'}

    if name!='':
        ii['artifact']=name
    if tags!='':
        ii['tags']=tags

    r = cmind.access(ii)
    if r['return']>0: return r

    lst = r['list']

    end_html = ''

    if len(lst)==0:
        st.markdown('Challenge was not found')
    else:
        artifact = None

        if len(lst)==1:
            artifact = lst[0]
        else:
            challenges = ['']
            artifacts = [None]

            for l in sorted(lst, key=lambda x: (-int(x.meta.get('date','0')),
                                                x.meta.get('title',''))):

                meta = l.meta
                name = meta.get('title', meta['alias'])

                challenges.append(name)
                artifacts.append(l)

            challenge = st.selectbox('Select your optimization and reproducibility challenge', 
                                     range(len(challenges)), 
                                     format_func=lambda x: challenges[x],
                                     index=0, key='challenge')

            if challenge>0:
                artifact = artifacts[challenge]

        # Process 1 challenge
        if artifact is not None:
            meta = artifact.meta

            name = meta.get('title', meta['alias'])

            st.write('''
             <center>
              <h4>Challenge: {}</h4>
             </center>
             '''.format(name),
             unsafe_allow_html=True
             )

            end_html='<center><small><i><a href="{}">Self link</a></i></small></center>'.format(parent.make_url(meta['alias'], action='challenges', md=False))

            date_print = meta.get('date_print','')
            if date_print!='':
                st.markdown('* **Publication date:** {}'.format(date_print))

            deadline_print = meta.get('deadline_print','')
            if deadline_print!='':
                st.markdown('* **Deadline:** {}'.format(deadline_print))

            urls = meta.get('urls',[])
            url = meta.get('url', '')

            if url!='': urls.append(url)

            if len(urls)>0:
                x = '* **External link:** '
                md = ''
                if len(urls)>1:
                    md = '* **External links:**\n'
                    x='   * '

                for u in urls:
                    md+=x+'[{}]({})\n'.format(u,u)
                st.markdown(md)


            # Check if has linked experiments
            experiments = meta.get('experiments',[])

            if len(experiments)>0:
                md = '* **Shared experiments:**\n'

                for e in experiments:
                    tags = e.get('tags','')
                    name = e.get('name','')

                    if tags!='':
                        md+='  * '+parent.make_url(tags, action='experiments', key='tags')
                    elif name!='':
                       md+='  * '+parent.make_url(name, action='experiments')

                st.markdown(md)

            # Check if has text
            path = artifact.path

            for f in ['README.md', 'info.html']:
                f1 = os.path.join(path, f)
                if os.path.isfile(f1):
                    r = cmind.utils.load_txt(f1)
                    if r['return']>0: return r

                    s = r['string']

                    st.markdown('---')

                    if f.endswith('.html'):
                        y = s.split('\n')
                        ss = ''
                        for x in y:
                            ss+=x.strip()+'\n'

                        st.write(ss, unsafe_allow_html=True)
                    else:
                        st.markdown(s)

                    break

    return {'return':0, 'end_html':end_html}
