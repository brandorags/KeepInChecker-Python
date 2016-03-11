import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from database import queries, entities
from datetime import datetime


date_last_email_was_sent = datetime.now()
has_email_been_sent = True


def send_email(sender_name, sender_email, sender_password, recipient):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = 'KeepInChecker User Activity Report for ' + sender_name
    msg.attach(MIMEText(generate_body_text(sender_name), 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, recipient, text)
    server.quit()


def generate_body_text(sender_name):
    email_body = 'Hello,\n\nOn behalf of ' + sender_name + ', you have received this email' \
                                                           ' with the following data,\n\n'

    packets = get_packet_data_for_email()
    if packets:
        packet_data = ''
        for packet in packets:
            if isinstance(packet, entities.Packets):
                packet_data += '\n' + packet.get_DateReceived() + ' ' + packet.get_Timezone() + ' ' + \
                              packet.get_Get() + ' ' + packet.get_Host() + ' ' + packet.get_Referer()

        email_body += str(len(packets)) + ' questionable sites were visited:\n'
        email_body += packet_data
    else:
        email_body += '0 questionable sites were visited.'

    email_body += '\n\nKeep staying accountable!\n\nSincerely,\nKeepInChecker'

    return email_body


def get_packet_data_for_email():
    return queries.get_packets()
