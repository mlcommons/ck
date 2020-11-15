#
# Collective Knowledge (preparing experiment reports)
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
var_post_autorefresh='report_autorefresh'
var_post_autorefresh_time='report_autorefresh_time'

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
# viewing entry as html

def html_viewer(i):
    """
    Input:  {
              data_uoa

              url_base
              url_pull

              url_pull_tmp
              tmp_data_uoa

              url_wiki

              html_share

              form_name     - current form name

              (all_params)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    import os

    h=''
    st=''
    raw='no'
    top='yes'

    duoa=i['data_uoa']
    burl=i['url_base']
    purl=i['url_pull']
    wurl=i.get('url_wiki','')

    tpurl=i['url_pull_tmp']
    tpuoa=i['tmp_data_uoa']

    ap=i.get('all_params',{})

    ruoa=ap.get('ck_top_repo','')
    muoa=ap.get('ck_top_module','')

    cparams=ap.get('graph_params','') # current graph params

    hshare=i.get('html_share','')

    form_name=i['form_name']
    form_submit='document.'+form_name+'.submit();'

    if duoa!='':
       # Load entry
       rx=ck.access({'action':'load',
                     'module_uoa':work['self_module_uid'],
                     'data_uoa':duoa})
       if rx['return']>0: return rx

       pp=rx['path']

       dd=rx['dict']
       duid=rx['data_uid']

       # Check what to do with top header
       if dd.get('top','')!='': top=dd['top']

       # Check auto-refresh
       dar=dd.get('auto_refresh','')
       if dar=='yes':
          ar=ap.get(var_post_autorefresh,'')
          art=ap.get(var_post_autorefresh_time,'')
          iart=4

          if art=='':
              art=dd.get('auto_refresh_time','')
          if art!='':
              try:
                 iart=int(art)
              except ValueError:
                 iart=4

          ap[var_post_autorefresh_time]=iart

          if ar=='':
              ar='on'
              ap[var_post_autorefresh]=ar

          if ar=='on':
             h+='\n'
             h+='<script language="javascript">\n'
             h+=' <!--\n'
             h+='  setTimeout(\''+form_submit+'\','+str(iart*1000)+');\n'
             h+=' //-->\n'
             h+='</script>\n'
             h+='\n'

       if dd.get('live','')!='yes':
          raw='yes'
       else:
          title=dd.get('title','')
          sub_title=dd.get('sub_title','')
          authors=dd.get('authors',[])
          affs=dd.get('affiliations',{})
          cauthor=dd.get('cor_author_email','')

          mwc=dd.get('media_wiki_commands','')

          h+='<div id="ck_entries">\n'

          h+='<center><span id="ck_article_title">'+title+'</span><br>\n'

          if sub_title!='':
             h+='<div id="ck_entries_space4"></div>\n'
             h+='<span id="ck_article_authors">\n'
             h+='<i>'+sub_title+'</i><br>\n'
             h+='</span>\n'

          if dd.get('skip_authors','')!='yes':
             if len(authors)!='':
                h+='<div id="ck_entries_space4"></div>\n'
                h+='<span id="ck_article_authors">\n'

                x=''
                for a in authors:
                    name=a.get('name','')
                    aff=a.get('affiliation','')

                    url=a.get('url','')
                    if url!='': name='<a href="'+url+'">'+name+'</a>'

                    if x!='': x+=', '
                    x+=name+'&nbsp;<sup>'+aff+'</sup>'

                h+=x+'<br>\n'
                h+='</span>\n'

             if len(affs)>0:
                h+='<div id="ck_entries_space4"></div>\n'
                h+='<span id="ck_article_affiliations">\n'

                x=''
                for a in sorted(affs, key=int):
                    af=affs[str(a)]
                    name=af.get('name','')

                    url=af.get('url','')
                    if url!='': name='<a href="'+url+'">'+name+'</a>'

                    if x!='': x+=',&nbsp;&nbsp;&nbsp;'
                    x+='<sup>'+str(a)+'</sup>&nbsp;'+name

                h+=x+'<br>\n'
                h+='</span>\n'

          if dd.get('add_date_to_the_top','')!='':
             h+='<span id="ck_article_affiliations">\n'
             h+='<div id="ck_entries_space4"></div>\n'
             h+='<i>\n'
             h+=dd['add_date_to_the_top']
             h+='</i>\n'
             h+='</span><br>\n'

          h+='</center>\n'

          if len(cauthor)>0:
             h+='<div id="ck_entries_space4"></div>\n'
             h+='<span id="ck_article_cauthor">\n'
             h+='<i>Corresponding author: <a href="mailto:'+cauthor+'">'+cauthor+'</a></i>\n'
             h+='</span>\n'

          if hshare!='' and dd.get('skip_sharing','')!='yes':
             h+='<div id="ck_entries_space4"></div>\n'
             h+=hshare
             h+=' <div id="ck_entries_space4"></div>\n'

          h+='<div style="text-align: right;">'

          x=''
          for q in dd.get('top_links',[]):
              qt=q['text']
              qu=q['url']

              if x!='': x+='&nbsp; '
              x+='[&nbsp;<a href="'+qu+'">'+qt+'</a>&nbsp;]\n'

          if x!='':
             h+='\n<br>\n'+x+'\n'

          top_urls=dd.get('top_urls',[])

          top_url=dd.get('top_url',{})
          if len(top_url)!=0:
             top_urls.append(top_url)

          for top_url in top_urls:
              n_top_url=top_url.get('name','')
              u_top_url=top_url.get('url','')
              if n_top_url!='' and u_top_url!='':
                 h+='[&nbsp;<a href="'+u_top_url+'">'+n_top_url+'</a>&nbsp;] '

          if wurl!='' and dd.get('skip_discussion_link','')!='yes':
             h+='[&nbsp;<a href="'+wurl+'">Discussion wiki (comments, reproducibility, etc.)</a>&nbsp;]'
          h+='</div>\n'

          h+='<div id="ck_entries_space4"></div>\n'
          h+='<div id="ck_entries_space4"></div>\n'

          # Checking template
          t=dd.get('template','')
          if t!='':
             h+='<span id="ck_article_text">\n'

             px=os.path.join(pp,t)
             th=''
             if os.path.isfile(px):
                rx=ck.load_text_file({'text_file':px})
                if rx['return']>0: return rx
                th=rx['string']

             # If MediaWiki, process extra
             if mwc=='yes':
                thx=th.split('\n')
                th=''

                for l in thx:
                    if l.startswith('=== '):
                       l='<h3>'+l[4:-4]+'</h3>'
                    elif l.startswith('== '):
                       l='<h2>'+l[3:-3]+'</h2>'
                    elif l.startswith('= '):
                       l='<h1>'+l[2:-2]+'</h1>'

                    j=l.find('[')
                    while j>=0:
                       j1=l.find(']',j)
                       if j1>0:
                          url=l[j+1:j1]
                          txt=url
                          j2=url.find(' ')
                          if j2>0:
                             txt=url[j2+1:].strip()
                             url=url[:j2].strip()

                          l=l[:j]+'<a href="'+url+'">'+txt+'</a>'+l[j1+1:]
                          
                       j=l.find('[',j+1)

                    if l=='': l='<p>'

                    th+=l
#                    if not l.endswith('>'):
#                       th+='<br>'
                    th+='\n'

             # Check CK access functions
             h+=th

             j=0
             while j!=-1:
                j=h.find('$#ck_access_start#$',j)
                if j>=0:
                   j1=h.find('$#ck_access_stop#$',j)
                   if j1>=0:
                       json=h[j+19:j1].strip()

                       ha=''

                       # Convert json to python dict
                       rx=ck.convert_json_str_to_dict({'str':json, 'skip_quote_replacement':'yes'})
                       if rx['return']==0:
                          nii=rx['dict']

                          if nii.get('action','')!='':
                             # Here we process active CK plugin (if there is an "action") to generate content (even possibly from remote repo)
                             nii['base_url']=burl

                             rx=ck.access(nii)
                             if rx['return']==0:
                                 ha=rx.get('html','')

                                 if nii.get('remove_script_src','')=='yes':
                                    k1=ha.find('<script src')
                                    if k1>=0:
                                       k2=ha.find('</script>', k1)
                                       if k2>0:
                                          ha=ha[:k1]+ha[k2+9:]

                                 st+=rx.get('style','')
                             else:
                                 ha+='\n<br>\nInternal error: '+rx['error']+'\n<br>\n'

                       h=h[:j]+ha+h[j1+18:]
                       
                   j+=1

             h+='</span\n'
          h+='</div>\n'

          # Checking global style
          xt=dd.get('style','')
          if t!='':
             px=os.path.join(pp,xt)
             if os.path.isfile(px):
                rx=ck.load_text_file({'text_file':px})
                if rx['return']>0: return rx
                st+=rx['string']
          st=st.replace('$#ck_root_url#$', burl)

          if dar=='yes':
             h+='<center>\n'
             checked=''
             if ar=='on': checked=' checked '
             h+='&nbsp;&nbsp;&nbsp;Auto-replot graph:&nbsp;<input type="checkbox" name="'+var_post_autorefresh+'" id="'+var_post_autorefresh+'" onchange="submit()"'+checked+'>,'
             h+='&nbsp;seconds: <input type="text" name="'+var_post_autorefresh_time+'" value="'+str(iart)+'">\n'
             h+='</center>\n'

          if dd.get('add_ck_info','')!='':
             h+='<br>\n'
             h+=' <center><i>\n'
             h+='  This interactive and reproducible article was automatically generated using <b><a href="http://github.com/ctuning/ck">Collective Knowledge framework</a></b>'
             h+=' </i></center><br>\n'

    return {'return':0, 'raw':raw, 'show_top':top, 'html':h, 'style':st}

##############################################################################
# copy file from an entry to current directory

def copy_file(i):
    """
    Input:  {
              (module_uoa) - module with file
              data_uoa     - entry with file
              file         - file to copy
              dir          - extra dir in current directory
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os
    import filecmp
    import shutil

    muoa=i['module_uoa']
    duoa=i['data_uoa']
    f=i['file']

    r=ck.access({'action':'find',
                 'module_uoa':muoa,
                 'data_uoa':duoa})
    if r['return']>0: return r

    p=r['path']

    pp=os.path.join(p,f)

    if not os.path.isfile(pp):
       return {'return':1, 'error':'file not found ('+pp+')'}

    ppn=os.getcwd()
    if i.get('dir','')!='':
       ppn=os.path.join(ppn,i['dir'])

    ppd=ppn

    ppn=os.path.join(ppn,f)

    if not os.path.isfile(ppn) or not filecmp.cmp(pp,ppn):
       if not os.path.isdir(ppd):
          os.makedirs(ppd)
    
       ck.out('Copying file '+f+' to '+ppn+' ...')
       shutil.copyfile(pp,ppn)

    return {'return':0}
