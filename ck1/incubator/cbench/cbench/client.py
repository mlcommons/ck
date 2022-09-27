#
# Web service for the client
# Partially based on CK web service
#
# Developer(s): Grigori Fursin
#               Herve Guillou
#

from . import config
from . import comm

import ck.kernel as ck

import json
import sys
import os
import tempfile
import cgi
#import ssl
import time
import requests

# Import various modules while supporting both Python 2.x and 3.x
try:
  from http.server import BaseHTTPRequestHandler, HTTPServer
except:
  from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

try:
  import urllib.parse as urlparse
except:
  import urlparse

try:
  from urllib.parse import quote as urlquote
except:
  from urllib import quote as urlquote

try:
  from urllib.parse import unquote as urlunquote
except:
  from urllib import unquote as urlunquote

#try:
#   import http.cookies as Cookie
#except:
#   import Cookie

try:
  from socketserver import ThreadingMixIn
except:
  from SocketServer import ThreadingMixInqZBMfAaH
  


context_types={
    "bz2": {
      "Content-disposition": "attachment; filename=$#filename#$", 
      "Content-title": "$#filename#$", 
      "Content-type": "application/x-bzip2"
    }, 
    "con": {
      "Content-type": "text/plain; charset=utf-8"
    }, 
    "css": {
      "Content-disposition": "inline; filename=$#filename#$", 
      "Content-title": "$#filename#$", 
      "Content-type": "text/css"
    }, 
    "csv": {
      "Content-disposition": "attachment; filename=$#filename#$", 
      "Content-title": "$#filename#$", 
      "Content-type": "text/csv"
    }, 
    "eps": {
      "Content-disposition": "attachment; filename=$#filename#$", 
      "Content-title": "$#filename#$", 
      "Content-type": "application/postscript"
    }, 
    "gif": {
      "Content-type": "image/gif"
    }, 
    "gz": {
      "Content-disposition": "attachment; filename=$#filename#$", 
      "Content-title": "$#filename#$", 
      "Content-type": "application/x-gzip"
    }, 
    "html": {
      "Content-type": "text/html; charset=utf-8"
    }, 
    "jpeg": {
      "Content-type": "image/jpeg"
    }, 
    "jpg": {
      "Content-type": "image/jpeg"
    }, 
    "js": {
      "Content-disposition": "inline; filename=$#filename#$", 
      "Content-title": "$#filename#$", 
      "Content-type": "text/javascript"
    }, 
    "json": {
      " -type": "w/json; charset=utf-8"
    }, 
    "pdf": {
      "Content-disposition": "attachment; filename=$#filename#$", 
      "Content-title": "$#filename#$", 
      "Content-type": "application/pdf"
    }, 
    "png": {
      "Content-type": "image/png"
    }, 
    "ps": {
      "Content-disposition": "attachment; filename=$#filename#$", 
      "Content-title": "$#filename#$", 
      "Content-type": "application/postscript"
    }, 
    "txt": {
      "Content-type": "text/plain; charset=utf-8"
    }, 
    "unknown": {
      "Content-disposition": "attachment; filename=$#filename#$", 
      "Content-title": "$#filename#$", 
      "Content-type": "application/octet-stream"
    }, 
    "zip": {
      "Content-disposition": "attachment; filename=$#filename#$", 
      "Content-title": "$#filename#$", 
      "Content-type": "application/zip"
    }
  }

# URL to tunnel requests to (useful for development boards and Raspberry Pi)
tunnel_url=''

# Skip print for hearbeat
heartbit_started=False
get_status_started=False

##############################################################################
# Class to handle requests in separate threads

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):

  """
  """

##############################################################################
# Send error to HTTP stream

def web_out(i):
  """
  Input:  {
            http       - http object
            type       - content type
            bin        - bytes to output
            (filename) - if !='', substitute filename in headers
          }

  Output: {
            return - 0
          }
  """

  http=i['http']
  bin=i['bin']

  tp=i['type']

  if tp=='' or tp=='web': tp='html'

  tpx=context_types.get(tp,{})
  if len(tpx)==0:
    tp='unknown'
    tpx=cfg['content_types'][tp]

  fn=i.get('filename','')

  # Output
  for k in sorted(tpx.keys()):
    v=tpx[k]
    if fn!='': v=v.replace('$#filename#$', fn)
    http.send_header(k,v)

  http.send_header('Access-Control-Allow-Origin', '*')
  http.send_header('Content-Length', str(len(bin)))
  http.end_headers()

  http.wfile.write(bin)

  return {'return':0}

