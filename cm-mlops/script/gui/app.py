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
                              'automation':'script', 
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
            title = 'GUI for the CK2 (CM) script "{}"'.format(script_alias)
        else:
            title = 'GUI for CK2 (CM)'

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

                st_variations[group_key] = st.selectbox(group_key_cap, sorted(y), index=selected_index, key=group_key)
            elif group_key == '*no-group*':
                for variation_key in sorted(variation_groups[group_key]):
                    st_variations[variation_key] = st.checkbox(variation_key.capitalize(), key=variation_key)


        # Prepare inputs
        input_desc=meta.get('input_description',{})

        if len(input_desc)>0:
            st.markdown("""---""")
            st.subheader('Script flags')
            
            for key in input_desc:
                value = input_desc[key]

                if type(value) == dict:
                    desc = value['desc']

                    choices = value.get('choices', [])
                    boolean = value.get('boolean', False)
                    default = value.get('default', '')

                    if boolean:
                        st_inputs[key] = st.checkbox(desc, value=default, key=key)
                    elif len(choices)>0:
                        selected_index = choices.index(default) if default!='' else 0
                        st_inputs[key] = st.selectbox(desc, choices, index=selected_index, key=key)
                    else:
                        st_inputs[key] = st.text_input(desc, value=default, key=key)
                        
                else:
                    desc = value
                    st_inputs[key] = st.text_input(desc)


    # Check tags
    selected_variations=[]
    for k in st_variations:
        v = st_variations[k]
        if type(v)==bool:
            if v:
                selected_variations.append('_'+k)
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

        if value!='' and (type(value)!=bool or value==True):
            flags+=' --'+key
            if type(value)!=bool:
                flags+='='+str(value)
    
    ########################################################
    # Extra CMD
    st.markdown("""---""")
    cmd_extension = st.text_input("CM Command Line extension")

    # Prepare CLI
    cli = 'cm run script {} {} {}'.format(tags, flags, cmd_extension)

    if no_run=='':
        cli+=' --pause'

    # Print CLI
    st.markdown("""---""")
    cli = st.text_area('**Generated CM Command Line**', cli)

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

if __name__ == "__main__":
    main()
