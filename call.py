import os
from twilio.rest import Client
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)
call = client.calls.create(
    twiml = '<Response><Say>Testing Testing</Say></Response>',
    to = '+9779860983610',
    from_ = '+37282721114'
)
print(call.sid)   #a unique identifier or a referenced ID generated automatically