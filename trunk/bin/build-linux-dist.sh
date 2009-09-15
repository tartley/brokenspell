#!/bin/sh

NAME=sinister-ducks
TARBALL=${NAME}-linux-bin.tar.gz

set -x -e

rm -rf dist
bb-freeze run_game.py 
cp -r README.txt config.ini data dist
cp lib/libavbin.so* dist
find dist -name .svn | xargs rm -rf 
mv dist $NAME
tar czf $TARBALL $NAME
rm -rf $NAME

