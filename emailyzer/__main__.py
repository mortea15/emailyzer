#!/usr/bin/env python
# -*- coding: utf-8 -*-
import getopt
import os
import sys

import emailyzer
from emailyzer.helpers.utils import (print_attachments, print_body, print_from,
                                     print_headers, print_html, print_subject,
                                     print_to, save_attachments)

current = os.path.realpath(os.path.dirname(__file__))


INDENT = '  '
HELPMSG = f'''usage: emailyzer [-h] (-e .EML FILE | -m .MSG FILE | -f FILE) [-b] [-a] [-r] [-t] [-o] [-u] [-sa] [-v]

    {INDENT * 1}--help                  {INDENT * 2}Print this message
    {INDENT * 1}-e, --eml               {INDENT * 2}Parse a .eml file
    {INDENT * 1}-m, --msg               {INDENT * 2}Parse a .msg file
    {INDENT * 1}-f, --file              {INDENT * 2}Parse a file (must be either .msg or .eml format)
    {INDENT * 1}-b, --body              {INDENT * 2}Print the body of the email
    {INDENT * 1}-a, --attachments       {INDENT * 2}Print the attachments of the email
    {INDENT * 1}-r, --headers           {INDENT * 2}Print the headers of the email
    {INDENT * 1}-t, --to                {INDENT * 2}Print the to of the email
    {INDENT * 1}-o, --from              {INDENT * 2}Print the from of the email
    {INDENT * 1}-u, --subject           {INDENT * 2}Print the subject of the email
    {INDENT * 1}-sa, --save-attachments {INDENT * 2}Save the attachments to disk
    {INDENT * 1}-v, --verbose           {INDENT * 2}Increase verbosity (can be used several times, e.g. -vv)
'''


def main():
    VERBOSITY = 0
    EMAIL = None
    if len(sys.argv) < 2:
        print(HELPMSG)
        print(f'emailyzer: error: no file specified')
        sys.exit(2)
    
    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, 'e:m:f:bhartousav', ['help', 'verbose', 'eml=', 'msg=', 'file=', 'body', 'html', 'attachments', 'headers', 'to', 'from', 'subject', 'save-attachments'])
    except getopt.GetoptError:
        print(HELPMSG)
        sys.exit(2)

    if not opts:
        print(HELPMSG)
        sys.exit(0)

    for opt, arg in opts:
        if opt in ('--help'):
            print(HELPMSG)
            sys.exit(0)
        elif opt in ('-v', '--verbose'):
            VERBOSITY += 1
        elif opt in ('-e', '--eml'):
            eml_path = arg
            EMAIL = emailyzer.from_eml(eml_path)
        elif opt in ('-m', '--msg'):
            msg_path = arg
            EMAIL = emailyzer.from_msg(msg_path)
        elif opt in ('-f', '--file'):
            fpath = arg
            EMAIL = emailyzer.from_file(fpath)
        elif opt in ('-b', '--body'):
            print_body(EMAIL)
        elif opt in ('-h', '--html'):
            print_html(EMAIL)
        elif opt in ('-a', '--attachments'):
            print_attachments(EMAIL)
        elif opt in ('-r', '--headers'):
            print_headers(EMAIL)
        elif opt in ('-t', '--to'):
            print_to(EMAIL)
        elif opt in ('-o', '--from'):
            print_from(EMAIL)
        elif opt in ('-u', '--subject'):
            print_subject(EMAIL)
        elif opt in ('-sa', '--save-attachments'):
            fnames = save_attachments(EMAIL)
            print(f'{len(EMAIL.attachments)} attachments saved to disk!')
            print(', '.join(fnames))

if __name__ == '__main__':
    main()
