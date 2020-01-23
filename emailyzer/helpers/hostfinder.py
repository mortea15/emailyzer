#!/usr/bin/env python3
import html.parser
import re
from urllib.parse import urlparse

import emailyzer.helpers.regex as REGEX


def get_ips(email):
    regex = REGEX.IP_REGEX
    html_matches = re.findall(regex, email.html, re.MULTILINE)
    text_matches = re.findall(regex, email.text, re.MULTILINE)
    subject_matches = re.findall(regex, email.subject, re.MULTILINE)
    header_matches = []
    for hdr in email.headers.values():
        if isinstance(hdr, list):
            ms = []
            for h in hdr:
                ms = ms + re.findall(regex, h, re.MULTILINE)
            header_matches = header_matches + ms
        else:
            header_matches = header_matches + \
                re.findall(regex, hdr, re.MULTILINE)

    # Merge, remove duplicates, return list of IPs
    return list(set(
        html_matches + text_matches +
        subject_matches + header_matches
    ))


def get_urls(email):
    regex = REGEX.URL_REGEX
    html_matches = re.findall(regex, email.html, re.MULTILINE)
    html_matches = [html_entity_converter(v) for v in html_matches]
    text_matches = re.findall(regex, email.text, re.MULTILINE)
    subject_matches = re.findall(regex, email.subject, re.MULTILINE)
    header_matches = []
    for hdr in email.headers.values():
        if isinstance(hdr, list):
            ms = []
            for h in hdr:
                ms = ms + re.findall(regex, h, re.MULTILINE)
            header_matches = header_matches + ms
        else:
            header_matches = header_matches + \
                re.findall(regex, hdr, re.MULTILINE)

    # Merge, remove duplicates, return list of IPs
    return list(set(
        html_matches + text_matches +
        subject_matches + header_matches
    ))


def html_entity_converter(text):
    h = html.parser.HTMLParser()
    return h.unescape(text)


def find_hosts(email):
    ips = get_ips(email)
    urls = get_urls(email)
    domains = [get_domain(url) for url in urls]
    sender = [email.sender_address.split('@')[1]]

    return list(filter(None, list(set(ips + urls + domains + sender))))


def get_domain(url):
    if 'http://' or 'https://' in url:
        return urlparse(url).netloc
    else:
        return url
