#!/usr/bin/env python3
import base64

from mailparser import parse_from_file_msg
from extract_msg import Message as ExtractMsg


class Msg:
    def __init__(self, filepath):
        self.message = self.__parse(filepath)
        self.__msg = ExtractMsg(filepath)
        self.subject = self.__get_subject()
        self.html = self.__get_html()
        self.html_to_text = self.__clean_html()
        self.text = self.__get_text()
        self.attachments = self.__get_attachments()
        self.headers = self.__get_headers()
        self.sender = self.__get_sender()
        self.date = self.__get_date()
        self.content_type = self.__get_content_type()
        self.dkim_domain = self.__get_dkim_domain()
        self.envelope_domain = self.__get_envelope_domain()
        self.filepath = filepath

    def __parse(self, filepath):
        return parse_from_file_msg(filepath)

    def __get_subject(self):
        return self.message.subject

    def __get_html(self):
        html = self.message.body.split('--- mail_boundary ---')[1]
        return html

    def __clean_html(self):
        return self.__msg.body

    def __get_text(self):
        txt = self.message.body.split('--- mail_boundary ---')[0]
        return txt

    def __get_attachments(self):
        attachments = []
        for attachment in self.message.attachments:
            enc = attachment.get('content_transfer_encoding')
            content = attachment.get('payload').replace('\n', '')
            if enc == 'base64':
                content = base64.b64decode(content)
            attachments.append({
                'filename': attachment.get('filename'),
                'filetype': attachment.get('mail_content_type'),
                'encoding': enc,
                'content': content,
                'disposition': None
            })
        return attachments

    def __get_headers(self):
        h = self.message.headers
        h['Received'] = [r.replace('\n', '')
                         for r in self.message.received_raw]
        return h

    def __get_sender(self):
        return self.message.headers.get('From')

    def __get_date(self):
        return self.message.headers.get('Date')

    def __get_content_type(self):
        ct = self.message.headers.get('Content-Type')
        return ct.split(';')[0]

    def __get_dkim_domain(self):
        dkim_sig = self.headers.get('DKIM-Signature')
        if dkim_sig:
            start = dkim_sig.split('d=')[1]
            end = start.find(';')
            dkim_domain = start[0:end]
            return dkim_domain
        return None

    def __get_envelope_domain(self):
        recv = self.headers.get('Received')
        if recv:
            for h in recv:
                if 'envelope-from' in h:
                    s = h.split('envelope-from')[1]
                    e = s.index('>)')
                    at = s.index('@')
                    efd = s[at + 1:e]
                    return efd
        else:
            return None
