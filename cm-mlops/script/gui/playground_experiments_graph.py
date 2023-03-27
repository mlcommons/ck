# Developer(s): Grigori Fursin

import cmind
import os

import streamlit as st
import streamlit.components.v1 as components

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

import numpy as np
import pandas as pd

import mpld3
from mpld3 import plugins
from mpld3 import utils




def page(st, params, parent, experiment):

    result_uid = params.get('result_uid',[''])[0].strip()

    meta = experiment.meta
    alias = meta['alias']

    uid = meta['uid']

    end_html='''
         <center>
          <small><a href="{}"><i>Self link</i></a></small>
         </center>
         '''.format(parent.make_url(meta['alias'], action='experiments', md=False))

    name = meta.get('title', meta['alias'].replace('--',','))

    st.write('''
             <center>
              <h4>Experiment set: {}</h4>
             </center>
             '''.format(name),
             unsafe_allow_html=True
             )

    path = experiment.path

    results = []

    r = cmind.utils.list_all_files({'path':path, 'all':'yes', 'file_name':'cm-result.json'})
    if r['return']>0: return r

    for path_to_result in r['list']:
        results.append(os.path.join(path, path_to_result))

    # Check results
    all_values = []
    keys = []
    all_data = []

    ###################################################
    if len(results)==0:
        st.markdown('No results yet')
        return {'return':0, 'end_html':end_html}

    x = 'experiment set(s)' if result_uid=='' else 'result'

    st.write('''
             <center>
              <i>Visualizing {} {} from the community</i>
              <hr>
             </center>
             '''.format(len(results), x),
             unsafe_allow_html=True
             )

#    derived_metrics = params.get('derived_metrics',[''])[0].strip()
#    derived_metrics_value = st.text_input("Optional: add derived metrics in Python (example: result['Accuracy2']=result['Acuracy']*2):", value = derived_metrics).strip()

    error_shown2 = False
    for path_to_result in results:
        r = cmind.utils.load_json_or_yaml(path_to_result)
        if r['return']>0: return r

        result_meta = r['meta']

        for result in result_meta:
#            if derived_metrics_value!='':
#                try:
#                   exec(derived_metrics_value)
#                except Exception as e:
#                   if not error_shown2:
#                       st.markdown('*Syntax error in derived metrics: {}*'.format(e))
#                       error_shown2 = True

            all_values.append(result)

            for k in result.keys():
                if k not in keys:
                    keys.append(k)

#    filter_value = params.get('filter',[''])[0].strip()
#    filter_value = st.text_input("Optional: add result filter in Python (example: result['Accuracy']>75):", value = filter_value).strip()
#
#    st.markdown('---')

    # all_values is a list of dictionaries with all keys
    error_shown=False
    for result in all_values:

#        if filter_value!='':
#            try:
#               if not eval(filter_value):
#                   continue
#            except Exception as e:
#               if not error_shown:
#                   st.markdown('*Syntax error in filter: {}*'.format(e))
#                   error_shown = True

        # Check if 1 result UID is selected
        if result_uid!='' and result.get('uid','')!=result_uid:
            continue

        data = []
        for k in sorted(keys):
            data.append(result.get(k))

        all_data.append(data)

        if result_uid!='': break

    ###################################################
    if len(all_data)==0:
        st.markdown('No results found for your selection.')
        return {'return':0, 'end_html':end_html}





    ###################################################
    # If experiment found and 1 UID, print a table
    if result_uid!='':
        data = all_data[0]

        result = {}

        j=0
        for k in sorted(keys):
            result[k] = data[j]
            j+=1

        x = ''
        for k in sorted(keys, key=lambda x: x.lower()):
            x+='* **{}**: {}\n'.format(k,str(result[k]))

        st.markdown(x)

        # Check associated reports
        r=cmind.access({'action':'find',
                        'automation':'report,6462ecdba2054467',
                        'tags':'result-{}'.format(result_uid)})
        if r['return']>0: return r

        lst = r['list']

        for l in lst:
            report_path = l.path

            f1 = os.path.join(report_path, 'README.md')
            if os.path.isfile(f1):
                report_meta = l.meta

                report_alias = report_meta['alias']
                report_title = report_meta.get('title','')

                report_name = report_title if report_title!='' else report_alias

                r = cmind.utils.load_txt(f1)
                if r['return']>0: return r

                s = r['string']

                st.markdown('---')
                st.markdown('### '+report_name)

                st.markdown(s)


        # Create self-link
        end_html='''
         <center>
          <small><a href="{}&result_uid={}"><i>Self link</i></a></small>
         </center>
         '''.format(parent.make_url(alias, action='experiments', md=False), result_uid)

        return {'return':0, 'end_html':end_html}



    ###################################################
    # Select 2D keys
    axis_key_x=''
    axis_key_y=''
    axis_key_c=''

    if len(keys)>0:
        keys = [''] + keys

        q_axis_key_x = params.get('x',[''])
        if len(q_axis_key_x)>0:
            axis_key_x = q_axis_key_x[0]
        i_axis_key_x = 0
        if axis_key_x != '' and axis_key_x in keys: i_axis_key_x = keys.index(axis_key_x)
        if axis_key_x == '' and 'Result' in keys: i_axis_key_x = keys.index('Result')
        axis_key_x = st.selectbox('Select X key', keys, index=i_axis_key_x, key='x')

        q_axis_key_y = params.get('y',[''])
        if len(q_axis_key_y)>0:
            axis_key_y = q_axis_key_y[0]
        i_axis_key_y = 0
        if axis_key_y != '' and axis_key_y in keys: i_axis_key_y = keys.index(axis_key_y)
        if axis_key_y == '' and 'Accuracy' in keys: i_axis_key_y = keys.index('Accuracy')
        axis_key_y = st.selectbox('Select Y key', keys, index=i_axis_key_y, key='y')

        q_axis_key_c = params.get('c',[''])
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


        t = 0
        for result in values:
#            if filter_value!='':
#                try:
#                   if not eval(filter_value):
#                       continue
#                except Exception as e:
#                   if not error_shown:
#                       st.markdown('*Syntax error in filter: {}*'.format(e))
#                       error_shown = True

            v = result

            t+=1

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
            for key in sorted(v.keys(), key=lambda x: x.lower()):
                value = v[key]
                info+='<b>'+str(key)+': </b>'+str(value)+'<br>\n'

            info2 = '<div style="padding:10px;background-color:#FFFFE0;"><small>'+info+'</small></div>'

            label = [info2]
            plugins.connect(fig, plugins.PointHTMLTooltip(graph, label))

            uid = v.get('uid','')
            if uid!='':
                url = '?action=experiments&name={}&result_uid={}'.format(alias, uid)

            if url!='':
                targets = [url]
                plugins.connect(fig, OpenBrowserOnClick(graph, targets = targets)) 




        fig_html = mpld3.fig_to_html(fig)

        #fig_html = '<div style="padding:10px;background-color:#F0F0F0;">'+fig_html+'</div>'

        #components.html(fig_html, width=1000, height=800)
        st.markdown('---')
        components.html(fig_html, width=1100, height=900)

        df = pd.DataFrame(
          all_data,
          columns=(k for k in sorted(keys) if k!='')
        )

        st.markdown('---')
        st.dataframe(df)
#        st.markdown(df.to_html(render_links=True, escape=False),unsafe_allow_html=True)

    return {'return':0, 'end_html':end_html}



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

