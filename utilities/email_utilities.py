import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from database import queries, entities


def send_email(sender, sender_password, recipient, subject):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(generate_body_text(None), 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, sender_password)
    text = msg.as_string()
    server.sendmail(sender, recipient, text)
    server.quit()


def generate_body_text(internet_traffic_output):
    email_body = 'Hello,\n\nYou have received this email with the following data,\n'

    packets = get_packet_data_for_email()
    for packet in packets:
        if isinstance(packet, entities.Packets):
            email_body += '\n' + packet.get_DateReceived() + ' ' + packet.get_Timezone() + ' ' + \
                          packet.get_Get() + ' ' + packet.get_Host() + ' ' + packet.get_Referer()
    # for value in internet_traffic_output:
    #     email_body += '\n' + value

    email_body += '\n\nKeep staying accountable!\n\nSincerely,\nKeepInChecker'

    return email_body


def get_packet_data_for_email():
    return queries.get_packets()
