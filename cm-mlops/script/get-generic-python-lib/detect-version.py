import pkg_resources
import os
try:
    package_name = os.environ.get('CM_PYTHON_PACKAGE_NAME')
    version = pkg_resources.get_distribution(package_name).version
    print(version)
except:
    pass
