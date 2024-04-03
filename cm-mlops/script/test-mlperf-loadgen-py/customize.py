from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']
    env = i['env']
    meta = i['meta']

    print ("********************************************************")
    print ('- Importing CM library ...')
    import cmind as cm
    print ('  SUCCESS!')

    print ('')
    print ('- List CM repos ...')
    print ('')
    r = cm.access({'action':'ls', 'automation':'repo', 'out':'con'})
    print ('')
    print ('  SUCCESS!')
    print ("********************************************************")


    return {'return':0}


def postprocess(i):

    env = i['env']
    state = i['state']

    return {'return':0}
