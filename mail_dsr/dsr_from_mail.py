import imaplib
import email
import os
import re


# Hotmail configuration using imap protocol
def connect():
    host = 'imap.outlook.com'
    username = os.environ.get('hotmail_email')
    password = os.environ.get('hotmail_password')

    # connecting to mail server
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    return mail


def filter_sender(mail, sender):
    mail.select('inbox')
    # all uid will be returned as byte string, result = OK
    # and data = [b'5 20 21 25 27 29 31 33 35 37]
    result, data = mail.uid('search', None, 'ALL')

    # convert strings to a list
    inbox_item_list = data[0].split()
    for value in inbox_item_list:
        # fetching the email data in bytes
        result2, email_data = mail.uid('fetch', value, '(RFC822)')
        # converting byte email to raw_email data
        raw_email = email_data[0][1].decode('utf-8', errors='ignore')
        # converting raw_email string to email message
        email_message = email.message_from_string(raw_email)
        # print(f'Email Sender: {email_message["From"]}')
        if email_message["From"] == sender:
            print(f'Email subject: {email_message["Subject"]}')
            print(f'Email content: {get_body(email_message)}')


def get_body(msg):
    # Checking if mail have attachements as well
    if msg.is_multipart():
        # multipart email body is returned as a list
        # getting the first element of the returned list
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)


def get_dsr(mail, sender):
    mail.select('inbox')
    # all uid will be returned as byte string, result = OK
    # and data = [b'5 20 21 25 27 29 31 33 35 37]
    result, data = mail.uid('search', None, 'ALL')

    # convert strings to a list
    inbox_item_list = data[0].split()
    for value in inbox_item_list:
        # fetching the email data in bytes
        result2, email_data = mail.uid('fetch', value, '(RFC822)')
        # converting byte email to raw_email data
        raw_email = email_data[0][1].decode('utf-8', errors='ignore')
        # converting raw_email string to email message
        email_message = email.message_from_string(raw_email)
        if email_message["Subject"].lower().__contains__("dsr"):
            # print(get_body(email_message).decode('utf-8'))
            data = get_body(email_message).decode('utf-8')
            # with open('body.txt', 'w') as f:
            #     f.write(get_body(email_message).decode('utf-8'))
    ms_dsr = literal_search(data)
    return ms_dsr


def literal_search(data):
    ms_hsd_list = [
        'ms_dip',
        'ms_water_dip',
        'ms_opening_stock',
        'ms_receipt',
        'ms_total_stock',
        'ms_totalizer_1',
        'ms_totalizer_2',
        'ms_testing',
        'ms_sales',
        'ms_cumulative_sales',
        'hsd_dip',
        'hsd_water_dip',
        'hsd_opening_stock',
        'hsd_receipt',
        'hsd_total_stock',
        'hsd_totalizer_1',
        'hsd_totalizer_2',
        'hsd_testing',
        'hsd_sales',
        'hsd_cumulative_sales'
    ]

    pattern_1 = re.compile(r'\s\d+\s')
    m = pattern_1.findall(data)
    val_list = []
    pattern_2 = re.compile(r'\d+')
    for val in m:
        val_list.append(int(pattern_2.search(val).group()))

    # Creating ms dictionary using 2 list
    dsr = {ms_hsd_list[i]: val_list[i] for i in range(len(ms_hsd_list))}
    return dsr


sender = 'Sardar Khan <vyapar123@outlook.com>'
# filter_sender(connect(), sender)
print(get_dsr(connect(), sender))
