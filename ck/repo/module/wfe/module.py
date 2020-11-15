#
# Collective Knowledge (CK web front-end)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: cTuning foundation
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel) 

# Local settings

import os

fdata_name='ck_top_data'
fmodule_name='ck_top_module'
frepo_name='ck_top_repo'

form_name='ck_top_form'
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
# index

def index(i):
    """

    Input:  {
              (template)             - use different template uoa
              (cid)                  - direct CID
              (search)               - search string
              (search_by_tags)       - search by tags (separated by comma or | for OR operator)

              (native_action)        - if !='', use this instead of action and just show output 
                                       (with menu but without query)

              (aview)                - if 'yes', alternative view (module+data UOA) in title instead of data_name (since not all may have it and there is currently no standard)
              (skip_links)           - if 'yes', do not show links (view meta, etc)
              (skip_desc)            - if 'yes', do not show desc
              (ignore_without_alias) - if 'yes', skip entries without alias (i.e. ignoring ENV when showing CK AI market entries)

              (limit)                - limit number of CK entries to show
              (force_limit)          - force limit number of CK entries to show
              (no_limit)             - show all entries
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              html         - unicoded html page
            }

    """

    nat=i.get('native_action','')
    nmuoa=i.get('native_module_uoa','')

    native=False
    if nat!='' and nmuoa!='': 
       native=True

    page=i.get('page','')
    if page!='':
       return view_page(i)

    fsearch_name='ck_top_search'
    fsearch_tag_name='ck_top_search_tag'

    fdate_after_name='ck_top_date_after'
    fdate_before_name='ck_top_date_before'

    fsubmit_name='ck_top_prune'
    fadd_name='ck_top_add'

    xskip_links=i.get('skip_links','')
    xskip_desc=i.get('skip_desc','')

    aview=(i.get('aview','')=='yes')

    flimit_name='ck_limit'
    fmore_button_name='ck_top_more'

    fview_raw='view_raw'

    # Check filters
    cid=i.get('wcid','')

    # That was not a good thing but I was using _ in some refs 
    if cid.find('_')>0 and cid.find(':')<0:
       cid=cid.replace('_',':')

    # Remove HTML characters to avoid hacking
    cid=cid.replace('<','').replace('%22','').replace('%3E','').replace('%3C','')

    cduoa=''
    cmuoa=''
    cruoa=''

    clruoa=[]
    x=i.get('repo_list','').strip()
    if x!='': clruoa=x.split(',')

    cs=i.get('search', '').strip()
    if fsearch_name in i: cs=i[fsearch_name]

    cst=i.get('search_by_tags','')
    if fsearch_tag_name in i: cst=i[fsearch_tag_name]

    find_cid=False
    if cs!='' and cs.lower().startswith('cid='):
       find_cid=True
       cid=cs[4:].strip()

    if cid!='':
       r=ck.parse_cid({'cid':cid})
       if r['return']>0: return r
       cduoa=r['data_uoa']
       cmuoa=r['module_uoa']
       cruoa=r.get('repo_uoa','')

    if i.get('wrepo_uoa','')!='':
       cruoa=i['wrepo_uoa']

    if not find_cid and fdata_name in i: cduoa=i[fdata_name]
    if not find_cid and fmodule_name in i: cmuoa=i[fmodule_name]
    if not find_cid and frepo_name in i: cruoa=i[frepo_name]

    cid=''
    cidx=''
    if cruoa!='' or cmuoa!='' or cduoa!='':
       if cduoa!='': cid=cduoa
       cid=':'+cid
       if cmuoa!='': cid=cmuoa+cid
       cid=':'+cid
       cidx=cid
       if cruoa!='': cid=cruoa+cid

    # Check host/port and default module/action.
    rx=form_url_prefix(i)
    if rx['return']>0: return rx
    url0=rx['url']
    url0w=rx['url_without_template']
    template=rx['template']
    d=rx['meta']
    p=rx['path']
    h=rx['html']
    url_template_pull=rx['url_template_pull']

    url00=url0w
    # wfe_url_prefix_subst is used to make "good" looking URL for referencing
    # when CK server is behind some redirecting services such as no-ip. 
    if ck.cfg.get('wfe_url_prefix_subst','')!='': url00=ck.cfg['wfe_url_prefix_subst']

    url=url0
    action=i.get('action','').replace('<','').replace('%22','').replace('%3E','').replace('%3C','')
    muoa=i.get('module_uoa','').replace('<','').replace('%22','').replace('%3E','').replace('%3C','')

    hstyle=''

    top_menu=cfg['top_menu']
    if len(d.get('top_menu',{})): 
       top_menu=d['top_menu']

    # Prepare URL
    url+='action='+action+'&'+'module_uoa='+muoa
    url1=url

    url_add=url0+'action=webadd&module_uoa='+muoa
    if cid!='': url_add+='&wcid='+cid

    # PRUNE *************************************************************
    view_entry=False
    lst=[]

    no_limit=i.get('no_limit','').replace('<','').replace('%22','').replace('%3E','').replace('%3C','')
    if no_limit=='yes':
       ln='-1'
    else:
       # Check limits
       if i.get('force_limit','')!='':
          ln=i['force_limit']
       else:
          ln=i.get(flimit_name,'')

    lnstep=15
    if ln=='': 
       ln=i.get('limit','').replace('<','').replace('%22','').replace('%3E','').replace('%3C','')
    if ln=='':
       ln=str(lnstep)
    if ln=='':
       ln=str(lnstep)

    if fmore_button_name in i: ln=str(int(ln)+lnstep)

    vr=i.get(fview_raw,'')

    if i.get('nolimit','')=='yes':
       ln=''

    if ln!='': url+='&limit='+ln

    # Check dates
    datea=i.get('search_by_date_after','')
    dateb=i.get('search_by_date_before','')
    if fdate_after_name in i: datea=i[fdate_after_name]
    if fdate_before_name in i: dateb=i[fdate_before_name]

    datea=datea.replace(' ','T') # To make ISO standard
    dateb=dateb.replace(' ','T') # To make ISO standard

    # If viewing a given entry
