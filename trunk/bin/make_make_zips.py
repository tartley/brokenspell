
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
    write_file(r'bin\make_win_zip.bat', [
        '@echo off',
        'setlocal',
        'cd dist',
        'rm -f %s.zip' % (WIN_BINARY,),
        'zip -rq %s.zip %s' % (WIN_BINARY, NAME),
    ])
    write_file(r'bin\make_src_zip.bat', [
        '@echo off',
        'setlocal',
        'rm -rf dist\%s' % (SRC_ZIP,),
        'svn export . dist\%s' % (SRC_ZIP,),
        'cd dist',
        'rm -f dist\%s.zip' % (SRC_ZIP,),
        'zip -rq %s.zip %s' % (SRC_ZIP, SRC_ZIP),
    ])


if __name__ == '__main__':
    write_make_zips()

