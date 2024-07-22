# Developer(s): Grigori Fursin

import cmind
import os
import misc

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

security = ['os.', 'streamlit.', 'matplotlib.', 'numpy.', 'pandas.', 'mpld3.']


repro_badges={
        'acm_ctuning_repro_badge_functional':{'img':'https://cTuning.org/images/artifacts_evaluated_functional_v1_1_small.png'},
        'acm_ctuning_repro_badge_reproduce':{'img':'https://cTuning.org/images/results_reproduced_v1_1_small.png'},
        'acm_ctuning_repro_badge_support_docker':{'img':'https://cTuning.org/images/docker_logo2_small.png'},
        'acm_ctuning_repro_badge_cm_interface':{'img':'https://cTuning.org/images/logo-ck-single-tr4.png'}
       }


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

    params = misc.get_params(st)

    # Set title
    st.title('CM experiment visualization')

    return visualize(st, params)




def visualize(st, query_params, action = ''):

    # Query experiment
    result_uid = os.environ.get('CM_GUI_GRAPH_EXPERIMENT_RESULT_UID','')
    q_result_uid = query_params.get('result_uid',[''])
    if len(q_result_uid)>0:
        if q_result_uid[0]!='':
            result_uid = q_result_uid[0]
    
    v_experiment_name = os.environ.get('CM_GUI_GRAPH_EXPERIMENT_NAME','')
    q_experiment_name = query_params.get('name',[''])
    if len(q_experiment_name)>0:
        if q_experiment_name[0]!='':
            v_experiment_name = q_experiment_name[0]

    v_experiment_tags=''
    if v_experiment_name=='':
        v_experiment_tags = os.environ.get('CM_GUI_GRAPH_EXPERIMENT_TAGS','')
        q_experiment_tags = query_params.get('tags',[''])
        if len(q_experiment_tags)>0:
            if q_experiment_tags[0]!='':
                v_experiment_tags = q_experiment_tags[0]
        v_experiment_tags = v_experiment_tags.replace(',',' ')

        # Check default
