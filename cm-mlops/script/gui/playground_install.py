# Developer(s): Grigori Fursin

import cmind
import os
import datetime
import misc

def page(st, params, extra):

    end_html = ''
    
    url_prefix = st.config.get_option('server.baseUrlPath')+'/'

    if not extra.get('skip_header', False):
        st.markdown('---')
        st.markdown('**Install [MLCommons Collective Mind automation framework](https://github.com/mlcommons/ck):**')
    


    md = ''
    
    ###################################################################
    # Select OS
    choices = [('Ubuntu, Debian and similar Linux', 'linux'),
               ('Red Hat and CentOS', 'redhat'),
               ('MacOS', 'macos'),
               ('Windows', 'windows')]

    host_os_selection = 0

    if extra.get('run_on_windows', False):
        host_os_selection = 3

    host_os = st.selectbox('Select your host OS:', 
                           range(len(choices)),
                           format_func = lambda x: choices[x][0], 
                           index = host_os_selection, 
                           key = 'install_select_host_os')

    host_os_index = choices[host_os][1]


    cur_script_file = __file__
    cur_script_path = os.path.dirname(cur_script_file)

    
    notes = os.path.join(cur_script_path, 'install', host_os_index+'.md')

    if os.path.isfile(notes):
        r = cmind.utils.load_txt(notes)
        if r['return']>0: return r
        s = r['string']
        if s != '':
            show = st.toggle('Show system dependencies?', value = True)
            if show:
                md += s


    need_user = ''
    python = 'python3'
    if host_os_index == 'redhat':
        need_user = ' --user'
    elif host_os_index == 'windows':
        python = 'python'
    
    
    ###################################################################
    # Select repository

    choices = [('Stable Git version from GitHub: mlcommons@ck', 'stable'),
               ('Dev Git version from GitHub: ctuning@mlcommons-ck', 'ctuning'),
               ('Small and stable ZIP from Zenodo: 20240223', 'zenodo')]

    repo = st.selectbox('Select repository with [automation recipes (CM scripts)](https://access.cknowledge.org/playground/?action=scripts):',
                         range(len(choices)),
                         format_func = lambda x: choices[x][0], 
                         index=0, 
                         key='select_repo')

    repo_index = choices[repo][1]


    # Add stable repo from Zenodo
    if repo_index == 'ctuning':
        cm_repo = 'ctuning@mlcommons-ck'
    elif repo_index == 'zenodo':
        cm_repo = '--url=https://zenodo.org/records/10787459/files/cm-mlops-repo-20240306.zip'
    else:
        cm_repo = 'mlcommons@ck'
    
    x =  '{} -m pip install cmind -U {}\n\n'.format(python, need_user)
    x += 'cm pull repo {}\n\n'.format(cm_repo)
    
    clean_cm_cache = st.toggle('Clean CM cache', value=True, key = 'install_clean_cm_cache')

    cm_clean_cache = 'cm rm cache -f\n\n' if clean_cm_cache else ''

    x += cm_clean_cache



    python_venv_name=params.get('@adr.python.name', '')
    python_ver_min=params.get('@adr.python.version_min', '')
    python_ver=params.get('@adr.python.version', '')

    if python_venv_name == '':
         use_python_venv = st.toggle('Use Python Virtual Environment for CM scripts?', value = False)
         if use_python_venv:
             python_venv_name = st.text_input('Enter some CM python venv name for your project:', value = "mlperf-v4.0")

             if python_ver_min == '':
                 python_ver_min = st.text_input('[Optional] Specify min version such as 3.8:')
         
    y = ''
    if python_venv_name!='':# or python_ver!='' or python_ver_min!='':
        y = 'cm run script "get sys-utils-cm"\n'

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


    md += '```bash\n{}\n```\n'.format(x)

    st.markdown('---')
    st.markdown(md)
    st.markdown('*Check [more CM installation notes at GitHub](https://github.com/mlcommons/ck/blob/master/docs/installation.md)*.')



    return {'return':0, 'end_html':end_html}
