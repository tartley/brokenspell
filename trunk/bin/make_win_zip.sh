#!/usr/bin/env bash

NAME=SinisterDucks
VERSION=`python -O ${NAME}.py --version | sed -e 's/\n//' `

cd dist
rm -f ${NAME}-${VERSION}-mswin.zip
zip -rq ${NAME}-${VERSION}-mswin.zip ${NAME}

