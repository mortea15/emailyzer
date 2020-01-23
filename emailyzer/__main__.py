#!/usr/bin/env python
# -*- coding: utf-8 -*-
import getopt
import os
import sys

import emailyzer

current = os.path.realpath(os.path.dirname(__file__))


INDENT = '  '
HELPMSG = f'''usage: emailyzer [-h] (-e .EML FILE | m .MSG FILE | -f FILE) [-b] [-a] [-r] [-t] [-dt] [-m] [-u] [-c] [-sa] [-v]

    {INDENT * 1}-h, --help      {INDENT * 2}Show this message
    {INDENT * 1}-e, --eml       {INDENT * 2}Parse a .eml file
    {INDENT * 1}-m, --msg       {INDENT * 2}Parse a .msg file
    {INDENT * 1}-v, --verbose   {INDENT * 2}Increase verbosity (can be used several times, e.g. -vv)
'''


def main():
    VERBOSITY = 0
    if len(sys.argv) < 2:
        print(HELPMSG)
        sys.exit(2)
    
    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, 'hve:m:a', ['help', 'verbose', 'eml=', 'msg=', 'all'])
    except getopt.GetoptError:
        print(HELPMSG)
        sys.exit(2)

    if not opts:
        print(HELPMSG)
        sys.exit(0)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(HELPMSG)
            sys.exit(0)
        elif opt in ('-v', '--verbose'):
            VERBOSITY += 1
        elif opt in ('-e', '--eml'):
            eml_path = arg
            print(msg_path)
        elif opt in ('-m', '--msg'):
            msg_path = arg
            print(msg_path)
        elif opt in ('-a', '--all'):
            print('All it is!')


if __name__ == '__main__':
    main()