# Developer(s): Grigori Fursin

import cmind

def page(st, params):

    name = params.get('name',[''])[0].strip()
    tags = params.get('tags',[''])[0].lower().replace(',',' ')

    if tags=='' and name=='': 
        tags='mlperf-inference all'

    if name=='':
        tags = st.text_input('Search for reproducibility and optimization experiments by tags:', value=tags, key='tags').strip()

    if name!='' or tags!='':

        # Get all experiment names
        ii = {'action':'find', 
              'automation':'experiment,a0a2d123ef064bcb'}

        if name!='':
            ii['artifact']=name

        if tags!='':
            ii['tags']=tags.strip().replace(' ',',')

        r = cmind.access(ii)
        if r['return']>0: return r

        lst = r['list']

        if len(lst)==0:
            st.markdown('No experiments found.')
        else:

            artifact = None

            if len(lst)==1:
                artifact = lst[0]
            else:
                experiments = ['']
                artifacts = [None]

                for l in sorted(lst, key=lambda x: ','.join(x.meta.get('tags',[]))):
                    meta = l.meta
                    name = meta.get('title', ','.join(meta.get('tags',[])))

                    experiments.append(name)
                    artifacts.append(l)

                select = st.selectbox('Select experiment from {} found entries:'.format(len(lst)),
                                       range(len(experiments)), 
                                       format_func=lambda x: experiments[x],
                                       index=0, key='experiment')

                if select>0:
                    artifact = artifacts[select]

            # Process 1 experiment
            if artifact is not None:
                # Check basic password
                password_hash = artifact.meta.get('password_hash','')
                view = True
                if password_hash!='':
                    view = False

                    password = st.text_input("Enter password", type="password", key="password")

                    if password!='':
                        import bcrypt
#                        salt = bcrypt.gensalt()
                        # TBD: temporal hack to demo password protection for experiments
#                        salt = bcrypt.gensalt()
                        password_salt = b'$2b$12$ionIRWe5Ft7jkn4y/7C6/e'
                        password_hash2 = bcrypt.hashpw(password.encode('utf-8'), password_salt)

                        if password_hash.encode('utf-8')==password_hash2:
                            view=True
                        else:
                            st.markdown('**Warning:** wrong password')

                if view:
                    from playground_experiments_graph import page as page2
                    return page2(st, params, artifact)

    return {'return':0}
