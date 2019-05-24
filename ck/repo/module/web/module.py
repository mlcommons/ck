#
# Collective Knowledge (CK web service)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel)

wfe_host=''
wfe_port=''

# Local settings
import os
import sys
import cgi
import urllib
import base64
import tempfile

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
   from SocketServer import ThreadingMixIn

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
# Access CK through CMD (can detach console)

def call_ck(i):

    """
    Input:  {
              Input for CK
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              (stdout)     - stdout, if available
              (stderr)     - stderr, if available
              (std)        - stdout+stderr
            }
    """

    import subprocess
    import re

    # Check action
    action=i.get('action','')
    if action=='':
       return {'return':1, 'error':'action is not defined'}

    # Check that no special characters, otherwise can run any command from CMD
    if not re.match('^[A-Za-z0-9-_]*$', action):
       return {'return':1, 'error':'action contains illegal characters'}

    # Generate tmp file
    fd, fn=tempfile.mkstemp(suffix='.tmp', prefix='ck-') # suffix is important - CK will delete such file!
    os.close(fd)

    dc=i.get('detach_console','')
    if dc=='yes': i['out']='con' # If detach, output as console

    # Prepare dummy output
    rr={'return':0}
    rr['stdout']=''
    rr['stderr']=''

    # Save json to temporay file
    rx=ck.save_json_to_file({'json_file':fn, 'dict':i})
    if rx['return']>0: return rx

    # Prepare command line
    cmd='ck '+action+' @'+fn
    if dc=='yes':
       # Check platform
       rx=ck.get_os_ck({})
       if rx['return']>0: return rx

       plat=rx['platform']

       dci=ck.cfg.get('detached_console',{}).get(plat,{})

       dcmd=dci.get('cmd','')
       if dcmd=='':
          return {'return':1, 'error':'detached console is requested but cmd is not defined in kernel configuration'}

       dcmd=dcmd.replace('$#cmd#$', cmd)

       if dci.get('use_create_new_console_flag','')=='yes':
          process=subprocess.Popen(dcmd, stdin=None, stdout=None, stderr=None, shell=True, close_fds=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
       else:
          # Will need to do the forking
          try:
             pid=os.fork()
          except OSError as e:
             return {'return':1, 'error':'forking detached console failed ('+format(e)+')'}

          if pid==0:
             os.setsid()

             pid=os.fork()
             if pid!=0: os._exit(0)

             try:
                 maxfd=os.sysconf("SC_OPEN_MAX")
             except (AttributeError, ValueError):
                 maxfd=1024

             for fd in range(maxfd):
                 try:
                    os.close(fd)
                 except OSError:
                    pass

             os.open('/dev/null', os.O_RDWR)
             os.dup2(0, 1)
             os.dup2(0, 2)

             # Normally child process
             process=os.system(dcmd)
             os._exit(0)

       stdout=ck.cfg.get('detached_console_html', 'Console was detached ...')
       stderr=''
    else:
       process=subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
       stdout,stderr=process.communicate()

    try: stdout=stdout.decode('utf8')
    except Exception as e: pass
    try: stderr=stderr.decode('utf8')
    except Exception as e: pass

    rr['std']=stdout+stderr
    rr['stdout']=stdout
    rr['stderr']=stderr

    return rr

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

    tpx=cfg['content_types'].get(tp,{})
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
# Process CK web service request (both GET and POST)

def process_ck_web_request(i):

    """

    Input:  {
              http - Python http object
            }

    Output: { None }
    """

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
#           xget[k]=b[k][0]
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
       bin=b'internal CK web service error [7101] ('+format(e).encode('utf8')+')'
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

    cj=ii.get('ck_json','').strip()
    if cj!='':
       r=ck.convert_json_str_to_dict({'str':cj, 'skip_quote_replacement':'yes'})
       if r['return']>0:
          bin=b'internal CK web service error [7102] ('+r['error'].encode('utf8')+b')'
          web_err({'http':http, 'type':xt, 'bin':bin})
          ck.out(ck.cfg['error']+bin.decode('utf8'))
          return

       del(ii['ck_json'])
       ii.update(r['dict'])

    # Misc parameters
    dc=ii.get('detach_console','')
    act=ii.get('action','')

    # Check output type
    if ii.get('out','')!='':
       xt=ii['out']

    if xt=='': xt='web'

    if xt!='json' and xt!='con' and xt!='web':
       web_out({'http':http,
                'type':'web',
                'bin':b'Unknown CK request ('+xt.encode('utf8')+b')!'})
       return

    # Prepare temporary output file
    fd, fn=tempfile.mkstemp(prefix='ck-')
    os.close(fd)
    os.remove(fn)

    # Check output
    if dc=='yes':
       if ck.cfg.get('forbid_detached_console','')=='yes':
          web_out({'http':http,
                   'type':'web',
                   'bin':b'Detached console is forbidden!'})
          return
    else:
       ii['out_file']=fn
       ii['web']='yes'
       if xt=='json' or xt=='web':
          ii['out']='json_file'
       # else output to console (for remote access for example)

    ii['con_encoding']='utf8'

    ii['host']=wfe_host
    ii['port']=wfe_port

    # Execute command *********************************************************
    if act=='':
       if cfg.get('if_web_action_not_defined','')!='' and cfg.get('if_web_module_not_defined','')!='':
          ii['module_uoa']=cfg['if_web_module_not_defined']
          ii['action']=cfg['if_web_action_not_defined']

    r=call_ck(ii)

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

    # If output to console or detached console
    if xt=='con' or dc=='yes':
       if os.path.isfile(fn): os.remove(fn)

       bout=r.get('std','').encode('utf8')

       web_out({'http':http, 'type':xt, 'bin':bout})

       return

    # If json or web
    # Try to load output file
    if not os.path.isfile(fn):
       web_err({'http':http,
                'type':xt,
                'bin':b'Output json file was not created, see output ('+r['std'].encode('utf8')+b')!'})
       return

    r=ck.load_text_file({'text_file':fn, 'keep_as_bin':'yes'})
    if r['return']>0:
       bout=r['error']

       try: bout=bout.encode('utf-8')
       except Exception as e: pass

       web_err({'http':http, 'type':xt, 'bin':bout})

       return

    bin=r['bin']

    if os.path.isfile(fn): os.remove(fn)

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
# Class to handle requests in separate threads

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):

    """
    """

