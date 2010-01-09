
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
	-find sinisterducks bin -name '*.py[oc]' -exec rm {} \;

tags:
	ctags -R sinisterducks

stats:
	find sinisterducks -name '*.py' | grep -v '/tests/' | xargs wc -l | sort
	find sinisterducks -name '*.py' | grep '/tests/' | xargs wc -l | sort

profile:
	python -O -m cProfile -o profile.out Sinister-Ducks.py
	runsnake profile.out

alltests:
	nosetests sinisterducks


py2exe:
	rm -rf dist\\SinisterDucks
	python setup.py --quiet py2exe


make_zips:
	python bin\\make_make_zips.py

zipwin: make_zips py2exe
	bin\\make_win_zip.bat

zipsrc: make_zips
	bin\\make_src_zip.bat

zips: zipsrc zipwin


.PHONY: clean tags stats profile py2exe alltests make_zips win_zip src_zip zips

