#!/usr/bin/env python3
from email.parser import BytesParser
from email.policy import default


class Eml:
    def __init__(self, filepath):
        self.message = self.__parse(filepath)
        self.subject = self.__get_subject()
        self.html = self.__get_html()
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
        with open(filepath, 'rb') as f:
            return BytesParser(policy=default).parse(f)

    def __get_subject(self):
        return self.message.get('Subject')

    def __get_html(self):
        try:
            return self.message.get_body(preferencelist=('html')).get_content()
        except AttributeError:
            body = self.message.get_body().get_content()
            if body.startswith('    Date: '):
                try:
                    body = body.split('|', 1)[1]
                except ValueError:
                    body = body.split('>', 1)[1]

            return body

    def __get_text(self):
        try:
            return self.message.get_body(preferencelist=('plain')).get_content()
        except Exception:
            return ''

    def __get_attachments(self):
        attachments = []
        for attachment in self.message.iter_attachments():
            attachments.append({
                'filename': attachment.get_filename(),
                'filetype': attachment.get_content_subtype(),
                'encoding': attachment.get('Content-Transfer-Encoding'),
                'content': attachment.get_content(),
                'disposition': attachment.get_content_disposition()
            })
        return attachments

    def __get_headers(self):
        headers = {}
        for k in self.message.keys():
            if k in headers:
                headers[k] = self.message.get_all(k)
            else:
                headers[k] = self.message.get(k)
        return headers

    def __get_sender(self):
        return self.message.get('From')

    def __get_date(self):
        return self.message.get('Date')

    def __get_content_type(self):
        return self.message.get_content_type()

    def __get_dkim_domain(self):
        dkim_sig = self.message.get('DKIM-Signature')
        if dkim_sig:
            start = dkim_sig.split('d=')[1]
            end = start.find(';')
            dkim_domain = start[0:end]
            return dkim_domain
        return None

    def __get_envelope_domain(self):
        if self.headers and self.headers.get('Received'):
            for h in self.headers.get('Received'):
                if 'envelope-from' in h:
                    s = h.split('envelope-from')[1]
                    try:
                        e = s.index('>)')
                    except ValueError:
                        e = s.index(')')
                    except Exception:
                        e = None
                    if s and e:
                        at = s.index('@')
                        efd = s[at + 1:e]
                        return efd
                    else:
                        return None
        else:
            return None
