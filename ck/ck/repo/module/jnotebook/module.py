#
# Collective Knowledge (Jupyter Notebook)
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
# remote output from Jupyter Notebook

def clean(i):
    """
    Input:  {
              file_in    - input jupyter notebook file
              (file_out) - output jupyter notebook file (otherwise {in}.out
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    o=i.get('out','')

    fin=i.get('file_in','')
    if fin=='':
       return {'return':1, 'error':'Usage: ck clean jnotebook --in={juypter notebook file} (--out={output file})'}

    fout=i.get('file_out','')
    if fout=='':
       fout=fin+'.out'

    r=ck.load_json_file({'json_file':fin})
    if r['return']>0: return r

    d=r['dict']

    cells=d['cells']

    for ic in range(0,len(cells)):
        c=cells[ic]
        if 'outputs' in c:
           c['outputs']=[]
        cells[ic]=c

    r=ck.save_json_to_file({'json_file':fout, 'dict':d})
    if r['return']>0: return r

    if o=='con':
       ck.out('Output file: '+fout)

    return {'return':0}

##############################################################################
# run Jupyter Notebook from a CK entry

def run(i):
    """
    Input:  {
              data_uoa     - CK Jupyter notebook entry
              (name)       - full name of file (if more than one)

              (original)   - if 'yes', do not generate tmp file
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    import os
    import shutil

    duoa=i.get('data_uoa','')
    if duoa=='':
       return {'return':1, 'error':'Usage: ck run jnotebook:{UOA} (--name={notebook filename if more than one}'}

    r=ck.access({'action':'load',
                 'module_uoa':work['self_module_uid'],
                 'data_uoa':duoa})
    if r['return']>0: return r

    p=r['path']

    name=i.get('name','')
    if name=='':
       ld=os.listdir(p)
       nbs=[]
       for f in ld:
           if f.endswith('.ipynb'):
              nbs.append(f)
       if len(nbs)==0:
          return {'return':1, 'error':'can\'t find \ipython/jupyter notebooks in the CK entry'}
       name=nbs[0]

    # Check if need tmp file or not
    ff=os.path.join(p,name)
    if i.get('original','')!='yes':
       rx=ck.gen_tmp_file({'prefix':'tmp-', 'suffix':'.ipynb', 'remove_dir':'no'})
       if rx['return']>0: return rx
       ftmp=rx['file_name']

       shutil.copy(ff, ftmp)
       ff=ftmp

    cmd='jupyter notebook '+ff
    os.system(cmd)

    return {'return':0}
