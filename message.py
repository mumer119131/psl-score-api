from twilio.rest import Client


def send_msg(data):
    account_sid = 'AC346c543b7882650a028201a7ba76db0b'
    auth_token = 'c7c78dec371a0d8118e94af522884fc5'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=data,
        to='whatsapp:+923456013122'
    )