##############################################################################
# Send error to HTTP stream

def web_err(i):
  """
  Input:  {
            http - http object
            type - content type
            bin  - bytes to output
          }

  Output: {
            return - 0
          }
  """

  http=i['http']
  tp=i['type']
  bin=i['bin']

  try: bin=bin.decode('utf-8')
  except Exception as e: pass

  if tp=='json':
    rx=ck.dumps_json({'dict':{'return':1, 'error':bin}})
    if rx['return']>0:
      bin2=rx['error'].encode('utf8')
    else:
      bin2=rx['string'].encode('utf-8')
  elif tp=='con':
    bin2=bin.encode('utf8')
  else:
    bin2=b'<html><body><pre>'+bin.encode('utf8')+b'</pre></body></html>'

  i['bin']=bin2
  return web_out(i)

##############################################################################
# Process CK web service request (both GET and POST)

def process_web_request(i):
  """

  Input:  {
            http - Python http object
          }

  Output: { None }
  """

  global heartbit_started, get_status_started

  from . import solution

  # http object
  http=i['http']

  # Parse GET variables and path
  xget={}
  xpath={'host':'', 'port':'', 'first':'', 'rest':'', 'query':''} # May be used in the future

  xt='json'

  xpath['host']=i.get('host','')
  xpath['port']=i.get('port','')

  # Check GET variables
  if http.path!='':
    http.send_response(200)

    a=urlparse.urlparse(http.path)
    xp=a.path
    xr=''

    if xp.startswith('/'): xp=xp[1:]

    u=xp.find('/')
    if u>=0:
      xr=xp[u+1:]
      xp=xp[:u]

    xt=xp

    xpath['first']=xp
    xpath['rest']=xr
    xpath['query']=a.query
    b=urlparse.parse_qs(a.query, keep_blank_values=True, )

    xget={}
    for k in b:
      xget[k]=urlunquote(b[k][0])
      if sys.version_info[0]<3:
        xget[k]=xget[k].decode('utf8')
  
  # Check POST
  xpost={}
  xpost1={}

  try:
    headers = http.headers
    content_type = headers.get('content-type')
    ctype=''
    if content_type != None:
      ctype, pdict = cgi.parse_header(content_type)
      # Python3 cgi.parse_multipart expects boundary to be bytes, not str.
      if sys.version_info[0]<3 and 'boundary' in pdict:
        pdict['boundary'] = pdict['boundary'].encode()

    if ctype == 'multipart/form-data':
      if sys.version_info[0]<3:
        xpost1 = cgi.parse_multipart(http.rfile, pdict)
      else:
        xxpost1 = cgi.FieldStorage(fp=http.rfile, headers=headers, environ={'REQUEST_METHOD':'POST'})
        for k in xxpost1.keys():
            xpost1[k]=[xxpost1[k].value]
    elif ctype == 'application/x-www-form-urlencoded':
      length = int(http.headers.get('content-length'))
      s=http.rfile.read(length)
      if sys.version_info[0]>2: s=s.decode('utf8')
      xpost1 = cgi.parse_qs(s, keep_blank_values=1)

  except Exception as e:
    web_err({'http':http, 'type':xt, 'bin':bin})
    ck.out(ck.cfg['error']+bin.decode('utf8'))
    return

  # Post processing
  for k in xpost1:
    v=xpost1[k]
    if k.endswith('[]'):
      k1=k[:-2]
      xpost[k1]=[]
      for l in v:
        xpost[k1].append(urlunquote(l))
    else:
      if k!='file_content':
        xpost[k]=urlunquote(v[0])
      else:
        xpost[k]=v[0]

    if k=='file_content':
      fcrt=xpost1.get('file_content_record_to_tmp','')
      if (type(fcrt)==list and len(fcrt)>0 and fcrt[0]=='yes') or fcrt=='yes':
        fd, fn=tempfile.mkstemp(suffix='.tmp', prefix='ck-') # suffix is important - CK will delete such file!
        os.close(fd)

        f=open(fn,'wb')
        f.write(xpost[k])
        f.close()

        xpost[k+'_uploaded']=fn
        del(xpost[k])
        k+='_uploaded'
      else:
        import base64
        xpost[k+'_base64']=base64.urlsafe_b64encode(xpost[k]).decode('utf8')
        del(xpost[k])
        k+='_base64'

    if sys.version_info[0]<3:
      xpost[k]=xpost[k].decode('utf8')

  # Prepare input and check if CK json present
  ii=xget
  ii.update(xpost)

  act=ii.get('action','')

  # Generate tmp file (to output images for example)
  fd, fn=tempfile.mkstemp(suffix='.tmp', prefix='ck-') # suffix is important - CK will delete such file!
  os.close(fd)
  if os.path.isfile(fn): os.remove(fn)

  # Get tmp dir
  p=tempfile.gettempdir()

  # Execute command *********************************************************
