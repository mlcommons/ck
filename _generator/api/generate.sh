rm -rf api

sphinx-apidoc -H "CM python package API" -f -T -o api ../../../cm/cmind

sphinx-build -M html . api

cd api/html
tar cf api.tar *
bzip2 api.tar

move api.tar.bz2 ../..
