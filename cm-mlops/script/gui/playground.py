# Developer(s): Grigori Fursin

import streamlit as st
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu

import os
import cmind
import misc

def main():

    st.set_page_config(layout="wide",
                       menu_items={})

    params = misc.get_params(st)

    # Set style
    # Green: background:#7fcf6f;
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}

            button {
                background:#2f6fb3;
                border:0 none;
                -webkit-border-radius: 2px;
                border-radius: 2px;
                color: #ffffff;
                margin:3px;
            }

            </style>
            """

    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    # Set title (check extra user HTML to embed before title if needed)
    extra = os.environ.get('CM_GUI_EXTRA_HTML','')

    if extra!='':
        url = ''
        for p in params:
            v=str(','.join(params[p]))
            if url!='': url+=';'
            url+=p+'='+v
        extra=extra.replace('{{CM_URL}}', url)+'\n\n'

    st.write('''
        <center>
        <h2 style="color:#2f6fb3">Collective Knowledge Playground</h2>
        <a href="/"><img src="https://cknowledge.org/images/logo-ck-tr.png" width="150"></a><br>
        {}
        <br>
        </center>
        '''.format(extra),
        unsafe_allow_html=True
    )

    extra_file = os.environ.get('CM_GUI_EXTRA_HTML_FILE','')
    if extra_file!='':
        r = cmind.utils.load_txt(extra_file)
        if r['return']>0: return r

        s = '\n\n'+r['string']+'\n\n'

        st.write(s, unsafe_allow_html=True)
    

    # Check action and basic menu
    action = params.get('action',['scripts'])[0].lower()

    style_action_scripts='font-style:italic;font-weight:bold;color:#ffffff' if action=='scripts' else ''
    style_action_howtorun='font-style:italic;font-weight:bold;color:#ffffff' if action=='howtorun' else ''
    style_action_challenges='font-style:italic;font-weight:bold;color:#ffffff' if action=='challenges' else ''
    style_action_contributors='font-style:italic;font-weight:bold;color:#ffffff' if action=='contributors' else ''
    style_action_experiments='font-style:italic;font-weight:bold;color:#ffffff' if action=='experiments' else ''
    style_action_reproduce='font-style:italic;font-weight:bold;color:#ffffff' if action=='reproduce' else ''
    style_action_apps='font-style:italic;font-weight:bold;color:#ffffff' if action=='apps' else ''
    style_action_reports='font-style:italic;font-weight:bold;color:#ffffff' if action=='reports' else ''
    style_action_beta='font-style:italic;font-weight:bold;color:#ffffff' if action=='beta' else ''
    style_action_install='font-style:italic;font-weight:bold;color:#ffffff' if action=='install' else ''

    st.write('''
        <center>
        <a target="_self" href="?action=scripts"><button style="{}">Automation recipes</button></a>
        <a target="_self" href="?action=howtorun"><button style="{}">Modular benchmarks</button></a>
        <a target="_self" href="?action=challenges"><button style="{}">Challenges</button></a>
        <a target="_self" href="?action=experiments"><button style="{}">Results</button></a>
        <a target="_self" href="?action=reproduce"><button style="{}">Reproducibility</button></a><br>
        <a target="_self" href="?action=contributors"><button style="{}">Leaderboard</button></a>
        <a target="_self" href="?action=reports"><button style="{}">Reports</button></a>
        <a target="_self" href="?action=beta"><button style="{}">Beta</button></a>
        <a target="_self" href="?action=scripts&tags=modular,app"><button style="{}">Modular apps</button></a><br>
        <a target="_self" href="https://discord.gg/JjWNWXKxwT"><button>Discord</button></a>
        <a target="_self" href="https://github.com/mlcommons/ck"><button>GitHub</button></a>
        <a target="_self" href="?action=install"><button style="{}">Install</button></a>
        </center>
        '''.format(
                   style_action_scripts,
                   style_action_howtorun,
                   style_action_challenges,
                   style_action_experiments, 
                   style_action_reproduce,
                   style_action_contributors,
                   style_action_reports,
                   style_action_beta,
                   style_action_apps,
                   style_action_install
                   ),
        unsafe_allow_html=True
    )

    # Check actions
#    st.markdown("""---""")
    st.markdown('')

    r={'return':0}

    if action == 'challenges':
        from playground_challenges import page
        r = page(st, params)
    elif action == 'howtorun':
        from playground_howtorun import page
        r = page(st, params)
    elif action == 'experiments':
        from graph import visualize
        r = visualize(st, params, action = 'experiments')
    elif action == 'contributors':
        from playground_contributors import page
        r = page(st, params)
    elif action == 'scripts' or action == 'recipes' or action == 'automation-recipes' or action == 'components':
        from playground_scripts import page
        r = page(st, params)
    elif action == 'reproduce' or action == 'repro' or action == 'reproducibility':
        from playground_reproduce import page
        r = page(st, params)
    elif action == 'apps' or action == 'optimized-apps':
        from playground_apps import page
        r = page(st, params)
    elif action == 'reports':
        from playground_reports import page
        r = page(st, params)
    elif action == 'beta':
        from playground_beta import page
        r = page(st, params)
    elif action == 'install' or action == 'setup':
        from playground_install import page
        r = page(st, params, {})

    if r['return']>0:
        st.markdown('**CM error:** {} . Please report [here](https://github.com/mlcommons/ck/issues)'.format(r['error']))

    end_html=r.get('end_html','')


    # Finalize all pages
    st.markdown("""---""")

    if end_html!='':
        st.write(end_html, unsafe_allow_html=True)

    st.write("""
             <center>
              Powered by <a href="https://github.com/mlcommons/ck">MLCommons Collective Mind</a>
             </center>
             """,  
             unsafe_allow_html=True)


def make_url(name, alias='', action='contributors', key='name', md=True):

    import urllib

    if alias == '': alias = name

    url = '?action={}&{}={}'.format(action, key, urllib.parse.quote_plus(alias))

    if md:
        md = '[{}]({})'.format(name, url)
    else:
        md = url

    return md


def convert_date(date):
    # date: format YYYYMMDD to YYYY month day

    import calendar

    try:
        year = date[0:4]
        month = calendar.month_abbr[int(date[4:6])]
        day = str(int(date[6:8]))
    except Exception as e:
        return {'return':1, 'error':'date "{}" is not of format YYYYMMDD: {}'.format(date, format(e))}

    return {'return':0, 'string':year+' '+month+' '+day}


if __name__ == "__main__":
    main()
