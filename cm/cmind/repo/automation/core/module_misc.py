import cmind.utils as utils

############################################################
def uid(i):

    console = i.get('out') == 'con'

    r = utils.gen_uid()

    if console:
        print (r['uid'])

    return r
