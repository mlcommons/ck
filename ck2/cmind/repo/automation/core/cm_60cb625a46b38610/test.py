import cmind.utils as utils

############################################################
def uid(i, con):
    """
    Generate CM UID
    """

    r = utils.gen_uid()

    if con:
        print (r['uid'])

    return r

