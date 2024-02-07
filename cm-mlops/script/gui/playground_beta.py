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

    readme = os.path.join(current_script_path, 'playground_beta_README.md')

    md = ''
    
    if os.path.isfile(readme):
        
        r = cmind.utils.load_txt(readme)
        if r['return']>0: return r

        md += r['string']

    md = md.replace('{{URL_PREFIX}}', url_prefix)
    
#    st.markdown(md)
    st.write(md, unsafe_allow_html = True)

    end_html=''

    return {'return':0, 'end_html':end_html}
