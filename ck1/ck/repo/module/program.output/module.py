#
# Collective Knowledge (check program output)
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
# check numerical program output with threshold

def check_numerical(i):
    """
    Input:  {
              file1 - file1 to check
                or
              dict1

              file2 - file2 to check
                or
              dict2

              (abs_threshold) - 0 by default
            }

    Output: {
              return        - return code =  0, if successful
                                          >  0, if error
              (error)       - error text if return > 0

              failed        - if True, failed
              fail_reason   - failure reason
            }

    """

    abs_threshold=i.get('abs_threshold','')
    if abs_threshold=='': abs_threshold='0.0'
    abs_threshold=float(abs_threshold)

    dict1={}

    file1=i.get('file1','')
    if file1!='':
       r=ck.load_json_file({'json_file':file1})
       if r['return']>0: return r
       dict1=r['dict']

    if len(dict1)==0:
       return {'return':1, 'error':'dict1 to compare is empty'}

    dict2={}
    file2=i.get('file2','')
    if file2!='':
       r=ck.load_json_file({'json_file':file2})
       if r['return']>0: return r
       dict2=r['dict']

    if len(dict2)==0:
       return {'return':1, 'error':'dict2 to compare is empty'}

    # For now expect that list - later can extend it
    if type(dict1)!=list:
       return {'return':1, 'error':'non lists are not supported yet - TBD!'}

    l1=len(dict1)
    l2=len(dict2)

    if l1!=l2:
       return {'return':0, 'failed':True, 'fail_reason':'different length of numerical outputs ('+str(l1)+' vs '+str(l2)+')'}

    err=''
    for k in range(0, l1):
        v1=dict1[k]
        v2=dict2[k]

        dv=abs(v1-v2)

        if dv>abs_threshold:
           err+=str(k)+') '+str(v1)+' vs '+str(v2)+'\n'

    if err!='':
       return {'return':0, 'failed':True, 'fail_reason':'Numerical outputs differ:\n'+err}

    return {'return':0, 'failed':False}