#    if cmuoa!='' and cduoa!='' and \
#       cmuoa.find('*')<0 and cmuoa.find('?')<0 and \
#       cduoa.find('*')<0 and cduoa.find('?')<0:
#       view_entry=True

    if not native:
       # Check if has | in string, then multiple searches
       qcst=cst.split('|')
       lst=[]

       for q in qcst:
          # Create pruned list 
          ii={'action':'search',
              'repo_uoa':cruoa,
              'module_uoa':cmuoa,
              'data_uoa':cduoa,
              'add_info':'yes',
              'add_meta':'yes',
              'ignore_case':'yes'}
          if ln!='' and int(ln)>0:
             ii['limit_size']=int(ln)
          if cs!='' and not find_cid:
             ii['search_string']=cs
          if cst!='' and not find_cid:
             ii['tags']=q
          if len(clruoa)>0:
             ii['repo_uoa_list']=clruoa

          if datea!='' or dateb!='':
             if datea==dateb:
                ii['add_if_date']=datea
             else:
                if datea!='':
                   ii['add_if_date_after']=datea
                if dateb!='':
                   ii['add_if_date_before']=dateb

          r=ck.access(ii)
          if r['return']>0: # On some machines, some modules are not available - so do not process error to avoid crashing ...
             r['lst']=[]

          lst+=r['lst']

       if len(lst)==1:
          view_entry=True

    # Top html ************************************************************
    ht=''

    ht+='<center><div id="ck_menu_0">\n'

    xcmuoa=cmuoa
    if view_entry and len(lst)==1:
       xcmuoa=lst[0]['module_uoa']

    skip_div_box=''
    for q in top_menu:
        name=q['name']
        x=q.get('url','')
        y=q.get('url_extra','')
        z=q.get('url_extra_browse','')
        muoas=q.get('module_uoas',[])
        xmuoa=q.get('module_uoa','')

        style='ck_menu_text_0'
        qnmuoa=q.get('native_module_uoa','')
        if (q.get('default','')!='yes' or (i.get('wcid','')=='' and cmuoa=='')) and \
           ((native and i.get('native_module_uoa','')==q.get('native_module_uoa','-')) or \
            (not native and (q.get('any_module','')=='yes' or (xcmuoa in muoas)))):
           style='ck_menu_text_0_selected'
           if qnmuoa!='' :
              if nmuoa=='':
                 nmuoa=qnmuoa
              if nat=='' and q.get('native_action','')!='':
                 nat=q['native_action']
              skip_div_box=q.get('skip_div_box','')
              native=True

        if x=='' and y=='':
           x=url0+'wcid='+xmuoa+':'
           if z!='':
              x+='&'+z
        elif y!='':
           x=url0+y

        xtb=''
        if q.get('new_window','')=='yes':
           xtb=' target="_blank"'

        line='<span id="'+style+'"><a href="'+x+'"'+xtb+'>'+name+'</a></span>'

        if q.get('bold','')=='yes':
           line='<b>'+line+'</b>'

        ht+=line+'\n'
    ht+='</div></center>\n'

    # Check if show after menu text, such as number of shared artifacts
    if d.get('extra_html_after_menu','')!='':
       ht+=d['extra_html_after_menu'].replace('$#ck_root_url#$', url0)

    ad=ck.cfg.get('extra_browser_text','')
    if ad!='':
       ht+=ad

    show_more=False

    # Check if html only **************************************************************
    if i.get('html_only','')=='yes':
       q=lst[0]

       ruoa=q['repo_uoa']
       muoa=q['module_uoa']

       muid=q['module_uid']
       ruid=q['repo_uid']

       duoa=q['data_uoa']
       duid=q['data_uid']

       xcid=muid+':'+duid

       utp=url0+'action=pull&common_func=yes&cid='+xcid+'&filename='

       utp_data_uoa='wfe'

       x='tmp:'+utp_data_uoa
       if ck.cfg.get('graph_tmp_repo_uoa','')!='':
          x=ck.cfg['graph_tmp_repo_uoa']+':'+x

       utp_tmp=url0+'action=pull&common_func=yes&cid='+x+'&filename='

       hp=''

       ii={'action':'html_viewer',
           'module_uoa':muid,
           'data_uoa':duid,
           'url_base':url0,
           'url_cid':x,
           'url_pull':utp,
           'url_pull_tmp':utp_tmp,
           'tmp_data_uoa':utp_data_uoa,
           'form_name':form_name,
           'all_params':i}
       rx=ck.access(ii)
       if rx['return']==0:
          hspec=rx.get('html','')
          hstyle+=rx.get('style','')+'\n'

          # Process special vars
          rx=process_ck_page({'html':hspec})
          if rx['return']>0: return rx
          hspec=rx['html']
          if rx.get('style','')!='':
             hstyle+='\n\n'+rx['style']+'\n\n'

          # Replace Root URL
          hspec=hspec.replace('$#ck_root_url#$', url0)
       else:
          x=rx['error']
          if 'not found in module' not in x:
             hspec='<b>CK warning</b>: '+rx['error']

       h='<html>\n'
       h+='<style>\n'
       h+=hstyle+'\n'
       h+='</style>\n'
       h+='<body>\n'
       h+=hspec+'\n'
       h+='</body>\n'
       h+='</html>\n'

       hp=''

    # Check if native action **************************************************************
    elif native:
       hp=''

       if skip_div_box!='yes':
          hp+='<div id="ck_box_with_shadow">\n'

       import copy
       ii=copy.deepcopy(i)
       ii['action']=nat
       if 'native_action' in i: del(i['native_action'])
       ii['module_uoa']=nmuoa
       if 'native_module_uoa' in i: del(i['native_module_uoa'])

       rx=ck.access(ii)
       if rx['return']>0:
          hp+='<b>Error:</b> '+rx['error']
       else:
          hp+=rx.get('html','')+'\n'
          hstyle+=rx.get('style','')+'\n'

       if skip_div_box!='yes':
          hp+='</div>\n'

    else:
       # Prepare query div ***************************************************************
       # Start form + URL (even when viewing entry)
       ii={'url':url1, 'name':form_name}
       r=start_form(ii)
       if r['return']>0: return r
       hf=r['html']

       # Some params
       for k in ['no_limit','aview','skip_links','skip_desc']:
           rx=create_input({'type':'hidden', 'name': k, 'value':i.get(k,'')})
           if rx['return']>0: return rx
           hf+=rx['html']+'\n'

       if view_entry:
          ht+='<script>\n'
          ht+=' function goBack() {window.history.back()}\n'
          ht+='</script>\n'
          ht+='\n'
   #       ht+='<div id="ck_go_back">\n'
   #       ht+=' <button onclick="goBack()">Go Back</button>\n'
   #       ht+='</div>\n'

       else:
          ht+=' <hr class="ck_hr">\n'

          # Get list of repos
          r=ck.access({'action':'list',
                       'module_uoa':ck.cfg["repo_name"],
                       'add_info':'yes',
                       'add_meta':'yes'})
          if r['return']>0: return r
          lm=r['lst']

          r=convert_ck_list_to_select_data({'lst':lm, 'add_empty':'yes', 'sort':'yes', 'value_uoa':cruoa, 'ignore_remote':'yes'})
          if r['return']>0: return r
          dlm=r['data']
          if r.get('value_uid','')!='': cruoa=r['value_uid']

          ii={'data':dlm, 'name':frepo_name, 'onchange':onchange, 'style':'width:300px;'}
          if cruoa!='': ii['selected_value']=cruoa
          r=create_selector(ii)
          if r['return']>0: return r
          hlr=r['html']

          # Get list of modules
          r=ck.access({'action':'list',
                       'module_uoa':ck.cfg["module_name"],
                       'add_info':'yes'})
          if r['return']>0: return r
          lm=r['lst']

          r=convert_ck_list_to_select_data({'lst':lm, 'add_empty':'yes', 'sort':'yes', 'value_uoa':cmuoa})
          if r['return']>0: return r
          dlm=r['data']
          if r.get('value_uid','')!='': cmuoa=r['value_uid']

          ii={'data':dlm, 'name':fmodule_name, 'onchange':onchange, 'style':'width:300px;'}
          if cmuoa!='': ii['selected_value']=cmuoa
          r=create_selector(ii)
          if r['return']>0: return r
          hlm=r['html']

          # Prepare general search
          r=create_input({'size':'25', 'name': fsearch_name, 'value':cs})
          if r['return']>0: return r
          hs1=r['html']

          # Prepare search by tags
          r=create_input({'size':'25', 'name': fsearch_tag_name, 'value':cst})
          if r['return']>0: return r
          hs2=r['html']

          # Prepare date after
          r=create_input({'size':'25', 'name': fdate_after_name, 'value':datea})
          if r['return']>0: return r
          hda=r['html']

          # Prepare date after
          r=create_input({'size':'25', 'name': fdate_before_name, 'value':dateb})
          if r['return']>0: return r
          hdb=r['html']

          # Prepare reset
          hreset='<a href="'+url1+'">[Reset form]</a>'

          # Prepare submit
          r=create_button({'name': fsubmit_name, 'value':'Search / Prune'})
          if r['return']>0: return r
          hsubmit=r['html']

          # Prepare add
          hadd='<a href="'+url_add+'">[Add new entry]</a>'

          # Prepare top
          ht+=hf
          ht+='<div id="ck_prune">\n'
          ht+='<small><b>Prune entries by:</b></small><br>\n'

          ht+='<center>\n'
          ht+='<table border="0" cellpadding="5">\n'
          ht+=' <tr>\n'
          ht+='  <td align="right">Module/class:</td>\n'
          ht+='  <td>'+hlm+'</td>\n'
          ht+='  <td align="right">String:</td>\n'
          ht+='  <td>'+hs1+'</td>\n'
          ht+='  <td align="right">After date (ISO):</td>\n'
          ht+='  <td>'+hda+'</td>\n'
          ht+=' </tr>\n'
          ht+=' <tr>\n'
          ht+='  <td align="right">Repository:</td>\n'
          ht+='  <td>'+hlr+'</td>\n'
          ht+='  <td align="right">Tags:</td>\n'
          ht+='  <td>'+hs2+'</td>\n'
          ht+='  <td align="right">Before date (ISO):</td>\n'
          ht+='  <td>'+hdb+'</td>\n'
          ht+=' </tr>\n'
          ht+='</table>\n'
          ht+='</center>\n'
          ht+=hreset+'&nbsp;&nbsp;'+hsubmit+'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'+hadd+'\n'

          if ck.cfg.get('use_indexing','')=='no':
             ht+='<br><br><b><i><small>Warning: Elastic Search indexing is off - search by string/tags/date can be slow ...</small></i></b><br>'

          ht+='</div>\n'

       # Continue showing entries
       if len(lst)==0:
          ########################################### No entries #############
          hp='<div id="ck_entries">\n'
          hp+='No entries found!'
          hp+='</div>\n'


       elif len(lst)==1:
          ########################################### Entry viewer #############
          import json

          q=lst[0]

          ruoa=q['repo_uoa']
          muoa=q['module_uoa']

          muid=q['module_uid']
          ruid=q['repo_uid']

          duoa=q['data_uoa']
          duid=q['data_uid']

          hp=hf # init html + form

          # Preset current entry params
          rx=create_input({'type':'hidden', 'name': frepo_name, 'value':ruid})
          if rx['return']>0: return rx
          hp+=rx['html']+'\n'

          rx=create_input({'type':'hidden', 'name': fmodule_name, 'value':muid})
          if rx['return']>0: return rx
          hp+=rx['html']+'\n'

          rx=create_input({'type':'hidden', 'name': fdata_name, 'value':duid})
          if rx['return']>0: return rx
          hp+=rx['html']+'\n'

   #       hp='<div id="ck_prune">\n'
   #       hp+='<b>View entry:</b><br>\n'
   #       hp+='<small>[ <a href="'+url0+'">Back to CK browser</a> ]</small>\n'
   #       hp+='</div>\n'
   #       hp+='\n'

          # Load for full info
          rx=ck.access({'action':'load', 'repo_uoa':ruid, 'module_uoa':muid, 'data_uoa':duid})
          if rx['return']>0: return rx
          dd=rx['dict']
          dx=rx.get('desc',{})
          pp=rx['path']

          skip_links=dd.get('skip_links','')

          info=q.get('info',{})
          control=info.get('control',{})

          author=control.get('author','')
          author_wp=control.get('author_webpage','')
          iso_datetime=control.get('iso_datetime','')
          license=control.get('license','')

          tags=dd.get('tags', [])
          stags=''
          if type(tags)!=list: stags=tags
          elif len(tags)>0:
             stags=''
             for q in tags:
                 if stags!='': stags+=','
                 stags+=str(q)

          desc=info.get('description','')

          au=''
          if author!='': au=author
          if author_wp!='': au='<a href="'+author_wp+'" target="_blank">'+au+'</a>'

          if iso_datetime!='':
             iso_datetime=iso_datetime.replace('T',' ')
