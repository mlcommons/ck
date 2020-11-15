#
# Collective Knowledge (universal advice about experiments, bugs, models, 
#                       features, optimizations, adaptation, 
#                       community remarks ...)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin, Grigori.Fursin@cTuning.org, http://fursin.net
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel) 

# Local settings

hextra='<center>\n'
hextra+=' [ <a href="http://cKnowledge.org/ai.html">Project website</a> ], '
hextra+=' [ <a href="http://cKnowledge.org/partners.html">Partners</a> ], '
hextra+=' [ <a href="http://dividiti.blogspot.fr/2017/02/we-received-test-of-time-award-for-our.html">CGO\'17 test of time award for our interdisiplinary R&D</a> ], '
hextra+=' [ <a href="http://cKnowledge.org/ai">Community-driven AI R&D powered by CK</a> ], '
hextra+=' [ <a href="https://github.com/dividiti/ck-caffe">CK-Caffe</a> ], '
hextra+=' [ <a href="https://github.com/ctuning/ck-tensorflow">CK-TensorFlow</a> ], '
hextra+=' [ <a href="https://en.wikipedia.org/wiki/Collective_Knowledge_(software)">Wikipedia</a>, \n'
hextra+='<a href="https://www.researchgate.net/publication/304010295_Collective_Knowledge_Towards_RD_Sustainability">paper 1</a>, \n'
hextra+='<a href="https://arxiv.org/abs/1506.06256">Paper 2</a>, \n'
hextra+='<a href="https://www.youtube.com/watch?v=Q94yWxXUMP0">YouTube CK intro</a> ] \n'
hextra+='</center>\n'
hextra+='\n'

form_name='ck_ai_web_form'
onchange='document.'+form_name+'.submit();'

##############################################################################
# Initialize module

