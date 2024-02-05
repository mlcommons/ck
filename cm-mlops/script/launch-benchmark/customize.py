from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    meta = i['meta']

    automation = i['automation']

    quiet = (env.get('CM_QUIET', False) == 'yes')

    return {'return':0}

def postprocess(i):

    env = i['env']

    return {'return':0}

def gui(i):

    st = i['streamlit_module']
    meta = i['meta']

    st.title('Collective Mind')

    st.markdown('### Launch benchmark')

    st.markdown(str(meta))

    return {'return':0}