#             ix=iso_datetime.find('.')
#             if ix>0: iso_datetime=iso_datetime[:ix]

          dn=info.get('data_name','')
          if dn=='': dn=duoa

          xcid=muid+':'+duid
          url2=url1+'&wcid='+xcid
          url3=url0+'&action=pull&common_func=yes&archive=yes&skip_tmp=yes&all=yes&cid='+xcid
          url3x=url0+'&action=pull&common_func=yes&archive=yes&skip_tmp=yes&cid='+xcid
          url4=url0+'&action=load&out=json&cid='+xcid
          url7=url0+'&action=webadd&update=yes&module_uoa=wfe&wcid='+xcid

          url5=ck.cfg.get('wiki_data_web','')
          if url5!='':
             url5+=muid+'_'+duid

          urlself1=url00+'wcid='+xcid
   #       urlself=url0+'action=index%26module_uoa=wfe%26wcid='+xcid
          urlself=url00+'wcid='+xcid


          url6=url0+'action=generate&module_uoa=qr-code&qr_level=6&image_size=170&string='+urlself

          hp+='<div id="ck_entries">\n'

          # Check if share
          ps=os.path.join(p, 'share.html')
          hshare=''
          ishare=False
          if os.path.isfile(ps):
             r=ck.load_text_file({'text_file':ps})
             if r['return']>0: return r
             hshare=r['string'].replace('$#url#$',url2)

          # Check if specialized rendering function exists for the given module
          raw=True
          show_top=True
          hspec=''
          utp=url0+'action=pull&common_func=yes&cid='+xcid+'&filename='

          utp_data_uoa='wfe'

          x='tmp:'+utp_data_uoa
          if ck.cfg.get('graph_tmp_repo_uoa','')!='':
             x=ck.cfg['graph_tmp_repo_uoa']+':'+x

          utp_tmp=url0+'action=pull&common_func=yes&cid='+x+'&filename='

          ii={'action':'html_viewer',
              'module_uoa':muid,
              'data_uoa':duid,
              'url_base':url0,
              'url_cid':x,
              'url_pull':utp,
              'url_pull_tmp':utp_tmp,
              'url_wiki':url5,
              'html_share':hshare,
              'tmp_data_uoa':utp_data_uoa,
              'form_name':form_name,
              'all_params':i}
   #       for q in i:
   #           if q.startswith('cur_form'):
   #              ii[q]=i[q]

          rx=ck.access(ii)
          if rx['return']==0:
             if rx.get('raw','')!='yes': raw=False
             if rx.get('show_top','')!='yes': show_top=False
             if vr=='on': 
                raw=True
                show_top=True
             hspec=rx.get('html','')
             hstyle=rx.get('style','')

             # Process special vars
             rx=process_ck_page({'html':hspec})
             if rx['return']>0: return rx
             hspec=rx['html']
             if rx.get('style','')!='':
                hstyle+='\n\n'+rx['style']+'\n\n'

             # Replace Root URL
             hspec=hspec.replace('$#ck_root_url#$', url0)
          else:
             x=rx['error']
             if 'not found in module' not in x:
                hspec='<b>CK warning</b>: '+rx['error']

          # Show top info
          if show_top:
             hp+=' <table border="0">\n'

             hp+='  <tr colspan="2">\n'
             hp+='   <td valign="top">\n'
             hp+='    <img src="'+url6+'">\n'

             # Check if share
             if hshare!='':
                ishare=True
                hp+=hshare+'\n'

             hp+='   </td>\n'
             hp+='   <td valign="top">\n'

             hp+='<span id="ck_entries1a">'+dn+'</span><br>\n'
             hp+=' <hr class="ck_hr">\n'

             hp+='<div id="ck_entries_space4"></div>\n'
             if au!='':
                hp+='<span id="ck_entries2"><b>Added by:</b> <i>'+au+'</i></span><br>\n'
             hp+='<span id="ck_entries2"><b>Date:</b> <i>'+iso_datetime+'</i></span><br>\n'
             hp+='<span id="ck_entries2"><b>License:</b> <i>'+license+'</i></span><br>\n'

             hp+='<div id="ck_entries_space4"></div>\n'

             hp+='<span id="ck_entries2"><b>Module:</b> <i>'+muoa+'</i></span><br>\n'
             hp+='<span id="ck_entries2"><b>Repo:</b> <i>'+ruoa+'</i></span><br>\n'

             hp+='<div id="ck_entries_space4"></div>\n'
             hp+='<span id="ck_entries2"><b>CID (DOI-like distributed ID):</b> <i><a href="'+urlself1+'">'+xcid+'</a></i></span><br>\n'

             if desc!='':
                hp+='<div id="ck_entries_space8"></div>\n'
                hp+='<span id="ck_entries3">'+desc+'</span><br>\n'


             hp+='<div id="ck_entries_space4"></div>\n'

             hp+='   </td>\n'
             hp+='  </tr>\n'

             hp+=' </table>\n'

             # Show tags
             if stags!='':
                hp+='<center><b>Tags:</b> <i>'+stags+'</i></center>\n'

             if skip_links!='yes':
                 hp+='<div id="ck_downloads">\n'
                 if url5!='': hp+='<a href="'+url5+'" target="_blank">[Discuss (wiki)]</a>&nbsp;\n'
                 hp+='<a href="'+url7+'" target="_blank">[Update]</a>&nbsp;\n'
                 hp+='<a href="'+url3+'">[Download entry as archive]</a>\n'
                 hp+='</div>\n'

          # Check if has specialized html
          if hspec!='' and vr!='on':
             hp+='<div id="ck_entries2">\n'
             hp+=' '+hspec+'\n'
             hp+='</div>\n'

          if raw:
             # Check files
             rx=ck.list_all_files({'path':pp, 'limit':10000})
             if rx['return']==0:
                files=rx['list']
                ll=sorted(files)

                if len(ll)>0:
                   hp+='<hr class="ck_hr">\n'
                   hp+='<span id="ck_text51"><b>Files:</b></span>\n'
                   hp+='<div id="ck_entries_space4"></div>\n'

                   hp+='<div id="ck_text55">\n'
                   for q in ll:
                       if not q.startswith('tmp'):
                          v=files[q]
                          hp+='<a href="'+utp+q+'">'+q+'</a>&nbsp;&nbsp;&nbsp;&nbsp;('+str(int((v.get('size',0)+999)/1000))+'KB)<br>\n'
                   hp+='</div>\n'

                   hp+='<div id="ck_downloads">\n'

                   if i.get('archive_all','')=='yes':
                      x=url3
                   else:
                      x=url3x

                   hp+='<a href="'+url3x+'">[Download archive]</a>\n'
                   hp+='</div>\n'

             ##################################################################################################
             # Show dependencies
             hp+=' <hr class="ck_hr">\n'

             hp+=' <span id="ck_text51"><b>Cross-linking (dependencies):</b></span>\n'
             hp+='<div id="ck_entries_space4"></div>\n'

             hp+='<div id="ck_text55">\n'
             hp+='</div>\n'

             # Show meta
             hp+=' <hr class="ck_hr">\n'

             hp+=' <span id="ck_text51"><b>Meta:</b></span>\n'
             hp+='<div id="ck_entries_space4"></div>\n'

             hp+='<div id="ck_text55">\n'
             hp+='<pre>\n'
             rx=ck.dumps_json({'dict':dd, 'sort_keys':'yes'})
             if rx['return']>0: return rx

             mt=rx['string']

             # Try to detect links
             i0=0
             while i0<len(mt):
                i1=mt.find('"',i0)
                if i1<0: break

                i2=mt.find('"',i1+1)
                if i2<0: break

                x=mt[i1+1:i2]
                if len(x)==16 and ck.is_uid(x):
                   y='<a href="'+url0+'wcid=:'+x+'">'+x+'</a>'
                   mt=mt[:i1+1]+y+mt[i2:]
                   i0=i1+len(y)
                elif x.startswith('http://') or x.startswith('https://'):
                   y='<a href="'+x+'">'+x+'</a>'
                   mt=mt[:i1+1]+y+mt[i2:]
                   i0=i1+len(y)
                elif x.startswith('cm:'):
                   # For compatibility with cM
                   x1=x[3:].split(':')
                   y='<a href="'+url0+'wcid='+x1[0]+':'+x1[1]+'">'+x+'</a>'
                   mt=mt[:i1+1]+y+mt[i2:]
                   i0=i1+len(y)

                else:   
                   i0=i1+1

             # Next is for compatibility with cM
             i0=0
             while True:
                i1=mt.find('$#cm_',i0)
                if i1<0: break

                i2=mt.find('#$',i1+1)
                if i2<0: break

                x=mt[i1:i2+2]
                x1=x[5:-2].split('_')
                if len(x1)>1:
                   y='<a href="'+url0+'wcid='+x1[0]+':'+x1[1]+'">'+x+'</a>'
                else:
                   y=x
                mt=mt[:i1]+y+mt[i2+2:]
                i0=i1+len(y)

             hp+=mt

             hp+='</pre>\n'
             hp+='</div>\n'

             ##################################################################################################
             # Show meta
             hp+=' <hr class="ck_hr">\n'

             hp+=' <span id="ck_text51"><b>API desc:</b></span>\n'
             hp+='<div id="ck_entries_space4"></div>\n'

             hp+='<div id="ck_text55">\n'
             hp+='<pre>\n'
             rx=ck.dumps_json({'dict':dx, 'sort_keys':'yes'})
             if rx['return']>0: return rx

             hp+=rx['string']

             hp+='</pre>\n'
             hp+='</div>\n'

             ##################################################################################################
             hp+='<div id="ck_downloads">\n'
             hp+='<a href="'+url4+'" target="_blank">[Download meta]</a>&nbsp;\n'
             hp+='</div>\n'

             # Check if report
             ps=os.path.join(p, 'report.html')
             if os.path.isfile(ps):
                r=ck.load_text_file({'text_file':ps})
                if r['return']>0: return r
                hp+=' <hr class="ck_hr">\n'
                htx=r['string'].replace('$#cid#$',xcid)
                hp+=htx+'\n'


          # Raw selector
          if hspec!='':
             checked=''
             if vr=='on': checked=' checked '
             hp+='<center><input type="checkbox" name="'+fview_raw+'" id="'+fview_raw+'" onchange="submit()"'+checked+'>View entry in raw format</center>\n'

          hp+='</div>\n'
          hp+='</form>\n'

       else:
          ######################################## View multiple entries ###############
          show_more=True
          if aview:
             lst1=sorted(lst, key=lambda k: (k['module_uoa']+':'+k['data_uoa']).lower())
          else:
             lst1=sorted(lst, key=lambda k: k.get('info',{}).get('data_name','').lower())

          hp=''
          iq=0
          for q in lst1:
              iq+=1
              siq=str(iq)

              ruoa=q['repo_uoa']
              muoa=q['module_uoa']

              muid=q['module_uid']
              ruid=q['repo_uid']

              duoa=q['data_uoa']
              duid=q['data_uid']

              meta=q.get('meta',{})
              info=q.get('info',{})
              control=info.get('control',{})

              author=control.get('author','')
              author_wp=control.get('author_webpage','')
              iso_datetime=control.get('iso_datetime','')

              tags=meta.get('tags', [])
              stags=''
              if type(tags)!=list: stags=tags
              elif len(tags)>0:
                 stags=''
                 for q in tags:
                     if stags!='': stags+=','
                     stags+=str(q)

              desc=info.get('description','')

              au=''

              if author!='': 
                 au=author
                 if author_wp!='': au='<a href="'+author_wp+'" target="_blank">'+au+'</a>'
                 au='Added by '+au

              if iso_datetime!='':
                 if au!='': au+=', '
                 x=iso_datetime.replace('T',' ')
                 ix=x.find('.')
                 if ix>0: x=x[:ix]
                 au+=x

              if au!='': au+=', '
              au+='Repo: '+ruoa

              if stags!='':
                 if au!='': au+=', '
                 au+='<b>Tags:</b> '+stags

              if aview:
                 dn=muoa+':'+duoa
              else:
                 dn=info.get('data_name','')
                 if dn=='': dn=duoa

              if i.get('ignore_without_alias','')=='yes' and ck.is_uid(duoa):
                 iq-=1
                 continue

