import pkg_resources
try:
    version = pkg_resources.get_distribution("tokenization").version
    print(version)
except ImportError as e:
    from sys import stderr
