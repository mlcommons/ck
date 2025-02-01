def check_return(r):
    if 'return' not in r:
        raise Exception(
            'CM access function should always return key \'return\'!')
    if 'error' in r:
        raise Exception(r['error'])


def check_list(r, string, found=True):
    check_return(r)
    if 'list' not in r:
        raise Exception('CM search should return a list!')
    if len(r['list']) < 1 and found:
        raise Exception('CM search returned an empty list for ' + string)
    if len(r['list']) > 0 and not found:
        raise Exception('CM search returned at lease one entry for ' + string)


def check_key_value(d, key, value, absent_ok=False):
    if not d.get(key):
        if absent_ok:
            return True
        else:
            raise Exception(f"{key} is missing. Current values are {d}")
    elif d[key] != value:
        raise Exception(
            f"{key} is not having the expected value of {value}. Current value is {d[key]}")
