# Developer(s): Grigori Fursin

import cmind
import os

import streamlit.components.v1 as components

import streamlit as st

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

import numpy as np
import pandas as pd

import mpld3
from mpld3 import plugins
from mpld3 import utils


class OpenBrowserOnClick(mpld3.plugins.PluginBase):

    JAVASCRIPT="""

    mpld3.register_plugin("openbrowseronclick", PointClickableHTMLTooltip);

    PointClickableHTMLTooltip.prototype = Object.create(mpld3.Plugin.prototype);
    PointClickableHTMLTooltip.prototype.constructor = PointClickableHTMLTooltip;
    PointClickableHTMLTooltip.prototype.requiredProps = ["id"];
    PointClickableHTMLTooltip.prototype.defaultProps = {targets:null};

    function PointClickableHTMLTooltip(fig, props){
        mpld3.Plugin.call(this, fig, props);
    };

    PointClickableHTMLTooltip.prototype.draw = function(){
       var obj = mpld3.get_element(this.props.id);
       var targets = this.props.targets;
       obj.elements()
           .on("mousedown", function(d, i){
                              window.open(targets[i]);
                               });
    };

    """

    def __init__(self, points, targets=None):
        self.points = points
        self.targets = targets
        self.dict_ = {"type": "openbrowseronclick",
                      "id": mpld3.utils.get_id(points, None),
                      "targets": targets}



def main():

    query_params = st.experimental_get_query_params()

    # Set title
    st.title('CM (CK2) experiment visualization')

    # Query experiment
    experiment_tags = os.environ.get('CM_GUI_GRAPH_EXPERIMENT_TAGS','')
    experiment_name = os.environ.get('CM_GUI_GRAPH_EXPERIMENT_NAME','')


    v_experiment_tags = ''
    q_experiment_tags = query_params.get('tags',[''])
    if len(q_experiment_tags)>0:
        v_experiment_tags = q_experiment_tags[0]
    v_experiment_tags = st.text_input('CM experiment tags', value=v_experiment_tags, key='v_experiment_tags').strip()

    # Get all experiment names
    ii = {'action':'find', 
          'automation':'experiment,a0a2d123ef064bcb'}

    if v_experiment_tags!='':
        ii['tags']=v_experiment_tags

    r = cmind.access(ii)
    if r['return']>0: return r

    lst_all = r['list']

    experiments_all = ['']
    for l in lst_all:
        experiments_all.append(l.meta['alias'])

    experiments_all=sorted(experiments_all)

    v_experiment_name = st.selectbox('CM experiment name', experiments_all, index=0, key='v_experiment_name').strip()

    lst = []
    if v_experiment_tags!='' or v_experiment_name!='':
        ii = {'action':'find', 
              'automation':'experiment,a0a2d123ef064bcb'}

        if v_experiment_tags!='':
            ii['tags']=v_experiment_tags
        if v_experiment_name!='':
            ii['artifact']=v_experiment_name

        r = cmind.access(ii)
        if r['return']>0: return r

        lst = r['list']

    # Check experiments
    st.markdown("""---""")

    st.markdown('Found CM experiment(s): {}'.format(len(lst)))

    results = []
    
    for experiment in lst:
        path = experiment.path

        r = cmind.utils.list_all_files({'path':path, 'all':'yes', 'file_name':'cm-result.json'})
        if r['return']>0: return r

        for path_to_result in r['list']:
            results.append(os.path.join(path, path_to_result))

    # Check results
    all_values = []
    keys = []

    if len(results)>0:
        st.markdown('Found CM results: {}'.format(len(results)))

        for path_to_result in results:
            r = cmind.utils.load_json_or_yaml(path_to_result)
            if r['return']>0: return r

            meta = r['meta']

            for m in meta:
                all_values.append(m)

                for k in m.keys():
                    if k not in keys:
                        keys.append(k)

    # Select 2D keys
    axis_key_x=''
    axis_key_y=''
    axis_key_c=''

    if len(keys)>0:
        keys = [''] + keys
        
        st.markdown("""---""")

        q_axis_key_x = query_params.get('x',[''])
        if len(q_axis_key_x)>0:
            axis_key_x = q_axis_key_x[0]
        i_axis_key_x = 0
        if axis_key_x != '' and axis_key_x in keys: i_axis_key_x = keys.index(axis_key_x)
        if axis_key_x == '' and 'Result' in keys: i_axis_key_x = keys.index('Result')
        axis_key_x = st.selectbox('Select X key', keys, index=i_axis_key_x, key='x')

        q_axis_key_y = query_params.get('y',[''])
        if len(q_axis_key_y)>0:
            axis_key_y = q_axis_key_y[0]
        i_axis_key_y = 0
        if axis_key_y != '' and axis_key_y in keys: i_axis_key_y = keys.index(axis_key_y)
        if axis_key_y == '' and 'Accuracy' in keys: i_axis_key_y = keys.index('Accuracy')
        axis_key_y = st.selectbox('Select Y key', keys, index=i_axis_key_y, key='y')

        q_axis_key_c = query_params.get('c',[''])
        if len(q_axis_key_c)>0:
            axis_key_c = q_axis_key_c[0]
        i_axis_key_c = 0
        if axis_key_c != '' and axis_key_c in keys: i_axis_key_c = keys.index(axis_key_c)
        if axis_key_c == '' and 'version' in keys: i_axis_key_c = keys.index('version')
        axis_key_c = st.selectbox('Select Color key', keys, index=i_axis_key_c, key='c')

        axis_key_s = st.selectbox('Select Style key', keys, index=0, key='s')


    # Select values
    values = []

    if axis_key_x!='' and axis_key_y!='':
        for v in all_values:
            x = v.get(axis_key_x, None)
            y = v.get(axis_key_y, None)

            if x!=None and y!=None:
                values.append(v)

    if len(values)>0:
        #fig, ax = plt.subplots(figsize=(12,6))
        fig, ax = plt.subplots()

        ax.set_xlabel(axis_key_x)
        ax.set_ylabel(axis_key_y)

        ax.set_title('') #, size=20)

        ax.grid(linestyle = 'dotted')

        #https://matplotlib.org/stable/api/markers_api.html
        
        unique_color_values = {}
