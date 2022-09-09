def check_return(r):
    if 'return' not in r:
        raise Exception('CM access function should always return key \'return\'!')
    if 'error' in r:
        raise Exception(r['error'])

def check_list(r, str):
    check_return(r)
    if 'list' not in r:
        raise Exception('CM search should return a list!')
    if len(r['list']) < 1:
        raise Exception('CM search returned an empty list for ' + str)