##############################################################################
# Class to handle CK web service requests

class server_handler(BaseHTTPRequestHandler):

    """
    Input:  Python http handler
    Output: None
    """

    # Process only GET
    def do_GET(self):
        process_ck_web_request({'http':self})
        return

    # Process GET and POST
    def do_POST(self):
        process_ck_web_request({'http':self})
        return

    def log_request(self, code='-', size='-'):
        self.log_message('"%s" %s %s', self.requestline, str(code), str(size))
        return

    def log_error(self, format, *args):
        self.log_message(format, *args)
        return

##############################################################################
# start web service

def start(i):
    """

    Input:  {
              (host)        - Internal web server host
              (port)        - Internal web server port

              (wfe_host)    - External web server host
              (wfe_port)    - External web server port

              (browser)     - if 'yes', open browser
              (template)    - if !='', add template
              (wcid)         - view a given entry
                or
              (cid)
              (extra_url)   - extra URL
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    # Define internal server host.
    host=ck.cfg.get('default_host','')
    host=i.get('host',host)
    if host=='': host='localhost' # 'localhost' if ''

    # Define external server host.
    global wfe_host
    wfe_host=i.get('wfe_host',host)

    # Define internal server port.
    port=ck.cfg.get('default_port','')
    port=i.get('port',port)
    if port=='': return {'return':1, 'error':'web port is not defined'}

    # Define external server port.
    global wfe_port
    wfe_port=i.get('wfe_port',port)

    # Assemble URL.
    url=host+':'+port
    wfe_url=wfe_host+':'+wfe_port

    ck.out('Starting CK web service on '+url+' (configured for access at '+wfe_url+') ...')
    ck.out('')

    sys.stdout.flush()

    if i.get('browser','')=='yes':
       rurl='http://'+url

       ext=''

       if i.get('template','')!='':
          ext='template='+i['template']

       cid=i.get('wcid','')
       if cid=='':
          cid=i.get('cid','')

       if cid!='' and cid!='web':
          if ext!='': ext+='&'
          ext+='wcid='+cid

       if i.get('extra_url','')!='':
          if ext!='': ext+='&'
          ext+=i['extra_url']

       if ext!='':
          rurl+='/?'+ext

       import webbrowser
       webbrowser.open(rurl)

    try:
       server = ThreadedHTTPServer((host, int(port)), server_handler)
       # Prevent issues with socket reuse
       server.allow_reuse_address=True
       server.serve_forever()
    except KeyboardInterrupt:
       ck.out('Keyboard interrupt, terminating CK web service ...')
       server.socket.close()
       return {'return':0}
    except OSError as e:
       return {'return':1, 'error':'problem starting CK web service ('+format(e)+')'}

    return {'return':0}

##############################################################################
# test web

def test(i):
    """

    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    h='<B>Test CK web (with unicode)</B><BR><BR>'

    r=ck.access({'action':'load',
                 'module_uoa':'test',
                 'data_uoa':'unicode'})
    if r['return']>0: return r

    d=r['dict']

    for q in d['languages']:
        h+=q+'<BR>'

    return {'return':0, 'html':h}
