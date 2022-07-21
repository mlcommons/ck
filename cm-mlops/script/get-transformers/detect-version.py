try:
    import transformers as tr
    print(tr.__version__)
except ImportError as e:
    from sys import stderr
