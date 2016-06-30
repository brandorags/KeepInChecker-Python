import smtplib

from email.mime.multipart import MIMEMultipart
from security_utilities import decrypt
from email.mime.text import MIMEText
from database import queries
from datetime import datetime


# keeps track of the date in which the
# last email was sent
date_last_email_was_sent = datetime.now()

# a boolean that's used to determine
# within a loop if an email has been sent
has_email_been_sent = True


def send_email(sender_name, sender_email, sender_password, recipients):
    """
    Sends the activity report to the user's
    accountability partners.

    :param sender_name: the name of the user (e.g., "John Doe")
    :param sender_email: the user's email address
    :param sender_password: the user's email address password
    :param recipients: the user's accountability partners' email addresses
    :return:
    """
    message = MIMEMultipart()
    message['From'] = sender_email
    message['Subject'] = 'KeepInChecker User Activity Report for ' + sender_name
    message.attach(MIMEText(generate_body_text(sender_name), 'plain'))

    recipients_list = [recipient.strip(' ') for recipient in recipients.split(',')]
    mail_server = get_mail_server(sender_email)
    port = get_port(mail_server)

    server = smtplib.SMTP(mail_server, port)
    server.starttls()
    server.login(sender_email, sender_password)
    text = message.as_string()
    server.sendmail(sender_email, recipients_list, text)
    server.quit()


def generate_body_text(sender_name):
    """
    Creates the body of the activity
    report. This will display all
    objectionable content found.

    :param sender_name: the name of the user (e.g., "John Doe")
    :return:
    """
    email_body = 'Hello,\n\nOn behalf of ' + sender_name + ', you have received this email' \
                                                           ' with the following data,\n\n'

    packets = get_packet_data_for_email()
    if packets:
        packet_data = ''
        for packet in packets:
            packet_data += '\n' + decrypt(packet['DateReceived']) + ' ' + packet['Timezone'] + ' ' + \
                           decrypt(packet['Get']) + ' ' + decrypt(packet['Host']) + ' ' + decrypt(packet['Referer'])

        email_body += str(len(packets)) + ' questionable sites were visited:\n'
        email_body += packet_data
    else:
        email_body += '0 questionable sites were visited.'

    email_body += '\n\nKeep staying accountable!\n\nSincerely,\nKeepInChecker'

    return email_body


def get_packet_data_for_email():
    """
    Calls the query that retrieves
    all the packets in the database.

    :return: a list of all the
    packet objects from the database
    """
    return queries.get_packets()


def get_mail_server(sender_email):
    """
    Gets the URL of the mail server
    given an email address.

    :param sender_email: the email address
    of the sender
    :return: a URL associated with the
    sender's email address domain (e.g.
    example@gmail.com would return
    'smtp.gmail.com'); an empty string
    if the domain is unknown
    """
    google_domains = ['gmail', 'googlemail']
    yahoo_domains = ['yahoo', 'ymail']
    microsoft_domains = ['live', 'msn', 'hotmail', 'outlook', 'passport']
    aol_domains = ['aol', 'aim']
    comcast_domains = ['comcast']
    verizon_domains = ['verizon']
    att_domains = ['att']

    sender_email = sender_email.lower()

    if any(domain in sender_email for domain in google_domains):
        return 'smtp.gmail.com'
    elif any(domain in sender_email for domain in yahoo_domains):
        return 'smtp.mail.yahoo.com'
    elif any(domain in sender_email for domain in microsoft_domains):
        return 'smtp-mail.outlook.com'
    elif any(domain in sender_email for domain in aol_domains):
        return 'smtp.aol.com'
    elif any(domain in sender_email for domain in comcast_domains):
        return 'smtp.comcast.net'
    elif any(domain in sender_email for domain in verizon_domains):
        return 'smtp.verizon.net'
    elif any(domain in sender_email for domain in att_domains):
        return 'smtp.att.net'

    return ''


def get_port(mail_server):
    """
    Gets the port number of a given
    email server.

    :param mail_server: the URL of the
    mail server
    :return: a number that corresponds
    to the mail server (e.g. 'smtp.gmail.com'
    would return the number 587); 0 if the
    mail server is unknown
    """
    five_eighty_seven_port_domains = ['smtp.gmail.com', 'smtp.mail.yahoo.com', 'smtp-mail.outlook.com',
                                      'smtp.aol.com', 'smtp.comcast.net']
    four_sixty_five_port_domains = ['smtp.verizon.net', 'smtp.att.net']

    if any(domain in mail_server for domain in five_eighty_seven_port_domains):
        return 587
    elif any(domain in mail_server for domain in four_sixty_five_port_domains):
        return 465

    return 0
