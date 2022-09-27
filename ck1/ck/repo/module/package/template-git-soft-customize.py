#
# Automatically generated
#

import os

##############################################################################
# setup environment

def setup(i):

    s=''

    cus=i['customize']
    env=i['env']

    fp=cus.get('full_path','')

    ep=cus.get('env_prefix','')

    if ep=='':
        return {'return':1, 'error':'environment prefix is not defined'}

    if fp=='':
        return {'return':1, 'error':''}

    # p1=os.path.dirname(fp)

    env[ep]=os.path.join(fp, 'src')
    
    # You can extend environent variables for your soft here:
    # env[ep+'_EXTENSION']=xyz

    return {'return':0, 'bat':s}
