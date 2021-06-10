import os
import sys
import re

############################################################
from setuptools import find_packages, setup, convert_path

try:
    from io import open
except ImportError:
    pass

############################################################
# Version
current_path = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(current_path, "cbase", "__init__.py"), encoding="utf-8") as f:
    output = re.search(r'__version__ = ["\']([^"\']+)', f.read())
    version = output.group(1)

############################################################
setup(
    name='cdatabase',

    author="Grigori Fursin",
    author_email="gfursin@gmail.com",

    version=version,

    description="Collective DataBase",

    license="Apache 2.0",

    long_description=open(convert_path('./README.md'), encoding="utf-8").read(),
    long_description_content_type="text/markdown",

    url="https://github.com/gfursin/cdatabase",

    python_requires="", # do not force for testing

    packages=find_packages(exclude=["tests*", "docs*"]),

    include_package_data=True,

    install_requires=[
      'pyyaml',
      'ck' # temporal
    ],

#    entry_points={"console_scripts": [
#                      "cdb = cdatabase.cli:run"
#                  ]},

    zip_safe=False,

    keywords="cdatabase,collective database",

    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
       ],
)
