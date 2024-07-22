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

    extra = i.get('extra', {})

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

    hide = params.get('hide_script_customization', False)
    
    if script_alias!='':
        show_customize = st.toggle('**Customize input for the CM script "[{}]({})"**'.format(script_alias, url_script), value = not hide)
        hide = not show_customize


    
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
        if len(variations)>0:
             if not hide:
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
                     
                     if hide:
                         st_variations[key2] = sorted(y)[selected_index]
                     else:
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
                         
                         if hide:
                             st_variations[key2] = v
                         else:
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

            if not hide:
                if len(sort_keys)>0:
                    st.markdown('**Select main flags:**')
                else:
                    st.markdown('**Select all flags:**')

            other_flags = False
            for key in all_keys:
                value = input_desc[key]

                if len(sort_keys)>0 and value.get('sort',0)==0 and not other_flags:
                    if not hide:
                        st.markdown('**Select other flags:**')
                    other_flags = True

                ii={'key':key,
                    'desc':value,
                    'params':params,
                    'st':st,
                    'st_inputs':st_inputs,
                    'hide':hide}
                
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



    
    # Add extras to inputs
    add_to_st_inputs = extra.get('add_to_st_inputs',{})
    if len(add_to_st_inputs)>0:
        st_inputs.update(add_to_st_inputs)

    
    ############################################################################
    st.markdown("""---""")
    st.markdown('**Run this CM script (Linux/MacOS/Windows):**')


    x = ''

    extra_notes_online = extra.get('extra_notes_online', '')
    if extra_notes_online != '': x+=' [ '+extra_notes_online+' ] '

    extra_faq_online = extra.get('extra_faq_online', '')
    if extra_faq_online != '': x+=' [ '+extra_faq_online+' ] '
    
    if x !='':
        st.markdown('*'+x.strip()+'*')



    host_os_windows = False if os.name != 'nt' else True
    host_os_use_windows = st.toggle('Run on Windows?', value = host_os_windows)
    if host_os_use_windows:
        var1 = '^'
        host_os_flag = 'windows'
#        st.markdown('*Check how to install [a few dependencies](https://github.com/mlcommons/ck/blob/master/docs/installation.md#windows) on Windows.*')
    else:
        var1 = '\\'
        host_os_flag = 'linux'

        
    show_cm_install = st.toggle('Install MLCommons Collective Mind', value=False)

    if show_cm_install:

        import playground_install
        extra = {'skip_header': True,
                 'run_on_windows': host_os_use_windows}
        r = playground_install.page(st, params, extra)
        if r['return']>0: return r

        
        st.markdown('---')


    ############################################################################
    shell = st.toggle('Open shell after executing CM script?', value=False)
    if shell:
        st_inputs['~shell'] = True

    ############################################################################
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


 
    
    
    
    ############################################################################
    run_via_docker = False
    if not extra.get('skip_script_docker_func', False) and len(meta.get('docker',{}))>0:
        run_via_docker = st.toggle('Use Docker', key='run_via_docker', value=False)

        if run_via_docker:
            st.markdown("*WARNING: CM automatically generates containers for a give script - it's a beta functionality - feel free to [test and provide feedback](https://discord.gg/JjWNWXKxwT)!*")

    action = 'docker' if run_via_docker else 'run'
    cli = 'cm {} script {} {}\n'.format(action, tags, flags)


    ############################################################################
    use_experiment_from_extra = extra.get('use_experiment', False)
    
    use_experiment = st.toggle('Use CM experiment for reproducibility', key='use_cm_experiment', value=use_experiment_from_extra)

    extra_cm_prefix = ''
    if use_experiment:
        cli = 'cm run experiment --tags={} -- {}\n '.format("repro,"+script_tags, var1) + cli

    ############################################################################
    
    extra_setup = extra.get('extra_setup','').strip()
    if len(extra_setup)>2:
        show_extra_setup_notes = st.toggle('Show extra setup notes?', value = True)

        if show_extra_setup_notes:
#            st.markdown('---')
            st.markdown(extra_setup)
#            st.markdown('---')

    
    show_python_api = st.toggle('Run via Python API', value=False)

    # Python API
    if show_python_api:
         
         final_script_tags = script_tags
         if len(selected_variations)>0:
             for sv in selected_variations:
                 final_script_tags += ' '+sv
         final_script_tags = final_script_tags.replace(' ',',')
                 
         if use_experiment:
             dd = {
                   'action': 'run',
                   'automation': 'experiment,a0a2d123ef064bcb',
                   'tags': script_tags,
                   'out': 'con'
                  }

             unparsed_cmd = ['cm',
                             'run',
                             'script,5b4e0237da074764',
                             '--tags='+final_script_tags]

             for flag in flags_dict:
                 value = flags_dict[flag]
                 unparsed_cmd.append('--' + flag + '=' + str(value))

             dd['unparsed_cmd'] = unparsed_cmd

         else:
             dd = {
                   'action':action,
                   'automation':'script,5b4e0237da074764',
                  }
                  
             dd['tags']=final_script_tags

             dd['out']='con'
             
             dd.update(flags_dict)

         import json
         dd_json=json.dumps(dd, indent=2)
         dd_json=dd_json.replace(': true', ': True').replace(': false', ': False')

         y = 'import cmind\n'
         y+= 'r = cmind.access('+dd_json+')\n'
         y+= 'if r[\'return\']>0: print (r[\'error\'])\n'

         x='''
     ```python
               {}
           '''.format(y)

     #    st.write(x.replace('\n','<br>\n'), unsafe_allow_html=True)

         st.markdown(x)

    
    
    ############################################################################
    show_cli = st.toggle('Run from the command line', value = True)

    if show_cli:
        # Add explicit button "Run"
        cli = st.text_area('', cli, height=600)
        
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

    # Some info
    x = '''
         <i>
         <center>
         We would like to thank <a href="https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md">all Collective Mind users and contributors</a> 
         for supporting this collaborative engineering effort -<br> 
         please don't hesitate report issues or suggest features at <a href="https://github.com/mlcommons/ck/issues">CM GitHub</a>!
         </center>
        '''
    st.write(x, unsafe_allow_html = True)

    return {'return':0}

if __name__ == "__main__":
    main()