#  ck.out('*** Received action request: ' + act)
  if act=='get_host_platform_info':
    r=ck.access({'action':'detect',
                  'module_uoa':'platform'})
    if r['return']>0: 
      # Process error properly
      web_err({'http':http, 'type':xt, 'bin':r['error'].encode('utf8')})
      return

    s=json.dumps(r, indent=2, sort_keys=True)
    web_out({'http':http, 'type':'json', 'bin':s.encode('utf8')})

    return
  #############################################################################################################3
  elif act=='init_workflow':

    data_id=ii.get('data_id','')

    r=solution.init({'uid':data_id})

    # start program
    #    r=ck.access({'action':'run',
    #          'module_uoa':'program',
    #          'data_uoa':ii.get('program_name',''), 
    #          'cmd_key': 'use_continuous',
    #          'deps.python': 'a699c0c7de43a121',
    #          'quiet': 'yes'})

    if r['return']>0: 
      ck.out(config.CR_LINE)
      ck.out("Error: "+r.get('error',''))
      ck.out(config.CR_LINE)

      # Process error properly
      web_err({'http':http, 'type':xt, 'bin':r['error'].encode('utf8')})
      return

    solution = {'status': True}
    s=json.dumps(solution, indent=4, sort_keys=True)

    ck.out(config.CR_LINE)
    ck.out("Success!")
    ck.out(config.CR_LINE)

    web_out({'http':http, 'type':'json', 'bin':s.encode('utf8')})

    return
  #############################################################################################################3
  elif act=='run_program':

    data_id=ii.get('data_id','')

    r=solution.run({'uid':data_id})

    # start program
    #    r=ck.access({'action':'run',
    #          'module_uoa':'program',
    #          'data_uoa':ii.get('program_name',''), 
    #          'cmd_key': 'use_continuous',
    #          'deps.python': 'a699c0c7de43a121',
    #          'quiet': 'yes'})

    if r['return']>0: 
      ck.out(config.CR_LINE)
      ck.out("Error: "+r.get('error',''))
      ck.out(config.CR_LINE)

      # Process error properly
      web_err({'http':http, 'type':xt, 'bin':r['error'].encode('utf8')})
      return

    solution = {'status': True}
    s=json.dumps(solution, indent=4, sort_keys=True)

    ck.out(config.CR_LINE)
    ck.out("Success!")
    ck.out(config.CR_LINE)

    web_out({'http':http, 'type':'json', 'bin':s.encode('utf8')})

    return

  #############################################################################################################3
  elif act=='benchmark_program':

    data_id=ii.get('data_id','')

    r=solution.benchmark({'uid':data_id})

    if r['return']>0: 
      ck.out(config.CR_LINE)
      ck.out("Error: "+r.get('error',''))
      ck.out(config.CR_LINE)

      # Process error properly
      web_err({'http':http, 'type':xt, 'bin':r['error'].encode('utf8')})
      return

#    solution = {'status': True}
#    s=json.dumps(solution, indent=4, sort_keys=True)
    # Need to pass info about graphs
    s=json.dumps(r, sort_keys=True)

    ck.out(config.CR_LINE)
    ck.out("Success!")
    ck.out(config.CR_LINE)

    web_out({'http':http, 'type':'json', 'bin':s.encode('utf8')})
    return

  #############################################################################################################3
  elif act=='publish_result':

    data_id=ii.get('data_id','')

    r=solution.publish_result({'uid':data_id})

    if r['return']>0: 
      # Process error properly
      web_err({'http':http, 'type':xt, 'bin':r['error'].encode('utf8')})
      return

    solution = {'status': True}
