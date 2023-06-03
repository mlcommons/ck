# Developer(s): Grigori Fursin

import streamlit as st
import os
import cmind

def main():

    query_params = st.experimental_get_query_params()

    script_path = os.environ.get('CM_GUI_SCRIPT_PATH','')
    script_alias = os.environ.get('CM_GUI_SCRIPT_ALIAS','')
    title = os.environ.get('CM_GUI_TITLE', '')
    no_run = os.environ.get('CM_GUI_NO_RUN', '')

    # Check if script tags are specified from CMD
    script_tags = ''
    script_tags_from_url = query_params.get('tags',[''])

    meta = {}
    if len(script_tags_from_url)>0:
        script_tags = script_tags_from_url[0]

        if script_tags !='':
            # Check type of tags
            if ' ' in script_tags:
                script_tags = script_tags.replace(' ',',')

            print ('Searching CM scripts using tags "{}"'.format(script_tags))

            r = cmind.access({'action':'find', 
                              'automation':'script,5b4e0237da074764', 
                              'tags':script_tags})
            if r['return']>0: return r

            lst = r['list']

            if len(lst)==1:
                script = lst[0]
                meta = script.meta
                script_path = script.path
                script_alias = meta['alias']

    if script_tags == '':
        script_tags = os.environ.get('CM_GUI_SCRIPT_TAGS','')

    # Read meta
    if len(meta)==0 and script_path!='' and os.path.isdir(script_path):
        fn = os.path.join(script_path, '_cm')
        r = cmind.utils.load_yaml_and_json(fn)
        if r['return'] == 0:
            meta = r['meta']

    if meta.get('gui_title','')!='':
        title = meta['gui_title']

    # Set title
    if title=='':
        if script_alias!='':
            title = 'GUI for the CM script "{}"'.format(script_alias)
        else:
            title = 'GUI for CM'

    st.title(title)

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
        st.subheader('Script variations')

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

                st_variations['~'+group_key] = st.selectbox(group_key_cap, sorted(y), index=selected_index, key='~'+group_key)
            elif group_key == '*no-group*':
                for variation_key in sorted(variation_groups[group_key]):
                    x = False
                    if variation_key in default_variations:
                        x=True
                    st_variations['#'+variation_key] = st.checkbox(variation_key.capitalize(), key='#'+variation_key, value=x)


        # Prepare inputs
        input_desc=meta.get('input_description',{})

        if len(input_desc)>0:
            st.markdown("""---""")
            st.subheader('Script flags')

            for key in sorted(input_desc, key = lambda x: input_desc[x].get('sort',0)):
                value = input_desc[key]

                key2 = '@'+key

                if type(value) == dict:
                    desc = value['desc']

                    choices = value.get('choices', [])
                    boolean = value.get('boolean', False)
                    default = value.get('default', '')

                    if boolean:
                        st_inputs[key2] = st.checkbox(desc, value=default, key=key2)
                    elif len(choices)>0:
                        selected_index = choices.index(default) if default!='' else 0
                        st_inputs[key2] = st.selectbox(desc, choices, index=selected_index, key=key2)
                    else:
                        st_inputs[key2] = st.text_input(desc, value=default, key=key2)

                else:
                    desc = value
                    st_inputs[key2] = st.text_input(desc)


    # Check tags
    selected_variations=[]
    for k in st_variations:
        v = st_variations[k]
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
    flags = ''
    for key in st_inputs:
        value = st_inputs[key]
        key2 = key[1:]

        if value!='' and (type(value)!=bool or value==True):
            flags+=' \\\n   --'+key2
            if type(value)!=bool:
                x = str(value)
                if ' ' in x or ':' in x or '/' in x or '\\' in x: 
                    x='"'+x+'"'
                flags+='='+x

    ########################################################
    # Extra CMD
    st.markdown("""---""")
    cmd_extension = st.text_input("CM Command Line extension").strip()

    # Prepare CLI
    x = '' if cmd_extension=='' else '\\\n   '+cmd_extension
    
    cli = 'cm run script {} {} {} \\\n'.format(tags, flags, x)

    if no_run=='':
        cli+='   --pause\n'

    # Print CLI
    st.markdown("""---""")

    x = 'python3 -m pip install cmind -U\n\ncm pull repo mlcommons@ck\n'

    # Hack to detect python virtual environment and version
    python_venv_name=st_inputs.get('adr.python.name', '')
    python_ver=st_inputs.get('adr.python.version', '')
    python_ver_min=st_inputs.get('adr.python.version_min', '')

    y = ''
    if python_venv_name!='' or python_ver!='':
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

    st.text_area('**Install [CM (CK2) framework](https://github.com/mlcommons/ck) with a few dependencies:**', x, height=170)

    cli = st.text_area('**Run CM script:**', cli, height=500)


    # Add explicit button "Run"
    if no_run=='' and st.button("Run"):
        if os.name == 'nt':
            cmd2 = 'start cmd /c {}'.format(cli)
        else:
            cli2 = cli.replace('"', '\\"')

            prefix = os.environ.get('CM_GUI_SCRIPT_PREFIX_LINUX','')
            if prefix!='': prefix+=' '

            cmd2 = prefix + 'bash -c "{}"'.format(cli2)

        print ('Running command: {}'.format(cmd2))

        os.system(cmd2)

    st.markdown("""---""")
    st.markdown("*Join the [open MLCommons taskforce](https://github.com/mlcommons/ck/blob/master/docs/mlperf-education-workgroup.md) and the public [Discord channel](https://discord.gg/JjWNWXKxwT) to participate in collaborative developments, benchmarking and design space exploration of ML Systems!"
                " Please report issues or suggest features [here](https://github.com/mlcommons/ck/issues).*")

if __name__ == "__main__":
    main()
