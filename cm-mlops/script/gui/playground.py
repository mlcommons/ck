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

    params = st.experimental_get_query_params()

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

    # Set title
    extra = os.environ.get('CM_GUI_EXTRA_HTML','')

    if extra!='':
        url = ''
        for p in params:
            v=str(','.join(params[p]))
            if url!='': url+=';'
            url+=p+'='+v
        extra=extra.replace('{{CM_URL}}', url)

    st.write('''
        <center>
        <h2 style="color:#2f6fb3">Collective Knowledge Playground</h2>
        <img src="https://cknowledge.org/images/logo-ck-tr.png" width="150">
        <br>
        {}
        <br>
        </center>
        '''.format(extra),
        unsafe_allow_html=True
    )

    # Check action and basic menu
    action = params.get('action',['contributors'])[0].lower()

    style_action_challenges='font-style:italic;font-weight:bold;color:#ffffff' if action=='challenges' else ''
    style_action_experiments='font-style:italic;font-weight:bold;color:#ffffff' if action=='experiments' else ''
    style_action_contributors='font-style:italic;font-weight:bold;color:#ffffff' if action=='contributors' else ''
    style_action_reports='font-style:italic;font-weight:bold;color:#ffffff' if action=='reports' else ''
    style_action_beta='font-style:italic;font-weight:bold;color:#ffffff' if action=='beta' else ''

    st.write('''
        <center>
        <a target="_self" href="?action=contributors"><button style="{}">Leaderboard</button></a>
        <a target="_self" href="?action=challenges"><button style="{}">Challenges</button></a>
        <a target="_self" href="?action=experiments"><button style="{}">Experiments and results</button></a>
        <a target="_self" href="?action=reports"><button style="{}">Reports</button></a>
        <a target="_self" href="?action=beta"><button style="{}">Beta features</button></a>
        <a target="_self" href="https://github.com/mlcommons/ck"><button>Docs / GitHub</button></a>
        <a target="_self" href="https://discord.gg/JjWNWXKxwT"><button>Discord</button></a>
        </center>
        '''.format(
                   style_action_contributors,
                   style_action_challenges,
                   style_action_experiments, 
                   style_action_reports,
                   style_action_beta
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
    elif action == 'experiments':
        from graph import visualize
        r = visualize(st, params, action = 'experiments')
    elif action == 'contributors':
        from playground_contributors import page
        r = page(st, params)
    elif action == 'reports':
        from playground_reports import page
        r = page(st, params)
    elif action == 'beta':
        from playground_beta import page
        r = page(st, params)

    if r['return']>0:
        st.markdown('**CM error:** {} . Please report [here](https://github.com/mlcommons/ck/issues)'.format(r['error']))

    end_html=r.get('end_html','')


    # Finalize all pages
    st.markdown("""---""")

    if end_html!='':
        st.write(end_html, unsafe_allow_html=True)

    st.write("""
             <center>
              Development: 
              <a href="https://cTuning.org">cTuning.org</a>,
              <a href="https://cKnowledge.org">cKnowledge.org</a>
              and <a href="https://github.com/mlcommons/ck/blob/master/docs/taskforce.md">MLCommons</a>.
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
