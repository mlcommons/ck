#
# Collective Knowledge (analysis of variation of experimental results)
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
# analyze variation of experimental results

def analyze(i):
    """
    Input:  {
              characteristics_table - characteristics table (list)

              (bins)                - number of bins (int, default = 100)

              (min)                 - min float value (if multiple ctables are processed)
              (max)                 - max float value (if multiple ctables are processed)

              (cov_factor)          - float covariance factor (0.5 by default)

              (skip_fail)           - if 'yes', do not fail, if SciPy and NumPy
                                      are not available
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              min        - min X values from input or calculated
              max        - max X values from input or calculated  

              xlist      - list of x values
              ylist      - list of y density values 

              xlist2     - list of x values with peaks
              ylist2     - list of y density values with peaks

              xlist2s    - list of sorted x values with peaks (max y -> hence 1st expected value)
              ylist2s    - list of sorted y density values with peaks
            }

    """

    import copy

    has_deps=True
    try:
       from scipy.stats import gaussian_kde
       from scipy.signal import argrelextrema
       import numpy as np
    except Exception as e: 
       has_deps=False
       if i.get('skip_fail','')!='yes':
          return {'return':1, 'error':'Seems that some scientific python modules are not installed ('+format(e)+')'}

    ctable1=i['characteristics_table']
    ctable=copy.deepcopy(ctable1) # since slightly changing it ...

    dmin=i.get('min',-1)
    dmax=i.get('max',-1)

    xlist=[]
    ylist=[]

    xlist2=[]
    ylist2=[]

    xlist2s=[]
    ylist2s=[]


    dmin=i.get('min',-1.0)
    dmax=i.get('max',-1.0)

    if has_deps:
       if len(ctable)>0:
          xlistx=[]
          if len(ctable)>1:
             bins=i.get('bins','')
             if bins=='': bins=100
             bins=int(bins)

             if dmin==dmax:
                dmin=min(ctable)
                dmax=max(ctable)

             cf=i.get('cov_factor','')
             if cf=='': cf=0.5
             cf=float(cf)

             ctable.insert(0,0.0)
             ctable.append(0.0)

             try:
                density = gaussian_kde(ctable)
                xlist = np.linspace(dmin,dmax,bins)

                if cf!=-1 and cf!='':
                   density.covariance_factor = lambda:cf
                   density._compute_covariance()

                ylist=density(xlist)

                ylist5=[0.0]
                for q in ylist:
                    ylist5.append(q)
                ylist5.append(0.0)

                ylist6=np.array(ylist5)

                xlistx=argrelextrema(ylist6, np.greater)[0] # np.less for local minima

                xlistxx=[]
                for q in xlistx:
                    xlistxx.append(q-1)

                xlistx=xlistxx

             except Exception as e:
                x=format(e)
                if x.find('singular matrix')<0:
                   ck.out('CK warning: '+x+' in analyze math.variation ...')
                pass

          else:
             xlist=[ctable[0]]
             ylist=[100.0]
             xlistx=[0]

          # Convert from numpy to float
          for q in range(0, len(xlist)):
              xlist[q]=float(xlist[q])
              ylist[q]=float(ylist[q])

          if len(xlistx)>0:
             for q in xlistx:
                 xlist2.append(float(xlist[q]))
                 ylist2.append(float(ylist[q]))

             ylist2s, xlist2s = (list(t) for t in zip(*sorted(zip(ylist2, xlist2),reverse=True)))

    return {'return':0, 'xlist':xlist, 'ylist':ylist, 
                        'xlist2':xlist2, 'ylist2':ylist2,
                        'xlist2s':xlist2s, 'ylist2s':ylist2s}

##############################################################################
# analyze speedup (prepared by Anton Lokhmotov)

