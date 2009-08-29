
from os import environ

from platform import system


def get_separator():
    if system() == 'Windows':
        return ';'
    else:
        return ':'


def get_env_name():
    if system() == 'Windows':
        return 'PATH'
    else:
        return 'LD_LIBRARY_PATH'


def append(name, value):
    orig = environ.get(name, '')
    if orig:
        orig += get_separator()
    orig += value
    environ[name] = orig


def set_env_vars():
    append(get_env_name(), 'lib')

