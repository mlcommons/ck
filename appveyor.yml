# TBD: we need to add more tests with Visual Studio to build and run programs!

environment:
  matrix:

    # For Python versions available on Appveyor, see
    # http://www.appveyor.com/docs/installed-software#python

    - PYTHON: "C:\\Python27"
#    - PYTHON: "C:\\Python33"
#    - PYTHON: "C:\\Python34"
    - PYTHON: "C:\\Python35"
    - PYTHON: "C:\\Python36"
    - PYTHON: "C:\\Python37"
    - PYTHON: "C:\\Python27-x64"
#    third-party pyyml fails in Python34-x64
#    - PYTHON: "C:\\Python34-x64"
    - PYTHON: "C:\\Python35-x64"
    - PYTHON: "C:\\Python36-x64"
    - PYTHON: "C:\\Python37-x64"

init:
    - set PATH=%PYTHON%;%PYTHON%\\Scripts;%PATH%
    - python --version

install:
    - "%PYTHON%\\Scripts\\pip.exe install pyyaml"

build: false

test_script:
  - "%PYTHON%\\python.exe setup.py install"
  - "ck pull repo:ck-web"
  - "%PYTHON%\\python.exe -m tests.test"
