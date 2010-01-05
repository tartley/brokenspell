from distutils.core import setup
from os import walk
from os.path import join, normpath
import sys

import py2exe

from gamelib import NAME, VERSION


NAME = NAME.replace(' ', '')
WIN_BINARY = '%s-%s-mswin' % (NAME, VERSION,)
DIST_DIR = 'dist\\%s' % (NAME,)


def write_make_zip():
    with open(r'bin\make_zip.bat', 'w') as fp:
        fp.write('@echo off\n')
        fp.write('cd dist\n')
        fp.write('zip -rq %s.zip %s\n' % (WIN_BINARY, NAME))


def get_py2exe_options():
    py2exe_options = dict(
        bundle_files=1, # causes problems with C extensions loaded at runtime
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
    return py2exe_options


def all_files(src):
    retval = []
    for (root, dirs, files) in walk(normpath(src)):
        if '.svn' in dirs:
            dirs.remove('.svn')
        retval.append((root, [join(root, file) for file in files]))
    return retval


def get_data_files():
    ms_visualc_runtime = (
        r'Microsoft.VC90.CRT', [
            r'lib\Microsoft.VC90.CRT\Microsoft.VC90.CRT.manifest',
            r'lib\Microsoft.VC90.CRT\msvcr90.dll',
    ])
    data_files = [
        # ms_visualc_runtime,
        (r'', [r'lib\avbin.dll']),
    ]
    data_files += all_files(r'data')
    return data_files


def get_config():
    config = dict(
        windows=[dict(
            script='run_game.py',
            icon_resources=[(1, 'data\SinisterDucks.ico')],
        )],
        data_files=get_data_files(),
        options=dict(
            py2exe=get_py2exe_options(),
        ),
        zipfile=None,
    )
    return config


if __name__ == '__main__':
    write_make_zip()
    setup(**get_config())

