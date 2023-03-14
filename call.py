from twilio.rest import Client
client = Client('ACe77bd388a1877d74f43befd79a854a12', 'b6a00b9a51cd6b60861a73d5c9a0df37')
call = client.calls.create(
    twiml = '<Response><Say>Testing Testing</Say></Response>',
    to = '+9779860983610',
    from_ = '+37282721114'
)
print(call.sid)   #a unique identifier or a referenced ID generated automatically