#              xcid=muid+':'+duid
              xcid=ruid+':'+muid+':'+duid
              url2=url0+'wcid='+xcid

              url3=url0+'&action=pull&common_func=yes&archive=yes&skip_tmp=yes&all=yes&cid='+xcid
              url3x=url0+'&action=pull&common_func=yes&archive=yes&skip_tmp=yes&cid='+xcid
              url4=url0+'&action=load&out=json&cid='+xcid
              url7=url0+'&action=webadd&update=yes&module_uoa=wfe&wcid='+xcid

              url5=ck.cfg.get('wiki_data_web','')
              if url5!='':
                 url5+=muid+'_'+duid

              hp+='<div id="ck_entries">\n'

              hp+='<small>'+str(iq)+') </small><span id="ck_entries1"><a href="'+url2+'">'+dn+' ('+muoa+')</a></span><br>\n'
              if au!='' and xskip_desc!='yes':
                 hp+='<div id="ck_entries_space4"></div>\n'
                 hp+='<span id="ck_entries2"><i>'+au+'</i></span><br>\n'

              if desc!='' and xskip_desc!='yes':
                 hp+='<div id="ck_entries_space8"></div>\n'
                 hp+='<span id="ck_entries3">'+desc+'</span><br>\n'

              if xskip_links!='yes':
                 hp+='<div id="ck_entries_space4"></div>\n'
                 hp+='<div id="ck_downloads">\n'
                 hp+='<a href="'+url4+'" target="_blank">[View meta]</a>&nbsp;\n'
                 if url5!='': hp+='<a href="'+url5+'" target="_blank">[Discuss (wiki)]</a>&nbsp;\n'
                 hp+='<a href="'+url7+'" target="_blank">[Update]</a>&nbsp;\n'
                 hp+='<a href="'+url3x+'">[Download entry]</a>\n'
                 hp+='</div>\n'

              hp+='</div>\n'

    # Replace styles
    if hstyle!='':
       hstyle='<style>\n'+hstyle+'\n</style>\n\n'
    h=h.replace('$#ck_styles#$',hstyle)

    # Replace top if needed
    h=h.replace('$#template_top#$',ht)

    # Prepare middle
    if view_entry:
       hp+='<div id="ck_go_back">\n'
       hp+=' <button onclick="goBack()">Go Back</button>\n'
       hp+='</div>\n'

    h=h.replace('$#template_middle#$',hp)

    hm=''
    if not native and not no_limit=='yes':
       # Show more
       r=create_input({'type':'hidden', 'name': flimit_name, 'value':ln})
       if r['return']>0: return r
       hm=r['html']+'\n'

       # Prepare submit
       if show_more:
          r=create_button({'name': fmore_button_name, 'value':'Show more entries'})
          if r['return']>0: return r
          hm+=r['html']+'<br>\n'

       hm+='</form>\n'

    h=h.replace('$#template_middle_finish#$', hm)

    # Check if visits
    px=os.path.join(p, 'visits.html')
    htx=''
    if os.path.isfile(px):
       r=ck.load_text_file({'text_file':px})
       if r['return']>0: return r
       htx=r['string']
    h=h.replace('$#template_end#$',htx)

    # Substitute specials
    h=h.replace('$#title#$', 'CK Browser')
    h=h.replace('$#ck_url_template_pull#$', url_template_pull)

    return {'return':0, 'html':h}

##############################################################################
# create HTML selector

def create_selector(i):
    """
    Input:  {
              (class)           - if !='', add this class
              (name)            - if !='', add this name
              (onchange)        - if !='', add this onchange function
              (style)           - if !='', use this style

              (data)            - [{'name':name, 'value': uid}, ...]
              (selected_value)  - if !='', select this item

              (skip_sort)       - if 'yes', do not sort
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              html         - returned generated HTML
            }

    """

    # Prepare header
    h='<select'

    cl=i.get('class','')
    if cl!='':
       h+=' class="'+cl+'"'

    nm=i.get('name','')
    if nm!='':
       h+=' name="'+nm+'"'

    oc=i.get('onchange','')
    if oc!='':
       h+=' onchange="'+oc+'"'

    hs=i.get('style','')
    if hs!='':
       h+=' style="'+hs+'"'

    h+='>\n'

    # Prepare 
    d=i['data']

    sv=i.get('selected_value','')

    if i.get('skip_sort','')!='yes':
       d=sorted(d, key=lambda k: k['name'])

    first=True
    for q in d:
        n=q['name']
        v=q['value']

        if first and sv=='' and v!='':
           sv=v

        h+='<option value="'+v+'"'
        if sv!='' and sv==v:
           h+=' SELECTED'
        x=n
        try:
           x=str(n)
        except:
           pass

        h+='>'+x+'</option>\n'

        if first:
           first=False

    # Finish
    h+='</select>\n'

    return {'return':0, 'html':h, 'selected_value':sv}

##############################################################################
# 

