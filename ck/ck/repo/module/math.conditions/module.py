#
# Collective Knowledge (check conditions)
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
# check conditions

def check(i):
    """
    Input:  {
              original_points - dict with original points
              new_points      - dict with new points
              results         - results for all points (from experiment)
              conditions      - list of conditions
              (middle_key)    - add this to keys in conditions (min, exp, mean, etc)
            }

    Output: {
              return           - return code =  0, if successful
                                             >  0, if error
              (error)          - error text if return > 0

              good_points      - list of good points
              points_to_delete - list of new points to delete

              keys             - list of checked keys
            }

    """

    o=i.get('out','')

    points1=i.get('original_points',[])
    points2=i['new_points']
    cc=i['conditions']
    results=i['results']

    mk=i.get('middle_key','')
    if mk=='': mk='#min'

    new=False
    points=[]  # good points (with correct conditions)
    dpoints=[] # points to delete if do not match conditions

    # Check keys
    keys=[]
    for c in cc:
        if len(c)!=4:
           import json
           return {'return':1, 'error':'condition length !=4 ('+json.dumps(c)+')'}

        kt=(c[0]+c[1]).replace('$#objective#$',mk)
        if kt not in keys:
           keys.append(kt)

    if o=='con':
       ck.out('')

    # Check conditions
    for q in points2:
        if q not in points1:
           # Find point in results
           qq={}
           for k in results:
               if k.get('point_uid','')==q:
                  qq=k
                  break

           if len(qq)>0:
              fine=True
              # Go over conditions

              for c in cc:
                  kt=(c[0]+c[1]).replace('$#objective#$',mk)

                  if kt not in keys:
                     keys.append(kt)

                  x=c[2]
                  y=c[3]

                  behavior=qq.get('flat',{})

                  dv=behavior.get(kt,None)

                  s='         - Condition on "'+kt+' '+str(x)+' '+str(y)+'" : '

                  if dv==None:
                     fine=False

                  if fine and x=='<' and dv>=y:
                     fine=False

                  if fine and (x=='<=' or x=='=<') and dv>y:
                     fine=False

                  if fine and x=='==' and dv!=y:
                     fine=False

                  if fine and x=='!=' and dv==y:
                     fine=False

                  if fine and x=='>' and dv<=y:
                     fine=False

                  if fine and (x=='>=' or x=='=>') and dv<y:
                     fine=False

                  if o=='con':
                     if fine:
                        s+='ok'
                     else:
                        s+='FAILED'

                     s+=' ('+str(dv)+')'
                     ck.out(s)

                  if not fine:
                     break

              if fine:
                 points.append(q)
              else:
                 dpoints.append(q)

    return {'return':0, 'good_points':points, 'points_to_delete':dpoints, 'keys':keys}
