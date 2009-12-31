
# These make targets aren't really critical, they are more of a cheatsheet to
# remind me of a few commonly-used commands.

# I run these on Windows, but they require Cygwin, both for the 'make'
# executable and for the commands that build each target. They might work ok
# from a standard Cygwin bash prompt, but just to be extra difficult, I run
# them from a Windows Cmd prompt, with C:\Cygwin\usr\bin at the start of my
# path (ie. before C:\Windows;C:\Windows\System32, etc, to make sure I pick up
# the Cygwin version of 'find.exe', 'sort.exe', etc, rather than the crappy DOS
# ones.)

clean:
	rm -rf build dist tags
	-find gamelib bin -name '*.py[oc]' -exec rm {} \;

tags:
	ctags -R gamelib

py2exe: clean
	python setup.py --quiet py2exe

stats:
	find gamelib -name '*.py' | grep -v '/tests/' | xargs wc -l | sort
	find gamelib -name '*.py' | grep '/tests/' | xargs wc -l | sort

profile:
	python -O run_game.py --profile
	runsnake profile.out

alltests:
	nosetests gamelib

zip: py2exe
	bin\\make_zip.bat

.PHONY: clean tags stats profile py2exe alltests

