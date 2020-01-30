#!/usr/bin/env python
# -*- coding: utf-8 -*-

from emailyzer.classes.email import Email


def from_msg(filepath):
    return Email.from_msg(filepath)


def from_eml(filepath):
    return Email.from_eml(filepath)


def from_file(filepath):
    try:
        return from_msg(filepath)
    except Exception as e:
        pass
    try:
        return from_eml(filepath)
    except Exception as e:
        pass
