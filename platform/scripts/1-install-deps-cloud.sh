#!/bin/bash

sudo a2enmod proxy_http

python3 -m pip install -r ../requirements.txt

cm pull repo ctuning@mlcommons-ck

