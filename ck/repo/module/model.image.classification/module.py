#
# Collective Knowledge (classify image using various models such as DNN)
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
hextra='<i><center>\n'
hextra+=' [ <a href="http://cKnowledge.org/ai">Community-driven AI R&D powered by CK</a> ], '
hextra+=' [ <a href="https://github.com/dividiti/ck-caffe">CK-Caffe</a> ], '
hextra+=' [ <a href="https://github.com/ctuning/ck-caffe2">CK-Caffe2</a> ], '
hextra+=' [ <a href="https://github.com/ctuning/ck-tensorflow">CK-TensorFlow</a> ], '
hextra+=' [ <a href="https://en.wikipedia.org/wiki/Collective_Knowledge_(software)">Wikipedia</a>, \n'
hextra+='<a href="https://www.researchgate.net/publication/304010295_Collective_Knowledge_Towards_RD_Sustainability">paper 1</a>, \n'
hextra+='<a href="https://arxiv.org/abs/1506.06256">Paper 2</a>, \n'
hextra+='<a href="https://www.youtube.com/watch?v=Q94yWxXUMP0">YouTube CK intro</a> ] \n'
hextra+='</center></i>\n'
hextra+='<br>\n'

hextra+='Optimizations results are continuously shared by volunteers across diverse programs, data sets and platforms: '
hextra+='<a href="http://cknowledge.org/repo/web.php?native_action=show&native_module_uoa=program.optimization&scenario=4dcf435bb0d92fa6">GCC</a> , \n'
hextra+='<a href="http://cknowledge.org/repo/web.php?native_action=show&native_module_uoa=program.optimization&scenario=1eb2f50d4620903e">LLVM</a> \n'