#        if v_experiment_tags == '' and v_experiment_name == '':
#            v_experiment_tags = 'mlperf-inference v4.0'
        
        v_experiment_tags = st.text_input('Select CM experiment tags separated by space:', value=v_experiment_tags, key='v_experiment_tags').strip()
        v_experiment_tags = v_experiment_tags.replace(',',' ')

    # Get all experiment names
    ii = {'action':'find', 
          'automation':'experiment,a0a2d123ef064bcb'}

    # If name is given, do not use tags 
    if v_experiment_name!='':
        ii['artifact']=v_experiment_name
    elif v_experiment_tags!='':
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

    if len(lst)>8:
        st.markdown('Too many experiments - continue pruning ...')
        return {'return':0}


    # Check experiments
    results = []
    results_with_password = []
    passwords = []
    results_meta = {}
    
    for experiment in lst:
        path = experiment.path

        for d in os.listdir(path):
            path2 = os.path.join(path, d)
            if os.path.isdir(path2):
                path_to_result = os.path.join(path, d, 'cm-result.json')

                if os.path.isfile(path_to_result):
                    emeta = experiment.meta
                    
                    desc = {'path':path_to_result,
                            'experiment_dir': d,
                            'experiment_uid':emeta['uid'],
                            'experiment_alias':emeta['alias'],
                            'experiment_tags':','.join(emeta.get('tags',[]))}

                    add = True
                    if result_uid!='':
                        add = False
                        r = cmind.utils.load_json(path_to_result)
                        if r['return'] == 0:
                            meta = r['meta']

                            results_meta[path_to_result] = meta

                            for m in meta:
                                if m.get('uid','') == result_uid:
                                    add = True
                                    break

                    if add:                
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
    if len(results)==0:
        st.markdown('No results found!')
        return {'return':0}


    if st.session_state.get('tmp_cm_results','')=='':
        st.session_state['tmp_cm_results']=len(results)    
    elif int(st.session_state['tmp_cm_results'])!=len(results):
        st.session_state['tmp_cm_results']=len(results)
        st.session_state['how']=0

    
    how = ''

    if result_uid=='':
        v_max_results = os.environ.get('CM_GUI_GRAPH_EXPERIMENT_MAX_RESULTS','')

        if v_max_results!='' and len(results)>int(v_max_results):
            st.markdown('Too many results - continue pruning ...')
            return {'return':0}

        v_how = os.environ.get('CM_GUI_GRAPH_EXPERIMENT_HOW','')
        q_how = query_params.get('type',[''])
        if len(q_how)>0:
            if q_how[0]!='':
                v_how = q_how[0]

        how_selection = ['', '2d-static', '2d', 'bar']
        how_selection_desc = ['', 'Scatter plot (static)', 'Scatter plot (interactive, slow - to be improved)', 'Bar plot (static)']
        
        how_index = 0
        if v_how!='' and v_how in how_selection:
            how_index = how_selection.index(v_how)

        how2 = st.selectbox('Select how to visualize {} CM experiment set(s):'.format(len(results)),
                           range(len(how_selection_desc)), 
                           format_func=lambda x: how_selection_desc[x],
                           index = how_index,
                           key = 'how')


        if how2 == '' or how2 == 0:
            return {'return':0}

        how = how_selection[how2]    

    how = how.strip()

    # Continue visualizing
    all_values = []
    keys = []
    all_data = []
    

    derived_metrics_value = query_params.get('derived_metrics',[''])[0].strip()
    derived_metrics_value = st.text_input("Optional: add derived metrics in Python. Example: result['Accuracy2'] = result['Accuracy']*2", 
                                          value = derived_metrics_value).strip()

    for x in security:
        if x in derived_metrics_value:
            derived_metrics_value=''
            break
    
    error_shown2 = False
    for desc in results:
        path_to_result = desc['path']

        if path_to_result in results_meta:
            result_meta = results_meta[path_to_result]
        else:
            r = cmind.utils.load_json_or_yaml(path_to_result)
            if r['return']>0: return r

            result_meta = r['meta']

        for result in result_meta:
            # Add extra info
            for k in ['experiment_dir', 'experiment_alias', 'experiment_uid', 'experiment_tags']:
                if k in desc:
                    result[k]=desc[k]

            if derived_metrics_value!='':
                try:
                   exec(derived_metrics_value)
                except Exception as e:
                   if not error_shown2:
                       st.markdown('*Syntax error in derived metrics: {}*'.format(e))
                       error_shown2 = True

            all_values.append(result)

            for k in result.keys():
                if k not in keys:
                    keys.append(k)

    first_keys = ['Organization', 'Model', 'Scenario', 'SystemName', 'notes', 'framework', 'Result', 'Result_Units', 'Accuracy']
    sorted_keys = [k for k in first_keys if k in keys] + [k for k in sorted(keys, key=lambda s: s.lower()) if k not in first_keys]

    filter_value = query_params.get('filter',[''])[0].strip()
    if result_uid=='': # and filter_value!='':
        filter_value = st.text_input("Optional: add result filter in Python. Examples: result['Accuracy']>75 or 'llama2' in result['Model']", value = filter_value).strip()

        st.markdown('---')

    for x in security:
        if x in filter_value:
            filter_value=''
            break

    # all_values is a list of dictionaries with all keys
    error_shown=False
    for result in all_values:

        if filter_value!='':
            try:
               if not eval(filter_value):
                   continue
            except Exception as e:
               if not error_shown:
                   st.markdown('*Syntax error in filter: {}*'.format(e))
                   error_shown = True

        # Check if 1 result UID is selected
        if result_uid!='' and result.get('uid','')!=result_uid:
            continue

        data = []
        for k in sorted_keys:
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
        st.markdown('---')
        st.markdown('# Result summary')


        data = all_data[0]


        result = {}

        j=0
        for k in sorted_keys:
            result[k] = data[j]
            j+=1


        # Check badges
        x = ''

        for k in repro_badges:
            if result.get(k, False):
                img = repro_badges[k]['img']

                x += '<a href="http://cTuning.org/ae" target="_blank"><img src="{}" height="64"></a>\n'.format(img)

        if x!='':
            st.write('<center>\n'+x+'\n</center>\n', unsafe_allow_html = True)
        
        
        x = ''
        for k in sorted_keys:
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


        # Create self link
        st.markdown("""---""")

        experiment_alias_or_uid = result['experiment_uid']

        end_html='''
         <center>
          <small><a href="{}&result_uid={}"><i>Self link</i></a></small>
         </center>
         '''.format(misc.make_url(experiment_alias_or_uid, action=action, md=False), result_uid)

        st.write(end_html, unsafe_allow_html=True)
                
        
        return {'return':0}






    ###################################################
    # Select 2D keys
    axis_key_x=''
    axis_key_y=''
    axis_key_c=''

    if len(keys)>0:
        keys = [''] + sorted_keys

        axis_key_x = os.environ.get('CM_GUI_GRAPH_EXPERIMENT_AXIS_KEY_X','')
        q_axis_key_x = query_params.get('x',[''])
        if len(q_axis_key_x)>0:
            if q_axis_key_x[0]!='':
               axis_key_x = q_axis_key_x[0]
        i_axis_key_x = 0
        if axis_key_x != '' and axis_key_x in keys: i_axis_key_x = keys.index(axis_key_x)
        if axis_key_x == '' and 'Result' in keys: i_axis_key_x = keys.index('Result')
        axis_key_x = st.selectbox('Select X key', keys, index=i_axis_key_x, key='x')

        axis_key_y = os.environ.get('CM_GUI_GRAPH_EXPERIMENT_AXIS_KEY_Y','')
        q_axis_key_y = query_params.get('y',[''])
        if len(q_axis_key_y)>0:
            if q_axis_key_y[0]!='':
                axis_key_y = q_axis_key_y[0]
        i_axis_key_y = 0
        if axis_key_y != '' and axis_key_y in keys: i_axis_key_y = keys.index(axis_key_y)
        if axis_key_y == '' and 'Accuracy' in keys: i_axis_key_y = keys.index('Accuracy')
        axis_key_y = st.selectbox('Select Y key', keys, index=i_axis_key_y, key='y')

        axis_key_c = os.environ.get('CM_GUI_GRAPH_EXPERIMENT_AXIS_KEY_C','')
        q_axis_key_c = query_params.get('c',[''])
        if len(q_axis_key_c)>0:
            if q_axis_key_c[0]!='':
                axis_key_c = q_axis_key_c[0]
        i_axis_key_c = 0
        if axis_key_c != '' and axis_key_c in keys: i_axis_key_c = keys.index(axis_key_c)
        if axis_key_c == '' and 'version' in keys: i_axis_key_c = keys.index('version')
        axis_key_c = st.selectbox('Select Color key', keys, index=i_axis_key_c, key='c')

        axis_key_s = os.environ.get('CM_GUI_GRAPH_EXPERIMENT_AXIS_KEY_S','')
        q_axis_key_s = query_params.get('s',[''])
        if len(q_axis_key_s)>0:
            axis_key_s = q_axis_key_s[0]
        i_axis_key_s = 0
        if axis_key_s != '' and axis_key_s in keys: i_axis_key_s = keys.index(axis_key_s)
        axis_key_s = st.selectbox('Select Style key', keys, index=i_axis_key_s, key='s')


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
        fig, ax = plt.subplots() #figsize=(6,4))

        ax.set_xlabel(axis_key_x)
        ax.set_ylabel(axis_key_y)

        title = os.environ.get('CM_GUI_GRAPH_EXPERIMENT_TITLE', '')
        q_title = query_params.get('title',[''])
        if len(q_title)>0:
            if q_title[0]!='':
                title = q_title[0]
        ax.set_title(title, size=16)

        if how == 'bar':
            ax.set_title('Under development ...', size=16)
            ax.yaxis.grid(linestyle = 'dotted')
        else:
            ax.grid(linestyle = 'dotted')
        #https://matplotlib.org/stable/api/markers_api.html

        unique_color_values = {}
