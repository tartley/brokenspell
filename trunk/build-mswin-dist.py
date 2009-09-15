from bbfreeze import Freezer
freeze = Freezer(distdir='mswin-binaries', excludes=('MSVCR90.dll'))
freeze.addScript('run_game.py', gui_only=True)
freeze()

