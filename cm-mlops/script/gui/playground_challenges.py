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
        st.markdown('Challenges were not found!')
    else:
        artifact = None

        if len(lst)==1:
            artifact = lst[0]
        else:
            challenges = ['']
            artifacts = [None]

            date_now = datetime.datetime.now().isoformat()
            date_now2 = int(date_now[0:4]+date_now[5:7]+date_now[8:10])

            ongoing = []
            
            for l in sorted(lst, key=lambda x: (
                                                -int(x.meta.get('date_open','0')),
                                                -int(x.meta.get('date_close','0')),
                                                x.meta.get('title','')
                                               )):

                row = {}
                
                meta = l.meta
                row['uid']= meta['uid']
                
                name = meta.get('title', meta['alias'])

                row['name']=name

                for k in ['points', 'trophies', 'prize']:
                    if k in meta:
                        row[k]=meta[k]
                
                under_preparation = meta.get('under_preparation', False)
                row['under_preparation']=under_preparation

                date_open = meta.get('date_open','')
                date_close = meta.get('date_close','')

                s_date_open = ''
                if date_open!='':
                    r = misc.convert_date(date_open)
                    s_date_open = r['string'] if r['return']==0 else ''

                    row['orig_date_open']=date_open
                    row['date_open']=s_date_open

                s_date_close = ''
                if date_close!='':
                    r = misc.convert_date(date_close)
                    s_date_close = r['string'] if r['return']==0 else ''

                    row['orig_date_close']=date_close
                    row['date_close']=s_date_close

                diff1 = 0
                diff2 = 0

                if date_open!='':
                    diff1 = int(date_open)-int(date_now2)

                if date_close!='':
                    diff2 = int(date_close)-int(date_now2)


                prefix = ''
                if under_preparation:
                    prefix = 'Under preparation: '
                else:
                    if date_open!='' and diff1>=0:
                        prefix = 'Opens on {}: '.format(s_date_open)
                    else:
                        if date_close!='':
                            if diff2<0:
                                prefix = 'Finished on {}: '.format(s_date_close)
                            else:
                                prefix = 'Open and finishes on {}: '.format(s_date_close)
                        else:
                            prefix = 'Open: '.format(s_date_close)


                # Check if open challenge even if under preparation
                if date_open and diff1<0 and diff2>0:
                    ongoing.append(row)


                challenges.append(prefix + name)
                artifacts.append(l)

            # Show selector for all
            challenge = st.selectbox('View past benchmarking, optimization, reproducibility and replicability challenges:', 
                                     range(len(challenges)), 
                                     format_func=lambda x: challenges[x],
                                     index=0, key='challenge')

            if challenge>0:
                artifact = artifacts[challenge]

            # Show ongoing if open
            if len(ongoing)>0:
                ind = 1
                
                st.markdown('#### Ongoing challenges')

                x = '''
                    <center>
                     <i>
                      We thank 
                      <a href="https://mlcommons.org">MLCommons organizations</a>, 
                      <a href="https://cTuning.org">cTuning.org</a> and 
                      <a href="https://cKnowledge.org">cKnowledge.org</a>
                      for sponsoring our reproducibility, replicability and optimization challenges!
                      <br>
                      Please contact <a href="https://cKnowledge.org/gfursin">Grigori Fursin</a>
                      if you would like to add or sponsor new challenges!
                      <br>
                      Join our <a href="https://discord.gg/JjWNWXKxwT">Discord server</a> 
                      to ask questions and learn more!</a></center><br>
                     </i>
                    </center>
                    '''
                st.write(x, unsafe_allow_html = True)

                
                for row in sorted(ongoing, key=lambda row: (int(row.get('orig_date_close', 0)),
                                                            row.get('name', ''),
                                                            row.get('under_preparation', False))):
                    md = ''
                    up = row.get('under_preparation', False)

                    x = row['name']
                    y = ''
                    if up:
                        x = x[0].lower() + x[1:]
                        y = '<i>Under preparation:</i> '

                    url = url_prefix + '?action=challenges&name={}'.format(row['uid'])
#                    md += '###### {}) {}[{}]({})\n'.format(str(ind), y, x, url)

                    x = '''
                         <div style="background-color:#dfdfdf">
                          <b>
                          {}) {}<a href="{}">{}</a>
                          </b>
                        </div>
                        '''.format(str(ind), y, url, x)
                    st.write(x, unsafe_allow_html = True)

                    
                    ind+=1

                    # Assemble info
                    x=''
                    
                    date_close = row['date_close']
                    if date_close!='' and date_close!=None:
                        x += '&nbsp;&nbsp;&nbsp;Closing date: **{}**\n'.format(date_close)


                    trophies = row.get('trophies',False)
                    if trophies:
                        x += ' &nbsp;&nbsp;Trophy: **Yes**\n'

                    points = row.get('points',0)
                    if points>0:
                        x += ' &nbsp;&nbsp;Points: **{}**\n'.format(str(points))

                    prize = row.get('prize','')
                    if prize!='':
                        x += ' &nbsp;&nbsp;Prize from [MLCommons organizations]({}): **{}**\n'.format('https://mlcommons.org', prize)

                    
                    if x!='':    
                        md += '&nbsp;&nbsp;&nbsp;&nbsp; '+x

                    st.markdown(md)


        # Process 1 challenge
        if artifact is not None:
            meta = artifact.meta

            name = meta.get('title', meta['alias'])
            uid = meta['uid']

            st.write('''
             <center>
              <h4>Challenge: {}</h4>
             </center>
             '''.format(name),
             unsafe_allow_html=True
             )

            end_html='<center><small><i><a href="{}">Self link</a></i></small></center>'.format(misc.make_url(meta['uid'], action='challenges', md=False))


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



            date_open = meta.get('date_open','')
            if date_open!='':
                # Format YYYYMMDD
                r = misc.convert_date(date_open)
                if r['return']>0: return r
                st.markdown('* **Open date:** {}'.format(r['string']))

            date_close = meta.get('date_close','')
            if date_close!='':
                # Format YYYYMMDD
                r = misc.convert_date(date_close)
                if r['return']>0: return r
                st.markdown('* **Close date:** {}'.format(r['string']))

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
                        md+='  * '+misc.make_url(tags, action='experiments', key='tags')
                    elif name!='':
                       md+='  * '+misc.make_url(name, action='experiments')

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

            # Check associated reports
            r=cmind.access({'action':'find',
                            'automation':'report,6462ecdba2054467',
                            'tags':'challenge-{}'.format(uid)})
            if r['return']>0: return r

            lst = r['list']

            for l in lst:
                report_path = l.path

                f1 = os.path.join(report_path, 'README.md')
                if os.path.isfile(f1):
                    report_meta = l.meta

                    report_alias = report_meta['alias']
                    report_title = report_meta.get('title','')

                    report_name = report_title if report_title!='' else report_alias

                    r = cmind.utils.load_txt(f1)
                    if r['return']>0: return r

                    s = r['string']

                    st.markdown('---')
                    st.markdown('### '+report_name)

                    st.markdown(s, unsafe_allow_html=True)



    return {'return':0, 'end_html':end_html}
