# Developer(s): Grigori Fursin

import cmind
import os
import misc

import streamlit.components.v1 as components

import streamlit as st

announcement = 'Under preparation. Please check the [MLCommons CM automation project](https://github.com/mlcommons/ck) for more details ...'


def main():
    params = misc.get_params(st)

    # Set title
    st.title('How to run benchmarks')

    st.markdown(announcement)


    return page(st, params)




def page(st, params, action = ''):

    st.markdown('----')
    st.markdown(announcement)
    
    url_prefix = st.config.get_option('server.baseUrlPath')+'/'

    st.markdown(url_prefix)



    return {'return':0}
