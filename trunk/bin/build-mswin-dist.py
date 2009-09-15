from distutils.core import setup
from glob import glob
import sys

import py2exe

import fixpath

from gamelib import VERSION


DIST_DIR = 'dist\\SinisterDucks-%s-mswin' % (VERSION,)


py2exe_options = dict(
    dist_dir=DIST_DIR,
    optimize=2,
    excludes=[
        # silence some warnings of missing modules
        '_imaging_gif',
        'dummy.Process',
        'email',
        'email.utils',

        # filter out unused .pyd files
        '_ssl',
        '_imaging',
        '_hashlib',
        'pyexpat',
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
    dll_excludes=["pywintypes26.dll"],
)

config = dict(
    windows=['run_game.py'],
    data_files=[
        ('', ['lib\\avbin.dll']),
        ('data', glob('data\\*.*')),
        ('data\\images', glob('data\\images\*.*')),
        ('data\\sounds', glob('data\\sounds\*.*')),
        ('data\\sprites', glob('data\\sprites\*.*')),
    ],
    options=dict(
        py2exe=py2exe_options
    ),
)


def main(config):
    if not 'py2exe' in sys.argv:
        sys.argv.append('py2exe')
    if not ('--verbose' in sys.argv or '-v' in sys.argv):
        sys.argv.append('--quiet')
    setup(**config)


if __name__ == '__main__':
    sys.exit(main(config))

