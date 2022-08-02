try:
    import cmind as cm

    r = cm.access(['test', 'script'])
    if 'return' not in r:
        raise Exception('CM access function should always return key \'return\'!')
    exit(0)

except ImportError as e:
    from sys import stderr
    from subprocess import call
    print('WARNING: CM module for python is not installed & jupyter notebooks will not be supported', file=stderr)
    retcode = call(['cm', 'test', 'script'])
    exit(retcode)
