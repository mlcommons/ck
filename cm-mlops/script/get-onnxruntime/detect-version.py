try:
    import onnxruntime as ort
    print(ort.__version__)
except ImportError as e:
    from sys import stderr
