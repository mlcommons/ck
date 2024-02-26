# Developer(s): Grigori Fursin

import cmind
import os
import misc

import streamlit.components.v1 as components

import streamlit as st

import json

announcement = 'Under development - please get in touch via [Discord](https://discord.gg/JjWNWXKxwT) for more details ...'

badges={
        'functional':{'url':'https://cTuning.org/images/artifacts_evaluated_functional_v1_1_small.png'},
        'reproduced':{'url':'https://cTuning.org/images/results_reproduced_v1_1_small.png'},
        'support_docker':{'url':'https://cTuning.org/images/docker_logo2_small.png'},
        'support_cm':{'url':'https://cTuning.org/images/logo-ck-single-tr4.png'}
       }


def main():
    params = misc.get_params(st)

    # Set title
    st.title('Reproducibility studies')

    st.markdown(announcement)

    return page(st, params)




def page(st, params, action = ''):

    end_html = ''


#    st.markdown('----')

    self_url = misc.make_url('', key='', action='reproduce', md=False)
    url_benchmarks = misc.make_url('', key='', action='howtorun', md=False)
    url_challenges = misc.make_url('', key='', action='challenges', md=False)

    # Some info
    x = '''
         <i>
         <small>
         [Under development] This is a new project to reproduce <a href="{}">modular benchmarks</a> 
         across different models, data sets, software and hardware 
         via <a href="{}">open challenges</a>
         based on the <a href="https://cTuning.org/ae">ACM/cTuning reproducibility methodology and badges</a>
         and <a href="https://sites.google.com/g.harvard.edu/mlperf-bench-hpca24/home">automatically compose 
         High-Performance and Cost-Efficient AI Systems with MLCommons' Collective Mind and MLPerf</a>.
         Note that this is a <a href="https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md">collaborative engineering effort</a> 
         - please report encountered issues and provide feedback
         <a href="https://github.com/mlcommons/ck/issues">here</a>
         and get in touch via <a href="https://discord.gg/JjWNWXKxwT">Discord</a>!
         </small>
         </i>
          <br>
          <br>
        '''.format(url_benchmarks, url_challenges)

    st.write(x, unsafe_allow_html = True)
    

    return {'return':0}


