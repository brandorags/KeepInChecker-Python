import smtplib
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class EmailUtilities(object):
    """
    A utility class for sending emails.
    """

    def __init__(self, sender, recipient, subject, body, attachment):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.attachment = attachment

    def is_sending_with_attachment(self):
        if self.attachment is not None:
            return True
        else:
            return False


    def send_email(self):
        msg = MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = self.recipient
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.body, 'plain'))

        if self.is_sending_with_attachment():
            filename = None