dlabels='collective_training_set'

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
# show dashboard

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

    import os
    import shutil
    import time
    import copy

    form_name='milepost_web_form'

    sh=i.get('skip_html','')

    ww=False
    if i.get('widget','')=='yes': ww=True

    # State reset
    dar=False
    if 'dnn_action_reset' in i: 
       dar=True

    # Start HTML
    h=''
    st=''

    h+='<center>\n'
    h+='\n\n<script language="JavaScript">function copyToClipboard (text) {window.prompt ("Copy to clipboard: Ctrl+C, Enter", text);}</script>\n\n' 

    if not ww:
       h+=hextra

    if ww:
       url0=i.get('prepared_url0','')
       url1=i.get('prepared_url1','')
       form_name=i.get('prepared_form_name','')
    else:
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

    url=url0
    onchange='document.'+form_name+'.submit();'

    # Header
    if not ww:
       h+='<h2>Unified CK AI JSON API to classify images using different DNN engines (Caffe, TensorFlow, etc) while monitoring/optimizing performance</h2>\n'

    # Select engine
    dt=[
        {'name':'Caffe', 'value':'caffe'},
        {'name':'Caffe2','value':'caffe2'},
        {'name':'TensorFlow', 'value':'tensorflow'}
       ]

    engine=i.get('dnn_engine','')
    if engine=='': engine='caffe'

    ii={'action':'create_selector',
        'module_uoa':cfg['module_deps']['wfe'],
        'data':dt,
        'name':'dnn_engine',
        'onchange':onchange, 
        'skip_sort':'yes',
        'selected_value':engine}
    r=ck.access(ii)
    if r['return']>0: return r
    x=r['html']

    h+='DNN engine: '+x+'<br><br>\n'

    # Search env to check if has installed
    r=ck.access({'action':'search',
                 'module_uoa':cfg['module_deps']['env'],
                 'tags':'lib,'+engine})
    if r['return']>0: return r
    el=r['lst']

    warning=''
    prediction=''

    if len(el)==0:
       h+='<i>DNN engine is not installed - contact <a href="mailto:admin@cKnowledge.org">admin</a> to install this engine and related models in the CK AI cloud</i><br><br>'
       warning='DNN engine is not installed'
    else:
       h+='<i>'+str(len(el))+' engine(s) installed (different optimizations and platforms)</i><br>'

       # Search models to check if has installed
       tx=engine+'model'
       if engine=='caffe2':
          tx='caffemodel2'

       r=ck.access({'action':'search',
                    'module_uoa':cfg['module_deps']['env'],
                    'tags':tx})
       if r['return']>0: return r
       models=r['lst']

       if len(models)==0:
          h+='<i>DNN models for this engine are not installed - contact <a href="mailto:admin@cKnowledge.org">admin</a> to install more models in the CK AI cloud</i><br><br>'
          warning='DNN models for this engine are not installed'
       else:
          h+='<i>'+str(len(models))+' model(s) installed (different topology and parameters)</i><br><br>'

          h+='<i>Optimization statistics shared by the community:\n'
          h+='[ <a href="http://cknowledge.org/repo/web.php?native_action=show&native_module_uoa=program.optimization&scenario=1eb2f50d4620903e">desktops and servers</a> ], \n'
          h+='[ <a href="http://cknowledge.org/repo/web.php?native_action=show&native_module_uoa=program.optimization&scenario=4dcf435bb0d92fa6">mobile devices and IoT</a> ] \n'
          h+='</i><br>'

          h+='<i>Mispredictions shared by the community:\n'
          h+='[ <a href="http://cknowledge.org/repo/web.php?wcid='+work['self_module_uid']+':'+dlabels+'">images and classifications</a> ] \n'
          h+='</i><br><br>'


          fc=i.get('file_content_base64','')
          fcu=i.get('file_content_uploaded','')

          if dar: 
             fc=''
             fcu=''

          if 'dnn_add_correct_label' in i:
             # Record correct label
             ftmp=i.get('dnn_saved_image_file','')
             label=i.get('dnn_correct_label','').strip()

             wlabel=i.get('dnn_original_classification','').strip()
 
             if label!='' and os.path.isfile(ftmp):
                # Check if already has holder for correct images
                r=ck.access({'action':'find',
                             'module_uoa':work['self_module_uid'],
                             'data_uoa':dlabels,
                             'repo_uoa':ck.cfg.get('record_local_repo_uoa','')})
                if r['return']>0 and r['return']!=16: return r
                if r['return']==16:
                   r=ck.access({'action':'add',
                                'module_uoa':work['self_module_uid'],
                                'data_uoa':dlabels,
                                'repo_uoa':ck.cfg.get('record_local_repo_uoa','')})
                   if r['return']>0: return r
                pl=r['path']

                # Copy image
                pl1=os.path.join(pl,os.path.basename(ftmp))
                shutil.copy(ftmp,pl1)

                # Record label
                r=ck.save_text_file({'text_file':pl1+'.label', 'string':label})
                if r['return']>0: return r

                if wlabel!='':
                   r=ck.save_text_file({'text_file':pl1+'.wrong_label', 'string':wlabel})
                   if r['return']>0: return r

                # Record label
                h+='<b>Thank you for submitting correct label and participating in a creation of a realistic and collective training sets!</b><br><br>\n'
          else:
             if fc=='' and fcu=='':
                # Select image
                h+='Your JPEG image: <input type="file" name="file_content"><br><br>'
                h+='<input type="submit" value="Classify using CK DNN cloud"><br><br>'
             else:
                # Gen tmp file
                rx=ck.gen_tmp_file({'prefix':'tmp-', 'suffix':'.jpg'})
                if rx['return']>0: return rx
                ftmp=rx['file_name']

                if fcu=='':
                   # Save user image
                   rx=ck.convert_upload_string_to_file({'file_content_base64':fc,
                                                        'filename':ftmp})
                   if rx['return']>0: return rx
                else:
                   shutil.copy(fcu,ftmp)

                h+='<input type="hidden" name="dnn_saved_image_file" value="'+ftmp+'">\n'

                # Classify
                ii={'action':'run',
                    'module_uoa':cfg['module_deps']['program'],
                    'data_uoa':cfg['classify_program'][engine],
                    'cmd_key':'classify_ck_ai_api',
                    'quiet':'yes',
                    'generate_rnd_tmp_dir':'yes',
                    'random':'yes',
                    'env':{'CK_AI_API_IMAGE_FILE':ftmp}}
                r=ck.access(ii)
                if r['return']>0:
                   warning='Problem running DNN engine: '+r['error']
                   h+='<b>WARNING:</b> '+warning+'<br><br>'
                else:
                   ch=r.get('characteristics',{})

                   if ch.get('run_success','')!='yes':
                      warning='Problem running DNN engine: '+ch.get('fail_reason','')
                      h+='<b>WARNING:</b> '+warning+'<br><br>'
                   else:
                      te=ch.get('execution_time','')

                      td=r.get('tmp_dir','')
                      deps=r.get('deps',{})

                      k1=engine+'model'
                      k2='lib-'+engine

                      n1=deps.get(k1,{}).get('name','')+' '+deps.get(k1,{}).get('cus',{}).get('package_extra_name','')
                      n2=deps.get(k2,{}).get('name','')+' '+deps.get(k2,{}).get('cus',{}).get('package_extra_name','')

                      # Attempt to read outputs
                      p1=os.path.join(td,'stdout.log')
                      p2=os.path.join(td,'stderr.log')

                      s1=''
                      s2=''

                      r=ck.load_text_file({'text_file':p1})
                      if r['return']==0: 
                         s1=r['string'].strip()

                      r=ck.load_text_file({'text_file':p2})
                      if r['return']==0:
                         s2=r['string']

                      s=s1+'\n'+s2
                      sx=s.split('\n')

                      sy=''
                      started=False
                      top=''
                      for q in sx:
                          q=q.strip()
                          if started:
                             if top=='': top=q
                             if q=='': break
                             sy+=q+'\n'
                          if q.startswith('-----'):
                             started=True

                      prediction=sy

                      s=sy.strip().replace('\n','<br>')

                      # Create table (left - classification, right - stats)
                      h+='<table border="1" cellpadding="10" cellspacing="0">\n'
                      h+=' <tr>\n'
                      h+='  <td valign="top">\n'

                      h+='   <b>Classification output:</b><br><br>\n'
                      h+=    s+'<br><br>\n'

                      h+='   <input type="hidden" name="dnn_original_classification" value="'+prediction.replace('"','\'')+'">\n'

                      h+='   <center>\n'
                      h+='   <b>If classification is wrong, please provide correct label:</b><br><input type="text" name="dnn_correct_label"><br><br>\n'
                      h+='   <button type="submit" name="dnn_add_correct_label">Submit label</button>\n'
                      h+='   ( <a href="'+url0+'&wcid='+work['self_module_uid']+':'+dlabels+'">view shared labels</a> )\n'
                      h+='   </center>\n'

                      h+='  </td>\n'

                      h+='  <td valign="top">\n'
                      h+='    <b>Engine species:</b> '+n2+'<br><br>'
                      h+='    <b>Model variant: </b> '+n1+'<br><br>'

                      h+='    <b>Execution time: </b> '+( '%.1f' % te )+' sec.<br>'

                      h+='  </td>\n'
                      h+=' </tr>\n'
                      h+='</table>\n'

          h+='<br><br>'
          h+='<button type="submit" name="dnn_action_reset">Start again</button>\n'
          h+='<br><br>'

    if sh=='yes':
       h=''
       st=''

    return {'return':0, 'html':h, 'style':st, 'warning':warning, 'prediction':prediction}

