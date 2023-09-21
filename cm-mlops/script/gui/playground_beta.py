# Developer(s): Grigori Fursin

import cmind
import os
import datetime
import misc

def page(st, params):

    current_script_path = os.environ.get('CM_TMP_CURRENT_SCRIPT_PATH', '')
    
    url_prefix = st.config.get_option('server.baseUrlPath')+'/'

    name = params.get('name',[''])[0].strip()
    tags = params.get('tags',[''])[0].lower()

    x = '''
        <center>
         <h3>Beta features requested by the community</h3>
         Join <a href="https://discord.gg/JjWNWXKxwT">our public Discord server</a> to discuss them or suggest the new ones ...
        </center>
        '''

    st.write(x, unsafe_allow_html = True)

    st.markdown('---')

    readme = os.path.join(current_script_path, 'playground_beta_README.md')

    md = ''
    
    if os.path.isfile(readme):
        
        r = cmind.utils.load_txt(readme)
        if r['return']>0: return r

        md += r['string']

    st.markdown(md)

    end_html=''

    return {'return':0, 'end_html':end_html}
