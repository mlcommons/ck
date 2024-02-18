# Developer(s): Grigori Fursin

import cmind
import os
import misc

import streamlit.components.v1 as components

import streamlit as st

announcement = 'Under development - please get in touch via [Discord](https://discord.gg/JjWNWXKxwT) for more details ...'

initialized = False
external_module_path = ''
external_module_meta = {}

def main():
    params = misc.get_params(st)

    # Set title
    st.title('Reproducibility studies')

    st.markdown(announcement)

    return page(st, params)




def page(st, params, action = ''):

    global initialized, external_module_path, external_module_meta

#    st.markdown('----')

    url_benchmarks = misc.make_url('', key='', action='howtorun', md=False)
    url_challenges = misc.make_url('', key='', action='challenges', md=False)

    # Some info
    x = '''
         <i>
         <small>
         This interface will help you find the <a href="{}">modular benchmarks' settings</a> 
         that <a href="{}">the community</a> have managed to successfully validate 
         across different models, data sets, software and hardware 
         based on the <a href="https://cTuning.org/ae">ACM/cTuning reproducibility methodology and badges</a> -
         please get in touch via <a href="https://discord.gg/JjWNWXKxwT">Discord</a> for more details.
         </small>
         </i>
          <br>
          <br>
        '''.format(url_benchmarks, url_challenges)

    st.write(x, unsafe_allow_html = True)
    
#    st.markdown(announcement)
    
    # If not initialized, find code for launch benchmark
    if not initialized:
        r = cmind.access({'action':'find',
                          'automation':'script',
                          'artifact':'5dc7662804bc4cad'})
        if r['return']>0: return r

        lst = r['list']

        if len(lst)>0:
            external_module_path = os.path.join(lst[0].path, 'dummy')
            external_module_meta = lst[0].meta

        if external_module_path =='':
            st.markdown('Warning: can\'t find internal module!')
            return {'return':0}

        initialized = True

    ii = {'streamlit_module': st,
          'params': params,
          'meta': external_module_meta,
          'skip_title': True,
          'misc_module': misc}

    return cmind.utils.call_internal_module(None, external_module_path , 'customize', 'gui', ii)