#        unique_colors = list(mcolors.CSS4_COLORS.keys())
        unique_colors = list(mcolors.TABLEAU_COLORS.keys())
        i_unique_color_values = 0

        unique_style_values = {}
#        unique_styles = ['o','v','^','<','>','1','2','3','4','8','s','p','P','*','+','D']
        unique_styles = ['circle', 'square', 'diamond', 'cross', 'x', 'triangle', 'pentagon', 'hexagram', 
                         'star', 'hourglass', 'bowtie', 'asterisk', 'hash']
        i_unique_style_values = 0

        # If Bar, use Style to separate results
        unique_x_values = []
        unique_s_values = []

        experiment_uids = []

        # Filter values
        values2 = []

        for result in values:
            if filter_value!='':
                try:
                   if not eval(filter_value):
                       continue
                except Exception as e:
                   if not error_shown:
                       st.markdown('*Syntax error in filter: {}*'.format(e))
                       error_shown = True

            values2.append(result)

            if how == 'bar':
                x = result.get(axis_key_x, None)
                if x != None and x!='' and x not in unique_x_values:
                    unique_x_values.append(x)

                s = result.get(axis_key_s, None)
                if s != None and s!='' and s not in unique_s_values:
                    unique_s_values.append(s)

        ############################################################################
        # Continue visualizing
        if how == '2d-static' or how == 'bar':

            xx = []
            yy = []
            cc = []
            ss = []
            io = []
            
            t = 0
            for result in values2:
                v = result

                t+=1

                x = v.get(axis_key_x, None)
                y = v.get(axis_key_y, None)

                xx.append(x)
                yy.append(y)

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

                cc.append(color)

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

                ss.append(style)

                info=''
                for key in sorted(v.keys(), key=lambda x: x.lower()):
                    value = v[key]
                    info+=str(key)+': '+str(value)+'<br>\n'

                io.append(info)

            import plotly.express as px

            dd = {axis_key_x:xx,axis_key_y:yy,axis_key_c:cc,axis_key_s:ss,'info':io}

            # https://docs.streamlit.io/library/api-reference/charts/st.bar_chart
            # https://docs.streamlit.io/library/api-reference/charts/st.plotly_chart
            # https://plotly.com/python/line-and-scatter/

            df = pd.DataFrame(dd)

            if how == 'bar':
                st.bar_chart(df, x=axis_key_x, y=axis_key_y)
            else:
                fig = px.scatter(df, x=axis_key_x, y=axis_key_y, color=axis_key_c, symbol=axis_key_s, hover_name='info', height=1000)

                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
                  
        

        elif how == '2d':
            #####################################################################
            # 2D interactive graph - very slow - need to be updated
            width = 1
            
            t = 0
            for result in values2:
                v = result

                t+=1

                x = v.get(axis_key_x, None)
                y = v.get(axis_key_y, None)

                url = v.get('url','')
                if url=='': url = v.get('git_url','')

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

                experiment_uid = v.get('experiment_uid','')
                if experiment_uid!='' and experiment_uid not in experiment_uids:
                    experiment_uids.append(experiment_uid)
                
                uid = v.get('uid','')
                if uid!='':
                    xaction = 'action={}&'.format(action) if action!='' else ''
                    url = '?{}name={}&result_uid={}'.format(xaction, experiment_uid, uid)

                if url!='':
                    targets = [url]
                    plugins.connect(fig, OpenBrowserOnClick(graph, targets = targets)) 

            # Render graph
            fig_html = mpld3.fig_to_html(fig)
            components.html(fig_html, width=1100, height=500)

            #fig_html = '<div style="padding:10px;background-color:#F0F0F0;">'+fig_html+'</div>'

            #components.html(fig_html, width=1000, height=800)
            #st.markdown('---')

        ########################################################################
        # Show all data
        df = pd.DataFrame(
          all_data,
          columns=(k for k in sorted_keys if k!='')
        )

        st.markdown('---')
        st.dataframe(df)

        # Check if can create self link
        if len(experiment_uids)==1:
            st.markdown("""---""")

            xtype = '&type={}'.format(how) if how!='' else ''

            end_html='''
             <center>
              <small><a href="{}{}"><i>Self link</i></a></small>
             </center>
             '''.format(misc.make_url(experiment_uids[0], action=action, md=False), xtype)

            st.write(end_html, unsafe_allow_html=True)


    return {'return':0}




if __name__ == "__main__":
    r = main()

    if r['return']>0: 
       
        st.markdown("""---""")
        st.markdown('**Error detected by CM:** {}'.format(r['error']))
