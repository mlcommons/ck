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
    st.title('How to run benchmarks')

    st.markdown(announcement)

    return page(st, params)




def page(st, params, action = ''):

    global initialized, external_module_path, external_module_meta

    end_html = ''
    
    st.markdown('----')
    st.markdown(announcement)


    return {'return':0, 'end_html':end_html}
