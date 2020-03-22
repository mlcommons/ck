#
# Collective Knowledge
#
# See CK LICENSE.txt for licensing details.
# See CK Copyright.txt for copyright details.
#

import sys
import os
import re
import ck.api

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



############################################################
# Global variables
install_dir=""

############################################################
# Find version
current_version=''
current_path=os.path.abspath(os.path.dirname(__file__))
kernel_file=os.path.join(current_path, 'ck', 'kernel.py')

with open(kernel_file, encoding="utf-8") as f:
    search = re.search(r'__version__ = ["\']([^"\']+)', f.read())

    if not search:
       raise ValueError("We can't find the version number in from ck/kernel.py")

    current_version = search.group(1)

############################################################
class custom_install(install):
    def run(self):
        global install_dir

        install.run(self)

        # Check if detected script directory
        if install_dir!="" and os.path.isdir(install_dir):
           # Check which python interpreter is used
           python_bin=sys.executable
           if os.path.isfile(python_bin):
              # Attempt to write to $SCRIPTS/ck-python.cfg
              p=os.path.join(install_dir, 'ck-python.cfg')

              file_type='wb'
              if sys.version_info[0]>2:
                 file_type='w'

              try:
                 with open(p, file_type) as f:
                    f.write(python_bin+'\n')

                 print ("writing CK python executable ("+python_bin+") to "+p)
              except Exception as e: 
                 print ("warning: can\'t write info about CK python executable to "+p+" ("+format(e)+")")
                 pass

        # Check default repo status before copying
        r=ck.api.request({'get':{'action':'get-default-repo-status', 'version': current_version}})
        d=r.get('dict',{})
        if d.get('skip_copy_default_repo', False):
           return

        # Copy default repo
        try:
           # Find home user directory (to record default repo)
           from os.path import expanduser
           import shutil
           user_home = expanduser("~")

           path_to_default_repo=os.path.join(current_path, 'ck', 'repo')
           path_to_copy_of_default_repo=os.path.join(user_home, '.ck', current_version, 'repo')

           if os.path.isdir(path_to_copy_of_default_repo):
              shutil.rmtree(path_to_copy_of_default_repo)

           shutil.copytree(path_to_default_repo, path_to_copy_of_default_repo)

           print ("copying default CK repo to "+path_to_copy_of_default_repo)
        except:
           print ("warning: can\'t copy default CK repo to "+path_to_copy_of_default_repo)
           pass

############################################################
class custom_install_scripts(install_scripts):
   def run(self):
       global install_dir
       install_scripts.run(self)
       install_dir=self.install_dir
       if install_dir!=None and install_dir!="":
          print ("detected installation directory: "+install_dir)

############################################################
# Describing CK setup
setup(
  name='ck',
  version=current_version,

  url='https://github.com/ctuning/ck',

  license='BSD 3-clause',

  author='Grigori Fursin',
  author_email='Grigori.Fursin@cTuning.org',

  description='Collective Knowledge - lightweight knowledge manager to organize, cross-link, share and reuse artifacts and workflows',

  long_description=open(convert_path('./README.md'), encoding="utf-8").read(),
  long_description_content_type="text/markdown",

  packages=['ck'],
  package_dir={'ck': 'ck'},

  zip_safe=False,

  package_data={'ck': ['repo/.ck*', 
                       'repo/.cm/*',
                       'repo/kernel/.cm/*',
                       'repo/kernel/default/*',
                       'repo/kernel/default/.cm/*',
                       'repo/module/.cm/*',
                       'repo/module/all/*.py',
                       'repo/module/all/.cm/*',
                       'repo/module/demo/*.py',
                       'repo/module/demo/.cm/*',
                       'repo/module/index/*.py',
                       'repo/module/index/.cm/*',
                       'repo/module/kernel/*.py',
                       'repo/module/kernel/.cm/*',
                       'repo/module/kernel/test/test*.py',
                       'repo/module/module/*.py',
                       'repo/module/module/*.input',
                       'repo/module/module/.cm/*',
                       'repo/module/repo/*.py',
                       'repo/module/repo/.cm/*',
                       'repo/module/cfg/*.py',
                       'repo/module/cfg/.cm/*',
                       'repo/module/test/*.py',
                       'repo/module/test/.cm/*',
                       'repo/module/tmp/*.py',
                       'repo/module/tmp/.cm/*',
                       'repo/module/web/*.py',
                       'repo/module/web/.cm/*',
                       'repo/module/web/php/*.php',
                       'repo/module/web/php/server-side/*',
                       'repo/repo/.cm/*',
                       'repo/repo/default/.cm/*',
                       'repo/repo/local/.cm/*',
                       'repo/repo/remote-ck/.cm/*',
                       'repo/test/.cm/*',
                       'repo/test/unicode/c*',
                       'repo/test/unicode/t*',
                       'repo/test/unicode/.cm/*',
                       'repo/test/unicode/dir/*']},

  scripts = ["bin/ck" ,"bin/ck.bat"],

  cmdclass={'install': custom_install, 
            'install_scripts': custom_install_scripts},

  classifiers = [
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
        "License :: OSI Approved :: BSD License",
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
