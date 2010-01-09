#!/usr/bin/env bash

NAME=SinisterDucks
VERSION=`python -O ${NAME}.py --version | sed -e 's/\n//' `

if [ ! -d dist ] ; then
    mkdir dist
fi

rm -rf dist/${NAME}
svn export . dist/${NAME}

cd dist
tar -czf ${NAME}-${VERSION}-src.tgz ${NAME}

