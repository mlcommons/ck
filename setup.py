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


class custom_install(install):
    def run(self):
        global dir_install_script

        install.run(self)

        # Check if detected script directory
        if dir_install_script != "" and os.path.isdir(dir_install_script):
            # Check which python interpreter is used
            python_bin = sys.executable
            real_python_bin = os.path.abspath(python_bin)

            if os.path.isfile(python_bin):
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

############################################################


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
# Describing CK setup
r = setup(
    name='ck',
    version=current_version,

    url='https://github.com/ctuning/ck',

    license='BSD 3-clause',

    author='Grigori Fursin',
    author_email='Grigori.Fursin@cTuning.org',

    description='Collective Knowledge - a lightweight knowledge manager to organize, cross-link, share and reuse artifacts and workflows',

    long_description=open(convert_path('./README.md'),
                          encoding="utf-8").read(),
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
                         'repo/module/advice/.cm/*',
                         'repo/module/advice/*',
                         'repo/module/algorithm/.cm/*',
                         'repo/module/algorithm/*',
                         'repo/module/all/.cm/*',
                         'repo/module/all/*',
                         'repo/module/apk/.cm/*',
                         'repo/module/apk/*',
                         'repo/module/artifact/.cm/*',
                         'repo/module/artifact/*',
                         'repo/module/caffe/.cm/*',
                         'repo/module/caffe/*',
                         'repo/module/caffe2/.cm/*',
                         'repo/module/caffe2/*',
                         'repo/module/cfg/.cm/*',
                         'repo/module/cfg/*',
                         'repo/module/choice/.cm/*',
                         'repo/module/choice/*',
                         'repo/module/clblast/.cm/*',
                         'repo/module/clblast/*',
                         'repo/module/cmdgen/.cm/*',
                         'repo/module/cmdgen/*',
                         'repo/module/compiler/.cm/*',
                         'repo/module/compiler/*',
                         'repo/module/crowdnode/.cm/*',
                         'repo/module/crowdnode/*',
                         'repo/module/dashboard/.cm/*',
                         'repo/module/dashboard/*',
                         'repo/module/dataset/.cm/*',
                         'repo/module/dataset/*',
                         'repo/module/dataset.features/.cm/*',
                         'repo/module/dataset.features/*',
                         'repo/module/demo/.cm/*',
                         'repo/module/demo/*',
                         'repo/module/device/.cm/*',
                         'repo/module/device/*',
                         'repo/module/docker/.cm/*',
                         'repo/module/docker/*',
                         'repo/module/env/.cm/*',
                         'repo/module/env/*',
                         'repo/module/experiment/.cm/*',
                         'repo/module/experiment/*',
                         'repo/module/experiment.bench.caffe/.cm/*',
                         'repo/module/experiment.bench.caffe/*',
                         'repo/module/experiment.bench.caffe2/.cm/*',
                         'repo/module/experiment.bench.caffe2/*',
                         'repo/module/experiment.bench.dnn/.cm/*',
                         'repo/module/experiment.bench.dnn/*',
                         'repo/module/experiment.bench.dnn.mobile/.cm/*',
                         'repo/module/experiment.bench.dnn.mobile/*',
                         'repo/module/experiment.bench.tensorflow/.cm/*',
                         'repo/module/experiment.bench.tensorflow/*',
                         'repo/module/experiment.check.algorithm.scalability/.cm/*',
                         'repo/module/experiment.check.algorithm.scalability/*',
                         'repo/module/experiment.check.numerical.stability/.cm/*',
                         'repo/module/experiment.check.numerical.stability/*',
                         'repo/module/experiment.detect.opencl.bugs/.cm/*',
                         'repo/module/experiment.detect.opencl.bugs/*',
                         'repo/module/experiment.model.program.behavior/.cm/*',
                         'repo/module/experiment.model.program.behavior/*',
                         'repo/module/experiment.raw/.cm/*',
                         'repo/module/experiment.raw/*',
                         'repo/module/experiment.scenario.mobile/.cm/*',
                         'repo/module/experiment.scenario.mobile/*',
                         'repo/module/experiment.tune.compiler.flags/.cm/*',
                         'repo/module/experiment.tune.compiler.flags/images/*',
                         'repo/module/experiment.tune.compiler.flags/*',
                         'repo/module/experiment.tune.compiler.flags.gcc/.cm/*',
                         'repo/module/experiment.tune.compiler.flags.gcc/*',
                         'repo/module/experiment.tune.compiler.flags.gcc.custom/.cm/*',
                         'repo/module/experiment.tune.compiler.flags.gcc.custom/*',
                         'repo/module/experiment.tune.compiler.flags.gcc.e/.cm/*',
                         'repo/module/experiment.tune.compiler.flags.gcc.e/*',
                         'repo/module/experiment.tune.compiler.flags.gcc.e.x/.cm/*',
                         'repo/module/experiment.tune.compiler.flags.gcc.e.x/*',
                         'repo/module/experiment.tune.compiler.flags.gcc.es/.cm/*',
                         'repo/module/experiment.tune.compiler.flags.gcc.es/*',
                         'repo/module/experiment.tune.compiler.flags.gcc.fuzz/.cm/*',
                         'repo/module/experiment.tune.compiler.flags.gcc.fuzz/*',
                         'repo/module/experiment.tune.compiler.flags.gcc.s/.cm/*',
                         'repo/module/experiment.tune.compiler.flags.gcc.s/*',
                         'repo/module/experiment.tune.compiler.flags.gcc.x/.cm/*',
                         'repo/module/experiment.tune.compiler.flags.gcc.x/*',
                         'repo/module/experiment.tune.compiler.flags.llvm/.cm/*',
                         'repo/module/experiment.tune.compiler.flags.llvm/*',
                         'repo/module/experiment.tune.compiler.flags.llvm.e/.cm/*',
                         'repo/module/experiment.tune.compiler.flags.llvm.e/*',
                         'repo/module/experiment.tune.compiler.flags.llvm.e.x/.cm/*',
                         'repo/module/experiment.tune.compiler.flags.llvm.e.x/*',
                         'repo/module/experiment.tune.compiler.flags.llvm.fuzz/.cm/*',
                         'repo/module/experiment.tune.compiler.flags.llvm.fuzz/*',
                         'repo/module/experiment.tune.compiler.flags.llvm.x/.cm/*',
                         'repo/module/experiment.tune.compiler.flags.llvm.x/*',
                         'repo/module/experiment.tune.cuda.ws.e/.cm/*',
                         'repo/module/experiment.tune.cuda.ws.e/*',
                         'repo/module/experiment.tune.custom.dimensions/.cm/*',
                         'repo/module/experiment.tune.custom.dimensions/*',
                         'repo/module/experiment.tune.dnn.batch_size/.cm/*',
                         'repo/module/experiment.tune.dnn.batch_size/*',
                         'repo/module/experiment.tune.openblas.threads/.cm/*',
                         'repo/module/experiment.tune.openblas.threads/*',
                         'repo/module/experiment.tune.opencl.clblast/.cm/*',
                         'repo/module/experiment.tune.opencl.clblast/*',
                         'repo/module/experiment.tune.opencl.lws.e/.cm/*',
                         'repo/module/experiment.tune.opencl.lws.e/*',
                         'repo/module/experiment.tune.opencl.lws.ep/.cm/*',
                         'repo/module/experiment.tune.opencl.lws.ep/*',
                         'repo/module/experiment.tune.openmp.threads/.cm/*',
                         'repo/module/experiment.tune.openmp.threads/*',
                         'repo/module/experiment.user/.cm/*',
                         'repo/module/experiment.user/*',
                         'repo/module/experiment.view/.cm/*',
                         'repo/module/experiment.view/*',
                         'repo/module/graph/.cm/*',
                         'repo/module/graph/templates/*',
                         'repo/module/graph/third-party/d3/*',
                         'repo/module/graph/third-party/*',
                         'repo/module/graph/*',
                         'repo/module/graph.dot/.cm/*',
                         'repo/module/graph.dot/*',
                         'repo/module/index/.cm/*',
                         'repo/module/index/*',
                         'repo/module/jnotebook/.cm/*',
                         'repo/module/jnotebook/*',
                         'repo/module/kernel/.cm/*',
                         'repo/module/kernel/test/*',
                         'repo/module/kernel/*',
                         'repo/module/log/.cm/*',
                         'repo/module/log/*',
                         'repo/module/machine/.cm/*',
                         'repo/module/machine/*',
                         'repo/module/math.conditions/.cm/*',
                         'repo/module/math.conditions/*',
                         'repo/module/math.frontier/.cm/*',
                         'repo/module/math.frontier/*',
                         'repo/module/math.variation/.cm/*',
                         'repo/module/math.variation/*',
                         'repo/module/me/.cm/*',
                         'repo/module/me/*',
                         'repo/module/misc/.cm/*',
                         'repo/module/misc/*',
                         'repo/module/mlperf/.cm/*',
                         'repo/module/mlperf/*',
                         'repo/module/mlperf.inference/.cm/*',
                         'repo/module/mlperf.inference/*',
                         'repo/module/mlperf.mobilenets/.cm/*',
                         'repo/module/mlperf.mobilenets/*',
                         'repo/module/model/.cm/*',
                         'repo/module/model/*',
                         'repo/module/model.image.classification/.cm/*',
                         'repo/module/model.image.classification/*',
                         'repo/module/model.r/.cm/*',
                         'repo/module/model.r/*',
                         'repo/module/model.sklearn/.cm/*',
                         'repo/module/model.sklearn/*',
                         'repo/module/model.species/.cm/*',
                         'repo/module/model.species/*',
                         'repo/module/model.tensorflowapi/.cm/*',
                         'repo/module/model.tensorflowapi/*',
                         'repo/module/model.tf/.cm/*',
                         'repo/module/model.tf/*',
                         'repo/module/module/.cm/*',
                         'repo/module/module/*',
                         'repo/module/nntest/.cm/*',
                         'repo/module/nntest/*',
                         'repo/module/os/.cm/*',
                         'repo/module/os/test/*',
                         'repo/module/os/*',
                         'repo/module/package/.cm/*',
                         'repo/module/package/*',
                         'repo/module/paper/.cm/*',
                         'repo/module/paper/*',
                         'repo/module/pipeline/.cm/*',
                         'repo/module/pipeline/*',
                         'repo/module/pipeline.cmd/.cm/*',
                         'repo/module/pipeline.cmd/*',
                         'repo/module/platform/.cm/*',
                         'repo/module/platform/*',
                         'repo/module/platform.cpu/.cm/*',
                         'repo/module/platform.cpu/*',
                         'repo/module/platform.dsp/.cm/*',
                         'repo/module/platform.dsp/*',
                         'repo/module/platform.gpgpu/.cm/*',
                         'repo/module/platform.gpgpu/*',
                         'repo/module/platform.gpu/.cm/*',
                         'repo/module/platform.gpu/*',
                         'repo/module/platform.init/.cm/*',
                         'repo/module/platform.init/*',
                         'repo/module/platform.nn/.cm/*',
                         'repo/module/platform.nn/*',
                         'repo/module/platform.npu/.cm/*',
                         'repo/module/platform.npu/*',
                         'repo/module/platform.os/.cm/*',
                         'repo/module/platform.os/*',
                         'repo/module/program/.cm/*',
                         'repo/module/program/*',
                         'repo/module/program.behavior/.cm/*',
                         'repo/module/program.behavior/*',
                         'repo/module/program.dynamic.features/.cm/*',
                         'repo/module/program.dynamic.features/*',
                         'repo/module/program.experiment.speedup/.cm/*',
                         'repo/module/program.experiment.speedup/*',
                         'repo/module/program.optimization/.cm/*',
                         'repo/module/program.optimization/images/*',
                         'repo/module/program.optimization/*',
                         'repo/module/program.optimization.mobile/.cm/*',
                         'repo/module/program.optimization.mobile/*',
                         'repo/module/program.output/.cm/*',
                         'repo/module/program.output/*',
                         'repo/module/program.species/.cm/*',
                         'repo/module/program.species/*',
                         'repo/module/program.static.features/.cm/*',
                         'repo/module/program.static.features/*',
                         'repo/module/qr-code/.cm/*',
                         'repo/module/qr-code/*',
                         'repo/module/repo/.cm/*',
                         'repo/module/repo/*',
                         'repo/module/report/.cm/*',
                         'repo/module/report/*',
                         'repo/module/result/.cm/*',
                         'repo/module/result/*',
                         'repo/module/script/.cm/*',
                         'repo/module/script/*',
                         'repo/module/soft/.cm/*',
                         'repo/module/soft/test/*',
                         'repo/module/soft/*',
                         'repo/module/solution/.cm/*',
                         'repo/module/solution/*',
                         'repo/module/sut/.cm/*',
                         'repo/module/sut/*',
                         'repo/module/table/.cm/*',
                         'repo/module/table/*',
                         'repo/module/tensorflow/.cm/*',
                         'repo/module/tensorflow/*',
                         'repo/module/test/.cm/*',
                         'repo/module/test/*',
                         'repo/module/tmp/.cm/*',
                         'repo/module/tmp/*',
                         'repo/module/user/.cm/*',
                         'repo/module/user/*',
                         'repo/module/web/.cm/*',
                         'repo/module/web/php/server-side/*',
                         'repo/module/web/php/*',
                         'repo/module/web/*',
                         'repo/module/wfe/.cm/*',
                         'repo/module/wfe/*',
                         'repo/module/xml/.cm/*',
                         'repo/module/xml/*',

                         'repo/repo/.cm/*',
                         'repo/repo/default/.cm/*',
                         'repo/repo/local/.cm/*',
                         'repo/repo/remote-ck/.cm/*',
                         'repo/test/.cm/*',
                         'repo/test/unicode/c*',
                         'repo/test/unicode/t*',
                         'repo/test/unicode/.cm/*',
                         'repo/test/unicode/dir/*']},

    scripts=["bin/ck", "bin/ck.bat"],

    cmdclass={
        'install': custom_install,
        'install_scripts': custom_install_scripts
    },

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