def init(i):
    """

    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    return {'return':0}

##############################################################################
# access available CK-AI self-optimizing functions

def show(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import copy

    h=''
    st=''

    h+='<center>\n'
    h+='\n\n<script language="JavaScript">function copyToClipboard (text) {window.prompt ("Copy to clipboard: Ctrl+C, Enter", text);}</script>\n\n' 

#    h+='<h2>Aggregated results from Caffe crowd-benchmarking (time, accuracy, energy, cost, ...)</h2>\n'

    h+=hextra

    # Check host URL prefix and default module/action
    rx=ck.access({'action':'form_url_prefix',
                  'module_uoa':'wfe',
                  'host':i.get('host',''), 
                  'port':i.get('port',''), 
                  'template':i.get('template','')})
    if rx['return']>0: return rx
    url0=rx['url']
    template=rx['template']

    url=url0
    action=i.get('action','')
    muoa=i.get('module_uoa','')

    url+='action=index&module_uoa=wfe&native_action='+action+'&'+'native_module_uoa='+muoa
    url1=url

    # Start form
    r=ck.access({'action':'start_form',
                 'module_uoa':cfg['module_deps']['wfe'],
                 'url':url1,
                 'name':form_name})
    if r['return']>0: return r
    h+=r['html']

    # Check available API is modules
    r=ck.access({'action':'search',
                 'module_uoa':cfg['module_deps']['module'],
                 'tags':'ck-ai-json-web-api'})
    if r['return']>0: return r
    l=r['lst']

    if len(l)==0:
       h='<b>WARNING:</b> No CK modules found with CK AI JSON web API\n'
    else:
       dt=[{'name':'', 'value':''}]

       for x in l:
           v=x['data_uid']

           # Load module info
           r=ck.access({'action':'load',
                        'module_uoa':cfg['module_deps']['module'],
                        'data_uoa':v})
           if r['return']>0: return r

           d=r['dict']

           name=d.get('actions',{}).get('ask_ai_web',{}).get('desc','')

           if name!='':
              dt.append({'name':name, 'value':v})

       # Create selector
       ai=i.get('ai_scenario','')

       ii={'action':'create_selector',
           'module_uoa':cfg['module_deps']['wfe'],
           'data':dt,
           'name':'ai_scenario',
           'onchange':onchange, 
           'skip_sort':'yes',
           'selected_value':ai}
       r=ck.access(ii)
       if r['return']>0: return r
       x=r['html']

       h+='<br><b>Select AI scenario with unified <a href="https://github.com/ctuning/ck/wiki/Unifying-AI-API">CK AI JSON API</a> :</b><br><br>'+x+'<br><br><br>'

       # Render scenario
       if ai!='':
          ii=copy.deepcopy(i)

          ii['action']='ask_ai_web'
          ii['module_uoa']=ai

          ii['widget']='yes'
          ii['prepared_url0']=url0
          ii['prepared_url1']=url1
          ii['prepared_form_name']=form_name

          r=ck.access(ii)
          if r['return']>0: return r

          h+='<div id="ck_box_with_shadow">\n'
          h+='\n\n'+r.get('html','')
          h+='</div>\n'

          st+='\n'+r.get('style','')+'\n'

    h+='<h2>Want to survive Cambrian AI/SW/HW explosion but lost in technological chaos?</h2>\n'
    h+='<img src="http://cKnowledge.org/images/ai-cloud-resize.png"><br><br>\n'

    h+='<b>Join the growing <a href="http://cKnowledge.org/partners.html">consortium</a>\n' 
    h+='using and enhancing <a href="http://cKnowledge.org">Collective Knowledge technology</a> to\n'
    h+=' a) clean up this mess, b) reinvent computer engineering and make it more collaborative, reproducible and reusable,\n'
    h+=' c) develop efficient and reliable computer systems from IoT to supercomputers, \n'
    h+=' d) enable open science via reusable and customizable artifacts,\n'
    h+='  and e) eventually enable and accelerate open AI research!\n'

    return {'return':0, 'html':h, 'style':st}

##############################################################################
# CK-AI dashboard

def browse(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    i['action']='browser'
    i['cid']=''
    i['module_uoa']=''
    i['template']='ck-ai-basic'

    return ck.access(i)

##############################################################################
# ask AI advice via CK JSON API and CK DNN engines

def ask(i):
    """
    Input:  {
              to - which advice ("predict_compiler_flags", "classify_image")

              (local) - if 'yes', use local optimization rather than public from cKnowledge.org/repo

              If predict_compiler_flags:

                compiler - compiler name
                  See GCC: http://cknowledge.org/repo/web.php?native_action=show&native_module_uoa=program.optimization&scenario=8289e0cf24346aa7
                  See LLVM: http://cknowledge.org/repo/web.php?native_action=show&native_module_uoa=program.optimization&scenario=2aaed4c520956635

                scenario
                cpu_name
                features (MILEPOST feature vector: http://ctuning.org/wiki/index.php/CTools:MilepostGCC:StaticFeatures:MILEPOST_V2.1)

              If classify_image

                dnn_engine (caffe, caffe2, tensorflow)
                image  - file with image
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    to=i.get('to','')
    if to=='':
       return {'return':1, 'error':'--to is not defined'}

    # Check where to look for optimizations
    er=i.get('exchange_repo','')
    if er=='': er=ck.cfg['default_exchange_repo_uoa']
    esr=''

    aa='show_json'
    if i.get('local','')=='yes': 
       er='local'
       esr=''
       aa='show'

    rr={'return':0}

    if to=='predict_compiler_flags':
       # This is just a demo of MILEPOST project combined with CK-powered collective optimization
       # We plan to considerably improve modeling based on our Collective Mind part II vision paper
       # (bringing community to share optimizations, features, models and enable dynamic adaptation).

       # Check if module exists
       r=ck.access({'action':'find',
                    'module_uoa':cfg['module_deps']['module'],
                    'data_uoa':cfg['module_deps']['milepost']})
       if r['return']>0 and r['return']!=16: return r

       if r['return']==16:
          return {'return':1, 'error':'Please, install CK MILEPOST repository using "ck pull repo:reproduce-milepost-project"'}

       compiler=i.get('compiler','')
       if compiler=='':
          return {'return':1, 'error':'--compiler is not defined'}

       scenario=i.get('scenario','')
       if scenario=='': 
          if compiler.lower().startswith('gcc'):
             scenario=cfg['module_deps']['experiment.tune.compiler.flags.gcc.e']
          elif compiler.lower().startswith('llvm'):
             scenario=cfg['module_deps']['experiment.tune.compiler.flags.llvm.e']
          else:
             return {'return':1, 'error':'scenario is not defined (see "ck search module --tags="program optimization,program-features"'}

       cpu_name=i.get('cpu_name','')
       if cpu_name=='':
          return {'return':1, 'error':'--cpu_name is not defined'}

       features=i.get('features',[])

       xfeatures={}
       for k in i:
           if k.startswith('ft'):
              k1=int(k[2:])
              v1=i[k]
              xfeatures[k1]=v1

       for k in range(0,66):
           if k in xfeatures:
              features.append(xfeatures[k])

       if len(features)==0:
          return {'return':1, 'error':'feature vector is not defined'}

       # Search optimization results
       ii={'action':aa,
           'module_uoa':cfg['module_deps']['program.optimization'],
           'repo_uoa':er,
           'remote_repo_uoa':esr,
           'scenario':scenario,
           '__web_prune__compiler':compiler,
           '__web_prune__cpu_name':cpu_name,
           'skip_html':'yes'}

       r=ck.access(ii)
       if r['return']>0: return r

       results=r['results']
       if len(results)==0:
          return {'return':1, 'error':'optimization results are not found for such configuration'}

       if len(results)>1:
          return {'return':1, 'error':'ambiguity - more then 1 configuration found'}

       # Predict
       muoa=results[0]['module_uoa']
       duoa=results[0]['data_uoa']

       ii={'action':aa,
           'module_uoa':cfg['module_deps']['milepost'],
           'repo_uoa':er,
           'remote_repo_uoa':esr,
           'view_solution_'+muoa+'_'+duoa:'',
           'skip_html':'yes'}

       j=1
       for v in features:
           ii['mft'+str(j)]=v
           j+=1

       rr=ck.access(ii)
       if rr['return']>0: return rr

       popt=rr.get('predicted_opt','')

       if popt=='':
          ck.out('WARNING: could not predict optimization')
       else:
          ck.out('Predicted optimization:')
          ck.out('')
          ck.out(popt)

    ############################################################################################################
    elif to=='classify_image':

       engine=i.get('dnn_engine','')
       if engine=='': engine='caffe'

       image=i.get('image','')
       if image=='' or not os.path.isfile(image):
          return {'return':1, 'error':'image not found'}

       r=ck.convert_file_to_upload_string({'filename':image})
       if r['return']>0: return r

       fcb64=r['file_content_base64']

       # Search optimization results
       ii={'action':aa,
           'module_uoa':cfg['module_deps']['model.image.classification'],
           'repo_uoa':er,
           'remote_repo_uoa':esr,
           'dnn_engine':engine,
           'file_content_base64':fcb64,
           'skip_html':'yes'}

       rr=ck.access(ii)
       if rr['return']>0: return rr

       warning=rr.get('warning','')
       prediction=rr.get('prediction','')

       if warning!='':
          ck.out('WARNING: '+warning)

       if prediction!='':
          ck.out('')
          ck.out('Preciction:')
          ck.out('')
          ck.out(prediction)

    else:
       return {'return':1, 'error':'we do not have such scenario yet ('+to+')'}

    return rr