def convert_ck_list_to_select_data(i):
    """
    Input:  {
              lst             - CK list object
              (add_empty)     - if 'yes', add empty line
              (sort)          - if 'yes', sort by name
              (value_uoa)     - if !='', find uoa and return uid
              (ignore_remote) - if 'yes', ignore if meta has 'remote':'yes' 
                                   (to avoid remote repositories)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              data         - data list in selector format
              (value_uid)  - if value_uoa  is set, find UID of the entry
            }

    """

    dat=[]

    if i.get('add_empty','')=='yes':
       dat.append({'name':'', 'value':''})

    lst=i['lst']

    vuoa=i.get('value_uoa','')
    vuid=''

    ir=i.get('ignore_remote','')

    for q in lst:
        duoa=q['data_uoa']
        duid=q['data_uid']

        skip=False
        if ir=='yes':
           meta=q.get('meta',{})
           if meta.get('remote','')=='yes':
              skip=True

        if not skip:
           dn=q.get('info',{}).get('data_name','')
           if dn=='': dn=duoa

           if vuoa!='' and vuoa==duoa:
              vuid=duid

           dat.append({'name':dn, 'value':duid}) 

    if i.get('sort','')=='yes':
       dat=sorted(dat, key=lambda k: k['name'].lower())

    return {'return':0, 'data':dat, 'value_uid':vuid}

##############################################################################
# start form

def start_form(i):
    """
    Input:  {
              (url) - url
              (name) - name
              (method) - 'POST' by default
              (enctype) - 'multipart/form-data' by default
              (charset) - 'utf-8' by default
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              html         - html for the form
            }

    """

    h='<form action="'

    url=i.get('url','')
    if url!='':
       h+=url
    h+='"'

    name=i.get('name','')
    if name!='':
       h+=' name="'+name+'"'

    method=i.get('method','')
    if method=='': method='post'
    h+=' method="'+method+'"'

    enctype=i.get('enctype','')
    if enctype=='': enctype='multipart/form-data'
    h+=' enctype="'+enctype+'"'

    charset=i.get('charset','')
    if charset=='': charset='utf-8'
    h+=' accept-charset="'+charset+'"'

    h+='>\n'

    return {'return':0, 'html':h}

##############################################################################
# create search

def create_input(i):
    """
    Input:  {
              (type)       - if '', set 'text'
              (size)       - size, 50 by default
              (spellcheck) - if !='yes', skip 
              (name)       - name
              (value)      - default value
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              html         - html for the form
            }

    """

    tp=i.get('type','')
    if tp=='': tp='text'

    h='<input type="'+tp+'"'

    sz=i.get('size','')
    if sz=='': sz='50'
    h+=' size="'+sz+'"'
       
    sp=i.get('spellcheck','')
    if sp!='yes':
       h+=' spellcheck="false"'

    name=i.get('name','')
    if name!='':
       h+=' name="'+name+'"'

    value=i.get('value','')
    if tp=='checkbox':
       if value=='on': h+=' checked'
    elif value!='':
       h+=' value="'+value+'"'

    h+='>\n' 

    return {'return':0, 'html':h}

##############################################################################
# create search

def create_textarea(i):
    """
    Input:  {
              (cols)       - columns, 50 by default
              (rows)       - raws, 10 by default
              (spellcheck) - if !='yes', skip 
              (name)       - name
              (value)      - default value
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              html         - html for the form
            }

    """

    cols=i.get('cols','')
    if cols=='': cols='50'

    rows=i.get('rows','')
    if rows=='': rows='10'
     
    h='<textarea cols="'+cols+'" rows="'+rows+'"'

    sp=i.get('spellcheck','')
    if sp!='yes':
       h+=' spellcheck="false"'

    name=i.get('name','')
    if name!='':
       h+=' name="'+name+'"'
    h+='>\n' 

    value=i.get('value','')
    if value!='': h+=value

    h+='</textarea>'

    return {'return':0, 'html':h}

##############################################################################
# create submit button

def create_button(i):
    """
    Input:  {
              (type)       - if '', use 'submit'
              (name)       - name
              (value)      - default value
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              html         - html for the form
            }

    """



    tp=i.get('type','')
    if tp=='': tp='submit'

    h='<input type="'+tp+'"'
    
    name=i.get('name','')
    if name!='':
       h+=' name="'+name+'"'

    value=i.get('value','')
    if value!='':
       h+=' value="'+value+'"'

    h+='>'

    return {'return':0, 'html':h}

##############################################################################
# add via web front end

