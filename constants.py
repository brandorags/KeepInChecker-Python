objectionable_words_list = ['stackoverflow']


def generate_body_text(internet_traffic_output):
    email_body = 'Hello,\n\nYou have received this email with the following data,\n'

    for value in internet_traffic_output:
        email_body += '\n' + value

    email_body += '\n\nKeep staying accountable!\n\nSincerely,\nKeepInChecker'

    return email_body
