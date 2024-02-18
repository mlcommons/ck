# Developer(s): Grigori Fursin

import streamlit as st
import os
import cmind

import misc

def page(i):

    st = i['st']
    params = i['params']
    script_path = i['script_path']
    script_alias = i['script_alias']
    script_tags = i['script_tags']
    skip_bottom = i.get('skip_bottom', False)

    meta = i['script_meta']
    repo_meta = i.get('script_repo_meta', None)

    no_run = os.environ.get('CM_GUI_NO_RUN', '')

    gui_meta = meta.get('gui',{})

    gui_func = gui_meta.get('use_customize_func', '')
    if gui_func!='':
        ii = {'streamlit_module':st,
              'meta':meta}
        return cmind.utils.call_internal_module(None, os.path.join(script_path, 'dummy') , 
                                                'customize', gui_func, ii)

    st.markdown("""---""")

    if gui_meta.get('title','')!='':
        title = gui_meta['title']


    # Set title
#    st.title('[Collective Mind](https://github.com/mlcommons/ck)')

    url_script = 'https://github.com/mlcommons/ck'
    if repo_meta != None and script_alias!='':
        url = repo_meta.get('url','')
        if url=='' and repo_meta.get('git', False):
            url = 'https://github.com/'+repo_meta['alias'].replace('@','/')

        if url!='':
            # Recreate GitHub path
            if not url.endswith('/'): url=url+'/'

            url += 'tree/master/'

            if repo_meta.get('prefix','')!='':
                url += repo_meta['prefix']

            if not url.endswith('/'): url=url+'/'
            
            url += 'script/'+script_alias

            url_script = url

    if script_alias!='':
        st.markdown('**Customize input for the CM script "[{}]({})":**'.format(script_alias, url_script))

    host_os_index = 0 if os.name != 'nt' else 1
    host_os_selection = ['Linux/MacOS', 'Windows']
    host_os = st.selectbox('Select host OS where you will run CM:', host_os_selection, index=host_os_index, key='host_os')
    var1 = '^' if host_os == 'Windows' else '\\'

    # Check if found path and there is meta
    # TBD (Grigori): need to cache it using @st.cache
    variation_groups = {}
    default_variations = []
    variation_md = {}
    variation_alias = {}

    st_inputs = {}

    st_variations = {}

    if len(meta)>0:
        variations = meta.get('variations',{})

        default_variation = meta.get('default_variation','')

        variation_keys = sorted(list(variations.keys()))

        for variation_key in sorted(variation_keys):
            variation = variations[variation_key]

            alias = variation.get('alias','').strip()

            if alias!='':
                aliases = variation_alias.get(alias, [])
                if variation_key not in aliases: 
                    aliases.append(variation_key)
                variation_alias[alias]=aliases

                # Do not continue this loop if alias
                continue

            if 'default_gui' in variation:
                default = variation['default_gui']
            else:
                default = variation.get('default', False)

            if not default:
                # Check outdated
                if default_variation == variation_key:
                    default = True

            extra1 = ''
            extra2 = ''
            if default:
                extra1 = '**'
                extra2 = '** (default)'

                default_variations.append(variation_key)

            group = variation.get('group','')

            if variation_key.endswith('_'):
                group = '*internal*'
            elif group == '':
                group = '*no-group*'

            if group not in variation_groups:
                variation_groups[group]=[]

            variation_groups[group].append(variation_key)

        # Prepare variation_groups
