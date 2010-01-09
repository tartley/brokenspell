
# These make targets aren't really critical, they are more of a cheatsheet to
# remind me of a few commonly-used commands.

# I run these under bash, or on Windows under Cygwin

NAME := SinisterDucks
VERSION := `python -O SinisterDucks.py --version`
PACKAGE := sinisterducks

clean:
	rm -rf build dist tags
	-find ${PACKAGE} bin -name '*.py[oc]' -exec rm {} \;

tags:
	ctags -R ${PACKAGE}

stats:
	find ${PACKAGE} -name '*.py' | grep -v '/tests/' | xargs wc -l | sort -g
	find ${PACKAGE} -name '*.py' | grep '/tests/' | xargs wc -l | sort -g

profile:
	python -O -m cProfile -o profile.out Sinister-Ducks.py
	runsnake profile.out

alltests:
	nosetests ${PACKAGE}


py2exe:
	rm -rf dist/${NAME}
	python setup.py --quiet py2exe

templates:
	python bin/template.py
	chmod 755 bin/*.sh

zipwin: templates py2exe
	bin/make_win_zip.bat

zipsrc: templates
	bin/make_src_zip.sh

zips: zipsrc zipwin

uploadwin:
	googlecode_upload.py \
        --project=brokenspell \
        --summary='MS Windows executable' \
        --user=tartley \
        --password=`cat ~/.googlecodepw` \
        --labels=Featured,Type-Executable,OpSys-Windows \
        dist\\${NAME}-${VERSION}-mswin.zip


.PHONY: clean tags stats profile alltests py2exe make_zips zipsrc zipwin zips uploadwin