#        unique_colors = list(mcolors.CSS4_COLORS.keys())
        unique_colors = list(mcolors.TABLEAU_COLORS.keys())
        i_unique_color_values = 0

        unique_style_values = {}
        unique_styles = ['o','v','^','<','>','1','2','3','4','8','s','p','P','*','+','D']
        i_unique_style_values = 0


        for v in values:
            x = v.get(axis_key_x, None)
            y = v.get(axis_key_y, None)

            url = v.get('url','')

            color = 'blue'
            if axis_key_c!='':
                c = v.get(axis_key_c, None)
                if c!=None:
                    if c in unique_color_values:
                        color = unique_color_values[c]
                    else:
                        color = unique_colors[i_unique_color_values]
                        unique_color_values[c] = color
                        if i_unique_color_values<(len(unique_colors)-1):
                            i_unique_color_values+=1
                          
            style = 'o'
            if axis_key_s!='':
                s = v.get(axis_key_s, None)
                if s!=None:
                    if s in unique_style_values:
                        style = unique_style_values[s]
                    else:
                        style = unique_styles[i_unique_style_values]
                        unique_style_values[s] = style
                        if i_unique_style_values<(len(unique_styles)-1):
                            i_unique_style_values+=1
            
            graph = ax.scatter(x, y, color=color, marker=style)

            info=''
            for key in sorted(v):
                value = v[key]
                info+='<b>'+str(key)+': </b>'+str(value)+'<br>\n'
            info2 = '<div style="padding:10px;background-color:#FFFFE0;"><small>'+info+'</small></div>'
            
            label = [info2]
            plugins.connect(fig, plugins.PointHTMLTooltip(graph, label))

            if url!='':
                targets = [url]
                plugins.connect(fig, OpenBrowserOnClick(graph, targets = targets)) 


        fig_html = mpld3.fig_to_html(fig)

        #fig_html = '<div style="padding:10px;background-color:#F0F0F0;">'+fig_html+'</div>'

        #components.html(fig_html, width=1000, height=800)
        components.html(fig_html, width=1100, height=900)

    return {'return':0}

if __name__ == "__main__":
    r = main()

    if r['return']>0: 
       
        st.markdown("""---""")
        st.markdown('**Error detected by CM:** {}'.format(r['error']))