def speedup(i):
    """
    Input:  {
              samples1 - list of original empirical results
              samples2 - list of new empirical results (lower than original is better)
 
              (key1)   - prefix for min/max/mean in return dict
              (key2)   - prefix for min/max/mean in return dict
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              {key1}_min
              {key2}_min

              {key1}_max
              {key2}_max

              {key1}_mean
              {key2}_mean

              {key1}_var
              {key2}_var

              {key1}_delta
              {key2}_delta

              {key1}_center
              {key2}_center

              naive_speedup
              naive_speedup_min
              naive_speedup_var - always >= 1.0
            }

    """

    s1=i['samples1']
    s2=i['samples2']

    s1min=min(s1)
    s1max=max(s1)

    s2min=min(s2)
    s2max=max(s2)

    s1mean=float(sum(s1))/len(s1)
    s2mean=float(sum(s2))/len(s2)

    s1delta=s1max-s1min
    s2delta=s2max-s2min

    s1var=None
    if s1mean!=0: s1var=s1delta/s1mean

    s2var=None
    if s2mean!=0: s2var=s2delta/s2mean

    s1center=s1min+float(s1delta/2)
    s2center=s2min+float(s2delta/2)

    # naive speedups
    ns_mean=s1mean/s2mean
    ns_min=s1min/s2min

    # check keys
    k1=i.get('key1','')
    if k1=='': k1='s1'

    k2=i.get('key2','')
    if k2=='': k2='s2'

    # Normally we should simply not use speedup if variation of both
    # variables is too high and there is an overlap ...
    # We should also perform stat analysis, but as some metric
    # we temporally calculate best and worst possible speedup
    # (again it should be used more as hints)
    
    if ns_mean>ns_min: 
       nsv=ns_mean/ns_min
    else:
       nsv=ns_min/ns_mean

    # perform statistical analysis, if available 
    # and detect expected value(s) and confidence interval
#    import pandas as pd




    rr={'return':0, k1+'_min':s1min, k1+'_max':s1max,
                    k2+'_min':s2min, k2+'_max':s2max,
                    k1+'_mean':s1mean, k2+'_mean': s2mean,
                    k1+'_var':s1var, k2+'_var': s2var,
                    k1+'_delta':s1delta, k2+'_delta': s2delta,
                    k1+'_center':s1center, k2+'_center': s2delta,
                    'naive_speedup':ns_mean, 
                    'naive_speedup_min':ns_min,
                    'naive_speedup_var':nsv}

    return rr

##############################################################################
# calculating geometric mean

def geometric_mean(i):
    """
    Input:  {
              input - list of values
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              gmean        - geometric mean
            }

    """

    import math

    x=i['input']
    y=math.exp(sum(math.log(j) for j in x) / len(x))

    return {'return':0, 'gmean':y}

##############################################################################
# convert plus minus vars to user friendly strings and with proper rounding

def process_plus_minus(i):
    """
    Input:  {
              var_mean   - mean value
              var_range  - variation

              (force_round) - if 'yes', use it in %.(force_round)f
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              var_mean  - rounded
              var_range - rounded

              string
              html
              tex
            }

    """

    import math

    vm=i['var_mean']
    vr=i['var_range']

    round=0
    if vr<1:
       vr1=1/vr
       x=int(math.log10(vr1))+1
       round=x

       y=pow(10,int(x))

       vr2=int(vr*y)
       vr=vr2/y

       vm1=int(vm*y)
       vm=vm1/y
    else:
       x=int(math.log10(vr))
       y=pow(10,int(x))

       vr2=int(vr/y)
       vr=vr2*y

       vm1=int(vm/y)
       vm=vm1*y

    fr=i.get('force_round',None)
    if fr!=None and fr!='':
       round=fr

    ff='%.'+str(round)+'f'

    x1=ff % vm
    x2=ff % vr

    s=x1 +' +- '+ x2
    h=x1 +' &plusmn; '+ x2
    t=x1 +' $\pm$ '+ x2

    return {'return':0, 'var_mean':vr, 'var_range':vr, 'string':s, 'html':h, 'tex':t}
