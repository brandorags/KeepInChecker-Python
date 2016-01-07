import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Emailer(object):

    def __init__(self, sender, recipient, sender_password, subject, body):
        self.sender = sender
        self.recipient = recipient
        self.sender_password = sender_password
        self.subject = subject
        self.body = body

    def send_email(self):
        msg = MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = self.recipient
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.sender, self.sender_password)
        text = msg.as_string()
        server.sendmail(self.sender, self.recipient, text)
        server.quit()
