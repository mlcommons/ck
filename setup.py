#
# Collective Knowledge
#
# See CK LICENSE.txt for licensing details.
# See CK Copyright.txt for copyright details.
#

from distutils.core import setup
from distutils.util import convert_path

setup(
  name='ck',
  version='1.8.2dev',
  url='https://github.com/ctuning/ck/wiki',
  license='BSD 3-clause',
  author='Grigori Fursin and non-profit cTuning foundation',
  author_email='Grigori.Fursin@cTuning.org',
  description='Collective Knowledge - lightweight knowledge manager to organize, cross-link, share and reuse artifacts',
  long_description=open(convert_path('./README.md')).read(),
  packages=['ck'],
  package_dir={'ck': 'ck'},
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
