#
# Collective Knowledge (caffe CK front-end)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: cTuning foundation, admin@cTuning.org, http://cTuning.org
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
# crowd-benchmark caffe

def crowdbench(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    i['action']='crowdsource'
    i['module_uoa']=cfg['module_deps']['experiment.bench.caffe']

    return ck.access(i)

##############################################################################
# TBD: classification demo using webcam + benchmarking/tuning via CK

def demo(i):
    """
    Input:  {
               (camera_id) - camera ID
               (delay)     - delay
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    # Deps
    import time
    import cv2
    import os

    # Prepare tmp entry if doesn't exist
    duoa=cfg['demo']['data_uoa']
    image_name=cfg['demo']['image_name']

    r=ck.access({'action':'load',
                 'module_uoa':cfg['module_deps']['tmp'],
                 'data_uoa':duoa})
    if r['return']>0:
        if r['return']!=16: return r

        r=ck.access({'action':'add',
                     'module_uoa':cfg['module_deps']['tmp'],
                     'data_uoa':duoa})
        if r['return']>0: return r

    p=r['path']

    pf=os.path.join(p, image_name)

    # Initialize web cam
    ci=int(i.get('camera_id',0))
    dl=int(i.get('delay',1))

    wcam = cv2.VideoCapture(ci)

    # Permanent loop
    while True:
       ck.out('Obtaining picture from webcam ...')

       s, img = wcam.read()

       if s:    # frame captured without any errors
#           cv2.namedWindow("cam-test")
#           cv2.imshow("cam-test",img)
#           destroyWindow("cam-test")

           cv2.imwrite(pf,img)

       time.sleep(dl)

    return {'return':0}

##############################################################################
# autotune Caffe workloads

def autotune(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    i['module_uoa']=cfg['module_deps']['program']
    i['data_uoa']='caffe'
    i['explore']='yes'
    i['extra_tags']='dnn'
    i['skip_collaborative']='yes'
    i['skip_pruning']='yes'
    i['iterations']=-1
    i['new']='yes'
    i['cmd_keys']=['time_cpu','time_gpu']

    return ck.access(i)
