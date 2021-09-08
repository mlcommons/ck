#
# Collective Knowledge
#
# See CK LICENSE.txt for licensing details.
# See CK Copyright.txt for copyright details.
#

import sys
import os
import re
import ck.net

############################################################
try:
    from io import open
except ImportError:
    pass

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    from setuptools import convert_path
except ImportError:
    from distutils.util import convert_path

try:
    from setuptools.command.install import install
except ImportError:
    from distutils.command.install import install

try:
    from setuptools.command.install_scripts import install_scripts
except ImportError:
    from distutils.command.install_scripts import install_scripts

try:
    from setuptools.command.install_lib import install_lib
except ImportError:
    from distutils.command.install_lib import install_lib

from distutils.sysconfig import get_python_lib

############################################################
# Global variables

dir_install_script = ""

############################################################
# Find version

current_version = ''
current_path = os.path.abspath(os.path.dirname(__file__))
kernel_file = os.path.join(current_path, 'ck', 'kernel.py')

with open(kernel_file, encoding="utf-8") as f:
    search = re.search(r'__version__ = ["\']([^"\']+)', f.read())

    if not search:
        raise ValueError("We can't find the CK version in ck/kernel.py")

    current_version = search.group(1)


############################################################
# Read dependencies

with open('requirements.txt', 'r', encoding='utf-8') as fr:
    requirements = []
    for l in fr:
        requirements.append(l)


############################################################
# Add all directories in "repo" to the distribution

repo=os.walk(os.path.join('ck','repo'))

repo_dirs=[os.path.join('repo','.ck*')]

for x in repo:
    directory=os.path.join(x[0],'*')
    if '__pycache__' not in directory:
        repo_dirs.append(directory[3:])


############################################################
# Customize installation

class custom_install(install):
    def run(self):
        global dir_install_script

        install.run(self)

        # Check if detected script directory
        if dir_install_script != "" and os.path.isdir(dir_install_script):
            # Check which python interpreter is used
            python_bin = sys.executable
            real_python_bin = os.path.abspath(python_bin)

            if os.environ.get('CK_PYTHON','').strip()!='':
                python_bin = os.environ.get('CK_PYTHON','').strip()

            if os.environ.get('CK_SKIP_SAVING_PYTHON_BIN','').strip().lower()!='yes' and os.path.isfile(python_bin):
                # Attempt to write to $SCRIPTS/ck-python.cfg
                file_type = 'wb'
                if sys.version_info[0] > 2:
                    file_type = 'w'

                p = os.path.join(dir_install_script, 'ck-python.cfg')

                try:
                    with open(p, file_type) as f:
                        f.write(python_bin+'\n')

                    print('')
                    print("Writing CK python executable ("+python_bin+") to "+p)
                    print('')
                except Exception as e:
                    print(
                        "warning: can\'t write info about CK python executable to "+p+" ("+format(e)+")")
                    pass

        # Check default repo status before copying
        r = ck.net.request(
            {'get': {'action': 'get-default-repo-status', 'version': current_version}})
        d = r.get('dict', {})
        if d.get('skip_copy_default_repo', False):
            return


class custom_install_scripts(install_scripts):
    def run(self):
        global dir_install_script

        install_scripts.run(self)

        dir_install_script = os.path.abspath(self.install_dir)

        if dir_install_script != None and dir_install_script != "" and os.path.isdir(dir_install_script):
            print('')
            print("Detected script installation directory: "+dir_install_script)
            print('')

        return


############################################################
# Describe CK setup

setup(
    name='ck',
    version=current_version,

    url='https://github.com/mlcommons/ck',

    license='Apache 2.0',

    author='Grigori Fursin',
    author_email='Grigori.Fursin@cTuning.org',

    description='Collective Knowledge - a lightweight knowledge manager to organize, cross-link, share and reuse artifacts and workflows based on FAIR principles',

    install_requires=requirements,

    long_description=open(convert_path('./README.md'),
                          encoding="utf-8").read(),
    long_description_content_type="text/markdown",

    packages=['ck'],
    package_dir={'ck': 'ck'},

    zip_safe=False,

    package_data={'ck': repo_dirs},

    cmdclass={
        'install': custom_install,
        'install_scripts': custom_install_scripts
    },

    entry_points='''
        [console_scripts]
        ck=ck.kernel:cli
    ''',

    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Plugins",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Topic :: System",
        "Topic :: System :: Benchmark",
        "Topic :: Education",
        "Topic :: Home Automation",
        "Topic :: Adaptive Technologies",
        "Topic :: Database",
        "Topic :: Utilities"
    ]
)
