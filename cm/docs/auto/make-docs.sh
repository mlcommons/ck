# Needs to be updated based on make-docs.bat

cd ..

rm -rf _build

export SOURCEDIR=.
export BUILDDIR=_build

sphinx-apidoc -H "API" -f -T -o api ../cmind
sphinx-build -M html ${SOURCEDIR} ${BUILDDIR} ${SPHINXOPTS}

cd _build/html
tar cf docs.tar *
bzip2 docs.tar

move docs.tar.bz2 ../..

