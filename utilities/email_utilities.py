import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(sender, sender_password, recipient, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, sender_password)
    text = msg.as_string()
    server.sendmail(sender, recipient, text)
    server.quit()


def generate_body_text(internet_traffic_output):
    email_body = 'Hello,\n\nYou have received this email with the following data,\n'

    for value in internet_traffic_output:
        email_body += '\n' + value

    email_body += '\n\nKeep staying accountable!\n\nSincerely,\nKeepInChecker'

    return email_body
