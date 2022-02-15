from twilio.rest import Client


def send_msg(data):
    account_sid = '[sid]'
    auth_token = '[key]'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=data,
        to='whatsapp:[ph# no]'
    )
