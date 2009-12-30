from distutils.core import setup
from glob import glob
from os import listdir
from os.path import isdir, join
import sys
from zipfile import ZipFile

import py2exe

from gamelib import NAME, VERSION


NAME = NAME.replace(' ', '')
WIN_BINARY = '%s-%s-bin-mswin' % (NAME, VERSION,)
DIST_DIR = 'dist\\%s' % (WIN_BINARY)


py2exe_options = dict(
    # bundle_files=1, # causes problems with C extensions loaded at runtime
    dist_dir=DIST_DIR,
    dll_excludes=["pywintypes26.dll"],
    optimize=2,
    excludes=[
        # silence some warnings of missing modules
        '_imaging_gif',
        '_scproxy',
        'dummy.Process',
        'email',
        'email.utils',
        'email.Utils',
        'ICCProfile',
        'Image',

        # filter out unused .pyd files
        '_ssl',
        '_imaging',
        '_hashlib',
        'pyexpat',
        'pyreadline',
        'win32api',
        'bz2',
        '_socket',
        '_multiprocessing',
        'win32pipe',
        'select',

        # filter out unused .pyo files in library.zip
        'doctest',
        'pyglet.window.xlib',
        'pyglet.window.carbon',
        'pyglet.window.carbon.constants',
        'pyglet.window.carbon.types',
        'win32con',
    ],
)

config = dict(
    windows=[dict(
        script='run_game.py',
        icon_resources=[(1, 'data\SinisterDucks.ico')],
    )],
    data_files=[
        (r'Microsoft.VC90.CRT', [
            r'lib\Microsoft.VC90.CRT\Microsoft.VC90.CRT.manifest',
            r'lib\Microsoft.VC90.CRT\msvcr90.dll',
        ]),

        (r'', [r'lib\avbin.dll']),

        (r'data', glob(r'data\*.*')),
        (r'data\images', glob(r'data\images\*.*')),
        (r'data\sounds', glob(r'data\sounds\*.*')),
    ],
    options=dict(
        py2exe=py2exe_options
    ),
    # zipfile=None,
)


def zip_directory():
    def zip_dir(archive, prefix, path):
        '''
        archive=zip file to write to
        prefix+path=directory to be zipped
        prefix is stripped from the paths within the zip
        '''
        fullpath = join(prefix, path)
        for filename in listdir(fullpath):
            filepath = join(fullpath, filename)
            zippath = join(path, filename)
            if isdir(filepath):
                zip_dir(archive, prefix, zippath)
            else:
                archive.write(filepath, zippath)

    zipname = join('dist', '%s.zip' % (WIN_BINARY,))
    archive = ZipFile(zipname, 'w')
    zip_dir(archive, 'dist', WIN_BINARY)
    archive.close()


def main():
    if not ('--verbose' in sys.argv or '-v' in sys.argv):
        sys.argv.append('--quiet')
    setup(**config)
    #zip_directory()


if __name__ == '__main__':
    main()

