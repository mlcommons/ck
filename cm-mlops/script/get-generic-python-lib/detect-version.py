import os

package_name = os.environ.get('CM_GENERIC_PYTHON_PACKAGE_NAME','')

filename = 'tmp-ver.out'

if os.path.isfile(filename):
    os.remove(filename)

if package_name != '':

    version = ''
    error = ''

    try:
        import importlib.metadata
        version = importlib.metadata.version(package_name)
    except Exception as e:
        error = format(e)

    if error != '':
        try:
            import pkg_resources
            version = pkg_resources.get_distribution(package_name).version
            error = ''
        except Exception as e:
            if error!='': error += '\n'
            error += format(e)

    # We generally skip error since it usually means that 
    # package is not installed

    with open(filename, 'w') as file:
        file.write(str(version)+'\n')
