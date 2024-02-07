# Developer(s): Grigori Fursin

import cmind
import os
import datetime
import misc

def page(st, params):

    url_prefix = st.config.get_option('server.baseUrlPath')+'/'

    name = params.get('name',[''])[0].strip()
    tags = params.get('tags',[''])[0].lower()

    ii = {'action':'find',
          'automation':'report,6462ecdba2054467'}

    if name!='':
        ii['artifact']=name
    if tags!='':
        ii['tags']=tags

    r = cmind.access(ii)
    if r['return']>0: return r

    lst = r['list']

    end_html = ''

    ##############################################################################
    if len(lst)==0:
        st.markdown('Reports were not found!')

    ##############################################################################
    elif len(lst)==1:
        l = lst[0]

        meta = l.meta

        uid = meta['uid']

        title = meta.get('title', meta['alias'])

        path = l.path

        x = '''
            <center>
             <h3>Community report</h3>
             <h5>{}</h5>
            </center>
            '''.format(title)

        st.write(x, unsafe_allow_html = True)

        end_html='<center><small><i><a href="{}">Self link</a></i></small></center>'.format(misc.make_url(meta['uid'], action='reports', md=False))


        # Check basic password
        password_hash = meta.get('password_hash','')
        view = True
        if password_hash!='':
            view = False

            password = st.text_input("Enter password", type="password", key="password")

            if password!='':
                import bcrypt
                # TBD: temporal hack to demo password protection for experiments
                password_salt = b'$2b$12$ionIRWe5Ft7jkn4y/7C6/e'
                password_hash2 = bcrypt.hashpw(password.encode('utf-8'), password_salt)

                if password_hash.encode('utf-8')==password_hash2:
                    view=True
                else:
                    st.markdown('**Warning:** wrong password')

        if not view:
            return {'return':0, 'end_html':end_html}

        # Check if has text
        for f in ['README.md']:
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


    ##############################################################################
    else:
        reports = []

        md = ''

        for l in sorted(lst, key=lambda x: x.meta.get('date',''), reverse=True):

            meta = l.meta

            if meta.get('private',False):
                continue

            uid = meta['uid']

            title = meta.get('title', meta['alias'])

            url = meta.get('redirect','')
            if url == '':
                url = url_prefix + '?action=reports&name={}'.format(uid)

            md += '* ['+title+']('+url+')\n'

        x = '''
            <center>
             <h3>Community reports</h3>
            </center>
            '''
        st.write(x, unsafe_allow_html = True)
        
        st.markdown(md)
    
    return {'return':0, 'end_html':end_html}
