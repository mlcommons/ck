@ECHO OFF

cd ..

rd /Q /S _build

set SOURCEDIR=.
set BUILDDIR=_build

call sphinx-apidoc -f -T -o _package ../cmind

call sphinx-build -M html %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%

cd _build/html
tar cf docs.tar *
bzip2 docs.tar

move docs.tar.bz2 ../..