#    s=json.dumps(solution, indent=4, sort_keys=True)
    s=json.dumps(r, sort_keys=True)

    ck.out(config.CR_LINE)
    ck.out("Success!")
    ck.out(config.CR_LINE)

    web_out({'http':http, 'type':'json', 'bin':s.encode('utf8')})
    return
  
  #############################################################################################################3
  elif act=='get_program_result_image':

    data_id=ii['data_id']
    program_name=ii['program_name']

    jpeg=ii.get('jpeg','')

    ck_entry=program_name.split(':')

    # Find solution
    r=ck.access({'action':'load',
                 'module_uoa':'solution',
                 'data_uoa':data_id})
    if r['return']>0:
      # Process error properly
      web_err({'http':http, 'type':xt, 'bin':r['error'].encode('utf8')})
      return

    p=r['path']

    meta=r['dict']
    workflow_output_dir=meta.get('workflow_output_dir','')

    workflow_repo=meta.get('workflow_repo_url','')
    j=workflow_repo.rfind('/')
    if j>0:
      workflow_repo=workflow_repo[j+1:]

    cur_dir=os.path.join(p, 'CK', workflow_repo, ck_entry[0], ck_entry[1])
    if workflow_output_dir!='':
      cur_dir=os.path.join(cur_dir, workflow_output_dir)

    #       r=ck.access({'action':'find',
    #            'module_uoa':'program',
    #            'data_uoa':ii.get('program_name','')})
    #
    #       if r['return']>0: 
    #          # Process error properly
    #          web_err({'http':http, 'type':xt, 'bin':r['error'].encode('utf8')})
    #          return

    #    cur_dir = 'D:\\Work1\\CK\\ck-repos\\local\\solution\\demo-obj-detection-kitti-min-tf-cpu-win\\CK\\ck-tensorflow\\program\\squeezedet\\tmp\\out' #os.path.join(r['path'],"tmp/out") 
    #    cur_dir='/home/cindex/CK/local/solution/demo-obj-detection-self-driving-win/CK/ck-tensorflow/program/squeezedet/tmp/out'
    #    cur_dir='/home/cindex/CK/local/solution/demo-obj-detection-kitti-min-tf-cpu-win/CK/ck-tensorflow/program/squeezedet/tmp/out'

    # find the penultimate image provided
    try:
      st = False
      filepath = ''
      filepath_buf = ''

      found_files=[]

      ck.out('')
      ck.out('Checking for output files in directory:')
      ck.out('  '+cur_dir)
      ck.out('')

      sorted_list=sorted(os.listdir(cur_dir))
      for file in sorted_list:
        if file.endswith(".png") and file.startswith("boxed_"):
          found_files.append(file)
          if len(found_files)==3:
            break
    except: 
      err = 'no files available'
      web_err({'http':http, 'type':xt, 'bin':err.encode('utf8')})
      return

    if len(found_files)==0:
      err = 'no files available'
      web_err({'http':http, 'type':xt, 'bin':err.encode('utf8')})
      return

    if len(found_files)==1:
      filepath=''
      filepath_buf=found_files[0]
    elif len(found_files)==2:
      filepath=''
      filepath_buf=found_files[1]
    elif len(found_files)==3:
      filepath=found_files[0]
      filepath_buf=found_files[1]

    # Check if convert to jpeg
    file_type='png'
    pinp=os.path.join(cur_dir, filepath_buf)

    if jpeg=='yes':
      quality=ii.get('jpeg_quality','')
      if quality==None or quality=='': quality='70'

      pout=os.path.join(cur_dir, filepath_buf+'.jpg')

      s='convert -quality '+quality+' '+pinp+' '+pout

      ck.out('')
      ck.out('  Converting to jpeg: '+s)

      os.system(s)

      pinp=pout
      filepath_buf+='.jpg'
      file_type='jpg'

    # First file will be deleted (only if 2 afterwards), second served
    ck.out('  Loading file '+ filepath_buf)
    r=ck.load_text_file({'text_file':pinp, 'keep_as_bin':'yes'})

    if jpeg=='yes':
      if os.path.isfile(pinp):
        os.remove(pinp)

    # Remove first
    if filepath!='':
      ck.out('  Trying to delete file '+ filepath)
      x=os.path.join(cur_dir, filepath)
      if os.path.isfile(x):
        os.remove(x)

    # Then finish checking previous one
    if r['return']>0:
      bout=r['error'].encode('utf-8')
    else:
      bout=r['bin']

    web_out({'http':http, 'type':file_type, 'bin':bout})

    return
  
  #############################################################################################################3
  elif act=='process_webcam':

    data_id=ii['data_id']
    program_name=ii['program_name']

    ck_entry=program_name.split(':')

    # Find solution
    r=ck.access({'action':'load',
                 'module_uoa':'solution',
                 'data_uoa':data_id})
    if r['return']>0:
      # Process error properly
      web_err({'http':http, 'type':xt, 'bin':r['error'].encode('utf8')})
      return

    pp=r['path'] # Path to solution!

    meta=r['dict']

    # Find workflow output path
    workflow_input_dir=meta.get('workflow_input_dir','')
    workflow_output_dir=meta.get('workflow_output_dir','')
    workflow_repo=meta.get('workflow_repo_url','')

    j=workflow_repo.rfind('/')
    if j>0:
      workflow_repo=workflow_repo[j+1:]

    workflow_dir=os.path.join(pp, 'CK', workflow_repo, ck_entry[0], ck_entry[1])

    if workflow_input_dir!='':
      p=os.path.join(workflow_dir, workflow_input_dir)
    else:
      p = os.path.join(workflow_dir, "tmp", "input") 

    if not os.path.isdir(p):  os.makedirs(p)

    if workflow_output_dir!='':
      pout=os.path.join(workflow_dir, workflow_output_dir)
    else:
      pout=os.path.join(workflow_dir, "tmp")

    if not os.path.isdir(pout):  os.makedirs(pout)

    # Record image
    image_uri=xpost.get('image_uri','')

    x='data:image/jpeg;base64,'
    if image_uri.startswith(x):
      image64=image_uri[len(x):]

    # Finding last file and incrementing
    ff='cr-stream-'

    l=os.listdir(p)

    inum=0
    ffound=''
    for f in os.listdir(p):
      if f.startswith(ff) and f.endswith('.jpg'):
        j=f.find('.')
        num=f[len(ff):j]
        if int(num)>inum:
          inum=int(num)
          ffound=f

    # New logic: if file already exists, just skip next request from web (otherwise many parallel requests)
    # When program starts, it should clean input/output to let this code continue processing image
    if (inum>0):
      time.sleep(1)
      ss='request skipped because there is already file in queue'
      ck.out('  Warning: '+ss+' ('+os.path.join(p,ffound)+') ...')
      s='{"return":16, "error":"'+ss+'"}'
      web_out({'http':http, 'type':'json', 'bin':s.encode('utf8')})
      return

    # Otherwise continue processing ...
    if inum==0:
      inum+=1
      sinum=str(inum)
      filename = ff+('0'*(8-len(sinum)))+sinum

      filename2=filename+'.jpg'
      pf=os.path.join(p, filename2)

      r=ck.convert_upload_string_to_file({'file_content_base64':image64, 'filename':pf})
      if r['return']>0: return r

      ck.out('  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      ck.out('  Recorded external image to '+pf)

      # Need extra converting
      pp1=os.path.join(pp, 'support-script-convert.sh')
      if os.path.isfile(pp1):
        ck.out('')
        ck.out('Extra image processing ...')
        ck.out('')

        extra_cmd='cd "'+p+'"\n'
        extra_cmd+='. "'+pp1+'" '+filename2+'\n'

        r=solution.run({'uid':data_id, 'cmd':extra_cmd})
        if r['return']>0:
          # Process error properly
          web_err({'http':http, 'type':xt, 'bin':r['error'].encode('utf8')})
          return

    else:
      sinum=str(inum)
      filename = ff+('0'*(8-len(sinum)))+sinum

      filename2=filename+'.jpg'
      pf=os.path.join(p, filename2)

    # Need extra pushing
    pp1=os.path.join(pp, 'support-script-push.sh')
    if os.path.isfile(pp1):
      ck.out('')
      ck.out('Extra image pushing to device ...')
      ck.out('')

      extra_cmd='cd "'+p+'"\n'
      extra_cmd+='. "'+pp1+'" '+filename+'\n'

      r=solution.run({'uid':data_id, 'cmd':extra_cmd})
      if r['return']>0:
        # Process error properly
        web_err({'http':http, 'type':xt, 'bin':r['error'].encode('utf8')})
        return

    # If Android-like device wait for the file ...
    ppull=os.path.join(pp, 'support-script-pull.sh')

    # Waiting for output file
    poutf=os.path.join(pout, filename +'.json')

    if not os.path.isfile(poutf):
      ck.out ('Waiting for output file: '+poutf)

    while not os.path.isfile(poutf):
      # Check if need to pull
      if os.path.isfile(ppull):
        ck.out('Trying to pull from device ...')

        extra_cmd='cd "'+pout+'"\n'
        extra_cmd+='export SOLUTION_PATH="'+pp+'"\n'
        extra_cmd+='export CR_SOLUTION_PATH="'+pp+'"\n'
        extra_cmd+='export CODEREEF_SOLUTION_PATH="'+pp+'"\n' # Keeping for compatibility with older version
        extra_cmd+='. "'+ppull+'" '+filename+'\n'

        r=solution.run({'uid':data_id, 'cmd':extra_cmd})
        if r['return']>0:
          # Process error properly
          web_err({'http':http, 'type':xt, 'bin':r['error'].encode('utf8')})
          return

      time.sleep(0.1)

    ck.out('')
    ck.out('Found solution!')
    ck.out('')

    with open(poutf) as json_file:
      solution = json.load(json_file)
      ck.out(json.dumps(solution, indent=2))

    if os.path.isfile(poutf):
      os.remove(poutf)

    if inum==1 and os.path.isfile(pf):
      ck.out('  REMOVING '+pf)
      os.remove(pf)

    ck.out('')

    s=json.dumps(solution, indent=4, sort_keys=True)
    web_out({'http':http, 'type':'json', 'bin':s.encode('utf8')})

    return

  #############################################################################################################3
  elif act=='get_image':
    num=ii.get('num','')
    inum=int(num)
    sinum=str(inum)

    # Finding last file and incrementing
    ff='cr-stream-'
    pf=os.path.join(p, ff+('0'*(8-len(sinum)))+sinum+'.jpg')

    ck.out('  Loaded file '+pf)

    r=ck.load_text_file({'text_file':pf, 'keep_as_bin':'yes'})
    if r['return']>0:
      bout=r['error'].encode('utf-8')
    else:
      bout=r['bin']

    web_out({'http':http, 'type':'jpeg', 'bin':bout})

    return

  #############################################################################################################3
  elif act=='get_result':

    data_id=ii['data_id']

    # Find solution
    r=ck.access({'action':'load',
                 'module_uoa':'solution',
                 'data_uoa':data_id})
    if r['return']>0:
      # Process error properly
      web_err({'http':http, 'type':xt, 'bin':r['error'].encode('utf8')})
      return

    pp=r['path'] # Path to solution!

    meta=r['dict']

    program_name = meta.get('workflow','')
    ck_entry=program_name.split(':')

    # Find workflow output path
    result_file=meta.get('result_file','')
    workflow_repo=meta.get('workflow_repo_url','')

    j=workflow_repo.rfind('/')
    if j>0:
      workflow_repo=workflow_repo[j+1:]

    workflow_dir=os.path.join(pp, 'CK', workflow_repo, ck_entry[0], ck_entry[1])

    if result_file!='':
      pout=os.path.join(workflow_dir, result_file)
    else:
      pout=os.path.join(workflow_dir, "tmp","tmp-ck-timer.json")

    # if not os.path.isdir(pout):  os.makedirs(pout)


    # If Android-like device wait for the file ...
    ppull=os.path.join(pp, 'support-script-pull.sh')

    # Waiting for output file
    if not os.path.isfile(pout):
      ck.out ('Waiting for output file: '+pout)

    while not os.path.isfile(pout):
      # Check if need to pull
      if os.path.isfile(ppull):
        ck.out('Trying to pull from device ...')

        extra_cmd='cd "'+pout+'"\n'
        extra_cmd+='export SOLUTION_PATH="'+pp+'"\n'
        extra_cmd+='export CR_SOLUTION_PATH="'+pp+'"\n'
        extra_cmd+='export CODEREEF_SOLUTION_PATH="'+pp+'"\n' # Keeping for compatibility with older version
        extra_cmd+='. "'+ppull+'" '+filename+'\n'

        r=solution.run({'uid':data_id, 'cmd':extra_cmd})
        if r['return']>0:
          # Process error properly
          web_err({'http':http, 'type':xt, 'bin':r['error'].encode('utf8')})
          return

      time.sleep(0.1)

    ck.out('')
    ck.out('Found solution!')
    ck.out('')

    rx=ck.load_json_file({'json_file':pout})
    if rx['return']>0: return rx

    rx=ck.flatten_dict(rx)
    if rx['return']>0: return rx

    rdf=rx['dict']
    crdf={}

    # Remove first ## (do not need here)
    for k in rdf:
      v=rdf[k]
      if k.startswith('##'): k=k[2:]
      crdf[k]=v
    ck.out(json.dumps(crdf, indent=2))

    # if os.path.isfile(pout):
    #   os.remove(pout)

    # if inum==1 and os.path.isfile(pf):
      # ck.out('  REMOVING '+pf)
      # os.remove(pf)

    ck.out('')

    s=json.dumps(crdf, indent=4, sort_keys=True)
    web_out({'http':http, 'type':'json', 'bin':s.encode('utf8')})

    return

  elif act=='get_status':
    data_id=ii['data_id']

    # Find solution
    r=ck.access({'action':'load',
                 'module_uoa':'solution',
                 'data_uoa':data_id})
    if r['return']>0:
      # Process error properly
      web_err({'http':http, 'type':xt, 'bin':r['error'].encode('utf8')})
      return

    pp=r['path'] # Path to solution!
    tmp_solStatus=os.path.join(pp, "tmp", "status.json")

    rx=ck.load_json_file({'json_file':tmp_solStatus})
    if rx['return']>0: return rx

    if not get_status_started:
       ck.out(json.dumps(rx, indent=2))

    rdf=rx['dict']

    if not get_status_started:
       ck.out('')

    s=json.dumps(rdf, indent=4, sort_keys=True)
    web_out({'http':http, 'type':'json', 'bin':s.encode('utf8')})

    get_status_started=True

    return

  #############################################################################################################3
  elif act=='heartbit':

    locdir = os.path.dirname(os.path.realpath(__file__))
    if not heartbit_started:
       ck.out('  Local directory: '+locdir)

    # Finding last file and incrementing
    pf=os.path.join(locdir, 'static/favicon.ico')

    if not heartbit_started:
       ck.out('  Loaded file '+pf)

    heartbit_started=True

    r=ck.load_text_file({'text_file':pf, 'keep_as_bin':'yes'})
    if r['return']>0:
      bout=r['error'].encode('utf-8')
    else:
      bout=r['bin']

    web_out({'http':http, 'type':'jpeg', 'bin':bout})

    return


    r={'return':0}
    xt='web'
    bout=b'TEST WORKS'

    web_out({'http':http, 'type':xt, 'bin':bout})
    return 

    # Process output
    if r['return']>0:
      if os.path.isfile(fn): os.remove(fn)

      bout=r['error']

      try: bout=bout.encode('utf-8')
      except Exception as e: pass

      web_err({'http':http,
                'type':xt,
                'bin':bout})
      return

    # If json or web
    # Try to load output file
    if not os.path.isfile(fn):
      web_err({'http':http,
                'type':xt,
                'bin':b'Output file was not created, see output ('+r['std'].encode('utf8')+b')!'})
      return

    r=ck.load_text_file({'text_file':fn, 'keep_as_bin':'yes'})
    if r['return']>0:
      bout=r['error']

      try: bout=bout.encode('utf-8')
      except Exception as e: pass

      web_err({'http':http, 'type':xt, 'bin':bout})

      return

    bin=r['bin']

    # Process JSON output from file
    fx=''

    if sys.version_info[0]>2: bin=bin.decode('utf-8')

    ru=ck.convert_json_str_to_dict({'str':bin, 'skip_quote_replacement':'yes'})
    if ru['return']>0:
      bout=ru['error']

      try: bout=bout.encode('utf-8')
      except Exception as e: pass

      web_err({'http':http, 'type':xt, 'bin':bout})

      return

    rr=ru['dict']
    if rr['return']>0:
      bout=rr['error']

      try: bout=bout.encode('utf-8')
      except Exception as e: pass

      web_err({'http':http, 'type':xt, 'bin':bout})
      return

    # Check if file was returned
    fr=False

    if 'file_content_base64' in rr and rr.get('filename','')!='':
      fr=True

    # Check if download
    if (xt=='web' and fr) or (act=='pull' and xt!='json'):
      import base64
      x=rr.get('file_content_base64','')

      fx=rr.get('filename','')
      if fx=='': fx=ck.cfg['default_archive_name']

      # Fixing Python bug
      if sys.version_info[0]==3 and sys.version_info[1]<3:
          x=x.encode('utf-8')
      else:
          x=str(x)
      bin=base64.urlsafe_b64decode(x) # convert from unicode to str since base64 works on strings
                                            # should be safe in Python 2.x and 3.x

      # Process extension
      fn1, fne = os.path.splitext(fx)
      if fne.startswith('.'): fne=fne[1:]
      if fne!='': xt=fne
      else: xt='unknown'
    else:
      # Check and output html
      if rr.get('html','')!='':
        bin=rr['html'].encode('utf-8')
      else:
        if sys.version_info[0]>2: # Unknown output
          bin=bin.encode('utf-8')

    web_out({'http':http, 'type':xt, 'bin':bin, 'filename':fx})

    return {'return':0}

##############################################################################
# Tunnel functionality

def process_web_request_post_via_tunnel(i):

    http=i['http']
    post=(i.get('post','')=='yes')

    target_url=tunnel_url+http.path

    ck.out('* Tunneling **************************************************************')

    try:

      if post:
        post_body = http.rfile.read(int(http.headers.get_all('content-length', 0)[0]))

      parsed_headers={}
      for h in http.headers:
        parsed_headers[h]=http.headers[h]

      if post: receive = requests.post(target_url, headers=parsed_headers, verify=False, data=post_body, )
      else:    receive = requests.get (target_url, headers=parsed_headers, verify=False)

      http.send_response(receive.status_code)

      received_headers = receive.headers
      for h in received_headers:
        h1=h.lower()
        if '-encoding' not in h1 and h1!='content-length': http.send_header(h, received_headers[h])

      http.send_header('Content-Length', len(receive.content))
      http.end_headers()

      http.wfile.write(receive.content)

    except Exception as e:
      print ('Error: '+format(e))
      http.send_error(500, 'problem accessing remote host')

    return

##############################################################################
# Class to handle web service requests

class server_handler(BaseHTTPRequestHandler):

    """
    Input:  Python http handler
    Output: None
    """

    # Process only GET
    def do_GET(self):
      if tunnel_url!='': process_web_request_post_via_tunnel({'http':self})
      else: process_web_request({'http':self})
      return

    # Process GET and POST
    def do_POST(self):
      if tunnel_url!='': process_web_request_post_via_tunnel({'http':self, 'post':'yes'})
      else: process_web_request({'http':self})
      return

    def log_request(self, code='-', size='-'):
      self.log_message('"%s" %s %s', self.requestline, str(code), str(size))
      return

    def log_error(self, format, *args):
      self.log_message(format, *args)
      return

###########################################################################
# Start web service

def start(i):
    global tunnel_url

    # Check tunnel URL
    tunnel=i.get('tunnel','')
    if tunnel!=None and tunnel!='': 
      tunnel_url=tunnel

      ck.out('All web requests will be tunneled to '+tunnel_url)

    host=i.get('host')
    if host=='' or host==None: host='localhost'

    port=i.get('port')
    if port=='' or port==None: port='4444'

    # Assemble URL.
    url=host+':'+port

    ck.out('Starting web service for the client on '+url+' ...')
    ck.out('')

    sys.stdout.flush()

    # We do not need secure HTTPS connection here since the user 
    # runs webbrowser on her/his machine and communicates with
    # the CB service on the same machine via 127.0.0.1 
    # while avoiding Internet!

    # Still it's possible to start this service with SSL
    # but it will require a propoer SSL certificate
    # otherwise the connection will not be validated
    # if it's purely local ...

    # Get certificates for SSL
    # ssl_certificate_file = {path to client.pem}

    # Generate it using "openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes"

    try:
      server = ThreadedHTTPServer((host, int(port)), server_handler)

#       Needed for SSL connection (non-SSL connection will not work then)
#       server.socket = ssl.wrap_socket (server.socket, server_side=True,
#                                       certfile=ssl_certificate_file)

      # Prevent issues with socket reuse
      server.allow_reuse_address=True

      server.serve_forever()
    except KeyboardInterrupt:
      ck.out('Keyboard interrupt, terminating web service ...')
      server.socket.close()
      return 1
    except OSError as e:
      ck.out('Internal web service error ('+format(e)+')')
      return 1

    return 0
