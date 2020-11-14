#
# Collective Knowledge (web-based user auth)
#
# 
# 
#
# Developer: 
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel) 

# Local settings

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
# authentication of a user

def auth(i):
    """
    Input:  {
              (web_vars_post)
              (web_vars_get)
              (web_vars_session)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              user_id
              session_id
            }

    """

    import re
    import hashlib

    rr={'return':0}

    wvp=i.get('web_vars_post',{})

    # Check username
    username=wvp.get('username','').strip()
    if username=='':
       return {'return':1, 'error':'username is empty'}

    if not re.match("^[A-Za-z0-9.@_-]*$", username):
       return {'return':1, 'error':'username contains forbidden characters'}

    # Check password
    password=wvp.get('password','').strip()
    if password=='':
       return {'return':1, 'error':'password is empty'}

    password_md5=hashlib.md5(password.encode('utf8')).hexdigest()

    # Check if entry exists
    default_repo=ck.cfg.get('default_repo_to_write','')
    if default_repo=='': default_repo='local'

    r=ck.access({'action':'load',
                 'module_uoa':work['self_module_uid'],
                 'repo_uoa':default_repo,
                 'data_uoa':username})
    if r['return']>0: 
       if r['return']==16: return {'return':16, 'error':'Username not registered'}
       return r

    d=r['dict']

    load_password_md5=d.get('password_md5','')
    if password_md5!=load_password_md5:
       return {'return':1, 'error':'password did not match'}

    # Generate random token for the session
    r=ck.gen_uid({})
    if r['return']>0: return r

    rr['session_id']=r['data_uid']
    rr['user_id']=username

    return rr

##############################################################################
# create account

def create(i):
    """
    Input:  {
              (web_vars_post)
              (web_vars_get)
              (web_vars_session)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              user_id
              session_id
            }

    """

    import re
    import hashlib

    rr={'return':0}

    wvp=i.get('web_vars_post',{})

    # Check username
    username=wvp.get('username','').strip()
    if username=='':
       return {'return':1, 'error':'username is empty'}

    if not re.match("^[A-Za-z0-9.@_-]*$", username):
       return {'return':1, 'error':'username contains forbidden characters'}

    # Check password
    password=wvp.get('password','').strip()
    if password=='':
       return {'return':1, 'error':'password is empty'}

    password_md5=hashlib.md5(password.encode('utf8')).hexdigest()

    # Check email
    email=wvp.get('email','').strip()
    if email=='':
       return {'return':1, 'error':'email is empty'}

    realname=wvp.get('realname','').strip()

    # Check if entry exists
    default_repo=ck.cfg.get('default_repo_to_write','')
    if default_repo=='': default_repo='local'

    r=ck.access({'action':'load',
                 'module_uoa':work['self_module_uid'],
                 'repo_uoa':default_repo,
                 'data_uoa':username})
    if r['return']==0:
       return {'return':32, 'error':'Username already registered'}

    if r['return']!=16: return r

    # Create entry
    d={'password_md5':password_md5,
       'email':email,
       'realname':realname}

    r=ck.access({'action':'add',
                 'module_uoa':work['self_module_uid'],
                 'repo_uoa':default_repo,
                 'data_uoa':username,
                 'dict':d,
                 'sort_key':'yes'})
    if r['return']>0: return r

    # Generate random token for the session
    r=ck.gen_uid({})
    if r['return']>0: return r

    rr['session_id']=r['data_uid']
    rr['user_id']=username

    return rr

##############################################################################
# renew user

def renew(i):
    """
    Input:  {
              (web_vars_post)
              (web_vars_get)
              (web_vars_session)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              user_id
              session_id
            }

    """

    import re
    import hashlib

    rr={'return':0}

    wvp=i.get('web_vars_post',{})

    # Check username
    username=wvp.get('username','').strip()
    if username=='':
       return {'return':1, 'error':'username is empty'}

    if not re.match("^[A-Za-z0-9.@_-]*$", username):
       return {'return':1, 'error':'username contains forbidden characters'}

    # Load user
    default_repo=ck.cfg.get('default_repo_to_write','')
    if default_repo=='': default_repo='local'

    r=ck.access({'action':'load',
                 'module_uoa':work['self_module_uid'],
                 'repo_uoa':default_repo,
                 'data_uoa':username})
    if r['return']>0: return r

    d=r['dict']

    # Check password
    password=wvp.get('password','').strip()
    if password!='':
       password_md5=hashlib.md5(password.encode('utf8')).hexdigest()
       d['password_md5']=password_md5

    # Check email
    email=wvp.get('email','').strip()
    if email!='':
       d['email']=email

    realname=wvp.get('realname','').strip()
    if realname!='':
       d['realname']=realname

    # Update entry
    r=ck.access({'action':'update',
                 'module_uoa':work['self_module_uid'],
                 'repo_uoa':default_repo,
                 'data_uoa':username,
                 'dict':d,
                 'substitute':'yes',
                 'sort_key':'yes'})
    if r['return']>0: return r

    return {'return':0}
