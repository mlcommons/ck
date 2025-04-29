# Author and developer: Grigori Fursin

# Add this code to the modulex.py
# r = utils.call_internal_module(None, __file__, 'modulex_test', 'test', {'input':i})


def test(i):
    print (i)
    return {'return':0, 'test':True}
