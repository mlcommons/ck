cd ..

rm -rf _build

export SOURCEDIR=.
export BUILDDIR=_build

sphinx-apidoc -H "cmind package" -f -T -o api ../cmind
sphinx-build -M html ${SOURCEDIR} ${BUILDDIR} ${SPHINXOPTS}

cd _build/html
tar cf docs.tar *
bzip2 docs.tar

move docs.tar.bz2 ../..

