import pandas as pd
from exchangelib import Account, Message, Credentials, HTMLBody
from exchangelib import Configuration, DELEGATE, FileAttachment
import os

def create_pivot(df, day_1, day_2):
    df = df.drop(columns=[
        'RO Market Type',
        'SO',
        'SO Code',
        'DO', 'DO Code',
        'SA Code',
        'Phase',
        'SAT Status',
        'VSAT Installation',
        'Control Record Reconcilation',
        'Unnamed: 15',
        'Transaction Stock Reconcilation',
        'Unnamed: 17',
        'Totalizer Sales',
        'Unnamed: 21',
        'Total Transaction Sales',
        'Total Totalizer Sales',
        'Average Issue Sales',
        'Average Totalizer Sales',
        'Percentage Difference',
        'RO Eligible'
        ])

    # Deleting 1st row; indexing start from 0
    df = df.drop(df.index[1])

    df = df.rename(columns={
        'Issue Sales': day_1,
        'Unnamed: 19': day_2
        })

    # filter out Proudct column
    df = df[
            (df['Product'] == 'XP') |
            (df['Product'] == 'MS') |
            (df['Product'] == 'HS')
            ]

    # Replace XP with MS in Product column
    df.loc[df['Product'] == 'XP', 'Product'] = 'MS'

    pvt_table = pd.pivot_table(
            df,
            index=["SA"],
            columns=["Product"],
            values=[day_1, day_2],
            aggfunc=sum)

    return pvt_table

def send_mail(html_table, first_file):
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
            subject="Nozzle Sales Report - Sambalpur DO",
            body=HTMLBody(html_table),
            to_recipients=['barnwalp@indianoil.in'],
            cc_recipients=['barnwalp@indianoil.in'])

    # attaching a file in the msg
    with open(first_file, 'rb') as f:
        my_file = FileAttachment(name='nozzle_sale_1.xlsx', content=f.read())
    msg.attach(my_file)

    msg.send_and_save()
