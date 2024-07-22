@ECHO OFF

rd /Q /S api

sphinx-apidoc -f -T -o api ../../../cm/cmind

cm replace_string_in_file utils --input=api/cmind.rst --string="cmind package" --replacement="CM python package API"

sphinx-build -M html . api

cd api/html
tar cf api.tar *
bzip2 api.tar

move api.tar.bz2 ../..

