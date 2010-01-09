
# These make targets aren't really critical, they are more of a cheatsheet to
# remind me of a few commonly-used commands.

# I run these under bash, or on Windows under Cygwin

clean:
	rm -rf build dist tags
	-find sinisterducks bin -name '*.py[oc]' -exec rm {} \;

tags:
	ctags -R sinisterducks

stats:
	find sinisterducks -name '*.py' | grep -v '/tests/' | xargs wc -l | sort -g
	find sinisterducks -name '*.py' | grep '/tests/' | xargs wc -l | sort -g

profile:
	python -O -m cProfile -o profile.out Sinister-Ducks.py
	runsnake profile.out

alltests:
	nosetests sinisterducks


py2exe:
	rm -rf dist/SinisterDucks
	python setup.py --quiet py2exe


make_zips:
	python bin/make_make_zips.py
	chmod 755 bin/*

zipwin: make_zips py2exe
	bin/make_win_zip.bat

zipsrc: make_zips
	bin/make_src_zip.sh

zips: zipsrc zipwin


.PHONY: clean tags stats profile alltests py2exe make_zips zipsrc zipwin zips

