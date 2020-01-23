#!/usr/bin/env python3
from emailyzer.classes.eml import Eml
from emailyzer.classes.msg import Msg
from emailyzer.helpers.cleaner import clean
from emailyzer.helpers.hostfinder import find_hosts


class Email(object):
    """
    Email provides a common object that can be generated
    from .eml and .msg email file formats
    """
    def __init__(self, message=None):
        """
        Initialize a new object from the message object
        """
        self._message = message
        self.parse()

    @classmethod
    def from_eml(cls, fp):
        """
        Create an Email object from a .eml file

        Args:
            fp (str): path of the .eml file
        Returns:
            Instance of Email
        """
        e = Eml(fp)
        return cls(e)

    @classmethod
    def from_msg(cls, fp):
        """
        Create an Email object from a .msg file

        Args:
            fp (str): path of the .msg file
        Returns:
            Instance of Email
        """
        m = Msg(fp)
        return cls(m)

    def parse(self):
        self.__subject = self._message.subject
        self.__html = self._message.html
        self.__text = self._message.text
        self.__attachments = self._message.attachments
        self.__headers = self._message.headers
        self.__sender = self._message.sender
        self.__date = self._message.date
        self.__content_type = self._message.content_type
        self.__dkim_domain = self._message.dkim_domain
        self.__envelope_domain = self._message.envelope_domain
        self.__hosts = find_hosts(self)

    @property
    def subject(self):
        """
        Returns the subject of the email
        """
        return self.__subject

    @property
    def html(self):
        """
        Returns the text html parts of the email
        """
        return self.__html

    @property
    def text(self):
        """
        Returns the text plain parts of the email
        """
        return self.__text

    @property
    def attachments(self):
        """
        Returns a list of all attachments in the email
        """
        return self.__attachments

    @property
    def headers(self):
        """
        Returns a dict with all the headers in the email
        """
        return self.__headers

    @property
    def sender(self):
        """
        Returns the sender of the email as in the headers `From`
        """
        return self.__sender

    @property
    def sender_address(self):
        """
        Returns the sender address of the email as in the headers `From`
        """
        if '<' in self.__sender:
            return self.__sender.split('<')[1].strip('>')
        return self.__sender

    @property
    def sender_name(self):
        """
        Returns the sender name of the email as in the headers `From`
        """
        if '<' in self.__sender:
            name = self.__sender.split('<')[0]
            return name[0:len(name) - 1]
        return None

    @property
    def date(self):
        """
        Returns the date of the email
        """
        return self.__date

    @property
    def content_type(self):
        """
        Returns the content-type of the email
        """
        return self.__content_type

    @property
    def sender_domain(self):
        """
        Returns the sender address domain of the email as in the headers `From`
        """
        sender = self.sender_address
        return sender.split('@')[1]

    @property
    def envelope_domain(self):
        """
        Returns the envelope-from address domain of the email from the headers
        """
        return self.__envelope_domain

    @property
    def dkim_domain(self):
        """
        Returns the DKIM-Signature address domain of the email from the headers
        """
        return self.__dkim_domain

    @property
    def html_as_text(self):
        """
        Returns the text html parts of the email as plain text
        """
        return clean(self.__html)

    @property
    def hosts(self):
        """
        Returns a list of all IPs and domains in the email (from all parts)
        """
        return self.__hosts

    @property
    def message(self):
        """
        Returns the message (<Msg> or <Eml>) object that was created from the file
        """
        return self._message
