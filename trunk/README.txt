Sinister Ducks
==============

A small game, with quacking.
http://code.google.com/p/brokenspell/
http://www.pyweek.org/e/BrokenSpell/


On Windows:

    Download the windows executable version, and double-click
    'SinisterDucks.exe'.


On Mac or Linux:

    Install each of the dependancies listed below.

    Download the Sinister Ducks source tarfile, untar it.
    Then from a terminal, cd to the game directory and type:

        python -O SinisterDucks.py

    A configuration file, config.ini, can be used to affect the game,
    particularly useful to work around problems with sound. See comments
    within that file.


Dependencies

      Python 2.6:   May work with 2.7, but will not work with 3.x.
                    http://python.org/download/releases/2.6.2/
      pyglet 1.1.4: http://pyglet.org/download.html
      AVBin:        This is included with pyglet Windows (.msi) and Mac (.dmg)
                    binary installers, but if you installed pyglet from source
                    (.tar.gz or .zip, or easy_install) then you'll need to get
                    AVBin separately from here:
                    http://code.google.com/p/avbin/downloads/list


How to play the game

    Z to flap. Left and Right to steer.

    Attack the sinister ducks by colliding with them. Whichever bird is highest
    will win the fight - the loser will shed a feather and plummet from the
    sky.

    Collecting feathers boosts your multiplier.
    More points are awarded for consecutively hitting other birds without
    collecting any feathers.

    Use M to toggle the music.

    Press Esc to exit.


Credits

    Entry in PyWeek #9  <http://www.pyweek.org/9/>
    Team: Broken Spell
    Members:
        Christian Muirhead, xtian
        Glenn Jones, millenniumhand
        Jonathan Hartley, tartley
        Menno Smits, mjs0

    Thanks to Chris De Leon for selfless advice and mentorship
    during the post-competition bugfix and polish phase.


Intellectual monopolies

    This whole work is published under the Creative Commons: Attribution -
    Noncommercial - Share Alike license, as detailed here:
    http://creativecommons.org/licenses/by-nc-sa/3.0/
    With the exception of the components listed below, which are licensed
    as specified by their respective owners.

    This program uses and redistributes Python, under the terms of its open
    source license: http://www.python.org/psf/license/

    This program requires and redistributes the library pyglet, which is
    licensed under the new BSD open source license, details of which are here:
    http://www.opensource.org/licenses/bsd-license.php

    The music is 'We Are All On Drugs', a cover of a Weezer track, performed by
    Rabato, published on 'Weezer - The 8-bit album':
        http://www.ptesquad.com/more/pte018.html
    This is licensed under the terms of the Creative Commons: Attribution -
    Noncommercial - No derivative works license:
        http://creativecommons.org/licenses/by-nc-nd/3.0/

    This game was originally based upon PyWeek Skellington code, licenced under
    the new BSD: http://www.opensource.org/licenses/bsd-license.php

