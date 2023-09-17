# Developer(s): Grigori Fursin

import cmind
import os
import datetime
import misc

def page(st, params):

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

    md = 'TBA'

    st.markdown(md)

    end_html=''

    return {'return':0, 'end_html':end_html}
