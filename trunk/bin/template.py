#!/usr/bin/env python

from glob import glob
import re
import sys

import fixpath

from sinisterducks import NAME, VERSION


matches = dict(
    NAME = NAME.replace(' ', ''),
    VERSION = VERSION,
)

def create_regexes(matches):
    regexes = {}
    for match, replace in matches.iteritems():
        regex = re.compile('\$\{%s\}' % (match,))
        regexes[regex] = replace
    return regexes


def process(filename, regexes):
    print filename
    lines = []
    with open(filename, 'r') as fp:
        for line in fp:
            line = line.strip()
            for match, replacement in regexes.iteritems():
                line = match.sub(replacement, line)
            lines.append(line)

    outputname = filename[:-len('.template')]
    with open(outputname, 'wb') as fp:
        for line in lines:
            fp.write(line + '\n')


def main():
    regexes = create_regexes(matches)
    files = glob('bin/*.template')
    for file in files:
        process(file, regexes)


if __name__ == '__main__':
    sys.exit(main())

