#
# Collective Knowledge (experiment participants and their stats)
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
# show users

def show(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              html         - generated HTML
            }

    """

    import os

    h='<center>'
    h+='<h2>Collective Knowledge Timeline<BR>(non-anonymous participation in collaborative experiments)</h2>\n'

    uu=[]

    # Load all
    rx=ck.access({'action':'load',
                  'module_uoa':work['self_module_uid'],
                  'data_uoa':'all'})
    if rx['return']>0:
       if rx['return']!=16:
          return rx
       else:
          h+='<b>Timeline is empty ...</b>'
    else:
       d=rx['dict']

       du=d.get('users',{})
       dt=d.get('timeline',[])

       for q in dt:
           user=q.get('user','')
           if user!='' and user not in uu:
              uu.append(user)

       unique_users=len(uu)

       h+='<i>Number of unique users: '+str(unique_users)+'</i><br><br>\n'

       # Check host URL prefix and default module/action
       rx=ck.access({'action':'form_url_prefix',
                     'module_uoa':'wfe',
                     'host':i.get('host',''), 
                     'port':i.get('port',''), 
                     'template':i.get('template','')})
       if rx['return']>0: return rx
       url0=rx['url']

       xdt=sorted(dt, key=lambda v: (v.get('iso_datetime','')))

       h+='<center>\n'
       h+='<table class="ck_table" border="0" cellpadding="5">\n'

       h+=' <tr style="background-color:#cfcfff;">\n'
       h+='  <td><b>\n'
       h+='   Date / time\n'
       h+='  </b></td>\n'

       h+='  <td><b>\n'
       h+='   User\n'
       h+='  </b></td>\n'

       h+='  <td align="center"><b>\n'
       h+='   Action\n'
       h+='  </b></td>\n'

       h+='  <td align="center"><b>\n'
       h+='   Scenario\n'
       h+='  </b></td>\n'

       h+=' </tr>\n'

       for q in dt:
           idt=q.get('iso_datetime','')
           nu=q.get('new_user','')
           user=q.get('user','')
           tp=q.get('type','')

           ix=user.find('@')
           if ix>1:
              user=user[:ix-1]+'{HiddenForPrivacy}'+user[ix+2:]

           a=''
           if nu=='yes': a='New user'
           else:
              suid=q.get('solution_uid','')
              scenario_uoa=q.get('scenario_uoa','')
              duoa=q.get('data_uoa','')

              a='<a href="'+url0+'wcid='+scenario_uoa+':'+duoa+'">Better solution found (UID='+suid+')</a>'

           h+='<tr>'

           h+=' <td align="left">'+idt.replace('T',' ')+'</td>'
           h+=' <td align="left">'+user+'</td>'
           h+=' <td align="left">'+a+'</td>'
           h+=' <td align="left">'+tp+'</td>'

           h+='</tr>'

       h+='</table>\n'

       h+='</center>\n'

    return {'return':0, 'html':h}
