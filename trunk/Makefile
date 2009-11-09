
# These make targets aren't really critical, they are more of a cheatsheet to
# remind me of a few commonly-used commands.

# I run these commands on Windows, but they require Cygwin. They might work ok
# from a standard Cygwin bash prompt, but just to be difficult, I run them from
# a Windows Cmd prompt, with C:\Cygwin\usr\bin at the start of my path (ie.
# before C:\Windows;C:\Windows\System32, etc, to make sure I pick up the
# Cygwin version of 'find.exe', 'sort.exe', etc, rather than the crappy DOS
# ones.)

clean:
	rm -rf build dist tags
	-find gamelib bin -name '*.py[oc]' -exec rm {} \;

tags:
	ctags -R gamelib

stats:
	find gamelib -name '*.py' | grep -v '/tests/' | xargs wc -l -c | sort
	find gamelib -name '*.py' | grep '/tests/' | xargs wc -l -c | sort

.PHONY: clean tags stats

