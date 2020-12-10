from twilio.rest import Client
import os

def send_whatsapp(message, contact):
    token = os.getenv('twilio_auth_token')
    sid = os.getenv('twilio_account_sid')
    client = Client(sid, token)

    to_number = f'whatsapp:+91{contact}'
    message = client.messages.create(
            from_ = 'whatsapp:+14155238886',
            body=message,
            to = to_number
            )
    return message.sid