#    st.markdown(announcement)

    # Check if test is selected
    test_uid = ''
    x = params.get('test_uid',[''])
    if len(x)>0 and x[0]!='': test_uid = x[0].strip()


    ############################################################################################
    # Select target hardware
    compute_uid = ''
    compute_meta = {}
    compute_selection = []

    if test_uid == '':
        x = params.get('compute_uid',[''])
        if len(x)>0 and x[0]!='': compute_uid = x[0].strip()
    
    ii = {'action':'load_cfg',
          'automation':'utils',
          'tags':'benchmark,compute',
          'skip_files':False}

    if compute_uid!='':
        ii['prune']={'uid':compute_uid}

    r = cmind.access(ii)
    if r['return']>0: return r
    compute_selection = r['selection']

    if test_uid == '':
        r = misc.make_selection(st, r['selection'], 'compute', 'target hardware', compute_uid)
        if r['return']>0: return r
        compute_meta = r['meta']
        compute_uid = compute_meta.get('uid','')


    ############################################################################################
    # Select benchmark
    bench_meta = {}

    bench_name = ''
    x = params.get('bench_name',[''])
    if len(x)>0 and x[0]!='': bench_name = x[0].strip()

    if test_uid == '':
        ii = {'action':'load_cfg',
              'automation':'utils',
              'tags':'benchmark,run',
              'skip_files':True}

        if bench_name!='':
            ii['artifact']=bench_name

        r = cmind.access(ii)
        if r['return']>0: return r

        # Prune by supported compute
        selection = r['selection']
        pruned_selection = []

        if compute_uid == '':
            pruned_selection = selection
        else:
            for s in selection:
                add = True

                if compute_uid in s.get('supported_compute',[]):
                    pruned_selection.append(s)

        r = misc.make_selection(st, pruned_selection, 'benchmark', 'benchmark', bench_name)
        if r['return']>0: return r

        bench_meta = r['meta']

    ############################################################################################
    # Select tests
    if test_uid == '' and compute_uid == '' and len(bench_meta) == 0:
        st.markdown('*Please prune search by device and/or benchmark ...*')

    else:
        ii = {'action':'load_cfg',
              'automation':'utils',
              'tags':'benchmark,run',
              'key':'run-',
              'key_end':['-meta.json', '-meta.yaml'],
              'skip_files':False}

        if len(bench_meta)>0 or bench_name!='':
            if len(bench_meta)>0:
                ii['artifact']=bench_meta['uid']
            else:
                ii['artifact']=bench_name
        elif compute_uid !='' :
            ii['prune']={'meta_key':'supported_compute',
                         'meta_key_uid':compute_uid}

        if compute_uid != '':
            if 'prune' not in ii: ii['prune']={}
            ii['prune']['key'] = 'compute_uid'
            ii['prune']['key_uid'] = compute_uid

        if test_uid!='':
            if 'prune' not in ii: ii['prune']={}
            ii['prune']['uid']=test_uid

        r = cmind.access(ii)
        if r['return']>0: return r

        # Prune by supported compute
        selection = r['selection']

        if len(selection)==0:
            st.markdown('*WARNING: No tests found!*')
        else:
            if len(selection)==1:
                ###################################################################
                # Show individual test
                s = selection[0]

                full_path = s['full_path']
                test_uid = s['uid']

                st.markdown('---')
                st.markdown('**Test {}**'.format(test_uid))

                # Check badges
                x = ''

                for b in badges:
                    if s.get(b, False) or b=='support_cm':
                        x += '<a href="http://cTuning.org/ae" target="_blank"><img src="{}" height="64"></a>\n'.format(badges[b]['url'])

                if x!='':
                    st.write(x, unsafe_allow_html = True)

                # Check benchmark
                bench_uid = s.get('bench_uid','')
                if bench_uid != '':
                    url_bench = url_benchmarks + '&bench_uid='+bench_uid
                    st.markdown('[Link to benchmark GUI]({})'.format(url_bench))
                
                # Check notes
                test_md = full_path[:-10]+'.md'
                if os.path.isfile(test_md):

                    r = cmind.utils.load_txt(test_md)
                    if r['return']>0: return r

                    x = r['string']

                    if x!='':
                        st.markdown('**Notes:**')
                        st.markdown(x)

                inp = {}
                input_file = full_path[:-10]+'-input'
                r = cmind.utils.load_yaml_and_json(input_file)
                if r['return']==0:
                    inp = r['meta']

                out = {}
                output_file = full_path[:-10]+'-output'
                r = cmind.utils.load_yaml_and_json(output_file)
                if r['return']==0:
                    out = r['meta']

                cmd = inp.get('cmd',[])
                if len(cmd)>0:
                   xcmd = ' \\\n   '.join(cmd)

                   st.markdown("""
**CM command line:**
```bash
cm run script {}
```
                               """.format(xcmd))

                
                st.markdown("""
**CM input dictionary:**
```json
{}
```
                           """.format(json.dumps(inp, indent=2)))


                st.markdown("""
**CM input dictionary:**
```json
{}
```
                               """.format(json.dumps(out, indent=2)))

                               
                st.markdown("""

**Test meta:**
```json
{}
```
                            """.format(json.dumps(s, indent=2)))


            else:
                ###################################################################
                # Show tables
                import pandas as pd
                import numpy as np

                html = ''

                all_data = []
                

                # TBD: should be taken from a given benchmark
                dimensions = []

                if len(bench_meta)>0:
                    dimensions = bench_meta.get('view_dimensions', [])

                dimension_values = {}
                dimension_keys = []
                              
                if len(dimensions) == 0:
                    keys = [('test', 'CM test', 400, 'leftAligned')]
                else:
                    keys = [('test', 'CM test', 50, 'leftAligned')]

                    for k in dimensions:
                        key = k[0]

                        keys.append((k[0], k[1], 100, 'leftAligned'))

                        dimension_values[key] = []
                        dimension_keys.append(key)

                    # If dimensions, sort by dimensions
                    for d in list(reversed(dimension_keys)):
                        selection = sorted(selection, key = lambda x: misc.get_with_complex_key_safe(selection, d))

                keys += [
                         ('functional', '<a href="https://github.com/mlcommons/ck/blob/master/docs/artifact-evaluation/submission.md">Functional</a>', 80, ''),
                         ('reproduced', '<a href="https://github.com/mlcommons/ck/blob/master/docs/artifact-evaluation/submission.md">Reproduced</a>', 80, ''),
                         ('support_docker', 'Support Docker', 80, ''),
                         ('support_cm', '<a href="https://github.com/mlcommons/ck">Has unified CM interface</a>', 80, ''),
                         ('notes', 'Notes', 200, 'lefAligned'),
                        ]

                j = 0


                for s in selection:

                    row = {}
                    
                    full_path = s['full_path']
                    test_uid = s['uid']

                    uid = s['uid']

                    url_test = misc.make_url(uid, key='test_uid', action='reproduce', md=False)
                    
                    bench_meta = s['main_meta']

                    inp = {}
                    input_file = full_path[:-10]+'-input'
                    r = cmind.utils.load_yaml_and_json(input_file)
                    if r['return']==0:
                        inp = r['meta']

                    out = {}
                    output_file = full_path[:-10]+'-output'
                    r = cmind.utils.load_yaml_and_json(output_file)
                    if r['return']==0:
                        out = r['meta']

                    row_meta = {'dict': s,
                                'input': inp,
                                'output': out}

                    if len(dimensions) == 0:
                        row['test'] = '<a href="{}" target="_blank">{}</a>'.format(url_test, uid)
                    else:
                        row['test'] = '<a href="{}" target="_blank">View</a>'.format(url_test)
                        for k in dimensions:
                            kk = k[0]

                            v = misc.get_with_complex_key_safe(row_meta, kk)

                            if len(k)>2 and k[2]=='tick':
                                if v!=None and v!='':
                                    v = '✅'
                            
                            row[kk] = str(v)


                    # Check ACM/IEEE functional badge
                    url = ''
                    
                    x = ''
                    if s.get('functional', False):
                        x = '<center><a href="{}" target="_blank"><img src="{}" height="32"></a></center>'.format(url, badges['functional']['url'])
                    row['functional'] = x

                    # Check ACM/IEEE reproduced badge
                    x = ''
                    if s.get('reproduced', False):
                        x = '<center><a href="{}" target="_blank"><img src="{}" height="32"></a></center>'.format(url, badges['reproduced']['url'])
                    row['reproduced'] = x

                    # Check Docker
                    x = ''
                    if s.get('support_docker', False):
                        x = '<center><a href="{}" target="_blank"><img src="{}" height="32"></a></center>'.format(url, badges['support_docker']['url'])
                    row['support_docker'] = x

                    x = ''
                    bench_uid = s.get('bench_uid','')
                    if bench_uid != '':
                        url_bench = url_benchmarks + '&bench_uid='+bench_uid
                        x = '<center><a href="{}" target="_blank"><img src="{}" height="32"></a></center>'.format(url_bench, badges['support_cm']['url'])
                    row['support_cm'] = x
                    
                    # Check misc notes
                    row['notes']='<small>'+s.get('notes','')+'</small>'
                    
                    # Finish row
                    all_data.append(row)

                # Visualize table
                pd_keys = [v[0] for v in keys]
                pd_key_names = [v[1] for v in keys]

                pd_all_data = []
                for row in sorted(all_data, key=lambda row: (row.get('x1',0))):
                    pd_row=[]
                    for k in pd_keys:
                        pd_row.append(row.get(k))
                    pd_all_data.append(pd_row)

                df = pd.DataFrame(pd_all_data, columns = pd_key_names)

                df.index+=1

                html=df.to_html(escape=False, justify='left')
                st.write(html, unsafe_allow_html = True)






    if bench_name!='':
        self_url+='&bench_name='+bench_name
    if test_uid!='':
        self_url+='&test_uid='+test_uid    
    elif compute_uid!='':
        self_url+='&compute_uid='+compute_uid

    end_html='<center><small><i><a href="{}">Self link</a></i></small></center>'.format(self_url)

    
    return {'return': 0, 'end_html': end_html}
