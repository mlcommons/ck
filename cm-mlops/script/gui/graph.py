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
    current = __import__(__name__)

    params = st.experimental_get_query_params()

    # Set title
    st.title('CM experiment visualization')

    return visualize(st, params, current)




def visualize(st, query_params, parent):

    # Query experiment
    v_experiment_tags = os.environ.get('CM_GUI_GRAPH_EXPERIMENT_TAGS','')
    q_experiment_tags = query_params.get('tags',[''])
    if len(q_experiment_tags)>0:
        if q_experiment_tags[0]!='':
            v_experiment_tags = q_experiment_tags[0]
    v_experiment_tags = v_experiment_tags.replace(',',' ')
    v_experiment_tags = st.text_input('Select CM experiment tags separated by space:', value=v_experiment_tags, key='v_experiment_tags').strip()
    v_experiment_tags = v_experiment_tags.replace(',',' ')

    v_experiment_name = os.environ.get('CM_GUI_GRAPH_EXPERIMENT_NAME','')
    q_experiment_name = query_params.get('name',[''])
    if len(q_experiment_name)>0:
        if q_experiment_name[0]!='':
            v_experiment_name = q_experiment_name[0]

    # Get all experiment names
    ii = {'action':'find', 
          'automation':'experiment,a0a2d123ef064bcb'}

    if v_experiment_tags!='':
        ii['tags']=v_experiment_tags.replace(' ',',')

    r = cmind.access(ii)
    if r['return']>0: return r

    lst_all = r['list']

    experiments = ['']

    selection = 0
    index = 1
    for l in sorted(lst_all, key=lambda x: (
                                            ','.join(x.meta.get('tags',[])),
                                            x.meta.get('alias',''),
                                            x.meta['uid']
                                           )):
    
        meta = l.meta

        if v_experiment_name!='' and (v_experiment_name == meta['alias'] or v_experiment_name == meta['uid']):
            selection = index

        name = ' '.join(meta.get('tags',[]))
        if name =='': name = meta.get('alias', '')
        if name =='': name = meta['uid']


        experiments.append(name)

        index+=1

    if len(lst_all) == 1:
        selection = 1

    # Show experiment artifacts
    experiment = st.selectbox('Select experiment from {} found:'.format(len(experiments)-1), 
                              range(len(experiments)), 
                              format_func=lambda x: experiments[x],
                              index=selection, 
                              key='experiment')


    lst = [lst_all[experiment-1]] if experiment > 0 else lst_all
    
    # Check experiments
    results = []
    results_with_password = []
    passwords = []
    
    for experiment in lst:
        path = experiment.path

        for d in os.listdir(path):
            path2 = os.path.join(path, d)
            if os.path.isdir(path2):
                path_to_result = os.path.join(path, d, 'cm-result.json')

                if os.path.isfile(path_to_result):
                    desc = {'path':path_to_result}

                    pwd = experiment.meta.get('password_hash','')
                    if pwd=='':
                        results.append(desc)
                    else:
                        desc['password_hash'] = pwd

                        if pwd not in passwords:
                            passwords.append(pwd)
                    
                        results_with_password.append(desc)

    # Check if password
    if len(passwords)>0:
        password = st.text_input('Some results are protected by password. Enter password to unlock them:', value='', key='v_experiment_pwd').strip()

        if password!='':
            import bcrypt
            # salt = bcrypt.gensalt()
            # TBD: temporal hack to demo password protection for experiments
            # salt = bcrypt.gensalt()
            password_salt = b'$2b$12$ionIRWe5Ft7jkn4y/7C6/e'
            password_hash2 = bcrypt.hashpw(password.encode('utf-8'), password_salt).decode('utf-8')

            for result in results_with_password:
                if result['password_hash'] == password_hash2:
                    results.append(result)
    
    # How to visualize selection

    if st.session_state.get('tmp_cm_results','')=='':
        st.session_state['tmp_cm_results']=len(results)    
    elif int(st.session_state['tmp_cm_results'])!=len(results):
        st.session_state['tmp_cm_results']=len(results)
        st.session_state['how']=''

    
    how = ''

    v_max_results = os.environ.get('CM_GUI_GRAPH_EXPERIMENT_MAX_RESULTS','')

    if v_max_results!='' and len(results)>int(v_max_results):
        st.markdown('Too many results - continue pruning ...')
        return {'return':0}

    v_how = os.environ.get('CM_GUI_GRAPH_EXPERIMENT_HOW','')
    q_how = query_params.get('type',[''])
    if len(q_how)>0:
        if q_how[0]!='':
            v_how = q_how[0]

            
    how_selection = ['', '2D', 'bar']
    
    how_index = 0
    if v_how!='' and v_how in how_selection:
        how_index = how_selection.index(v_how)

    how = st.selectbox('Select how to visualize {} CM experiment set(s):'.format(len(results)),
                       how_selection,
                       index = how_index, 
                       key = 'how')

    if how == '':
        return {'return':0}
    

    
    
    
    
    
    
    # Check results
    all_values = []
    keys = []

    if len(results)>0:
        for result in results:
            path_to_result = result['path']
            
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
