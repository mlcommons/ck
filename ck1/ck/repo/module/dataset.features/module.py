#
# Collective Knowledge (dataset features)
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
# extract dataset features

def extract(i):
    """
    Input:  {
              (repo_uoa)        - repository UOA
              (data_uoa)        - dataset UOA (can be wildcards)

              (tags)            - tags to process specific datasets

              (target_repo_uoa) - repo, where to save features - if =='', use repo_uoa


            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              dict         - final dict with key 'features'={...} 
            }

    """

    import os
    import json

    o=i.get('out','')

    muoa=cfg['module_deps']['dataset']
    duoa=i.get('data_uoa','')
    ruoa=i.get('repo_uoa','')

    truoa=i.get('target_repo_uoa','')
    if truoa=='' and ruoa!='': truoa=ruoa

    tags=i.get('tags','')

    rx=ck.access({'action':'search',
                  'repo_uoa':ruoa,
                  'module_uoa':muoa,
                  'data_uoa':duoa,
                  'tags':tags})
    if rx['return']>0: return rx

    lst=rx['lst']

    feat1={}

    for q in lst:
        duid=q['data_uid']
        duoa=q['data_uoa']

        if o=='con':
           ck.out('Processing '+duoa+' ...')

        rx=ck.access({'action':'load',
                      'module_uoa':muoa,
                      'data_uoa':duoa})
        if rx['return']>0: return rx

        d=rx['dict']
        p=rx['path']

        df=d.get('dataset_files','')
        dt=d.get('tags','')

        feat={}

        otags=d.get('tags',[])

        ddd={'tags':otags, 'dataset_uid':duid, 'dataset_uoa':duoa}

        ts=0
        for f in df:
            p1=os.path.join(p,f)
            if os.path.isfile(p1):
               ts+=os.path.getsize(p1)

        if ts!=0: feat['total_size']=ts

        if 'image' in dt:
           if o=='con':
              ck.out('  Image detected.')

              for f in df:
                  p1=os.path.join(p,f)
                  if os.path.isfile(p1):
                     try:
                       from PIL import Image
                       im = Image.open(p1)

                       feat['mode']=str(im.mode)
                       feat['format']=str(im.format)
                       feat['width']=im.size[0]
                       feat['height']=im.size[1]

                       inf=im.info
                       feat['compression']=inf.get('compression','')
                       dpi=inf.get('dpi',[])
                       if len(dpi)>1:
                          feat['xdpi']=dpi[0]
                          feat['ydpi']=dpi[1]
                       
                       feat['raw_info']=im.info
                     except Exception as e: 
                        pass

        if len(feat)>0:
           rr=ck.dumps_json({'dict':feat, 'sort_keys':'yes', 'skip_indent':'yes'})
           if rr['return']>0: 
              if 'raw_info' in feat: # Usually source of problems
                 del(feat['raw_info'])
                 rr=ck.dumps_json({'dict':feat, 'sort_keys':'yes', 'skip_indent':'yes'})
                 if rr['return']>0: return rr
              else:
                 return rr

           sfeat=rr['string']
           ck.out('  '+sfeat)

           found=False
           ry=ck.access({'action':'load',
                         'module_uoa':work['self_module_uid'],
                         'data_uoa':duid})
           if ry['return']==0: 
              ddd=ry['dict']              
              found=True

           feat1=ddd.get('features',{})
           rz=ck.merge_dicts({'dict1':feat1, 'dict2':feat})
           if rz['return']>0: return rz
           feat1=rz['dict1']

           ddd['features']=feat1
           ddd['tags']=otags

           ii={}
           ii['action']='add'
           if found: ii['action']='update'
           ii['module_uoa']=work['self_module_uid']
           ii['data_uoa']=duoa
           ii['data_uid']=duid
           ii['repo_uoa']=truoa
           ii['dict']=ddd
           ii['substitute']='yes'
           ry=ck.access(ii)
           if ry['return']>0: return ry

    return {'return':0, 'dict':{'features':feat1}}

##############################################################################
# converting raw RGB image to png or other formats

def convert_raw_rgb_image(i):
    """
    Input:  {
              input_file    - input raw RGB file
              output_file   - output file
              width         - image width
              height        - image height
              (mode)        - mode: RGB (default), RGBA, ...
              (output_type) - type of output file: PNG (default), JPEG ...
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    fi=i['input_file']
    fo=i['output_file']

    w=int(i['width'])
    h=int(i['height'])

    ot=i.get('output_type','')
    if ot=='': ot='png'

    mode=i.get('mode','')
    if mode=='': mode='RGB'

    # Load binary file
    r=ck.load_text_file({'text_file':fi, 'keep_as_bin':'yes'})
    if r['return']>0: return r

    bin=r['bin']

    # Create image
    from PIL import Image

    im = Image.frombuffer(mode, (w,h), bin, "raw", mode, 0, 1)

    im.save(fo, ot)

    return {'return':0}
