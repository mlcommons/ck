#
# Developer(s): Grigori Fursin
#               Herve Guillou
#

import os
import sys
import imp

############################################################
from setuptools import find_packages, setup, convert_path

try:
    from io import open
except ImportError:
    pass

############################################################
# Version
version = imp.load_source(
    'cbench.__init__', os.path.join('cbench', '__init__.py')).__version__

# Default portal
portal_url='https://cKnowledge.io'


############################################################
setup(
    name='cbench',

    author="Grigori Fursin",
    author_email="Grigori.Fursin@cTuning.org",

    version=version,

    description="A cross-platform client to perform collaborative and reproducible benchmarking, optimization and co-design of software and hardware for emerging workloads (AI, ML, quantum, IoT) via the open cKnowledge.io portal",

    license="Apache Software License (Apache 2.0)",

    long_description=open(convert_path('./README.md'), encoding="utf-8").read(),
    long_description_content_type="text/markdown",

    url=portal_url,

    python_requires=">=2.7",

    packages=find_packages(exclude=["tests*", "docs*"]),
    package_data={"cbench":['static/*']},

    include_package_data=True,

    install_requires=[
      'requests',
      'click>=7.0',
      'ck',
      'virtualenv'
    ],

    entry_points={
      "console_scripts": 
        [
         "cr = cbench.main:cli",
         "cb = cbench.main:cli",
         "cbench = cbench.main:cli"
        ]
    },

    zip_safe=False,

    keywords="reproducible benchmarking, customizable benchmarking, portable workflows, reusable computational components, reproducibility, collaborative experiments, automation, optimization, co-design, collective knowledge",

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Environment :: Console",
        "Environment :: Plugins",
        "Environment :: Web Environment",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Topic :: System",
        "Topic :: System :: Benchmark",
        "Topic :: Education",
        "Topic :: Utilities"
       ],
)

###########################################################
# Get release notes 
import cbench.comm_min
r=cbench.comm_min.send({'url':portal_url+'/api/v1/?',
                        'action':'event', 
                        'dict':{'type':'get-cbench-release-notes','version':version}})
notes=r.get('notes','')
if notes!='':
   print ('*********************************************************************')
   print ('Release notes:')
   print ('')
   print (notes)
   print ('*********************************************************************')
