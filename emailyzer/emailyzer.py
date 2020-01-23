#!/usr/bin/env python
# -*- coding: utf-8 -*-

from emailyzer.classes.email import Email


def from_msg(filepath):
    return Email.from_msg(filepath)


def from_eml(filepath):
    return Email.from_eml(filepath)


def from_file(filepath):
    if 'msg' in filepath:
        return from_msg(filepath)
    elif 'eml' in filepath:
        return from_eml(filepath)
    else:
        return None


"""
fp = 'tests/emails/lastpass-phishing.'
e = from_eml(fp + 'eml)
eml = e.create_email()
m = from_msg(fp + 'msg')
msg = m.create_email()
"""
