import html.parser
import re

from bs4 import BeautifulSoup as bs

import emailyzer.helpers.regex as REGEX


def clean(raw_html):
    no_tags = clean_html(raw_html)
    no_dirt = clean_dirt(no_tags)
    no_nl = clean_nl(no_dirt)
    no_rtf_tags = clean_rtf(no_nl)
    clean = clean_non_alphanum(no_nl)
    return clean.strip()


def clean_rtf(text):
    cleaned = re.sub(REGEX.HTML_RTF_REGEX, ' ', text, 0, re.MULTILINE)
    return cleaned


def clean_nl(text):
    cleaned = re.sub(REGEX.MULTI_BLANK_REGEX, '\\n', text, 0, re.MULTILINE)
    if cleaned.startswith('\n'):
        cleaned = cleaned.replace('\n', '', 1)
    if cleaned.endswith('\n'):
        cleaned = cleaned[0:len(cleaned) - 2]
    return cleaned


def clean_dirt(text):
    dirt = ['&nbsp;', 'nbsp;']
    for d in dirt:
        text = text.replace(d, ' ')
    return text


def clean_html(raw_html):
    raw_html = re.sub(REGEX.HTML_SCRIPT_REGEX, ' ', raw_html, 0, re.MULTILINE)
    no_html = bs(raw_html, 'lxml').text
    h = html.parser.HTMLParser()
    return h.unescape(no_html)


def clean_non_alphanum(text):
    pattern = re.compile(REGEX.NON_ALPHANUM_REGEX)
    return pattern.sub(' ', text)
