#!/usr/bin/env python
# -*- coding: utf-8 -*-

from emailyzer.classes.email import Email
from emailyzer.helpers.logger import rootLogger as logger

def from_msg(filepath):
    try:
        return Email.from_msg(filepath)
    except Exception as e:
        logger.error(e)
        return Email.from_msg(filepath)


def from_eml(filepath):
    try:
        return Email.from_eml(filepath)
    except Exception as e:
        logger.error(e)
        return Email.from_eml(filepath)


def from_file(filepath):
    try:
        return from_msg(filepath)
    except Exception as e:
        logger.error(e)
        pass
    try:
        return from_eml(filepath)
    except Exception as e:
        logger.error(e)
