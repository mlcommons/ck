import pkg_resources
import os

package_name = os.environ.get('CM_PYTHON_PACKAGE_NAME','')

if package_name != '':
    try:
        version = pkg_resources.get_distribution(package_name).version
        print (version)
    except:
        pass
