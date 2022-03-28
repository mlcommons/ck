import os
import sys
import re

from setuptools import find_packages, setup, convert_path

# Get version
current_path = os.path.abspath(os.path.dirname(__file__))

# Get all dependencies
requirements = []

with open(os.path.join(current_path, "requirements.txt"), "r", encoding="utf-8") as f:
    for req in f:
        if not req.startswith("--") and not req.startswith("#"):
            requirements.append(req)

# Attempt to get the name of the module
module_name = ''
dirs = os.listdir(current_path)
for d in dirs:
    if os.path.isdir(d) and d.startswith('cmind_') and 'egg-info' not in d:
        module_name=d
        break

############################################################
# Add all directories in "automations" to the distribution

setup(
    name=module_name,

    author="OctoML",
    author_email="grigori@octoml.ai",

    version='0.0.1',

    description="CM CK wrapper",

    license="Apache 2.0",

    url="TBA",

    python_requires="", # do not force for testing

    packages=find_packages(exclude=["tests*", "docs*"]),

    include_package_data=False,

    package_data={module_name: ['../_cm.json']},

    install_requires=requirements,

    zip_safe=False,

    keywords="collective mind,cmind,automation,actions,meta descriptions,JSON,YAML,python",

)
