cd ..

rm -rf _build

export SOURCEDIR=.
export BUILDDIR=_build

sphinx-apidoc -H "cmind package" -f -T -o _package ../cmind
sphinx-build -M html ${SOURCEDIR} ${BUILDDIR} ${SPHINXOPTS}
