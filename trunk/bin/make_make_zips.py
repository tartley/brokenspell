#!/usr/bin/env python

from os.path import join

import fixpath

from sinisterducks import NAME, VERSION

NAME = NAME.replace(' ', '')
WIN_BINARY = '%s-%s-mswin' % (NAME, VERSION,)
SRC_ZIP = '%s-%s-src' % (NAME, VERSION,)


def write_file(name, text):
    with open(name, 'w') as fp:
        for line in text:
            fp.write(line + '\n')


def write_make_zips():
    write_file(join('bin', 'make_win_zip.bat'), [
        '@echo off',
        'setlocal',
        'cd dist',
        'rm -f %s.zip' % (WIN_BINARY,),
        'zip -rq %s.zip %s' % (WIN_BINARY, NAME),
    ])
    write_file(join('bin', 'make_src_zip.sh'), [
        '#!/usr/bin/env bash',
        'if [ ! -d dist ] ; then',
        '    mkdir dist',
        'fi',
        'rm -rf dist/SinisterDucks',
        'svn export . dist/SinisterDucks',
        'cd dist',
        'tar -czf %s.tgz SinisterDucks' % (SRC_ZIP, ),
    ])


if __name__ == '__main__':
    write_make_zips()

