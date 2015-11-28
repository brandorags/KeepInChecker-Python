import datetime
import smtplib
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


class Emailer(object):

    def __init__(self, sender, recipient, sender_password, subject, body, attachment):
        self.sender = sender
        self.recipient = recipient
        self.sender_password = sender_password
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
            screenshot_data = open(self.attachment, 'rb').read()
            screenshot = MIMEImage(screenshot_data, name=os.path.basename(self.attachment))
            msg.attach(screenshot)

        # TODO: since this is a utility class, I'll need to make this more rrrrrrrobust later
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.sender, self.sender_password)
        text = msg.as_string()
        server.sendmail(self.sender, self.recipient, text)
        server.quit()


def get_body_text():
    # date = command_line_utilities.convert_output_to_string(subprocess.Popen('date', stdout=subprocess.PIPE))
    # date = '-'.join(date.split(' '))
    date = datetime.datetime.now()
    body = 'Hello,\n\nYou have received this email with the following screenshot, which was taken at ' + str(date) + '.'
    return body
