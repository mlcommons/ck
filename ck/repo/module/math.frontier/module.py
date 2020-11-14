#
# Collective Knowledge (detect frontier for multi-objective optimizations (such as execution time vs energy vs code size vs faults vs price ...))
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
# Filter frontier (leave only best points) - my own greedy and probably not very optimal algorithm
#
# TBD: should leave only a few points otherwise can be quickly too many 
#  particularly if more than 2 dimensions (performance, energy, size, faults)
#
# Note, that we minimize all dimensions. Otherwise, provide reversed dimension.
#
# HELP IS APPRECIATED!

def filter(i):
    """
    Input:  {
              points          - dict with points, each has dict with optimization dimensions (should have the same names)
                              
              (frontier_keys) - list of keys to leave only best points during multi-objective autotuning
                                 (multi-objective optimization)
                                If omited, use all keys

              (reverse_keys)  - list of values associated with above keys. If True, reverse sorting for a give key
                                (by default descending) - can't be used without "frontier_keys" due to lack of order in python dicts2

              (margins)        - list of margins when comparing values, i.e. Vold/Vnew < this number (such as 1.10 instead of 1).
                                 will be used if !=None  
            }

    Output: {
              return         - return code =  0, if successful
                                           >  0, if error
              (error)        - error text if return > 0

              points         - filtered points!
              deleted_points - deleted points
            }

    """

    oo=i.get('out','')

    points=i['points']
    lp=len(points)

    dpoints={}

    uids=list(points.keys())

    if oo=='con':
       ck.out('Original number of points:        '+str(lp))

    fk=i.get('frontier_keys',[])
    fkr=i.get('reverse_keys',[])
    lrk=len(fkr)

    mar=i.get('margins',[])
    lmar=len(mar)

    if lp>1:
       for l0 in range(0,lp,1):
           ul0=uids[l0]
           if ul0!='':
              p0=points[ul0]
 
              # Check if there is at least one point with all better dimensions

              keep=True

              for l1 in range(0,lp,1):
                  ul1=uids[l1]
                  if ul1!='' and ul1!=ul0:
                     p1=points[ul1]

                     better=True

                     if len(fk)>0:
                        ks=fk
                     else:
                        ks=list(p0.keys())

                     for dim in range(0, len(ks)):
                         d0=ks[dim]

                         v0=p0[d0]
                         if v0!=None and v0!='':
                            v0=float(v0)

                            v1=p1.get(d0,None)
                            if v1!=None and v1!='':
                               v1=float(v1)

                               if v1==0: v1=v0/10
                               if v1==0: v1=0.01

                               m=1.0
                               if dim<lmar and mar[dim]!=None: 
                                  m=mar[dim]

                               if dim<lrk and fkr[dim]==True:
                                  if v1==0 or (v0/v1)>m:
                                     better=False
                                     break
                               elif v0==0 or (v0/v1)<m:
                                  better=False
                                  break

                     if better:
                        keep=False
                        break

              if not keep:
                 dpoints[ul0]=points[ul0]
                 del(points[ul0])
                 uids[l0]=''

    lp=len(points)
    if oo=='con':
       ck.out('Number of points after filtering: '+str(lp))

    return {'return':0, 'points':points, 'deleted_points':dpoints}
