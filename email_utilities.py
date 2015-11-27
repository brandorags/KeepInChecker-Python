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
            file = open(self.attachment, 'rb')
            filename = file.split('/')[len(file) - 1]

            part = MIMEBase('application', 'octet-stream')
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content Disposition', 'attachment; filename= ' + filename)

            msg.attach(part)

        # TODO: since this is a utility class, I'll need to make this more rrrrrrrobust later
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.sender, 'hmmmdoIputmypasswordhere?')
        text = msg.as_string()
        server.sendmail(self.sender, self.recipient, text)
        server.quit()