##############################################################################
# open dashboard

def dashboard(i):
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
    i['extra_url']='native_action=show&native_module_uoa=model.image.classification'

    return ck.access(i)

##############################################################################
# CK AI JSON API for web (needed to automatically find such function from higher-level CK AI API)

def ask_ai_web(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    return show(i)

##############################################################################
# return json instead of html

def show_json(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    r=show(i)

    if 'html' in r: del(r['html'])
    if 'style' in r: del(r['style'])

    return r

##############################################################################
# user-friendly html view

def html_viewer(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    h='' #'<hr>'

    # Check host URL prefix and default module/action *********************************************
    rx=ck.access({'action':'form_url_prefix',
                  'module_uoa':cfg['module_deps']['wfe'],
                  'host':i.get('host',''), 
                  'port':i.get('port',''), 
                  'template':i.get('template','')})
    if rx['return']>0: return rx
    url0=rx['url']
    url0w=rx['url'] #rx['url_without_template']
    template=rx['template']

    purl=i['url_pull']

    muoa=i['module_uoa']
    duoa=i['data_uoa']

    r=ck.access({'action':'load',
                 'module_uoa':muoa,
                 'data_uoa':duoa})
    if r['return']>0: return r

    p=r['path']

    # First find images
    l=[]
    d=os.listdir(p)

    for f in d:
        if f.endswith('.jpg'):
           y={'file':f, 'original_file':f, 'url':purl}

           f1=os.path.join(p,f+'.label')
           f2=os.path.join(p,f+'.wrong_label')

           if os.path.isfile(f1):
              r=ck.load_text_file({'text_file':f1})
              if r['return']>0: return r
              x1=r['string'].strip()
              y['label']=x1

           if os.path.isfile(f2):
              r=ck.load_text_file({'text_file':f2})
              if r['return']>0: return r
              x2=r['string'].strip().replace('\n','<br>')
              y['wrong_label']=x2

           l.append(y)

    # Trying to add visualization from Mobile crowd-benchmarking/crowd-tuning/crowd-learning entries
    r=ck.access({'action':'search',
                 'module_uoa':'experiment.bench.dnn.mobile',
                 'add_meta':'yes'})
    if r['return']==0:
       lst=r['lst']

       for q in lst:
           duid=q['data_uid']
           p=q['path']

           # FGG: temporal hack
           xurl=purl.replace('42b9a1221eb50259:287d4bee982e03c1','experiment.bench.dnn.mobile:'+duid)
           yurl=url0+'wcid=experiment.bench.dnn.mobile:'+duid

           arr=q['meta'].get('all_raw_results',[])

           for y in arr:
               m=y.get('mispredictions',[])
               for z in m:
                   f=z.get('mispredicted_image','')
                   px=os.path.join(p,f)
                   if os.path.isfile(px):

                      ff=f+'.cached.jpg'
                      pxx=os.path.join(p,ff)
                      if not os.path.isfile(pxx):
                         try:
                            import PIL
                            from PIL import Image

                            img=Image.open(px)

                            wx=float(240/float(img.size[0]))
                            h=int((float(img.size[1])*wx))

                            img=img.resize((240, h))
                            img.save(pxx)
                         except Exception as e:
                            pass

                      if os.path.isfile(pxx):
                         x1=z.get('correct_answer','')
                         x2=z.get('misprediction_results','').replace('\n','<br>')

                         y={'file':ff, 'original_file':f, 'entry_url':yurl, 'url':xurl, 'label':x1, 'wrong_label':x2}
                         l.append(y)

    if len(l)==0:
       h+='<br><center><b>No shared mispredictions - community training set is empty!</b></center><br>\n'
    else:
       h+='<center>\n'
       h+='<h2>Collaborative and realistic training set (mispredictions)</h2><br>\n'
       h+='<table border="1" cellpadding="8" cellspacing="0">\n'
       h+=' <tr>\n'
       h+='  <td align="center" valign="top"><b>#</b></td>\n'
       h+='  <td align="center" valign="top"><b>Image</b></td>\n'
       h+='  <td align="center" valign="top"><b>Correct classification</b></td>\n'
       h+='  <td align="center" valign="top"><b>Misclassification</b></td>\n'
       h+=' </tr>\n'

       q=0
       for y in l:
           q+=1
           f=y['file']
           ff=y['original_file']
           url=y['url']
           eurl=y.get('entry_url','')
           px=url+f
           pxx=url+ff
           x1=y['label']
           x2=y['wrong_label']

           z=str(q)
           if eurl!='':
              z='<a href="'+eurl+'">'+z+'</a>'

           h+=' <tr>\n'
           h+='  <td align="center" valign="top">'+z+'</td>\n'
           h+='  <td align="center" valign="top"><a href="'+pxx+'"><img src="'+px+'" width="120"></a></td>\n'
           h+='  <td align="center" valign="top">'+x1+'</td>\n'
           h+='  <td align="center" valign="top">'+x2+'</td>\n'
           h+=' </tr>\n'

       h+='</table>\n'
       h+='</center>\n'

    h+='<BR><center><i>Please, report any illegal/copyrighted content <a href="mailto:admin@cKnowledge.org">here</a> and we will remove it within 48 hours!</i></center><br><br>'

    h+='<hr>\n'

    return {'return':0, 'html':h, 'show_top':'yes'}
