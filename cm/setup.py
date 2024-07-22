import os
import sys
import re

from setuptools import find_packages, setup

try:
    from setuptools.command.install import install
except ImportError:
    from distutils.command.install import install

# Get version
current_path = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(current_path, "cmind", "__init__.py"), encoding="utf-8") as f:
    output = re.search(r'__version__ = ["\']([^"\']+)', f.read())

    if not output:
        raise ValueError("Error: can't find version in cmind/__init__.py")

    version = output.group(1)

## Get all dependencies
#requirements = []
#
#with open(os.path.join(current_path, "requirements.txt"), "r", encoding="utf-8") as f:
#    for req in f:
#        if not req.startswith("--") and not req.startswith("#"):
#            requirements.append(req)

# Customize installation if needed

class custom_install(install):
    def run(self):
        global dir_install_script

        install.run(self)

        # Check if this version is deprecated or has vulnerabilities! 
        import cmind.net

        r = cmind.net.request(
            {'get': {'action': 'get-cm-version-notes-setup', 'version': version}})
        notes = r.get('dict', {}).get('notes','')
        if notes !='':
            print (notes)


############################################################
# Add all directories in "automations" to the distribution

root = 'cmind'

repo=os.walk(os.path.join(root,'repo'))

repo_dirs=['']

for artifact in repo:
    directory=os.path.join(artifact[0], '*')
    ignore=False
    for ignore_dir in ['__pycache__', 'build', 'egg-info', 'dist']:
        if ignore_dir in directory:
            ignore=True
            break
    if not ignore:
        repo_dirs.append(directory[len(root)+1:])

setup(
    name="cmind",

    author="Grigori Fursin",
    author_email="gfursin@cKnowledge.org",

    version=version,

    description="cmind",

    license="Apache 2.0",

    long_description=open('README.md', encoding="utf-8").read(),
    long_description_content_type="text/markdown",

    url="https://github.com/mlcommons/ck/tree/master/cm",

    python_requires="", # do not force for testing

    packages=['cmind'],

    include_package_data=False,

    package_data={'cmind': repo_dirs},

    cmdclass={
        'install': custom_install
    },

    install_requires=['pyyaml', 'requests', 'setuptools', 'giturlparse'],

    entry_points={"console_scripts": [
                      "cmind = cmind.cli:run",
                      "cm = cmind.cli:run",
                      "cmr = cmind.cli:run_script",
                      "cmrd = cmind.cli:docker_script",
                      "cmg = cmind.cli:gui_script",
                      "cme = cmind.cli:run_experiment"
                 ]},

    zip_safe=False,

    keywords="cm,collective mind,cmind,ck3,cdatabase,cmeta,automation,portability,reusability,productivity,meta,JSON,YAML,python,api,cli"
)