#            st.markdown("""---""")
        if len(variations)>0:
             st.markdown('**Select variations to update multiple flags and environment variables:**')

             variation_groups_order = meta.get('variation_groups_order',[])
             for variation in sorted(variation_groups):
                 if variation not in variation_groups_order:
                     variation_groups_order.append(variation)

             for group_key in variation_groups_order:
                 group_key_cap = group_key.replace('-',' ').capitalize()
                 if not group_key.startswith('*'):
                     y = ['']

                     index = 0
                     selected_index = 0
                     for variation_key in sorted(variation_groups[group_key]):
                         index += 1
                         y.append(variation_key)
                         if variation_key in default_variations:
                             selected_index=index

                     key2 = '~~'+group_key

                     x = params.get(key2, None)
                     if x!=None and len(x)>0 and x[0]!=None:
                         x = x[0]
                         if x in y:
                             selected_index = y.index(x) if x in y else 0
                     
                     st_variations[key2] = st.selectbox(group_key_cap, sorted(y), index=selected_index, key=key2)

                 elif group_key == '*no-group*':
                     for variation_key in sorted(variation_groups[group_key]):
                         v = False
                         if variation_key in default_variations:
                             v=True

                         key2 = '~'+variation_key

                         x = params.get(key2, None)
                         if x!=None and len(x)>0 and x[0]!=None:
                             if x[0].lower()=='true':
                                 v = True
                             elif x[0].lower()=='false':
                                 v = False
                         
                         st_variations[key2] = st.checkbox(variation_key.capitalize(), key=key2, value=v)


        # Prepare inputs
        input_desc=meta.get('input_description',{})

        if len(input_desc)>0:
            
            sort_desc = {}
            sort_keys = []
            for k in input_desc:
                sort = input_desc[k].get('sort',0)
                if sort>0:
                    sort_desc[k]=sort
            if len(sort_desc)>0:
                sort_keys = sorted(sort_desc, key = lambda k: sort_desc[k])

            other_keys = sorted([k for k in input_desc if input_desc[k].get('sort',0)==0])
            
            all_keys = [] if len(sort_keys)==0 else sort_keys
            all_keys += other_keys

            if len(sort_keys)>0:
                st.markdown('**Select main flags:**')
            else:
                st.markdown('**Select all flags:**')

            other_flags = False
            for key in all_keys:
                value = input_desc[key]

                if len(sort_keys)>0 and value.get('sort',0)==0 and not other_flags:
                    st.subheader('Other flags')
                    other_flags = True

                ii={'key':key,
                    'desc':value,
                    'params':params,
                    'st':st,
                    'st_inputs':st_inputs}
                
                r2 = misc.make_selector(ii)
                if r2['return']>0: return r2

    # Check tags
    selected_variations=[]
    for k in st_variations:
        v = st_variations[k]

        if k.startswith('~~'):
            k2 = k[2:]
        elif k.startswith('~'):
            k2 = k[1:]

        if type(v)==bool:
            if v:
                selected_variations.append('_'+k2)
        elif v!='':
            selected_variations.append('_'+v)

    x = script_tags
    if ' ' in script_tags:
        if len(selected_variations)>0:
            x+=' '+' '.join(selected_variations)

        tags = '"{}"'.format(x)
    else:
        if len(selected_variations)>0:
            x+=','+','.join(selected_variations)

        tags = '--tags={}'.format(x)

    # Check flags
    flags_dict = {}
    flags = ''
    for key in st_inputs:
        value = st_inputs[key]
        key2 = key[1:]

        if value!='' and (type(value)!=bool or value==True):
            flags+=' '+var1+'\n   --'+key2

            z = True
            if type(value)!=bool:
                x = str(value)
                z = x

                if ' ' in x or ':' in x or '/' in x or '\\' in x: 
                    x='"'+x+'"'
                flags+='='+x

            flags_dict[key2]=z

    ########################################################
    # Extra CMD
    st.markdown("""---""")
    cmd_extension = st.text_input("Add extra to CM script command line").strip()

    run_via_docker = False
    if len(meta.get('docker',{}))>0:
        run_via_docker = st.checkbox('Run via Docker', key='run_via_docker', value=False)

    # Prepare CLI
    action = 'docker' if run_via_docker else 'run'
    cli = 'cm {} script {} {} '.format(action, tags, flags,)

    x = '' if cmd_extension=='' else var1+'\n   '+cmd_extension
    
    if x!='':
        cli+=var1+x

    cli+='\n'

#    if no_run=='':
#        cli+='   --pause\n'

    
    # Print CLI
    st.markdown("""---""")

    x = 'pip install cmind -U\n\ncm pull repo mlcommons@ck\n\ncm rm cache -f\n'

    # Hack to detect python virtual environment and version
    python_venv_name=st_inputs.get('@adr.python.name', '')
    python_ver=st_inputs.get('@adr.python.version', '')
    python_ver_min=st_inputs.get('@adr.python.version_min', '')

    y = ''
    if python_venv_name!='':# or python_ver!='' or python_ver_min!='':
        y = '\ncm run script "get sys-utils-cm"\n'

        if python_venv_name!='':
            y+='cm run script "install python-venv" --name='+str(python_venv_name)
        else:
            y+='cm run script "get python"'

        if python_ver!='':
            y+=' --version='+str(python_ver)

        if python_ver_min!='':
            y+=' --version_min='+str(python_ver_min)

    if y!='':
        x+=y


    st.markdown("**Install [MLCommons CM](https://github.com/mlcommons/ck/blob/master/docs/installation.md) with a few dependencies and clean CM cache (optional):**")
    
    st.markdown('```bash\n{}\n```\n'.format(x))

   
#    st.text_area('**Install [MLCommons CM](https://github.com/mlcommons/ck/blob/master/docs/installation.md) with a few dependencies and clean CM cache (optional):**', x, height=200)


    st.markdown("**Run CM script from Python:**")

    # Python API
    dd = {
          'action':action,
          'automation':'script,5b4e0237da074764',
          'tags':script_tags
         }

    x = script_tags
    if len(selected_variations)>0:
        for sv in selected_variations:
            x+=' '+sv
         
    dd['tags']=x.replace(' ',',')

    dd.update(flags_dict)

    import json
    dd_json=json.dumps(dd, indent=2)

    y = 'import cmind\n'
    y+= 'r = cmind.access('+dd_json+')\n'
    y+= 'if r[\'return\']>0: print (r)\n'

    x='''
```python
          {}
      '''.format(y)

#    st.write(x.replace('\n','<br>\n'), unsafe_allow_html=True)

    st.markdown(x)

    
    cli = st.text_area('**Run CM script from command line:**', cli, height=500)



    # Add explicit button "Run"
    if no_run=='' and st.button("Run in the new terminal"):
        cli = cli+var1+'--pause\n'

        cli = cli.replace(var1, ' ').replace('\n',' ')

        if os.name == 'nt':
            cmd2 = 'start cmd /c {}'.format(cli)
        else:
            cli2 = cli.replace('"', '\\"')

            prefix = os.environ.get('CM_GUI_SCRIPT_PREFIX_LINUX','')
            if prefix!='': prefix+=' '

            cmd2 = prefix + 'bash -c "{}"'.format(cli2)

        print ('Running command:')
        print ('')
        print ('  {}'.format(cmd2))
        print ('')

        os.system(cmd2)

    if not skip_bottom:
        st.markdown("""---""")
        st.markdown("*Learn more about the MLCommons CM interface at [GitHub](https://github.com/mlcommons/ck)"
                    " and report issues or suggest features [here](https://github.com/mlcommons/ck/issues).*")

    return {'return':0}

if __name__ == "__main__":
    main()
