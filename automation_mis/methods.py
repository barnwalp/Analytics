import pandas as pd
from exchangelib import Account, Message, Credentials, HTMLBody
from exchangelib import Configuration, DELEGATE, FileAttachment
import os


def create_html(df, vendor):
    df = df[df['Dependency'] == vendor]
    df = df.drop(columns=[
        'S No',
        'RO Code',
        'Mode of Transfer'
        ])
    html_table = df.to_html()
    html_content = """
    <html><body><h5>Pl find the list of issues due to which real time data transfer
    is not happenning. You are requesetd to resolve these issues on priority</h5>
    """
    html_content += html_table
    html_content += """
    <p>
    <br>
    With Regards<br>
    Pankaj Barnwal<br>
    </p>
    </body>
    </html>
    """
    return html_content


def send_mail(html_content, cc_list, vendor):
    outlook_user = os.environ.get('OUTLOOK_USER')
    outlook_password = os.environ.get('OUTLOOK_PASS')
    outlook_server = os.environ.get('OUTLOOK_SERVER')
    outlook_email = os.environ.get('OUTLOOK_EMAIL')
    credentials = Credentials(
            username=outlook_user,
            password=outlook_password)
    config = Configuration(
            server=outlook_server,
            credentials=credentials)
    account = Account(
            primary_smtp_address=outlook_email,
            config=config,
            autodiscover=False,
            access_type=DELEGATE)
    msg = Message(
            account=account,
            subject=f'Data Transfer - {vendor} depenency - Sambalpur DO',
            body=HTMLBody(html_content),
            to_recipients=['barnwalp@indianoil.in'],
            #cc_recipients=cc_list)
            )
    msg.send_and_save()