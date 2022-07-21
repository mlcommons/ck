try:
    import torch as th
    print(th.__version__)
except ImportError as e:
    from sys import stderr
