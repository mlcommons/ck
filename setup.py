#
# Collective Knowledge
#
# See CK LICENSE.txt for licensing details.
# See CK Copyright.txt for copyright details.
#

from distutils.core import setup

setup(
  name='ck',
  version='1.5.0915',
  url='https://github.com/ctuning/ck/wiki',
  license='BSD 3-clause',
  author='Grigori Fursin and non-profit cTuning foundation',
  author_email='Grigori.Fursin@cTuning.org',
  description='CK - lightweight knowledge manager to organize, cross-link, share and reuse artifacts',
  long_description=open('README.md').read(),
  packages=['ck'],
  package_data={'ck': ['repo/.*', 
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
                       'repo/module/module/*.py',
                       'repo/module/module/.cm/*',
                       'repo/module/repo/*.py',
                       'repo/module/repo/.cm/*',
                       'repo/module/test/*.py',
                       'repo/module/test/.cm/*',
                       'repo/module/tmp/*.py',
                       'repo/module/tmp/.cm/*',
                       'repo/module/web/*.py',
                       'repo/module/web/.cm/*',
                       'repo/module/web/php/*',
                       'repo/module/web/php/server-side/*',
                       'repo/repo/.cm/*',
                       'repo/repo/default/.cm/*',
                       'repo/repo/local/.cm/*',
                       'repo/repo/remote-ck/.cm/*',
                       'repo/test/.cm/*',
                       'repo/test/unicode/*',
                       'repo/test/unicode/.cm/*',
                       'repo/test/unicode/dir/*',
                       'repo/test/unicode/.cm/*']},
  data_files=[('Scripts', ['bin/ck', 
                           'bin/ck.bat',
                           'bin/ckcd',
                           'bin/ckcd.bat']),
              ('bin',     ['bin/ck', 
                           'bin/ck.bat',
                           'bin/ckcd',
                           'bin/ckcd.bat'])]
)