def webadd(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    fda_name='ck_top_data_alias'
    fdu_name='ck_top_data_uid'
    fdn_name='ck_top_data_name'

    fauthor_name='ck_top_author'
    fauthor_email_name='ck_top_author_email'
    fauthor_web_name='ck_top_author_web'
    fcopyright_name='ck_top_copyright'
    flicense_name='ck_top_license'

    ftags_name='ck_top_tags'

    ffile_name='file_content'
    ffile_overwrite_name='file_content_overwrite'
    ffile1_name=ffile_name+'_uploaded'

    fmeta_name='ck_top_meta'

    fadd_name1='ck_top_final_add'

    # Check if submission
    submission=False
    missing=False
    meta_bad=False
    if fadd_name1 in i: submission=True

    # Check filters
    cid=i.get('wcid','')
    cduoa=''
    cmuoa=''
    cruoa=''

    if cid!='':
       r=ck.parse_cid({'cid':cid})
       if r['return']>0: return r
       cduoa=r['data_uoa']
       cmuoa=r['module_uoa']
       cruoa=r.get('repo_uoa','')

    if i.get('wrepo_uoa','')!='':
       cruoa=i['wrepo_uoa']

    if fdata_name in i: cduoa=i[fdata_name]
    if fmodule_name in i: cmuoa=i[fmodule_name]
    if frepo_name in i: cruoa=i[frepo_name]

    cid=''
    cidx=''
    if cruoa!='' or cmuoa!='' or cduoa!='':
       if cduoa!='': cid=cduoa
       cid=':'+cid
       if cmuoa!='': cid=cmuoa+cid
       cid=':'+cid
       cidx=cid
       if cruoa!='': cid=cruoa+cid

    dalias=i.get('data_alias','')
    if fda_name in i: dalias=i[fda_name]

    duid=i.get('data_uid','')
    if fdu_name in i: duid=i[fdu_name]

    if dalias!='': cduoa=dalias
    if duid!='': cduoa=duid

    dname=i.get('data_name','')
    if fdn_name in i: dname=i[fdn_name]

    dtags=i.get('tags','')
    if ftags_name in i: dtags=i[ftags_name]

    xauthor=i.get('author','')
    if fauthor_name in i: xauthor=i[fauthor_name]

    xauthor_email=i.get('author_email','')
    if fauthor_email_name in i: xauthor_email=i[fauthor_email_name]

    xauthor_web=i.get('author_web','')
    if fauthor_web_name in i: xauthor_web=i[fauthor_web_name]

    xcopyright=i.get('copyright','')
    if fcopyright_name in i: xcopyright=i[fcopyright_name]

    xlicense=i.get('license','')
    if flicense_name in i: xlicense=i[flicense_name]

    xmeta=i.get('meta','')
    if fmeta_name in i: xmeta=i[fmeta_name]
    if xmeta=='': xmeta='{\n}\n'

    xfoverwrite=i.get(ffile_overwrite_name,'')

    ddx={}
    rddx=''
    rx=ck.convert_json_str_to_dict({'str':xmeta, 'skip_quote_replacement':'yes'})
    if rx['return']>0: 
       missing=True
       meta_bad=True
       rddx=rx['error']
    else:
       ddx=rx['dict']

    # Check if already exists - then update
    if cmuoa!='' and cduoa!='':
       ii={'action':'load', 'module_uoa':cmuoa, 'data_uoa':cduoa}
       if cruoa!='': ii['repo_uoa']=cruoa
       rx=ck.access(ii)
       if rx['return']==0:
          dd=rx['dict']
          di=rx['info']

          ry=ck.dumps_json({'dict':dd, 'sort_keys':'yes'})
          if ry['return']==0:
             xmeta=ry['string']

          duid=rx['data_uid']
          dname=rx['data_name']

          atags=dd.get('tags',{})
          if len(atags)>0 and dtags=='':
             for q in atags:
                 if dtags!='': dtags+=','
                 dtags+=q

          control=di.get('control',{})

          if control.get('author','')!='': xauthor=control['author']
          if control.get('author_email','')!='': xauthor_email=control['author_email']
          if control.get('author_webpage','')!='': xauthor_web=control['author_webpage']
          if control.get('copyright','')!='': xcopyright=control['copyright']
          if control.get('license','')!='': xlicense=control['license']

    # Check host/port and default module/action.
    rx=form_url_prefix(i)
    if rx['return']>0: return rx
    url0=rx['url']
    template=rx['template']
    d=rx['meta']
    p=rx['path']
    h=rx['html']
    url_template_pull=rx['url_template_pull']

    url00=url0

    # wfe_url_prefix_subst is used to make "good" looking URL for referencing
    # when CK server is behind some redirecting services such as no-ip. 
    if ck.cfg.get('wfe_url_prefix_subst','')!='': url00=ck.cfg['wfe_url_prefix_subst']

    url=url0
    action=i.get('action','')
    muoa=i.get('module_uoa','')

    # Prepare URL
    url_add=url0+'action=webadd'
    if i.get('update','')=='yes': url_add+='&update=yes'
    url_add+='&module_uoa='+muoa
    url_add1=url_add
    if cid!='': url_add+='&wcid='+cid

    # Check submission
    if submission:
       if cmuoa=='': missing=True

    if submission and not missing:
       ht='<center><br><br>\n'

       if dtags!='':
          xtags=dtags.split(',')
          xtags1=[]
          for q in xtags:
              xtags1.append(q.strip())
          ddx['tags']=xtags1

       ii={'action':'add',
           'dict': ddx,
           'module_uoa':cmuoa}

       if i.get('update','')=='yes': ii['action']='update'

       if cruoa!='': ii['repo_uoa']=cruoa 
       if dalias!='': ii['data_uoa']=dalias
       if duid!='': ii['data_uid']=duid
       if dname!='': ii['data_name']=dname

       info={}
       if xauthor!='': info['author']=xauthor
       if xauthor_email!='': info['author_email']=xauthor_email
       if xauthor_web!='': info['author_webpage']=xauthor_web
       if xcopyright!='': info['copyright']=xcopyright
       if xlicense!='': info['license']=xlicense

       ii['extra_info']=info

       rx=ck.access(ii)
       if rx['return']>0: 
          ht+=rx['error']
       else:
          p=rx['path']

          duoa=rx['data_uoa']
          duid=rx['data_uid']

          x=duoa
          if duoa!=duid: 
             x+=' ('+duid+')'

          xu='added'
          if i.get('update','')=='yes': xu='updated'

          ht+='<b>Entry '+x+' '+xu+'!</b><br><br>\n'

          overwrite=False
          if xfoverwrite=='on': overwrite=True

          farc=i.get(ffile1_name, '')
          if farc!='' and os.path.isfile(farc):
             # Process if archive
             import zipfile
             f=open(farc,'rb')

             arc=True
             try:
                z=zipfile.ZipFile(f)
             except Exception as e: 
                ht+='<b><i>Problem uploading archive ('+format(e)+')</i></b><br>'
                arc=False
                pass

             if arc:
                ht+='<i>Archive uploaded.</i><br><br>'
                for d in z.namelist():
                    if not d.startswith('.') and not d.startswith('/') and not d.startswith('\\'):
                       pp=os.path.join(p,d)
                       if d.endswith('/'): 
                          # create directory 
                          if not os.path.exists(pp): os.makedirs(pp)
                       else:
                          ppd=os.path.dirname(pp)
                          if not os.path.exists(ppd): os.makedirs(ppd)

                          # extract file
                          if os.path.isfile(pp) and not overwrite:
                             ht+='Warning:  File <i>"'+d+'"</i> already exists in the entry - skipping ...<br>\n'
                          else:
                             fo=open(pp, 'wb')
                             fo.write(z.read(d))
                             fo.close()
             f.close()

             try:
                os.remove(farc)
             except Exception as e:
                pass

#          import json
#          ht+='<br><pre>'+json.dumps(i, indent=2)+'</pre>'

       ht+='</center><br>'
       hm=''

    else:
       # Start form + URL
       ii={'url':url_add1, 'name':form_name}
       r=start_form(ii)
       if r['return']>0: return r
       hf=r['html']

       # Get list of repos
       r=ck.access({'action':'list',
                    'module_uoa':ck.cfg["repo_name"],
                    'add_info':'yes',
                    'add_meta':'yes'})
       if r['return']>0: return r
       lm=r['lst']

       r=convert_ck_list_to_select_data({'lst':lm, 'add_empty':'yes', 'sort':'yes', 'value_uoa':cruoa, 'ignore_remote':'yes'})
       if r['return']>0: return r
       dlm=r['data']
       if r.get('value_uid','')!='': cruoa=r['value_uid']

       ii={'data':dlm, 'name':frepo_name, 'onchange':onchange, 'style':'width:300px;'}
       if cruoa!='': ii['selected_value']=cruoa
       r=create_selector(ii)
       if r['return']>0: return r
       hlr=r['html']

       # Get list of modules
       r=ck.access({'action':'list',
                    'module_uoa':ck.cfg["module_name"],
                    'add_info':'yes'})
       if r['return']>0: return r
       lm=r['lst']

       r=convert_ck_list_to_select_data({'lst':lm, 'add_empty':'yes', 'sort':'yes', 'value_uoa':cmuoa})
       if r['return']>0: return r
       dlm=r['data']
       if r.get('value_uid','')!='': cmuoa=r['value_uid']

       ii={'data':dlm, 'name':fmodule_name, 'onchange':onchange, 'style':'width:300px;'}
       if cmuoa!='': ii['selected_value']=cmuoa
       r=create_selector(ii)
       if r['return']>0: return r
       hlm=r['html']

       # Prepare add
       xu='Add'
       if i.get('update','')=='yes': xu='Update'

       r=create_button({'name': fadd_name1, 'value':xu+' entry'})
       if r['return']>0: return r
       hadd=r['html']

       # Prepare alias
       r=create_input({'size':'38', 'name': fda_name, 'value':dalias})
       if r['return']>0: return r
       hdalias=r['html']

       # Prepare UID
       r=create_input({'size':'38', 'name': fdu_name, 'value':duid})
       if r['return']>0: return r
       hduid=r['html']

       # Prepare name
       r=create_input({'size':'38', 'name': fdn_name, 'value':dname})
       if r['return']>0: return r
       hdname=r['html']

       # Prepare tags
       r=create_input({'size':'38', 'name': ftags_name, 'value':dtags})
       if r['return']>0: return r
       hdtags=r['html']

       # Prepare author
       r=create_input({'size':'38', 'name': fauthor_name, 'value':xauthor})
       if r['return']>0: return r
       hauthor=r['html']

       # Prepare author email
       r=create_input({'size':'38', 'name': fauthor_email_name, 'value':xauthor_email})
       if r['return']>0: return r
       hauthor_email=r['html']

       # Prepare author web
       r=create_input({'size':'38', 'name': fauthor_web_name, 'value':xauthor_web})
       if r['return']>0: return r
       hauthor_web=r['html']

       # Prepare copyright
       r=create_input({'size':'38', 'name': fcopyright_name, 'value':xcopyright})
       if r['return']>0: return r
       hcopyright=r['html']

       # Prepare author web
       r=create_input({'size':'38', 'name': flicense_name, 'value':xlicense})
       if r['return']>0: return r
       hlicense=r['html']

       # Prepare zip file upload
       r=create_input({'type':'file', 'size':'38', 'name': ffile_name})
       if r['return']>0: return r
       hfile=r['html']

       # Prepare zip file upload
       r=create_input({'type':'checkbox', 'size':'38', 'name': ffile_overwrite_name, 'value':xfoverwrite})
       if r['return']>0: return r
       hfile_overwrite=r['html']

       # Prepare meta
       r=create_textarea({'cols':'120', 'rows':'30', 'name': fmeta_name, 'value':xmeta})
       if r['return']>0: return r
       hmeta=r['html']

       r=create_input({'type':'hidden', 'name': 'file_content_record_to_tmp', 'value':'yes'})
       if r['return']>0: return r
       hx1=r['html']+'\n'

       # Prepare top
       ht=hf

       ht+='<div id="ck_prune">\n'
       ht+='<b>Add/update entry:</b><br>\n'
       ht+='<small>[ <a href="'+url0+'">Back to CK browser</a> ]</small>\n'
       ht+='</div>\n'
       ht+='\n'

       ht+='<table border="0" cellpadding="5">\n'
       ht+=' <tr>\n'
       tx=''
       if submission and missing and cmuoa=='':
          tx=' style="color:red" '
       ht+='  <td align="right"'+tx+'>Module/class:</td>\n'
       ht+='  <td>'+hlm+'</td>\n'
       ht+=' </tr>\n'
       ht+=' <tr>\n'
       ht+='  <td align="right">Repository:</td>\n'
       ht+='  <td>'+hlr+'</td>\n'
       ht+=' </tr>\n'

       ht+=' <tr>\n'
       ht+='  <td align="right"><br></td>\n'
       ht+='  <td><br></td>\n'
       ht+=' </tr>\n'

       ht+=' <tr>\n'
       ht+='  <td align="right">Alias:</td>\n'
       ht+='  <td>'+hdalias+'</td>\n'
       ht+=' </tr>\n'
       ht+=' <tr>\n'
       ht+='  <td align="right">(UID):</td>\n'
       ht+='  <td>'+hduid+'</td>\n'
       ht+=' </tr>\n'
       ht+=' <tr>\n'
       ht+='  <td align="right">User-friendly name:</td>\n'
       ht+='  <td>'+hdname+'</td>\n'
       ht+=' </tr>\n'

       ht+=' <tr>\n'
       ht+='  <td align="right"><br></td>\n'
       ht+='  <td><br></td>\n'
       ht+=' </tr>\n'

       ht+=' <tr>\n'
       ht+='  <td align="right">Tags:</td>\n'
       ht+='  <td>'+hdtags+'</td>\n'
       ht+=' </tr>\n'

       ht+=' <tr>\n'
       ht+='  <td align="right"><br></td>\n'
       ht+='  <td><br></td>\n'
       ht+=' </tr>\n'

       ht+=' <tr>\n'
       ht+='  <td align="right">Author:</td>\n'
       ht+='  <td>'+hauthor+'</td>\n'
       ht+=' </tr>\n'
       ht+=' <tr>\n'
       ht+='  <td align="right">Author email:</td>\n'
       ht+='  <td>'+hauthor_email+'</td>\n'
       ht+=' </tr>\n'
       ht+=' <tr>\n'
       ht+='  <td align="right">Author web-page:</td>\n'
       ht+='  <td>'+hauthor_web+'</td>\n'
       ht+=' </tr>\n'
       ht+=' <tr>\n'
       ht+='  <td align="right">Entry copyright:</td>\n'
       ht+='  <td>'+hcopyright+'</td>\n'
       ht+=' </tr>\n'
       ht+=' <tr>\n'
       ht+='  <td align="right">Entry license:</td>\n'
       ht+='  <td>'+hlicense+'</td>\n'
       ht+=' </tr>\n'

       ht+=' <tr>\n'
       ht+='  <td align="right"><br></td>\n'
       ht+='  <td><br></td>\n'
       ht+=' </tr>\n'

       ht+=' <tr>\n'
       tx=''
       txr=''
       if meta_bad: 
          tx=' style="color:red" '
          txr='<br><small><i>'+rddx+'</i></small>'
       ht+='  <td align="right" valign="top"'+tx+'>Meta-description in JSON:'+txr+'</td>\n'
       ht+='  <td>'+hmeta+'</td>\n'
       ht+=' </tr>\n'

       ht+=' <tr>\n'
       ht+='  <td align="right"><br></td>\n'
       ht+='  <td><br></td>\n'
       ht+=' </tr>\n'

       ht+=' <tr>\n'
       ht+='  <td align="right" valign="top">Upload zip file:</td>\n'
       ht+='  <td>'+hfile+'\n'+hx1+'</td>\n'
       ht+=' </tr>\n'

       ht+=' <tr>\n'
       ht+='  <td align="right" valign="top">Overwrite existing files:</td>\n'
       ht+='  <td>'+hfile_overwrite+'</td>\n'
       ht+=' </tr>\n'

       ht+=' <tr>\n'
       ht+='  <td align="right"><br></td>\n'
       ht+='  <td><br></td>\n'
       ht+=' </tr>\n'

       ht+='</table>\n'

       hm=hadd+'<br>\n'
       hm+='</form>\n'

    # Replace top if needed
    ht='<center><div id="ck_box_with_shadow">\n'+ht+'</div></center>\n'


    h=h.replace('$#template_top#$',ht)

    hp=''
    h=h.replace('$#template_middle#$',hp)

    h=h.replace('$#template_middle_finish#$',hm)

    h=h.replace('$#ck_styles#$','')

    # Check if visits
    px=os.path.join(p, 'visits.html')
    htx=''
    if os.path.isfile(px):
       r=ck.load_text_file({'text_file':px})
       if r['return']>0: return r
       htx=r['string']
    h=h.replace('$#template_end#$',htx)

    # Substitute specials
    h=h.replace('$#title#$', 'CK Browser')
    h=h.replace('$#ck_url_template_pull#$', url_template_pull)

    return {'return':0, 'html':h}

##############################################################################
# view page

def view_page(i):
    """
    Input:  {
              (page) 
              (wfe_template_data_uoa) - only if not defined in ck.cfg
                      or
              (template)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              html         - unicoded html page
            }

    """

    page=i.get('page','')

    # Get default path to the entry with pages (web_tempalte_uoa in kernel)
    truoa=ck.cfg.get('wfe_template_repo_uoa','')
    tduoa=ck.cfg.get('wfe_template_data_uoa','')

    if tduoa=='':
       tduoa=i.get('wfe_template_data_uoa','')

    temp_uoa=i.get('template','')
    if tduoa=='':
       tduoa=temp_uoa

    r=ck.access({'action':'load',
                 'module_uoa':work['self_module_uoa'],
                 'repo_uoa':truoa,
                 'data_uoa':tduoa})
    if r['return']>0: return r

    dd=r['dict']
    pp=r['path']

    # Find page html
    h=page

    p=os.path.join(pp, h)
    if not os.path.isfile(p):
       p=os.path.join(pp, h+'.html')
       if os.path.isfile(p):
          h=h+'.html'
       else:
          p=os.path.join(pp, h, 'index.html')
          if os.path.isfile(p):
             h=os.path.join(h,'index.html')
          else:
             return {'return':1, 'error':'page not found'}

    # Check if page has associated meta (.json)
    dp={}

    x=p.rfind('.')
    if x>=0:
       px=p[:x]+'.json'
       if os.path.isfile(px):
          rx=ck.load_json_file({'json_file':px})
          if rx['return']>0: return rx
          dp=rx['dict']

    # Make smart merge of original dict with this one (inheritance via json)
    rx=ck.merge_dicts({'dict1':dd, 'dict2':dp})
    if rx['return']>0: return rx
    dd=rx['dict1']

    # Load (default) page template if needed
    html=''

    tf=dp.get('template_file','')
    if tf=='': tf=dd.get('template_file','')

    if tf!='':
       r=ck.load_text_file({'text_file':os.path.join(pp,tf)}) 
       if r['return']>0: return r
       html=r['string']

    # Prepare substitutes
    rurl=''
    if os.environ.get('CK_WFE_URL_PREFIX_SKIP','')!='yes':
       rurl=os.environ.get('CK_WFE_URL_PREFIX','')
       if rurl=='':
          # Check host/port and default module/action.
          rx=form_url_prefix(i)
          if rx['return']>0: return rx
          rurl=rx['url']

    # Check if different template
    if temp_uoa!='':
       rurl+='template='+temp_uoa+'&'

    rurlp=rurl
    add_html=''
    if os.environ.get('CK_WFE_URL_PREFIX_PAGE_SKIP','')!='yes':
       rurlp+='page='
    else:
       add_html='.html'

    rutp=rurl
    if os.environ.get('CK_WFE_URL_PREFIX_PULL_SKIP','')!='yes':
       rutp+='action=pull&common_func=yes&cid='
       if truoa!='': rutp+=truoa+':'
       rutp+='wfe:'+tduoa+'&filename='

    # Prepare menu
    menu=''

    mdesc=dd.get('menu_desc',[])
    mn=dd.get('menu',[])

    im=0
    st='' # subtitle, if needed
    for m in mn:
        #Get style
        md=mdesc[im]

        ms=md.get('html_start','')
        me=md.get('html_end','')

        menu+='   '+ms+'\n'

        for mx in md.get('nodes',[]):

            idx=mx.get('id','')
            name=mx.get('name','')

            if mx.get('external_link','')=='yes':
                ah=''
            else:
                ah=add_html

            link=mx.get('link','')+ah

            if idx==m: menu+='     '+md.get('html_on_start','')
            else:      menu+='     '+md.get('html_off_start','')

            x1=''
            x2=''
            if mx.get('bold','')=='yes':
               x1='<b>'
               x2='</b>'

            x3=''
            if mx.get('target_blank','')=='yes':
               x3=' target="_blank"'

            xm='<a href="'+link+'"'+x3+'>'+x1+name+x2+'</a>'
            menu+=xm

            if idx==m:
               if st=='': st='Back to '+xm
               else: st+='&nbsp;/&nbsp;'+xm

            if idx==m: menu+='     '+md.get('html_on_end','')+'\n'
            else:      menu+='     '+md.get('html_off_end','')+'\n'

        menu+='   '+me+'\n'

        im+=1

    # Update menu
    html=html.replace('$#ck_menu#$', menu)

    # Load page
    ii={'text_file':p}
    if not (p.endswith('.txt') or p.endswith('.html') or p.endswith('.htm') or p.endswith('.json')):
       return {'return':1, 'error':'can view only pages'}
    r=ck.load_text_file(ii) 
    if r['return']>0: return r
    template=r['string']

    if p.endswith('.txt') or p.endswith('.txt'):
       # Process links
       r=parse_txt({'string':template, 'skip_search_only_inside_quotes':'yes'})
       if r['return']>0: return r
       template=r['string']

       template='<pre>'+template+'</pre>'

    # Check if sub-title
    stx=dp.get('subtitle','')
    if stx!='':
       template='<div id="ck_subtitle">'+st+'</div><div id="ck_subtitle1">'+stx+'</div>'+template

    # Substitute middle in template
    if html=='':
       html=template
    else:
       html=html.replace('$#ck_template_middle#$',template)

    # Replace various vars
    title=dp.get('title','')
    if title=='': title=dd.get('title','')
    html=html.replace('$#ck_title#$',title)

    keys=dd.get('global_keywords','')
    keys1=dp.get('keywords','')
    if keys!='' and keys1!='': keys+=','
    keys+=keys1
    html=html.replace('$#ck_page_keywords#$',keys)

    # Replace various vars
    share=dd.get('share','')
    html=html.replace('$#ck_var_share#$',share)

    html=html.replace('$#ck_root_url#$', rurl)
    html=html.replace('$#ck_root_page_url#$', rurlp)
    html=html.replace('$#wfe_url_prefix_page#$',rurlp)
    html=html.replace('$#ck_page_suffix#$',add_html)

    html=html.replace('$#ck_url_template_pull#$', rutp)

    html=html.replace('$#ck_var_page_name#$', page)

    # Replace pre-set vars
    vr=dd.get('vars','')
    for k in vr:
        v=vr[k]
        html=html.replace('$#'+k+'#$',v)

    return {'return':0, 'html':html}

##############################################################################
# parse text/json/etc files to detect http,CM,CK ...

def parse_txt(i):
    """
    Input:  {
               string                           - text to process
               (cm_url)                         - root URL when detecting CM refs
               (skip_search_only_inside_quotes) - if 'yes', do not search inside quotes
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    mt=i['string']

    url0=i.get('cm_url','')

    ss=i.get('skip_search_only_inside_quotes','')

    # Try to detect links
    for prefix in ['http://', 'https://']:
        i0=0
        while i0>=0:
           i0=mt.find(prefix, i0)

           if i0<0: break

           j=[]
           jx=mt.find('\r',i0)
           if jx>0: j.append(jx)
           jx=mt.find('\n',i0)
           if jx>0: j.append(jx)
           jx=mt.find(' ',i0)
           if jx>0: j.append(jx)
           jx=mt.find('"',i0)
           if jx>0: j.append(jx)
           j.append(len(mt))
           j0=min(j)
           if j0>i0:
              url=mt[i0:j0]
              add='<a href="'+url+'">'+url+'</a>'
              mt=mt[:i0]+add+mt[j0:]
           i0+=len(add)

    # Next is for compatibility with cM
    i0=0
    while True:
       i1=mt.find('$#cm_',i0)
       if i1<0: break

       i2=mt.find('#$',i1+1)
       if i2<0: break

       x=mt[i1:i2+2]
       x1=x[5:-2].split('_')
       y='<a href="'+url0+'wcid='+x1[0]+':'+x1[1]+'">'+x+'</a>'
       mt=mt[:i1]+y+mt[i2+2:]
       i0=i1+len(y)

    return {'return':0, 'string':mt}

##############################################################################
# clean tmp cache

def clean(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')

    if o=='con':
       ck.out('Cleaning web cache ...')

    # Check if tmp exists
    rx=ck.access({'action':'load',
                  'module_uoa':'tmp',
                  'data_uoa':work['self_module_uoa']})
    if rx['return']==0:
       p=rx['path']

       dirList=os.listdir(p)
       for fn in dirList:
           if fn.startswith('tmp-'):
              pp=os.path.join(p, fn)
              if os.path.isfile(pp):
                 try:
                    os.remove(pp)
                 except Exception as e:
                     None

    return {'return':0}

##############################################################################
# process ck special instructions in html pages

def process_ck_page(i):
    """
    Input:  {
              html
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    h=i.get('html','')
    st=''

    j=0

    while True:
       j1=h.find('$#ck_include_start#$', j)
       if j1>0:
          j2=h.find('$#ck_include_stop#$', j1)
          if j2>0:
             sparams=h[j1+20:j2]

             subst=''

             # Convert JSON params to dict
             rx=ck.convert_json_str_to_dict({'str':sparams, 'skip_quote_replacement':'yes'})
             if rx['return']==0:
                params=rx['dict']

                cid=params.get('cid','')
                fh=params.get('html','')
                fs=params.get('style','')

                where=params.get('where','')
                if where=='': where='body'

                if cid!='':
                   rx=ck.access({'action':'load',
                                 'cid':cid})
                   if rx['return']==0:
                      pp=rx['path']

                      if fh!='':
                         px=os.path.join(pp, fh)
                         if os.path.isfile(px):
                            r=ck.load_text_file({'text_file':px})
                            if r['return']>0: return r
                            subst=r['string']

                         # Replace where to attach
                         subst=subst.replace('$#ck_where#$', where)

                      if fs!='':
                         px=os.path.join(pp, fs)
                         if os.path.isfile(px):
                            r=ck.load_text_file({'text_file':px})
                            if r['return']>0: return r
                            st=r['string']

                if params.get('add_div','')=='yes':
                   where1=where
                   if where.startswith('div#'):
                      where1=where[4:]
                   subst='\n<div id="'+where1+'" style="text-align:center">\n'+subst+'\n</div>\n'

                if params.get('add_box','')=='yes':
                   wx=params.get('box_width','')
                   if wx!='': wx=' style="width:'+str(wx)+'px;'
                   subst='\n<div id="ck_box_with_shadow"'+wx+'">\n'+subst+'\n</div>\n'

                if params.get('remove_script_src','')=='yes':
                   k1=subst.find('<script src')
                   if k1>=0:
                      k2=subst.find('</script>', k1)
                      if k2>0:
                         subst=subst[:k1]+subst[k2+9:]

             h=h[:j1]+subst+h[j2+19:]
       
             j=j1
             continue

       break

    return {'return':0, 'html':h, 'style':st}

##############################################################################
# process all pages and convert them into static ones

def process_all_pages(i):
    """
    Input:  {
              data_uoa  - website/html templates
              (web_dir) - website directory

              (dirs)    - list of dirs
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os

    # Check current path
    wd=i.get('web_dir','')
    if wd=='': wd='tmp-website'

    try:
        cp=os.getcwd()
    except OSError:
        os.chdir('..')
        cp=os.getcwd()

    cpw=os.path.join(cp, wd)

    if not os.path.isdir(cpw):
       os.makedirs(cpw)

    duoa=i['data_uoa']

    # Find templates
    ii={'action':'load',
        'module_uoa':work['self_module_uoa'],
        'data_uoa':duoa}
    rx=ck.access(ii)
    if rx['return']>0: return rx
    pp=rx['path']
    dd=rx['dict']


    dirs=i.get('dirs',[])

    dd=[""]
    for q in dirs:
        dd.append(q)

    # Get all htmls
    for p0 in dd:

        if p0!='':
           pz=os.path.join(cpw, p0)
           if not os.path.isdir(pz): 
              os.makedirs(pz)

        p1=os.path.join(pp,p0)
        dirList=os.listdir(p1)
        for fn in dirList:
            if fn.endswith('.html'):
               page=fn[:-5]
               page1=os.path.join(p0, fn)
               ppage=os.path.join(pp, page1)

               ck.out('Processing page "'+page1+'" ...')

               r=view_page({'page':page1, 'wfe_template_data_uoa':duoa})
               if r['return']>0: return r
               html=r['html']

               px=os.path.join(cpw, p0, fn)
               r=ck.save_text_file({'text_file':px, 'string':html})
               if r['return']>0: return r

    return {'return':0}

##############################################################################
# form URL prefix (if used via CK web server or via third-party web server and PHP)
#  together with host, port and template

def form_url_prefix(i):
    """
    Input:  {
              original input

              (host)         - prepared by CK web server
              (port)         - prepared by CK web server

              (template)     - possible web template

              (base_url)     - already prepared base url

              (use_repo_uoa) - use specific repo
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              url                  - prepared URL (with template)
              url_without_template - URL without template
              template             - template UOA (or default)
              meta                 - meta of a template
              html                 - html of a template
              path                 - path to template
              url_template_pull    - URL to pull resources from template entry
            }

    """

    url0=''

    # Check host/port and default module/action.
    host=i.get('host','')
    port=i.get('port','')
    burl=i.get('base_url','')

    if burl!='':
       url0=burl
    elif host!='' and port!='':
       url0='http://%s:%s/web?' % (host, port)
    else:
       url0=ck.cfg.get('wfe_url_prefix','')

    url0w=url0

    template=i.get('template','')
    if template=='': 
       template=ck.cfg.get('wfe_template','')

    url_template_pull=url0+'action=pull&common_func=yes&cid=wfe:'+template+'&filename='

    if template!='' and template!='default':
       url0+='template='+template+'&'

    # Load template
    ii={'action':'load',
        'common':'yes',
        'repo_uoa':i.get('use_repo_uoa',''),
        'module_uoa':work['self_module_uoa'],
        'data_uoa':template}
    r=ck.access(ii)
    if r['return']>0: return r
    d=r['dict']
    p=r['path']

    tf=d.get('template_file','')
    if tf=='': tf='template.html'

    px=os.path.join(p, tf)
    if not os.path.isfile(px):
       return {'return':1, 'error':'template file not found ('+px+')'}

    r=ck.load_text_file({'text_file':px})
    if r['return']>0: return r
    h=r['string']

    return {'return':0, 'url':url0, 'url_without_template':url0w, 'template':template, 'html':h, 'meta':d, 'path':p, 'url_template_pull':url_template_pull}
